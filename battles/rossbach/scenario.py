"""Rossbach, 5 November 1757 (v2, rebuilt the Austerlitz way). See brief.md for sources, choices and confidence.
Positions: the georeferenced French 1:50,000 staff plan ('gal', RMSE 227 m) via gp(x, y) for the lettered positions,
otherwise named places and offsets. Phases 0-9 are 09:00 ... 16:45. Strengths at phase 0 follow Wikipedia (citing Duffy,
Showalter, Redman, Bodart) for army totals and Millar's order of battle for units; per-unit strengths and losses are estimates.
"""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "..", "tools"))
os.chdir(HERE)
from battlekit import Battle, mv
from georef import Georef
gp = Georef(HERE)("gal")

B = Battle("rossbach", HERE)

# ---------------- sources
B.source("gal", "Bataille de Rossbach le 5 novembre 1757, French staff map 1:50,000 (19th century), Bibliothèque nationale de France GE D-1165", "https://commons.wikimedia.org/wiki/File:Bataille_de_Rossbach_le_5_novembre_1757_-_btv1b8440065h.jpg", "georeferenced (RMSE 227 m); lettered positions: camps, the Prussian march, Moller's battery (L), Seydlitz (N, M), the Prussian line (Q), the Allied columns and rout; army strengths", "staff-map")
B.source("planc", "Plan der Bataille welche den 5. Nov. 1757 ... bey Rossbach in Sachsen geliefert worden (No. 14), contemporary engraving", "https://commons.wikimedia.org/wiki/File:Schlacht_bei_Rosbach-C.jpg", "period plan with lettered legend: Allied camp, St Germain's corps, the Imperial army's march in three columns, the Prussian camp, march and battle position", "period-map")
B.source("plana", "Plan der bey Rosbach ohnweit Weissenfels in Sachsen ... vorgefallenen Bataille (Nuremberg, 1757), contemporary engraving", "https://commons.wikimedia.org/wiki/File:Schlacht_bei_Rosbach-A.jpg", "period plan of the armies' movements", "period-map")
B.source("eb", "C. F. Atkinson, 'Rossbach', Encyclopaedia Britannica, 11th ed. (1911), article and map", "https://en.wikisource.org/wiki/1911_Encyclop%C3%A6dia_Britannica/Rossbach", "camps, plan, march routes, 38 squadrons, Moller at 15:15, rally near Tagewerben, seven battalions engaged", "reference")
B.source("wiki", "Wikipedia: Battle of Rossbach (citing Duffy, Showalter, Redman, Fuller, Bodart, Blanning, Clodfelter)", "https://en.wikipedia.org/wiki/Battle_of_Rossbach", "strengths and losses; minute-by-minute sequence; Seydlitz's two lines (20 + 18 squadrons); the rally between Reichardtswerben and Obschütz; seven squadrons left at Rossbach", "reference")
B.source("millar", "Simon Millar, Rossbach and Leuthen 1757 (Osprey Campaign 113, 2002), bird's-eye plate of Rossbach (consulted as a screenshot supplied by Nathan)", None, "timings 12:00-16:45; order of battle with battalion and squadron counts", "scholarly")
B.source("wpm", "U.S. Military Academy: Battle of Rossbach, maneuver for position, 2-4 November 1757", "https://commons.wikimedia.org/wiki/File:Battle_of_Rossbach_-_Maneuver_for_position,_2-4_November_1757.png", "the armies' positions before the battle", "staff-map")
B.source("data", "AWS Terrain Tiles (elevation); OpenStreetMap place nodes, Overpass (mining pits, spoil heaps), Wikidata and Wikipedia (place identification)", "https://registry.opendata.aws/terrain-tiles/", "terrain, villages and modern ground changes", "data")

# ---------------- meta
B.meta = {
    "title": "Rossbach", "year": "1757", "era": "early-modern", "war": "Seven Years' War",
    "eyebrow": "5 November 1757 · Saxony · Seven Years' War",
    "subtitle": "Frederick the Great against the French and the army of the Holy Roman Empire, in ninety minutes.",
    "sides": {
        "pr": {"name": "Prussian", "top": "#2b4f93", "side": "#1d3767", "mark": "#f3efe4", "arrow": "#3c6fd8", "flag": "#1f1f1f"},
        "fr": {"name": "French", "top": "#f1ede2", "side": "#b9b3a4", "mark": "#1d2a44", "arrow": "#fbfaf5", "chart": "#8a7f6c"},
        "re": {"name": "Reichsarmee / Austrian", "top": "#b5432f", "side": "#7f2d20", "mark": "#f6f1e6", "arrow": "#d4513a"},
    },
    "belligerents": [
        {"name": "Prussian army", "short": "Prussians", "commander": "Frederick II", "sides": ["pr"], "code": "letters"},
        {"name": "Allied army", "short": "Allies", "commander": "Soubise & Hildburghausen", "sides": ["fr", "re"], "code": "numbers"},
    ],
    "forces": {
        "start": [{"label": "Prussians", "n": 22000, "segs": [["pr", 1]]}, {"label": "Allies", "n": 41100, "segs": [["fr", 0.73], ["re", 0.27]]}],
        "end": [{"label": "Prussians", "n": 550, "segs": [["pr", 1]]}, {"label": "Allies", "n": 10150, "segs": [["fr", 0.65], ["re", 0.35]]}],
    },
    "sun": {"lat": 51.25, "decl": -15.6, "note": "Sunset about 16:40 local solar time."},
    "wind": 270, "view": {"az": -0.32, "el": 0.72}, "unitLabelDist": 10,
    "ground": {"season": "autumn", "relief": 70},
    "strengthNote": "Army totals from Wikipedia (Duffy; Bodart); unit strengths are estimates from the battalion and squadron counts in Millar's order of battle (about 630 men per Prussian battalion, 500 per Allied battalion, 115-120 per squadron). Losses are spread across units following the narrative.",
    "method": "Unit positions follow the lettered positions of a 19th-century French 1:50,000 staff plan of the battle, georeferenced against fourteen villages (RMSE 227 m), checked against two contemporary plans of 1757 and the 1911 Britannica map. Times come from Millar and from Wikipedia's account (Duffy, Showalter, Redman); the order of battle from Millar. Village positions were taken from OpenStreetMap settlement nodes and cross-checked with Wikidata; the open-cast mines, flooded pits and spoil heaps that now cover parts of the field were detected automatically and smoothed out, and the Janus and Pölzen hills restored from the period plan.",
    "notes": "The v1 map placed Reichardtswerben 1.3 km and Tagewerben 1.7 km too far north-east (a geocoding error caught by the new gazetteer); everything around them has moved. Heights are exaggerated about three times; roads and woods are illustrative; the wind for drifting smoke is assumed.",
}

# ---------------- places and ground
for hist, key in [("Rossbach", "Roßbach"), ("Schortau", None), ("Leiha", None), ("Almsdorf", None), ("Gröst", None), ("Branderoda", None),
                  ("Mücheln", None), ("Zeuchfeld", None), ("Pettstädt", None), ("Lunstädt", None), ("Reichardtswerben", None), ("Tagewerben", None),
                  ("Posendorf", None), ("Obschütz", None), ("Storkau", None), ("Burgwerben", None), ("Großkayna", None), ("Krumpa", None)]:
    B.place(hist, B.geo[key or hist])
B.place("Bedra", gp(977, 643)); B.place("Braunsdorf", gp(1140, 647)); B.place("Nahlendorf", gp(1068, 995), size=0.5)
B.hill("Janus Hill", (51.2710, 11.9370)); B.hill("Pölzen Hill", (51.2724, 11.9724))
B.hill("Schortau heights", gp(700, 680)); B.hill("Galgenberg", (51.2525, 11.8640))
B.roads = [["Branderoda", "Gröst", "Almsdorf", "Leiha", "Rossbach", "Lunstädt", "Reichardtswerben", "Tagewerben", "Burgwerben"],
           ["Zeuchfeld", "Pettstädt", "Storkau", "Obschütz"], ["Pettstädt", "Reichardtswerben"], ["Schortau", "Leiha"], ["Schortau", "Bedra", "Braunsdorf"],
           ["Rossbach", "Bedra"], ["Reichardtswerben", "Großkayna"], ["Storkau", "Tagewerben"], ["Gröst", "Zeuchfeld"], ["Rossbach", "Pettstädt"],
           ["Mücheln", "Branderoda"], ["Reichardtswerben", "Posendorf"]]
B.woods = [[*gp(300, 760), 420, 300], [*gp(430, 1150), 300, 380], [*gp(905, 1320), 280, 160]]
P = lambda pts: [list(gp(x, y)) for x, y in pts]
B.water["rivers"] = [{"p": P([(600, 835), (700, 838), (780, 835), (845, 833), (860, 780), (872, 700)]), "w": 2, "ford": True},
                     {"p": P([(470, 690), (600, 690), (760, 690), (872, 700), (920, 660), (980, 652), (1060, 648), (1140, 648), (1230, 680), (1300, 700)]), "w": 2, "ford": True}]
B.water["labels"] = {"Geisel": gp(1060, 640)}
B.overlay("gal", "French staff map of the battle (1:50,000)", "overlay_gal.webp", "period", 0.9,
          "19th-century French staff plan of the battle with lettered positions, warped onto the terrain (14 villages, RMSE 227 m).")
B.camps = [{"a": [51.2625, 11.8975], "b": [51.2770, 11.8975], "rows": 3, "until": 1}, {"a": [51.2680, 11.8150], "b": [51.2960, 11.8150], "rows": 3, "until": 0}]

# ---------------- units
def U(uid, side, typ, name, strength, frontage, keys, note, conf, men, cite, via=None, **kw):
    u = B.unit(uid, side, typ, name, strength, frontage, note=note, conf=conf, cite=cite, men=men, **kw)
    for ph, (pos, f, form) in keys.items():
        u.at(ph, pos, f, form, via=(via or {}).get(ph))

# Prussian infantry. Camp line along the Rossbach-Bedra road facing west [eb] [gal F]; the march behind the Janus [gal P];
# the echelon line Q on the plan, left (south-east) leading, facing south-west [gal] [wiki].
QN, QS = gp(1125, 1020), gp(1225, 1170)
def qline(i, n=5, back=0, fwd=0):  # i=0 is the left (south-east) end
    lat = QS[0] + (QN[0] - QS[0]) * i / (n - 1); lon = QS[1] + (QN[1] - QS[1]) * i / (n - 1)
    p = mv((lat, lon), 35, back + i * 110)  # echelon: each group a little further back
    return mv(p, 215, fwd)
camp = lambda i: (51.2632 + i * 0.0029, 11.8935)
march2 = lambda i: mv(gp(1080, 840), 275, i * 420)
march3 = lambda i: mv((51.2735, 11.9290), 285, i * 520)
pi = [("pi1", "Grenadier battalions (Kremzow, Heyden, Wedell)", "3 bns", 1890, -60),
      ("pi2", "Garde & Garde Grenadier battalion", "3 bns", 1890, -50),
      ("pi3", "Itzenplitz & Forcade", "4 bns", 2520, -40),
      ("pi4", "Jung-Kleist & Alt-Braunschweig", "4 bns", 2520, -20),
      ("pi5", "Winterfeldt & Goltz", "4 bns", 2520, -10)]
for i, (uid, nm, bns, m0, loss) in enumerate(pi):
    U(uid, "pr", "inf", nm, f"First line · {bns} [millar]", 650,
      {0: (camp(i), 270, "X"), 2: (march2(i), 95, "C"), 3: (qline(i, back=1250), 125, "C"), 4: (qline(i, back=550), 215, "L"),
       5: (qline(i, back=300), 215, "L"), 6: (qline(i), 215, "F"), 7: (qline(i, fwd=180), 215, "F"), 8: (qline(i, fwd=520), 215, "L")},
      "One of the battalions of Prince Henry's line; only about seven Prussian battalions actually fired [wiki] [eb]." if i < 2 else "Part of the Prussian line that formed on the slope west of the Janus; it barely engaged [wiki].",
      "medium", {0: m0, 6: m0 + loss // 2, 8: m0 + loss}, ["gal", "millar", "wiki", "eb"], via={2: [gp(990, 830)]})
for i, (uid, nm, bns, m0) in enumerate([("pj1", "Markgraf Karl & Meyerinck", "4 bns", 2520), ("pj2", "Hülsen & grenadiers (Jung-Billerbeck, Börnstädt, Lubath)", "4 bns", 2520)]):
    U(uid, "pr", "inf", nm, f"Second line · {bns} [millar]", 600,
      {0: ((51.2650 + i * 0.006, 11.9015), 270, "X"), 2: (mv(march2(i), 0, 400), 95, "C"), 3: (mv(qline(i * 3, back=1250), 35, 450), 125, "C"),
       4: (mv(qline(i * 3, back=550), 35, 450), 215, "L"), 6: (mv(qline(i * 3), 35, 500), 215, "L"), 8: (mv(qline(i * 3, fwd=520), 35, 500), 215, "L")},
      "Reserve line; these battalions never fired a shot [wiki].", "medium", {0: m0}, ["millar", "wiki", "gal"])
U("pmo", "pr", "art", "Moller's battery", "18 heavy guns [eb] [wiki]", 260,
  {0: ((51.2690, 11.8985), 270, "X"), 2: (gp(1250, 860), 95, "C"), 3: (gp(1365, 945), 215, "F"), 8: (mv(gp(1365, 945), 215, 700), 215, "F"), 9: (mv(gp(1365, 945), 215, 700), 215, "L")},
  "Colonel von Moller's 18 heavy guns, posted on the reverse of the Janus between the infantry and the cavalry, opened at 15:15 [wiki] [eb]; siege guns from Leipzig joined later [wiki]. Marked L on the French plan [gal].",
  "high", {0: 18}, ["gal", "eb", "wiki"])
cav = [("pc1", "Garde du Corps & Gendarmes", "8 sqns", 920, "First line of the charge (20 squadrons) [wiki]."),
       ("pc2", "Leib & Seydlitz Cuirassiers", "10 sqns", 1150, "First line of the charge [wiki]."),
       ("pc3", "Czettritz & Meinicke Dragoons", "10 sqns", 1150, "Second line (18 squadrons), sent in once the first line was locked in the melee [wiki]."),
       ("pc4", "Driesen Cuirassiers", "5 sqns", 575, "Second line [wiki]."),
       ("ph1", "Szekely Hussars", "5 sqns with Seydlitz", 575, "Light horse with Seydlitz's second line; the rest of the hussars stayed at Rossbach [wiki].")]
N1 = [gp(1440, 915), gp(1545, 985)]; N2 = [gp(1420, 940), gp(1520, 1005)]
line_pt = (lambda L, t: (L[0][0] + (L[1][0] - L[0][0]) * t, L[0][1] + (L[1][1] - L[0][1]) * t))
rally = (51.2385, 11.9440)
for i, (uid, nm, sq, m0, note) in enumerate(cav):
    first = i < 2
    pos3 = line_pt(N1 if first else N2, 0.25 + 0.5 * (i % 2 if first else (i - 2) / 2))
    clash = mv((51.2555, 11.9470), 215 if first else 250, (0 if first else 250) + i * 180)
    U(uid, "pr", "lc" if uid == "ph1" else "cav", nm, f"{sq} [millar]", 420,
      {0: ((51.2630 + i * 0.0035, 11.9085), 270, "X"), 2: (mv((51.2745, 11.9300), 90, i * 700), 95, "C"), 3: (pos3, 215, "L"),
       4: (clash if first else mv(pos3, 215, 500), 215, "L"), 5: (mv(rally, 90 * i, 260), 300, "L"), 6: (mv(rally, 90 * i, 220), 310, "L"),
       7: (mv((51.2450, 11.9300), 120, i * 220), 300, "L"), 8: (mv((51.2370, 11.9150), 120, i * 260), 225, "L")},
      note, "medium", {0: m0, 4: m0 - 40, 7: m0 - 70, 8: m0 - 80}, ["gal", "wiki", "millar", "eb"],
      via={3: [mv((51.2765, 11.9480), 90, i * 150)], 5: [mv(rally, 0, 900)], 7: [mv((51.2420, 11.9380), 0, 0)]})
U("pfb", "pr", "lt", "Flank guard: Frei-Bataillon Mayr & hussars", "1 bn and 7 squadrons [wiki] [millar]", 300,
  {0: ((51.2670, 11.8840), 270, "L"), 7: ((51.2670, 11.8840), 270, "L"), 8: ((51.2600, 11.8780), 240, "L")},
  "Light troops and seven squadrons left at Rossbach to watch Saint-Germain's advanced post [wiki].", "medium", {0: 1230}, ["wiki", "millar"])

# Allies. Camp between Branderoda and Mücheln facing east [wiki] [eb]; St Germain on the Schortau heights and the Galgenberg [wiki] [eb];
# the march by Zeuchfeld towards Pettstädt and Reichardtswerben in three columns [wiki] [planc]; the column heads and the rout [gal].
heads = gp(1175, 1225); headsW = gp(1050, 1215)
def col(i, base, face):  # i: 0 first line (left column), 1 second line (right), 2 reserve (further right)
    return mv(base, face + 90, i * 330)
fr_inf = [("fi1", "Piémont & Mailly (head of the column)", "8 bns", 4000, 0, "The French regiments at the head of the march [wiki]; they tried a bayonet attack in column and were shot down [wiki] [eb]."),
          ("fi2", "Poitou, Provence, St-Chamond & La Marck", "8 bns", 4000, 1, "French line regiments of the main columns [millar]."),
          ("fi3", "French first and second lines (other regiments)", "≈11 bns", 5500, 0, "The rest of the French main columns, lost all order in the attempted wheel to the east [wiki]."),
          ("fi4", "French reserve corps (Broglie)", "≈8 bns", 4000, 2, "The foot reserve marching on the right; part of it got wedged between the main columns [wiki].")]
re_inf = [("ri1", "Reichsarmee infantry (Franconian regiments)", "≈8 bns", 4000, 1, "Three Franconian Imperial regiments threw down their muskets and ran when Seydlitz struck [wiki]."),
          ("ri2", "Reichsarmee infantry (Blau-Würzburg, Hessen-Darmstadt, Kur-Trier)", "≈8 bns", 4000, 2, "Imperial contingents named in Millar's order of battle [millar].")]
loss = {"fi1": 1800, "fi2": 1200, "fi3": 1000, "fi4": 600, "ri1": 1500, "ri2": 1000}
for k, (uid, nm, bns, m0, c, note) in enumerate(fr_inf + re_inf):
    side = "fr" if uid.startswith("f") else "re"
    off = k * 0.0045
    L = loss[uid]
    U(uid, side, "inf", nm, f"{bns} [millar]", 650,
      {0: ((51.2700 + off, 11.8190 - (0.008 if k % 2 else 0)), 90, "X"), 1: (mv(col(c, (51.2560 - k * 0.0028, 11.8290), 180), 0, 0), 180, "C"),
       2: (mv(col(c, (51.2385, 11.8600 - k * 0.006), 75), 0, 0), 75, "C"), 3: (mv(col(c, mv(heads, 250, 2500 + k * 380), 60), 0, 0), 60, "C"),
       4: (mv(col(c, mv(heads, 250, 1700 + k * 380), 55), 0, 0), 55, "C"), 5: (mv(col(c, mv(heads, 250, 900 + k * 380), 50), 0, 0), 50, "C"),
       6: (mv(col(c, heads if k == 0 else mv(heads, 250, 350 + k * 330), 40), 0, 0), 40, "F" if k == 0 else "C"),
       7: (mv(col(c, heads if k == 0 else mv(heads, 250, 350 + k * 330), 40), 0, 0), 40, "F" if k < 2 else "R" if uid == "ri1" else "C"),
       8: (mv(gp(1145, 1320), 240, 300 + k * 350), 225, "R"), 9: (mv(gp(1145, 1320), 235, 1700 + k * 350), 230, "R")},
      note, "medium", {0: m0, 6: m0 - L // 6, 7: m0 - L // 2, 8: m0 - L * 4 // 5, 9: m0 - L}, ["gal", "wiki", "millar", "planc"],
      via={1: [(51.2620 - k * 0.002, 11.8250)], 2: [(51.2355, 11.8300 + 0.0 * k)]})
U("fart", "fr", "art", "Allied reserve artillery", "French & Imperial guns", 240,
  {0: ((51.2790, 11.8300), 90, "X"), 1: ((51.2580, 11.8300), 180, "C"), 2: ((51.2390, 11.8540), 75, "C"), 3: ((51.2420, 11.8950), 50, "C"),
   5: ((51.2450, 11.9080), 45, "C"), 6: (mv(heads, 225, 900), 40, "F"), 8: (mv(heads, 225, 900), 40, "R")},
  "Marched between the two main columns, where it could not deploy [wiki]; the Prussians took 72 guns [wiki].", "medium", {0: 30, 8: 12}, ["wiki"])
ac = [("ac1", "re", "Austrian cuirassiers (Bretlach, Trautmannsdorf)", "14 sqns [millar]", 1700, 700, "At the head of the right column, they deployed and met Seydlitz's first line [wiki]."),
      ("ac2", "re", "Reichsarmee cavalry", "19 sqns [millar]", 2300, 900, "Imperial horse on the flank of the right column [wiki]."),
      ("ac3", "fr", "French cavalry of the right wing", "≈20 sqns [millar]", 2400, 900, "FitzJames, Bourbon-Busset, La Reine and others, hurried forward in what they thought was a pursuit [wiki]."),
      ("ac4", "fr", "French reserve & left-wing cavalry", "≈22 sqns [wiki]", 2600, 400, "Ten squadrons in reserve and twelve guarding the left flank; some were called forward for the 'pursuit' [wiki].")]
for k, (uid, side, nm, sq, m0, L, note) in enumerate(ac):
    U(uid, side, "cav", nm, sq, 450,
      {0: ((51.2560 - k * 0.0035, 11.8165), 90, "X"), 1: ((51.2400 + 0.0015 * k, 11.8330 + 0.004 * k), 120, "C"),
       2: ((51.2415 + 0.001 * k, 11.8930 - 0.009 * k), 65, "C"), 3: (mv((51.2530, 11.9420), 225, k * 420), 45, "C"),
       4: (mv((51.2540, 11.9455), 225, k * 360), 45, "L" if k < 2 else "C"), 5: (mv((51.2390, 11.9590), 250, k * 500), 195, "R"),
       6: (mv((51.2300, 11.9550), 250, k * 500), 210, "R"), 8: (mv((51.2220, 11.9400), 250, k * 600), 225, "R")},
      note, "medium" if k < 3 else "low", {0: m0, 4: m0 - L // 3, 5: m0 - L * 3 // 4, 8: m0 - L}, ["wiki", "millar", "gal"])
U("sg", "fr", "inf", "Saint-Germain's corps", "Touraine, Condé, La Marine (8 bns) & horse [millar]", 900,
  {0: (gp(700, 680), 90, "L"), 6: (gp(700, 680), 90, "L"), 7: (mv(gp(700, 680), 175, 950), 175, "C"), 8: (mv(gp(700, 680), 175, 1900), 165, "C"), 9: (gp(605, 1000), 75, "L")},
  "The Allied advanced post on the Schortau heights, which overlooked the Prussian camp [wiki]; at dusk it covered the retreat (H on the French plan) [gal] [millar].", "medium",
  {0: 5400, 9: 5300}, ["wiki", "gal", "millar", "eb"])
U("lou", "re", "lt", "Loudon's light troops", "Croats & hussars [millar]", 360,
  {0: ((51.2525, 11.8640), 90, "L"), 7: ((51.2525, 11.8640), 90, "L"), 8: ((51.2440, 11.8720), 120, "C"), 9: ((51.2390, 11.8790), 70, "L")},
  "Austrian light troops on the Galgenberg; with Saint-Germain they covered the withdrawal at 16:45 [millar].", "low", {0: 1800, 9: 1750}, ["millar", "eb"])

# ---------------- commanders
B.commander("fred", "pr", "Frederick II", {0: "Rossbach", 2: (51.2725, 11.9200), 3: (51.2700, 11.9330), 8: (51.2560, 11.9250)},
            "Watched the Allied march from the roof of the Goldacker manor house at Rossbach [wiki].")
B.commander("soub", "fr", "Soubise & Hildburghausen", {0: (51.2800, 11.8200), 1: (51.2560, 11.8310), 2: (51.2400, 11.8650), 3: (51.2420, 11.8930),
            5: (51.2440, 11.9050), 8: (51.2330, 11.8880), 9: (51.2270, 11.8760)}, "The two allied commanders shared command and disagreed throughout [wiki].")

# ---------------- phases
A = B.arrow
B.phase("09:00", "Morning", "Two camps, six kilometres apart",
        "Frederick's army of about 22,000 is camped between Rossbach on the left and Bedra on the right, facing west [wiki] [eb]. About 41,000 French and Imperial troops under the Prince de Soubise and the Prince of Saxe-Hildburghausen hold the heights from Branderoda to Mücheln, with Saint-Germain's advanced post on the Schortau heights overlooking the Prussian camp [wiki]. The Allies decide to march round the Prussian left and get between Frederick and the Saale crossings [wiki] [eb].",
        ("Turning movement", "Marching around an enemy's flank to threaten his line of retreat. It needs speed and good scouting, and the Allies had neither [wiki].", "turning-movement"),
        (51.2700, 11.8700), 13, conf="high", cite=["wiki", "eb", "gal", "planc"],
        events=[("Rossbach", "Frederick's headquarters in the Goldacker manor", ["wiki"]), (gp(700, 680), "Saint-Germain's post overlooks the Prussian camp", ["wiki"])])
B.phase("12:00", "Allies march", "The allied army sets off south",
        "Late in the morning the Allied columns begin a long march south towards Zeuchfeld, cavalry in the lead [millar] [wiki]. Saint-Germain stays on the heights to hold the Prussians' attention [wiki]. Frederick, watching from the roof of the Rossbach manor, at first takes the movement for a retreat towards the magazines at Freyburg; at about noon he goes to dinner, leaving Captain Gaudi on the roof [wiki].",
        ("Fixing force", "Saint-Germain's corps was meant to hold the Prussians in place while the main army marched round them. It never fought [wiki].", "fixing-force"),
        (51.2560, 11.8520), 11, conf="medium", cite=["millar", "wiki", "planc"],
        debate="Wikipedia's account has the Allies leaving camp 'after eleven' [wiki]; Millar's plate puts the start of the march at 12:00 [millar]. The map shows noon.",
        arrows=[A("fr", "move", (51.2620, 11.8250), (51.2480, 11.8270), (51.2370, 11.8330), (51.2360, 11.8520))],
        events=[(gp(700, 680), "Saint-Germain stays to pin the Prussians", ["wiki"]), ((51.2380, 11.8380), "Cavalry vanguard turns east by Zeuchfeld", ["wiki", "eb"])])
B.phase("14:30", "Prussians move", "Frederick strikes camp",
        "Gaudi reports the Allied columns turning east past Zeuchfeld; when Frederick sees hostile cavalry and infantry already approaching Pettstädt, he understands they mean to take him in flank and rear [wiki]. By 15:00 the camp is struck and the army in column [wiki]. Seydlitz takes all 38 squadrons east behind the Janus and Pölzen hills, hidden from view, with Moller's 18 guns following [wiki] [eb]. Seeing the tents fall, the Allies conclude the Prussians are retreating and hurry on [wiki].",
        ("Using dead ground", "The Prussians moved along the far side of a low ridge, so the Allies could not see where they were going [wiki].", "dead-ground"),
        (51.2560, 11.8950), 11, conf="high", cite=["wiki", "eb", "gal"],
        arrows=[A("fr", "move", (51.2360, 11.8450), (51.2385, 11.8700), (51.2420, 11.8950), (51.2500, 11.9250), (51.2560, 11.9420)),
                A("pr", "move", gp(990, 840), gp(1080, 840), gp(1350, 880)), A("pr", "move", (51.2710, 11.9100), (51.2760, 11.9350), (51.2765, 11.9550))],
        events=[(gp(985, 780), "Camp struck in minutes", ["wiki"]), ((51.2400, 11.8650), "The Allies hurry to cut off a 'retreat'", ["wiki"])])
B.phase("15:15", "Guns open", "Moller's battery opens fire",
        "Moller's 18 heavy guns open from the Janus on the Allied cavalry, now north of Reichardtswerben and far ahead of its own infantry [wiki] [eb]. The Allied commanders take the cannonade for the cover of a retreat and press on, and their columns, attempting a wheel to the east, lose all order [wiki]. Behind the Pölzen, Seydlitz forms two lines, 20 squadrons and 18, out of sight [wiki] [gal].",
        ("Massed artillery", "Heavy guns on high ground firing into troops packed in columns did terrible damage, and covered the hidden cavalry's approach [wiki].", "massed-artillery"),
        (51.2590, 11.9300), 7.5, conf="medium", cite=["wiki", "eb", "gal"],
        arrows=[A("pr", "fire", gp(1365, 945), (51.2560, 11.9440)), A("pr", "fire", gp(1365, 945), (51.2470, 11.9200)),
                A("fr", "move", (51.2440, 11.9050), (51.2510, 11.9280), (51.2550, 11.9420))],
        events=[(gp(1365, 945), "18 guns on the Janus (L on the French plan)", ["gal", "wiki"]), (line_pt(N1, 0.5), "Seydlitz forms two lines behind the Pölzen (N)", ["gal", "wiki"])])
B.phase("15:30", "Seydlitz charges", "Seydlitz's charge",
        "At 15:30 Seydlitz brings his first 20 squadrons over the Pölzen at the gallop, knee to knee, into the Allied cavalry still strung out in column [wiki]. The Austrian cuirassiers manage to deploy and meet him; Seydlitz is wounded in the melee and sends in his other 18 squadrons, which strike the French horse at an angle [wiki]. Within about half an hour the Allied cavalry is broken [wiki] [eb].",
        ("Shock cavalry", "Heavy cavalry charging in close order at the gallop hits like a wall. Seydlitz trained his men to keep formation at speed, which few cavalry of the time could do [wiki].", "shock-cavalry"),
        (51.2580, 11.9450), 5.6, conf="medium", cite=["wiki", "eb", "gal"],
        arrows=[A("pr", "charge", line_pt(N1, 0.4), gp(1370, 1045), (51.2560, 11.9480)), A("pr", "charge", line_pt(N2, 0.5), gp(1395, 1080), (51.2530, 11.9500))],
        events=[((51.2550, 11.9470), "Cavalry clash north of Reichardtswerben (M)", ["gal", "wiki"])])
B.phase("15:45", "Cavalry routed", "The Allied cavalry breaks",
        "The melee drifts south past the Allied infantry and the Allied horse streams away [wiki]. Instead of chasing it off the field, Seydlitz recalls his squadrons and rallies them in a copse about 2 km away, between Reichardtswerben and Obschütz, on the Allied flank and rear [wiki]. On the slope west of the Janus the Prussian infantry forms in echelon [wiki] [gal].",
        ("Rally and re-form", "Horses and riders are blown after a charge, and scattered cavalry is useless. Rallying quickly gave Seydlitz a formed force to strike again [wiki].", "rally-reform"),
        (51.2480, 11.9450), 6.4, conf="low", cite=["wiki", "eb"],
        debate="Accounts differ on where Seydlitz rallied: Wikipedia, following Redman, puts it in a copse between Reichardtswerben and Obschütz [wiki]; the 1911 Britannica says near Tagewerben [eb]. The map places it between the two.",
        arrows=[A("re", "retreat", (51.2540, 11.9460), (51.2440, 11.9560), (51.2320, 11.9550)), A("pr", "move", (51.2520, 11.9480), (51.2460, 11.9500), rally)],
        events=[(rally, "Seydlitz rallies his squadrons", ["wiki", "eb"])])
B.phase("16:00", "Infantry fight", "The Prussian infantry advances in echelon",
        "The Allied infantry, freed of the cavalry, turns on the Prussian infantry threatening its left: about four battalions in line [wiki]. Instead of deploying, the Allied battalions form columns and advance with the bayonet, led by Piémont and Mailly [wiki] [eb]. Prince Henry's volleys and Moller's guns shred them; only about seven Prussian battalions fire at all, five to fifteen rounds a man [wiki] [eb].",
        ("Echelon attack", "In an echelon each unit is set back from the one beside it, so the line meets the enemy one unit at a time from its strong end [wiki].", "echelon"),
        (51.2500, 11.9300), 5.2, conf="medium", cite=["wiki", "eb", "gal"],
        arrows=[A("pr", "fire", qline(0), mv(qline(0), 215, 420)), A("pr", "fire", qline(1), mv(qline(1), 215, 450)), A("fr", "charge", mv(heads, 220, 400), heads)],
        events=[(heads, "French columns attack with the bayonet", ["wiki", "eb"]), (qline(1), "Prince Henry's volleys (Q on the French plan)", ["gal", "wiki"])])
B.phase("16:15", "Second charge", "Seydlitz strikes the infantry",
        "With the Allied infantry held by fire from the front, Seydlitz brings all 38 squadrons in against its flank and rear [wiki] [millar]. Three Franconian Imperial regiments throw down their muskets and run, and the French run with them [wiki].",
        ("Combined arms", "Infantry fire held the enemy in front while cavalry struck the flank. Neither alone would have broken the Allied army so fast [wiki].", "combined-arms"),
        (51.2450, 11.9300), 5.6, conf="medium", cite=["wiki", "millar"],
        arrows=[A("pr", "charge", rally, (51.2425, 11.9360), (51.2450, 11.9290)), A("pr", "charge", mv(rally, 90, 400), (51.2410, 11.9330), (51.2420, 11.9230))],
        events=[((51.2440, 11.9300), "Seydlitz's second charge, all 38 squadrons", ["wiki"])])
B.phase("16:30", "Rout", "The Allied army dissolves",
        "The Allied army breaks and flees south-west, past Pettstädt, Storkau and Obschütz, abandoning its guns [wiki] [gal]. Seydlitz's troopers pursue until darkness makes it impossible [wiki]. Saint-Germain finally marches south from the heights to cover the retreat [millar].",
        ("Pursuit", "A beaten army is most vulnerable in flight. Darkness on a November afternoon saved most of the Allied army [wiki].", "pursuit"),
        (51.2410, 11.9100), 7.4, conf="medium", cite=["wiki", "gal", "millar"],
        arrows=[A("fr", "retreat", (51.2460, 11.9250), gp(1145, 1320), (51.2290, 11.9050)), A("fr", "retreat", (51.2430, 11.9150), (51.2350, 11.9000), (51.2270, 11.8900)),
                A("re", "retreat", (51.2420, 11.9080), (51.2330, 11.8870), (51.2240, 11.8780)), A("fr", "move", gp(700, 680), mv(gp(700, 680), 175, 1900), gp(605, 1000))],
        events=[(gp(1145, 1320), "Rout to the south-west (S and O on the French plan)", ["gal"]), ((51.2420, 11.9100), "Guns and baggage abandoned", ["wiki"])])
B.phase("16:45", "Nightfall", "Saint-Germain and Loudon cover the withdrawal",
        "Saint-Germain's corps and Loudon's light troops cover the retreat as darkness falls [millar] [gal]. The battle has lasted about ninety minutes [wiki] [eb]. The Prussians have lost roughly 550 men; the Allies about 10,000 (some 6,600 French and 3,550 Imperial), about half of them prisoners, with 72 guns and 21 standards taken [wiki].",
        ("Rearguard", "Fresh troops at the rear slow a pursuer and let a beaten army escape; here the coming of night mattered more [wiki].", "rearguard"),
        (51.2380, 11.8920), 8.4, conf="high", cite=["wiki", "eb", "millar", "gal"],
        debate="Prussian losses are disputed: Frederick claimed almost none; Bodart counted about 170 dead and 430 wounded; studies of regimental records give fewer still [wiki].",
        arrows=[A("fr", "retreat", (51.2290, 11.8920), (51.2260, 11.8700), (51.2250, 11.8450)), A("re", "retreat", (51.2220, 11.8800), (51.2200, 11.8600))],
        events=[(gp(605, 1000), "Rearguard (H on the French plan)", ["gal", "millar"])])

B.export()
