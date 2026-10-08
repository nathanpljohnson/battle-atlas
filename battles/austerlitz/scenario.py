"""Austerlitz, 2 December 1805 (v2). See brief.md for sources, choices, confidence and review responses.
Positions are mostly read off the georeferenced U.S. Military Academy map series (maps 22-24, 1920 px wide)
with wp(x, y); phases 0-8 are 07:00 ... 16:30. Strengths at phase 0 follow the Wikipedia order of battle
(citing Duffy 1977 and Smith 1998) with Stutterheim (1807) and Mikhailovsky-Danilevsky (1846) for structure;
later strengths are estimates that spread the sourced army losses across units according to the narrative.
"""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "..", "tools"))
os.chdir(HERE)
from battlekit import Battle
from georef import Georef
wp = Georef(HERE)("wp23")

B = Battle("austerlitz", HERE)

# ---------------- sources
B.source("wp22", "U.S. Military Academy, Dept. of History: Austerlitz map 22, situation at 18:00, 1 Dec 1805", "https://commons.wikimedia.org/wiki/File:Battle_of_Austerlitz,_Situation_at_1800,_1_December_1805.png", "Allied columns on the Pratzen the evening before", "staff-map")
B.source("wp23", "U.S. Military Academy: Austerlitz map 23, situation at 09:00, 2 Dec 1805", "https://commons.wikimedia.org/wiki/File:Battle_of_Austerlitz_-_Situation_at_0900,_2_December_1805.png", "georeferenced; most positions read from it (RMSE 245 m)", "staff-map")
B.source("wp24", "U.S. Military Academy: Austerlitz map 24, situation at 14:00, 2 Dec 1805", "https://commons.wikimedia.org/wiki/File:Battle_of_Austerlitz_-_Situation_at_1400,_2_December_1805.png", "the envelopment and the Allied centre re-formed on the Littawa", "staff-map")
B.source("md1844", "A. I. Mikhailovsky-Danilevsky, Description of the First War of Emperor Alexander with Napoleon in 1805 (St Petersburg, 1844), maps 6-8", "https://commons.wikimedia.org/wiki/Category:Maps_of_the_Battle_of_Austerlitz", "Russian official history maps: start and end of the battle; map 7 georeferenced as the historical-map layer", "period-map")
B.source("md1846", "A. I. Mikhailovsky-Danilevsky, Relation de la campagne de 1805: Austerlitz, trans. L. Narischkine (Paris, 1846)", "https://archive.org/details/relationdelacam00dangoog", "Russian official history: the plan, Uvarov's move to Bagration, Kamensky's brigade, the dyke and the ice", "official-history")
B.source("stut", "Karl von Stutterheim, A Detailed Account of the Battle of Austerlitz, by an Austrian Officer, trans. J. Pine-Coffin (London, 1807)", "https://archive.org/details/detailedaccounto00stut", "eyewitness: column composition (battalions and squadrons), routes, the lake", "primary")
B.source("burton", "R. G. Burton, From Boulogne to Austerlitz: Napoleon's Campaign of 1805 (London, 1912)", "https://archive.org/details/fromboulognetoau00burtrich", "staff study: the fog lifting off the heights by 07:00", "scholarly")
B.source("oob", "Wikipedia: Battle of Austerlitz order of battle (citing C. Duffy, Austerlitz 1805, 1977, and D. Smith, The Napoleonic Wars Data Book, 1998)", "https://en.wikipedia.org/wiki/Battle_of_Austerlitz_order_of_battle", "strengths of every column and corps; brigade composition", "reference")
B.source("wiki", "Wikipedia: Battle of Austerlitz", "https://en.wikipedia.org/wiki/Battle_of_Austerlitz", "strength and loss ranges; summary of Chandler, Duffy, Goetz", "reference")
B.source("fn", "Fondation Napoléon: Austerlitz, 2 December 1805, a timeline", "https://www.napoleon.org/en/history-of-the-two-empires/timelines/austerlitz-2-december-1805-a-timeline/", "times of the main events", "reference")
B.source("wh", "Warhistory.org: Battle of Austerlitz, parts I-II", "https://warhistory.org/article/battle-of-austerlitz-2-december-1805-part-i?amp=0", "brigade-level detail on the Pratzen and the retreat", "popular")
B.source("ice", "Den of Geek: The real history of Napoleon's greatest victory", "https://www.denofgeek.com/movies/real-history-napoleon-greatest-victory-didnt-happen", "what was found when the ponds were drained", "popular")
B.source("thi", "The Memoirs of Baron Thiébault, trans. A. J. Butler, vol. 2 (London, 1896)", "https://archive.org/details/memoirsofbaronth02thiuoft", "brigade commander on the Pratzen: Soult's 'twenty minutes at most', the fog, the fight with Kolowrat and Kamensky, Blasowitz", "primary")
B.source("segur", "Philippe-Paul de Ségur, An Aide-de-Camp of Napoleon: Memoirs 1800-1812 (New York, 1895)", "https://archive.org/details/aidedecampnapole00segu", "present at headquarters: 08:00 and Soult's 'ten minutes'", "primary")
B.source("marbot", "The Memoirs of Baron de Marbot, trans. A. J. Butler, vol. 1 (London, 1892)", "https://archive.org/details/memoirsofbaronde01marbuoft", "the Guard artillery fired on the ice by Napoleon's order; source of the exaggerated 'thousands drowned'", "primary")
B.source("fraser", "Edward Fraser, The War Drama of the Eagles (London, 1912)", "https://archive.org/details/wardramaeaglesn00frasgoog", "the eagles of the 4e Ligne and 24e Léger (use with care)", "popular")
B.source("lgh", "Wikipedia: Life Guard Horse Regiment", "https://en.wikipedia.org/wiki/Life_Guard_Horse_Regiment", "the privates who took the eagle of the 4e Ligne", "reference")
B.source("millar04", "Stephen Millar, 'Russian-Austrian Order-of-Battle at Austerlitz', The Napoleon Series (2004)", "https://www.napoleon-series.org/military/battles/1805/Austerlitz/AusterlitzOOB/c_austerlitzoob.html", "Allied strength range 73,200-85,400; 131 guns lost (Kutuzov's report)", "scholarly")
B.source("fnplaces", "Fondation Napoléon: Austerlitz, places of the battle", "https://www.napoleon.org/en/magazine/places/austerlitz-2/", "Napoleon at the Zuran, Staré Vinohrady and St Anthony's chapel", "reference")
B.source("data", "AWS Terrain Tiles (elevation); OpenStreetMap Nominatim, Wikidata and Wikipedia (place identification)", "https://registry.opendata.aws/terrain-tiles/", "terrain and village locations", "data")

# ---------------- meta
B.meta = {
    "title": "Austerlitz", "year": "1805", "era": "napoleonic", "war": "War of the Third Coalition",
    "eyebrow": "2 December 1805 · Moravia · War of the Third Coalition",
    "subtitle": "Napoleon lets the Russians and Austrians attack his weak right, then breaks their centre on the Pratzen heights.",
    "sides": {
        "fr": {"name": "French", "top": "#2c4a8c", "side": "#1d3363", "mark": "#f3efe4", "arrow": "#3f73dd", "flag": "#2c4a8c"},
        "ru": {"name": "Russian", "top": "#2f5b3a", "side": "#1f3e27", "mark": "#f1ead8", "arrow": "#d24a35", "flag": "#2f5b3a"},
        "au": {"name": "Austrian", "top": "#efebe1", "side": "#b7b1a2", "mark": "#3a2a18", "arrow": "#e8735a", "flag": "#efebe1", "chart": "#8a7f6c"},
    },
    "belligerents": [
        {"name": "Grande Armée", "short": "French", "commander": "Napoleon I", "sides": ["fr"], "code": "letters"},
        {"name": "Russo-Austrian army", "short": "Allies", "commander": "Kutuzov, with Alexander I and Francis II", "sides": ["ru", "au"], "code": "numbers"},
    ],
    "forces": {
        "start": [{"label": "French", "n": 73000, "segs": [["fr", 1]]}, {"label": "Allies", "n": 85400, "segs": [["ru", 0.82], ["au", 0.18]]}],
        "end": [{"label": "French", "n": 9000, "segs": [["fr", 1]]}, {"label": "Allies", "n": 27000, "segs": [["ru", 0.78], ["au", 0.22]]}],
    },
    "sun": {"lat": 49.14, "decl": -21.9, "note": "Sunrise about 07:50, sunset about 16:10."},
    "wind": 300, "view": {"az": -0.42, "el": 0.7}, "unitScale": 2.1, "unitLabelDist": 13,
    "ground": {"season": "winter", "relief": 130},
    "strengthNote": "Starting strengths from Duffy (1977) and Smith (1998) via the Wikipedia order of battle; losses through the day are estimates that spread the sourced totals (≈9,000 French, ≈27,000 Allied) across units following the narrative. Artillery is not counted.",
    "method": "Unit positions were read off the U.S. Military Academy situation maps for 18:00 on 1 December and 09:00 and 14:00 on 2 December after georeferencing them against fourteen village locations (RMSE 245 m), and checked against the maps of the 1844 Russian official history. Strengths and unit composition come from the order of battle compiled by Duffy and Smith, Stutterheim's 1807 eyewitness account and the Russian official history; times between the maps come from those and four other accounts. Every unit and moment is cited and carries a confidence level; disagreements are noted where they matter.",
    "notes": "Not shown as separate units: Margaron's and Trelliard's light cavalry, Walther's and Beaumont's dragoons and Milhaud's brigade (about 5,000 sabres), and both armies' artillery reserves. The Satschan, Menitz and Kobelnitz ponds were drained in the 19th century and are drawn from the West Point maps. Heights are exaggerated about three times; roads and woods are illustrative; the wind direction for drifting smoke is assumed.",
}

# ---------------- places, terrain features
for n in ["Telnitz", "Sokolnitz", "Kobelnitz", "Puntowitz", "Schlappanitz", "Girzikowitz", "Pratzen", "Blasowitz", "Holubitz",
          "Bosenitz", "Welatitz", "Kowalowitz", "Krzenowitz", "Hostieradek", "Aujezd", "Satschan", "Menitz", "Zbysov", "Bellowitz"]:
    B.place(n)
B.place("Austerlitz", size=1.8)
B.place("Posoritz post house", B.geo["Posoritz post"], size=0.4)
B.place("Sokolnitz castle", B.geo["Sokolnitz castle"], size=0.35)
B.hill("Santon", B.geo["Santon"]); B.hill("Zuran", B.geo["Zuran"])
B.hill("Pratzen heights", B.geo["Pratzeberg"]); B.hill("Staré Vinohrady", wp(1140, 690))
B.roads = [
    [wp(560, 395), wp(800, 400), "Bosenitz", wp(1250, 390), "Posoritz post house", wp(1600, 300)],
    ["Posoritz post house", wp(1500, 500), "Austerlitz"], ["Schlappanitz", "Girzikowitz", "Blasowitz", "Holubitz"],
    ["Puntowitz", "Pratzen", "Krzenowitz", "Austerlitz"], ["Kobelnitz", "Pratzen"], ["Sokolnitz", "Telnitz", "Menitz"],
    ["Telnitz", "Aujezd", "Hostieradek", "Krzenowitz"], ["Sokolnitz", "Kobelnitz", "Puntowitz", "Schlappanitz", "Bellowitz"],
    ["Aujezd", "Satschan"], ["Pratzen", "Zbysov"], ["Blasowitz", "Pratzen"], ["Girzikowitz", "Welatitz"],
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
    {"p": P([(1130, 800), (1043, 770), (965, 742), (898, 725)]), "w": 2, "ford": True},
    {"p": P([(1190, 545), (1120, 548), (1040, 545), (985, 530), (905, 540)]), "w": 2, "ford": True},
]
B.water["labels"] = {"Satschan pond": wp(880, 1165), "Menitz pond": wp(715, 1350), "Goldbach": wp(835, 905), "Littawa": wp(1300, 905)}
# Goldbach crossings at the villages (bridges, mill dams); Littawa crossings; the dyke between the ponds [stut] [md1846]
for name, xy in [("Telnitz bridge", (752, 1098)), ("Sokolnitz bridge", (790, 1035)), ("Sokolnitz castle", (805, 975)), ("Kobelnitz dam", (870, 800)),
                 ("Puntowitz bridge", (893, 672)), ("Girzikowitz", (905, 560)), ("Schlappanitz", (880, 520)), ("Goldbach ford above Kobelnitz", (884, 760)),
                 ("Goldbach ford below Kobelnitz", (850, 905)), ("Krzenowitz bridge", (1420, 830)), ("Austerlitz bridge", (1600, 712)),
                 ("Dyke between the ponds", (790, 1228)), ("Littawa crossing at Satschan", (990, 1175)), ("Littawa bridge on the Aujezd-Satschan road", (1010, 1135))]:
    B.crossing(name, wp(*xy))
B.crossing("Hostieradek bridge", "Hostieradek")
B.crossing("Aujezd", "Aujezd")
B.overlay("ru7", "Russian official history, 1844: the battle at its start", "overlay_ru7.webp", "period", 0.9,
          "Mikhailovsky-Danilevsky's map 7, warped onto the terrain using 15 villages (2nd-order fit, RMSE 207 m).")
B.overlay("wp23", "West Point atlas: situation at 09:00", "overlay_wp23.webp", "staff-map", 0.85,
          "U.S. Military Academy map 23, the main source for positions, warped onto the terrain (RMSE 245 m).")

# ---------------- units
def U(uid, side, typ, name, strength, frontage, keys, note, conf, men, cite, via=None, **kw):
    u = B.unit(uid, side, typ, name, strength, frontage, note=note, conf=conf, cite=cite, men=men, **kw)
    for ph, (x, y, f, form) in keys.items():
        u.at(ph, wp(x, y), f, form, via=[wp(*p) for p in (via or {}).get(ph, [])] or None)

POS = ["wp23", "wp22", "wp24"]
# French: right wing (Legrand, Davout)
U("leg1", "fr", "inf", "3e Ligne & Tirailleurs du Po", "Legrand's division · 3 bns", 700,
  {0: (748, 1095, 110, "F"), 1: (705, 1105, 90, "L"), 2: (720, 1100, 90, "L"), 6: (735, 1100, 95, "F"), 7: (760, 1100, 110, "F"), 8: (770, 1105, 110, "L")},
  "Held Telnitz against Kienmayer from 07:00 until Dokhturov's column arrived [fn].", "high", {0: 1800, 1: 1500, 7: 1300, 8: 1200}, POS + ["oob", "fn"])
U("leg2", "fr", "inf", "26e Léger & Tirailleurs corses", "Legrand's division · 4 bns", 700,
  {0: (782, 1032, 100, "F"), 1: (765, 1035, 100, "F"), 2: (742, 1030, 90, "L"), 3: (758, 1030, 90, "F"), 4: (750, 1020, 90, "L"), 7: (785, 1035, 95, "F"), 8: (795, 1040, 100, "L")},
  "Defended Sokolnitz village, which changed hands several times [wiki] [thi].", "medium", {0: 2200, 2: 1900, 4: 1700, 8: 1600}, POS + ["oob", "wiki", "thi"])
U("leg3", "fr", "inf", "Levasseur's brigade (18e, 75e Ligne)", "Legrand's division · 4 bns", 650,
  {0: (800, 850, 120, "L"), 1: (790, 930, 160, "C"), 2: (782, 962, 100, "F"), 6: (800, 985, 100, "F"), 7: (820, 995, 90, "F"), 8: (825, 1000, 90, "L")},
  "Legrand's reserve, fed into the fight for Sokolnitz castle.", "medium", {0: 2500, 3: 2300, 8: 2100}, ["wp23", "oob", "wh"])
U("fri1", "fr", "inf", "Heudelet's brigade (108e Ligne, voltigeurs of the 15e Léger)", "Friant's division, III Corps · 4 bns", 600,
  {0: (585, 1140, 50, "C"), 1: (708, 1108, 80, "F"), 2: (728, 1098, 90, "L"), 3: (722, 1085, 90, "L"), 7: (758, 1092, 110, "F"), 8: (775, 1100, 110, "L")},
  "Davout's advance guard. After marching about 110 km in two days it retook Telnitz around 08:00, then was thrown out again by Austrian hussars [wiki].", "high",
  {0: 1400, 1: 1150, 2: 1000, 8: 800}, POS + ["oob", "wiki"], via={1: [(650, 1125)]})
U("fri2", "fr", "inf", "Friant's division (Kister, Lochet)", "III Corps · 6 bns", 900,
  {0: (560, 1175, 45, "C"), 1: (630, 1105, 55, "C"), 2: (700, 1050, 75, "L"), 3: (742, 1015, 85, "F"), 7: (788, 1028, 95, "F"), 8: (800, 1040, 100, "L")},
  "Retook Sokolnitz and held the Goldbach line all day against twice its numbers [wiki] [wh].", "high", {0: 2000, 3: 1600, 6: 1400, 8: 1200}, POS + ["oob", "wiki", "wh"])
U("bou", "fr", "cav", "Bourcier's dragoons", "Attached to III Corps · ≈830 sabres", 600,
  {0: (540, 1110, 50, "C"), 1: (690, 1088, 80, "L"), 8: (690, 1085, 80, "L")},
  "Covered Davout's arrival on the right.", "medium", {0: 830, 8: 730}, ["wp23", "oob"])

# French: centre (Soult's IV Corps)
U("sh1", "fr", "inf", "Morand's brigade (10e Léger)", "St Hilaire's division · 2 bns", 450,
  {0: (930, 760, 90, "C"), 2: (1030, 775, 100, "C"), 3: (1085, 838, 140, "F"), 5: (1082, 848, 140, "L"), 6: (1020, 930, 200, "C"), 7: (990, 1035, 190, "F"), 8: (1000, 1058, 180, "L")},
  "Advance guard: sent to take the plateau commanding the southern part of the heights [thi]; with Thiébault it drove Kamensky back and took two batteries [thi].", "medium", {0: 1500, 3: 1250, 4: 1150, 8: 1100}, POS + ["oob", "thi"],
  via={2: [(975, 770)], 6: [(1050, 900)]})
U("sh2", "fr", "inf", "Thiébault's brigade (14e, 36e Ligne)", "St Hilaire's division · 4 bns", 650,
  {0: (925, 790, 90, "C"), 2: (1015, 800, 110, "C"), 3: (1060, 860, 150, "F"), 5: (1060, 870, 150, "L"), 6: (968, 950, 210, "C"), 7: (930, 1000, 220, "F"), 8: (905, 1010, 220, "L")},
  "Took Pratzen village [thi]; then, with nine guns loaded with round and grape, broke Kolowrat's advancing regiments at 30-40 yards and helped Morand drive Kamensky back [thi].", "medium", {0: 2700, 3: 2200, 4: 2000, 8: 1900}, POS + ["oob", "thi"],
  via={2: [(965, 800)], 6: [(1020, 920)]})
U("sh3", "fr", "inf", "Varé's brigade (43e, 55e Ligne)", "St Hilaire's division · 4 bns", 650,
  {0: (915, 820, 90, "C"), 2: (1000, 822, 110, "C"), 3: (1040, 880, 160, "L"), 4: (1045, 885, 160, "F"), 6: (1060, 960, 190, "C"), 7: (1050, 1048, 190, "F"), 8: (1050, 1068, 180, "L")},
  "St Hilaire's third brigade; with Vandamme it attacked the eastern part of the heights [thi].", "medium", {0: 2600, 4: 2300, 8: 2100}, POS + ["oob", "thi"], via={2: [(955, 825)]})
U("va1", "fr", "lt", "Schiner's brigade (24e Léger)", "Vandamme's division · 2 bns", 450,
  {0: (920, 650, 90, "C"), 2: (1050, 660, 60, "C"), 3: (1130, 642, 60, "F"), 4: (1168, 642, 60, "F"), 5: (1118, 662, 240, "R"), 6: (1062, 760, 180, "C"), 7: (1082, 960, 180, "C"), 8: (1100, 1060, 180, "F")},
  "Broken by the Russian Guard cavalry around 13:00, then re-formed for the afternoon sweep south [wh].", "medium", {0: 1600, 4: 1450, 5: 1250, 8: 1200}, POS + ["oob", "wh"],
  via={2: [(985, 655)], 7: [(1070, 860)]})
U("va2", "fr", "inf", "Ferey's brigade (4e, 28e Ligne)", "Vandamme's division · 4 bns", 650,
  {0: (915, 680, 90, "C"), 2: (1040, 690, 70, "C"), 3: (1115, 680, 70, "F"), 4: (1160, 680, 70, "F"), 5: (1108, 692, 240, "R"), 6: (1070, 800, 180, "C"), 7: (1120, 1000, 190, "C"), 8: (1118, 1035, 190, "F")},
  "Driven back by the Russian Guard infantry; the Life Guard Horse then rode down a battalion of the 4e Ligne and took its eagle [lgh] [fraser].", "medium", {0: 2800, 4: 2500, 5: 2150, 8: 2100}, POS + ["oob", "lgh", "fraser", "wh"],
  via={2: [(980, 685)], 7: [(1095, 900)]})
U("va3", "fr", "inf", "Candras's brigade (46e, 57e Ligne)", "Vandamme's division · 4 bns", 650,
  {0: (905, 705, 90, "C"), 2: (1030, 720, 80, "C"), 3: (1100, 720, 80, "L"), 4: (1140, 720, 80, "F"), 5: (1140, 720, 60, "F"), 6: (1110, 850, 170, "C"), 7: (1150, 1010, 180, "C"), 8: (1150, 1025, 200, "F")},
  "In the afternoon Vandamme's men took Aujezd and the heights above the ponds [stut].", "medium", {0: 2600, 4: 2450, 8: 2300}, POS + ["oob", "stut"],
  via={2: [(970, 712)], 7: [(1135, 930)]})

# French: north and reserves
U("ber1", "fr", "inf", "Rivaud's division", "Bernadotte's I Corps · 6 bns", 800,
  {0: (830, 470, 90, "C"), 1: (880, 560, 120, "C"), 2: (985, 600, 100, "C"), 3: (1060, 600, 100, "L"), 4: (1110, 600, 100, "L"), 5: (1130, 610, 100, "L"), 6: (1200, 640, 110, "L"), 7: (1280, 680, 110, "L"), 8: (1300, 690, 110, "L")},
  "Bernadotte's advance was slow; many historians criticise his passivity [wiki].", "medium", {0: 5700, 8: 5600}, POS + ["oob", "wiki"], via={2: [(905, 560)]})
U("ber2", "fr", "inf", "Drouet's division", "Bernadotte's I Corps · 6 bns", 800,
  {0: (840, 500, 90, "C"), 1: (890, 590, 120, "C"), 2: (990, 630, 110, "C"), 3: (1060, 640, 110, "L"), 4: (1100, 650, 100, "L"), 5: (1150, 665, 70, "F"), 6: (1210, 700, 110, "L"), 7: (1300, 730, 110, "L"), 8: (1320, 745, 110, "L")},
  "Gave the French cavalry a line to rally behind during the Guard battle [wiki].", "medium", {0: 5800, 5: 5650, 8: 5600}, POS + ["oob", "wiki"], via={2: [(905, 565)]})
U("gdi", "fr", "gd", "Imperial Guard infantry", "Foot Grenadiers & Chasseurs · 8 bns", 700,
  {0: (760, 470, 120, "L"), 2: (850, 520, 110, "C"), 3: (950, 640, 120, "C"), 4: (990, 700, 110, "L"), 5: (1050, 700, 90, "L"), 6: (990, 705, 90, "L"), 7: (1020, 760, 150, "L")},
  "Napoleon's last reserve. Barely engaged [wiki].", "medium", {0: 4100}, POS + ["oob", "wiki"], via={3: [(893, 672)]})
U("gdc", "fr", "cav", "Imperial Guard cavalry (Bessières, Rapp)", "Chasseurs, Horse Grenadiers, Mamelukes", 600,
  {0: (780, 450, 120, "L"), 2: (860, 500, 110, "C"), 3: (960, 620, 110, "C"), 4: (1020, 660, 90, "L"), 5: (1150, 642, 60, "L"), 6: (1080, 680, 90, "L"), 7: (1100, 700, 120, "L")},
  "Rapp's charge against the Russian Guard cavalry around 13:00 decided the fight for Staré Vinohrady [wiki].", "medium", {0: 1100, 5: 900}, POS + ["oob", "wiki"], via={3: [(905, 560)]})
U("gren", "fr", "gd", "Grenadier division (Oudinot's grenadiers, under Duroc)", "Combined grenadiers · 10 bns", 800,
  {0: (800, 520, 110, "L"), 2: (880, 600, 120, "C"), 3: (950, 700, 130, "C"), 4: (995, 780, 130, "L"), 5: (995, 810, 130, "L")},
  "In reserve behind the Pratzen attack; Oudinot was convalescent, so Duroc commanded [oob].", "medium", {0: 5700, 8: 5650}, POS + ["oob"], via={3: [(893, 672)]})
U("kel", "fr", "lc", "Kellermann's light cavalry", "I Corps light cavalry, with Murat", 600,
  {0: (980, 470, 90, "L"), 2: (1080, 500, 80, "L"), 3: (1150, 520, 80, "L"), 4: (1080, 510, 90, "L"), 5: (1150, 490, 80, "L"), 6: (1230, 480, 80, "L"), 7: (1300, 470, 70, "L"), 8: (1320, 460, 70, "L")},
  "Took the first shock of the Uhlans' charge and fell back through Caffarelli's infantry [wh].", "medium", {0: 1300, 3: 1050, 8: 1000}, POS + ["oob", "wh"])
U("nan", "fr", "cav", "Nansouty's heavy cavalry", "Carabiniers & cuirassiers · Murat's reserve", 600,
  {0: (960, 500, 90, "C"), 2: (1050, 520, 90, "L"), 3: (1120, 540, 90, "L"), 4: (1180, 540, 90, "L"), 5: (1220, 520, 70, "L"), 6: (1260, 500, 70, "L"), 7: (1330, 470, 60, "L")},
  "Counter-charged the Allied cavalry near Blasowitz.", "medium", {0: 1600, 4: 1450, 8: 1400}, POS + ["oob"])
U("hau", "fr", "cav", "d'Hautpoul's cuirassiers", "Murat's reserve", 600,
  {0: (950, 450, 90, "C"), 2: (1040, 470, 80, "C"), 3: (1100, 480, 80, "L"), 4: (1160, 490, 70, "L"), 5: (1220, 470, 60, "L"), 6: (1250, 450, 60, "L"), 7: (1300, 430, 60, "L")},
  "Heavy cavalry that charged Bagration's line in the afternoon.", "low", {0: 1200, 6: 1100, 8: 1050}, ["wp23", "oob"])
U("suc", "fr", "inf", "Suchet's division", "Lannes' V Corps · 10 bns", 900,
  {0: (1060, 430, 90, "L"), 2: (1110, 415, 90, "L"), 3: (1150, 415, 80, "F"), 4: (1180, 410, 80, "F"), 5: (1200, 410, 70, "F"), 6: (1195, 402, 70, "F"), 7: (1260, 390, 60, "L"), 8: (1300, 380, 60, "L")},
  "Pushed Bagration slowly back along the Olmütz road [wh].", "medium", {0: 5000, 4: 4600, 6: 4300, 8: 4200}, POS + ["oob", "wh"])
U("caf", "fr", "inf", "Caffarelli's division", "Lannes' V Corps · 9 bns", 900,
  {0: (940, 450, 120, "C"), 1: (1000, 500, 110, "C"), 2: (1080, 545, 90, "L"), 3: (1110, 555, 90, "F"), 4: (1150, 540, 80, "F"), 5: (1190, 470, 70, "F"), 6: (1205, 440, 70, "F"), 7: (1260, 440, 60, "L"), 8: (1300, 440, 60, "L")},
  "Its squares and volleys stopped the Allied cavalry near Blasowitz [wh].", "medium", {0: 5600, 3: 5300, 6: 5000, 8: 4900}, POS + ["oob", "wh"])
U("san", "fr", "lt", "Claparède's brigade (17e Léger) on the Santon", "Suchet's division · 3 bns", 280,
  {0: (1062, 382, 60, "L"), 3: (1062, 382, 60, "F"), 6: (1062, 382, 60, "L")},
  "Ordered to hold the fortified Santon hill to the last man; with it stood 18 guns [wiki].", "high", {0: 1500, 8: 1400}, POS + ["wiki"])
U("sanb", "fr", "art", "Santon battery", "18 guns", 220,
  {0: (1078, 374, 60, "L"), 3: (1078, 374, 60, "F"), 6: (1078, 374, 60, "L")},
  "Anchored the French left on the Olmütz road [wiki].", "high", {0: 18}, ["wp23", "wiki"])

# Allies: left wing (Buxhöwden)
U("kie1", "au", "lt", "Kienmayer's infantry (Brod & Szekler Grenzer)", "Austrian advance guard · 5 bns [oob]", 500,
  {0: (802, 1095, 270, "F"), 1: (790, 1100, 270, "F"), 3: (820, 1110, 260, "L"), 6: (850, 1130, 250, "L"), 7: (880, 1190, 200, "R"), 8: (985, 1240, 120, "R")},
  "Opened the battle with attacks on Telnitz [fn] [stut].", "high", {0: 3440, 1: 3100, 3: 2900, 7: 2700, 8: 2540}, POS + ["oob", "stut", "fn"],
  via={7: [(810, 1200)], 8: [(790, 1228), (880, 1240)]})
U("kie2", "au", "lc", "Kienmayer's hussars, chevaulegers & Cossacks", "Austrian advance guard · 22 Austrian and 10 Cossack sqns [stut]", 550,
  {0: (852, 1122, 270, "L"), 1: (800, 1125, 280, "L"), 2: (772, 1120, 280, "L"), 3: (845, 1118, 270, "L"), 7: (745, 1172, 45, "L"), 8: (738, 1188, 45, "L")},
  "The Hessen-Homburg hussars drove Davout's first troops back out of Telnitz [wiki]. In the afternoon they went ahead round the lake, while the O'Reilly chevaulegers and Szekler hussars covered Dokhturov's retreat from the hill between Telnitz and Menitz under the fire of the French Guard guns [stut] [md1846].", "medium", {0: 3440, 2: 3200, 7: 2800, 8: 2500}, POS + ["oob", "stut", "wiki", "md1846"])
U("col1", "ru", "inf", "1st Column (Dokhturov)", "Russian · 24 bns, ≈13,240 [oob] [stut]", 1200,
  {0: (930, 1050, 240, "C"), 1: (812, 1085, 260, "F"), 2: (792, 1095, 270, "F"), 3: (780, 1095, 270, "F"), 4: (790, 1090, 270, "L"), 6: (840, 1100, 90, "L"), 7: (800, 1125, 160, "R"), 8: (900, 1245, 110, "R")},
  "Took Telnitz but was held at the Goldbach for most of the day [wh]; Dokhturov gathered it on the plain between Telnitz and the lake [stut] and re-formed it beyond the dyke between the ponds [md1846].", "medium",
  {0: 13240, 1: 12700, 3: 12200, 6: 11700, 7: 10700, 8: 9740}, POS + ["oob", "stut", "md1846"],
  via={0: [(990, 1040)], 8: [(790, 1228)]})
U("col2", "ru", "inf", "2nd Column (Langeron)", "Russian · Olsufiev's brigade, 9 bns", 1000,
  {0: (980, 1000, 240, "C"), 1: (840, 1040, 250, "C"), 2: (812, 1035, 260, "F"), 3: (792, 1035, 270, "F"), 4: (786, 1030, 270, "F"), 6: (830, 1040, 90, "L"), 7: (902, 1110, 150, "R"), 8: (1000, 1200, 130, "R")},
  "Delayed at dawn when Liechtenstein's cavalry crossed its line of march [wiki]. Only part of it escaped: Buxhöwden got through Aujezd with a few battalions, and about 4,000 men were taken prisoner in and around the village [stut].", "medium",
  {0: 7250, 2: 6800, 4: 6300, 6: 5800, 7: 4300, 8: 3250}, POS + ["oob", "stut"], via={7: [(870, 1075)], 8: [(988, 1074), (1010, 1135)]})
U("kam", "ru", "inf", "Kamensky's brigade (Fanagoria Grenadiers, Ryazhsk)", "2nd Column · 2 regiments [md1846]", 500,
  {0: (1010, 950, 230, "C"), 1: (1000, 930, 230, "C"), 2: (1030, 880, 30, "C"), 3: (1062, 890, 330, "F"), 4: (1080, 930, 340, "F"), 5: (1120, 950, 150, "R"), 6: (1145, 972, 130, "R"), 7: (1150, 975, 300, "L")},
  "Turned back to fight for the southern Pratzen heights, where Thiébault and Morand drove it off [thi] [md1846]; it ended the day near Hostieradek [md1844].", "medium",
  {0: 4000, 3: 3400, 4: 2600, 5: 2200, 8: 2000}, ["wp23", "wp24", "oob", "md1846", "md1844", "thi"])
U("col3", "ru", "inf", "3rd Column (Przhebyshevsky)", "Russian · 18 bns [stut], ≈7,700 [oob]", 800,
  {0: (1020, 920, 240, "C"), 1: (870, 980, 250, "C"), 2: (822, 975, 260, "F"), 3: (806, 975, 270, "F"), 6: (820, 990, 0, "F"), 7: (830, 960, 20, "R")},
  "Cut off at Sokolnitz when Soult swung south; most of it was captured near Kobelnitz [wh].", "medium",
  {0: 7700, 2: 7300, 3: 6900, 6: 5900, 7: 1200}, POS + ["oob", "stut", "wh"])
# Allies: centre (4th Column)
U("milo", "ru", "inf", "4th Column, Russian (Miloradovich)", "Russian · 12 bns [stut]", 800,
  {0: (1230, 760, 270, "C"), 1: (1150, 760, 270, "C"), 2: (1082, 760, 260, "F"), 3: (1120, 730, 250, "F"), 4: (1170, 720, 250, "R"), 5: (1280, 740, 100, "R"), 6: (1400, 740, 90, "R"), 7: (1440, 700, 90, "L"), 8: (1580, 700, 90, "L")},
  "Marched into St Hilaire's division at Pratzen village around 09:00 and was routed by 11:00 [thi] [wh].", "medium",
  {0: 4600, 2: 4100, 3: 3600, 4: 3000, 8: 2600}, POS + ["oob", "stut", "thi", "wh"])
U("jur", "au", "inf", "Jurczik's brigade", "Kolowrat's Austrians · 7 bns and Jäger [oob]", 700,
  {0: (1260, 800, 270, "C"), 1: (1180, 820, 260, "C"), 2: (1120, 830, 240, "L"), 3: (1100, 860, 240, "F"), 4: (1150, 880, 220, "R"), 5: (1300, 860, 100, "R"), 6: (1440, 700, 90, "L"), 8: (1600, 680, 90, "L")},
  "Many young recruits [stut]. Kolowrat led its regiments against Thiébault's line, which broke them with canister at 30-40 yards [thi].", "medium",
  {0: 4400, 3: 3800, 4: 3200, 8: 2600}, POS + ["oob", "stut", "thi"], via={6: [(1380, 820), (1420, 830)]})
U("rot", "au", "inf", "Rottermund's brigade", "Kolowrat's Austrians · 8 bns [oob]", 700,
  {0: (1280, 740, 270, "C"), 1: (1220, 720, 260, "C"), 2: (1172, 690, 250, "L"), 3: (1160, 682, 250, "F"), 4: (1180, 690, 240, "F"), 5: (1290, 700, 90, "R"), 6: (1480, 650, 90, "L"), 8: (1600, 620, 90, "L")},
  "Held Staré Vinohrady against Vandamme before giving way [wh].", "low",
  {0: 4500, 3: 4100, 4: 3500, 5: 3100, 8: 3000}, POS + ["oob", "wh"])
# Allies: right (Liechtenstein, Guard, Bagration)
U("uhl", "ru", "lc", "Grand Duke Constantine's Uhlans & Cossacks (Essen II, Meller-Zakomelsky)", "5th Column · Russian [oob] [md1846]", 700,
  {0: (1150, 800, 270, "C"), 1: (1180, 640, 0, "C"), 2: (1232, 560, 290, "L"), 3: (1170, 530, 280, "L"), 4: (1230, 520, 270, "R"), 5: (1350, 560, 90, "R"), 6: (1490, 640, 90, "L"), 7: (1520, 640, 90, "L")},
  "The Uhlans charged Kellermann near Blasowitz, rode on into Caffarelli's infantry and were shattered [wh].", "medium",
  {0: 2300, 3: 1900, 4: 1500, 8: 1400}, POS + ["oob", "md1846", "wh"])
U("lau", "au", "cav", "Austrian cuirassiers (Caramelli, Weber)", "5th Column · Nassau, Lorraine, Kaiser · 20 sqns [oob]", 700,
  {0: (1180, 780, 270, "C"), 1: (1220, 650, 0, "C"), 2: (1292, 540, 290, "L"), 3: (1220, 520, 270, "L"), 4: (1250, 500, 270, "L"), 5: (1380, 520, 100, "R"), 6: (1500, 600, 90, "L"), 7: (1530, 600, 90, "L")},
  "Liechtenstein's Austrian heavy horse, under Prince Hohenlohe. Sources give the Austrian squadrons of the 5th Column as 20 [oob], 32 [md1846] or 40 very weak ones [stut]; the order-of-battle figure is used.", "low", {0: 1100, 5: 900, 8: 800}, ["wp23", "oob", "md1846", "stut"])
U("uva", "ru", "cav", "Uvarov's dragoons & hussars", "Chernigov and Kharkov Dragoons, Elisabethgrad Hussars [oob]", 700,
  {0: (1330, 500, 270, "L"), 2: (1290, 480, 270, "L"), 3: (1240, 470, 270, "L"), 4: (1270, 470, 90, "R"), 5: (1330, 470, 90, "L"), 6: (1400, 420, 60, "L"), 8: (1520, 380, 60, "L")},
  "Moved from Liechtenstein's column to Bagration's left the evening before the battle [md1846].", "low", {0: 2000, 4: 1750, 8: 1700}, ["oob", "md1846"])
U("rgi", "ru", "gd", "Russian Imperial Guard infantry", "Grand Duke Constantine · 10 bns [stut]", 800,
  {0: (1430, 770, 290, "C"), 1: (1330, 650, 300, "C"), 2: (1232, 572, 300, "L"), 3: (1220, 580, 270, "L"), 4: (1210, 620, 240, "L"), 5: (1182, 660, 250, "F"), 6: (1350, 720, 100, "R"), 7: (1480, 650, 90, "L"), 8: (1560, 640, 90, "L")},
  "Its bayonet charge at Staré Vinohrady drove back the 4e Ligne and 24e Léger [wh] [fraser]. Its Jäger had held Blasowitz against Lannes's first division in the late morning [thi].", "medium",
  {0: 6730, 4: 6450, 5: 6000, 6: 5730}, POS + ["oob", "stut", "wh", "fraser", "thi"])
U("rgc", "ru", "cav", "Russian Imperial Guard cavalry", "Chevalier Guards, Horse Guards, Guard Hussars & Cossacks · 18 sqns [stut]", 700,
  {0: (1450, 740, 290, "C"), 1: (1350, 640, 300, "C"), 2: (1252, 582, 300, "L"), 3: (1250, 600, 270, "L"), 4: (1230, 640, 260, "L"), 5: (1172, 650, 250, "L"), 6: (1330, 700, 100, "R"), 7: (1440, 620, 90, "L"), 8: (1550, 600, 90, "L")},
  "The Life Guard Horse rode down a battalion of the 4e Ligne and took its eagle [lgh] before the Guard cavalry was beaten by Rapp's [wh].", "medium",
  {0: 3700, 5: 3300, 6: 3100}, POS + ["oob", "stut", "wh", "lgh"])
U("bagi", "ru", "inf", "Bagration's advance guard infantry", "Russian · 12 bns [stut]", 1000,
  {0: (1500, 330, 240, "C"), 1: (1400, 360, 250, "C"), 2: (1300, 385, 260, "L"), 3: (1262, 395, 260, "F"), 4: (1250, 400, 260, "F"), 5: (1290, 390, 260, "F"), 6: (1390, 350, 250, "L"), 7: (1450, 330, 240, "L"), 8: (1550, 300, 240, "L")},
  "Fought Lannes to a standstill for much of the day, then withdrew in good order towards Raussnitz [wh].", "medium",
  {0: 9200, 4: 8800, 6: 8500, 8: 8400}, POS + ["oob", "stut", "wh"])
U("bagc", "ru", "lc", "Bagration's cavalry (Wittgenstein, Voropaitzky, Chaplits)", "Hussars, cuirassiers, dragoons & Cossacks · 40 sqns [stut]", 800,
  {0: (1520, 350, 240, "C"), 1: (1420, 400, 250, "L"), 2: (1322, 430, 260, "L"), 3: (1200, 380, 280, "L"), 4: (1300, 430, 260, "R"), 5: (1380, 400, 250, "L"), 6: (1420, 380, 250, "L"), 8: (1550, 330, 240, "L")},
  "Tried to get round the Santon and was stopped by its guns [wh].", "low", {0: 4500, 4: 4200, 8: 4100}, ["wp23", "oob", "stut", "wh"])

# ---------------- commanders
B.commander("nap", "fr", "Napoleon", {0: B.geo["Zuran"], 4: wp(1095, 860), 5: wp(1140, 700), 7: wp(1085, 985)},
            "Watched from the Zuran at dawn, moved onto the Pratzen heights, received the captured colours from Rapp at Staré Vinohrady, and watched the retreat over the ponds from St Anthony's chapel above Aujezd [fnplaces].")
B.commander("kut", "ru", "Kutuzov & the emperors", {0: wp(1300, 770), 2: wp(1180, 780), 4: wp(1330, 760), 6: wp(1520, 690), 8: wp(1640, 690)},
            "Kutuzov rode with the 4th Column and was wounded on the Pratzen; Alexander and Francis joined him about 09:00.")

# ---------------- phases
A = B.arrow
B.phase("07:00", "Dawn & fog", "The Allies march into the trap",
        "Before sunrise, in thick fog, the Allied left (about 40,000 men: three columns of about 32,000 and Kienmayer's Austrian advance guard [oob]) starts down from the Pratzen heights towards Telnitz and Sokolnitz, where Napoleon has left only Legrand's thin division [wh]. Kienmayer attacks Telnitz first [fn]. Liechtenstein's cavalry, posted in the wrong place overnight, cuts across the columns and holds up Langeron [wiki]. Soult's two divisions wait unseen in the fog of the Goldbach valley, while the hilltops stand clear above it like islands [burton].",
        ("Deliberate weakness (bait)", "Napoleon weakened his right on purpose and gave up the high ground, inviting the Allies to attack where he wanted them to. Every battalion they sent south was one fewer on the Pratzen [wiki].", "bait"),
        wp(950, 900), 12, fog=0.95, conf="medium", cite=["wp22", "wp23", "stut", "fn", "oob"],
        arrows=[A("au", "move", wp(880, 1110), wp(810, 1098)), A("ru", "move", wp(990, 1020), wp(900, 1060), wp(820, 1085)),
                A("ru", "move", wp(1040, 960), wp(920, 1010), wp(840, 1035)), A("ru", "move", wp(1060, 900), wp(930, 960), wp(840, 975)),
                A("ru", "move", wp(1150, 820), wp(1170, 720), wp(1200, 620)), A("fr", "move", wp(560, 1150), wp(640, 1120), wp(700, 1105))],
        events=[(wp(762, 1099), "Kienmayer attacks Telnitz", ["fn"]), (B.geo["Zuran"], "Napoleon on the height near Schlappanitz", ["md1846"]), (wp(900, 700), "Soult's corps hidden in the valley fog", ["burton"])],
        debate="The French accounts and the Fondation Napoléon put Kienmayer's first attack at 07:00 [fn]; the Russian official history says the three columns left their bivouacs only at 08:00 [md1846]. The map follows the earlier time, which most modern accounts use.")
B.phase("08:00", "Telnitz falls", "The fight for the Goldbach villages",
        "Dokhturov's 1st Column joins Kienmayer and takes Telnitz [wh]. Davout's lead brigade, after a march of about 110 km in two days, arrives from the south-west and retakes it, only to be thrown out by Austrian hussars [wiki]. Langeron and Przhebyshevsky attack Sokolnitz village and its castle, which change hands again and again [wiki]. On the plateau the 4th Column begins to move off the heights as well [fn].",
        ("Defending villages and strongpoints", "Stone farm buildings and walls let a few battalions hold off many times their number. Villages along a stream became small fortresses, which is why so few French held the Goldbach for so long.", "strongpoint-defence"),
        wp(800, 1020), 7, fog=0.75, conf="medium", cite=["wp23", "wiki", "wh", "fn", "thi"],
        arrows=[A("ru", "charge", wp(870, 1080), wp(800, 1090)), A("fr", "charge", wp(640, 1120), wp(705, 1105)),
                A("ru", "move", wp(900, 1035), wp(830, 1037)), A("ru", "move", wp(920, 980), wp(840, 976)), A("fr", "move", wp(800, 860), wp(790, 930))],
        events=[(wp(762, 1099), "Telnitz taken, retaken and lost again", ["wiki"]), (wp(791, 972), "Sokolnitz castle changes hands", ["wiki"])])
B.phase("09:00", "Sun of Austerlitz", "Soult storms the Pratzen heights",
        "As the sun clears the mist from the high ground, Napoleon sees the Allied centre emptying [md1846] and asks Soult how long he needs to reach the top. By Thiébault's account Soult answered twenty minutes at most, and Napoleon waited a further quarter of an hour so the fog in the valleys would hide the approach [thi]; Ségur remembered the answer as ten minutes [segur]. Morand's advance guard heads for the southern summit, Thiébault's brigade for Pratzen village, and Varé with all of Vandamme's division for the eastern part of the heights [thi]. They run into Miloradovich's Russians and Kolowrat's Austrians, still in march column [wh]. The Tsar and the Emperor Francis have just reached Kutuzov [md1846]. In the north, Lannes, Murat and Bernadotte advance east as Bagration comes down the Olmütz road [wp23].",
        ("Central position", "The Allies had stripped their centre to strengthen the attack on the French right. A sudden blow at the weakened centre would split the Allied army in two.", "central-position"),
        wp(1050, 760), 8, fog=0.4, conf="high", cite=["wp23", "md1846", "thi", "segur", "wh"],
        arrows=[A("fr", "move", wp(930, 760), wp(990, 770), wp(1050, 790)), A("fr", "move", wp(920, 805), wp(980, 815), wp(1030, 835)),
                A("fr", "move", wp(920, 660), wp(990, 665), wp(1070, 655)), A("fr", "move", wp(910, 700), wp(990, 712), wp(1060, 715)),
                A("fr", "move", wp(880, 560), wp(950, 590), wp(1020, 600)), A("ru", "move", wp(1600, 300), wp(1450, 345), wp(1320, 382)),
                A("ru", "move", wp(1380, 700), wp(1300, 620), wp(1240, 572))],
        events=[(wp(1043, 766), "St Hilaire meets the 4th Column at Pratzen", ["wh"]), (wp(1140, 690), "Vandamme heads for Staré Vinohrady", ["wiki"])],
        debate="Ségur, at headquarters, puts the order at about 08:00 [segur]; others give 08:30-09:00 [fn] [wiki]. The West Point map shows the attack under way at 09:00 [wp23], which is used here. The exchange with Soult survives in different versions (twenty minutes in Thiébault, ten in Ségur) and should be read as a reported anecdote.")
B.phase("10:00", "The Pratzeberg", "Fighting for the summit",
        "The Allies make four desperate attempts over more than three hours to retake the Pratzen heights [thi]. Kolowrat leads his Austrian regiments at Thiébault's brigade, which waits with nine guns loaded with round and grape and breaks them at 30-40 yards; Thiébault and Morand then drive back Kamensky's brigade, which had turned back from Langeron's column, and take two batteries [thi] [md1846]. In the north Grand Duke Constantine's Uhlans charge Kellermann's light horse near Blasowitz, ride on into Caffarelli's infantry and are cut to pieces [wh]. Bagration's attack on the French left breaks against the guns on the Santon [wh].",
        ("Infantry against cavalry", "Formed infantry that kept its nerve could stop a cavalry charge with volleys, and cavalry that broke a charge on it was then open to a counter-charge. Lannes' infantry and Murat's cavalry worked together this way all morning.", "infantry-vs-cavalry"),
        wp(1100, 680), 8.5, fog=0.12, conf="medium", cite=["thi", "md1846", "wh", "wp23"], debate="Who turned Kamensky's brigade back is disputed: the Russian official history credits Kamensky himself [md1846], while Langeron's memoirs claim the decision was his.",
        arrows=[A("ru", "charge", wp(1010, 930), wp(1040, 905), wp(1062, 892)), A("fr", "charge", wp(1050, 840), wp(1075, 870)),
                A("ru", "charge", wp(1260, 540), wp(1200, 530), wp(1160, 522)), A("fr", "charge", wp(1060, 540), wp(1110, 540), wp(1140, 535)),
                A("ru", "move", wp(1300, 420), wp(1240, 395), wp(1200, 382)), A("fr", "fire", wp(1078, 374), wp(1190, 384))],
        events=[(wp(1060, 860), "Thiébault's guns break Kolowrat's attack at 30-40 yards", ["thi"]), (wp(1160, 528), "The Uhlans' charge broken near Blasowitz", ["wh"]), (B.geo["Santon"], "Santon battery checks Bagration", ["wh"])])
B.phase("11:00", "Plateau taken", "The Allied army is cut in two",
        "Vandamme takes Staré Vinohrady from Rottermund's Austrians and the last of Miloradovich's battalions [wh]. Kamensky is driven off to the south-east [md1846]. By 11:00 the French hold the Pratzen plateau from end to end [wh], and the Allied left wing in the Goldbach valley is cut off from the rest of the army [fn]. Napoleon rides up onto the heights [wiki].",
        ("Central position", "Holding the high ground in the middle of the field let Napoleon turn either way. The Allied wings could no longer support each other, and he could deal with them one at a time.", "central-position"),
        wp(1110, 780), 8, conf="high", cite=["wh", "fn", "md1846", "wiki"],
        arrows=[A("fr", "charge", wp(1120, 650), wp(1170, 642)), A("fr", "charge", wp(1110, 690), wp(1160, 680)),
                A("ru", "retreat", wp(1170, 720), wp(1260, 740), wp(1340, 745)), A("au", "retreat", wp(1120, 860), wp(1220, 870), wp(1300, 860)),
                A("ru", "retreat", wp(1080, 930), wp(1130, 975), wp(1160, 995))],
        events=[(wp(1140, 690), "Staré Vinohrady falls", ["wh"]), (wp(1095, 860), "Napoleon on the Pratzen heights", ["wiki"]), (B.places["Blasowitz"][:2], "Russian Guard Jäger defend Blasowitz against Lannes", ["thi"])])
B.phase("13:00", "Guard against Guard", "The Russian Imperial Guard counterattacks",
        "Grand Duke Constantine throws the Russian Imperial Guard at Vandamme near Staré Vinohrady [wh]. The Guard infantry drives back the 4e Ligne and the 24e Léger; then the Life Guard Horse ride down a battalion of the 4e and take its eagle, the only French eagle not recovered that day [lgh] [fraser].  Napoleon sends in Bessières with the cavalry of his own Guard [wiki]. In a great cavalry melee Rapp's chasseurs and Mamelukes beat the Russian Guard horse, Drouet's division gives the French a line to rally on, and the Russian Guard falls back towards Krzenowitz [wh]. Rapp brings the captured colours to Napoleon at Staré Vinohrady [fnplaces].",
        ("Committing the reserve", "Both commanders kept their best troops back for the decisive moment. Napoleon committed only his Guard cavalry and kept his Guard infantry fresh [wiki].", "reserve-commitment"),
        wp(1150, 660), 6, conf="medium", cite=["wh", "wiki", "lgh", "fraser", "fnplaces"],
        arrows=[A("ru", "charge", wp(1240, 610), wp(1210, 640), wp(1185, 660)), A("ru", "charge", wp(1260, 600), wp(1200, 630), wp(1150, 655)),
                A("fr", "charge", wp(1030, 660), wp(1090, 650), wp(1145, 642)), A("fr", "move", wp(1100, 650), wp(1150, 665))],
        events=[(wp(1110, 690), "The Life Guard Horse take the eagle of the 4e Ligne", ["lgh"]), (wp(1150, 645), "Rapp's charge beats the Russian Guard cavalry", ["wh"])],
        debate="Accounts put the Guard counterattack anywhere from late morning to about 13:00 [fn] [wh]; the order of events is agreed, the exact time is not.")
B.phase("14:00", "The trap closes", "Soult wheels south",
        "With the centre won, Napoleon turns Soult's corps south off the plateau into the rear of the three Allied columns still fighting along the Goldbach, while Davout and Legrand press from the west [wp24] [wh]. Przhebyshevsky's column is cut off at Sokolnitz [wh]. In the north Bagration falls back to the Posoritz post house, and Kolowrat, Liechtenstein and the Russian Guard re-form east of the Littawa near Austerlitz [wp24].",
        ("Envelopment", "An enemy attacked from front and rear at once has to fight both ways or run. The Allied columns, already exhausted, were caught between Davout and Soult.", "envelopment"),
        wp(920, 1000), 8.5, conf="high", cite=["wp24", "wh"],
        arrows=[A("fr", "move", wp(1040, 860), wp(1020, 930), wp(990, 1030)), A("fr", "move", wp(1080, 800), wp(1090, 900), wp(1110, 995)),
                A("fr", "move", wp(1120, 860), wp(1150, 940), wp(1160, 1010)), A("fr", "move", wp(1000, 870), wp(950, 950), wp(915, 1000)),
                A("ru", "retreat", wp(1300, 395), wp(1360, 365), wp(1395, 350)), A("fr", "move", wp(1110, 600), wp(1200, 640), wp(1270, 680))],
        events=[(wp(820, 990), "Przhebyshevsky's column cut off at Sokolnitz", ["wh"]), (wp(1460, 690), "Allied centre re-forms near Austerlitz", ["wp24"])])
B.phase("15:30", "The ponds", "Retreat around the frozen ponds",
        "Przhebyshevsky surrenders near Sokolnitz and Kobelnitz [wh]. Vandamme takes Aujezd, where about 4,000 Allied soldiers are captured; Buxhöwden escapes with a few battalions [stut]. Dokhturov's column gathers on the plain between Telnitz and the lake [stut] and escapes along the dyke between the Satschan and Menitz ponds, so narrow that only two men could pass abreast; a bridge gives way under the guns, some troops try the frozen pond, and the ice breaks under them while the French Guard artillery, placed on the heights by Napoleon himself, fires on the ponds [md1846] [marbot]. Kienmayer's cavalry covers the retreat from the hill between Telnitz and Menitz [stut].",
        ("Rearguard and escape route", "Dokhturov kept enough order to fight a rearguard action and get most of his men across the one narrow exit. A beaten army that keeps its formations can still escape.", "escape-route"),
        wp(900, 1150), 7, conf="medium", cite=["md1846", "stut", "marbot", "wh", "ice"],
        arrows=[A("ru", "retreat", wp(840, 1100), wp(805, 1135), wp(790, 1228), wp(880, 1240)), A("ru", "retreat", wp(880, 1080), wp(960, 1110), wp(1050, 1115)),
                A("au", "move", wp(845, 1118), wp(780, 1150), wp(745, 1172)), A("fr", "fire", wp(1118, 1035), wp(960, 1165)),
                A("fr", "fire", wp(1100, 1060), wp(930, 1120)), A("fr", "move", wp(990, 1035), wp(950, 1080))],
        events=[(wp(880, 1170), "Ice breaks at the pond edge", ["md1846", "ice"]), (wp(830, 960), "Przhebyshevsky surrenders", ["wh"]), (wp(790, 1228), "The narrow dyke between the ponds", ["md1846"]), (wp(1110, 1065), "French Guard artillery fires on the ponds (Napoleon's order)", ["marbot", "md1846"])],
        debate="Napoleon's bulletin and Marbot spoke of thousands drowned [marbot]. Stutterheim and the Russian official history confirm that men died on the ice [stut] [md1846], but when the ponds were drained soon afterwards the finds reported were 28-30 guns, about 150 horses and only two or three bodies [ice]. Popular modern estimates of the drowned run from a few dozen to about 200 [wh]; the evidence for any exact figure is weak.")
B.phase("16:30", "Nightfall", "The Battle of the Three Emperors ends",
        "As the sun sets, the last Allied troops leave the field towards Austerlitz and Hungary, and Bagration withdraws towards Raussnitz [wh] [md1844]. The Allies have lost about 27,000 men, nearly half of them prisoners [wiki], and between 131 guns (Kutuzov's own report [millar04]) and about 180 [wiki]; the French about 9,000 [wiki]. Emperor Francis asked for an armistice, and the Third Coalition collapsed [stut].",
        ("Decisive battle", "Napoleon aimed not just to win the field but to destroy the enemy army's ability to keep fighting. Austerlitz did that in a single day.", "decisive-battle"),
        wp(1150, 850), 12, conf="high", cite=["wiki", "md1844", "wh", "stut", "millar04"],
        arrows=[A("ru", "retreat", wp(1450, 720), wp(1560, 700), wp(1640, 700)), A("ru", "retreat", wp(1450, 330), wp(1550, 300), wp(1620, 280)),
                A("ru", "retreat", wp(1000, 1240), wp(1080, 1260), wp(1150, 1280))],
        events=[(wp(1660, 653), "Allied army retreats past Austerlitz", ["wp24", "md1844"]), (wp(1085, 985), "Napoleon at St Anthony's chapel", ["wiki"])])

B.export()
