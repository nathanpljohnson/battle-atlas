"""Leuthen, 5 December 1757. See brief.md for sources, choices and confidence.
Positions: the georeferenced 1:25,000 plans of the 1904 Prussian General Staff history, gA(x, y) = Plan 12A (to 15:00),
gB(x, y) = Plan 12B (15:00 to the end); pixel coordinates are in the 4000 px scans in sources/. Phases 0-11 are 07:30 ... 18:00.
Strengths follow the General Staff's orders of battle and army totals (35,000 Prussians, 65,000 Austrians); unit strengths
and the losses per phase are estimates spread from the sourced totals.
"""
import math, os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "..", "tools"))
os.chdir(HERE)
from battlekit import Battle, mv
from georef import Georef
G = Georef(HERE)
gA, gB, g24 = G("gs12a"), G("gs12b"), G("gs1824")

B = Battle("leuthen", HERE)

# ---------------- sources
B.source("kriemann", "Hans-Peter Kriemann, Die Schlacht von Leuthen (ZMSBw, 2 December 2022)", "https://zms.bundeswehr.de/de/mediathek/die-schlacht-von-leuthen-1757-5535676", "modern institutional cross-check of terrain, attack timing and final cavalry action; differs on Borne command and opening battery position; see brief", "reference")
B.source("gs1904", "Großer Generalstab, Die Kriege Friedrichs des Großen, III. Teil: Der Siebenjährige Krieg 1756-1763, Bd. 6: Leuthen (Berlin, 1904)", "https://archive.org/details/diekriegefriedrit3b6prus", "official history from the Prussian, Austrian, Bavarian, Württemberg, Saxon and French archives: times, strengths, both orders of battle, the march, the attack, losses; appendices correcting earlier accounts", "official-history")
B.source("gs12a", "Plan 12A of the same volume (1:25,000): both sides' positions in the night of 4-5 December and the fighting against the Austrian left until about 15:00", "https://archive.org/details/diekriegefriedrit3b6prus", "georeferenced (27 villages, RMSE 241 m); regiment-by-regiment positions; the Austrian dispositions follow the Walter-Wiercker plan in the Vienna Kriegsarchiv", "staff-map")
B.source("gs12b", "Plan 12B of the same volume (1:25,000): the fighting from 15:00 to the end", "https://archive.org/details/diekriegefriedrit3b6prus", "georeferenced (19 villages, RMSE 193 m); the line south of Leuthen, the Austrian front after the wheel, Lucchesi's and Driesen's charges, the end position", "staff-map")
B.source("gs1824", "Schlacht bei Leuthen am 5ten December 1757 (1:50,000), from the Prussian General Staff's Geschichte des siebenjährigen Krieges (Berlin, 1824-47), SLUB Dresden", "https://commons.wikimedia.org/wiki/File:Schlacht_bei_Leuthen_am_5ten_December_1757.jpg", "georeferenced (RMSE 242 m); lettered positions after Gaudi, with the Austrian line drawn on its night-camp position", "staff-map")
B.source("beaulieu", "[Major] de Beaulieu, Plan de la bataille près de Leuthen en Silésie le 5 décembre 1757 entre l'armée impériale et royale et l'armée prussienne (Vienna: Trattner, 1757), BnF GE D-13585", "https://commons.wikimedia.org/wiki/File:Plan_de_la_bataille_pr%C3%A8s_de_Leuthen_en_Sil%C3%A9sie_le_5_d%C3%A9cembre_1757_entre_l%27arm%C3%A9e_imp%C3%A9riale_et_royale_et_l%27arm%C3%A9e_prussienne_-_par..._de_Beaulieu..._-_btv1b8491666p.jpg", "the Austrian staff's own plan (georeferenced, RMSE 289 m) with a lettered legend: the night position, the advance to the heights, Nádasdy's corps, the cavalry counter-attacks, the reserve's flank", "period-map")
B.source("usma", "Three maps in the style of the U.S. Military Academy atlas: Battle of Leuthen, 'The fix', 'The press', 'The kill' (Wikimedia Commons)", "https://commons.wikimedia.org/wiki/Category:Maps_of_the_Battle_of_Leuthen", "schematic modern maps; phase structure only", "staff-map")
B.source("carlyle", "Thomas Carlyle, History of Friedrich II of Prussia, Book XVIII, ch. X: 'Battle of Leuthen' (1865)", "https://archive.org/details/historyoffriedri027718mbp", "narrative after Tempelhof (an eyewitness), Archenholtz, Retzow, Kutzen and the Prince de Ligne", "reference")
B.source("wiki", "Wikipedia: Battle of Leuthen (citing Duffy 1985 and 2003, Showalter 1996, Redman 2014, Asprey, Blanning, Bodart, Clodfelter)", "https://en.wikipedia.org/wiki/Battle_of_Leuthen", "modern synthesis: strength and loss ranges, the churchyard, Ligne's account, the chorale", "reference")
B.source("data", "AWS Terrain Tiles (elevation); OpenStreetMap (villages, woods, quarries); Wikidata and German Wikipedia (place identification)", "https://registry.opendata.aws/terrain-tiles/", "terrain, villages and modern ground changes", "data")


def brg(a, b):
    a, b = B.pos(a), B.pos(b)
    dy = (b[0] - a[0]) * 111200; dx = (b[1] - a[1]) * 111200 * math.cos(math.radians(a[0]))
    return round(math.degrees(math.atan2(dx, dy)) % 360)


def along(pts, t):
    pts = [B.pos(p) for p in pts]
    seg = [math.dist((p[0], p[1] * 0.63), (q[0], q[1] * 0.63)) for p, q in zip(pts, pts[1:])]
    d = t * sum(seg)
    for (p, q), s in zip(zip(pts, pts[1:]), seg):
        if d <= s:
            f = d / s if s else 0
            return (p[0] + (q[0] - p[0]) * f, p[1] + (q[1] - p[1]) * f)
        d -= s
    return pts[-1]


def lerp(a, b, f):
    a, b = B.pos(a), B.pos(b)
    return (a[0] + (b[0] - a[0]) * f, a[1] + (b[1] - a[1]) * f)


# ---------------- meta
B.meta = {
    "title": "Leuthen", "year": "1757", "era": "early-modern", "war": "Seven Years' War",
    "eyebrow": "5 December 1757 · Silesia · Seven Years' War",
    "subtitle": "Frederick the Great hides his army behind a chain of low rises, falls on the Austrian left in oblique order, and breaks an army nearly twice his size.",
    "sides": {
        "pr": {"name": "Prussian", "top": "#2b4f93", "side": "#1d3767", "mark": "#f3efe4", "arrow": "#3c6fd8", "flag": "#1f1f1f"},
        "au": {"name": "Austrian", "top": "#f1ede2", "side": "#b9b3a4", "mark": "#7a1f1f", "arrow": "#d4513a", "flag": "#e9d27a", "chart": "#8a7f6c"},
        "rc": {"name": "Imperial contingents (Württemberg, Bavaria, Würzburg)", "top": "#7f9cc4", "side": "#566f93", "mark": "#f6f1e6", "arrow": "#e8735a", "chart": "#6f8db8"},
        "sx": {"name": "Saxon", "top": "#b5432f", "side": "#7f2d20", "mark": "#f6f1e6", "arrow": "#e8735a"},
    },
    "belligerents": [
        {"name": "Prussian army", "short": "Prussians", "commander": "Frederick II", "sides": ["pr"], "code": "letters"},
        {"name": "Imperial and Royal army", "short": "Austrians", "commander": "Prince Charles of Lorraine & Daun", "sides": ["au", "rc", "sx"], "code": "numbers"},
    ],
    "forces": {
        "start": [{"label": "Prussians", "n": 35000, "segs": [["pr", 1]]}, {"label": "Austrians", "n": 65000, "segs": [["au", 0.78], ["rc", 0.2], ["sx", 0.02]]}],
        "end": [{"label": "Prussians", "n": 6400, "segs": [["pr", 1]]}, {"label": "Austrians", "n": 22000, "segs": [["au", 0.80], ["rc", 0.16], ["sx", 0.04]]}],
    },
    "sun": {"lat": 51.13, "decl": -22.4, "note": "Sunrise about 07:55, sunset about 16:00 local solar time; dark by about 16:40."},
    "wind": 270, "view": {"az": -0.35, "el": 0.75}, "unitLabelDist": 11,
    "ground": {"season": "winter", "relief": 90},
    "strengthNote": "Army totals from the 1904 General Staff history: 35,000 Prussians in 47½ battalions and 133 squadrons, 65,000 Austrians in 85 battalions and 125 squadrons with about 5,000 light troops [gs1904]. Unit strengths are estimates from those battalion and squadron counts (about 520 men per Prussian battalion and 80 per squadron; 550 per Austrian battalion and 110 per squadron). Losses (Prussian 6,400; Austrian about 22,000, over half of them prisoners) are spread across units following the narrative. Guns are not counted.",
    "method": "Unit positions follow the regiment-by-regiment Plans 12A and 12B of the 1904 Prussian General Staff history, drawn at 1:25,000 on a modern survey and georeferenced against twenty-seven and nineteen villages (RMSE 241 m and 193 m); the Austrian dispositions on them come from the plan drawn for the Vienna Kriegsarchiv just after the battle. They were checked against the Austrian staff's published plan of 1757 and the General Staff's earlier 1:50,000 map. Times and strengths come from the 1904 history's text and appendices, which use the archives of both sides; between the plans, positions are interpolated. Village locations come from OpenStreetMap and Wikidata with the German names resolved by hand; modern woods, which the elevation model shows as 15-20 m hills, have been smoothed out of the ground.",
    "notes": "Per-moment losses are estimates. The Austrian battle line is drawn 1,000-2,000 paces west of the night camp, as the 1904 history and the Austrian plans show; older maps put it on the camp line east of the villages. Positions between 08:30 and 12:30, and after dark, are reconstructed from the narrative. Not shown separately: the grenadier companies and pickets in the villages, the Croats in the Zettelbusch and the woods west of Borne, and the battalion guns. The Kiefernberg south of Sagschütz was wooded in 1757 and is now ploughland; the Leuthen and Rathen woods, the Zettelbusch and the Faulbusch are drawn from the 1904 plans, and the Mittel-Teich at Gross-Gohlau from Plan 12A. Heights are exaggerated about four times; roads are illustrative. The wind for drifting smoke is assumed. No historical-map overlay is offered.",
}

# ---------------- places and ground
for n in ["Leuthen", "Borne", "Nippern", "Frobelwitz", "Guckerwitz", "Sagschütz", "Lobetinz", "Radaxdorf", "Schriegwitz", "Kertschütz",
          "Krampitz", "Rathen", "Saarawenze", "Muckerau", "Stabelwitz", "Goldschmieden", "Romberg", "Lampersdorf", "Kammendorf", "Polkendorf"]:
    B.place(n)
B.place("Gross-Heidau", B.geo["Groß Heidau"]); B.place("Gross-Gohlau", B.geo["Groß Gohlau"])
B.place("Lissa", B.geo["Lissa"], size=1.4)
B.place("Klein-Gohlau", gA(2958, 2200), size=0.5); B.place("Saara", gA(3190, 1190), size=0.5); B.place("Klein-Heidau", gA(3410, 1330), size=0.5)
B.place("Arnoldsmühle", gA(3310, 1715), size=0.4)
B.hill("Schönberg", gB(2190, 1095)); B.hill("Butterberg", gA(2215, 1418)); B.hill("Sophienberg", gA(1880, 1535)); B.hill("Schleierberg", gA(1945, 1305))
B.hill("Heideberg", gA(1747, 1760)); B.hill("Wachberg", gA(1863, 1799)); B.hill("Judenberg", gA(2360, 1765)); B.hill("Glanzberg", gB(2435, 1958))
B.hill("Kiefernberg", gB(2483, 1896)); B.hill("Kirchberg", gA(2670, 1868)); B.hill("Gohlauer Berg", gB(2910, 1760)); B.hill("Breslauer Berg", gB(2750, 1121))
B.hill("Windmill height", gA(2530, 1372))
B.roads = [["Kammendorf", gA(1280, 1000), "Borne", "Gross-Heidau", gA(2560, 1110), "Saara", "Lissa"],
           ["Borne", "Radaxdorf", "Lobetinz", "Kertschütz"], ["Leuthen", "Radaxdorf"], ["Leuthen", "Sagschütz", "Schriegwitz", "Kertschütz"],
           ["Leuthen", "Frobelwitz", "Guckerwitz", "Nippern"], ["Lobetinz", "Schriegwitz"], ["Sagschütz", "Gross-Gohlau", "Romberg"],
           ["Leuthen", gA(2950, 1520), "Rathen", gA(3600, 1330), "Lissa"], ["Guckerwitz", "Krampitz", "Saarawenze", "Muckerau"],
           ["Gross-Heidau", "Nippern"], ["Frobelwitz", "Krampitz"], ["Lampersdorf", "Borne"], ["Lissa", "Stabelwitz"], ["Lissa", "Goldschmieden"]]
B.woods = [[*gB(2390, 690), 520, 420], [*gA(2950, 1450), 380, 200], [*gA(3090, 1430), 300, 230], [*gB(2483, 1896), 130, 110],
           [*gA(2625, 2035), 180, 110], [*gA(3300, 620), 900, 450], [*gA(1500, 1250), 450, 300]]
P = lambda pts, g=gA: [list(g(x, y)) for x, y in pts]
weistritz = P([(3860, 840), (3840, 920), (3800, 1030), (3740, 1080), (3720, 1140), (3690, 1200), (3675, 1270), (3700, 1340), (3660, 1400),
               (3620, 1450), (3600, 1500), (3570, 1560), (3530, 1570), (3470, 1580), (3400, 1600), (3380, 1640), (3330, 1660), (3310, 1700),
               (3300, 1760), (3250, 1810), (3220, 1860), (3140, 1930), (3110, 2000), (3120, 2100), (3110, 2250), (3120, 2350)])
B.water["rivers"] = [
    {"p": weistritz, "w": 3},
    {"p": P([(1998, 1595), (2233, 1611), (2500, 1675), (2766, 1654), (2958, 1675), (3086, 1707), (3278, 1696)], gB), "w": 1.5, "ford": True},
    {"p": P([(2600, 1700), (2730, 1740), (2860, 1830), (2960, 1860)]), "w": 1.2, "ford": True},
    {"p": P([(2280, 400), (2330, 560), (2380, 700), (2440, 800), (2470, 980)], gB), "w": 1.5, "ford": True},
]
B.water["lakes"] = [P([(2800, 2010), (2860, 2020), (2910, 2060), (2910, 2110), (2860, 2090), (2810, 2040)])]
B.water["labels"] = {"Weistritz (Schweidnitzer Wasser)": gA(3560, 1560), "Mittel-Teich": gA(2870, 2060), "Gohlau ditch": gA(2760, 1770)}
for nm, p in [("Lissa stone bridge", gA(3675, 1265)), ("Lissa second bridge", gA(3690, 1215)), ("Stabelwitz bridge", gA(3745, 1090)),
              ("Rathen bridge", gA(3440, 1585)), ("Arnoldsmühle", gA(3305, 1720))]:
    B.crossing(nm, p)

# ---------------- reference lines read off the plans
# Austrian night camp (Plan 12A A) and battle position (Plan 12A C), north to south
AN1 = [gA(2700, 600), gA(2670, 1080), gA(2690, 1440)]; AN2 = [gA(2800, 600), gA(2785, 1100), gA(2800, 1440)]
AC1 = [gA(2560, 800), gA(2535, 865), gA(2540, 1045), gA(2515, 1070), gA(2450, 1410)]
AC2 = [gA(2600, 830), gA(2575, 875), gA(2585, 1045), gA(2570, 1070), gA(2490, 1410)]
# Austrian front after the wheel (Plan 12B C): north of Leuthen west to east, and the refused right wing towards Gross-Heidau
CF1 = [gB(2400, 1295), gB(2540, 1360), gB(2715, 1425), gB(2820, 1500)]; CF2 = [gB(2380, 1335), gB(2500, 1390), gB(2735, 1390), gB(2840, 1460)]
CR1 = [gB(2100, 1010), gB(2400, 1150)]; CR2 = [gB(2160, 1000), gB(2380, 1110)]
# Prussian deployment (Plan 12A D), advance (F) and line south of Leuthen (Plan 12B A), left to right
D1 = [gA(1797, 1777), gA(2116, 1898)]; D2 = [gA(1830, 1832), gA(2116, 1953)]
F1 = [gA(2028, 1843), gA(2589, 1997)]; F2 = [gA(1962, 1887), gA(2578, 2030)]
L6a = [gA(2250, 1760), gA(2640, 1870)]; L6b = [gA(2200, 1830), gA(2600, 1950)]
A1 = [gB(2276, 1451), gB(2798, 1585), gB(2905, 1553)]
N9 = [gB(2300, 1395), gB(2620, 1410), gB(2820, 1470)]; N10 = [gB(2330, 1335), gB(2640, 1370), gB(2870, 1420)]
END = [gA(2750, 1010), gA(3450, 1235)]
fD, fF = (brg(*D1) - 90) % 360, (brg(*F1) - 90) % 360

# ---------------- units
def U(uid, side, typ, name, strength, frontage, keys, note, conf, men, cite, via=None, **kw):
    u = B.unit(uid, side, typ, name, strength, frontage, note=note, conf=conf, cite=cite, men=men, **kw)
    for ph, k in keys.items():
        pos, f, form = k[:3]
        u.at(ph, pos, f, form, via=(via or {}).get(ph), bend=k[3] if len(k) > 3 else 0)
    return u

# Prussian march columns (07:30-08:30): four columns along the Neumarkt road, cavalry outside [gs1904]
col = lambda north_m, east_m: mv(mv((51.1600, 16.6420), 0, north_m), 90, east_m * 0.7)
CITE_P = ["gs1904", "gs12a", "gs12b"]

pinf = [  # id, name, battalions, men, column (north offset), order in column, D-line fraction, line, loss
    ("pfl", "Left-flank grenadiers (Dieringshofen, I/Kurssell) under Bornstedt", "2 bns", 1000, 300, 3, 1 / 24, 1, 100),
    ("p1d", "Geist's brigade (gren. Schenckendorff and Hacke, Alt-Braunschweig, Forcade)", "6 bns", 3300, 300, 0, 5 / 24, 1, 650),
    ("p1c", "Münchow's brigade (Winterfeldt, Geist)", "4 bns", 2200, 300, 1, 10 / 24, 1, 500),
    ("p1b", "Kahlden's brigade (Pannwitz, Kannacher, gren. Retzow)", "5 bns", 2600, -300, 1, 14.5 / 24, 1, 800),
    ("p1a", "Prince Ferdinand's brigade (II-III/Garde, Markgraf Karl, gren. Kremzow)", "5 bns", 3000, -300, 0, 19.5 / 24, 1, 1000),
    ("pfr", "Right-flank grenadiers (Unruh, Kleist) under Rohr", "2 bns", 1000, -300, 3, 23 / 24, 1, 250),
    ("p2l", "Oldenburg's brigade, second line (Kalckstein, Prinz Heinrich, Prinz Ferdinand, gren. Kahlden and Ploetz)", "6 bns", 2900, 300, 2, 3 / 11, 2, 400),
    ("p2r", "Bülow's brigade, second line (Alt-Württemberg, Jung-Braunschweig, Münchow, Prinz von Preussen, gren. Ostenreich)", "5 bns", 2250, -300, 2, 8.5 / 11, 2, 450),
]
notes = {
    "pfl": "Grenadiers covering the left of the first line [gs1904].",
    "p1d": "The left of the first line; it came up level west of Leuthen into a firefight under the guns on the windmill height. Grenadier battalion Schenckendorff took those batteries at the end [gs1904].",
    "p1c": "Part of the first line's left wing in the echelon advance [gs1904] [gs12a].",
    "p1b": "Grenadier battalion Retzow assaulted the Leuthen churchyard with the Garde; the king praised Pannwitz for 'wonders of bravery' [gs1904].",
    "p1a": "The right of the first line, the first to follow Wedel in echelon. Kremzow's grenadiers, led by Prince Moritz himself, took the Kirchberg battery; III/Garde under Captain von Möllendorff forced the west gate of the Leuthen churchyard [gs1904] [wiki].",
    "pfr": "Grenadiers under General von Rohr on the right of the first line; Rohr was mortally wounded [gs1904].",
    "p2l": "Second line under Forcade; its battalions filled gaps in the first line during the Leuthen fight [gs1904].",
    "p2r": "Second line; several of its regiments were down to one battalion after the defeat at Breslau on 22 November [gs1904].",
}
for uid, nm, bns, m0, colN, order, fr, line, loss in pinf:
    Dl, Fl, L6, Dn = (D1, F1, L6a, 0) if line == 1 else (D2, F2, L6b, 1)
    dpos = along(Dl, fr); fpos = along(Fl, fr)
    lead = {"p1a": 0.7, "pfr": 0.75, "p1b": 0.45, "p1c": 0.2, "p1d": 0.0, "pfl": 0.0, "p2r": 0.4, "p2l": 0.0}[uid]
    a1 = along(A1, {"pfl": 0.0, "p1d": 0.06, "p1c": 0.18, "p1b": 0.32, "p1a": 0.5, "pfr": 0.72, "p2l": 0.1, "p2r": 0.62}[uid])
    if line == 2: a1 = mv(a1, 190, 250)
    n9 = along(N9, {"pfl": 0.0, "p1d": 0.08, "p1c": 0.24, "p1b": 0.42, "p1a": 0.6, "pfr": 0.85, "p2l": 0.16, "p2r": 0.72}[uid])
    n10 = along(N10, {"pfl": 0.0, "p1d": 0.08, "p1c": 0.24, "p1b": 0.42, "p1a": 0.6, "pfr": 0.85, "p2l": 0.16, "p2r": 0.72}[uid])
    if line == 2: n9, n10 = mv(n9, 200, 220), mv(n10, 200, 220)
    end = along(END, {"pfl": 0.05, "p1d": 0.15, "p1c": 0.3, "p1b": 0.45, "p1a": 0.6, "pfr": 0.75, "p2l": 0.2, "p2r": 0.55}[uid])
    if line == 2: end = mv(end, 340, 300)
    p3 = gA(1850 if line == 1 else 1810, {"p1a": 1560, "pfr": 1610, "p1b": 1480, "p1c": 1400, "p1d": 1320, "pfl": 1250, "p2r": 1540, "p2l": 1380}[uid])
    keys = {0: (col(colN, 2200 - order * 700 - (0 if line == 1 else 300)), 90, "C"),
            1: (col(colN, 3000 - order * 700 - (0 if line == 1 else 300)), 90, "C"),
            2: (gA(1930 - order * 60 - (0 if line == 1 else 40), 905 if colN > 0 else 1070), 90, "C" if order else "L"),
            3: (p3, 170, "C"), 4: (dpos, fD, "L"), 5: (lerp(dpos, fpos, lead), fF, "L"),
            6: (mv(along(L6, fr), 200, 0 if line == 1 else 220), 20, "F" if line == 1 else "L"), 7: (lerp(along(L6, fr), a1, 0.5), 15, "L"), 8: (a1, 15, "F"), 9: (n9, 15, "F"), 10: (n10, 20, "L"),
            11: (end, 60, "L")}
    men = {0: m0, 5: m0 - loss // 10, 6: m0 - loss // 4, 8: m0 - loss // 2, 9: m0 - loss * 3 // 4, 10: m0 - loss * 9 // 10, 11: m0 - loss}
    U(uid, "pr", "gd" if uid == "p1a" else "inf", nm, f"{bns} [gs1904]", 140 * int(bns.split()[0]), keys, notes[uid], "medium" if uid not in ("pfl", "pfr") else "low", men, CITE_P,
      via={3: [gA(1870 if line == 1 else 1830, 1060)], 4: [gA(1860 if line == 1 else 1820, 1720)]})

wedelP = mv(along(D1, 1.0), fD, 300)
U("wedel", "pr", "inf", "Wedel's 'Attacke' (I-II/Meyerinck, II/Itzenplitz)", "3 bns [gs1904]", 420,
  {0: (col(0, 3400), 90, "C"), 1: (gA(1450, 950), 90, "C"), 2: (gA(1850, 1060), 120, "C"), 3: (gA(1880, 1660), 170, "C"), 4: (wedelP, fD, "L"),
   5: (mv(B.pos("Kiefernberg"), 225, 120), 40, "F"), 6: (mv(B.pos("Kirchberg"), 200, 150), 40, "F"), 7: (along(A1, 0.88), 340, "L"), 8: (along(A1, 0.9), 340, "F"),
   9: (gB(2850, 1440), 330, "F"), 10: (gB(2880, 1380), 330, "L"), 11: (along(END, 0.85), 60, "L")},
  "The three avant-garde battalions under G.M. von Wedel that opened the attack: one volley, then the bayonet, and they were among the Württemberg guns on the Kiefernberg before the second enemy volley. With Kremzow's grenadiers they then took the Kirchberg battery [gs1904] [gs12a].",
  "high", {0: 1800, 5: 1650, 6: 1500, 8: 1400, 10: 1320, 11: 1300}, CITE_P, via={3: [gA(1880, 1080)], 4: [gA(1900, 1780)], 7: [gA(2760, 1700)]})
U("bevern", "pr", "inf", "Prince Karl of Bevern's flank battalions (gren. Manteuffel, Wedel, Ramin; Bornstedt, Asseburg, I/Itzenplitz)", "6 bns [gs1904]", 700,
  {0: (col(0, 2900), 90, "C"), 1: (gA(1400, 960), 90, "C"), 2: (gA(1790, 1080), 120, "C"), 3: (gA(1910, 1760), 160, "C"), 4: (gA(2470, 2085), 45, "L"),
   5: (gA(2560, 2150), 60, "F"), 6: (gA(2870, 1850), 330, "F"), 7: (along(A1, 1.0), 330, "L"), 8: (mv(along(A1, 1.0), 20, 150), 330, "F"), 9: (gB(2930, 1395), 300, "F"),
   10: (gB(2950, 1330), 300, "L"), 11: (mv(B.pos("Lissa"), 255, 350), 75, "F")},
  "The six avant-garde battalions sent with Zieten as his flank guard. Their musketry and canister drove off Nádasdy's 43 squadrons; Prince Moritz then led them round the Austrian position at the Gohlau ditch. Three of them (Manteuffel, Wedel, Ramin) followed the king to Lissa after dark [gs1904].",
  "high", {0: 3200, 5: 3100, 6: 2950, 8: 2900, 10: 2850, 11: 2800}, CITE_P, via={3: [gA(1880, 1100)], 4: [gA(1960, 1840), gA(2300, 2000)], 6: [gA(2700, 2020)]})
U("angel", "pr", "lt", "Angelelli's free battalions (Angelelli, Kalben, Le Noble) and the foot Jäger", "3½ bns [gs1904]", 450,
  {0: (col(0, 4700), 90, "C"), 1: (gA(1520, 930), 90, "C"), 2: ("Borne", 90, "L"), 7: ("Borne", 90, "L"), 8: (gB(1950, 1080), 100, "C"),
   9: (gB(2080, 1100), 100, "C"), 10: (gB(2200, 1150), 110, "L"), 11: (gB(2470, 1335), 60, "F")},
  "Light infantry that held Borne through the day, then marched east at dusk and joined the attack on Wallis and Baden-Durlach on the windmill height [gs1904]. Their arrival is shown late, after dark, because the map cannot move them faster than a march.",
  "medium", {0: 1500, 10: 1400, 11: 1350}, CITE_P, via=None)

pcav = [  # id, name, strength text, men, typ, note, loss
    ("zi1", "Zieten's first line (Gardes du Corps, Gensd'armes, Seydlitz, Markgraf Friedrich and Baron Schönaich cuirassiers)", "23 sqns", 2070, "cav",
     "The right-wing cuirassiers; repulsed Nádasdy's charge with Bevern's help, then charged between the Faulbusch and the Gohlau ponds. Lentulus's brigade took 15 guns and nearly destroyed the Jung-Modena Dragoons; the Seydlitz Cuirassiers went with the king to Lissa [gs1904].", 400),
    ("zi2", "Zieten's second line (Stechow, Krockow, Czettritz and Normann dragoons)", "20 sqns", 1600, "cav",
     "Came into the first line in the broken ground; General von Krockow was wounded and captured [gs1904].", 200),
    ("zhus", "Zieten Hussars (Seelen)", "10 sqns", 800, "lc",
     "Scouted ahead of the march south; at the end of Zieten's charge they swung past their own cavalry onto the fleeing infantry and took about 2,000 prisoners [gs1904].", 80),
    ("dr1", "Driesen's first line (Bayreuth Dragoons, Driesen and Krockow cuirassiers, Carabiniers)", "25 sqns", 2125, "cav",
     "The left-wing cavalry, held back behind the rises to cover the infantry's left; at dusk it took Lucchesi's cavalry in the flank: 15 cuirassier squadrons and the 10 squadrons of the Bayreuth Dragoons in the first line [gs1904] [gs12b].", 200),
    ("dr2", "Bredow's second line (Gessler, Prinz Schönaich and Kyau cuirassiers)", "15 sqns", 1275, "cav",
     "The second line of Driesen's charge [gs1904].", 100),
    ("putt", "Puttkamer Hussars", "10 sqns", 750, "lc",
     "Joined the left wing for the march south; in Driesen's charge they overlapped on the left and fell on the Austrian cavalry's rear [gs1904].", 60),
    ("wurt", "Reserve cavalry under Prince Eugen of Württemberg (Werner, Warnery, Seydlitz and Szekely hussars, Württemberg Dragoons)", "30 sqns", 2250, "lc",
     "The avant-garde cavalry: its 30 first-line squadrons broke Nostitz's Saxons at Borne; it screened the march south on the ridge with the king, then stood in reserve and joined Driesen's charge [gs1904].", 130),
]
pcav_keys = {
    "zi1": {0: (col(-900, 2600), 90, "C"), 1: (col(-900, 3500), 90, "C"), 2: (gA(1850, 1150), 120, "C"), 3: (gA(1880, 1740), 150, "C"), 4: (gA(2500, 2150), 35, "L"),
            5: (gA(2470, 2175), 35, "L"), 6: (gA(2760, 1900), 20, "L"), 7: (gA(2980, 1770), 20, "L"), 8: (gA(3020, 1760), 0, "L"), 11: (mv(B.pos("Lissa"), 230, 450), 60, "L")},
    "zi2": {0: (col(-900, 1800), 90, "C"), 1: (col(-900, 2700), 90, "C"), 2: (gA(1780, 1160), 120, "C"), 3: (gA(1840, 1700), 150, "C"), 4: (gA(2490, 2195), 35, "L"),
            6: (gA(2720, 1960), 20, "L"), 7: (gA(2940, 1810), 20, "L"), 8: (gA(2990, 1800), 0, "L"), 11: (gA(3050, 1700), 20, "L")},
    "zhus": {0: (col(0, 5200), 90, "C"), 1: (gA(1500, 960), 90, "L"), 2: (gA(2030, 1000), 90, "L"), 3: (gA(1960, 1820), 150, "C"), 4: (gA(2457, 2239), 35, "L"),
             6: (gA(2700, 2010), 20, "L"), 7: (gA(3020, 1650), 40, "L"), 8: (gA(3150, 1620), 40, "L"), 11: (gA(3250, 1450), 40, "L")},
    "dr1": {0: (col(900, 2600), 90, "C"), 1: (col(900, 3500), 90, "C"), 2: (gA(1880, 820), 90, "L"), 3: (gA(1850, 1150), 170, "C"), 4: (gA(1835, 1620), 90, "L"),
            8: (gB(1998, 1442), 60, "L"), 9: (gB(1985, 1300), 20, "C"), 10: (gB(2095, 1228), 135, "L"), 11: (gA(3200, 1240), 80, "L")},
    "dr2": {0: (col(900, 1800), 90, "C"), 1: (col(900, 2700), 90, "C"), 2: (gA(1820, 790), 90, "L"), 3: (gA(1810, 1120), 170, "C"), 4: (gA(1795, 1650), 90, "L"),
            8: (gB(1965, 1465), 60, "L"), 9: (gB(1950, 1340), 20, "C"), 10: (gB(2060, 1265), 135, "L"), 11: (gA(3150, 1290), 80, "L")},
    "putt": {0: (col(500, 5000), 90, "C"), 1: (gA(1500, 870), 90, "L"), 2: (gA(2060, 830), 90, "L"), 3: (gA(1820, 1080), 170, "C"), 4: (gA(1745, 1560), 90, "L"),
             8: (gB(1930, 1400), 60, "L"), 9: (gB(1960, 1250), 20, "C"), 10: (gB(2160, 1185), 160, "L"), 11: (gA(3120, 1180), 80, "L")},
    "wurt": {0: (col(0, 5600), 90, "C"), 1: (gA(1600, 885), 290, "L"), 2: (gA(2050, 900), 90, "L"), 3: (gA(1990, 1450), 90, "L"), 4: (mv(along(D2, 0.5), (fD + 180) % 360, 450), fD, "L"),
             7: (mv(along(D2, 0.5), (fD + 180) % 360, 450), fD, "L"), 8: (gB(2345, 1630), 15, "L"), 10: (gB(2200, 1330), 120, "L"), 11: (gA(3250, 1300), 80, "L")},
}
pcav_via = {"dr1": {9: [gB(1960, 1380)]}, "dr2": {9: [gB(1930, 1410)]}, "wurt": {8: [gA(2150, 1950)]}, "zi1": {11: [gA(3200, 1600), gA(3350, 1400)]}}
for uid, nm, sq, m0, typ, note, loss in pcav:
    men = {0: m0, 1: m0 - (40 if uid == "wurt" else 0), 6: m0 - loss // 2, 10: m0 - loss * 9 // 10, 11: m0 - loss}
    U(uid, "pr", typ, nm, f"{sq} [gs1904]", 45 * int(sq.split()[0]), pcav_keys[uid], note, "medium", men, CITE_P, via=pcav_via.get(uid))

part = [("brum", "The 'Brummer' battery: ten Glogau fortress 12-pounders", "10 guns [gs1904]", 10,
         {0: (col(0, 2300), 90, "C"), 1: (col(0, 3100), 90, "C"), 2: (gA(1900, 1000), 90, "C"), 3: (gA(1890, 1590), 170, "C"), 4: (mv(wedelP, (fD + 270) % 360, 250), fD, "L"),
          5: (B.pos("Glanzberg"), 30, "F"), 6: (mv(B.pos("Kirchberg"), 300, 120), 0, "F"), 8: (gB(2240, 1455), 40, "F"), 11: (gB(2240, 1455), 40, "L")},
         "Ten heavy fortress guns brought from Glogau; they fired from the Glanzberg on the Kiefernberg, followed to the Kirchberg, and ended on the south-east slope of the Butterberg [gs1904] [carlyle].", "high"),
        ("pa_c", "Heavy batteries of the centre", "two batteries, ≈34 guns [gs1904]", 34,
         {0: (col(0, 1500), 90, "C"), 1: (col(0, 2300), 90, "C"), 2: (gA(1800, 1000), 90, "C"), 3: (gA(1890, 1450), 170, "C"), 4: (mv(along(D1, 0.5), fD, 200), fD, "L"),
          5: (mv(B.pos("Judenberg"), 225, 150), 40, "F"), 6: (mv(B.pos("Kirchberg"), 260, 450), 20, "F"), 8: (gB(2440, 1530), 10, "F"), 11: (gB(2440, 1530), 10, "L")},
         "Two batteries before the centre of the first line; they fired from the Judenberg into Nádasdy's crowded infantry, then moved to the left of the Kirchberg and finally south of Leuthen [gs1904].", "medium"),
        ("pa_r", "Heavy battery of the right wing", "≈17 guns [gs1904]", 17,
         {0: (col(0, 1200), 90, "C"), 1: (col(0, 2000), 90, "C"), 2: (gA(1780, 1020), 90, "C"), 3: (gA(1890, 1400), 170, "C"), 4: (mv(along(D1, 0.85), fD, 200), fD, "L"),
          5: (mv(B.pos("Judenberg"), 120, 350), 40, "F"), 6: (mv(B.pos("Kirchberg"), 250, 250), 20, "F"), 8: (gB(2620, 1565), 10, "F"), 11: (gB(2620, 1565), 10, "L")},
         "The battery before the right of the first line [gs1904].", "medium"),
        ("pa_l", "Heavy battery of the left wing", "≈17 guns [gs1904]", 17,
         {0: (col(0, 900), 90, "C"), 1: (col(0, 1700), 90, "C"), 2: (gA(1760, 1040), 90, "C"), 3: (gA(1890, 1330), 170, "C"), 4: (mv(along(D1, 0.12), fD, 200), fD, "L"),
          6: (mv(along(L6a, 0.0), 20, 200), 20, "F"), 8: (gB(2222, 1438), 45, "F"), 11: (gB(2222, 1438), 45, "L")},
         "The battery before the left of the first line; the king put it on the south-east slope of the Butterberg when the left wing wavered west of Leuthen [gs1904].", "medium")]
for uid, nm, st, guns, keys, note, conf in part:
    U(uid, "pr", "art", nm, st, 160, keys, note, conf, {0: guns}, CITE_P, via={3: [gA(1890, 1080)], 4: [gA(1900, 1720)]})

# ---------------- Austrians
CITE_A = ["gs1904", "gs12a", "gs12b", "beaulieu"]
ainf = [  # id, name, bns, men, night line, night fraction, battle fraction, wheel position, loss
    ("a5", "Andlau's brigade (Kaiser, Neipperg, Botta)", 6, 3350, AN1, 0.30, 0.10, ("R", 0.25), 1000),
    ("a4", "Macquire's brigade (Leopold Daun, Puebla, Arenberg)", 5, 2800, AN1, 0.48, 0.30, ("R", 0.72), 1000),
    ("a3", "Angern's brigade (Alt-Wolfenbüttel, Joseph Esterházy)", 4, 2250, AN1, 0.63, 0.50, ("F", 0.85), 800),
    ("a2", "d'Arberg's brigade (Nikolaus Esterházy, Thürheim, Kheul)", 5, 2800, AN1, 0.78, 0.68, ("F", 0.5), 1300),
    ("a1", "Puebla's brigade (Moltke, Hildburghausen, Erzherzog Karl)", 5, 2800, AN1, 0.93, 0.88, ("F", 0.15), 1300),
    ("b3", "Winulf Starhemberg's brigade, second line (Karl Lothringen, Waldeck, Wallis, Pallavicini, Kolowrat, Baden-Durlach)", 7, 3900, AN2, 0.35, 0.15, ("F2", 0.15), 1400),
    ("b2", "Haller's brigade, second line (Deutschmeister, Browne, Bethlen, Harsch)", 5, 2800, AN2, 0.62, 0.50, ("F2", 0.65), 1100),
    ("b1", "Wied's brigade, second line (Baden-Baden, Gaisruck, Ludwig Wolfenbüttel, Harrach)", 6, 3350, AN2, 0.88, 0.85, ("V", 0), 1100),
]
anote = {
    "a5": "The right of the first line, west of Guckerwitz; after the wheel it formed the refused right towards Gross-Heidau [gs12a] [gs12b].",
    "a4": "First line between Guckerwitz and Frobelwitz [gs12a]; three Austrian regiments were later hurried south to Nádasdy, Maguire's own among them [gs1904].",
    "a3": "First line west of Frobelwitz [gs12a].",
    "a2": "First line between Frobelwitz and Leuthen [gs12a].",
    "a1": "The left of the main army's first line, bending round the west end of Leuthen [gs1904] [gs12a].",
    "b3": "Second line, right. Its regiments Wallis and Baden-Durlach made the last stand on the windmill height north of Leuthen and were ridden down by the Carabiniers and Bayreuth Dragoons [gs1904].",
    "b2": "Second line, centre; its Würzburg battalion was posted in the Leuthen churchyard (shown separately) [gs1904].",
    "b1": "Second line, left. After the reserve was thrown back, battalions of the left of the second line held Leuthen itself and threw up a breastwork [gs1904].",
}
for uid, nm, nb, m0, night, fn, fb, (wk, wf), loss in ainf:
    first = uid.startswith("a")
    bat = along(AC1 if first else AC2, fb)
    if wk == "R": wheel, wf_face = along(CR1, wf), 225
    elif wk == "R2": wheel, wf_face = along(CR2, wf), 225
    elif wk == "F": wheel, wf_face = along(CF1, wf), 200
    elif wk == "F2": wheel, wf_face = along(CF2, wf), 200
    else: wheel, wf_face = gB(2610, 1440), 190
    rout = mv(wheel, 55, 1200)
    keys = {0: (along(night, fn), 265, "X"), 1: (bat, 260, "L"), 6: (bat, 260, "L"), 7: (lerp(bat, wheel, 0.6), wf_face, "C"), 8: (wheel, wf_face, "F" if uid in ("a1", "a2", "b1") else "L"),
            9: (wheel, wf_face, "F"), 10: (rout, 60, "R"), 11: (mv(B.pos("Lissa"), 75 + (sum(map(ord, uid)) % 40) - 20, 800 + 80 * nb), 80, "R")}
    if uid == "b3": keys[10] = (B.pos("Windmill height"), 225, "F")
    men = {0: m0, 8: m0 - loss // 6, 9: m0 - loss // 3, 10: m0 - loss * 2 // 3, 11: m0 - loss}
    U(uid, "au", "inf", nm, f"{nb} bns [gs1904]", 140 * nb, keys, anote[uid], "medium", men, CITE_A,
      via={11: [gA(3300, 1250), gA(3675, 1265)] if sum(map(ord, uid)) % 2 else [gA(3400, 1150), gA(3690, 1215)]})

U("rw", "rc", "inf", "Roth-Würzburg battalion (Würzburg contingent)", "1 bn [gs1904]", 140,
  {0: (along(AN2, 0.7), 265, "X"), 1: (along(AC2, 0.6), 260, "L"), 6: (along(AC2, 0.6), 260, "L"), 7: (gB(2553, 1451), 190, "L"), 8: (gB(2553, 1451), 190, "F"),
   9: (gB(2600, 1330), 30, "R")},
  "The Würzburg battalion that held the walled churchyard of Leuthen's Catholic church. Its guns and muskets swept the road from Schriegwitz until III/Garde forced the west gate; only 4 officers and 33 men escaped with one of its four colours [gs1904] [wiki].",
  "high", {0: 600, 8: 450, 9: 40}, CITE_A)
U("res1", "au", "inf", "Reserve corps: Los Rios, Königsegg, Sachsen-Gotha (Arenberg)", "3 bns [gs1904]", 420,
  {0: (gA(2980, 620), 250, "X"), 1: (gA(2980, 620), 250, "L"), 2: ("Nippern", 250, "L"), 5: ("Nippern", 250, "L"), 6: (gA(2620, 820), 190, "C"),
   7: (gB(2420, 1545), 250, "L"), 8: (gB(2470, 1335), 200, "R"), 9: (gB(2560, 1300), 200, "L"), 10: (gB(2700, 1200), 60, "R"),
   11: (mv(B.pos("Lissa"), 60, 1600), 80, "R")},
  "Three battalions of the Duke of Arenberg's reserve, sent to hold Nippern when Lucchesi feared for the right; ordered back south at the crisis, they arrived at Leuthen breathless and in disorder and tried to form a front south of the village with a refused flank [gs1904] [gs12a] [gs12b].",
  "medium", {0: 1700, 8: 1250, 10: 1000, 11: 800}, CITE_A, via={7: ["Leuthen"], 11: [gA(3400, 1150), gA(3690, 1215)]})
U("res2", "au", "inf", "Reserve corps: Ligne, Mercy, Andlau, Haller, d'Arberg (Arenberg)", "5 bns [gs1904]", 700,
  {0: (gA(2990, 730), 250, "X"), 1: (gA(2990, 730), 250, "L"), 2: (gA(2750, 570), 250, "L"), 5: (gA(2750, 570), 250, "L"), 6: (gA(2660, 1050), 190, "C"),
   7: (gB(2525, 1472), 190, "L"), 8: (gB(2600, 1365), 200, "R"), 9: (gB(2650, 1330), 200, "L"), 10: (gB(2780, 1250), 60, "R"),
   11: (mv(B.pos("Lissa"), 90, 1800), 80, "R")},
  "The rest of the reserve, posted south-east of Nippern at about 10:30, then marched back south through Leuthen. The young Prince de Ligne commanded the battalion of his father's regiment after its officers fell, and drew its last 200 men back to the windmill north of the village [gs1904] [carlyle] [wiki].",
  "medium", {0: 2800, 8: 2000, 10: 1600, 11: 1200}, CITE_A, via={7: ["Frobelwitz"], 11: [gA(3300, 1250), gA(3675, 1265)]})

acav = [  # id, name, sqns, men, night, battle, note, loss
    ("c3", "Lucchesi's cavalry, right wing first line (Löwenstein, Stampach, Lucchesi, Erzherzog Leopold cuirassiers, Erzherzog Joseph Dragoons)", 25, 2750,
     gA(2715, 640), gA(2640, 670), "The right-wing cavalry under General Count Lucchesi d'Averna. His alarm at the Prussian feint drew the reserve and the left-wing cavalry north. At dusk he led more than 70 squadrons against the Prussian left without scouting south, was taken in flank by Driesen and killed in the melee [gs1904] [wiki].", 900),
    ("c4", "Esterházy's cavalry, right wing second line (Anhalt-Zerbst, Serbelloni cuirassiers, Württemberg and Benedikt Daun dragoons)", 20, 2200,
     gA(2780, 650), gA(2700, 700), "The second line of the right wing [gs12a].", 600),
    ("c1", "Serbelloni's cavalry, left wing first line (Hessen-Darmstadt Dragoons, Erzherzog Ferdinand, Kalkreuth, Gelhay and Anspach-Bayreuth cuirassiers)", 26, 2860,
     gA(2740, 1560), gA(2440, 1560), "Sent north with Daun at about 10:30 to support Lucchesi, so the threatened left lost most of its cavalry; it joined Lucchesi's last charge [gs1904].", 400),
    ("c2", "Stampach's cavalry, left wing second line (Kolowrat Dragoons, Birkenfeld, Schmerzing and O'Donell cuirassiers)", 21, 2300,
     gA(2820, 1570), gA(2480, 1550), "The squadrons left on the left wing; they covered the reserve's attempt to form south of Leuthen until cannon fire drove them behind the Leuthen wood [gs1904].", 300),
]
for uid, nm, sq, m0, night, bat, note, loss in acav:
    if uid == "c3":
        keys = {0: (night, 265, "X"), 1: (bat, 240, "L"), 7: (bat, 240, "L"), 8: (gB(2300, 1170), 210, "L"), 9: (along([gB(2055, 1335), gB(2190, 1205)], 0.5), 135, "L"),
                10: (gB(2330, 1200), 45, "R"), 11: (mv(B.pos("Lissa"), 40, 1500), 60, "R")}
    elif uid == "c4":
        keys = {0: (night, 265, "X"), 1: (bat, 240, "L"), 7: (bat, 240, "L"), 8: (gB(2250, 1115), 210, "L"), 9: (along([gB(2120, 1405), gB(2300, 1240)], 0.5), 135, "L"),
                10: (gB(2420, 1260), 45, "R"), 11: (mv(B.pos("Lissa"), 20, 1700), 60, "R")}
    elif uid == "c1":
        keys = {0: (night, 265, "X"), 1: (bat, 260, "L"), 2: (gA(2800, 780), 260, "L"), 7: (gA(2800, 780), 260, "L"), 8: (gB(2360, 1115), 210, "L"),
                9: (along([gB(2090, 1370), gB(2265, 1210)], 0.5), 135, "L"), 10: (gB(2380, 1230), 45, "R"), 11: (mv(B.pos("Lissa"), 50, 1900), 60, "R")}
    else:
        keys = {0: (night, 265, "X"), 1: (bat, 260, "L"), 6: (bat, 260, "L"), 7: (gB(2700, 1530), 200, "L"), 8: (gA(2950, 1360), 220, "L"),
                10: (gA(3150, 1300), 60, "R"), 11: (mv(B.pos("Lissa"), 120, 1500), 80, "R")}
    men = {0: m0, 8: m0 - loss // 6, 10: m0 - loss // 2, 11: m0 - loss}
    U(uid, "au", "cav", nm, f"{sq} sqns [gs1904]", 45 * sq, keys, note, "medium", men, CITE_A,
      via={2: [gA(2700, 1150)], 8: [gA(2850, 900), gB(2500, 1050)] if uid in ("c3", "c4") else ([gA(2700, 1000)] if uid == "c1" else None),
           11: [gA(3400, 1150), gA(3745, 1090)] if uid in ("c3", "c4") else [gA(3300, 1250), gA(3690, 1215)]})

# Nádasdy's corps on the Sagschütz heights (Plan 12A C1); first line Austrians and Bavarians facing west, Württembergers facing south-west
WUE = [gA(2470, 1885), gA(2540, 1910), gA(2605, 1955), gA(2615, 1985)]
nad = [
    ("n3", "au", "inf", "Arenberg's Austrians under Forgách, first line (Heinrich Daun, Leopold Pálffy, Haller, Maguire)", "5 bns [gs1904]", 2750, gA(2845, 1000), gA(2505, 1705), 265,
     "The Austrian regiments north of the Bavarians; three regiments (Maguire, Johann Pálffy, Haller) were hurried forward in front of the Bavarians at the last moment and gave way [gs1904].", 1400),
    ("n4", "au", "inf", "Wolffersdorff's Austrians, second line (Johann Pálffy, Adam Batthyányi, Forgách, Clerici, Luzan)", "5 bns [gs1904]", 2750, gA(2845, 1150), gA(2548, 1705), 265,
     "Second line of Nádasdy's corps; Nádasdy rallied what he could behind the Gohlau ditch and, at night, held the Weistritz crossings at Lissa [gs1904].", 1300),
    ("n2", "rc", "inf", "Bavarian contingent (Seyssel d'Aix): Minucci, Morawitzky, Leib-Regiment, Herzog Clemens, Kurprinz", "10 bns [gs1904]", 5500, gA(2845, 1300), gA(2505, 1810), 260,
     "The Bavarian auxiliaries north of Sagschütz; they were swept away when the Württembergers and the regiments before them broke. Losses 49 officers and 581 men [gs1904].", 630),
    ("wue", "rc", "inf", "Württemberg contingent (Spiznass): Truchsess, Roeder, Prinz Louis, Leib-Regiment, Spiznass", "10 bns [gs1904]", 5200, gA(2845, 1420), along(WUE, 0.45), 220,
     "The Württembergers held the first line on the west and south slopes of the Sagschütz hills, three battalions in the Kiefernberg wood. Roeder lost 20% before falling back, but the contingent fought reluctantly and lost very many 'missing' [gs1904].", 1800),
    ("wueg", "rc", "inf", "Württemberg grenadier battalions (Plessen, Georgi, Kettenburg)", "3 bns [gs1904]", 1500, gA(2845, 1480), gA(2620, 2005), 220,
     "Three grenadier battalions in the Faulbusch; they gave way with the Kiefernberg garrison without being attacked [gs1904].", 350),
]
for uid, side, typ, nm, st, m0, night, bat, face, note, loss in nad:
    keys = {0: (night, 265, "X"), 1: (bat, face, "L", 0.15 if uid == "wue" else 0), 4: (bat, face, "L", 0.15 if uid == "wue" else 0), 5: (bat, face, "F", 0.15 if uid == "wue" else 0)}
    if uid == "wue": keys[5] = (mv(bat, 45, 450), 225, "R")
    if uid == "wueg": keys[5] = (mv(bat, 45, 500), 225, "R")
    keys[6] = ({"n3": gA(2780, 1720), "n4": gA(2800, 1790), "n2": gA(2740, 1810), "wue": gA(2900, 1700), "wueg": gA(2950, 1760)}[uid], 220, "L" if uid == "n4" else "R")
    keys[7] = ({"n3": gA(3120, 1480), "n4": gA(2950, 1600), "n2": gA(3080, 1550), "wue": gA(3200, 1520), "wueg": gA(3250, 1560)}[uid], 45, "R")
    keys[9] = (mv(gA(3440, 1585), 95, 450 + 120 * len(uid)), 80, "R") if uid != "n4" else (gA(3600, 1300), 250, "L")
    keys[11] = (mv(B.pos("Lissa"), 125, 1500 + 120 * len(uid)), 80, "R") if uid != "n4" else (mv(B.pos("Lissa"), 90, 700), 250, "L")
    men = {0: m0, 5: m0 - loss // 5, 6: m0 - loss // 2, 7: m0 - loss * 4 // 5, 11: m0 - loss}
    U(uid, side, typ, nm, st, 150 * int(st.split()[0]), keys, note, "high" if uid in ("wue", "n2") else "medium", men, CITE_A,
      via={9: [gA(3380, 1600), gA(3440, 1585)] if uid != "n4" else None, 11: [gA(3675, 1265)] if uid == "n4" else None})

U("n5", "au", "cav", "Nádasdy's cavalry (Zweibrücken, Batthyányi, Jung-Modena and Sachsen-Gotha dragoons)", "21 sqns [gs1904]", 950,
  {0: (gA(2850, 1560), 265, "X"), 1: (gA(2650, 1705), 260, "L"), 4: (gA(2650, 1705), 260, "L"), 5: (gA(2740, 2120), 240, "L"), 6: (gA(3000, 1700), 45, "R"),
   7: (gA(3080, 1340), 200, "L"), 10: (gA(3300, 1250), 80, "R"), 11: (mv(B.pos("Lissa"), 105, 1400), 80, "R")},
  "Nádasdy's dragoons. Massed with the Saxons and hussars behind the Faulbusch, they charged Zieten and were stopped by Bevern's battalions; when Zieten came on, the Jung-Modena Dragoons were nearly destroyed. They rallied north of the Rathen wood [gs1904] [gs12a].",
  "medium", {0: 2300, 5: 2100, 6: 1700, 11: 1500}, CITE_A, via={5: [gA(2700, 1900)], 11: [gA(3675, 1265)]})
U("nos", "sx", "cav", "Nostitz's Saxon chevau-légers (Prinz Karl, Prinz Albrecht, Graf Brühl)", "12 sqns [gs1904]", 540,
  {0: (gA(1600, 860), 270, "L"), 1: (gA(2120, 960), 80, "R"), 2: (gA(2700, 1000), 260, "L"), 3: (gA(2665, 1960), 230, "L"), 5: (gA(2800, 2150), 240, "L"),
   6: (gA(3050, 1750), 45, "R"), 7: (gA(3120, 1350), 200, "L"), 10: (gA(3300, 1300), 80, "R"), 11: (mv(B.pos("Lissa"), 110, 1250), 80, "R")},
  "General Count Nostitz's three Saxon light-horse regiments, the outpost west of Borne. Caught in the fog by the Prussian avant-garde, they lost 11 officers, about 600 men and 2 standards. Rejoining Nádasdy, Nostitz charged Zieten in the afternoon and was captured with fourteen wounds; he died twelve days later [gs1904] [carlyle].",
  "medium", {0: 1400, 1: 800, 6: 600, 11: 500}, CITE_A, via={2: [gA(2300, 960)], 3: [gA(2780, 1300)], 11: [gA(3675, 1265)]})
U("mor", "au", "lc", "Morocz's hussars and Croats (Nádasdy and Dessewffy hussars)", "≈2 regts [gs1904]", 450,
  {0: (gA(1640, 940), 270, "L"), 1: (gA(2140, 1010), 80, "R"), 2: (gA(2720, 1080), 260, "L"), 3: (gA(2690, 1985), 230, "L"), 5: (gA(2780, 2105), 240, "L"),
   6: (gA(2950, 1650), 45, "R"), 10: (gA(3350, 1350), 80, "R"), 11: (mv(B.pos("Lissa"), 100, 1100), 80, "R")},
  "Austrian hussars with some hundreds of Croats pushed out before the right wing with Nostitz; they fled with him at Borne and joined Nádasdy [gs1904].",
  "low", {0: 2500, 1: 2300, 6: 2100, 11: 2000}, CITE_A, via={2: [gA(2300, 1010)], 3: [gA(2800, 1350)], 11: [gA(3675, 1265)]})
U("lus", "au", "lt", "Luszinsky's hussars and Croats", "≈2 regts [gs1904]", 450,
  {0: (gA(2300, 1750), 260, "L"), 3: (gA(2300, 1750), 260, "L"), 4: (gA(2420, 1700), 220, "L"), 5: (gA(2560, 1640), 220, "R"), 7: (gA(3000, 1500), 60, "R"),
   11: (mv(gA(3440, 1585), 95, 900), 80, "R")},
  "Light troops pushed out before the left wing [gs1904]; their movements in the battle are not recorded, and their positions here are inferred.",
  "low", {0: 2500, 5: 2400, 11: 2300}, CITE_A, via={11: [gA(3440, 1585)]})

U("aart_n", "au", "art", "Nádasdy's heavy batteries", "two batteries, ≈20 guns [gs1904]", 160,
  {0: (gA(2845, 1250), 265, "X"), 1: (gA(2462, 1845), 250, "L"), 4: (gA(2462, 1845), 250, "F"), 5: ("Kirchberg", 230, "F"), 6: (mv(B.pos("Kirchberg"), 45, 450), 45, "R")},
  "Two batteries north-west of Sagschütz; the Prussian guns on the Glanzberg drove them back to the Kirchberg, where Wedel and Kremzow's grenadiers took them all [gs1904] [carlyle].", "medium", {0: 20, 6: 0}, CITE_A)
U("aart_m", "au", "art", "Main army heavy batteries", "four batteries, ≈45 guns [gs1904]", 220,
  {0: (along(AN1, 0.6), 265, "X"), 1: (mv(along(AC1, 0.55), 260, 200), 260, "L"), 6: (mv(along(AC1, 0.55), 260, 200), 260, "L"), 7: ("Windmill height", 210, "F"),
   9: ("Windmill height", 210, "F"), 10: ("Windmill height", 210, "R")},
  "Four heavy batteries before the main army's front; after the wheel every gun that could be brought up fired from the windmill height north of Leuthen, until grenadier battalion Schenckendorff stormed them [gs1904].", "medium", {0: 45, 10: 5, 11: 0}, CITE_A)

# ---------------- commanders
B.commander("fred", "pr", "Frederick II", {0: col(0, 5300), 1: gA(1650, 940), 2: "Schönberg", 3: gA(1990, 1450), 4: "Wachberg", 7: gB(2100, 1580), 8: gB(2080, 1570),
            11: "Lissa"}, "Frederick rode with the avant-garde, studied the Austrian line from the Schönberg, rode with the hussar screen during the march, watched the attack from the Wachberg and spent the evening under fire near Radaxdorf before riding to Lissa in the dark [gs1904].")
B.commander("karl", "au", "Prince Charles of Lorraine", {0: "Breslauer Berg", 7: gB(2650, 1300), 10: gB(2800, 1200), 11: mv(B.pos("Lissa"), 90, 2000)},
            "Watched from the windmill on the Breslauer Berg, east of Frobelwitz, and took the Prussian demonstration for the real attack [gs1904].")
B.commander("daun", "au", "Field Marshal Daun", {0: "Breslauer Berg", 2: gA(2800, 760), 8: gB(2400, 1100), 11: mv(B.pos("Lissa"), 70, 2200)},
            "Went north with the cavalry to Lucchesi's wing; 'the good folk are slipping off, let them go' [gs1904] [carlyle].")
B.commander("nad", "au", "Nádasdy", {0: gA(2845, 1300), 1: gA(2580, 1800), 6: gA(2820, 1760), 7: gA(3080, 1400), 10: "Lissa"},
            "Franz Leopold Nádasdy commanded the left wing on the Sagschütz heights and sent message after message asking for help [gs1904].")

# ---------------- phases
A = B.arrow
B.phase("07:30", "March", "Night camps and the march from Neumarkt",
        "The Austrian army has spent a cold night under arms in two lines east of Nippern, Frobelwitz and Leuthen, with Nádasdy's corps and the reserve behind; its baggage is beyond the Weistritz [gs1904] [gs12a] [beaulieu]. Charles and Daun have decided to accept battle, but only on the defensive [gs1904]. The Prussians left Neumarkt before dawn in four columns, infantry inside and cavalry outside, behind an avant-garde of all the hussars, the free battalions and nine battalions of foot; ten heavy fortress guns from Glogau march with them [gs1904]. Thick fog lies over the fields [gs1904].",
        ("March column vs. battle line", "An eighteenth-century army marched in columns and fought in lines; turning one into the other took time and drill. The Prussian columns were organised so that they could become two battle lines by a simple wheel [gs1904].", "column-vs-line"),
        col(400, 4000), 14, conf="medium", cite=["gs1904", "gs12a", "beaulieu"], fog=0.9,
        arrows=[A("pr", "move", col(0, 1000), col(0, 4500), gA(1500, 940))],
        events=[(col(0, 5600), "Avant-garde: the hussars lead", ["gs1904"]), (gA(1600, 860), "Saxon outpost west of Borne", ["gs1904"]),
                (along(AN1, 0.5), "Austrian night camp east of the villages", ["gs12a", "beaulieu"])])
B.phase("08:30", "Borne", "The Saxon outpost is overrun at Borne",
        "In the fog the avant-garde runs into a line of horse west of Borne: Nostitz's three Saxon light-horse regiments and two of Morocz's hussar regiments [gs1904]. Thirty Prussian squadrons charge it front and flank; the Saxons are ridden down on their heavier-laden horses, losing 11 officers, about 600 men and two standards, and the Prussian hussars chase the rest past Gross-Heidau to the Austrian guns [gs1904] [carlyle]. Hearing of the advance, Charles moves his whole army 1,000-2,000 paces forward onto the crest west of the villages, Leuthen hooked into the line, and sends Nádasdy to the Sagschütz heights to cover the left [gs1904] [gs12a] [beaulieu].",
        ("Exposed advanced position", "An outpost in mist can neither see nor be supported. The loss of Nostitz's screen blinded the Austrians: from then on they could not see what Frederick was doing behind Borne [gs1904] [carlyle].", "exposed-outpost"),
        gA(1900, 1000), 9, conf="high", cite=["gs1904", "gs12a", "carlyle", "beaulieu"], fog=0.75,
        debate="Carlyle has Nostitz mortally wounded at Borne; the 1904 history, from a Saxon officer's report, shows he was wounded and captured in the afternoon charge on Zieten [gs1904] [carlyle]. Some accounts give the charge to Zieten; the General Staff found no evidence and gives it to the avant-garde cavalry under Prince Eugen of Württemberg [gs1904]. The map follows the General Staff.",
        arrows=[A("pr", "charge", gA(1480, 880), gA(1600, 870)), A("sx", "retreat", gA(1620, 860), "Borne", gA(2120, 960)),
                A("au", "move", along(AN1, 0.5), along(AC1, 0.5))],
        events=[(gA(1600, 870), "Nostitz's Saxons broken: about 600 prisoners", ["gs1904"]), (along(AC1, 0.6), "The Austrian army moves forward to the heights", ["gs1904", "gs12a"])])
B.phase("10:30", "Feint", "A demonstration against the Austrian right",
        "Frederick rides through Borne to the Schönberg and sees the Austrian line almost end to end; only the right-wing cavalry is hidden behind the Zettelbusch [gs1904] [carlyle]. He decides to attack Nádasdy at Sagschütz. East of Borne his columns begin to deploy as if against the right north of Frobelwitz [gs1904]. From the windmill on the Breslauer Berg, Charles takes this for the main attack; Lucchesi sends message after message for help; the reserve corps is sent to Nippern and Serbelloni with most of the left-wing cavalry north towards Guckerwitz, Daun with them [gs1904] [carlyle] [gs12a]. A French officer at headquarters objects that only an army of snipes could manoeuvre in the marshes there [gs1904].",
        ("Demonstration (feint)", "A show of force against the Austrian right made the Austrians weaken their left, which was the real target [gs1904].", "demonstration"),
        gA(2250, 850), 10, conf="medium", cite=["gs1904", "gs12a", "carlyle"], fog=0.5,
        debate="Was the deployment east of Borne a deliberate feint? Lentulus, Barsewisch and Tempelhof say so, and the Austrian reports agree that they saw a threat; Gaudi thought the columns were simply following the avant-garde before orders had been given [gs1904]. The map follows the General Staff's reading: a deliberate, partial deployment.",
        arrows=[A("au", "move", gA(2980, 620), "Nippern"), A("au", "move", gA(2990, 730), gA(2750, 570)), A("au", "move", gA(2440, 1560), gA(2700, 1150), gA(2800, 780)),
                A("pr", "move", "Borne", gA(1950, 905))],
        events=[("Schönberg", "Frederick on the Schönberg", ["gs1904"]), ("Breslauer Berg", "Charles and Daun at the windmill", ["gs1904"]),
                ("Nippern", "Reserve sent to the right", ["gs1904", "gs12a"])])
B.phase("11:30", "March south", "The march south behind the rises",
        "The army turns its columns into two battle lines on the march and heads south, aiming at the Zobtenberg on the horizon [gs1904] [carlyle]. It passes west of the Schleier-, Butter- and Sophienberg, low swells that hide it from the Austrian line; 25 hussar squadrons screen it on the ridge, with the king riding among them, and ammunition wagons march between the lines [gs1904]. From the Frobelwitz heights the Austrians see the turn south but not the march; Daun remarks 'the good folk are slipping off, let them go' [gs1904] [carlyle]. Driesen's cavalry stays behind the rises to cover the left [gs1904].",
        ("Using dead ground", "Ground the enemy cannot see. In 1904 officers on the Breslauer Berg could not see a white flag carried along the line of march [gs1904].", "dead-ground"),
        gA(1950, 1450), 9, conf="high", cite=["gs1904", "carlyle", "gs12a"], fog=0.3,
        arrows=[A("pr", "move", gA(1870, 1060), gA(1860, 1400), gA(1880, 1720)), A("pr", "move", gA(1830, 1060), gA(1820, 1400), gA(1840, 1700))],
        events=[(gA(1990, 1450), "Hussar screen on the ridge, the king with it", ["gs1904"]), ("Sophienberg", "Columns hidden behind the rises", ["gs1904"])])
B.phase("12:30", "Deploy", "The line forms south of Lobetinz",
        "Soon after noon the head of the columns reaches Schriegwitz. The platoons wheel left and the army stands in two lines facing north-east between the Wachberg and Schriegwitz, at an angle to Nádasdy's flank [gs1904] [gs12a]. Zieten's 53 squadrons form round and beyond Schriegwitz, guarded by Bevern's six battalions; Driesen stands north of the Heideberg facing east; three battalions under Wedel are posted ahead of the right as the 'Attacke', with the ten Brummers beside them [gs1904]. The king takes post on the Wachberg [gs1904].",
        ("Oblique order", "The whole weight of the army stands opposite the end of the enemy line, while the rest of it is held back out of reach [gs1904].", "oblique-order"),
        gA(2150, 1950), 6.5, conf="high", cite=["gs1904", "gs12a"], fog=0.1,
        arrows=[A("pr", "move", "Schriegwitz", gA(2500, 2150))],
        events=[("Wachberg", "Frederick on the Wachberg", ["gs1904"]), (wedelP, "Wedel's 'Attacke'", ["gs1904", "gs12a"])])
B.phase("13:00", "Attack", "Wedel storms the Kiefernberg",
        "At about one o'clock, with barely four hours of daylight left, Wedel's three battalions advance half-right on the wooded Kiefernberg south of Sagschütz [gs1904]. The Brummers open from the start and then fire from the Glanzberg. Past a wet ditch 300 paces short of the hill Wedel fires one volley and goes in with the bayonet; three Württemberg battalions there give way, and the Württembergers to their left and three grenadier battalions in the Faulbusch fall back too [gs1904] [gs12a]. On the extreme right Nádasdy's 43 squadrons charge Zieten, and Bevern's battalions stop them with musketry and canister [gs1904]. Behind Wedel the infantry follows battalion by battalion, each 50 paces behind the one to its right [gs1904] [carlyle].",
        ("Echelon attack", "Each battalion stepped off a little after the one beside it, so the line struck the enemy flank first at its strongest end and kept coming [gs1904] [carlyle].", "echelon"),
        gA(2450, 1950), 4.8, conf="high", cite=["gs1904", "gs12a", "carlyle"],
        debate="Some Austrian reports say the Württembergers all turned at once crying 'Long live the King of Prussia'. The Kiefernberg garrison lost 20% before falling back, so this is untrue of it, though the contingent fought reluctantly and lost very many missing [gs1904].",
        arrows=[A("pr", "charge", wedelP, B.pos("Kiefernberg")), A("pr", "fire", "Glanzberg", B.pos("Kiefernberg")), A("au", "charge", gA(2740, 2120), gA(2600, 2160)),
                A("pr", "fire", gA(2560, 2150), gA(2700, 2130))],
        events=[("Kiefernberg", "Wedel's bayonets take the Württemberg guns", ["gs1904"]), (gA(2620, 2150), "Nádasdy's cavalry stopped by Bevern", ["gs1904"])])
B.phase("14:00", "Roll-up", "Nádasdy's corps is rolled up",
        "North of the Kiefernberg three Austrian regiments pushed in front of the Bavarians give way, and the whole of Nádasdy's infantry streams back [gs1904]. The echelons come on 'with the regularity of clockwork', the guns on the Judenberg firing into infantry packed three lines deep [gs1904]. Wedel and Kremzow's grenadiers take the battery on the Kirchberg; Nádasdy rallies behind the Gohlau ditch, and Bevern's battalions outflank him again [gs1904]. Zieten leads his squadrons between the Faulbusch and the Gohlau ponds; Lentulus takes fifteen guns, and Zieten's hussars about 2,000 prisoners [gs1904].",
        ("Combined arms", "Infantry fire held Nádasdy's horse off Zieten's flank; then Zieten's charges caught the infantry as it tried to re-form [gs1904].", "combined-arms"),
        gA(2700, 1850), 5.2, conf="medium", cite=["gs1904", "gs12a", "beaulieu"],
        arrows=[A("pr", "charge", gA(2700, 2000), gA(2800, 1850), gA(2900, 1720)), A("pr", "move", along(F1, 0.5), along(L6a, 0.6)),
                A("rc", "retreat", gA(2600, 1900), gA(2900, 1700), gA(3150, 1500)), A("pr", "fire", "Judenberg", gA(2560, 1800))],
        events=[("Kirchberg", "Kirchberg battery taken", ["gs1904"]), (gA(2800, 1790), "Nádasdy rallies behind the Gohlau ditch", ["gs1904"]),
                (gA(2740, 2010), "Zieten charges past the ponds", ["gs1904"])])
B.phase("15:00", "Wheel", "The Austrians try to face south",
        "Too late, Charles sees that Nádasdy's appeals were justified. He orders a general wheel to the left with Leuthen as the pivot and sends the reserve back south through the village; it arrives breathless and in disorder, and Arenberg tries to form a front south of Leuthen with a refused flank [gs1904] [gs12b]. The manoeuvre, done in haste against a stream of fugitives, crowds the infantry together north of the village, in places a hundred ranks deep [gs1904]. Every gun that can be brought up unlimbers on the windmill height [gs1904]. The Prussian line comes on towards Leuthen from the south.",
        ("Change of front under attack", "A long line turned to face a new threat crowds towards the pivot and loses its order; at Leuthen the Austrians could no longer use their numbers [gs1904].", "change-of-front"),
        gB(2550, 1450), 6, conf="medium", cite=["gs1904", "gs12b"],
        arrows=[A("au", "move", gA(2620, 820), "Frobelwitz", gB(2525, 1472)), A("au", "move", along(AC1, 0.3), gB(2250, 1080)), A("pr", "move", along(L6a, 0.5), along(A1, 0.4))],
        events=[(gB(2525, 1472), "Arenberg's reserve tries to form south of Leuthen", ["gs1904", "gs12b"]), ("Windmill height", "Austrian guns on the windmill height", ["gs1904"])])
B.phase("15:30", "Leuthen", "The storm of Leuthen",
        "At about half past three the Prussian infantry storms the 1,800-pace front of Leuthen [gs1904]. The Würzburg battalion in the walled churchyard of the Catholic church sweeps the road from Schriegwitz with guns and muskets; the Garde and Retzow's grenadiers attack it in vain until the third battalion of the Garde under Captain von Möllendorff forces the west gate, and a breach is shot in the south wall [gs1904] [wiki]. After half an hour of fighting among the farmyards and hedges the village is clear [gs1904]. West of it the Prussian left comes up level with the refused Austrian right and stands in a firefight under the guns on the windmill height; some battalions waver until one from the second line steadies them, and the king brings the left-wing battery and the Brummers to the Butterberg [gs1904].",
        ("Defending villages and strongpoints", "A walled churchyard made a fortress; it held up the Prussian centre for half an hour while the Austrians tried to form behind it [gs1904].", "strongpoint-defence"),
        gB(2550, 1440), 3.6, conf="high", cite=["gs1904", "gs12b", "wiki", "carlyle"],
        arrows=[A("pr", "charge", gB(2553, 1520), gB(2553, 1460)), A("pr", "charge", gB(2470, 1500), gB(2530, 1455)), A("pr", "fire", gB(2240, 1455), "Windmill height"),
                A("au", "fire", "Windmill height", gB(2290, 1440))],
        events=[(gB(2553, 1451), "Leuthen churchyard: Möllendorff forces the west gate", ["gs1904", "wiki"]), (gB(2222, 1438), "Prussian guns on the Butterberg", ["gs1904"])])
B.phase("16:15", "Stalemate", "The battle stands north of Leuthen",
        "Beyond the village the Prussian line, much thinned and short of breath, comes up against the deep ditch along the north edge of Leuthen and a dense, mostly fresh Austrian mass behind it, including the grenadiers [gs1904]. Moritz's nine battalions on the right outflank it again, but 'the battle stood; the short day was ending' [gs1904]. On the Austrian right more than 70 squadrons under Lucchesi and Serbelloni have gathered south-east of Gross-Heidau; Lucchesi now leads them out to fall on the Prussian left between the Butterberg and Leuthen, without scouting south [gs1904] [gs12b].",
        ("Committing the reserve", "Lucchesi's cavalry was the Austrians' last intact force; thrown in without a look at what lay behind the rises, it rode into a trap [gs1904].", "reserve-commitment"),
        gB(2350, 1330), 5.5, conf="medium", cite=["gs1904", "gs12b"],
        debate="The 1904 history gives no time for Lucchesi's charge. The map puts it at about 16:15-16:30, after the half-hour village fight that began about 15:30 and before full dark (sunset was about 16:00). Wikipedia's claim that Lucchesi was decapitated by a cannonball is not in the 1904 account, which says only that he fell in the melee [gs1904] [wiki].",
        arrows=[A("au", "move", gB(2300, 1170), gB(2122, 1270), gB(2200, 1380)), A("pr", "fire", along(N9, 0.4), along(CF1, 0.4)), A("pr", "move", gB(1998, 1442), gB(1985, 1300))],
        events=[(gB(2300, 1170), "Lucchesi's 70 squadrons move out", ["gs1904", "gs12b"]), ("Sophienberg", "Driesen watches from the Sophienberg", ["gs1904"])])
B.phase("16:30", "Driesen", "Driesen's charge breaks the Austrian army",
        "Driesen, watching from the Sophienberg, wheels his 50 squadrons left, moves north behind the rises until he overlaps the Austrian horse, then wheels right and appears on the heights in its flank: 15 cuirassier squadrons and the Bayreuth Dragoons in front, 15 cuirassier squadrons behind, the Puttkamer Hussars overlapping on the left into the rear [gs1904] [gs12b]. Prince Eugen of Württemberg's 30 squadrons join in. Lucchesi is killed; his squadrons flee into their own infantry, and the Austrian right breaks in panic, whole battalions throwing down their muskets [gs1904] [wiki]. Wallis and Baden-Durlach make a last stand on the windmill height and are ridden down; Schenckendorff's grenadiers take the guns there; Angelelli's free battalions come up from Borne [gs1904].",
        ("Shock cavalry", "Cavalry kept back and hidden struck an enemy already committed to a charge of its own, in the flank. The defeated horse then disrupted its own infantry [gs1904] [kriemann].", "shock-cavalry"),
        gB(2250, 1270), 4.8, conf="medium", cite=["gs1904", "gs12b", "wiki"],
        arrows=[A("pr", "charge", gB(1985, 1300), gB(2095, 1228), gB(2200, 1260)), A("pr", "charge", gB(1960, 1250), gB(2160, 1185), gB(2280, 1200)),
                A("au", "retreat", gB(2300, 1200), gB(2550, 1150), gA(3190, 1190)), A("pr", "charge", gB(2050, 1100), gB(2470, 1335))],
        events=[(gB(2150, 1260), "Lucchesi killed", ["gs1904"]), ("Windmill height", "Wallis and Baden-Durlach overrun", ["gs1904"])])
B.phase("18:00", "Lissa", "Flight to the Weistritz; the king at Lissa",
        "The beaten army pours over Saara and Klein-Heidau to the Weistritz bridges, where Nádasdy holds the crossings long enough for many to escape [gs1904]. The Prussian infantry halts north of the Breslau road. About six o'clock, in falling snow and darkness, Frederick takes three grenadier battalions and the Seydlitz Cuirassiers to Lissa, a lantern-bearing innkeeper beside his horse; there is a last fight for the bridges east of the town shortly before seven, and the king spends the night in the Schloss [gs1904]. The Prussians have lost about 6,400 men; the Austrians about 22,000, more than half of them prisoners, with 131 guns and 55 colours and standards [gs1904] [wiki].",
        ("Pursuit", "Darkness and the river line saved the Austrian army from destruction, but its losses in the following days made Leuthen the most complete victory of the war [gs1904].", "pursuit"),
        gA(3300, 1200), 9, conf="medium", cite=["gs1904", "gs12b", "wiki"],
        debate="The Prussian army is said to have sung the hymn 'Nun danket alle Gott' in the dark: the 1904 history says individual men began it during the night march to Lissa and it spread from regiment to regiment. Historians since (Kroener 2000) have traced how it grew into a national myth, and Wikipedia calls it likely apocryphal [gs1904] [wiki]. The story that Frederick walked into the Lissa Schloss full of Austrian officers and bluffed his way out with 'Bon soir, Messieurs' is a legend [gs1904].",
        arrows=[A("au", "retreat", gB(2700, 1200), "Saara", gA(3675, 1265)), A("pr", "move", "Saara", "Lissa"), A("au", "retreat", gA(3200, 1350), gA(3440, 1585), mv(B.pos("Lissa"), 120, 1500))],
        events=[("Lissa", "Fight for the Lissa bridges; the king in the Schloss", ["gs1904"]), (along(END, 0.5), "Prussian army camps on the snow", ["gs1904"])])

B.export()
