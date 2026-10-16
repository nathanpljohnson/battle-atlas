"""Authoring kit for battle scenarios (v2).

A battle's scenario.py builds a Battle, adds sources, places, units, phases and arrows, then calls export().
Positions can be written the way historians describe them:
    (lat, lon)                    absolute
    "Prace"                       a named place or hill
    ("Prace", 135, 800)           800 m from Prace on bearing 135 (south-east)
    ("Prace", 135, 800, 90, 200)  then a further 200 m on bearing 90 (chained offsets)

v2 additions
    B.source(id, label, url=None, note=None, kind=None)      citable source; cite with cite=[ids] or inline "[id]" in text
    B.unit(..., cite=[ids], men={phase: n})                    strength over time (carried forward)
    unit.at(phase, pos, facing, form, men=None, via=[pos...], bend=0)  via = route waypoints; bend bows the line (+ convex toward facing, - concave), as a fraction of frontage
    B.phase(..., day=1, fog=0.0, cite=[ids], tactic=(name, body, tactic_id))
    B.crossing(name, pos)                                       bridges / fords / causeways for the river-crossing check
    B.overlay(id, label, file, kind="period", opacity=0.85)     georeferenced map drapes (see tools/georef.py --overlays)
    meta: era ("ancient" | "medieval" | "early-modern" | "napoleonic" | "industrial" | "modern"), war, wind (deg FROM)

export(strict=False) validates (errors always fail; physical sanity warnings fail only when strict or
BATTLEKIT_STRICT=1), writes battles/<id>/<id>.json (terrain embedded), validation.md and check.png.
"""
import base64, json, math, os, re, struct

FORMS = {"X", "C", "L", "F", "R"}
TYPES = {"inf", "gd", "cav", "lc", "art", "lt", "hi", "arc", "kn", "ele", "cha", "arm", "mech", "mg"}
ARROWS = {"move", "charge", "retreat", "fire"}
CONF = {None, "high", "medium", "low"}
ERAS = {"ancient", "medieval", "early-modern", "napoleonic", "industrial", "modern"}
# sustained speed between phases, km/h (generous upper bounds; charges are short)
SPEED = {"inf": 5, "gd": 5, "lt": 6, "hi": 4.5, "arc": 5, "mg": 5, "art": 4.5, "cav": 15, "lc": 18, "kn": 12,
         "ele": 6, "cha": 14, "arm": 30, "mech": 30}
CITE_RE = re.compile(r"\[([a-z0-9_]+)\]")


def mv(p, bearing, meters):
    lat, lon = p
    b = math.radians(bearing)
    return (lat + math.cos(b) * meters / 111200, lon + math.sin(b) * meters / (111200 * math.cos(math.radians(lat))))


def dist_m(a, b):
    kx = 111200 * math.cos(math.radians((a[0] + b[0]) / 2))
    return math.hypot((a[0] - b[0]) * 111200, (a[1] - b[1]) * kx)


def minutes(t, day=1):
    h, m = t.split(":")[:2]
    return (day - 1) * 1440 + int(h) * 60 + int(m)


def seg_intersect(p1, p2, q1, q2):
    """Intersection point of segments p1p2 and q1q2 in (lat, lon), or None."""
    (y1, x1), (y2, x2), (y3, x3), (y4, x4) = p1, p2, q1, q2
    den = (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)
    if abs(den) < 1e-15: return None
    t = ((x1 - x3) * (y3 - y4) - (y1 - y3) * (x3 - x4)) / den
    u = -((x1 - x2) * (y1 - y3) - (y1 - y2) * (x1 - x3)) / den
    if 0 <= t <= 1 and 0 <= u <= 1:
        return (y1 + t * (y2 - y1), x1 + t * (x2 - x1))
    return None


def in_poly(pt, poly):
    y, x = pt; inside = False
    for i in range(len(poly)):
        (y1, x1), (y2, x2) = poly[i - 1], poly[i]
        if (y1 > y) != (y2 > y) and x < (x2 - x1) * (y - y1) / ((y2 - y1) or 1e-12) + x1:
            inside = not inside
    return inside


class Unit:
    def __init__(self, battle, uid, side, type, name, strength, frontage, note="", conf=None, lines=None, blocks=None, code=None, cite=None, men=None):
        self.b, self.d = battle, dict(id=uid, side=side, type=type, name=name, strength=strength, w=frontage, keys={}, note=note)
        if conf: self.d["conf"] = conf
        if lines: self.d["lines"] = lines
        if blocks: self.d["blocks"] = blocks
        if code: self.d["code"] = code
        if cite: self.d["cite"] = list(cite)
        if men is not None:
            self.d["men"] = {0: men} if isinstance(men, int) else dict(men)

    def at(self, phase, pos, facing, form="L", men=None, via=None, bend=0):
        lat, lon = self.b.pos(pos)
        self.d["keys"][phase] = [round(lat, 5), round(lon, 5), facing, form] + ([round(bend, 3)] if bend else [])
        if men is not None:
            self.d.setdefault("men", {})[phase] = men
        if via:
            self.d.setdefault("via", {})[phase] = [[round(v, 5) for v in self.b.pos(p)] for p in via]
        return self

    def key(self, i):
        return next((self.d["keys"][j] for j in range(i, -1, -1) if j in self.d["keys"]), None)

    def men_at(self, i):
        m = self.d.get("men", {})
        return next((m[j] for j in range(i, -1, -1) if j in m), None)


class Battle:
    def __init__(self, bid, root):
        self.id, self.root = bid, root
        self.meta, self.places, self.hills, self.roads, self.woods = {}, {}, {}, [], []
        self.water = {"rivers": [], "lakes": [], "labels": {}}
        self.camps, self.units, self.hq, self.phases = [], [], [], []
        self.sources, self.crossings, self.overlays = {}, [], []
        pf = os.path.join(root, "places.json")
        self.geo = json.load(open(pf)) if os.path.exists(pf) else {}

    # ---- sources
    def source(self, sid, label, url=None, note=None, kind=None):
        """kind: 'primary' | 'official-history' | 'scholarly' | 'staff-map' | 'period-map' | 'reference' | 'popular' | 'data'"""
        self.sources[sid] = {k: v for k, v in dict(id=sid, label=label, url=url, note=note, kind=kind).items() if v}
        return sid

    # ---- positions
    def pos(self, p):
        if isinstance(p, str):
            if p in self.places: return tuple(self.places[p][:2])
            if p in self.hills: return tuple(self.hills[p])
            if p in self.geo: return tuple(self.geo[p][:2])
            raise KeyError(f"unknown place {p!r}")
        if isinstance(p, (list, tuple)) and len(p) >= 3 and isinstance(p[0], (str, tuple, list)):
            base = self.pos(p[0]); rest = p[1:]
            for i in range(0, len(rest), 2):
                base = mv(base, rest[i], rest[i + 1])
            return base
        return (float(p[0]), float(p[1]))

    def place(self, name, pos=None, size=1.0):
        lat, lon = self.pos(pos) if pos is not None else tuple(self.geo[name][:2])
        self.places[name] = [round(lat, 5), round(lon, 5)] + ([size] if size != 1.0 else [])

    def hill(self, name, pos):
        self.hills[name] = [round(v, 5) for v in self.pos(pos)]

    def crossing(self, name, pos):
        self.crossings.append({"name": name, "p": [round(v, 5) for v in self.pos(pos)]})

    def overlay(self, oid, label, file, kind="period", opacity=0.85, note=None):
        self.overlays.append({k: v for k, v in dict(id=oid, label=label, file=file, kind=kind, opacity=opacity, note=note).items() if v is not None})

    # ---- units and commanders
    def unit(self, *a, **k):
        u = Unit(self, *a, **k); self.units.append(u); return u

    def commander(self, cid, side, name, keys, note=""):
        self.hq.append(dict(id=cid, side=side, name=name, keys={p: [round(v, 5) for v in self.pos(x)] for p, x in keys.items()}, note=note))

    # ---- phases
    def arrow(self, side, kind, *pts):
        return dict(s=side, k=kind, p=[[round(v, 5) for v in self.pos(x)] for x in pts])

    def phase(self, t, label, title, text, tactic, focus, dist, arrows=(), events=(), conf=None, debate=None, day=1, fog=0.0, cite=None):
        evs = []
        for e in events:
            p, txt = e[0], e[1]
            ev = [*[round(v, 5) for v in self.pos(p)], txt]
            if len(e) > 2: ev.append(list(e[2]))
            evs.append(ev)
        tac = list(tactic)
        ph = dict(t=t, label=label, title=title, text=text, tactic=tac[:2], arrows=list(arrows), events=evs,
                  focus=[*[round(v, 5) for v in self.pos(focus)], dist])
        if len(tac) > 2 and tac[2]: ph["tacticId"] = tac[2]
        if day != 1: ph["day"] = day
        if fog: ph["fog"] = fog
        if conf: ph["conf"] = conf
        if debate: ph["debate"] = debate
        if cite: ph["cite"] = list(cite)
        self.phases.append(ph)
        return len(self.phases) - 1

    # ---- validation
    def validate(self, bbox):
        W, S, E, N = bbox
        errs, warns = [], []
        inside = lambda la, lo: S <= la <= N and W <= lo <= E
        sides = self.meta.get("sides", {})
        n = len(self.phases)
        src_ids = set(self.sources)
        if not src_ids and isinstance(self.meta.get("sources"), list):
            src_ids = {s.get("id") for s in self.meta["sources"] if s.get("id")}
        def check_cites(where, ids):
            for c in ids or []:
                if c not in src_ids: errs.append(f"{where}: unknown source id [{c}]")
        bel_of = {s: b["name"] for b in self.meta.get("belligerents", []) for s in b["sides"]}
        if self.meta.get("era") and self.meta["era"] not in ERAS: errs.append(f"meta.era must be one of {sorted(ERAS)}")
        for u in self.units:
            d = u.d
            if d["side"] not in sides: errs.append(f"{d['id']}: side {d['side']} not in meta.sides")
            if d["type"] not in TYPES: errs.append(f"{d['id']}: bad type {d['type']}")
            if 0 not in d["keys"]: errs.append(f"{d['id']}: no position at phase 0")
            if d.get("conf") not in CONF: errs.append(f"{d['id']}: bad conf")
            check_cites(d["id"], d.get("cite"))
            if src_ids and not d.get("cite"): warns.append(f"{d['id']}: no citation")
            if "men" not in d: warns.append(f"{d['id']}: no strength (men)")
            for p, (la, lo, f, form, *_) in d["keys"].items():
                if not 0 <= p < n: errs.append(f"{d['id']}: phase {p} out of range")
                if form not in FORMS: errs.append(f"{d['id']}@{p}: bad form {form}")
                if not inside(la, lo): errs.append(f"{d['id']}@{p}: outside map")
            for p, pts in d.get("via", {}).items():
                for la, lo in pts:
                    if not inside(la, lo): errs.append(f"{d['id']}@{p}: via point outside map")
        for i, ph in enumerate(self.phases):
            if not re.fullmatch(r"\d{1,2}:\d{2}", ph["t"]): errs.append(f"phase {i}: time must be HH:MM")
            check_cites(f"phase {i}", ph.get("cite"))
            for txt in (ph["text"], ph.get("debate", ""), *ph["tactic"]):
                check_cites(f"phase {i} text", CITE_RE.findall(txt))
            for ev in ph["events"]:
                check_cites(f"phase {i} event", ev[3] if len(ev) > 3 else [])
            if src_ids and not (ph.get("cite") or CITE_RE.findall(ph["text"])): warns.append(f"phase {i}: no citation")
            if not ph.get("conf"): warns.append(f"phase {i}: no confidence level")
            for a in ph["arrows"]:
                if a["k"] not in ARROWS: errs.append(f"phase {i}: bad arrow kind {a['k']}")
                if a["s"] not in sides: errs.append(f"phase {i}: arrow side {a['s']}")
                if len(a["p"]) < 2: errs.append(f"phase {i}: arrow needs 2+ points")
                for la, lo in a["p"]:
                    if not inside(la, lo): errs.append(f"phase {i}: arrow point outside map")
        tmin = [minutes(ph["t"], ph.get("day", 1)) for ph in self.phases]
        if any(b <= a for a, b in zip(tmin, tmin[1:])): errs.append("phase times must strictly increase (use day= for later days)")
        for h in self.hq:
            if 0 not in h["keys"]: errs.append(f"hq {h['id']}: no position at phase 0")
        ids = [u.d["id"] for u in self.units]
        if len(ids) != len(set(ids)): errs.append("duplicate unit ids")
        for b in self.meta.get("belligerents", []):
            for s in b["sides"]:
                if s not in sides: errs.append(f"belligerent {b['name']}: side {s}")
        for k in ("title", "year", "eyebrow", "subtitle", "sides", "belligerents", "forces", "sun", "method"):
            if k not in self.meta: errs.append(f"meta.{k} missing")
        if not src_ids and not self.meta.get("sources"): errs.append("no sources: add B.source(...)")
        if errs:
            return errs, warns
        warns += self.sanity(tmin, bel_of)
        return errs, warns

    def sanity(self, tmin, bel_of):
        """Physical plausibility checks; returns warnings."""
        w = []
        lakes = self.water.get("lakes", [])
        rivers = [r["p"] for r in self.water.get("rivers", []) if not r.get("ford")]  # ford=True: brook crossable anywhere
        cross = [c["p"] for c in self.crossings]
        n = len(self.phases)
        for u in self.units:
            d = u.d; kp = sorted(d["keys"])
            for a, b in zip(kp, kp[1:]):
                pa, pb = d["keys"][a][:2], d["keys"][b][:2]
                path = [pa] + d.get("via", {}).get(b, []) + [pb]
                dist = sum(dist_m(p, q) for p, q in zip(path, path[1:]))
                hrs = (tmin[b] - tmin[a]) / 60
                vmax = SPEED[d["type"]] * (1.6 if d["keys"][b][3] == "R" else 1)  # men in flight briefly outrun a march
                if hrs > 0 and dist / 1000 / hrs > vmax and dist > 400:
                    w.append(f"SPEED {d['id']} phase {a}->{b}: {dist/1000:.1f} km in {hrs*60:.0f} min = {dist/1000/hrs:.1f} km/h (max {vmax:g} for {d['type']}{' routing' if vmax > SPEED[d['type']] else ''})")
                for p, q in zip(path, path[1:]):
                    for r in rivers:
                        for r1, r2 in zip(r, r[1:]):
                            x = seg_intersect(p, q, r1, r2)
                            if x and not any(dist_m(x, c) < 450 for c in cross):
                                w.append(f"CROSSING {d['id']} phase {a}->{b} crosses a river at ({x[0]:.4f}, {x[1]:.4f}) with no declared bridge/ford within 450 m (B.crossing)")
            for i in range(n):
                k = u.key(i)
                if k and any(in_poly(k[:2], L) for L in lakes) and not (u.d.get("onIce") or {}).get(i):
                    w.append(f"WATER {d['id']} phase {i}: centre is in a lake/pond")
        # WOODS: a deployed line whose ends stand well inside a drawn wood
        for u in self.units:
            for p, k in u.d["keys"].items():
                if k[3] not in "LF": continue
                th = math.radians(k[2]); half = u.d["w"] / 2
                ends = [mv(tuple(k[:2]), (k[2] + 90) % 360, half), mv(tuple(k[:2]), (k[2] + 270) % 360, half), tuple(k[:2])]
                for wl, wo, rx, ry in self.woods:
                    for e in ends:
                        dy, dx = (e[0] - wl) * 111200, (e[1] - wo) * 111200 * math.cos(math.radians(wl))
                        if (dx / max(rx - 60, 1)) ** 2 + (dy / max(ry - 60, 1)) ** 2 < 1:
                            w.append(f"WOODS {u.d['id']}@{p}: frontage reaches more than 60 m into the wood at ({wl:.4f}, {wo:.4f})"); break
                    else: continue
                    break
        for i in range(n):
            arrows = self.phases[i]["arrows"]
            pts = [(u, u.key(i)) for u in self.units if u.key(i)]
            for x in range(len(pts)):
                for y in range(x + 1, len(pts)):
                    (u1, k1), (u2, k2) = pts[x], pts[y]
                    if bel_of.get(u1.d["side"]) == bel_of.get(u2.d["side"]): continue
                    if dist_m(k1[:2], k2[:2]) < 150 and k1[3] not in "FR" and k2[3] not in "FR":
                        near_charge = any(a["k"] == "charge" and min(dist_m(p, k1[:2]) for p in a["p"]) < 600 for a in arrows)
                        if not near_charge:
                            w.append(f"OVERLAP phase {i}: {u1.d['id']} and {u2.d['id']} (hostile) are {dist_m(k1[:2], k2[:2]):.0f} m apart without firing, routing or a charge")
        fs = self.meta.get("forces", {}).get("start", [])
        for row in fs:
            sides_in = [s for s, _ in row["segs"]]
            tot = sum((u.men_at(0) or 0) for u in self.units if u.d["side"] in sides_in)
            if tot and abs(tot - row["n"]) / row["n"] > 0.15:
                w.append(f"STRENGTH {row['label']}: units sum to {tot:,} at phase 0 vs forces.start {row['n']:,} (>15% apart; detachments off-map should be explained in notes)")
        return w

    # ---- export
    def export(self, strict=None):
        strict = strict if strict is not None else os.environ.get("BATTLEKIT_STRICT") == "1"
        T = json.load(open(os.path.join(self.root, "terrain.json")))
        errs, warns = self.validate(T["bbox"])
        report = ["# Validation", "", f"{len(errs)} errors, {len(warns)} warnings", ""] + [f"- ERROR {e}" for e in errs] + [f"- {w}" for w in warns]
        open(os.path.join(self.root, "validation.md"), "w").write("\n".join(report) + "\n")
        if errs:
            raise SystemExit("VALIDATION FAILED:\n  " + "\n  ".join(errs))
        if warns:
            print(f"{len(warns)} warnings (see validation.md):\n  " + "\n  ".join(warns[:25]) + ("\n  ..." if len(warns) > 25 else ""))
            if strict:
                raise SystemExit("STRICT: warnings must be resolved")
        meta = dict(self.meta)
        if self.sources:
            meta["sources"] = list(self.sources.values())
        if self.overlays:
            meta["overlays"] = [{**o, "file": f"battles/{self.id}.{o['id']}.webp"} for o in self.overlays]
        terrain = {"w": T["w"], "h": T["h"], "bbox": T["bbox"], "exag": T.get("exag", 3.2),
                   "b64": base64.b64encode(struct.pack("<%dH" % len(T["z"]), *T["z"])).decode()}
        out = dict(id=self.id, meta=meta, terrain=terrain, phases=self.phases,
                   units=[u.d for u in self.units], hq=self.hq, places=self.places, hills=self.hills,
                   roads=self.roads, woods=self.woods, water=self.water, camps=self.camps, crossings=self.crossings)
        path = os.path.join(self.root, f"{self.id}.json")
        json.dump(out, open(path, "w"), ensure_ascii=False)
        self.check_plot(T)
        print(f"{self.id}: {len(self.units)} units, {len(self.phases)} phases -> {path} ({os.path.getsize(path)//1024} KB), check.png")

    def check_plot(self, T):
        from PIL import Image, ImageDraw
        import numpy as np
        W, S, E, N = T["bbox"]
        z = np.array(T["z"], dtype=float).reshape(T["h"], T["w"])
        PW = 560; PH = round(PW * T["h"] / T["w"])
        base = Image.fromarray((z / max(1, z.max()) * 160 + 60).astype(np.uint8)).resize((PW, PH)).convert("RGB")
        px = lambda la, lo: ((lo - W) / (E - W) * PW, (N - la) / (N - S) * PH)
        cols = {k: tuple(int(v["top"].lstrip("#")[i:i + 2], 16) for i in (0, 2, 4)) for k, v in self.meta["sides"].items()}
        panels = []
        kx = 111200 * math.cos(math.radians((S + N) / 2))
        mpp = (E - W) * kx / PW
        for i, ph in enumerate(self.phases):
            im = base.copy(); d = ImageDraw.Draw(im)
            for line in self.water["rivers"]:
                d.line([px(*p) for p in line["p"]], fill=(60, 110, 200), width=2)
            for poly in self.water["lakes"]:
                d.polygon([px(*p) for p in poly], fill=(90, 140, 210))
            for c in self.crossings:
                x, y = px(*c["p"]); d.rectangle([x - 3, y - 3, x + 3, y + 3], outline=(0, 0, 160))
            for n_, v in self.places.items():
                x, y = px(*v[:2]); d.rectangle([x - 2, y - 2, x + 2, y + 2], fill=(0, 0, 0)); d.text((x + 3, y - 5), n_[:10], fill=(0, 70, 0))
            for a in ph["arrows"]:
                d.line([px(*p) for p in a["p"]], fill=(255, 140, 0) if a["k"] != "fire" else (255, 0, 0), width=2)
                x, y = px(*a["p"][-1]); d.ellipse([x - 3, y - 3, x + 3, y + 3], fill=(255, 140, 0))
            for u in self.units:
                k = u.key(i)
                la, lo, f, form = k[:4]; x, y = px(la, lo)
                if i in u.d.get("via", {}):
                    prev = u.key(i - 1) if i > 0 else k
                    d.line([px(*prev[:2])] + [px(*p) for p in u.d["via"][i]] + [px(la, lo)], fill=(140, 140, 140), width=1)
                L = u.d["w"] / mpp / 2
                ang = math.radians(f if form == "C" else f + 90)
                dx, dy = math.sin(ang) * L, -math.cos(ang) * L
                d.line([x - dx, y - dy, x + dx, y + dy], fill=cols[u.d["side"]], width=1 if form == "R" else 4)
                fx, fy = math.sin(math.radians(f)) * 6, -math.cos(math.radians(f)) * 6
                d.line([x, y, x + fx, y + fy], fill=(0, 0, 0), width=1)
                men = u.men_at(i)
                d.text((x + 4, y + 2), u.d.get("code", u.d["id"])[:6] + (f" {men//1000 if men >= 1000 else men}{'k' if men >= 1000 else ''}" if men else ""), fill=(20, 20, 20))
            for e_i, ev in enumerate(ph["events"]):
                x, y = px(ev[0], ev[1]); d.ellipse([x - 6, y - 6, x + 6, y + 6], outline=(230, 190, 60), width=2); d.text((x - 3, y - 6), str(e_i + 1), fill=(0, 0, 0))
            d.rectangle([0, 0, 230, 14], fill=(0, 0, 0)); d.text((4, 2), f"{i}  D{ph.get('day', 1)} {ph['t']}  {ph['label']}", fill=(255, 255, 0))
            panels.append(im)
        cols_n = 2
        G = Image.new("RGB", (PW * cols_n, PH * math.ceil(len(panels) / cols_n)), (40, 40, 40))
        for i, p in enumerate(panels):
            G.paste(p, ((i % cols_n) * PW, (i // cols_n) * PH))
        G.save(os.path.join(self.root, "check.png"))
