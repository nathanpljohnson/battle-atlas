"""Thermopylae, 480 BC (three days of fighting, late summer).

Herodotus 7.175-233 is the framework; Diodorus 11.4-11 is the counter-account. The 480 BC coastline
comes from the Kromayer-Veith 1:25,000 and 1:100,000 maps, georeferenced to OSM's Phocian wall, Kolonos
and old baths (25 m) and to seven villages (173 m), pulled in at the Middle Gate to Kraft et al.'s
20-30 m pass. The Anopaea route and Phocian post follow Pritchett/MacKay/Wallace (see brief.md). Clock times other than lamp-lighting, dawn and 'the hour the market fills'
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
B.source("kv", "J. Kromayer and G. Veith, Schlachten-Atlas zur antiken Kriegsgeschichte, Griech. Abt. Blatt 1, maps 5-7 and text (Leipzig, 1922-29), after L. and E. Harmening in Antike Schlachtfelder IV", "https://archive.org/details/kromayerveithschlachtenatlas", "German staff-quality maps built on Grundy's survey and the Carte de la Grèce: the 480 BC shore, the West, Middle and East Gates, the Phocian wall, the camps, Kromayer's Phocian post on the Sastani saddle and five path hypotheses; georeferenced (map 6: 25 m; map 5: 173 m). German text translated in sources/NOTES.md", "staff-map")
B.source("grundy", "G. B. Grundy, The Great Persian War and its Preliminaries (London, 1901), ch. on Thermopylae", "https://archive.org/details/greatpersianwari00grunuoft", "field survey: the 480 BC shore at about the 5-10 yard contour; the mounds at the Middle Gate; the last stand on the 'second mound'", "scholarly")
B.source("stronk", "J. P. Stronk, 'Thermopylae 480 BC: ancient accounts of a battle', Talanta 46-47 (2014-15) 165-236", "https://www.talanta.nl/wp-content/uploads/2017/08/Stronk.pdf", "modern comparison of all the ancient accounts: the strengths table, the coast 1-8 km further out today, the unsettled Anopaea route, the date in August or September", "scholarly")
B.source("kraft", "J. C. Kraft, G. Rapp, G. J. Szemler, C. Tziavos and E. W. Kase, 'The Pass at Thermopylae, Greece', Journal of Field Archaeology 14 (1987) 181-198; redrawn after Rapp and Hill, Geoarchaeology (2006) fig. 3.19", "https://commons.wikimedia.org/wiki/File:Thermopylae_shoreline_changes_map.png", "geoarchaeology from boreholes: the 480 BC shoreline close under the cliffs and the pass some tens of metres wide. Consulted through the redrawn figure and summaries, not the article itself", "scholarly")
B.source("panel", "Thermopylae monument, site panel 'The area of Thermopyles and the Greek and Persian camps before the battle' (photo D. Mauro, 2018)", "https://commons.wikimedia.org/wiki/File:Maps_of_Thermopylae_01.jpg", "on-site Greek/English map: probable 480 BC coast, the Persian camp between the Melas and the Asopus, the gates, the Greek camp, the Anopaia path", "staff-map")
B.source("museum", "Thermopylae Battle Museum panel 'The Battle of Thermopyles (480 B.C.)' (photo D. Mauro, 2018)", "https://commons.wikimedia.org/wiki/File:Map_of_the_Battle_of_Thermopylae.jpg", "days 1-2 in front of the wall, the day 3 sortie further west, the end on Kolonos, the Anopaia path", "staff-map")
B.source("standrews", "'Kallidromos', Mountains of Greece blog (University of St Andrews, 2025), summarising P. W. Wallace, AJA 84 (1980) 15-23 and W. K. Pritchett", "https://mountainsofgreece.wp.st-andrews.ac.uk/2025/12/13/kallidromos/", "near-consensus that the middle of the path ran through the upper Asopus meadows from Eleftherochori to Nevropoli", "reference")
B.source("wp", "Wikipedia, 'Battle of Thermopylae' (after Lazenby 1993, Green 1996, Holland 2005, Cartledge 2006) and 'Kolonos Hill'", "https://en.wikipedia.org/wiki/Battle_of_Thermopylae", "modern estimates of the Persian army (most between 120,000 and 300,000, a few lower) and the Greek dead", "reference")
B.source("isoc", "Isocrates, Panegyricus 90, tr. G. Norlin (Loeb, 1928)", "https://cts.perseids.org/read/greekLit/tlg0010/tlg011/perseus-eng2/82-90", "the Lacedaemonians went to Thermopylae 'with a thousand picked soldiers of their own, supported by a few of their allies'", "primary")
B.source("rop", "J. Rop, 'The Phocian Betrayal at Thermopylae', Historia 68 (2019) 413-435", "https://conservancy.umn.edu/items/a0255c6c-681f-4201-84e1-21c544728752", "the Phocian post on the hill near Nevropolis (Pritchett 1958 and 1982, MacKay 1963, Wallace 1980); the Persians probably knew of the path on arrival; the Phocians may have stood aside deliberately; most scholars date the battle to August (Sacks and Hammond: mid-September)", "scholarly")
B.source("reed", "Reed College Humanities 110, 'Thermopylae' (archived 2020)", "https://web.archive.org/web/20201127012143/https://www.reed.edu/humanities/110Tech/Thermopylae.html", "teaching summary: Kraft et al. 1987 put the pass at no more than 20-30 m wide; Kolonos is the second hill (Marinatos); the Vardates (Wallace, Burn) and Kalkomata (Pritchett) ascents", "reference")
B.source("brown", "A. R. Brown, 'Remembering Thermopylae and the Persian Wars in Antiquity', in C. Matthew and M. Trundle (eds.), Beyond the Gates of Fire (2013), as summarised by S. Manning", "https://scottmanning.com/content/these-weapons-killed-leonidas/", "Marinatos's 1939 finds on Kolonos: about 100 bronze and iron arrowheads and a few spearheads, probably but not certainly Persian", "reference")
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
        "start": [{"label": "Greeks", "n": 8100, "segs": [["spa", 0.272], ["gre", 0.728]]},
                  {"label": "Persians", "n": 120000, "segs": [["per", 0.917], ["imm", 0.083]]}],
        "end": [{"label": "Greeks", "n": 5660, "segs": [["spa", 0.174], ["gre", 0.826]]},
                {"label": "Persians", "n": 100000, "segs": [["per", 0.93], ["imm", 0.07]]}],
    },
    "sun": {"lat": 38.80, "decl": 12.5, "note": "Herodotus ties the campaign to the Carneia and the Olympic games. Most scholars date the battle to August 480 BC; Sacks and Hammond argue for mid-September [rop] [stronk]. The sun is set for about 20 August: first light about 04:50, sunrise about 05:20 local solar time. Herodotus's own times: Hydarnes leaves 'about lamp-lighting', reaches the summit at dawn, and Xerxes attacks at 'the hour when the market fills' [hdt]."},
    "wind": 45, "view": {"az": 0.0, "el": 0.95}, "unitScale": 0.7, "unitLabelDist": 6,
    "ground": {"season": "summer", "relief": 160},
    "days": ["Day 1", "Day 2", "Day 3"],
    "strengthNote": "Greeks: Herodotus's list (5,200 with 1,000 Phocians), plus the 1,000 Lacedaemonians of Diodorus and Isocrates (usually read as perioikoi), 900 helots and 1,000 Opuntian Locrians = 8,100. Diodorus gives about 7,400 (with 1,000 Malians, not shown); Pausanias up to 11,200 [hdt] [diod] [isoc] [paus]. Persians: Herodotus's millions are impossible; 120,000 is a commonly cited modern figure in a range that runs from under 100,000 to about 300,000 [wp] [kv]. The Medes' and Cissians' myriads (10,000 each) and the 20,000 sent in on day 3 are illustrative; only the Immortals' 10,000 is a source figure [hdt]. Losses follow Herodotus's 20,000 Persian dead and the modern figure of about 2,000 Greek dead [hdt] [wp]; how they are spread across the moments is an estimate. On day 3 the dismissed allies (about 4,700 with the Lacedaemonians) and the Phocians (about 1,000) leave or stand aside; the Thebans (about 340 left) surrender.",
    "method": "The 480 BC shoreline and the pass come from the Kromayer-Veith maps of 1922-29, which rest on Grundy's 1899 survey and the French staff survey. They are georeferenced to OSM's Phocian wall, Kolonos and old baths (map 6, 25 m) and to seven villages (map 5, 173 m) [kv] [data]. The vanished water is drawn over today's Spercheios plain, and the ground inside it is lowered to sea level. At the Middle Gate the shore is pulled in to 40-60 m from the cliff foot to follow the borehole study (pass 20-30 m wide), and the floor of the pass is lowered from today's 20-35 m of later travertine and alluvium to a schematic 6 m [kraft] [reed] [stronk]. Elsewhere the line agrees with Grundy's 5-10 yard contour [grundy]. Unit positions follow Herodotus's sequence on that ground [hdt]. The Anopaea route and the Phocian post follow the majority modern view (Pritchett, MacKay, Wallace), and are low confidence [rop] [standrews] [kv].",
    "notes": "The pass at the Middle Gate was some 15-30 m wide in 480 [hdt] [kraft]; at this map's 43 m grid the narrowest stretch shows as a strip about 50 m wide, and the units' frontages are drawn wider than the files would have been. The wall stood where the strip opened out round Kolonos. Today's shore lies 1-8 km further north [stronk]. The Anopaea route shown runs up from the Asopus by the Kalkomata spring (Pritchett's ascent; Wallace preferred Vardates) to the Phocian post by Nevropoli, then east by Drakospilia, over the Sastani saddle and down the Alpenoi ravine. Kromayer's shorter line via Alt-Damasta, with the Phocians on the Sastani saddle, is described in the debate notes. Diodorus's night attack on Xerxes' tent is not shown. The oak woods on Kallidromos are drawn schematically from Herodotus's 'all the mountain was covered with oak-trees'. Phocian and Locrian contingent positions in camp are illustrative. No historical-map overlay is offered.",
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
                     "Asopus": k5(1130, 800), "Melas": k5(870, 500), "Hot springs (Chytroi)": (38.7934, 22.5292)}

WALL = (38.7953, 22.5357)              # across the strip from the cliff foot (OSM 'Teichos Phokeon' 38.79445, 22.53568) to the 480 BC shore
F12 = (38.7942, 22.5320)               # days 1-2: in the narrows just west of the wall (kv map 7 '1'; strip about 50 m wide here)
F3 = (38.7948, 22.5245)                # day 3: the broader ground west of the narrows (kv map 7 '2'; hdt 7.223)
GCAMP = k6(1760, 730)
WEST_GATE, EAST_GATE = k6(240, 610), k6(2392, 505)
ANTH = k6(700, 700); MID = k6(1000, 840)
PCAMP = k5(1080, 760)
ASOPUS_X = k5(935, 835)                # the Asopus where the path begins (near Mustaphabey)
KALK, PALEO, QUELLE, NEVRO = k5(990, 1010), k5(995, 1163), k5(1170, 1225), k5(1283, 1276)
POST = "Phocian post (hill by Nevropoli)"   # DEM 1,125 m, 550 m NE of the lake (Pritchett, MacKay, Wallace via Rop n. 26)
PEAK = (38.7390, 22.5134)              # nearest higher summit (DEM 1,301 m), off the Persian line of march
M2, ALTDRAK, SADDLE = k5(1560, 1160), k5(1590, 1095), k5(1655, 1040)
NIGHT = (38.7595, 22.4570)             # 01:00, about halfway up, past Paleo-Eleftherochori
PLATEAU = (38.7560, 22.5110)
D1, D2, D3, D4, D5, UNTDRAK = k5(1727, 1050), k5(1809, 1027), k5(1882, 973), k5(1918, 909), k5(1936, 836), k5(2008, 780)
ALPENOI = k5(2005, 670)
KOL = "Kolonos (last stand)"

B.place("Trachis", k5(757, 742), size=0.7)
B.place("Anthela", "Anthele", size=0.5)
B.place("Alpenoi", ALPENOI, size=0.5)
B.hill(KOL, "Kolonos Hill")
B.hill("Phocian wall", WALL)
B.hill("Sastani saddle", SADDLE)
B.hill(POST, (38.7536, 22.4988))
B.hill("Nevropoli meadows", NEVRO)
B.hill("Kallidromos", (38.745, 22.540))
B.roads = [["Trachis", (38.8005, 22.4400), (38.8030, 22.4700), (38.8030, 22.4880), WEST_GATE, ANTH, MID, (38.7945, 22.5250), (38.7937, 22.5285), (38.7940, 22.5310), (38.7946, 22.5335), WALL, (38.7962, 22.5390), GCAMP, (38.8028, 22.5500), EAST_GATE, (38.8043, 22.5690), (38.8040, 22.5850), (38.8070, 22.6050), (38.8105, 22.6200), (38.8130, 22.6290)]]
B.woods = [[38.7570, 22.4700, 1400, 700], [38.7560, 22.5110, 1300, 650], [38.7630, 22.5470, 900, 700], [38.7750, 22.5600, 600, 600]]
B.camps = [{"a": [38.7982, 22.5385], "b": [38.8003, 22.5450], "rows": 2, "until": 6},
           {"a": [38.8020, 22.4520], "b": [38.7970, 22.4730], "rows": 4, "until": 9}]

def U(uid, side, typ, name, strength, frontage, keys, note, conf, men, cite, via=None, blocks=None, code=None, lines=None):
    u = B.unit(uid, side, typ, name, strength, frontage, note=note, conf=conf, men=men, cite=cite, blocks=blocks, code=code, lines=lines)
    for phase, (pos, facing, form, *bend) in keys.items():
        u.at(phase, pos, facing, form, via=(via or {}).get(phase), bend=bend[0] if bend else 0)
    return u

W, E = 250, 70   # facing down the pass towards the Persians (west-south-west) and towards the Greeks

# ---- Greeks. Order of battle from Herodotus 7.202-203; helots and the Locrian figure as in brief.md.
U("spartans", "spa", "hi", "Spartans (Leonidas)", "300 hoplites", 50,
  {0: ((WALL, W, 70), W, "L"), 1: ((F12, E, 40), W, "F"), 2: (F12, W, "F"), 3: ((GCAMP, 255, 120), W, "X"), 7: ((WALL, W, 40), W, "L"),
   8: (F3, W, "F"), 9: ((KOL, 0, 10), W, "F")},
  "The 300, chosen from men who had sons. During the wait they happened to be outside the wall when Xerxes' scout rode up; used feigned flights against the Immortals, and died in the sortie and on the kolonos; only Aristodemos and Pantites, who were away, survived [hdt].",
  "high", {0: 300, 2: 290, 3: 285, 8: 180, 9: 60}, ["hdt"], via={9: [WALL]}, code="A")
U("lacedaemonians", "spa", "hi", "Lacedaemonians (perioikoi?)", "1,000 (Diodorus, Isocrates)", 80,
  {0: ((GCAMP, 75, 40), W, "X"), 2: ((WALL, 70, 40), W, "C"), 7: ((38.8040, 22.5850), E, "C"), 8: ((38.8132, 22.6280), E, "C")},
  "Diodorus has 1,000 Lacedaemonians besides the 300 Spartiates, and Isocrates 'a thousand picked soldiers of their own'; most moderns read them as perioikoi, which also squares Herodotus's 3,100 Peloponnesians with the epigram's 4,000. Herodotus does not mention them. Shown leaving with the allies on day 3; whether they stayed is unknown [diod] [isoc] [hdt].",
  "low", {0: 1000, 3: 985}, ["diod", "isoc", "hdt"], code="K")
U("helots", "spa", "lt", "Helots", "about 900", 50,
  {0: ((GCAMP, 255, 60), W, "X"), 7: ((WALL, 75, 60), W, "C"), 8: ((F3, E, 110), W, "L"), 9: ((KOL, 180, 40), W, "F")},
  "Herodotus mentions helots among the dead (8.25) and a helot leading the blind Eurytos to the fight. The 900 (three per Spartan) is a modern inference, and so is their presence at the end [hdt] [wp].",
  "low", {0: 900, 3: 890, 8: 700, 9: 200}, ["hdt", "wp"], via={9: [WALL]}, code="B")
U("thespians", "gre", "hi", "Thespians (Demophilos)", "700 hoplites", 60,
  {0: ((GCAMP, 75, 150), W, "X"), 1: ((WALL, 75, 60), W, "C"), 3: ((F12, E, 30), W, "F"), 4: ((GCAMP, 75, 150), W, "X"), 7: ((WALL, 75, 30), W, "L"),
   8: ((F3, 345, 60), W, "F"), 9: ((KOL, 90, 35), W, "F")},
  "The Thespians chose to stay with Leonidas on the last day and died with him; Dithyrambos was named the bravest of them [hdt].",
  "high", {0: 700, 3: 680, 8: 480, 9: 150}, ["hdt"], via={9: [WALL]}, code="C")
U("thebans", "gre", "hi", "Thebans (Leontiades)", "400 hoplites", 50,
  {0: ((GCAMP, 75, 260), W, "X"), 1: ((WALL, 75, 140), W, "C"), 7: ((WALL, 75, 80), W, "L"), 8: ((F3, 165, 50), W, "L"), 9: ((WALL, W, 35), W, "R")},
  "Herodotus says Leonidas kept them as hostages; they fought for a while on day 3, then broke away while the others made for the hillock and surrendered. Some were killed as they came over; the rest were branded [hdt].",
  "medium", {0: 400, 3: 390, 8: 340, 9: 0}, ["hdt", "diod"], code="D")
U("tegeans", "gre", "hi", "Tegeans", "500 hoplites", 50,
  {0: ((GCAMP, 75, 360), W, "X"), 2: ((F12, E, 70), W, "L"), 3: ((WALL, 75, 60), W, "C"), 4: ((GCAMP, 75, 360), W, "X"), 7: ((38.8020, 22.5520), E, "C"), 8: ((38.8070, 22.6000), E, "C")},
  "Arcadian contingent of 500 [hdt]. Which contingents stood in the line on day 1 is not recorded; this one is shown in support during the Immortals' attack. It was dismissed on day 3 [hdt].",
  "medium", {0: 500, 3: 480}, ["hdt"], code="E")
U("mantineans", "gre", "hi", "Mantineans", "500 hoplites", 80,
  {0: ((GCAMP, 75, 470), W, "X"), 2: ((WALL, 75, 40), W, "C"), 7: ((38.8030, 22.5575), E, "C"), 8: ((38.8085, 22.6080), E, "C")},
  "Arcadian contingent of 500 [hdt]; dismissed on day 3 [hdt].",
  "medium", {0: 500, 3: 480}, ["hdt"], code="F")
U("arcadians", "gre", "hi", "Orchomenians and other Arcadians", "1,120 hoplites", 50,
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
  {0: (POST, 250, "X"), 6: ((POST, 140, 900), 140, "R"), 7: (PEAK, 320, "L")},
  "They volunteered to guard the Anopaea path. Surprised at dawn by the noise of the Persians in the oak leaves, and under arrows, they fell back to the peak expecting to be attacked; the Persians ignored them [hdt]. The post on the hill by Nevropoli is the majority modern placement (Pritchett, MacKay, Wallace) [rop]; Kromayer put it on the Sastani saddle [kv]. Rop argues they stood aside deliberately [rop].",
  "low", {0: 1000, 6: 980}, ["hdt", "rop", "kv"], code="J")

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
   4: (ASOPUS_X, 170, "C"), 5: (NIGHT, 110, "C"), 6: ((POST, 250, 350), 70, "F"), 7: (ALTDRAK, 45, "C"), 8: ((38.8000, 22.5780), 270, "C"), 9: ((KOL, 70, 230), W, "F")},
  "Persia's royal guard, 10,000 strong by Herodotus's count. They failed against the wall on day 1. At lamp-lighting on day 2 they left with Ephialtes over the Anopaea path, reached the summit at dawn, brushed the Phocians aside and came down behind the Greeks [hdt]. Positions in the pass are medium confidence; the mountain route (phases 4-8) is low [rop] [kv] [standrews].",
  "low", {0: 10000, 2: 8500, 9: 8000}, ["hdt", "rop", "kv", "standrews"],
  via={2: [ANTH, MID], 3: [MID, WEST_GATE], 5: [KALK, PALEO], 6: [QUELLE, NEVRO], 7: [PLATEAU, M2], 8: [SADDLE, D1, D2, D3, D4, D5, UNTDRAK], 9: [EAST_GATE, GCAMP]}, blocks=6, lines=2, code="3")
U("assault", "per", "arc", "Xerxes' assault columns (day 3)", "about 20,000 (illustrative)", 110,
  {0: ((PCAMP, 0, 200), E, "X"), 7: ((ANTH, 255, 200), E, "C"), 8: ((F3, W, 110), E, "F"), 9: ((WALL, W, 70), E, "F")},
  "Sent in at 'the hour when the market fills', driven forward by officers with whips; many were pushed into the sea or trampled. Two of Xerxes' brothers, Abrocomes and Hyperanthes, fell [hdt]. The strength is illustrative.",
  "medium", {0: 20000, 8: 12000, 9: 10000}, ["hdt"], via={7: [WEST_GATE], 8: [MID]}, blocks=8, lines=2, code="4")
U("pcamp", "per", "inf", "Persian main army in camp", "about 70,000 (illustrative)", 900,
  {0: ((PCAMP, 315, 400), E, "X")},
  "The rest of the army, including the cavalry, stayed on the Trachinian plain, where it could not be used in the pass [hdt] [kv]. Herodotus's millions are discarded; 120,000 in all is a commonly cited modern figure [wp].",
  "low", {0: 70000}, ["hdt", "kv", "wp"], blocks=12, code="5")

B.commander("leonidas", "spa", "Leonidas", {0: WALL, 1: F12, 3: WALL, 8: F3}, "King of Sparta and commander of the whole force; he fell in the day-3 sortie, and the Spartans recovered his body after a struggle [hdt].")
B.commander("xerxes", "per", "Xerxes", {0: (PCAMP, 90, 150), 1: (ANTH, 200, 300), 4: (PCAMP, 90, 150), 8: (ANTH, 200, 300)}, "He watched from a seat and is said to have leapt up three times in fear for his army; on day 3 he poured libations at sunrise before the attack [hdt]. His viewpoint is not recorded and is placed illustratively.")
B.commander("hydarnes", "imm", "Hydarnes and Ephialtes", {0: (PCAMP, 180, 350), 4: ASOPUS_X, 5: NIGHT, 6: (POST, 250, 420), 7: ALTDRAK, 8: (38.8005, 22.5790), 9: (KOL, 70, 260)}, "Hydarnes commanded the Immortals; Ephialtes son of Eurydemos, a Malian, guided them [hdt].")

ARR = B.arrow
tac = lambda n, b, i: (n, b, i)

B.phase("07:00", "Day 1, morning", "Two armies at the gates",
  "On the fifth day after Xerxes reached Malis, the Greeks hold the Middle Gate behind the rebuilt Phocian wall [hdt]. In 480 the sea came almost to the cliffs at three points; just west of the wall the strip between Kallidromos and the water was only some 20-30 m wide [hdt] [kv] [kraft]. During the four days of waiting, Xerxes' scout had found the Lacedaemonians posted outside the wall [hdt]. A thousand Phocians guard the mountain path [hdt]. The Persian army is encamped on the Trachinian plain beyond the Asopus [hdt] [panel].",
  tac("Narrow front", "A small army chooses ground so narrow that the enemy can only bring as many men into contact as it has itself; numbers and cavalry stop counting.", "narrow-front"),
  (38.800, 22.505), 10.5,
  arrows=[], events=[(WALL, "The rebuilt Phocian wall at the Middle Gate [hdt]", ["hdt"]), ((38.8000, 22.5500), "The 480 BC shore: today this is dry land 3-5 km from the sea [kv] [stronk]", ["kv", "stronk"]),
          (POST, "Phocians guard the Anopaea path on the mountain [hdt] [rop]", ["hdt", "rop"])],
  conf="medium", day=1, cite=["hdt", "kv", "kraft", "panel"],
  debate="Herodotus's compass is turned through 90 degrees: his 'west' is the mountain (south) and his 'east' the sea (north) [stronk]. Kromayer's 10 m line gives a strip 100-200 m wide here; the borehole study puts it at 20-30 m, and Pritchett thought even that too wide [kv] [reed]. The map follows the borehole figure for the narrows west of the wall and keeps Kolonos on the shore [kraft] [reed].")
B.phase("10:00", "Medes attack", "The Medes and Cissians come on",
  "Angry that the Greeks have not fled, Xerxes sends in the Medes and Cissians with orders to bring them alive. They lose heavily all day without breaking the line; fresh men keep coming up [hdt]. Diodorus says the long Greek shields and close ranks beat the Persians' 'small round or irregularly shaped shields' in the narrows [diod].",
  tac("Narrow front", "In the narrows only the front ranks fight; the Persian advantage in numbers counts for almost nothing.", "narrow-front"),
  F12, 2.0,
  arrows=[ARR("per", "move", ANTH, MID, (F12, W, 160)), ARR("spa", "charge", (F12, E, 40), (F12, W, 100))],
  events=[(F12, "The Medes lose heavily in the narrows [hdt]", ["hdt"])], conf="medium", day=1, cite=["hdt", "diod", "kv"],
  debate="The time is illustrative: Herodotus says only that the combat 'went on throughout the day' [hdt]. Diodorus adds Sacae to the second wave [diod].")
B.phase("16:00", "The Immortals", "Feigned flights",
  "When the Medes are worn out, Hydarnes' Immortals take their place and fare no better: their spears are shorter and they cannot use their numbers. The Spartans turn their backs as if in flight, wait for the Persians to rush after them in disorder, then face about and cut them down. Xerxes is said to have leapt from his seat three times [hdt].",
  tac("Feigned retreat", "Drilled troops turned and pretended to run; when the pursuers broke ranks, they faced about and struck.", "feigned-retreat"),
  F12, 2.0,
  arrows=[ARR("imm", "charge", MID, (F12, W, 150)), ARR("spa", "retreat", F12, (F12, E, 60)), ARR("per", "retreat", (F12, W, 200), ANTH)],
  events=[(F12, "Spartan feigned flights [hdt]", ["hdt"]), ((ANTH, 200, 300), "Xerxes leaps from his seat [hdt]", ["hdt"])], conf="medium", day=1, cite=["hdt", "diod"])
B.phase("10:00", "Day 2", "The contingents take turns",
  "The next day the Persians attack again, hoping the few defenders are exhausted. The Greeks are drawn up by companies and nations and fight in turn, all except the Phocians, who are on the mountain [hdt]. Diodorus has picked men from every nation sent in, threatened with death if they fled, with the reserves blocking their retreat [diod].",
  tac("Rally and re-form", "Rotating fresh units into a narrow front keeps the line strong while tired men rest behind the wall.", "rally-reform"),
  F12, 2.0,
  arrows=[ARR("per", "move", ANTH, MID, (F12, W, 150))],
  events=[(F12, "Contingents relieve each other in the line [hdt]", ["hdt"])], conf="medium", day=2, cite=["hdt", "diod"],
  debate="Herodotus does not say which contingents fought when; the Thespians and Arcadians are shown in the line only to illustrate the rotation [hdt]. Diodorus says the opposite of rotation on this day: the lines that usually relieved each other 'would not withdraw' [diod].")
B.phase("20:00", "Lamp-lighting", "Ephialtes leads Hydarnes out",
  "Ephialtes, a Malian, tells Xerxes about the path over the mountain. 'About the time when the lamps are lit' Hydarnes leaves the camp with his men. Herodotus says the path 'begins from the river Asopos, which flows through the cleft'; the path and the mountain are both called Anopaia [hdt]. The Malians had once led the Thessalians against the Phocians by it [hdt]. Diodorus says 20,000 men went [diod].",
  tac("Turning movement", "A force marches round the enemy's flank by a route he thinks too hard or too little known, to arrive in his rear.", "turning-movement"),
  ASOPUS_X, 6.0,
  arrows=[ARR("imm", "move", (PCAMP, 180, 350), ASOPUS_X)],
  events=[(ASOPUS_X, "The Persians cross the Asopus; the Anopaea begins [hdt]", ["hdt"])], conf="medium", day=2, cite=["hdt", "diod", "rop"],
  debate="Herodotus names rival informers, Onetes of Karystos and Korydallos of Antikyra, and rejects them for Ephialtes [hdt]. Rop argues that the Persians knew of the path from the moment they arrived and planned the attack round it; Ephialtes' role may be a later simplification [rop].")
B.phase("01:00", "Night march", "Up the mountain in the dark",
  "The column climbs all night, with the Oetaean mountains on its right and the Trachinian on its left [hdt]. In the Greek camp the seer Megistias reads death at dawn in the sacrifices, and deserters come in before daylight with the news that the Persians are going round [hdt]. Diodorus names one, Tyrrhastiadas of Cyme [diod].",
  tac("Turning movement", "A night march over a mountain path is slow and blind; everything depends on the guide.", "turning-movement"),
  NIGHT, 9.0,
  arrows=[ARR("imm", "move", ASOPUS_X, KALK, PALEO, NIGHT)],
  events=[(KALK, "Ascent by the Kalkomata spring (Pritchett) [reed]", ["reed"]), (GCAMP, "Megistias and deserters warn the Greeks [hdt]", ["hdt"])],
  conf="low", day=3, cite=["hdt", "diod", "reed", "kv"],
  debate="Herodotus fixes only the ends: from the Asopus to Alpenos [hdt]. The ascent shown is Pritchett's by the Kalkomata spring; Wallace, Myres and Burn preferred the Vardates ravine further west [reed]. Kromayer's shorter route ran by Alt-Damasta and the north side of Lithitza [kv]. Pausanias says Hydarnes used the easier of two paths, 'through the territory of the Aenianians' [paus]. About 8 km and 1,000 m of climbing lie between the Asopus and the Phocian post: roughly 1 km/h for nine hours of darkness.")
B.phase("05:00", "First light", "The Phocians hear the leaves",
  "At first light the Persians reach the top. The air is still and the ground deep in oak leaves, so the Phocians hear them coming and snatch up their arms. Hydarnes fears they are Spartans until Ephialtes tells him otherwise. Under a shower of arrows the Phocians fall back to the summit to make a stand, but the Persians ignore them and press on [hdt]. Day-watchers run down to the Greeks with the news [hdt].",
  tac("Exposed outpost", "A detachment guarding a remote approach is surprised and stands aside; once the outpost has failed, the main position is turned.", "exposed-outpost"),
  POST, 4.5,
  arrows=[ARR("imm", "fire", (POST, 250, 300), POST), ARR("gre", "retreat", POST, PEAK), ARR("imm", "move", (POST, 250, 300), PLATEAU, M2)],
  events=[(POST, "The Phocians surprised by the Nevropoli meadows [hdt] [rop]", ["hdt", "rop"]), (PEAK, "The Phocians make for the peak [hdt]", ["hdt"])],
  conf="low", day=3, cite=["hdt", "rop"],
  debate="The post is placed on the hill by Nevropoli, following Pritchett, MacKay and Wallace [rop]. Kromayer and some later summaries put the dawn encounter on the Sastani saddle above Drakospilia instead [kv] [reed]. Rop argues that the Phocians, as Delphians, may have stood aside deliberately; Herodotus is silent on what became of them [rop].")
B.phase("06:30", "Dismissal", "Leonidas sends the allies away",
  "A council divides the Greeks. Most march off to their cities; Herodotus thinks Leonidas sent them away himself to save them, keeping the Spartans, the Thespians (who refused to go) and the Thebans (held as hostages) [hdt]. Leonidas also tries to send away Megistias, who stays and sends his son instead [hdt]. Xerxes has poured libations at sunrise and waits, as Ephialtes advises [hdt].",
  tac("Rearguard", "A force sacrifices itself to hold the enemy while the rest of the army gets away.", "rearguard"),
  (38.8010, 22.5500), 6.5,
  arrows=[ARR("gre", "move", (GCAMP, 75, 300), EAST_GATE, (38.8045, 22.5780), (38.8070, 22.6000)), ARR("imm", "move", M2, ALTDRAK, SADDLE)],
  events=[(GCAMP, "Council: the allies go, the Thespians and Thebans stay [hdt]", ["hdt"]), (ALTDRAK, "Hydarnes heads east for the Alpenoi ravine [kv]", ["kv"])],
  conf="medium", day=3, cite=["hdt", "diod", "kv"],
  debate="Diodorus has the council at midnight, keeps only the Lacedaemonians and Thespians (about 500), and sends them on a night attack on Xerxes' tent [diod]. That version is rejected here, as by most modern writers, in favour of Herodotus [stronk]. Which road the allies took is not recorded; the coast road east past Alpenoi, before the Immortals reached it, is assumed. Whether Diodorus's 1,000 Lacedaemonians left or stayed is also unknown [diod] [isoc].")
B.phase("10:00", "The last sortie", "Into the broader part of the pass",
  "At 'the hour when the market fills' Xerxes advances. Knowing they are to die, the Greeks go out much further than before, west of the narrows into the broader part of the pass. Many Persians, driven on by officers with whips, are pushed into the sea or trampled. With most of their spears broken, the Greeks fight with swords. Leonidas falls, and so do Abrocomes and Hyperanthes, brothers of Xerxes. The Greeks drive the enemy back four times and recover the king's body [hdt].",
  tac("Frontal assault", "A huge force pushed head-on into a narrow front pays heavily for every metre.", "frontal-assault"),
  F3, 2.4,
  arrows=[ARR("per", "charge", MID, (F3, W, 130)), ARR("spa", "charge", (WALL, W, 40), F12, F3), ARR("imm", "move", ALPENOI, EAST_GATE)],
  events=[(F3, "Leonidas falls; four rallies over his body [hdt]", ["hdt"]), ((38.7962, 22.5235), "Persians driven into the sea [hdt]", ["hdt"])],
  conf="medium", day=3, cite=["hdt", "kv", "museum"],
  debate="Kromayer's map 7 and the Thermopylae museum both put this fight west of the narrows [kv] [museum]. Diodorus's night raid on the royal tent is a different, later tradition [diod] [stronk].")
B.phase("11:30", "The kolonos", "The last stand",
  "When word comes that Hydarnes is behind them, the survivors fall back past the wall to the hillock in the entrance to the pass, 'where the stone lion now stands for Leonidas'. The Thebans break away and surrender. On the hillock the rest fight with daggers, hands and teeth until they are buried under missiles; some Persians break down the wall in front while others close in from all sides [hdt]. Marinatos's 1939 excavation of Kolonos found about 100 bronze and iron arrowheads and a few spearheads [brown].",
  tac("Last stand", "Cut off front and rear, the remnant takes the strongest ground left and fights until overwhelmed.", "last-stand"),
  "Kolonos Hill", 1.9,
  arrows=[ARR("imm", "charge", (KOL, 70, 300), (KOL, 70, 60)), ARR("per", "charge", (WALL, W, 120), (KOL, 230, 60)), ARR("spa", "retreat", F3, F12, WALL, (KOL, 230, 20))],
  events=[("Kolonos Hill", "The last stand on Kolonos [hdt] [brown]", ["hdt", "brown"]), ((WALL, W, 40), "The Thebans surrender [hdt]", ["hdt"])],
  conf="medium", day=3, cite=["hdt", "brown", "reed", "grundy", "kv"],
  debate="The hillock is identified with Kolonos, Kromayer's and Grundy's 'second' hill: before Marinatos's finds it was usually taken to be the hill by the wall [reed] [kv] [grundy]. Herodotus gives 20,000 Persian dead and 4,000 Greek bodies, including helots; most modern writers accept roughly 2,000 Greek dead [hdt] [wp].")

B.export()
