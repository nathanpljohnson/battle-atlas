"""Build the library site.

usage: python3 tools/build_library.py
Reads library.json (ordered battle ids), tactics.json, and battles/<id>/<id>.json (+ overlay_<ov>.webp).
Writes:
  dist/index.html            body fragment for publishing as a claude.ai Artifact; battle data fetched from dist/battles/*.json
  dist/battles/<id>.json     battle data
  dist/battles/<id>.<ov>.webp  georeferenced map overlays
  dist/preview.html          full HTML document with all battle JSON inlined (overlays still load from battles/)
  dist/battle-atlas-offline.html  one standalone HTML file: data, overlays, and local Three.js runtime inlined
  dist/files.json            the `files` map to pass to the Artifact publish call
"""
import base64, copy, json, os, shutil

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ids = json.load(open(os.path.join(ROOT, "library.json")))
tactics = json.load(open(os.path.join(ROOT, "tactics.json")))
src = open(os.path.join(ROOT, "engine", "index.src.html")).read()
dist = os.path.join(ROOT, "dist"); os.makedirs(os.path.join(dist, "battles"), exist_ok=True)
manifest, inline, offline_inline, files, uses = [], {}, {}, {}, {}
for bid in ids:
    bdir = os.path.join(ROOT, "battles", bid)
    data = json.load(open(os.path.join(bdir, f"{bid}.json")))
    m = data["meta"]
    confs = [p.get("conf") for p in data["phases"]] + [u.get("conf") for u in data["units"]]
    conf = {k: sum(c == k for c in confs) for k in ("high", "medium", "low")}
    W, S, E, N = data["terrain"]["bbox"]
    manifest.append({"id": bid, "title": m["title"], "year": m["year"], "eyebrow": m["eyebrow"], "subtitle": m["subtitle"],
                     "war": m.get("war", ""), "era": m.get("era", ""), "center": [round((S + N) / 2, 3), round((W + E) / 2, 3)],
                     "belligerents": [{"name": b["name"], "commander": b["commander"], "color": m["sides"][b["sides"][0]]["top"]} for b in m["belligerents"]],
                     "forces": m["forces"]["start"], "phases": len(data["phases"]), "units": len(data["units"]), "conf": conf,
                     "nsources": len(m.get("sources", []))})
    for i, ph in enumerate(data["phases"]):
        tid = ph.get("tacticId")
        if tid:
            if tid not in tactics:
                raise SystemExit(f"{bid} phase {i}: tacticId {tid!r} not in tactics.json")
            uses.setdefault(tid, []).append({"battle": bid, "phase": i, "t": ph["t"], "day": ph.get("day", 1), "label": ph["label"], "title": m["title"], "year": m["year"]})
    out = os.path.join(dist, "battles", f"{bid}.json")
    json.dump(data, open(out, "w"), ensure_ascii=False)
    files[f"battles/{bid}.json"] = out
    for ov in m.get("overlays", []):
        oid = ov["id"]; s = os.path.join(bdir, f"overlay_{oid}.webp"); d = os.path.join(dist, "battles", f"{bid}.{oid}.webp")
        if not os.path.exists(s):
            raise SystemExit(f"{bid}: overlay {oid} missing: run python3 tools/georef.py battles/{bid} --overlays")
        shutil.copy(s, d); files[f"battles/{bid}.{oid}.webp"] = d
    inline[bid] = data
    standalone = copy.deepcopy(data)
    for ov in standalone["meta"].get("overlays", []):
        oid = ov["id"]
        source = os.path.join(bdir, f"overlay_{oid}.webp")
        with open(source, "rb") as image:
            ov["file"] = "data:image/webp;base64," + base64.b64encode(image.read()).decode("ascii")
    offline_inline[bid] = standalone
tindex = {tid: {**t, "uses": uses.get(tid, [])} for tid, t in tactics.items()}
for k in ("/*MANIFEST*/[]", "/*INLINE*/null", "/*TACTICS*/{}"):
    assert k in src, k
page = src.replace("/*MANIFEST*/[]", json.dumps(manifest, ensure_ascii=False)).replace("/*TACTICS*/{}", json.dumps(tindex, ensure_ascii=False))
open(os.path.join(dist, "index.html"), "w").write(page.replace("/*INLINE*/null", "null"))
full = page.replace("/*INLINE*/null", json.dumps(inline, ensure_ascii=False))
open(os.path.join(dist, "preview.html"), "w").write(
    '<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">'
    '<style>:root{color-scheme:light}body{margin:0;font:14px system-ui}[hidden]{display:none!important}img{max-width:100%}</style></head><body>'
    + full + "</body></html>")
# A portable release file: it has no sibling data/image files and no CDN runtime
# dependency.  The vendored copies retain the upstream Three.js MIT license headers.
three = open(os.path.join(ROOT, "engine", "vendor", "three.min.js")).read()
controls = open(os.path.join(ROOT, "engine", "vendor", "OrbitControls.js")).read()
standalone = page.replace("/*INLINE*/null", json.dumps(offline_inline, ensure_ascii=False))
for tag in (
    '<link rel="preconnect" href="https://fonts.googleapis.com">',
    '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>',
    '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=IM+Fell+English+SC&family=Alegreya+Sans:ital,wght@0,400;0,500;0,700;1,400&family=Alegreya+Sans+SC:wght@500;700&display=swap">',
):
    standalone = standalone.replace(tag, "")
standalone = standalone.replace(
    '<script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/0.147.0/three.min.js"></script>',
    '<script>\n' + three + '\n</script>')
standalone = standalone.replace(
    '<script src="https://cdn.jsdelivr.net/npm/three@0.147.0/examples/js/controls/OrbitControls.js"></script>',
    '<script>\n' + controls + '\n</script>')
open(os.path.join(dist, "battle-atlas-offline.html"), "w").write(
    '<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">'
    '<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns=%27http://www.w3.org/2000/svg%27 viewBox=%270 0 64 64%27%3E%3Crect width=%2764%27 height=%2764%27 fill=%27%23101419%27/%3E%3Cpath d=%27M10 49L32 9l22 40z%27 fill=%27%23d4a44e%27/%3E%3C/svg%3E">'
    '<style>:root{color-scheme:light}body{margin:0}[hidden]{display:none!important}img{max-width:100%}</style></head><body>'
    + standalone + "</body></html>")
json.dump(files, open(os.path.join(dist, "files.json"), "w"), indent=1)
# test page: python3 tools/build_library.py also writes dist/preview_tests.html with fixtures from tests/*/ (never published)
import glob
fx = {}
for fp in glob.glob(os.path.join(ROOT, "tests", "*", "*.json")):
    d = json.load(open(fp))
    if "meta" in d and "phases" in d: fx[d["id"]] = d
if fx:
    tman = manifest + [{"id": k, "title": v["meta"]["title"], "year": v["meta"]["year"], "eyebrow": v["meta"]["eyebrow"], "subtitle": v["meta"]["subtitle"], "war": "Test", "era": v["meta"].get("era", ""),
                        "center": [0, 0], "belligerents": [], "forces": v["meta"]["forces"]["start"], "phases": len(v["phases"]), "units": len(v["units"]), "conf": {"high": 1, "medium": 0, "low": 0}, "nsources": 1} for k, v in fx.items()]
    tp = src.replace("/*MANIFEST*/[]", json.dumps(tman, ensure_ascii=False)).replace("/*TACTICS*/{}", json.dumps(tindex, ensure_ascii=False)).replace("/*INLINE*/null", json.dumps({**inline, **fx}, ensure_ascii=False))
    open(os.path.join(dist, "preview_tests.html"), "w").write('<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"></head><body>' + tp + "</body></html>")
print(f"dist/index.html + {len(ids)} battles ({', '.join(ids)}), {sum(len(v) for v in uses.values())} tactic links, {len(files)} publish files, standalone release")
