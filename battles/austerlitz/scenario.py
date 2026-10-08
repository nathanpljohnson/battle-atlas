"""Austerlitz, 2 December 1805. See brief.md for sources, choices and confidence.
Positions are mostly given in pixel coordinates of the West Point map series (maps 22-24, 1920 px wide),
converted with georef.wp(); phases 0-8 are 07:00 ... 16:30.
"""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "..", "tools"))
sys.path.insert(0, HERE)
os.chdir(HERE)
from battlekit import Battle
from georef import wp

B = Battle("austerlitz", HERE)

# ---------------- meta
B.meta = {
    "title": "Austerlitz", "year": "1805",
    "eyebrow": "2 December 1805 · Moravia · War of the Third Coalition",
    "subtitle": "Napoleon lets the Russians and Austrians attack his weak right, then breaks their centre on the Pratzen heights.",
    "sides": {
        "fr": {"name": "French", "top": "#2c4a8c", "side": "#1d3363", "mark": "#f3efe4", "arrow": "#3f73dd", "flag": "#2c4a8c"},
        "ru": {"name": "Russian", "top": "#2f5b3a", "side": "#1f3e27", "mark": "#f1ead8", "arrow": "#d24a35", "flag": "#2f5b3a"},
        "au": {"name": "Austrian", "top": "#efebe1", "side": "#b7b1a2", "mark": "#3a2a18", "arrow": "#e8735a", "flag": "#efebe1"},
    },
    "belligerents": [
        {"name": "Grande Armée", "commander": "Napoleon I", "sides": ["fr"], "code": "letters"},
        {"name": "Russo-Austrian army", "commander": "Kutuzov, with Alexander I and Francis II", "sides": ["ru", "au"], "code": "numbers"},
    ],
    "forces": {
        "start": [{"label": "French", "n": 73000, "segs": [["fr", 1]]}, {"label": "Allies", "n": 85000, "segs": [["ru", 0.72], ["au", 0.28]]}],
        "end": [{"label": "French", "n": 9000, "segs": [["fr", 1]]}, {"label": "Allies", "n": 27000, "segs": [["ru", 0.78], ["au", 0.22]]}],
    },
    "sun": {"lat": 49.14, "decl": -21.9, "note": "Sunrise about 07:50, sunset about 16:10."},
    "view": {"az": -0.42, "el": 0.7},
    "unitScale": 2.1, "unitLabelDist": 13,
    "ground": {"season": "winter", "relief": 130},
    "method": "Unit positions were read off the U.S. Military Academy situation maps for 18:00 on 1 December and 09:00 and 14:00 on 2 December, after georeferencing them against fifteen village locations (most within 300 m). They were checked against the maps in the 1844 Russian official history, and the times in between were filled in from four written accounts. Where the sources disagree, the brief records the choice made; every unit and moment carries a confidence level.",
    "sources": [
        {"label": "U.S. Military Academy, Dept. of History: Austerlitz situation maps 22-24", "url": "https://commons.wikimedia.org/wiki/Category:Maps_of_the_Battle_of_Austerlitz", "note": "positions at 18:00 (1 Dec), 09:00 and 14:00"},
        {"label": "A. I. Mikhailovsky-Danilevsky, Description of the First War of Emperor Alexander with Napoleon in 1805 (St Petersburg, 1844), maps 6-8", "url": "https://commons.wikimedia.org/wiki/Category:Maps_of_the_Battle_of_Austerlitz", "note": "Russian official history; independent check of Allied positions and the end state"},
        {"label": "Fondation Napoléon: Austerlitz, 2 December 1805, a timeline", "url": "https://www.napoleon.org/en/history-of-the-two-empires/timelines/austerlitz-2-december-1805-a-timeline/", "note": "times"},
        {"label": "Wikipedia: Battle of Austerlitz", "url": "https://en.wikipedia.org/wiki/Battle_of_Austerlitz", "note": "strengths and losses ranges; summary of Chandler, Duffy, Goetz"},
        {"label": "Warhistory.org: Battle of Austerlitz, parts I-II", "url": "https://warhistory.org/article/battle-of-austerlitz-2-december-1805-part-i?amp=0", "note": "brigade-level detail on the Pratzen and the retreat"},
        {"label": "Den of Geek: The real history of Napoleon's greatest victory", "url": "https://www.denofgeek.com/movies/real-history-napoleon-greatest-victory-didnt-happen", "note": "pond-draining evidence against the ice legend"},
        {"label": "AWS Terrain Tiles; OpenStreetMap Nominatim", "url": "https://registry.opendata.aws/terrain-tiles/", "note": "elevation and village locations"},
    ],
    "notes": "The Satschan, Menitz and Kobelnitz ponds were drained in the 19th century and are drawn from the West Point maps. Heights are exaggerated about three times; roads and woods are illustrative. Allied columns are drawn as single masses, as the sources map them.",
}

# ---------------- places (historical names; modern Czech in brief.md)
for n in ["Telnitz", "Sokolnitz", "Kobelnitz", "Puntowitz", "Schlappanitz", "Girzikowitz", "Pratzen", "Blasowitz", "Holubitz",
          "Bosenitz", "Welatitz", "Kowalowitz", "Krzenowitz", "Hostieradek", "Aujezd", "Satschan", "Menitz", "Zbysov", "Bellowitz"]:
    B.place(n)
B.place("Austerlitz", size=1.8)
B.place("Posoritz post house", B.geo["Posoritz post"], size=0.4)
B.place("Sokolnitz castle", B.geo["Sokolnitz castle"], size=0.35)
B.hill("Santon", B.geo["Santon"])
B.hill("Zuran", B.geo["Zuran"])
B.hill("Pratzen heights", B.geo["Pratzeberg"])
B.hill("Staré Vinohrady", wp(1140, 690))

B.roads = [
    [wp(560, 395), wp(800, 400), "Bosenitz", wp(1250, 390), "Posoritz post house", wp(1600, 300)],
    ["Posoritz post house", wp(1500, 500), "Austerlitz"],
    ["Schlappanitz", "Girzikowitz", "Blasowitz", "Holubitz"],
    ["Puntowitz", "Pratzen", "Krzenowitz", "Austerlitz"],
    ["Kobelnitz", "Pratzen"], ["Sokolnitz", "Telnitz", "Menitz"], ["Telnitz", "Aujezd", "Hostieradek", "Krzenowitz"],
    ["Sokolnitz", "Kobelnitz", "Puntowitz", "Schlappanitz", "Bellowitz"], ["Aujezd", "Satschan"], ["Pratzen", "Zbysov"],
    ["Blasowitz", "Pratzen"], ["Girzikowitz", "Welatitz"],
]
B.woods = [[*wp(1180, 980), 500, 260], [*wp(1300, 900), 360, 220], [*wp(980, 300), 280, 180]]
P = lambda pts: [list(wp(x, y)) for x, y in pts]
B.water["lakes"] = [
    P([(760, 1188), (790, 1165), (840, 1146), (900, 1142), (950, 1150), (980, 1172), (985, 1192), (960, 1203), (915, 1196), (880, 1182), (848, 1176), (815, 1190), (790, 1212), (765, 1215)]),
    P([(648, 1238), (705, 1238), (760, 1258), (785, 1300), (792, 1380), (775, 1445), (705, 1452), (655, 1425), (640, 1340)]),
    P([(842, 732), (860, 716), (872, 760), (866, 805), (858, 842), (834, 850), (818, 820), (824, 770)]),
    P([(1470, 770), (1500, 735), (1545, 712), (1555, 735), (1520, 775), (1490, 815), (1470, 830)]),
]
B.water["rivers"] = [
    {"p": P([(905, 540), (898, 640), (887, 715), (880, 800), (862, 880), (836, 950), (800, 1020), (760, 1082), (722, 1140), (690, 1192), (662, 1240)]), "w": 3},
    {"p": P([(1660, 690), (1600, 712), (1555, 728), (1505, 790), (1420, 830), (1320, 895), (1220, 980), (1120, 1070), (1040, 1120), (985, 1170)]), "w": 4},
    {"p": P([(1130, 800), (1043, 770), (965, 742), (898, 725)]), "w": 2},
    {"p": P([(1190, 545), (1120, 548), (1040, 545), (985, 530), (905, 540)]), "w": 2},
]
B.water["labels"] = {"Satschan pond": wp(880, 1165), "Menitz pond": wp(715, 1350), "Goldbach": wp(835, 905), "Littawa": wp(1300, 905)}

# ---------------- units
def U(uid, side, typ, name, strength, frontage, keys, note="", conf="medium", **kw):
    u = B.unit(uid, side, typ, name, strength, frontage, note=note, conf=conf, **kw)
    for ph, (x, y, f, form) in keys.items():
        u.at(ph, wp(x, y), f, form)

# French: right wing (Legrand, Davout)
U("leg1", "fr", "inf", "3e Ligne & Tirailleurs du Po", "Legrand's division · 3 bns", 700,
  {0: (748, 1095, 110, "F"), 1: (705, 1105, 90, "L"), 2: (720, 1100, 90, "L"), 6: (735, 1100, 95, "F"), 7: (760, 1100, 110, "F"), 8: (770, 1105, 110, "L")},
  "Held Telnitz against Kienmayer from 07:00 until Dokhturov's column arrived.", "high")
U("leg2", "fr", "inf", "26e Léger & Tirailleurs corses", "Legrand's division · 4 bns", 700,
  {0: (782, 1032, 100, "F"), 1: (765, 1035, 100, "F"), 2: (742, 1030, 90, "L"), 3: (758, 1030, 90, "F"), 4: (750, 1020, 90, "L"), 7: (785, 1035, 95, "F"), 8: (795, 1040, 100, "L")},
  "Defended Sokolnitz village, which changed hands several times.", "high")
U("leg3", "fr", "inf", "Levasseur's brigade (18e, 75e Ligne)", "Legrand's division · 4 bns", 650,
  {0: (800, 850, 120, "L"), 1: (790, 930, 160, "C"), 2: (782, 962, 100, "F"), 6: (800, 985, 100, "F"), 7: (820, 995, 90, "F"), 8: (825, 1000, 90, "L")},
  "Legrand's reserve, fed into the fight for Sokolnitz castle.", "medium")
U("fri1", "fr", "inf", "Heudelet's brigade (108e Ligne, 15e Léger)", "Friant's division, III Corps · 4 bns", 600,
  {0: (585, 1140, 50, "C"), 1: (708, 1108, 80, "F"), 2: (728, 1098, 90, "L"), 3: (722, 1085, 90, "L"), 7: (758, 1092, 110, "F"), 8: (775, 1100, 110, "L")},
  "Davout's advance guard. After marching about 110 km in two days it retook Telnitz around 08:00, then was driven out again by Austrian hussars.", "high")
U("fri2", "fr", "inf", "Friant's division (Kister, Lochet)", "III Corps · 6 bns", 900,
  {0: (560, 1175, 45, "C"), 1: (630, 1105, 55, "C"), 2: (700, 1050, 75, "L"), 3: (742, 1015, 85, "F"), 7: (788, 1028, 95, "F"), 8: (800, 1040, 100, "L")},
  "Retook Sokolnitz and held the Goldbach line all day against twice its numbers.", "high")
U("bou", "fr", "cav", "Bourcier's dragoons", "Attached to III Corps · 12 sqns", 600,
  {0: (540, 1110, 50, "C"), 1: (690, 1088, 80, "L"), 8: (690, 1085, 80, "L")},
  "Covered Davout's arrival on the right.", "medium")

# French: centre (Soult's IV Corps)
U("sh1", "fr", "inf", "Morand's brigade (10e Léger)", "St Hilaire's division · 2 bns", 450,
  {0: (930, 760, 90, "C"), 2: (1030, 775, 100, "C"), 3: (1085, 838, 140, "F"), 5: (1082, 848, 140, "L"), 6: (1020, 930, 200, "C"), 7: (990, 1035, 190, "F"), 8: (1000, 1058, 180, "L")},
  "Led St Hilaire's climb, bypassing Pratzen village towards the summit.", "medium")
U("sh2", "fr", "inf", "Thiébault's brigade (14e, 36e Ligne)", "St Hilaire's division · 4 bns", 650,
  {0: (925, 790, 90, "C"), 2: (1015, 800, 110, "C"), 3: (1060, 860, 150, "F"), 5: (1060, 870, 150, "L"), 6: (968, 950, 210, "C"), 7: (930, 1000, 220, "F"), 8: (905, 1010, 220, "L")},
  "Nearly out of ammunition on the Pratzeberg before a bayonet charge broke Kamensky.", "medium")
U("sh3", "fr", "inf", "Varé's brigade (43e, 55e Ligne)", "St Hilaire's division · 4 bns", 650,
  {0: (915, 820, 90, "C"), 2: (1000, 822, 110, "C"), 3: (1040, 880, 160, "L"), 4: (1045, 885, 160, "F"), 6: (1060, 960, 190, "C"), 7: (1050, 1048, 190, "F"), 8: (1050, 1068, 180, "L")}, "", "medium")
U("va1", "fr", "lt", "Schiner's brigade (24e Léger)", "Vandamme's division · 2 bns", 450,
  {0: (920, 650, 90, "C"), 2: (1050, 660, 60, "C"), 3: (1130, 642, 60, "F"), 4: (1168, 642, 60, "F"), 5: (1118, 662, 240, "R"), 6: (1062, 760, 180, "C"), 7: (1082, 960, 180, "C"), 8: (1100, 1060, 180, "F")},
  "Broken by the Russian Guard cavalry around 13:00, then re-formed for the afternoon sweep south.", "medium")
U("va2", "fr", "inf", "Ferey's brigade (4e, 28e Ligne)", "Vandamme's division · 4 bns", 650,
  {0: (915, 680, 90, "C"), 2: (1040, 690, 70, "C"), 3: (1115, 680, 70, "F"), 4: (1160, 680, 70, "F"), 5: (1108, 692, 240, "R"), 6: (1070, 800, 180, "C"), 7: (1120, 1000, 190, "C"), 8: (1130, 1068, 180, "F")},
  "A battalion of the 4e Ligne lost its eagle to the Russian Guard, the only French eagle lost that day.", "medium")
U("va3", "fr", "inf", "Candras's brigade (46e, 57e Ligne)", "Vandamme's division · 4 bns", 650,
  {0: (905, 705, 90, "C"), 2: (1030, 720, 80, "C"), 3: (1100, 720, 80, "L"), 4: (1140, 720, 80, "F"), 5: (1140, 720, 60, "F"), 6: (1110, 850, 170, "C"), 7: (1150, 1010, 180, "C"), 8: (1160, 1060, 190, "F")},
  "In the afternoon Vandamme's guns fired from above Aujezd onto the retreat around the ponds.", "medium")

# French: north and reserves
U("ber1", "fr", "inf", "Rivaud's division", "Bernadotte's I Corps · 6 bns", 800,
  {0: (830, 470, 90, "C"), 1: (880, 560, 120, "C"), 2: (985, 600, 100, "C"), 3: (1060, 600, 100, "L"), 4: (1110, 600, 100, "L"), 5: (1130, 610, 100, "L"), 6: (1200, 640, 110, "L"), 7: (1280, 680, 110, "L"), 8: (1300, 690, 110, "L")},
  "Bernadotte's advance was slow; many historians criticise his passivity.", "medium")
U("ber2", "fr", "inf", "Drouet's division", "Bernadotte's I Corps · 6 bns", 800,
  {0: (840, 500, 90, "C"), 1: (890, 590, 120, "C"), 2: (990, 630, 110, "C"), 3: (1060, 640, 110, "L"), 4: (1100, 650, 100, "L"), 5: (1150, 665, 70, "F"), 6: (1210, 700, 110, "L"), 7: (1300, 730, 110, "L"), 8: (1320, 745, 110, "L")},
  "Gave the French cavalry a line to rally behind during the Guard battle.", "medium")
U("gdi", "fr", "gd", "Imperial Guard infantry", "Foot Grenadiers & Chasseurs · 8 bns", 700,
  {0: (760, 470, 120, "L"), 2: (850, 520, 110, "C"), 3: (950, 640, 120, "C"), 4: (990, 700, 110, "L"), 5: (1050, 700, 90, "L"), 6: (990, 705, 90, "L"), 7: (1020, 760, 150, "L")},
  "Napoleon's last reserve. Barely engaged.", "medium")
U("gdc", "fr", "cav", "Imperial Guard cavalry (Bessières, Rapp)", "Chasseurs, Horse Grenadiers, Mamelukes · 12 sqns", 600,
  {0: (780, 450, 120, "L"), 2: (860, 500, 110, "C"), 3: (960, 620, 110, "C"), 4: (1020, 660, 90, "L"), 5: (1150, 642, 60, "L"), 6: (1080, 680, 90, "L"), 7: (1100, 700, 120, "L")},
  "Rapp's charge against the Russian Guard cavalry around 13:00 decided the fight for Staré Vinohrady.", "medium")
U("gren", "fr", "gd", "Grenadier division (Oudinot's grenadiers, under Duroc)", "Combined grenadiers · 10 bns", 800,
  {0: (800, 520, 110, "L"), 2: (880, 600, 120, "C"), 3: (950, 700, 130, "C"), 4: (995, 780, 130, "L"), 5: (995, 810, 130, "L")},
  "In reserve behind the Pratzen attack.", "medium")
U("kel", "fr", "lc", "Kellermann's light cavalry", "Murat's Cavalry Reserve · 12 sqns", 600,
  {0: (980, 470, 90, "L"), 2: (1080, 500, 80, "L"), 3: (1150, 520, 80, "L"), 4: (1080, 510, 90, "L"), 5: (1150, 490, 80, "L"), 6: (1230, 480, 80, "L"), 7: (1300, 470, 70, "L"), 8: (1320, 460, 70, "L")},
  "Took the first shock of Liechtenstein's charge and fell back through Caffarelli's infantry.", "medium")
U("nan", "fr", "cav", "Nansouty's heavy cavalry", "Carabiniers & cuirassiers · 12 sqns", 600,
  {0: (960, 500, 90, "C"), 2: (1050, 520, 90, "L"), 3: (1120, 540, 90, "L"), 4: (1180, 540, 90, "L"), 5: (1220, 520, 70, "L"), 6: (1260, 500, 70, "L"), 7: (1330, 470, 60, "L")},
  "Counter-charged Liechtenstein's cavalry near Blasowitz.", "medium")
U("hau", "fr", "cav", "d'Hautpoul's cuirassiers", "Murat's Cavalry Reserve · 12 sqns", 600,
  {0: (950, 450, 90, "C"), 2: (1040, 470, 80, "C"), 3: (1100, 480, 80, "L"), 4: (1160, 490, 70, "L"), 5: (1220, 470, 60, "L"), 6: (1250, 450, 60, "L"), 7: (1300, 430, 60, "L")}, "", "medium")
U("suc", "fr", "inf", "Suchet's division", "Lannes' V Corps · 10 bns", 900,
  {0: (1060, 430, 90, "L"), 2: (1110, 415, 90, "L"), 3: (1150, 415, 80, "F"), 4: (1180, 410, 80, "F"), 5: (1200, 410, 70, "F"), 6: (1195, 402, 70, "F"), 7: (1260, 390, 60, "L"), 8: (1300, 380, 60, "L")},
  "Pushed Bagration slowly back along the Olmütz road.", "medium")
U("caf", "fr", "inf", "Caffarelli's division", "Lannes' V Corps · 9 bns", 900,
  {0: (940, 450, 120, "C"), 1: (1000, 500, 110, "C"), 2: (1080, 545, 90, "L"), 3: (1110, 555, 90, "F"), 4: (1150, 540, 80, "F"), 5: (1190, 470, 70, "F"), 6: (1205, 440, 70, "F"), 7: (1260, 440, 60, "L"), 8: (1300, 440, 60, "L")},
  "Its squares and volleys stopped Liechtenstein's cavalry near Blasowitz.", "medium")
U("san", "fr", "lt", "Claparède's brigade (17e Léger) on the Santon", "Suchet's division · 3 bns", 280,
  {0: (1062, 382, 60, "L"), 3: (1062, 382, 60, "F"), 6: (1062, 382, 60, "L")},
  "Ordered to hold the fortified Santon hill to the last man.", "high")
U("sanb", "fr", "art", "Santon battery", "18 guns", 220,
  {0: (1078, 374, 60, "L"), 3: (1078, 374, 60, "F"), 6: (1078, 374, 60, "L")},
  "Anchored the French left on the Olmütz road.", "high")

# Allies: left wing (Buxhöwden)
U("kie1", "au", "lt", "Kienmayer's infantry (Szekler Grenzer)", "Austrian advance guard · 5 bns", 500,
  {0: (802, 1095, 270, "F"), 1: (790, 1100, 270, "F"), 3: (820, 1110, 260, "L"), 6: (850, 1130, 250, "L"), 7: (880, 1190, 200, "R"), 8: (985, 1240, 120, "R")},
  "Opened the battle at 07:00 with attacks on Telnitz.", "high")
U("kie2", "au", "lc", "Kienmayer's hussars & chevaulegers", "Austrian advance guard · 20 sqns", 550,
  {0: (852, 1122, 270, "L"), 1: (800, 1125, 280, "L"), 2: (772, 1120, 280, "L"), 3: (860, 1150, 270, "L"), 7: (900, 1210, 160, "R"), 8: (1005, 1252, 120, "R")},
  "The Hessen-Homburg hussars drove Davout's first troops back out of Telnitz.", "medium")
U("col1", "ru", "inf", "1st Column (Dokhturov)", "Russian · 24 bns, ≈13,800", 1200,
  {0: (930, 1050, 240, "C"), 1: (812, 1085, 260, "F"), 2: (792, 1095, 270, "F"), 3: (780, 1095, 270, "F"), 4: (790, 1090, 270, "L"), 6: (840, 1100, 90, "L"), 7: (872, 1170, 160, "R"), 8: (960, 1230, 120, "R")},
  "Took Telnitz but was then held at the Goldbach for most of the day; it escaped by the causeway between the ponds.", "high")
U("col2", "ru", "inf", "2nd Column (Langeron)", "Russian · 11 bns, ≈8,000", 1000,
  {0: (980, 1000, 240, "C"), 1: (840, 1040, 250, "C"), 2: (812, 1035, 260, "F"), 3: (792, 1035, 270, "F"), 4: (786, 1030, 270, "F"), 6: (830, 1040, 90, "L"), 7: (902, 1110, 150, "R"), 8: (1000, 1200, 130, "R")},
  "Delayed at dawn when Liechtenstein's cavalry crossed its line of march. Langeron got five of his nine remaining battalions away.", "high")
U("kam", "ru", "inf", "Kamensky's brigade", "2nd Column · 5 bns", 500,
  {0: (1010, 950, 230, "C"), 1: (1000, 930, 230, "C"), 2: (1030, 880, 30, "C"), 3: (1062, 890, 330, "F"), 4: (1080, 930, 340, "F"), 5: (1150, 990, 150, "R"), 6: (1200, 1030, 120, "R"), 7: (1230, 1010, 90, "L")},
  "Turned back on its own initiative to fight for the Pratzeberg, and ended the day at Hostieradek (Russian official map).", "medium")
U("col3", "ru", "inf", "3rd Column (Przhebyshevsky)", "Russian · 9 bns, ≈7,700", 800,
  {0: (1020, 920, 240, "C"), 1: (870, 980, 250, "C"), 2: (822, 975, 260, "F"), 3: (806, 975, 270, "F"), 6: (820, 990, 0, "F"), 7: (830, 960, 20, "R")},
  "Cut off at Sokolnitz when Soult swung south; most of it was captured.", "high")
# Allies: centre (4th Column, Kolowrat and Miloradovich, with Kutuzov)
U("milo", "ru", "inf", "4th Column, Russian (Miloradovich)", "Russian · 12 bns", 800,
  {0: (1230, 760, 270, "C"), 1: (1150, 760, 270, "C"), 2: (1082, 760, 260, "F"), 3: (1120, 730, 250, "F"), 4: (1170, 720, 250, "R"), 5: (1280, 740, 100, "R"), 6: (1400, 740, 90, "R"), 7: (1480, 720, 90, "L"), 8: (1550, 700, 90, "L")},
  "Marched into St Hilaire's division at Pratzen village around 09:00 and was routed by 11:00.", "medium")
U("jur", "au", "inf", "Jurczik's brigade", "Kolowrat's Austrians · 8 bns", 700,
  {0: (1260, 800, 270, "C"), 1: (1180, 820, 260, "C"), 2: (1120, 830, 240, "L"), 3: (1100, 860, 240, "F"), 4: (1150, 880, 220, "R"), 5: (1300, 860, 100, "R"), 6: (1470, 780, 90, "L"), 8: (1560, 740, 90, "L")},
  "Many young recruits; briefly held the southern summit before giving way.", "medium")
U("rot", "au", "inf", "Rottermund's brigade", "Kolowrat's Austrians · 7 bns", 700,
  {0: (1280, 740, 270, "C"), 1: (1220, 720, 260, "C"), 2: (1172, 690, 250, "L"), 3: (1160, 682, 250, "F"), 4: (1180, 690, 240, "F"), 5: (1290, 700, 90, "R"), 6: (1480, 650, 90, "L"), 8: (1560, 620, 90, "L")},
  "Held Staré Vinohrady against Vandamme until outnumbered two to one.", "medium")
# Allies: right (Liechtenstein, Guard, Bagration)
U("lru", "ru", "cav", "5th Column: Russian cavalry", "Liechtenstein · ≈30 sqns", 800,
  {0: (1150, 800, 270, "C"), 1: (1180, 640, 0, "C"), 2: (1232, 560, 290, "L"), 3: (1170, 530, 280, "L"), 4: (1230, 520, 270, "R"), 5: (1350, 560, 90, "R"), 6: (1490, 640, 90, "L"), 7: (1520, 640, 90, "L")},
  "Charged Kellermann near Blasowitz and was stopped by Caffarelli's infantry and Nansouty's cuirassiers.", "medium")
U("lau", "au", "cav", "5th Column: Austrian cuirassiers (Hohenlohe)", "Liechtenstein · ≈20 sqns", 700,
  {0: (1180, 780, 270, "C"), 1: (1220, 650, 0, "C"), 2: (1292, 540, 290, "L"), 3: (1220, 520, 270, "L"), 4: (1250, 500, 270, "L"), 5: (1380, 520, 100, "R"), 6: (1500, 600, 90, "L"), 7: (1530, 600, 90, "L")}, "", "low")
U("rgi", "ru", "gd", "Russian Imperial Guard infantry", "Grand Duke Constantine · 10 bns", 800,
  {0: (1430, 770, 290, "C"), 1: (1330, 650, 300, "C"), 2: (1232, 572, 300, "L"), 3: (1220, 580, 270, "L"), 4: (1210, 620, 240, "L"), 5: (1182, 660, 250, "F"), 6: (1350, 720, 100, "R"), 7: (1480, 720, 90, "L"), 8: (1560, 700, 90, "L")},
  "Its bayonet charge at Staré Vinohrady broke a battalion of the 4e Ligne.", "medium")
U("rgc", "ru", "cav", "Russian Imperial Guard cavalry", "Chevalier Guards, Horse Guards, Guard Hussars · 17 sqns", 700,
  {0: (1450, 740, 290, "C"), 1: (1350, 640, 300, "C"), 2: (1252, 582, 300, "L"), 3: (1250, 600, 270, "L"), 4: (1230, 640, 260, "L"), 5: (1172, 650, 250, "L"), 6: (1330, 700, 100, "R"), 7: (1470, 690, 90, "L"), 8: (1550, 680, 90, "L")},
  "Took the eagle of the 4e Ligne before being beaten by Rapp's Guard cavalry.", "medium")
U("bagi", "ru", "inf", "Bagration's advance guard infantry", "Russian · ≈13 bns", 1000,
  {0: (1500, 330, 240, "C"), 1: (1400, 360, 250, "C"), 2: (1300, 385, 260, "L"), 3: (1262, 395, 260, "F"), 4: (1250, 400, 260, "F"), 5: (1290, 390, 260, "F"), 6: (1390, 350, 250, "L"), 7: (1450, 330, 240, "L"), 8: (1550, 300, 240, "L")},
  "Fought Lannes to a standstill for much of the day, then withdrew in good order towards Raussnitz.", "medium")
U("bagc", "ru", "lc", "Bagration's cavalry", "Hussars, Cossacks & dragoons · ≈30 sqns", 800,
  {0: (1520, 350, 240, "C"), 1: (1420, 400, 250, "L"), 2: (1322, 430, 260, "L"), 3: (1200, 380, 280, "L"), 4: (1300, 430, 260, "R"), 5: (1380, 400, 250, "L"), 6: (1420, 380, 250, "L"), 8: (1550, 330, 240, "L")},
  "Tried to get round the Santon and was stopped by its guns.", "low")

# ---------------- commanders
B.commander("nap", "fr", "Napoleon", {0: B.geo["Zuran"], 4: wp(1095, 860), 6: wp(1085, 985)},
            "Watched from the Zuran hill at dawn, then moved to the Pratzen heights and, in the afternoon, to St Anthony's chapel above Aujezd.")
B.commander("kut", "ru", "Kutuzov & the emperors", {0: wp(1300, 770), 2: wp(1180, 780), 4: wp(1330, 760), 6: wp(1520, 690), 8: wp(1640, 690)},
            "Kutuzov rode with the 4th Column and was wounded on the Pratzen.")

# ---------------- phases
A = B.arrow
B.phase("07:00", "Dawn & fog", "The Allies march into the trap",
        "Before sunrise, in thick fog, the Allied left (about 40,000 men in three columns plus Kienmayer's Austrian advance guard) starts down from the Pratzen heights towards Telnitz and Sokolnitz, where Napoleon has left only Legrand's thin division. Kienmayer attacks Telnitz first. Liechtenstein's cavalry, posted in the wrong place overnight, cuts across the columns and holds up Langeron. Soult's two divisions wait unseen in the fog of the Goldbach valley.",
        ("Bait", "Napoleon weakened his right on purpose and gave up the high ground, inviting the Allies to attack where he wanted them to. Every battalion they sent south was one fewer on the Pratzen."),
        wp(950, 900), 12,
        arrows=[A("au", "move", wp(880, 1110), wp(810, 1098)), A("ru", "move", wp(990, 1020), wp(900, 1060), wp(820, 1085)),
                A("ru", "move", wp(1040, 960), wp(920, 1010), wp(840, 1035)), A("ru", "move", wp(1060, 900), wp(930, 960), wp(840, 975)),
                A("ru", "move", wp(1150, 820), wp(1170, 720), wp(1200, 620)), A("fr", "move", wp(560, 1150), wp(640, 1120), wp(700, 1105))],
        events=[(wp(762, 1099), "Kienmayer attacks Telnitz, about 07:00"), (B.geo["Zuran"], "Napoleon on the Zuran hill"), (wp(900, 700), "Soult's corps hidden in the valley fog")],
        conf="high")
B.phase("08:00", "Telnitz falls", "The fight for the Goldbach villages",
        "Dokhturov's 1st Column joins Kienmayer and takes Telnitz. Davout's lead brigade, after a march of about 110 km in two days, arrives from the south-west and retakes it, only to be thrown out by Austrian hussars. Langeron and Przhebyshevsky attack Sokolnitz village and its castle, which change hands again and again. On the plateau the 4th Column begins to move off the heights as well.",
        ("Defending villages", "Stone farm buildings and walls let a few battalions hold off many times their number. Villages along a stream became small fortresses, which is why so few French held the Goldbach for so long."),
        wp(800, 1020), 7,
        arrows=[A("ru", "charge", wp(870, 1080), wp(800, 1090)), A("fr", "charge", wp(640, 1120), wp(705, 1105)),
                A("ru", "move", wp(900, 1035), wp(830, 1037)), A("ru", "move", wp(920, 980), wp(840, 976)), A("fr", "move", wp(800, 860), wp(790, 930))],
        events=[(wp(762, 1099), "Telnitz taken, retaken and lost again"), (wp(791, 972), "Sokolnitz castle changes hands")],
        conf="high")
B.phase("09:00", "Sun of Austerlitz", "Soult storms the Pratzen heights",
        "As the sun burns the mist off the high ground, Napoleon asks Soult how long he needs to reach the top: 'less than twenty minutes, Sire.' St Hilaire's division climbs towards Pratzen village and the Pratzeberg; Vandamme's heads for Staré Vinohrady. They run straight into Miloradovich's Russians and Kolowrat's Austrians, still in march column. In the north, Lannes, Murat and Bernadotte advance east as Bagration comes down the Olmütz road.",
        ("Attacking the centre", "The Allies had stripped their centre to strengthen the attack on the French right. A sudden blow at the weakened centre would split the Allied army in two."),
        wp(1050, 760), 8,
        arrows=[A("fr", "move", wp(930, 760), wp(990, 770), wp(1050, 790)), A("fr", "move", wp(920, 805), wp(980, 815), wp(1030, 835)),
                A("fr", "move", wp(920, 660), wp(990, 665), wp(1070, 655)), A("fr", "move", wp(910, 700), wp(990, 712), wp(1060, 715)),
                A("fr", "move", wp(880, 560), wp(950, 590), wp(1020, 600)), A("ru", "move", wp(1600, 300), wp(1450, 345), wp(1320, 382)),
                A("ru", "move", wp(1380, 700), wp(1300, 620), wp(1240, 572))],
        events=[(wp(1043, 766), "St Hilaire meets the 4th Column at Pratzen"), (wp(1140, 690), "Vandamme heads for Staré Vinohrady")],
        conf="high",
        debate="Sources place Soult's attack between 08:30 and 09:00; the West Point maps show it under way at 09:00, which is used here.")
B.phase("10:00", "The Pratzeberg", "Fighting for the summit",
        "Kamensky's brigade turns back from Langeron's column and, with Jurczik's Austrians, fights St Hilaire for the Pratzeberg, the highest point of the plateau. Thiébault's brigade, low on ammunition, holds on with artillery support and finally clears the summit with the bayonet. In the north Liechtenstein's cavalry charges Kellermann's light horse near Blasowitz but is stopped by the volleys of Caffarelli's infantry and a counter-charge by Nansouty's cuirassiers. Bagration's attack on the French left breaks against the guns on the Santon.",
        ("Infantry against cavalry", "Formed infantry that kept its nerve could stop a cavalry charge with volleys, and cavalry that broke a charge on it was then open to a counter-charge. Lannes' infantry and Murat's cavalry worked together this way all morning."),
        wp(1100, 680), 8.5,
        arrows=[A("ru", "charge", wp(1010, 930), wp(1040, 905), wp(1062, 892)), A("fr", "charge", wp(1050, 840), wp(1075, 870)),
                A("ru", "charge", wp(1260, 540), wp(1200, 530), wp(1160, 522)), A("fr", "charge", wp(1060, 540), wp(1110, 540), wp(1140, 535)),
                A("ru", "move", wp(1300, 420), wp(1240, 395), wp(1200, 382)), A("fr", "fire", wp(1078, 374), wp(1190, 384))],
        events=[(B.geo["Pratzeberg"], "Thiébault's bayonet charge clears the Pratzeberg"), (wp(1160, 528), "Liechtenstein's charge stopped near Blasowitz"), (B.geo["Santon"], "Santon battery checks Bagration")],
        conf="medium")
B.phase("11:00", "Plateau taken", "The Allied army is cut in two",
        "Vandamme takes Staré Vinohrady from Rottermund's Austrians and the last of Miloradovich's battalions. Kamensky is driven off to the south-east. By 11:00 the French hold the Pratzen plateau from end to end, and the Allied left wing in the Goldbach valley is separated from the rest of the army. Napoleon rides up onto the heights.",
        ("Central position", "Holding the high ground in the middle of the field let Napoleon turn either way. The Allied wings could no longer support each other, and he could deal with them one at a time."),
        wp(1110, 780), 8,
        arrows=[A("fr", "charge", wp(1120, 650), wp(1170, 642)), A("fr", "charge", wp(1110, 690), wp(1160, 680)),
                A("ru", "retreat", wp(1170, 720), wp(1260, 740), wp(1340, 745)), A("au", "retreat", wp(1120, 860), wp(1220, 870), wp(1300, 860)),
                A("ru", "retreat", wp(1080, 930), wp(1130, 975), wp(1160, 995))],
        events=[(wp(1140, 690), "Staré Vinohrady falls"), (wp(1095, 860), "Napoleon on the Pratzen heights")],
        conf="high")
B.phase("13:00", "Guard against Guard", "The Russian Imperial Guard counterattacks",
        "Grand Duke Constantine throws the Russian Imperial Guard at Vandamme near Staré Vinohrady. Guard infantry breaks a battalion of the 4e Ligne, which loses its eagle (the only one the French lost that day), and the Chevalier Guards ride down the 24e Léger. Napoleon sends in Bessières with the cavalry of his own Guard. In a great cavalry melee Rapp's chasseurs and Mamelukes beat the Russian Guard horse, Drouet's division gives the French a line to rally on, and the Russian Guard falls back towards Krzenowitz.",
        ("Committing the reserve", "Both commanders kept their best troops back for the decisive moment. Napoleon committed only his Guard cavalry and kept his Guard infantry fresh."),
        wp(1150, 660), 6,
        arrows=[A("ru", "charge", wp(1240, 610), wp(1210, 640), wp(1185, 660)), A("ru", "charge", wp(1260, 600), wp(1200, 630), wp(1150, 655)),
                A("fr", "charge", wp(1030, 660), wp(1090, 650), wp(1145, 642)), A("fr", "move", wp(1100, 650), wp(1150, 665))],
        events=[(wp(1110, 690), "4e Ligne loses its eagle"), (wp(1150, 645), "Rapp's charge beats the Russian Guard cavalry")],
        conf="medium",
        debate="Accounts put the Guard counterattack anywhere from late morning to about 13:00; the order of events is agreed, the exact time is not.")
B.phase("14:00", "The trap closes", "Soult wheels south",
        "With the centre won, Napoleon turns Soult's corps south off the plateau into the rear of the three Allied columns still fighting along the Goldbach, while Davout and Legrand press from the west. Przhebyshevsky's column is cut off at Sokolnitz. In the north Bagration falls back to the Posoritz post house, and Kolowrat, Liechtenstein and the Russian Guard re-form east of the Littawa near Austerlitz.",
        ("Envelopment", "An enemy attacked from front and rear at once has to fight both ways or run. The Allied columns, already exhausted, were caught between Davout and Soult."),
        wp(920, 1000), 8.5,
        arrows=[A("fr", "move", wp(1040, 860), wp(1020, 930), wp(990, 1030)), A("fr", "move", wp(1080, 800), wp(1090, 900), wp(1110, 995)),
                A("fr", "move", wp(1120, 860), wp(1150, 940), wp(1160, 1010)), A("fr", "move", wp(1000, 870), wp(950, 950), wp(915, 1000)),
                A("ru", "retreat", wp(1300, 395), wp(1360, 365), wp(1395, 350)), A("fr", "move", wp(1110, 600), wp(1200, 640), wp(1270, 680))],
        events=[(wp(820, 990), "Przhebyshevsky's column cut off at Sokolnitz"), (wp(1500, 700), "Allied centre re-forms near Austerlitz")],
        conf="high")
B.phase("15:30", "The ponds", "Retreat around the frozen ponds",
        "Przhebyshevsky surrenders near Sokolnitz. Langeron gets part of his column out through Aujezd. Dokhturov and Kienmayer escape south-east along the narrow causeway between the Satschan and Menitz ponds, under fire from Vandamme's guns on the heights above Aujezd. Some troops try the ice of the Satschan pond and it breaks under the weight and the cannon fire.",
        ("Rearguard and escape route", "Dokhturov kept enough order to fight a rearguard action and get most of his men across the one narrow exit. A beaten army that keeps its formations can still escape."),
        wp(900, 1150), 7,
        arrows=[A("ru", "retreat", wp(840, 1100), wp(860, 1160), wp(900, 1215), wp(990, 1240)), A("ru", "retreat", wp(880, 1080), wp(960, 1110), wp(1020, 1160)),
                A("au", "retreat", wp(830, 1125), wp(880, 1200), wp(1000, 1250)), A("fr", "fire", wp(1130, 1068), wp(960, 1165)),
                A("fr", "fire", wp(1100, 1060), wp(930, 1120)), A("fr", "move", wp(990, 1035), wp(950, 1080))],
        events=[(wp(890, 1165), "Ice breaks at the pond edge"), (wp(830, 960), "Przhebyshevsky surrenders"), (wp(1060, 1080), "Vandamme's guns above Aujezd")],
        conf="medium",
        debate="Marbot's legend of thousands drowning is not supported: when the ponds were drained soon afterwards, the finds were 28-30 guns, about 150 horses and two or three bodies. Modern estimates of the drowned range from a few dozen to about 200.")
B.phase("16:30", "Nightfall", "The battle of the Three Emperors ends",
        "As the sun sets, the last Allied troops leave the field towards Austerlitz and Hungary, and Bagration withdraws towards Raussnitz. The Allies have lost about 27,000 men, around half of them prisoners, and some 180 guns; the French about 9,000. Two days later Emperor Francis asked for an armistice, and the Third Coalition collapsed.",
        ("Decisive battle", "Napoleon aimed not just to win the field but to destroy the enemy army's ability to keep fighting. Austerlitz did that in a single day."),
        wp(1150, 850), 12,
        arrows=[A("ru", "retreat", wp(1450, 720), wp(1560, 700), wp(1640, 700)), A("ru", "retreat", wp(1450, 330), wp(1550, 300), wp(1620, 280)),
                A("ru", "retreat", wp(1000, 1240), wp(1080, 1260), wp(1150, 1280))],
        events=[(wp(1660, 653), "Allied army retreats past Austerlitz"), (wp(1085, 985), "Napoleon at St Anthony's chapel")],
        conf="high")

B.export()
