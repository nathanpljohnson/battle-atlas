"""Build the library site.

usage: python3 tools/build_library.py
Reads library.json (ordered battle ids), tactics.json, and battles/<id>/<id>.json (+ overlay_<ov>.webp).
Writes:
  dist/index.html            body fragment for publishing as a claude.ai Artifact; battle data fetched from dist/battles/*.json
  dist/battles/<id>.json     battle data
  dist/battles/<id>.<ov>.webp  georeferenced map overlays
  dist/preview.html          full HTML document with all battle JSON inlined (overlays still load from battles/)
  dist/files.json            the `files` map to pass to the Artifact publish call
"""
import json, os, shutil

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ids = json.load(open(os.path.join(ROOT, "library.json")))
tactics = json.load(open(os.path.join(ROOT, "tactics.json")))
src = open(os.path.join(ROOT, "engine", "index.src.html")).read()
dist = os.path.join(ROOT, "dist"); os.makedirs(os.path.join(dist, "battles"), exist_ok=True)
manifest, inline, files, uses = [], {}, {}, {}
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
json.dump(files, open(os.path.join(dist, "files.json"), "w"), indent=1)
print(f"dist/index.html + {len(ids)} battles ({', '.join(ids)}), {sum(len(v) for v in uses.values())} tactic links, {len(files)} files")
