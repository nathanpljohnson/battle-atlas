"""Find historical place names on the modern map, cross-checking two independent gazetteers.

usage: python3 tools/gazetteer.py battles/<id> [names.json]

names.json (default battles/<id>/names.json):
  {"bbox": [W, S, E, N],                     # optional, else terrain_config.json bbox
   "langs": ["de", "en", "cs"],              # languages to search labels and aliases in
   "names": {"Bosenitz": {}, "Pratzen": {"modern": "Prace"}, "Zuran": {"kind": "hill"}}}

For each historical name:
  1. Wikidata: search labels and aliases (where historical names live) in each language,
     keep candidates whose coordinates fall inside the bbox (plus 3 km).
  2. Nominatim (OpenStreetMap): search the modern name if given, else the historical one, bounded to the bbox.
  3. Agree within 1 km -> use the Wikidata point. Disagree -> flag in the report and use Wikidata if it exists.
Writes places.json (merging with what is there; existing entries are kept unless --overwrite) and gazetteer_report.md.
"""
import json, math, os, re, subprocess, sys, time, urllib.parse

UA = "BattleAtlas/0.2 (https://claude.ai/; personal non-commercial history project)"


def get(url, tries=4):
    for k in range(tries):
        r = subprocess.run(["curl", "-s", "-A", UA, url], capture_output=True, text=True)
        time.sleep(1.1)
        try:
            return json.loads(r.stdout or "null")
        except json.JSONDecodeError:
            time.sleep(4 * (k + 1))  # rate limited: back off
    return None


def dist_m(a, b):
    kx = 111200 * math.cos(math.radians((a[0] + b[0]) / 2))
    return math.hypot((a[0] - b[0]) * 111200, (a[1] - b[1]) * kx)


def wikidata(name, langs, bbox):
    W, S, E, N = bbox; pad = 0.04
    ids = []
    for lg in langs:
        q = urllib.parse.urlencode({"action": "wbsearchentities", "search": name, "language": lg, "uselang": lg, "limit": 12, "format": "json", "type": "item"})
        res = get("https://www.wikidata.org/w/api.php?" + q) or {}
        for it in res.get("search", []):
            if it["id"] not in ids:
                ids.append(it["id"])
    if not ids:
        return []
    q = urllib.parse.urlencode({"action": "wbgetentities", "ids": "|".join(ids[:40]), "props": "claims|labels", "languages": "en|cs|de|fr|pl|it|ru", "format": "json"})
    ents = (get("https://www.wikidata.org/w/api.php?" + q) or {}).get("entities", {})
    out = []
    for qid, e in ents.items():
        c = e.get("claims", {}).get("P625")
        if not c:
            continue
        v = c[0]["mainsnak"].get("datavalue", {}).get("value")
        if not v:
            continue
        la, lo = v["latitude"], v["longitude"]
        if S - pad <= la <= N + pad and W - pad <= lo <= E + pad:
            labels = e.get("labels", {})
            local = next((labels[k]["value"] for k in ("cs", "de", "pl", "fr", "it", "ru", "en") if k in labels), qid)
            out.append({"qid": qid, "lat": round(la, 5), "lon": round(lo, 5), "label": local, "en": labels.get("en", {}).get("value", ""), "src": "wikidata"})
    return out


def wikipedia(name, langs, bbox):
    """Full-text search Wikipedia articles (which give historical names in their first lines) and keep
    only articles whose coordinates fall inside the bbox."""
    W, S, E, N = bbox; pad = 0.03; out = []
    for lg in langs:
        q = urllib.parse.urlencode({"action": "query", "generator": "search", "gsrsearch": f'"{name}"', "gsrlimit": 20,
                                    "prop": "coordinates", "format": "json", "colimit": "max"})
        res = get(f"https://{lg}.wikipedia.org/w/api.php?" + q) or {}
        for p in (res.get("query") or {}).get("pages", {}).values():
            co = (p.get("coordinates") or [None])[0]
            if p["title"].split()[0] in ("Liste", "List", "Okres", "District", "Bezirk", "Seznam"):
                continue
            if co and S - pad <= co["lat"] <= N + pad and W - pad <= co["lon"] <= E + pad:
                out.append({"lat": round(co["lat"], 5), "lon": round(co["lon"], 5), "label": p["title"], "src": f"{lg}.wikipedia", "rank": p.get("index", 99)})
        if out:
            break
    return sorted(out, key=lambda c: c["rank"])


def osm_place_nodes(names, bbox):
    """Exact settlement nodes (place=village/town/hamlet/...) from OpenStreetMap via Overpass. Nominatim can return
    an administrative-area centroid that is a kilometre or more from the village itself; place nodes sit on it."""
    W, S, E, N = bbox; pad = 0.03
    rx = "|".join(re.escape(n) for n in names if n)
    q = f'[out:json][timeout:60];node["place"]["name"~"^({rx})$"]({S - pad},{W - pad},{N + pad},{E + pad});out;'
    for k in range(5):
        r = subprocess.run(["curl", "-s", "-A", UA, "--data-urlencode", "data=" + q, "https://overpass-api.de/api/interpreter"], capture_output=True, text=True)
        try:
            els = json.loads(r.stdout)["elements"]
            break
        except Exception:
            time.sleep(12 * (k + 1))
    else:
        return {}
    out = {}
    for e in els:
        out.setdefault(e["tags"]["name"], []).append({"lat": round(e["lat"], 5), "lon": round(e["lon"], 5), "label": e["tags"]["name"], "src": "osm-node:" + e["tags"].get("place", "")})
    return out


def nominatim(q, bbox):
    W, S, E, N = bbox
    p = urllib.parse.urlencode({"q": q, "format": "json", "limit": 3, "viewbox": f"{W},{N},{E},{S}", "bounded": 1})
    res = get("https://nominatim.openstreetmap.org/search?" + p) or []
    return [{"lat": round(float(r["lat"]), 5), "lon": round(float(r["lon"]), 5), "label": r["display_name"].split(",")[0], "type": r.get("type")} for r in res]


def main(bdir, names_path=None, overwrite=False):
    cfg = json.load(open(names_path or os.path.join(bdir, "names.json")))
    bbox = cfg.get("bbox") or json.load(open(os.path.join(bdir, "terrain_config.json")))["bbox"]
    langs = cfg.get("langs", ["de", "en"])
    pp = os.path.join(bdir, "places.json")
    places = json.load(open(pp)) if os.path.exists(pp) else {}
    rep = ["# Gazetteer report", "", f"bbox {bbox}, languages {langs}", "",
           "| historical name | Wikidata or Wikipedia | OSM Nominatim | gap | used |", "|---|---|---|---|---|"]
    flags = []
    nodes = osm_place_nodes([n for o in cfg["names"].items() for n in (o[0], (o[1].get("modern") or "").split(",")[0].strip())], bbox)
    rep[4] = "| historical name | Wikidata or Wikipedia | OSM (place node, else Nominatim) | gap | used |"
    for name, opt in cfg["names"].items():
        wd = wikidata(name, langs, bbox)
        if opt.get("modern"):
            wd += [c for c in wikidata(opt["modern"], langs, bbox) if c["qid"] not in {w["qid"] for w in wd}]
        wp = [] if wd else wikipedia(name, langs, bbox)
        if not wd and wp:
            wd = wp
        key = (opt.get("modern") or "").split(",")[0].strip()
        nm = nodes.get(name) or nodes.get(key) or nominatim(opt.get("modern") or (wp[0]["label"] if wp else name), bbox)
        best_w = wd[0] if wd else None
        if best_w and len(wd) > 1 and nm:
            best_w = min(wd, key=lambda c: dist_m((c["lat"], c["lon"]), (nm[0]["lat"], nm[0]["lon"])))
        best_n = nm[0] if nm else None
        gap = dist_m((best_w["lat"], best_w["lon"]), (best_n["lat"], best_n["lon"])) if best_w and best_n else None
        norm = lambda x: (x or "").lower().replace("ß", "ss").split(",")[0].split("(")[0].strip()
        targets = {norm(name), norm(opt.get("modern"))} - {""}
        osm_is_village = best_n and any(norm(best_n["label"]).startswith(t) or t.startswith(norm(best_n["label"])) for t in targets)
        wd_is_village = best_w and any(norm(best_w["label"]).startswith(t) for t in targets)
        # OSM points sit on the village itself; Wikidata sometimes gives a municipality centroid or a landmark in it
        if best_n and best_n.get("src", "").startswith("osm-node"):
            pick = best_n  # a settlement node is the most precise point available
        else:
            pick = best_n if osm_is_village and (not wd_is_village or (gap or 0) > 400) else (best_w or best_n)
        note = ""
        if pick is None:
            note = "NOT FOUND"; flags.append(name)
        elif gap is not None and gap > 1000:
            note = f"**CHECK: sources {gap/1000:.1f} km apart**"; flags.append(name)
        elif len(wd) > 1:
            note = f"{len(wd)} Wikidata candidates; nearest to OSM used"
        if pick and (overwrite or name not in places):
            places[name] = [pick["lat"], pick["lon"]]
        fmt = lambda c, k="label": f"{c[k]} ({c['lat']}, {c['lon']})" + (f" {c.get('qid') or c.get('src', '')}" if c.get('src') or c.get('qid') else "") if c else "-"
        rep.append(f"| {name} | {fmt(best_w)} | {fmt(best_n)} | {'' if gap is None else f'{gap:.0f} m'} | {('kept existing' if name in places and pick and not overwrite and places[name] != [pick['lat'], pick['lon']] else 'yes') if pick else 'no'} {note} |")
        print(f"{name:22s} wd={fmt(best_w)[:46]:46s} osm={fmt(best_n)[:40]:40s} {note}")
    if flags:
        rep += ["", f"**Needs a human or source check:** {', '.join(flags)}. Confirm against a period map (georef.py residuals help) before using."]
    json.dump(places, open(pp, "w"), ensure_ascii=False, indent=1)
    open(os.path.join(bdir, "gazetteer_report.md"), "w").write("\n".join(rep) + "\n")


if __name__ == "__main__":
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    main(args[0], args[1] if len(args) > 1 else None, "--overwrite" in sys.argv)
