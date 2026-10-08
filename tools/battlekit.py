"""Authoring kit for battle scenarios.

A battle's scenario.py builds a Battle, adds places, units, phases and arrows, then calls export().
Positions can be written the way historians describe them:
    (lat, lon)                    absolute
    "Prace"                       a named place
    ("Prace", 135, 800)           800 m from Prace on bearing 135 (south-east)
    ("Prace", 135, 800, 90, 200)  then a further 200 m on bearing 90 (chained offsets)
export() validates the data, writes battles/<id>/<id>.json (with terrain embedded) and check.png,
a top-down panel per phase for comparing against source maps.
"""
import base64, json, math, os, struct

FORMS = {"X", "C", "L", "F", "R"}
TYPES = {"inf", "gd", "cav", "lc", "art", "lt"}
ARROWS = {"move", "charge", "retreat", "fire"}
CONF = {None, "high", "medium", "low"}


def mv(p, bearing, meters):
    lat, lon = p
    b = math.radians(bearing)
    return (lat + math.cos(b) * meters / 111200, lon + math.sin(b) * meters / (111200 * math.cos(math.radians(lat))))


class Unit:
    def __init__(self, battle, uid, side, type, name, strength, frontage, note="", conf=None, lines=None, blocks=None, code=None):
        self.b, self.d = battle, dict(id=uid, side=side, type=type, name=name, strength=strength, w=frontage, keys={}, note=note)
        if conf: self.d["conf"] = conf
        if lines: self.d["lines"] = lines
        if blocks: self.d["blocks"] = blocks
        if code: self.d["code"] = code

    def at(self, phase, pos, facing, form="L"):
        lat, lon = self.b.pos(pos)
        self.d["keys"][phase] = [round(lat, 5), round(lon, 5), facing, form]
        return self


class Battle:
    def __init__(self, bid, root):
        self.id, self.root = bid, root
        self.meta, self.places, self.hills, self.roads, self.woods = {}, {}, {}, [], []
        self.water = {"rivers": [], "lakes": [], "labels": {}}
        self.camps, self.units, self.hq, self.phases = [], [], [], []
        pf = os.path.join(root, "places.json")
        self.geo = json.load(open(pf)) if os.path.exists(pf) else {}

    # ---- positions
    def pos(self, p):
        if isinstance(p, str):
            if p in self.places: return tuple(self.places[p][:2])
            if p in self.hills: return tuple(self.hills[p])
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

    # ---- units and commanders
    def unit(self, *a, **k):
        u = Unit(self, *a, **k); self.units.append(u); return u

    def commander(self, cid, side, name, keys, note=""):
        self.hq.append(dict(id=cid, side=side, name=name, keys={p: [round(v, 5) for v in self.pos(x)] for p, x in keys.items()}, note=note))

    # ---- phases
    def arrow(self, side, kind, *pts):
        return dict(s=side, k=kind, p=[[round(v, 5) for v in self.pos(x)] for x in pts])

    def phase(self, t, label, title, text, tactic, focus, dist, arrows=(), events=(), conf=None, debate=None):
        ph = dict(t=t, label=label, title=title, text=text, tactic=list(tactic), arrows=list(arrows),
                  events=[[*[round(v, 5) for v in self.pos(p)], txt] for p, txt in events],
                  focus=[*[round(v, 5) for v in self.pos(focus)], dist])
        if conf: ph["conf"] = conf
        if debate: ph["debate"] = debate
        self.phases.append(ph)
        return len(self.phases) - 1

    # ---- validation + export
    def validate(self, bbox):
        W, S, E, N = bbox
        errs = []
        inside = lambda la, lo: S <= la <= N and W <= lo <= E
        sides = self.meta.get("sides", {})
        n = len(self.phases)
        for u in self.units:
            d = u.d
            if d["side"] not in sides: errs.append(f"{d['id']}: side {d['side']} not in meta.sides")
            if d["type"] not in TYPES: errs.append(f"{d['id']}: bad type {d['type']}")
            if 0 not in d["keys"]: errs.append(f"{d['id']}: no position at phase 0")
            if d.get("conf") not in CONF: errs.append(f"{d['id']}: bad conf")
            for p, (la, lo, f, form) in d["keys"].items():
                if not 0 <= p < n: errs.append(f"{d['id']}: phase {p} out of range")
                if form not in FORMS: errs.append(f"{d['id']}@{p}: bad form {form}")
                if not inside(la, lo): errs.append(f"{d['id']}@{p}: outside map")
        for i, ph in enumerate(self.phases):
            for a in ph["arrows"]:
                if a["k"] not in ARROWS: errs.append(f"phase {i}: bad arrow kind {a['k']}")
                if a["s"] not in sides: errs.append(f"phase {i}: arrow side {a['s']}")
                if len(a["p"]) < 2: errs.append(f"phase {i}: arrow needs 2+ points")
                for la, lo in a["p"]:
                    if not inside(la, lo): errs.append(f"phase {i}: arrow point outside map")
        for h in self.hq:
            if 0 not in h["keys"]: errs.append(f"hq {h['id']}: no position at phase 0")
        ids = [u.d["id"] for u in self.units]
        if len(ids) != len(set(ids)): errs.append("duplicate unit ids")
        for b in self.meta.get("belligerents", []):
            for s in b["sides"]:
                if s not in sides: errs.append(f"belligerent {b['name']}: side {s}")
        for k in ("title", "year", "eyebrow", "subtitle", "sides", "belligerents", "forces", "sun", "sources", "method"):
            if k not in self.meta: errs.append(f"meta.{k} missing")
        return errs

    def export(self):
        T = json.load(open(os.path.join(self.root, "terrain.json")))
        errs = self.validate(T["bbox"])
        if errs:
            raise SystemExit("VALIDATION FAILED:\n  " + "\n  ".join(errs))
        terrain = {"w": T["w"], "h": T["h"], "bbox": T["bbox"], "exag": T.get("exag", 3.2),
                   "b64": base64.b64encode(struct.pack("<%dH" % len(T["z"]), *T["z"])).decode()}
        out = dict(id=self.id, meta=self.meta, terrain=terrain, phases=self.phases,
                   units=[u.d for u in self.units], hq=self.hq, places=self.places, hills=self.hills,
                   roads=self.roads, woods=self.woods, water=self.water, camps=self.camps)
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
            for n_, v in self.places.items():
                x, y = px(*v[:2]); d.rectangle([x - 2, y - 2, x + 2, y + 2], fill=(0, 0, 0)); d.text((x + 3, y - 5), n_[:10], fill=(0, 70, 0))
            for a in ph["arrows"]:
                d.line([px(*p) for p in a["p"]], fill=(255, 140, 0) if a["k"] != "fire" else (255, 0, 0), width=2)
                x, y = px(*a["p"][-1]); d.ellipse([x - 3, y - 3, x + 3, y + 3], fill=(255, 140, 0))
            for u in self.units:
                k = next(u.d["keys"][j] for j in range(i, -1, -1) if j in u.d["keys"])
                la, lo, f, form = k; x, y = px(la, lo)
                L = u.d["w"] / mpp / 2
                ang = math.radians(f if form == "C" else f + 90)
                dx, dy = math.sin(ang) * L, -math.cos(ang) * L
                d.line([x - dx, y - dy, x + dx, y + dy], fill=cols[u.d["side"]], width=1 if form == "R" else 4)
                fx, fy = math.sin(math.radians(f)) * 6, -math.cos(math.radians(f)) * 6
                d.line([x, y, x + fx, y + fy], fill=(0, 0, 0), width=1)
                d.text((x + 4, y + 2), u.d.get("code", u.d["id"])[:6], fill=(20, 20, 20))
            for e_i, (la, lo, _) in enumerate(ph["events"]):
                x, y = px(la, lo); d.ellipse([x - 6, y - 6, x + 6, y + 6], outline=(230, 190, 60), width=2); d.text((x - 3, y - 6), str(e_i + 1), fill=(0, 0, 0))
            d.rectangle([0, 0, 200, 14], fill=(0, 0, 0)); d.text((4, 2), f"{i}  {ph['t']}  {ph['label']}", fill=(255, 255, 0))
            panels.append(im)
        cols_n = 2
        G = Image.new("RGB", (PW * cols_n, PH * math.ceil(len(panels) / cols_n)), (40, 40, 40))
        for i, p in enumerate(panels):
            G.paste(p, ((i % cols_n) * PW, (i // cols_n) * PH))
        G.save(os.path.join(self.root, "check.png"))
