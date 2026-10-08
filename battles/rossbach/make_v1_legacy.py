"""Convert the original Rossbach project (~/battle-maps/rossbach) into the library format.

usage: python3 battles/rossbach/make.py
The battle content itself lives in ../../rossbach/data/scenario.py; edit there, rerun it, then rerun this.
"""
import base64, json, os, struct

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "..", "..", "rossbach", "data")
s = json.load(open(os.path.join(SRC, "scenario.json")))
h = json.load(open(os.path.join(SRC, "height.json")))

FOCUS = [[51.2610, 11.8700, 13], [51.2560, 11.8520, 11], [51.2560, 11.8950, 11], [51.2590, 11.9250, 7.5], [51.2580, 11.9370, 5.6],
         [51.2530, 11.9420, 6.4], [51.2540, 11.9260, 5.2], [51.2500, 11.9320, 5.6], [51.2440, 11.9080, 7.4], [51.2380, 11.8920, 8.4]]
for ph, f in zip(s["phases"], FOCUS):
    ph["focus"] = f
    ph["conf"] = "medium"
s["phases"][0]["conf"] = "high"
for u in s["units"]:
    u["keys"] = {int(k): v for k, v in u["keys"].items()}
    u["conf"] = "medium"
for hq in s["hq"]:
    hq["keys"] = {int(k): v for k, v in hq["keys"].items()}

meta = {
    "title": "Rossbach", "year": "1757",
    "eyebrow": "5 November 1757 · Saxony · Seven Years' War",
    "subtitle": "Frederick the Great against the French and the army of the Holy Roman Empire, in ninety minutes.",
    "sides": {
        "pr": {"name": "Prussian", "top": "#2b4f93", "side": "#1d3767", "mark": "#f3efe4", "arrow": "#3c6fd8", "flag": "#1f1f1f"},
        "fr": {"name": "French", "top": "#f1ede2", "side": "#b9b3a4", "mark": "#1d2a44", "arrow": "#fbfaf5"},
        "re": {"name": "Reichsarmee / Austrian", "top": "#b5432f", "side": "#7f2d20", "mark": "#f6f1e6", "arrow": "#d4513a"},
    },
    "belligerents": [
        {"name": "Prussian army", "commander": "Frederick II", "sides": ["pr"], "code": "letters"},
        {"name": "Allied army", "commander": "Soubise & Hildburghausen", "sides": ["fr", "re"], "code": "numbers"},
    ],
    "forces": {
        "start": [{"label": "Prussians", "n": 22000, "segs": [["pr", 1]]}, {"label": "Allies", "n": 41000, "segs": [["fr", 0.74], ["re", 0.26]]}],
        "end": [{"label": "Prussians", "n": 550, "segs": [["pr", 1]]}, {"label": "Allies", "n": 10000, "segs": [["fr", 0.74], ["re", 0.26]]}],
    },
    "sun": {"lat": 51.25, "decl": -15.6, "note": "Sunset about 16:40."},
    "view": {"az": -0.32, "el": 0.72},
    "method": "Built from a published bird's-eye map (Millar, Osprey Campaign 113) and standard narrative accounts, cross-checked for timings and order of battle. Unit positions are placed relative to the villages and hills named in those accounts and are approximate. Terrain is modern elevation data with 20th-century lignite pits smoothed out and the Janus and Polzen hills restored by estimate.",
    "sources": [
        {"label": "Simon Millar, Rossbach and Leuthen 1757 (Osprey Campaign 113, 2002)", "note": "timings, order of battle, bird's-eye map"},
        {"label": "Wikipedia: Battle of Rossbach", "url": "https://en.wikipedia.org/wiki/Battle_of_Rossbach", "note": "strengths and losses"},
        {"label": "AWS Terrain Tiles (elevation)", "url": "https://registry.opendata.aws/terrain-tiles/"},
        {"label": "OpenStreetMap Nominatim (village locations)", "url": "https://nominatim.openstreetmap.org/"},
    ],
    "notes": "Heights exaggerated about three times. Roads, woods and village outlines are illustrative.",
    "ground": {"season": "autumn", "relief": 70},
}
out = {
    "id": "rossbach", "meta": meta,
    "terrain": {"w": h["w"], "h": h["h"], "bbox": h["bbox"], "exag": 3.2, "b64": base64.b64encode(struct.pack("<%dH" % len(h["z"]), *h["z"])).decode()},
    "phases": s["phases"], "units": s["units"], "hq": s["hq"], "places": s["places"], "hills": s["hills"],
    "roads": s["roads"], "woods": s["woods"], "water": {"rivers": [], "lakes": [], "labels": {}},
    "camps": [{"a": [51.2625, 11.8965], "b": [51.2785, 11.8965], "rows": 3, "until": 1}, {"a": [51.2560, 11.8275], "b": [51.2800, 11.8275], "rows": 3, "until": 0}],
}
json.dump(out, open(os.path.join(HERE, "rossbach.json"), "w"), ensure_ascii=False)
print("rossbach.json", os.path.getsize(os.path.join(HERE, "rossbach.json")) // 1024, "KB")
