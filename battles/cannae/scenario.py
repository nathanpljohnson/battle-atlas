"""Cannae, 2 August 216 BC.

This reconstruction uses Polybius 3.110-117 for the sequence, force structure and
relative deployment. Exact ground coordinates are deliberately approximate: the
course of the Aufidus and the battle location remain disputed. See brief.md.
"""
import os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "..", "tools"))
os.chdir(HERE)
from battlekit import Battle, mv

B = Battle("cannae", HERE)

# Sources: the map is a schematic guide, not a georeferenced positional authority.
B.source("poly", "Polybius, Histories 3.110-117, trans. W. R. Paton", "https://penelope.uchicago.edu/Thayer/E/Roman/Texts/Polybius/3*.html", "earliest surviving continuous account: camps, deployment, tactical sequence, strengths and losses", "primary")
B.source("livy", "Livy, Ab urbe condita 22.44-54", "https://www.perseus.tufts.edu/hopper/text?doc=Perseus:text:1999.02.0200:book=22", "later Roman narrative; alternative casualty total and dramatic aftermath", "primary")
B.source("wp", "U.S. Military Academy, The Battle of Cannae: Initial Roman Attack and Defeat of Roman Cavalry", None, "schematic initial deployment and the broad relationship of camps, river and armies; supplied local image", "staff-map")
B.source("roth", "Johannes Rothert, Geschichte des römischen Volkes, Cannae tactical diagram", None, "period-era schematic supplied locally; supports the broad double-envelopment sequence, not exact coordinates", "period-map")
B.source("mahaney", "William C. Mahaney, 'Cannae Battlefield: a geomorphic-geoarchaeologic perspective,' Studia Quaternaria 41 (2024), 37-42", "https://doi.org/10.24425/sq.2023.148037", "modern geomorphology: the Ofanto floodplain, terraces and limits of reconstructing the ancient field", "scholarly")
B.source("gold", "Adrian Goldsworthy, Cannae: Hannibal's Greatest Victory (2001)", "https://www.routledge.com/Cannae-The-Experience-of-Battle-in-the-Second-Punic-War/Goldsworthy/p/book/9780415327435", "identified bibliographically; no map claim depends on its unavailable unit-level detail", "scholarly")
B.source("data", "AWS Terrain Tiles; OpenStreetMap and Overpass", "https://registry.opendata.aws/terrain-tiles/", "modern elevation, river and modern-change detection", "data")

B.meta = {
    "title": "Cannae", "year": "216 BC", "era": "ancient", "war": "Second Punic War",
    "eyebrow": "2 August 216 BC · Apulia · Second Punic War",
    "subtitle": "Hannibal yields the centre, turns the flanks and closes the most famous double envelopment in ancient warfare.",
    "sides": {
        "rom": {"name": "Roman", "top": "#9f3028", "side": "#72231e", "mark": "#f8eee0", "arrow": "#d64a3b", "flag": "#9f3028"},
        "car": {"name": "Carthaginian", "top": "#253f72", "side": "#162847", "mark": "#f3ead7", "arrow": "#527ac9", "flag": "#253f72"},
    },
    "belligerents": [
        {"name": "Roman Republic and allies", "short": "Romans", "commander": "Varro and Paullus", "sides": ["rom"], "code": "numbers"},
        {"name": "Carthaginian army", "short": "Carthaginians", "commander": "Hannibal Barca", "sides": ["car"], "code": "letters"},
    ],
    "forces": {
        "start": [{"label": "Romans", "n": 86400, "segs": [["rom", 1]]}, {"label": "Carthaginians", "n": 50000, "segs": [["car", 1]]}],
        "end": [{"label": "Romans", "n": 67500, "segs": [["rom", 1]]}, {"label": "Carthaginians", "n": 5700, "segs": [["car", 1]]}],
    },
    "sun": {"lat": 41.30, "decl": 17.5, "note": "August sun and wind are approximations; ancient local time and calendar conversion are uncertain."},
    "wind": 315, "view": {"az": 0.0, "el": 1.0}, "unitScale": 1.45, "unitLabelDist": 11,
    "ground": {"season": "summer", "relief": 80},
    "strengthNote": "Polybius gives about 80,000 Roman infantry and just over 6,000 cavalry against a Carthaginian force of just over 40,000 infantry and 10,000 cavalry [poly]. The Roman headline includes 10,000 men left in camp; they are shown separately and captured after the field battle. Losses across moments are illustrative allocations of Polybius's totals, not a casualty return. Livy's lower Roman death total (48,200) is shown in the debate notes [livy].",
    "method": "This is a tactical reconstruction, not a surveyed battlefield map. Unit positions are placed on a modern terrain window around Canne della Battaglia using Polybius's relative order (Romans facing south; Carthaginians north; Carthaginian cavalry left/right and African flank reserves), checked against two schematic maps [poly] [wp] [roth]. The ancient Aufidus channel and exact battle location are unsettled; all coordinate-level claims are low confidence [mahaney]. Modern terrain is shown only as a relief context.",
    "notes": "The two Roman camps and Hannibal's camp are shown schematically. No historical map overlay is offered because the available maps are tactical diagrams rather than georeferenceable surveys. Heights are exaggerated; woodland, roads and the exact river trace are illustrative. The intentionally coarse unit groupings are a readability choice, not evidence for exact tactical subdivisions.",
}

# The modern Ofanto is a visual anchor only. Polybius calls it the Aufidus and places
# the two armies and camps in a configuration that cannot be fixed to its ancient bends.
B.place("Cannae")
B.hill("Canne ridge", (41.300, 16.151))
B.hill("Ofanto terraces", (41.305, 16.112))
B.water["rivers"] = [{"p": [(41.288, 16.057), (41.287, 16.080), (41.289, 16.103), (41.287, 16.126), (41.290, 16.150), (41.286, 16.174), (41.288, 16.194)], "w": 4, "ford": True}]
B.water["labels"] = {"Aufidus / Ofanto (modern course)": (41.288, 16.125)}
B.roads = [[(41.318, 16.075), (41.315, 16.105), (41.310, 16.130), "Cannae"], [(41.330, 16.090), (41.320, 16.125), (41.305, 16.151)]]
B.woods = [[41.334, 16.072, 480, 220], [41.301, 16.178, 340, 180]]
B.camps = [
    {"a": [41.327, 16.068], "b": [41.327, 16.082], "rows": 3, "until": 0},
    {"a": [41.316, 16.060], "b": [41.316, 16.073], "rows": 2, "until": 0},
    {"a": [41.294, 16.150], "b": [41.294, 16.165], "rows": 3, "until": 1},
]

def U(uid, side, typ, name, strength, frontage, keys, note, conf, men, cite, via=None):
    u = B.unit(uid, side, typ, name, strength, frontage, note=note, conf=conf, men=men, cite=cite)
    for phase, (pos, facing, form) in keys.items():
        u.at(phase, pos, facing, form, via=(via or {}).get(phase))
    return u

# Roman line: Polybius describes an unusually deep, compressed centre, with cavalry at
# each end. These coordinates make that relationship legible but are low-confidence.
U("r_cav_right", "rom", "cav", "Roman citizen cavalry", "2,400 cavalry", 560,
  {0: ((41.324, 16.088), 180, "L"), 2: ((41.318, 16.090), 180, "F"), 3: ((41.310, 16.081), 235, "R"), 5: ((41.302, 16.070), 235, "R")},
  "Roman cavalry on the right beside the river in Polybius's order; it was defeated by Hasdrubal's Spanish and Celtic horse [poly].", "medium", {0: 2400, 3: 700, 5: 180}, ["poly", "wp"], {3: [(41.315, 16.085)]})
U("r_legions", "rom", "hi", "Roman legions", "25,000 heavy infantry", 1250,
  {0: ((41.326, 16.112), 180, "C"), 1: ((41.322, 16.112), 180, "C"), 2: ((41.317, 16.112), 180, "C"), 3: ((41.312, 16.117), 180, "F"), 4: ((41.3075, 16.122), 180, "F"), 5: ((41.306, 16.122), 180, "F")},
  "The Roman citizen heavy infantry, packed more deeply and closely than normal [poly].", "medium", {0: 25000, 3: 23800, 4: 19000, 5: 8000}, ["poly", "livy", "wp"])
U("r_allies", "rom", "hi", "Italian allied infantry", "30,000 heavy infantry", 1350,
  {0: ((41.326, 16.132), 180, "C"), 1: ((41.322, 16.132), 180, "C"), 2: ((41.317, 16.132), 180, "C"), 3: ((41.308, 16.127), 180, "F"), 4: ((41.3035, 16.122), 180, "F"), 5: ((41.3025, 16.122), 180, "F")},
  "Allied heavy infantry forms the other half of the unusually deep Roman mass [poly].", "medium", {0: 30000, 3: 28500, 4: 22500, 5: 9000}, ["poly", "livy", "wp"])
U("r_velites", "rom", "arc", "Roman light troops", "15,000 velites and light infantry", 900,
  {0: ((41.319, 16.122), 180, "L"), 1: ((41.315, 16.122), 180, "F"), 2: ((41.311, 16.122), 180, "R"), 4: ((41.305, 16.122), 180, "R")},
  "Light infantry was posted in front of the line and opened the battle with the opposing skirmishers [poly].", "medium", {0: 15000, 2: 13200, 4: 9000}, ["poly", "wp"])
U("r_cav_left", "rom", "cav", "Italian allied cavalry", "4,000 cavalry", 700,
  {0: ((41.324, 16.155), 180, "L"), 2: ((41.319, 16.154), 180, "F"), 3: ((41.314, 16.163), 125, "R"), 5: ((41.306, 16.177), 125, "R")},
  "Allied cavalry on the Roman left was held by the Numidians until Hasdrubal arrived [poly].", "medium", {0: 4000, 3: 3000, 5: 500}, ["poly", "wp"], {3: [(41.317, 16.160)]})
U("r_camp", "rom", "hi", "Roman camp garrison", "10,000 infantry", 1050,
  {0: ((41.316, 16.066), 180, "L"), 1: ((41.316, 16.066), 180, "L"), 6: ((41.316, 16.066), 180, "R")},
  "Polybius says Lucius left 10,000 infantry in the camp; Hannibal's camp guard trapped and captured them after the field victory [poly].", "medium", {0: 10000, 6: 0}, ["poly"], {6: [(41.310, 16.070)]})

# Hannibal's army: Spanish/Celtic centre gives ground; African heavy infantry turns in;
# the two cavalry wings are kept separate so their distinct roles remain visible.
U("c_celtiber", "car", "hi", "Spanish and Celtic centre", "24,000 infantry", 1600,
  {0: ((41.307, 16.122), 0, "C"), 1: ((41.311, 16.122), 0, "C"), 2: ((41.314, 16.122), 0, "C"), 3: ((41.310, 16.122), 0, "R"), 4: ((41.300, 16.122), 0, "F"), 5: ((41.2995, 16.122), 0, "F")},
  "Spaniards and Celts formed the projecting centre. Polybius says it yielded under pressure, drawing the Roman mass between the Africans [poly].", "medium", {0: 24000, 3: 21000, 5: 20000}, ["poly", "roth", "wp"])
U("c_africa_w", "car", "hi", "African heavy infantry, western wing", "4,000 infantry", 760,
  {0: ((41.307, 16.100), 0, "L"), 2: ((41.307, 16.100), 0, "L"), 3: ((41.309, 16.104), 90, "F"), 4: ((41.307, 16.109), 90, "F"), 5: ((41.304, 16.113), 90, "F")},
  "African heavy infantry held back on the flank, then faced inward against the Roman side [poly].", "medium", {0: 4000, 5: 3500}, ["poly", "roth"])
U("c_africa_e", "car", "hi", "African heavy infantry, eastern wing", "4,000 infantry", 760,
  {0: ((41.307, 16.144), 0, "L"), 2: ((41.307, 16.144), 0, "L"), 3: ((41.309, 16.140), 270, "F"), 4: ((41.307, 16.135), 270, "F"), 5: ((41.304, 16.131), 270, "F")},
  "The second African wing mirrors the inward turn described by Polybius [poly].", "medium", {0: 4000, 5: 3500}, ["poly", "roth"])
U("c_skirm", "car", "arc", "Slingers and javelin troops", "8,000 light troops", 850,
  {0: ((41.313, 16.122), 0, "L"), 1: ((41.316, 16.122), 0, "F"), 2: ((41.312, 16.122), 0, "R"), 3: ((41.308, 16.122), 0, "R")},
  "Hannibal sent slingers and javelin troops forward before the main line crossed and deployed [poly].", "medium", {0: 8000, 3: 6800}, ["poly", "wp"])
U("c_hasdrubal", "car", "cav", "Spanish and Celtic cavalry (Hasdrubal)", "6,000 cavalry", 860,
  {0: ((41.307, 16.081), 0, "L"), 1: ((41.313, 16.084), 0, "F"), 2: ((41.317, 16.088), 0, "F"), 3: ((41.314, 16.150), 85, "C"), 4: ((41.313, 16.140), 180, "F"), 5: ((41.3095, 16.122), 180, "F")},
  "Hasdrubal's cavalry defeated the Roman right, then rode across to decide the other cavalry fight and attack the infantry's rear [poly].", "high", {0: 6000, 5: 5800}, ["poly", "wp"], {3: [(41.320, 16.110), (41.318, 16.135)], 4: [(41.316, 16.142)], 5: [(41.315, 16.130)]})
U("c_numidian", "car", "lc", "Numidian cavalry (Hanno)", "4,000 cavalry", 760,
  {0: ((41.307, 16.165), 0, "L"), 1: ((41.313, 16.158), 0, "F"), 2: ((41.317, 16.154), 0, "F"), 3: ((41.316, 16.158), 0, "F"), 4: ((41.312, 16.148), 225, "C"), 5: ((41.307, 16.170), 110, "F")},
  "Numidians kept the allied cavalry occupied; Hasdrubal then joined them and left them to pursue the fugitives [poly].", "high", {0: 4000, 5: 3800}, ["poly", "wp"])

B.commander("varro", "rom", "Varro", {0: (41.329, 16.120), 2: (41.321, 16.120), 4: (41.311, 16.120)}, "Command alternated by day; Polybius makes Varro commander on the battle morning [poly].")
B.commander("paullus", "rom", "Paullus", {0: (41.325, 16.094), 2: (41.318, 16.095), 4: (41.307, 16.108)}, "Paullus rode from the Roman right into the infantry fight and was killed there [poly].")
B.commander("hannibal", "car", "Hannibal and Mago", {0: (41.305, 16.122), 2: (41.311, 16.122), 4: (41.305, 16.122)}, "Hannibal and Mago commanded the centre [poly].")

B.phase("06:00", "Deployment", "A battle on uncertain ground",
  "Varro brings the troops from both Roman camps across the Aufidus and faces south. Polybius gives about 80,000 Roman infantry and more than 6,000 cavalry. Hannibal's line faces north: Spanish and Celtic cavalry by the river, Africans on the flanks, the Spanish-Celtic centre forward, and Numidians on the far wing [poly].",
  ("Double envelopment", "A centre gives ground without breaking while strong wings turn inward. It only works if the enemy keeps pressing into the pocket.", "double-envelopment"), (41.313, 16.122), 8.5,
  arrows=[B.arrow("rom", "move", (41.330, 16.120), (41.320, 16.120)), B.arrow("car", "move", (41.300, 16.122), (41.308, 16.122))],
  events=[((41.296, 16.151), "Cannae and the ancient river course anchor the reconstruction, but not an exact battlefield grid [mahaney]", ["mahaney"])], conf="low",
  debate="The ancient Aufidus channel and exact field are disputed. These coordinate placements are illustrative; Polybius's relative deployment is the higher-confidence claim [poly] [mahaney].", cite=["poly", "mahaney", "wp"])
B.phase("07:00", "Skirmishers", "The front screens collide",
  "The advanced guards begin the fight. Polybius says neither side gained an advantage in this preliminary contest; the main infantry and cavalry are still forming their decisive relationships [poly].",
  ("Fixing force", "Light troops can occupy and test an enemy while the main formation remains intact.", "fixing-force"), (41.314, 16.122), 7.0,
  arrows=[B.arrow("rom", "fire", (41.319, 16.122), (41.313, 16.122)), B.arrow("car", "fire", (41.313, 16.122), (41.319, 16.122))],
  events=[((41.315, 16.122), "Skirmishers engage before the heavy infantry [poly]", ["poly"])], conf="medium", cite=["poly"])
B.phase("08:00", "Cavalry decision", "Hasdrubal breaks the Roman right",
  "The Spanish and Celtic horse defeats the Roman cavalry near the river. At the same time the heavy infantry begins its struggle; the Roman mass pushes into the projecting Spanish and Celtic centre [poly].",
  ("Shock cavalry", "Close-order cavalry can decide a wing quickly, then exploit its mobility elsewhere.", "shock-cavalry"), (41.315, 16.112), 6.0,
  arrows=[B.arrow("car", "charge", (41.307, 16.081), (41.318, 16.090)), B.arrow("rom", "move", (41.322, 16.122), (41.316, 16.122))],
  events=[((41.317, 16.088), "The Roman right-wing cavalry gives way [poly]", ["poly"])], conf="medium", cite=["poly", "wp"])
B.phase("09:00", "The centre yields", "The Roman mass presses into the crescent",
  "The Spanish and Celts fall back under the pressure of the legions. Polybius's key point is sequential contact: the centre was engaged before the African wings, so the pursuing Roman mass advanced into the gap [poly].",
  ("Using dead ground", "A formation can conceal its intended shape until the enemy's commitment makes a response too late.", "dead-ground"), (41.311, 16.122), 5.0,
  arrows=[B.arrow("rom", "move", (41.317, 16.112), (41.310, 16.112)), B.arrow("rom", "move", (41.317, 16.132), (41.310, 16.132)), B.arrow("car", "retreat", (41.314, 16.122), (41.310, 16.122))],
  events=[((41.310, 16.122), "The centre's controlled withdrawal draws the Roman mass forward [poly]", ["poly"])], conf="medium", cite=["poly", "roth"])
B.phase("10:00", "Flanks close", "The Roman mass is pinched from both sides",
  "First the Africans turn inward against both exposed Roman flanks. Hasdrubal has crossed to the other cavalry wing, but the rear is still open: this moment is the pinch, not yet the completed ring [poly].",
  ("Envelopment", "A force attacks front and flank together, denying the enemy room to face every threat.", "envelopment"), (41.307, 16.122), 4.2,
  arrows=[B.arrow("car", "charge", (41.309, 16.104), (41.307, 16.109)), B.arrow("car", "charge", (41.309, 16.140), (41.307, 16.135)), B.arrow("car", "charge", (41.314, 16.150), (41.313, 16.140))],
  events=[((41.307, 16.109), "Western African wing turns into the Roman flank [poly]", ["poly"]), ((41.307, 16.135), "Eastern African wing turns into the other flank [poly]", ["poly"]), ((41.313, 16.140), "Hasdrubal wins the second cavalry fight and can ride behind the Roman mass [poly]", ["poly"])], conf="medium", cite=["poly"])
B.phase("11:00", "Cavalry seals the rear", "The ring closes behind the Romans",
  "Only now does Hasdrubal's cavalry arrive behind the Roman mass. The Africans keep both flanks pinned while cavalry closes the northern exit and the rallied Spanish and Celtic centre holds the front, while the Numidians pursue the broken allied horse. Polybius describes Romans turning in small groups to meet attacks from every direction [poly].",
  ("Rear attack", "A force that has won a wing can turn mobility into a rear attack before the enemy can re-form.", "rearguard"), (41.305, 16.122), 5.0,
  arrows=[B.arrow("car", "charge", (41.307, 16.109), (41.304, 16.113)), B.arrow("car", "charge", (41.307, 16.135), (41.304, 16.131)), B.arrow("car", "charge", (41.313, 16.140), (41.315, 16.130), (41.3095, 16.122)), B.arrow("car", "move", (41.312, 16.148), (41.307, 16.170))],
  events=[((41.3095, 16.122), "Hasdrubal's cavalry seals the Roman rear [poly]", ["poly"]), ((41.304, 16.122), "The trapped Roman mass has no room to turn or deploy [poly]", ["poly"]), ((41.305, 16.122), "Paullus is killed in the infantry struggle [poly]", ["poly"])], conf="medium",
  debate="The sequence of the final slaughter is much clearer than its duration. This model uses hourly moments only to make the tactical relationship legible, not to assert an exact stopwatch chronology [poly] [livy].", cite=["poly", "livy"])
B.phase("12:00", "Destruction and flight", "The Roman army collapses",
  "Polybius reports about 70,000 Roman dead, 10,000 captives not in the main battle, and only about 3,000 infantry escaping the field; he gives 5,700 Carthaginian dead. Livy gives a much lower Roman death total. The strength chart follows Polybius while preserving this disagreement [poly] [livy].",
  ("Pursuit", "Pursuit turns a defeated army into a destroyed one, but the sources must distinguish field losses, camp captures and fugitives.", "pursuit"), (41.303, 16.122), 3.8,
  arrows=[B.arrow("rom", "retreat", (41.304, 16.112), (41.302, 16.070)), B.arrow("rom", "retreat", (41.304, 16.132), (41.306, 16.177))],
  events=[((41.303, 16.122), "Polybius's loss total is adopted for the chart; Livy's lower figure remains a live disagreement [poly] [livy]", ["poly", "livy"])], conf="medium",
  debate="Polybius: about 70,000 Roman dead and 5,700 Carthaginian losses. Livy: 48,200 Romans killed and 8,000 Carthaginians killed. Ancient casualty figures cannot be reconciled here; both are reported, and neither makes the coordinate reconstruction more certain [poly] [livy].", cite=["poly", "livy"])

B.export()
