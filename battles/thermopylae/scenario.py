"""Thermopylae, 480 BC (three days of fighting, late summer).

Herodotus 7.175-233 is the framework; Diodorus 11.4-11 is the counter-account. The pass and the
480 BC coastline come from the Kromayer-Veith 1:25,000 and 1:100,000 maps (georeferenced, 25 m and
173 m) checked against OSM's Phocian wall and Kolonos. The Anopaea route is one reconstruction of
several (see brief.md). Clock times other than lamp-lighting, dawn and 'the hour the market fills'
are illustrative.
"""
import json, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "..", "tools"))
os.chdir(HERE)
from battlekit import Battle
from georef import Georef

B = Battle("thermopylae", HERE)
_g = Georef(HERE)
k5, k6 = _g("kv5"), _g("kv6")  # Kromayer-Veith map 5 (1:100,000) and map 6 (1:25,000)

B.source("hdt", "Herodotus, Histories 7.175-233 and 8.21-25, tr. G. C. Macaulay (1890)", "https://www.gutenberg.org/ebooks/2456", "the earliest account: the three narrows, the Phocian wall, the order of battle, the four-day wait, the three days of fighting, the Anopaea path, the kolonos and the losses", "primary")
B.source("diod", "Diodorus Siculus, Library 11.4-11, tr. C. H. Oldfather (Loeb, 1946)", "https://penelope.uchicago.edu/Thayer/E/Roman/Texts/Diodorus_Siculus/11A*.html", "later account after Ephorus: different Greek numbers (about 7,400), Medes then Cissians and Sacae, the deserter Tyrrhastiadas, and a night attack on Xerxes' tent", "primary")
B.source("paus", "Pausanias, Description of Greece 10.20-22, tr. W. H. S. Jones (Loeb, 1918)", "https://www.theoi.com/Text/Pausanias10B.html", "the Locrians put at no more than 6,000; two paths over Oeta, Hydarnes taking the easier one", "primary")
B.source("strabo", "Strabo, Geography 9.4.13-17, tr. H. L. Jones (Loeb, 1924)", "https://penelope.uchicago.edu/Thayer/E/Roman/Texts/Strabo/9D*.html", "Callidromus above the pass; Trachis, the Asopus and Melas", "primary")
B.source("kv", "J. Kromayer and G. Veith, Schlachten-Atlas zur antiken Kriegsgeschichte, Griech. Abt. Blatt 1, maps 5-7 and text (Leipzig, 1922-29), after L. and E. Harmening in Antike Schlachtfelder IV", "https://archive.org/details/kromayerveithschlachtenatlas", "German staff-quality maps built on Grundy's survey and the Carte de la Grèce: the 480 BC shore, the West, Middle and East Gates, the Phocian wall, the camps, the Phocian post on the Sastani saddle and five path hypotheses; georeferenced (map 6: 25 m; map 5: 173 m). German text translated in sources/NOTES.md", "staff-map")
B.source("grundy", "G. B. Grundy, The Great Persian War and its Preliminaries (London, 1901), ch. on Thermopylae", "https://archive.org/details/greatpersianwari00grunuoft", "field survey: the 480 BC shore at about the 5-10 yard contour; the mounds at the Middle Gate; the last stand on the 'second mound'", "scholarly")
B.source("stronk", "J. P. Stronk, 'Thermopylae 480 BC: ancient accounts of a battle', Talanta 46-47 (2014-15) 165-236", "https://www.talanta.nl/wp-content/uploads/2017/08/Stronk.pdf", "modern comparison of all the ancient accounts: the strengths table, the coast 1-8 km further out today, the unsettled Anopaea route, the date in August or September", "scholarly")
B.source("kraft", "J. C. Kraft, G. Rapp, G. J. Szemler, C. Tziavos and E. W. Kase, 'The Pass at Thermopylae, Greece', Journal of Field Archaeology 14 (1987) 181-198; redrawn after Rapp and Hill, Geoarchaeology (2006) fig. 3.19", "https://commons.wikimedia.org/wiki/File:Thermopylae_shoreline_changes_map.png", "geoarchaeology from boreholes: the 480 BC shoreline close under the cliffs and the pass some tens of metres wide. Consulted through the redrawn figure and summaries, not the article itself", "scholarly")
B.source("panel", "Thermopylae monument, site panel 'The area of Thermopyles and the Greek and Persian camps before the battle' (photo D. Mauro, 2018)", "https://commons.wikimedia.org/wiki/File:Maps_of_Thermopylae_01.jpg", "on-site Greek/English map: probable 480 BC coast, the Persian camp between the Melas and the Asopus, the gates, the Greek camp, the Anopaia path", "staff-map")
B.source("museum", "Thermopylae Battle Museum panel 'The Battle of Thermopyles (480 B.C.)' (photo D. Mauro, 2018)", "https://commons.wikimedia.org/wiki/File:Map_of_the_Battle_of_Thermopylae.jpg", "days 1-2 in front of the wall, the day 3 sortie further west, the end on Kolonos, the Anopaia path", "staff-map")
B.source("standrews", "'Kallidromos', Mountains of Greece blog (University of St Andrews, 2025), summarising P. W. Wallace, AJA 84 (1980) 15-23 and W. K. Pritchett", "https://mountainsofgreece.wp.st-andrews.ac.uk/2025/12/13/kallidromos/", "near-consensus that the middle of the path ran through the upper Asopus meadows from Eleftherochori to Nevropoli", "reference")
B.source("wp", "Wikipedia, 'Battle of Thermopylae' (after Lazenby 1993, Green 1996, Holland 2005, Cartledge 2006) and 'Kolonos Hill'", "https://en.wikipedia.org/wiki/Battle_of_Thermopylae", "modern estimates of the Persian army (120,000-300,000) and the Greek dead; Marinatos's 1939 arrowhead finds on Kolonos", "reference")
B.source("data", "AWS Terrain Tiles; OpenStreetMap (Phocian wall, Kolonos, Anthele, Melampygos stone, village points); Wikidata", "https://registry.opendata.aws/terrain-tiles/", "modern relief and place coordinates", "data")

B.meta = {
    "title": "Thermopylae", "year": "480 BC", "era": "ancient", "war": "Greco-Persian Wars",
    "eyebrow": "Late summer 480 BC · Malis · Greco-Persian Wars",
    "subtitle": "A few thousand Greeks hold the gap between Mount Kallidromos and the sea for two days, until a mountain path turns the position.",
    "sides": {
        "spa": {"name": "Spartans and helots", "top": "#9c2a22", "side": "#6e1c17", "mark": "#f1e4c8", "arrow": "#cf4a3a", "flag": "#9c2a22"},
        "gre": {"name": "Other Greeks", "top": "#a77a2c", "side": "#73531c", "mark": "#f6ecd6", "arrow": "#d39a3c", "flag": "#a77a2c"},
        "per": {"name": "Persian army", "top": "#4b3a7a", "side": "#30254f", "mark": "#efe6c9", "arrow": "#7d68c2", "flag": "#4b3a7a"},
        "imm": {"name": "Immortals (Hydarnes)", "top": "#2f6a6e", "side": "#1e4548", "mark": "#f2e3a6", "arrow": "#4fa3a8", "flag": "#2f6a6e"},
    },
    "belligerents": [
        {"name": "Hellenic League", "short": "Greeks", "commander": "Leonidas of Sparta", "sides": ["spa", "gre"], "code": "letters"},
        {"name": "Achaemenid Persian Empire", "short": "Persians", "commander": "Xerxes", "sides": ["per", "imm"], "code": "numbers"},
    ],
    "forces": {
        "start": [{"label": "Greeks", "n": 7100, "segs": [["spa", 0.169], ["gre", 0.831]]},
                  {"label": "Persians", "n": 120000, "segs": [["per", 0.917], ["imm", 0.083]]}],
        "end": [{"label": "Greeks", "n": 4675, "segs": [["gre", 1]]},
                {"label": "Persians", "n": 100000, "segs": [["per", 0.93], ["imm", 0.07]]}],
    },
    "sun": {"lat": 38.80, "decl": 8.0, "note": "Herodotus ties the campaign to the Carneia and the Olympic games; modern dates run from August to September 480 BC [stronk]. The sun is set for about 1 September. Herodotus's own times: Hydarnes leaves 'about lamp-lighting', reaches the summit at dawn, and Xerxes attacks at 'the hour when the market fills' [hdt]."},
    "wind": 45, "view": {"az": 0.0, "el": 0.95}, "unitScale": 0.7, "unitLabelDist": 6,
    "ground": {"season": "summer", "relief": 160},
    "days": {"1": "Day 1", "2": "Day 2", "3": "Day 3"},
    "strengthNote": "Greeks: Herodotus's list (5,200 with 1,000 Phocians) plus 900 helots and 1,000 Opuntian Locrians = 7,100. Diodorus gives about 7,400; Pausanias up to 11,200 [hdt] [diod] [paus]. Persians: Herodotus's millions are impossible; 120,000 is the low end of modern estimates [wp] [kv]. The Medes' and Cissians' myriads (10,000 each) and the 20,000 sent in on day 3 are illustrative; only the Immortals' 10,000 is a source figure [hdt]. Losses follow Herodotus's 20,000 Persian dead and the modern figure of about 2,000 Greek dead [hdt] [wp]; how they are spread across the moments is an estimate. On day 3 the dismissed allies (about 3,700) and the Phocians (about 1,000) leave or stand aside; the Thebans (about 340 left) surrender.",
    "method": "The 480 BC shoreline and the pass come from the Kromayer-Veith maps of 1922-29, which rest on Grundy's 1899 survey and the French staff survey. They are georeferenced to OSM's Phocian wall, Kolonos and old baths (map 6, 25 m) and to seven villages (map 5, 173 m) [kv] [data]. The vanished water is drawn over today's Spercheios plain, and the ground inside it is lowered to sea level; it agrees with Grundy's 5-10 yard contour and the geoarchaeological reconstruction [grundy] [kraft]. Unit positions follow Herodotus's sequence on that ground [hdt]. The Anopaea route and the Phocian post are one reconstruction among several, and are low confidence [kv] [standrews].",
    "notes": "The pass at the Middle Gate was some 15-30 m wide in 480; at this map's 43 m grid it shows as a strip, and the units' frontages are drawn wider than the hoplite files would have been. Today's shore lies 1-8 km further north [stronk]. The Anopaea route shown runs up from the Asopus crossing by Kalkomata and Paleo-Eleftherochori, through the Nevropoli meadows, over the Sastani saddle and down the Alpenoi ravine. Kromayer's shorter line via Alt-Damasta, and Leake's and Grundy's variants, are described in the debate notes. Diodorus's night attack on Xerxes' tent is not shown. The oak woods on Kallidromos are drawn schematically from Herodotus's 'all the mountain was covered with oak-trees'. Phocian and Locrian contingent positions in camp are illustrative. No historical-map overlay is offered.",
}

# ---- ground
COAST = json.load(open(os.path.join(HERE, "coast480.json")))
B.water["lakes"] = [COAST["poly"]]
B.water["rivers"] = [
    {"p": [k5(*p) for p in [(790, 1010), (830, 950), (880, 880), (930, 840), (990, 830), (1060, 830), (1130, 800), (1190, 770), (1240, 730), (1260, 680), (1290, 645), (1330, 620)]], "w": 3, "ford": True},
    {"p": [k5(*p) for p in [(640, 690), (700, 640), (760, 560), (870, 500), (950, 470), (1000, 462), (1040, 462)]], "w": 2, "ford": True},
    {"p": [k5(*p) for p in [(1300, 720), (1310, 680), (1318, 640)]], "w": 1.5, "ford": True},
]
B.water["labels"] = {"Malian Gulf in 480 BC (now dry land)": (38.828, 22.530), "Today's shore lies 3-5 km north": (38.858, 22.555),
                     "Asopus": k5(1130, 800), "Melas": k5(870, 500), "Hot springs (Chytroi)": (38.7943, 22.5300)}

WALL = (38.79478, 22.53519)            # midpoint of the wall on map 6 (OSM 'Teichos Phokeon' 38.79445, 22.53568)
WALL_N, WALL_S = k6(1531, 850), k6(1520, 990)
F12 = k6(1430, 905)                    # fighting ground of days 1-2, just west of the wall (kv map 7 '1')
F3 = k6(1300, 935)                     # the broader ground of the day-3 sortie, by the baths (kv map 7 '2')
GCAMP = k6(1760, 730)
WEST_GATE, EAST_GATE = k6(240, 610), k6(2392, 505)
ANTH = k6(700, 700); MID = k6(1000, 840)
PCAMP = k5(1080, 760)
ASOPUS_X = k5(935, 835)                # the Asopus where the path begins (near Mustaphabey)
KALK, PALEO, QUELLE, NEVRO = k5(990, 1010), k5(995, 1163), k5(1170, 1225), k5(1283, 1276)
M1, M2, ALTDRAK, SADDLE, SUMMIT = k5(1450, 1240), k5(1560, 1160), k5(1590, 1095), k5(1655, 1040), k5(1613, 1022)
D1, D2, D3, D4, D5, UNTDRAK = k5(1727, 1050), k5(1809, 1027), k5(1882, 973), k5(1918, 909), k5(1936, 836), k5(2008, 780)
ALPENOI = k5(2005, 670)
KOL = "Kolonos (last stand)"

B.place("Trachis", k5(757, 742), size=0.7)
B.place("Anthela", "Anthele", size=0.5)
B.place("Alpenoi", ALPENOI, size=0.5)
B.hill(KOL, "Kolonos Hill")
B.hill("Phocian wall", WALL)
B.hill("Sastani saddle", SADDLE)
B.hill("Kallidromos", (38.745, 22.540))
B.roads = [["Trachis", (38.8005, 22.4400), (38.8030, 22.4700), (38.8030, 22.4880), WEST_GATE, ANTH, MID, (38.7940, 22.5280), (38.7950, 22.5330), WALL, (38.7966, 22.5390), GCAMP, (38.8028, 22.5500), EAST_GATE, (38.8043, 22.5690), (38.8040, 22.5850), (38.8070, 22.6050), (38.8105, 22.6200), (38.8130, 22.6290)]]
B.woods = [[38.7570, 22.4700, 1400, 700], [38.7560, 22.5110, 1300, 650], [38.7630, 22.5470, 900, 700], [38.7750, 22.5600, 600, 600]]
B.camps = [{"a": [38.7982, 22.5385], "b": [38.8003, 22.5450], "rows": 2, "until": 6},
           {"a": [38.8020, 22.4520], "b": [38.7970, 22.4730], "rows": 4, "until": 9}]

def U(uid, side, typ, name, strength, frontage, keys, note, conf, men, cite, via=None, blocks=None, code=None, lines=None):
    u = B.unit(uid, side, typ, name, strength, frontage, note=note, conf=conf, men=men, cite=cite, blocks=blocks, code=code, lines=lines)
    for phase, (pos, facing, form, *bend) in keys.items():
        u.at(phase, pos, facing, form, via=(via or {}).get(phase), bend=bend[0] if bend else 0)
    return u

W, E = 255, 75   # facing down the pass towards the Persians (west-south-west) and towards the Greeks

# ---- Greeks. Order of battle from Herodotus 7.202-203; helots and the Locrian figure as in brief.md.
U("spartans", "spa", "hi", "Spartans (Leonidas)", "300 hoplites", 70,
  {0: ((WALL, W, 70), W, "L"), 1: ((F12, E, 40), W, "F"), 2: (F12, W, "F"), 3: ((GCAMP, 255, 120), W, "X"), 7: ((WALL, W, 40), W, "L"),
   8: (F3, W, "F"), 9: ((KOL, 0, 10), W, "F")},
  "The 300, chosen from men who had sons. They were outside the wall when Xerxes' scout rode up, used feigned flights against the Immortals, and died in the sortie and on the kolonos; only Aristodemos and Pantites, who were away, survived [hdt].",
  "high", {0: 300, 2: 290, 3: 285, 8: 180, 9: 60}, ["hdt"], via={9: [WALL]}, code="A")
U("helots", "spa", "lt", "Helots and Lacedaemonian light troops", "about 900", 80,
  {0: ((GCAMP, 255, 60), W, "X"), 7: ((WALL, 75, 60), W, "C"), 8: ((F3, E, 110), W, "L"), 9: ((KOL, 180, 40), W, "F")},
  "Herodotus mentions helots among the dead and a helot leading the blind Eurytos to the fight. The 900 (three per Spartan) is a modern inference, and so is their presence at the end [hdt] [wp].",
  "low", {0: 900, 3: 890, 8: 700, 9: 200}, ["hdt", "wp"], via={9: [WALL]}, code="B")
U("thespians", "gre", "hi", "Thespians (Demophilos)", "700 hoplites", 90,
  {0: ((GCAMP, 75, 150), W, "X"), 1: ((WALL, 75, 60), W, "C"), 3: ((F12, E, 30), W, "F"), 4: ((GCAMP, 75, 150), W, "X"), 7: ((WALL, 75, 30), W, "L"),
   8: ((F3, 345, 60), W, "F"), 9: ((KOL, 90, 35), W, "F")},
  "The Thespians chose to stay with Leonidas on the last day and died with him; Dithyrambos was named the bravest of them [hdt].",
  "high", {0: 700, 3: 680, 8: 480, 9: 150}, ["hdt"], via={9: [WALL]}, code="C")
U("thebans", "gre", "hi", "Thebans (Leontiades)", "400 hoplites", 70,
  {0: ((GCAMP, 75, 260), W, "X"), 1: ((WALL, 75, 140), W, "C"), 7: ((WALL, 75, 80), W, "L"), 8: ((F3, 165, 50), W, "L"), 9: ((WALL, W, 35), W, "R")},
  "Herodotus says Leonidas kept them as hostages; they fought for a while on day 3, then broke away while the others made for the hillock and surrendered. Some were killed as they came over; the rest were branded [hdt].",
  "medium", {0: 400, 3: 390, 8: 340, 9: 0}, ["hdt", "diod"], code="D")
U("tegeans", "gre", "hi", "Tegeans", "500 hoplites", 80,
  {0: ((GCAMP, 75, 360), W, "X"), 2: ((F12, E, 70), W, "L"), 3: ((WALL, 75, 60), W, "C"), 4: ((GCAMP, 75, 360), W, "X"), 7: ((38.8020, 22.5520), E, "C"), 8: ((38.8070, 22.6000), E, "C")},
  "Arcadian contingent of 500 [hdt]. Which contingents stood in the line on day 1 is not recorded; this one is shown in support during the Immortals' attack. It was dismissed on day 3 [hdt].",
  "medium", {0: 500, 3: 480}, ["hdt"], code="E")
U("mantineans", "gre", "hi", "Mantineans", "500 hoplites", 80,
  {0: ((GCAMP, 75, 470), W, "X"), 2: ((WALL, 75, 40), W, "C"), 7: ((38.8030, 22.5575), E, "C"), 8: ((38.8085, 22.6080), E, "C")},
  "Arcadian contingent of 500 [hdt]; dismissed on day 3 [hdt].",
  "medium", {0: 500, 3: 480}, ["hdt"], code="F")
U("arcadians", "gre", "hi", "Orchomenians and other Arcadians", "1,120 hoplites", 110,
  {0: ((GCAMP, 75, 580), W, "X"), 3: ((F12, E, 60), W, "F"), 4: ((GCAMP, 75, 580), W, "X"), 7: ((38.8042, 22.5710), E, "C"), 8: ((38.8115, 22.6215), E, "C")},
  "120 from Orchomenos and 1,000 from the rest of Arcadia [hdt]. They are shown taking a turn in the line on day 2, when 'they fought successively each in turn' [hdt].",
  "medium", {0: 1120, 3: 1090}, ["hdt"], code="G")
U("corinthians", "gre", "hi", "Corinthians, Phliasians and Mycenaeans", "680 hoplites", 90,
  {0: ((GCAMP, 75, 700), W, "X"), 7: ((38.8040, 22.5635), E, "C"), 8: ((38.8100, 22.6150), E, "C")},
  "400 Corinthians, 200 from Phlius and 80 from Mycenae [hdt]; dismissed on day 3 [hdt].",
  "medium", {0: 680, 3: 665}, ["hdt"], code="H")
U("locrians", "gre", "hi", "Opuntian Locrians", "1,000 (Diodorus)", 110,
  {0: ((GCAMP, 75, 820), W, "X"), 7: ((38.8040, 22.5790), E, "C"), 8: ((38.8125, 22.6260), E, "C")},
  "Herodotus says they came 'in full force' without a number; Diodorus gives 1,000 and Pausanias up to 6,000. The lowest figure is shown [hdt] [diod] [paus].",
  "low", {0: 1000, 3: 980}, ["hdt", "diod", "paus"], code="I")
U("phocians", "gre", "hi", "Phocians on the mountain", "1,000 hoplites", 120,
  {0: (SADDLE, 225, "X"), 6: (SUMMIT, 135, "R"), 7: (SUMMIT, 135, "L")},
  "They volunteered to guard the Anopaea path. Surprised at dawn by the noise of the Persians in the oak leaves, and under arrows, they fell back to the peak expecting to be attacked; the Persians ignored them [hdt]. Their post on the Sastani saddle follows Kromayer [kv].",
  "low", {0: 1000, 6: 980}, ["hdt", "kv"], code="J")

# ---- Persians. Only the waves Herodotus names are separate; the rest of the army is a camp block.
U("medes", "per", "arc", "Medes", "about 10,000 (illustrative)", 80,
  {0: ((PCAMP, 270, 500), E, "X"), 1: ((F12, W, 130), E, "F"), 2: ((ANTH, 255, 300), W, "C"), 3: ((F12, W, 120), E, "F"), 4: ((PCAMP, 270, 500), E, "X")},
  "Sent first with the Cissians, with orders to take the Greeks alive; they lost heavily all day and came on again on day 2 [hdt]. Diodorus adds the kinsmen of the Marathon dead [diod]. Their strength is not recorded.",
  "medium", {0: 10000, 1: 7500, 3: 6000}, ["hdt", "diod"], via={1: [WEST_GATE, ANTH, MID], 4: [WEST_GATE]}, blocks=6, lines=2, code="1")
U("cissians", "per", "arc", "Cissians", "about 10,000 (illustrative)", 80,
  {0: ((PCAMP, 90, 500), E, "X"), 1: ((F12, W, 450), E, "C"), 2: ((ANTH, 255, 500), W, "C"), 3: ((F12, W, 420), E, "C"), 4: ((PCAMP, 90, 500), E, "X")},
  "Attacked alongside the Medes on day 1 [hdt]; Diodorus has them, with Sacae, relieving the Medes [diod]. Their strength is not recorded.",
  "medium", {0: 10000, 1: 8500, 3: 7000}, ["hdt", "diod"], via={1: [WEST_GATE, ANTH], 4: [WEST_GATE]}, blocks=6, lines=2, code="2")
U("immortals", "imm", "inf", "Immortals (Hydarnes), guided by Ephialtes", "10,000", 90,
  {0: ((PCAMP, 180, 350), E, "X"), 1: ((ANTH, 75, 150), E, "C"), 2: ((F12, W, 140), E, "F"), 3: ((PCAMP, 180, 350), E, "X"),
   4: (ASOPUS_X, 170, "C"), 5: (M1, 70, "C"), 6: (SADDLE, 60, "F"), 7: (D3, 30, "C"), 8: ((UNTDRAK, 345, 600), 0, "C"), 9: ((KOL, 75, 230), W, "F")},
  "Persia's royal guard, 10,000 strong by Herodotus's count. They failed against the wall on day 1. At lamp-lighting on day 2 they left with Ephialtes over the Anopaea path, reached the summit at dawn, brushed the Phocians aside and came down behind the Greeks [hdt]. The route is a reconstruction [kv] [standrews].",
  "medium", {0: 10000, 2: 8500, 9: 8000}, ["hdt", "kv", "standrews"],
  via={2: [ANTH, MID], 3: [MID, WEST_GATE], 5: [KALK, PALEO, QUELLE, NEVRO], 6: [M2, ALTDRAK], 7: [D1, D2], 8: [D4, D5, UNTDRAK], 9: [ALPENOI, EAST_GATE, GCAMP]}, blocks=6, lines=2, code="3")
U("assault", "per", "arc", "Xerxes' assault columns (day 3)", "about 20,000 (illustrative)", 110,
  {0: ((PCAMP, 0, 200), E, "X"), 7: ((ANTH, 255, 200), E, "C"), 8: ((F3, W, 110), E, "F"), 9: ((WALL, W, 70), E, "F")},
  "Sent in at 'the hour when the market fills', driven forward with whips; many were pushed into the sea or trampled. Two of Xerxes' brothers, Abrocomes and Hyperanthes, fell [hdt]. The strength is illustrative.",
  "medium", {0: 20000, 8: 12000, 9: 10000}, ["hdt"], via={7: [WEST_GATE], 8: [MID]}, blocks=8, lines=2, code="4")
U("pcamp", "per", "inf", "Persian main army in camp", "about 70,000 (illustrative)", 900,
  {0: ((PCAMP, 315, 400), E, "X")},
  "The rest of the army, including the cavalry, stayed on the Trachinian plain, where it could not be used in the pass [hdt] [kv]. Herodotus's millions are discarded; 120,000 in all is the low end of modern estimates [wp].",
  "low", {0: 70000}, ["hdt", "kv", "wp"], blocks=12, code="5")

B.commander("leonidas", "spa", "Leonidas", {0: WALL, 1: F12, 3: WALL, 8: F3}, "King of Sparta and commander of the whole force; he fell in the day-3 sortie, and the Spartans recovered his body after a struggle [hdt].")
B.commander("xerxes", "per", "Xerxes", {0: (PCAMP, 90, 150), 1: (ANTH, 200, 300), 4: (PCAMP, 90, 150), 8: (ANTH, 200, 300)}, "He watched from a seat and is said to have leapt up three times in fear for his army; on day 3 he poured libations at sunrise before the attack [hdt]. His viewpoint is not recorded and is placed illustratively.")
B.commander("hydarnes", "imm", "Hydarnes and Ephialtes", {0: (PCAMP, 180, 350), 4: ASOPUS_X, 5: M1, 6: SADDLE, 7: D3, 8: (UNTDRAK, 345, 600), 9: (KOL, 75, 250)}, "Hydarnes commanded the Immortals; Ephialtes son of Eurydemos, a Malian, guided them [hdt].")

ARR = B.arrow
tac = lambda n, b, i: (n, b, i)

B.phase("07:00", "Day 1, dawn", "Two armies at the gates",
  "On the fifth day after Xerxes reached Malis, the Greeks hold the Middle Gate behind the rebuilt Phocian wall [hdt]. In 480 the sea came almost to the cliffs at three points; at the wall only a narrow strip of ground lay between Kallidromos and the water [hdt] [kv] [kraft]. The Lacedaemonians are posted outside the wall [hdt]. A thousand Phocians guard the mountain path [hdt]. The Persian army is encamped on the Trachinian plain beyond the Asopus [hdt] [panel].",
  tac("Narrow front", "A small army chooses ground so narrow that the enemy can only bring as many men into contact as it has itself; numbers and cavalry stop counting.", "narrow-front"),
  (38.800, 22.505), 10.5,
  arrows=[], events=[(WALL, "The rebuilt Phocian wall at the Middle Gate [hdt]", ["hdt"]), ((38.8000, 22.5500), "The 480 BC shore: today this is dry land 3-5 km from the sea [kv] [stronk]", ["kv", "stronk"]),
          (SADDLE, "Phocians guard the Anopaea path on the mountain [hdt] [kv]", ["hdt", "kv"])],
  conf="medium", day=1, cite=["hdt", "kv", "panel"],
  debate="Herodotus's compass is turned through 90 degrees: his 'west' is the mountain (south) and his 'east' the sea (north) [stronk]. The wall is placed where Kromayer's 1:25,000 map draws it, 190 m south-west of Kolonos; OSM's excavated wall segment agrees [kv] [data].")
B.phase("10:00", "Medes attack", "The Medes and Cissians come on",
  "Angry that the Greeks have not fled, Xerxes sends in the Medes and Cissians with orders to bring them alive. They lose heavily all day without breaking the line; fresh men keep coming up [hdt]. Diodorus says the Greek shields and close ranks beat the Persians' light wicker shields in the narrows [diod].",
  tac("Narrow front", "In the narrows only the front ranks fight; the Persian advantage in numbers counts for almost nothing.", "narrow-front"),
  F12, 2.4,
  arrows=[ARR("per", "move", ANTH, MID, (F12, W, 160)), ARR("spa", "charge", (F12, E, 40), (F12, W, 110))],
  events=[(F12, "The Medes lose heavily in front of the wall [hdt]", ["hdt"])], conf="medium", day=1, cite=["hdt", "diod", "kv"],
  debate="The time is illustrative: Herodotus says only that the combat 'went on throughout the day' [hdt]. Diodorus adds Sacae to the second wave [diod].")
B.phase("16:00", "The Immortals", "Feigned flights",
  "When the Medes are worn out, Hydarnes' Immortals take their place and fare no better: their spears are shorter and they cannot use their numbers. The Spartans turn their backs as if in flight, wait for the Persians to rush after them in disorder, then face about and cut them down. Xerxes is said to have leapt from his seat three times [hdt].",
  tac("Feigned retreat", "Drilled troops turned and pretended to run; when the pursuers broke ranks, they faced about and struck.", "feigned-retreat"),
  F12, 2.4,
  arrows=[ARR("imm", "charge", MID, (F12, W, 150)), ARR("spa", "retreat", F12, (F12, E, 60)), ARR("per", "retreat", (F12, W, 200), ANTH)],
  events=[(F12, "Spartan feigned flights [hdt]", ["hdt"]), ((ANTH, 200, 300), "Xerxes leaps from his seat [hdt]", ["hdt"])], conf="medium", day=1, cite=["hdt", "diod"])
B.phase("10:00", "Day 2", "The contingents take turns",
  "The next day the Persians attack again, hoping the few defenders are exhausted. The Greeks are drawn up by companies and nations and fight in turn, all except the Phocians, who are on the mountain [hdt]. Diodorus has picked men from every nation sent in, with whips at their backs [diod].",
  tac("Rally and re-form", "Rotating fresh units into a narrow front keeps the line strong while tired men rest behind the wall.", "rally-reform"),
  F12, 2.4,
  arrows=[ARR("per", "move", ANTH, MID, (F12, W, 150))],
  events=[(F12, "Contingents relieve each other in the line [hdt]", ["hdt"])], conf="medium", day=2, cite=["hdt", "diod"],
  debate="Herodotus does not say which contingents fought when; the Thespians and Arcadians are shown in the line only to illustrate the rotation [hdt].")
B.phase("20:00", "Lamp-lighting", "Ephialtes leads Hydarnes out",
  "Ephialtes, a Malian, tells Xerxes about the path over the mountain. 'About the time when the lamps are lit' Hydarnes leaves the camp with his men. The path begins at the Asopus, where it flows out of its gorge; it is called the Anopaea, like the mountain [hdt]. Herodotus says the Malians had once led the Thessalians against the Phocians by it [hdt]. Diodorus says 20,000 men went [diod].",
  tac("Turning movement", "A force marches round the enemy's flank by a route he thinks too hard or too little known, to arrive in his rear.", "turning-movement"),
  ASOPUS_X, 6.0,
  arrows=[ARR("imm", "move", (PCAMP, 180, 350), ASOPUS_X)],
  events=[(ASOPUS_X, "The Persians cross the Asopus; the Anopaea begins [hdt]", ["hdt"])], conf="medium", day=2, cite=["hdt", "diod"])
B.phase("01:00", "Night march", "Through the oak woods in the dark",
  "The column climbs all night, with the Oetaean mountains on its right and the Trachinian on its left [hdt]. In the Greek camp the seer Megistias reads death at dawn in the sacrifices, and deserters come in before daylight with the news that the Persians are going round [hdt]. Diodorus names one, Tyrrhastiadas of Cyme [diod].",
  tac("Turning movement", "A night march over a mountain path is slow and blind; everything depends on the guide.", "turning-movement"),
  NEVRO, 9.0,
  arrows=[ARR("imm", "move", ASOPUS_X, KALK, PALEO, QUELLE, NEVRO, M1)],
  events=[(NEVRO, "The upper Asopus meadows (Nevropoli) [standrews]", ["standrews"]), (GCAMP, "Megistias and deserters warn the Greeks [hdt]", ["hdt"])],
  conf="low", day=3, cite=["hdt", "diod", "standrews", "kv"],
  debate="Herodotus fixes only the ends: from the Asopus to Alpenos [hdt]. This route goes up past the Kalkomata spring and Paleo-Eleftherochori and along the upper Asopus meadows, where most modern topographers put it (Gordon's line on Kromayer's map; Wallace 1980; Pritchett) [kv] [standrews]. Kromayer's own route is shorter: Alt-Damasta, along the north side of Lithitza, to Alt-Drakospilia. Leake and Grundy go by the Panagia monastery [kv]. Pausanias says Hydarnes used the easier of two paths, 'through the territory of the Aenianians' [paus]. The route shown is about 18 km; a column could cover it at about 2 km/h in a summer night.")
B.phase("05:45", "Dawn on the summit", "The Phocians hear the leaves",
  "At dawn the Persians reach the top. The air is still and the ground deep in oak leaves, so the Phocians hear them coming and snatch up their arms. Hydarnes fears they are Spartans until Ephialtes tells him otherwise. Under a shower of arrows the Phocians fall back to the summit to make a stand, but the Persians ignore them and hurry down the mountain [hdt]. Day-watchers run down to the Greeks with the news [hdt].",
  tac("Exposed outpost", "A detachment guarding a remote approach is surprised and stands aside; once the outpost has failed, the main position is turned.", "exposed-outpost"),
  SADDLE, 4.0,
  arrows=[ARR("imm", "fire", (SADDLE, 225, 150), SUMMIT), ARR("gre", "retreat", SADDLE, SUMMIT), ARR("imm", "move", SADDLE, D1, D2)],
  events=[(SADDLE, "Phocians surprised on the Sastani saddle [hdt] [kv]", ["hdt", "kv"]), (SUMMIT, "The Phocians make for the peak [hdt]", ["hdt"])],
  conf="low", day=3, cite=["hdt", "kv"],
  debate="The Phocian post is placed on the Sastani saddle, following Kromayer, who sends every route but Munro's over it [kv]. Others put the encounter on the height north-east of the Nevropoli lake [standrews].")
B.phase("07:00", "Dismissal", "Leonidas sends the allies away",
  "A council divides the Greeks. Most march off to their cities; Herodotus thinks Leonidas sent them away himself to save them, keeping the Spartans, the Thespians (who refused to go) and the Thebans (held as hostages) [hdt]. Leonidas also tries to send away Megistias, who stays and sends his son instead [hdt]. Xerxes pours libations at sunrise and waits, as Ephialtes advises [hdt].",
  tac("Rearguard", "A force sacrifices itself to hold the enemy while the rest of the army gets away.", "rearguard"),
  (38.8010, 22.5500), 6.5,
  arrows=[ARR("gre", "move", (GCAMP, 75, 300), EAST_GATE, (38.8045, 22.5780), (38.8070, 22.6000)), ARR("imm", "move", D2, D3, D4)],
  events=[(GCAMP, "Council: the allies go, the Thespians and Thebans stay [hdt]", ["hdt"]), (D3, "Hydarnes descends the Alpenoi ravine [kv]", ["kv"])],
  conf="medium", day=3, cite=["hdt", "diod", "kv"],
  debate="Diodorus has the council at midnight, keeps only the Lacedaemonians and Thespians (about 500), and sends them on a night attack on Xerxes' tent [diod]. That version is rejected here, as by most modern writers, in favour of Herodotus [stronk]. Which road the allies took is not recorded; the coast road east past Alpenoi, before the Immortals reached it, is assumed.")
B.phase("10:00", "The last sortie", "Into the broader part of the pass",
  "At 'the hour when the market fills' Xerxes advances. Knowing they are to die, the Greeks go out much further than before into the broader part of the pass. Many Persians, driven on by officers with whips, are pushed into the sea or trampled. With most of their spears broken, the Greeks fight with swords. Leonidas falls, and so do Abrocomes and Hyperanthes, brothers of Xerxes. The Greeks drive the enemy back four times and recover the king's body [hdt].",
  tac("Frontal assault", "A huge force pushed head-on into a narrow front pays heavily for every metre.", "frontal-assault"),
  F3, 2.6,
  arrows=[ARR("per", "charge", MID, (F3, W, 130)), ARR("spa", "charge", (WALL, W, 40), F3), ARR("imm", "move", (UNTDRAK, 345, 600), ALPENOI, EAST_GATE)],
  events=[(F3, "Leonidas falls; four rallies over his body [hdt]", ["hdt"]), ((38.7962, 22.5250), "Persians driven into the sea [hdt]", ["hdt"])],
  conf="medium", day=3, cite=["hdt", "kv", "museum"],
  debate="Kromayer's map 7 and the Thermopylae museum both put this fight west of the narrows, near the old baths [kv] [museum]. Diodorus's night raid on the royal tent is a different, later tradition [diod] [stronk].")
B.phase("11:00", "The kolonos", "The last stand",
  "When word comes that Hydarnes is behind them, the survivors fall back past the wall to the hillock in the entrance to the pass, 'where the stone lion now stands for Leonidas'. The Thebans break away and surrender. On the hillock the rest fight with daggers, hands and teeth until they are buried under missiles; some Persians break down the wall in front while others close in from all sides [hdt]. Marinatos's 1939 excavation found masses of arrowheads on Kolonos [wp].",
  tac("Last stand", "Cut off front and rear, the remnant takes the strongest ground left and fights until overwhelmed.", "last-stand"),
  "Kolonos Hill", 1.9,
  arrows=[ARR("imm", "charge", (KOL, 75, 300), (KOL, 75, 60)), ARR("per", "charge", (WALL, W, 120), (KOL, 230, 60)), ARR("spa", "retreat", F3, WALL, (KOL, 230, 20))],
  events=[("Kolonos Hill", "The last stand on Kolonos [hdt] [wp]", ["hdt", "wp"]), ((WALL, W, 40), "The Thebans surrender [hdt]", ["hdt"])],
  conf="medium", day=3, cite=["hdt", "wp", "grundy", "kv"],
  debate="The hillock is identified with Kolonos, where Marinatos found the arrowheads [wp]. Kromayer labels a hill farther east as the Leonidashügel but writes that the end came 'probably on hill 2', which matches Kolonos; Grundy says the 'second mound' [kv] [grundy]. Herodotus gives 20,000 Persian dead and 4,000 Greek bodies, including helots; most modern writers accept roughly 2,000 Greek dead [hdt] [wp].")

B.export()
