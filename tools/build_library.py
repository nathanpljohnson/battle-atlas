"""Build the library site.

usage: python3 tools/build_library.py
Reads library.json (ordered list of battle ids) and battles/<id>/<id>.json.
Writes dist/index.html (body fragment for publishing as a claude.ai Artifact; battle data in dist/battles/*.json,
fetched on demand) and dist/preview.html (full HTML document with all battles inlined; opens straight from disk).
"""
import json, os, shutil

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ids = json.load(open(os.path.join(ROOT, "library.json")))
src = open(os.path.join(ROOT, "engine", "index.src.html")).read()
os.makedirs(os.path.join(ROOT, "dist", "battles"), exist_ok=True)
manifest, inline = [], {}
for bid in ids:
    p = os.path.join(ROOT, "battles", bid, f"{bid}.json")
    data = json.load(open(p))
    m = data["meta"]
    manifest.append({"id": bid, "title": m["title"], "year": m["year"]})
    shutil.copy(p, os.path.join(ROOT, "dist", "battles", f"{bid}.json"))
    inline[bid] = data
for k in ("/*MANIFEST*/[]", "/*INLINE*/null"):
    assert k in src, k
page = src.replace("/*MANIFEST*/[]", json.dumps(manifest, ensure_ascii=False))
open(os.path.join(ROOT, "dist", "index.html"), "w").write(page.replace("/*INLINE*/null", "null"))
full = page.replace("/*INLINE*/null", json.dumps(inline, ensure_ascii=False))
open(os.path.join(ROOT, "dist", "preview.html"), "w").write(
    '<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">'
    '<style>:root{color-scheme:light}body{margin:0;font:14px system-ui}[hidden]{display:none!important}img{max-width:100%}</style></head><body>'
    + full + "</body></html>")
print("dist/index.html +", len(ids), "battles:", ", ".join(ids))
