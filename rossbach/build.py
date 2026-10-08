import json, base64, struct
h = json.load(open("data/height.json"))
s = json.load(open("data/scenario.json"))
b64 = base64.b64encode(struct.pack("<%dH" % len(h["z"]), *h["z"])).decode()
meta = {"w": h["w"], "h": h["h"], "bbox": h["bbox"]}
src = open("src.html").read()
for k, v in [("/*SCENARIO*/null", json.dumps(s, ensure_ascii=False)), ("/*HMETA*/null", json.dumps(meta)), ("/*HEIGHT*/", b64)]:
    assert k in src, k
    src = src.replace(k, v)
open("rossbach.html", "w").write(src)
print("rossbach.html", len(src))
open("preview.html", "w").write('<!doctype html><html><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover"><style>:root{color-scheme:light}body{margin:0;font:14px system-ui}[hidden]{display:none!important}img{max-width:100%}</style></head><body>' + src + '</body></html>')
