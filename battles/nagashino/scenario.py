"""Nagashino (Shitaragahara), 28-29 June 1575 (Tenshō 3, 5th month, 20th-21st days).

Built around Baba Mino-no-kami Nobuharu, who held the Takeda right, took Maruyama, covered Katsuyori's
retreat and was killed. Positions come from the Shinshiro battlefield markers (OSM) and the General Staff's
1903 1:20,000 map (georeferenced, 143 m); the narrative from Shinchō kōki, Kōyō gunkan ch. 52 and the 1903
staff history. See brief.md for the readings chosen.
"""
import json, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "..", "tools"))
os.chdir(HERE)
from battlekit import Battle

B = Battle("nagashino", HERE)

B.source("shincho", "Ōta Gyūichi, Shinchō kōki, book 8, ch. 4 'Sanshū Nagashino o-kassen no koto' (Wagajikan wagasho text, ja.wikisource)", "https://ja.wikisource.org/wiki/%E4%BF%A1%E9%95%B7%E5%85%AC%E8%A8%98/%E6%88%91%E8%87%AA%E5%88%8A%E6%88%91%E6%9B%B8", "Nobunaga's chronicler: the camps, the hidden 30,000, the palisade, Sakai's raid on Tobigasu at the hour of the dragon, ~1,000 guns under five commanders, the five Takeda waves (Yamagata, Nobukado, Obata, Nobutoyo, Baba), fighting until the hour of the sheep, ~10,000 dead, Baba's conduct 'beyond compare'", "primary")
B.source("koyo", "Kōyō gunkan, ch. 52 (Takeda-side chronicle, early 17th c.), ja.wikisource", "https://ja.wikisource.org/wiki/%E7%94%B2%E9%99%BD%E8%BB%8D%E9%91%91/%E5%93%81%E7%AC%AC%E4%BA%94%E5%8D%81%E4%BA%8C", "the Takeda account: 15,000 (12,000 in the field); Baba's 700 drove Sakuma's ~6,000 inside the palisade; Naitō's ~1,000 against Takigawa; Yamagata's 1,500 against the Tokugawa; Sanada and Tsuchiya killed at the palisade; Baba left with ~80 men, covered the retreat and died without drawing his sword", "primary")
B.source("nsenshi", "General Staff (Sanbō honbu), Nihon senshi: Nagashino-eki (Tokyo, 1903), pp. 12-19 (NDL pid 771066, OCR via NDL Lab)", "https://dl.ndl.go.jp/pid/771066", "official Meiji history: full order of battle for both armies, the Takeda wings and their villages, Sakuma and Ōkubo outside the palisade, Baba at Maruyama, his last stand at Idesawa, fighting 05:00-15:00; also the origin of the '3,000 guns by turns' story", "official")
B.source("nsmap", "General Staff, 'Nagashino senzu' 1:20,000 map in Nihon senshi: Nagashino-eki (1903)", "https://dl.ndl.go.jp/pid/771066", "georeferenced on six points (RMSE 143 m); the allied line along the west of the Rengo-gawa, the Tobigasu forts, the Takeda camps of the 20th", "staff-map")
B.source("byobu", "Nagashino battle folding screen (Edo period), Wikimedia Commons", "https://commons.wikimedia.org/wiki/File:Battle-of-Nagashino-Map-Folding-Screen-1575.png", "pictorial: palisades along the Rengo-gawa, the Tokugawa on the south, the castle on the right", "period-map")
B.source("sites", "Shinshiro city battlefield markers, via OpenStreetMap (camps, graves, the reconstructed palisade, Baba's grave and death site)", "https://www.openstreetmap.org/#map=15/34.922/137.53", "coordinates of the marked sites; modern identifications", "data")
B.source("wpja", "ja.wikipedia, '長篠の戦い' and '馬場信春' (after Takayanagi 1960, Fujimoto Masayuki, Suzuki Masaya, Hirayama Yū 2014, Kaneko Taku 2018/2023)", "https://ja.wikipedia.org/wiki/%E9%95%B7%E7%AF%A0%E3%81%AE%E6%88%A6%E3%81%84", "strength ranges, the Tamon'in nikki loss figure, the gun and 'cavalry' debates, Baba's 700 against Sakuma at Maruyama, his death at Idesawa", "reference")
B.source("wpen", "en.wikipedia, 'Battle of Nagashino'", "https://en.wikipedia.org/wiki/Battle_of_Nagashino", "narrative; the three-rank volley traced to Oze Hoan's Shinchōki and the 1903 staff history", "reference")
B.source("hiut", "Historiographical Institute, University of Tokyo: joint research project 'Reconstructing the battle of Nagashino from related sources' (Kaneko Taku), reports 2013-14", "https://www.hi.u-tokyo.ac.jp/collaboration/kyoten/h26/shinsei_h26_fukugou.pdf", "the state of the sources: later screens and compilations being re-examined", "scholarly")
B.source("data", "AWS Terrain Tiles; OpenStreetMap (rivers, villages); Wikidata", "https://registry.opendata.aws/terrain-tiles/", "modern elevation and geography", "data")

B.meta = {
    "title": "Nagashino", "year": "1575", "era": "early-modern", "war": "Sengoku period: Takeda against Oda and Tokugawa",
    "eyebrow": "29 June 1575 · Mikawa province · Sengoku period",
    "subtitle": "Takeda Katsuyori attacks Oda Nobunaga and Tokugawa Ieyasu behind their palisade at Shitaragahara, and Baba Nobuharu dies covering the retreat.",
    "sides": {
        "oda": {"name": "Oda", "top": "#b98a24", "side": "#7a5a14", "mark": "#1f1a10", "arrow": "#d9a636", "flag": "#b98a24"},
        "tok": {"name": "Tokugawa", "top": "#2c4f86", "side": "#1b3358", "mark": "#efe6c8", "arrow": "#4f7cc4", "flag": "#2c4f86"},
        "tak": {"name": "Takeda", "top": "#a8322d", "side": "#6e1f1b", "mark": "#f3e7cf", "arrow": "#d2503f", "flag": "#a8322d"},
    },
    "belligerents": [
        {"name": "Oda and Tokugawa allies", "short": "Allies", "commander": "Oda Nobunaga and Tokugawa Ieyasu", "sides": ["oda", "tok"], "code": "letters"},
        {"name": "Takeda army", "short": "Takeda", "commander": "Takeda Katsuyori", "sides": ["tak"], "code": "numbers"},
    ],
    "forces": {
        "start": [{"label": "Allies", "n": 40500, "segs": [["oda", 0.765], ["tok", 0.235]]}, {"label": "Takeda", "n": 15000, "segs": [["tak", 1]]}],
        "end": [{"label": "Allies", "n": 6000, "segs": [["oda", 0.6], ["tok", 0.4]]}, {"label": "Takeda", "n": 10000, "segs": [["tak", 1]]}],
    },
    "days": ["5th month, 20th day (28 June 1575)", "5th month, 21st day (29 June 1575)"],
    "sun": {"lat": 34.92, "decl": 22.4, "note": "29 June 1575 in the Julian calendar is 9 July in ours; sunrise about 04:50 local solar time. The sources give the old two-hour 'hours' (dragon ~07-09, sheep ~13-15), so times are approximate [shincho] [nsenshi]."},
    "view": {"az": -0.35, "el": 0.8}, "unitScale": 1.0, "unitLabelDist": 8,
    "ground": {"season": "summer", "relief": 60},
    "wind": 270,
    "strengthNote": "Traditional figures: Oda ~30,000 and Tokugawa ~8,000, Takeda 15,000 of whom 12,000 fought at Shitaragahara [shincho] [koyo] [nsenshi]; Takayanagi (1960) estimated 16-18,000 against 8-10,000 [wpja]. Shinchō kōki gives ~10,000 Takeda dead, the Tamon'in nikki 'over a thousand' of the Kai gentry [shincho] [wpja]; allied losses are not recorded (the 6,000 lost row is a modern estimate including desertions, low confidence) [wpja]. Strengths inside each Takeda wing and most allied contingents are my division of the sourced totals; per-moment losses are estimates following the narrative.",
    "method": "Camps, graves and the reconstructed palisade are placed from the Shinshiro battlefield markers [sites]; the allied line, the Takeda camps and the Tobigasu forts from the 1903 General Staff map georeferenced on six points (143 m) [nsmap]; the sequence from Shinchō kōki, Kōyō gunkan and the 1903 staff history [shincho] [koyo] [nsenshi]. The Takeda attack positions east of the Rengo-gawa are inferred, and positions are good to a few hundred metres.",
    "notes": "The Baba contingent is featured: its note, a commander flag for Baba himself, and events in phases 3, 5, 6, 8 and 9 follow him from Maruyama to his death. Shinchō kōki makes Baba the fifth and last Takeda wave, while the Takeda tradition puts his capture of Maruyama at the start; both are shown, in that order (my reconciliation) [shincho] [koyo] [nsenshi]. The three-rank volley of 3,000 guns is a later story and is not shown [wpen] [wpja]. The 2016 Shin-Tōmei expressway embankments across the field are removed from the terrain. No historical-map overlay is offered. Per-moment losses are estimates.",
}

# ---- geography
R = json.load(open("sources/rivers.json"))
thin = lambda c, k: c[::k] + [c[-1]]
B.water["rivers"] = [{"p": thin(R["豊川"][0], 3), "w": 22}, {"p": thin(R["宇連川"][0], 3), "w": 16},
                     {"p": thin(R["連吾川"][0], 2), "w": 4, "ford": True}, {"p": thin(R["大宮川"][0], 3), "w": 3, "ford": True},
                     {"p": thin(R["有海原川"][0], 3), "w": 3, "ford": True}]
B.water["labels"] = {"Rengo-gawa": (34.9135, 137.5250), "Kansa-gawa (Takisawa)": (34.9380, 137.5520), "Toyokawa (Norimoto-gawa)": (34.9055, 137.5350), "Ure-gawa": (34.9260, 137.5700)}
B.crossing("Sakai's night ford", (34.9054, 137.5201))
B.crossing("Nagashino bridge site", (34.9218, 137.5585))
B.crossing("Idesawa crossing", (34.9448, 137.5456))

for n, s in [("Shinshiro", 0.8), ("Arumi", 0.5), ("Kiyoida", 0.5), ("Takehiro", 0.5), ("Sunaga", 0.5), ("Ōmiya", 0.5), ("Idesawa", 0.5), ("Ōmi (Ōami)", 0.5)]:
    B.place(n, size=s)
B.place("Nagashino Castle", size=0.6)
for n in ["Maruyama", "Chausuyama", "Danjōyama", "Gokurakujiyama", "Saino-kami"]:
    B.hill(n, n)
B.hill("Tobigasu-yama", (34.9197, 137.5660))
B.hill("Baba Nobuharu's grave", "Baba grave")
B.hill("Where Baba fell (marker)", "Baba death site")
B.roads = [[(34.9020, 137.4950), "Chausuyama", (34.9230, 137.5240), "Kiyoida", "Arumi", (34.9218, 137.5585)],
           [(34.9230, 137.5240), "Sunaga", "Idesawa", (34.9448, 137.5456), (34.9560, 137.5520)],
           ["Kiyoida", "Ōmi (Ōami)", "Iōji"]]
B.roads = [[n if n in B.places else tuple(B.pos(n)) for n in r] for r in B.roads]

def U(uid, side, typ, name, men, w, keys, note, conf, cite, via=None):
    m0 = men[0] if isinstance(men, dict) else men
    u = B.unit(uid, side, typ, name, f"~{m0:,} men", w, note=note, conf=conf, men=men if isinstance(men, dict) else {0: men}, cite=cite)
    for ph, (pos, facing, form, *bend) in keys.items():
        u.at(ph, pos, facing, form, via=(via or {}).get(ph), bend=bend[0] if bend else 0)
    return u

# ================= TAKEDA (camps of the 20th from the 1903 map; attack positions east of the Rengo-gawa)
# --- right wing (north)
U("baba", "tak", "inf", "Baba Mino-no-kami Nobuharu", {0: 700, 3: 650, 5: 600, 6: 300, 7: 150, 8: 80, 9: 20}, 140,
  {0: ((34.9293, 137.5335), 250, "L"), 1: ((34.9262, 137.5292), 270, "L"), 3: ((34.9253, 137.5266), 265, "F"), 5: ((34.9252, 137.5268), 265, "L"),
   6: ((34.9240, 137.5266), 265, "F"), 7: ((34.9270, 137.5310), 250, "F"), 8: ((34.9320, 137.5332), 220, "F"), 9: ("Baba death site", 220, "F")},
  "Baba Mino-no-kami Nobuharu (Nobufusa), aged about 61, Takeda retainer for forty years and the backbone of the right wing. With 700 men he drove Sakuma's larger force inside the palisade and took the Maruyama knoll, then held there while the Sanada and Tsuchiya went forward [koyo] [nsenshi] [wpja]. Shinchō kōki makes his own attack the fifth and last wave [shincho]. He urged Katsuyori to withdraw, covered the retreat with a few score men and, once Katsuyori was out of sight, turned to fight at Idesawa and was killed; Ōta Gyūichi wrote that his conduct was 'beyond compare' [nsenshi] [koyo] [shincho].",
  "medium", ["koyo", "nsenshi", "shincho", "wpja", "sites"], {8: [(34.9290, 137.5320)], 9: [(34.9380, 137.5370)]})
U("sanada", "tak", "inf", "Sanada Nobutsuna and Masateru", {0: 800, 5: 500, 6: 80}, 160,
  {0: ((34.9285, 137.5352), 250, "L"), 1: ((34.9282, 137.5300), 265, "L"), 5: ((34.9272, 137.5266), 260, "F"), 6: ((34.9292, 137.5317), 70, "R")},
  "The Sanada brothers passed Baba on Maruyama, broke into the first palisade and were both killed; Nobutsuna's grave marker stands on the slope behind (strength an estimate) [koyo] [nsenshi] [sites] [shincho].", "medium", ["koyo", "nsenshi", "sites", "shincho"])
U("tsuchiya", "tak", "inf", "Tsuchiya Masatsugu", {0: 400, 5: 250, 6: 40}, 110,
  {0: ((34.9275, 137.5340), 250, "L"), 1: ((34.9240, 137.5293), 270, "L"), 5: ((34.9226, 137.5266), 265, "F"), 6: ((34.9235, 137.5300), 80, "R")},
  "Tsuchiya, who had wanted to follow Shingen in death, was killed at the palisade; a marker stands at the spot (strength an estimate) [koyo] [nsenshi] [sites].", "medium", ["koyo", "nsenshi", "sites"])
U("ichijo", "tak", "inf", "Ichijō Nobutatsu", {0: 500, 7: 350, 8: 300}, 120,
  {0: ((34.9302, 137.5360), 250, "L"), 1: ((34.9268, 137.5322), 265, "L"), 7: ((34.9300, 137.5345), 60, "R"), 8: ((34.9420, 137.5420), 30, "R")},
  "Shingen's half-brother, on the right beside Baba; in Kōyō gunkan he rides up to Baba as the line breaks (strength an estimate) [nsenshi] [koyo].", "low", ["nsenshi", "koyo"])
U("anayama", "tak", "inf", "Anayama Nobukimi", {0: 600, 7: 580}, 130,
  {0: ((34.9310, 137.5385), 250, "L"), 1: ((34.9290, 137.5340), 265, "L"), 7: ((34.9380, 137.5420), 40, "R")},
  "Katsuyori's kinsman withdrew without fighting, according to Kōyō gunkan (strength an estimate) [koyo] [nsenshi].", "low", ["koyo", "nsenshi"])
# --- centre
U("nobukado", "tak", "inf", "Takeda Nobukado (Shōyōken)", {0: 800, 3: 600, 7: 350, 8: 300}, 150,
  {0: ((34.9240, 137.5352), 255, "L"), 1: ((34.9223, 137.5296), 270, "L"), 3: ((34.9212, 137.5264), 270, "F"), 4: ((34.9222, 137.5295), 270, "L"), 7: ((34.9260, 137.5340), 60, "R"), 8: ((34.9410, 137.5400), 30, "R")},
  "Shingen's brother; the second wave in Shinchō kōki, driven back by the guns (strength an estimate) [shincho] [nsenshi].", "medium", ["shincho", "nsenshi"])
U("naito", "tak", "inf", "Naitō Masatoyo", {0: 1000, 6: 600, 7: 400, 8: 60}, 170,
  {0: ((34.9228, 137.5360), 255, "L"), 1: ((34.9207, 137.5292), 270, "L"), 6: ((34.9205, 137.5265), 270, "F"), 7: ((34.9215, 137.5290), 260, "F"), 8: ((34.9233, 137.5305), 250, "F")},
  "About 1,000 men, who drove Takigawa's troops back to the palisade in the Takeda account; Naitō covered the retreat and died near Miyawaki before Baba [koyo] [nsenshi] [sites].", "medium", ["koyo", "nsenshi", "sites"])
U("hara", "tak", "inf", "Hara Masatane", {0: 500, 6: 250, 7: 120}, 110,
  {0: ((34.9215, 137.5370), 255, "L"), 1: ((34.9190, 137.5293), 270, "L"), 6: ((34.9188, 137.5268), 270, "F"), 7: ((34.9182, 137.5285), 80, "R")},
  "Killed in the attack on the palisade; his grave marker stands on the slope east of the Rengo-gawa (strength an estimate) [nsenshi] [sites] [wpja].", "medium", ["nsenshi", "sites", "wpja"])
U("annaka", "tak", "inf", "Annaka Kageshige, Wada and the West Kōzuke men", {0: 700, 6: 450, 7: 250, 8: 200}, 140,
  {0: ((34.9210, 137.5390), 255, "L"), 1: ((34.9205, 137.5318), 270, "L"), 6: ((34.9200, 137.5285), 270, "F"), 7: ((34.9240, 137.5360), 60, "R"), 8: ((34.9400, 137.5390), 30, "R")},
  "The rest of the centre in the 1903 order of battle; Annaka was killed (strength an estimate) [nsenshi] [wpja].", "low", ["nsenshi", "wpja"])
# --- left wing (south)
U("yamagata", "tak", "inf", "Yamagata Masakage", {0: 1500, 2: 1350, 3: 1200, 6: 500, 7: 250}, 220,
  {0: ((34.9160, 137.5352), 255, "L"), 1: ((34.9135, 137.5290), 265, "L"), 2: ((34.9118, 137.5250), 255, "F"), 3: ((34.9130, 137.5272), 265, "F"), 6: ((34.9168, 137.5266), 265, "F"), 7: ((34.9170, 137.5320), 70, "R")},
  "The first wave. His 1,500 tried to turn the allied right south of the Rengo bridge and fought the Ōkubo brothers back and forth nine times; Yamagata was shot and killed, and his grave marker stands near the stream [shincho] [koyo] [nsenshi] [sites].", "medium", ["shincho", "koyo", "nsenshi", "sites"])
U("obata", "tak", "inf", "Obata Nobusada (West Kōzuke 'red' men)", {0: 500, 4: 300, 7: 150}, 120,
  {0: ((34.9170, 137.5370), 255, "L"), 1: ((34.9170, 137.5300), 270, "L"), 4: ((34.9178, 137.5265), 270, "F"), 5: ((34.9182, 137.5290), 270, "L"), 7: ((34.9185, 137.5330), 70, "R")},
  "The third wave: the Obata of West Kōzuke in red armour, good horsemen, who attacked mounted with drums beating and were shot down; an Obata grave marker stands nearby (strength an estimate) [shincho] [nsenshi] [sites].", "medium", ["shincho", "nsenshi", "sites"])
U("nobutoyo", "tak", "inf", "Takeda Nobutoyo (Tenkyū)", {0: 500, 4: 350, 7: 250, 8: 220}, 120,
  {0: ((34.9185, 137.5385), 255, "L"), 1: ((34.9185, 137.5315), 270, "L"), 4: ((34.9194, 137.5268), 270, "F"), 5: ((34.9195, 137.5300), 270, "L"), 7: ((34.9220, 137.5360), 60, "R"), 8: ((34.9400, 137.5410), 30, "R")},
  "Katsuyori's cousin; the fourth wave, which also failed at the palisade (strength an estimate) [shincho] [nsenshi].", "medium", ["shincho", "nsenshi"])
U("oyamada", "tak", "inf", "Oyamada, Atobe, Amari and Ogasawara", {0: 500, 3: 420, 6: 250, 7: 200}, 140,
  {0: ((34.9150, 137.5385), 255, "L"), 1: ((34.9150, 137.5312), 265, "L"), 3: ((34.9140, 137.5290), 260, "F"), 7: ((34.9180, 137.5370), 60, "R")},
  "The rest of the left wing; Atobe's men were the first to run and Amari was killed (strength an estimate) [nsenshi] [koyo] [sites].", "low", ["nsenshi", "koyo", "sites"])
# --- reserve and the siege
U("katsuyori", "tak", "gd", "Takeda Katsuyori (main body)", {0: 2500, 7: 1800, 8: 600, 9: 300}, 220,
  {0: ((34.9195, 137.5460), 260, "L"), 1: ("Saino-kami", 270, "L"), 6: ((34.9218, 137.5310), 270, "L"), 7: ((34.9245, 137.5345), 30, "C"), 8: ((34.9400, 137.5400), 30, "R"), 9: ((34.9520, 137.5510), 40, "R")},
  "The general reserve under Katsuyori, west of Arumi on the 20th; Katsuyori watched from Saino-kami, committed his men late and escaped north with a few hundred (strength an estimate) [nsenshi] [sites] [wpja].", "medium", ["nsenshi", "sites", "wpja"],
  {8: [(34.9300, 137.5360)], 9: [(34.9448, 137.5456)]})
U("mochizuki", "tak", "inf", "Mochizuki Nobumasa and Takeda Nobutomo", {0: 500, 6: 300, 7: 150}, 110,
  {0: ((34.9210, 137.5470), 260, "L"), 1: ((34.9205, 137.5335), 270, "L"), 6: ((34.9198, 137.5285), 270, "F"), 7: ((34.9230, 137.5350), 60, "R")},
  "The rest of the reserve, sent forward late; Mochizuki was killed (strength an estimate) [nsenshi] [wpja].", "low", ["nsenshi", "wpja"])
U("watch", "tak", "inf", "Castle watch (Oyamada Masayuki, Kōsaka Masazumi, Muroga)", {0: 2000, 5: 1400, 6: 1100}, 260,
  {0: ((34.9205, 137.5530), 70, "L"), 4: ((34.9205, 137.5530), 120, "F"), 5: ((34.9260, 137.5495), 330, "R"), 6: ((34.9330, 137.5480), 20, "R")},
  "Two thousand left west of the castle to keep the garrison in; routed by Sakai's column and the garrison, Kōsaka Masazumi killed (strength from Kōyō gunkan and the 1903 history) [koyo] [nsenshi].", "medium", ["koyo", "nsenshi"])
U("tobigasu", "tak", "inf", "Tobigasu forts (Kawakubo Nobuzane)", {0: 1000, 4: 300, 5: 150}, 200,
  {0: ((34.9197, 137.5660), 315, "L"), 4: ((34.9175, 137.5640), 180, "R"), 5: ((34.9120, 137.5620), 200, "R")},
  "Five forts on the heights south of the castle; stormed from behind at the hour of the dragon, Kawakubo Nobuzane killed [shincho] [nsenshi] [nsmap].", "high", ["shincho", "nsenshi", "nsmap"])

# ================= ALLIES (palisade on the west bank of the Rengo-gawa)
def A(uid, side, name, men, w, keys, note, conf, cite, via=None, typ="inf"):
    return U(uid, side, typ, name, men, w, keys, note, conf, cite, via)

A("sakuma", "oda", "Sakuma Nobumori", {0: 6000, 3: 5600, 9: 5400}, 300,
  {0: ((34.9262, 137.5228), 90, "L"), 1: ((34.9256, 137.5262), 90, "L"), 3: ((34.9264, 137.5228), 95, "F"), 7: ((34.9265, 137.5290), 80, "F"), 9: ((34.9395, 137.5385), 40, "F")},
  "Placed outside the palisade around Maruyama as bait in the 1903 history; Kōyō gunkan has Baba's 700 drive about 6,000 of his men inside it [nsenshi] [koyo] [wpja].", "medium", ["nsenshi", "koyo", "wpja", "sites"], {9: [(34.9310, 137.5330)]})
A("ikeda", "oda", "Ikeda, Mizuno, Gamō, Mori and others", {0: 3500, 9: 3400}, 260,
  {0: ((34.9282, 137.5232), 100, "L"), 7: ((34.9290, 137.5290), 90, "F")},
  "Contingents named east of the four hills in the 1903 order of battle, shown together at the north end of the line (strength an estimate) [nsenshi].", "low", ["nsenshi"])
A("niwa", "oda", "Niwa Nagahide", {0: 2000, 9: 1900}, 160,
  {0: ((34.9240, 137.5228), 95, "L"), 7: ((34.9240, 137.5290), 90, "F")},
  "Moved forward onto Arumihara facing east with Takigawa and Hashiba (strength an estimate) [shincho] [nsenshi].", "medium", ["shincho", "nsenshi"])
A("takigawa", "oda", "Takigawa Kazumasu", {0: 3000, 6: 2800, 9: 2750}, 220,
  {0: ((34.9218, 137.5242), 90, "L"), 2: ((34.9218, 137.5242), 90, "F"), 7: ((34.9215, 137.5300), 85, "F")},
  "Behind the palisade on Arumihara, facing east; about 3,000 in Kōyō gunkan, driven back to the palisade by Naitō [shincho] [koyo].", "medium", ["shincho", "koyo", "sites"])
A("gunners", "oda", "Arquebusiers of the five commanders (Sassa, Maeda, Nonomura, Fukutomi, Ban)", {0: 1000, 9: 950}, 500,
  {0: ((34.9200, 137.5248), 90, "L"), 2: ((34.9200, 137.5248), 90, "F"), 7: ((34.9205, 137.5300), 85, "F"), 9: ((34.9400, 137.5395), 40, "F")},
  "About 1,000 guns drawn from many units and put under five commanders along the palisade [shincho]; the later '3,000 firing by turns' is a myth [wpen] [wpja]. Ban Naomasa's man Kawai Sanjūrō is credited with taking Baba's head [wpja].", "medium", ["shincho", "wpen", "wpja"], {9: [(34.9300, 137.5330)]})
A("hashiba", "oda", "Hashiba Hideyoshi", {0: 2000, 5: 1900}, 160,
  {0: ((34.9296, 137.5125), 100, "L"), 1: ((34.9296, 137.5200), 100, "L"), 5: ((34.9300, 137.5258), 165, "F"), 7: ((34.9310, 137.5310), 110, "F")},
  "On Arumihara with Takigawa and Niwa; in the 1903 history he and Shibata came round the north end to take the Sanada in flank (camp marker; strength an estimate) [shincho] [nsenshi] [sites].", "medium", ["shincho", "nsenshi", "sites"])
A("shibata", "oda", "Shibata Katsuie", {0: 2000, 5: 1900}, 160,
  {0: ((34.9150, 137.5060), 80, "L"), 1: ((34.9268, 137.5160), 90, "L"), 5: ((34.9312, 137.5240), 150, "F"), 7: ((34.9320, 137.5300), 110, "F")},
  "With Nobunaga at Gokurakujiyama in the 1903 order of battle, then round the north flank with Hashiba (strength an estimate) [nsenshi].", "low", ["nsenshi"])
A("nobunaga", "oda", "Oda Nobunaga's horse guards", {0: 4500}, 260,
  {0: ("Chausuyama", 90, "L")},
  "Nobunaga camped at Gokurakujiyama, kept his 30,000 hidden in the hollow, and moved to Chausuyama on the night of the 20th (strength an estimate) [shincho] [nsenshi] [sites].", "medium", ["shincho", "nsenshi", "sites"])
A("nobutada", "oda", "Oda Nobutada", {0: 3000}, 220,
  {0: ((34.9195, 137.5100), 90, "L")},
  "Nobunaga's heir, camped on Shinmidōyama (Tenjinyama in the 1903 history) in reserve (exact hill uncertain; strength an estimate) [shincho] [nsenshi].", "low", ["shincho", "nsenshi"])
A("nobukatsu", "oda", "Kitabatake Nobukatsu and Inaba Ittetsu", {0: 2000}, 180,
  {0: ((34.9160, 137.5080), 90, "L")},
  "In reserve on Midōyama in the 1903 order of battle (strength an estimate) [nsenshi].", "low", ["nsenshi"])
A("kanamori", "oda", "Oda guns with Sakai (Kanamori Nagachika)", {0: 1000, 4: 950}, 120,
  {0: ((34.9040, 137.5150), 120, "C"), 1: ((34.9075, 137.5600), 20, "C"), 4: ((34.9185, 137.5630), 340, "F"), 6: ((34.9198, 137.5525), 300, "F"), 8: ((34.9220, 137.5470), 290, "F")},
  "500 of Nobunaga's own guns and his inspectors, Kanamori Nagachika among them, sent with Sakai's column (strength from Shinchō kōki's total of ~4,000) [shincho] [nsenshi].", "medium", ["shincho", "nsenshi"],
  {1: [(34.9054, 137.5201), (34.8930, 137.5380), (34.8862, 137.5535), (34.8990, 137.5600)], 6: [(34.9218, 137.5585)]})
# --- Tokugawa
A("ieyasu", "tok", "Tokugawa Ieyasu", {0: 2000}, 200,
  {0: ("Danjōyama", 90, "L")},
  "Ieyasu camped on Takamatsuyama (Danjōyama) on the Tatsumi slope, where Nobunaga joined him to watch the battle (camp marker; strength an estimate) [shincho] [nsenshi] [sites].", "medium", ["shincho", "nsenshi", "sites"])
A("honda", "tok", "Honda Tadakatsu", {0: 700, 6: 650}, 110,
  {0: ((34.9183, 137.5242), 90, "L"), 2: ((34.9183, 137.5242), 90, "F"), 7: ((34.9180, 137.5295), 80, "F")},
  "Behind the Tokugawa palisade (strength an estimate) [nsenshi].", "low", ["nsenshi"])
A("sakakibara", "tok", "Sakakibara Yasumasa", {0: 700, 6: 650}, 110,
  {0: ((34.9163, 137.5235), 90, "L"), 2: ((34.9163, 137.5235), 90, "F"), 7: ((34.9160, 137.5290), 80, "F")},
  "Behind the Tokugawa palisade (strength an estimate) [nsenshi].", "low", ["nsenshi"])
A("ishikawa", "tok", "Ishikawa Kazumasa, Torii Mototada, Hiraiwa and others", {0: 600, 6: 550}, 110,
  {0: ((34.9143, 137.5224), 90, "L"), 2: ((34.9143, 137.5224), 90, "F"), 7: ((34.9140, 137.5285), 80, "F")},
  "The rest of the Tokugawa line in the 1903 order of battle (strength an estimate) [nsenshi].", "low", ["nsenshi"])
A("okubo", "tok", "Ōkubo Tadayo and Tadasuke", {0: 1000, 2: 900, 3: 800, 7: 750}, 140,
  {0: ("Ōkubo brothers' camp", 80, "L"), 1: ((34.9105, 137.5235), 75, "L"), 2: ((34.9108, 137.5238), 70, "F"), 7: ((34.9125, 137.5290), 70, "F")},
  "Outside the palisade on the allied right; the brothers fought Yamagata's men back and forth nine times (camp marker; strength an estimate) [nsenshi] [koyo] [sites].", "medium", ["nsenshi", "koyo", "sites"])
A("nobuyasu", "tok", "Matsudaira Nobuyasu", {0: 1000}, 140,
  {0: ((34.9135, 137.5170), 90, "L")},
  "Ieyasu's heir, on Matsuoyama behind the Tokugawa line in the 1903 order of battle (hill and strength uncertain) [nsenshi].", "low", ["nsenshi"])
A("sakai", "tok", "Sakai Tadatsugu's column", {0: 3000, 4: 2800, 6: 2700}, 220,
  {0: ((34.9035, 137.5130), 120, "C"), 1: ((34.9065, 137.5615), 10, "C"), 4: ((34.9192, 137.5650), 330, "F"), 6: ((34.9195, 137.5508), 300, "F"), 8: ((34.9215, 137.5450), 290, "F")},
  "About 2,000 picked Tokugawa archers and gunners and their commanders; they crossed the Toyokawa at night in rain, climbed by Matsuyama-goe and stormed the Tobigasu forts from behind at dawn, then cleared the castle watch at Arumi, cutting the Takeda line of retreat [shincho] [nsenshi] [wpja] [sites].", "high", ["shincho", "nsenshi", "wpja", "sites"],
  {1: [(34.9054, 137.5201), (34.8930, 137.5380), (34.8862, 137.5535), (34.8990, 137.5600)], 6: [(34.9218, 137.5585)]})
A("okudaira", "tok", "Nagashino garrison (Okudaira Sadamasa)", {0: 500, 6: 420}, 90,
  {0: ("Nagashino Castle", 270, "X"), 4: ((34.9220, 137.5575), 250, "F"), 6: ((34.9210, 137.5540), 250, "F")},
  "About 500 men who had held the castle for weeks; they sortied to join Sakai once Tobigasu fell [wpen] [shincho] [nsenshi].", "medium", ["wpen", "shincho", "nsenshi"])

B.commander("baba_hq", "tak", "Baba Nobuharu", {0: (34.9297, 137.5338), 1: (34.9266, 137.5296), 3: (34.9257, 137.5270), 6: (34.9244, 137.5270), 7: (34.9273, 137.5313), 8: (34.9323, 137.5336), 9: "Baba death site"},
            "Baba led from the front; the flag follows him from Maruyama to Idesawa [koyo] [nsenshi].")
B.commander("katsuyori_hq", "tak", "Takeda Katsuyori", {0: (34.9195, 137.5465), 1: "Saino-kami", 7: (34.9250, 137.5350), 8: (34.9405, 137.5405), 9: (34.9525, 137.5515)}, "Katsuyori watched from Saino-kami [sites].")
B.commander("nobunaga_hq", "oda", "Oda Nobunaga", {0: "Chausuyama", 2: "Danjōyama"}, "On the morning of the 21st Nobunaga went up to Ieyasu's camp on Takamatsuyama to watch and direct [shincho].")
B.commander("ieyasu_hq", "tok", "Tokugawa Ieyasu", {0: (34.9162, 137.5205)}, "Takamatsuyama (Danjōyama) [shincho] [sites].")

# ================= PHASES
B.phase("20:00", "Night raid", "Sakai sets out for Tobigasu",
  "The Takeda have crossed the Takisawa (Kansa) river and camp east of the Rengo-gawa: the right wing near Asagi, the centre at Kiyoida, the left on the heights to the south, Katsuyori's reserve west of Arumi, with 2,000 watching the castle and 1,000 in the forts on Tobigasu-yama [nsenshi] [koyo]. About 2 km to the west the allies wait behind a palisade, most of Nobunaga's 30,000 hidden in the hollow of Shitaragahara [shincho]. At 20:00 Sakai Tadatsugu leads about 4,000 men, 500 of them Nobunaga's own gunners, across the Toyokawa in the rain to circle round the Takeda [shincho] [nsenshi].",
  ("A threat to the rear", "A force sent round behind the enemy turns his siege lines into a trap and leaves his army with no safe way home.", "rear-threat"), (34.9180, 137.5380), 7.5, day=1,
  arrows=[B.arrow("tok", "move", (34.9035, 137.5130), (34.9054, 137.5201), (34.8930, 137.5380), (34.8862, 137.5535), (34.8990, 137.5600), (34.9065, 137.5615))],
  events=[((34.8862, 137.5535), "Sakai's column climbs by Matsuyama-goe in the dark [nsenshi] [sites]", ["nsenshi", "sites"]), ((34.9262, 137.5292), "Baba Nobuharu's 700 on the Takeda right [koyo]", ["koyo"])],
  conf="medium", cite=["nsenshi", "koyo", "shincho", "sites"])
B.phase("04:45", "Dawn", "Facing the palisade",
  "At first light the Takeda deploy facing west a few hundred metres east of the Rengo-gawa, Shinchō kōki's 'thirteen bodies' about 15,000 strong [shincho] [nsenshi]. In front of them a palisade runs along the west bank of the stream; Sakuma Nobumori stands outside it on the Maruyama knoll at the north end and the Ōkubo brothers outside it at the south end, both as bait [nsenshi] [sites]. Nobunaga has moved to Chausuyama in the night; Ieyasu is on Danjōyama [shincho] [nsenshi] [sites]. Baba Nobuharu holds the Takeda right opposite Maruyama [koyo] [nsenshi].",
  ("Field fortifications", "A palisade and ditch let a larger army fight on ground of its own choosing; the enemy must attack across a stream into prepared fire.", "field-obstacles"), (34.9210, 137.5280), 3.8, day=2,
  events=[((34.9216, 137.5250), "The allied palisade along the Rengo-gawa (reconstructed today) [sites] [shincho]", ["sites", "shincho"]), ((34.9256, 137.5262), "Sakuma outside the palisade on Maruyama [nsenshi]", ["nsenshi"])],
  conf="medium", cite=["shincho", "nsenshi", "sites", "koyo"])
B.phase("05:30", "First wave", "Yamagata attacks in the south",
  "Yamagata Masakage's men come on with drums beating and are driven back by the guns [shincho]. In the 1903 history he tries to turn the allied right south of the Rengo bridge, finds the stream too deep and its banks too steep, and turns on the Ōkubo brothers outside the palisade; Kōyō gunkan counts nine clashes [nsenshi] [koyo].",
  ("Frontal assault", "Attacking a prepared position head on across a stream and into massed fire.", "frontal-assault"), (34.9150, 137.5265), 2.4, day=2,
  arrows=[B.arrow("tak", "charge", (34.9135, 137.5290), (34.9118, 137.5255)), B.arrow("tok", "fire", (34.9108, 137.5238), (34.9117, 137.5252)), B.arrow("tok", "fire", (34.9150, 137.5232), (34.9125, 137.5255))],
  events=[((34.9112, 137.5246), "Yamagata against the Ōkubo brothers: nine clashes [koyo]", ["koyo"])],
  conf="medium", cite=["shincho", "nsenshi", "koyo"])
B.phase("06:30", "Maruyama", "Baba takes Maruyama",
  "On the Takeda right Baba Nobuharu attacks Sakuma Nobumori outside the palisade. Sakuma falls back inside, feigning defeat in the 1903 history, and Baba takes the Maruyama knoll and halts there instead of following him to the palisade [nsenshi] [koyo] [wpja]. In the centre Takeda Nobukado leads the second wave forward and is driven back by the guns [shincho].",
  ("Bait", "Sakuma's men stood outside the palisade to be driven in and draw the enemy onto the guns; Baba took the ground and refused the lure.", "bait"), (34.9240, 137.5265), 2.0, day=2,
  arrows=[B.arrow("tak", "charge", (34.9262, 137.5292), (34.9254, 137.5268)), B.arrow("oda", "retreat", (34.9256, 137.5262), (34.9264, 137.5232)), B.arrow("tak", "charge", (34.9223, 137.5296), (34.9213, 137.5266)),
          B.arrow("oda", "fire", (34.9205, 137.5248), (34.9213, 137.5264))],
  events=[((34.9251, 137.5250), "Baba's 700 take Maruyama from Sakuma [koyo] [nsenshi] [sites]", ["koyo", "nsenshi", "sites"])],
  conf="medium", cite=["nsenshi", "koyo", "wpja", "shincho", "sites"],
  debate="Shinchō kōki, the only primary account, makes Baba the fifth and last wave; the Takeda tradition (Kōyō gunkan) and the 1903 history put his attack on Sakuma first. This map shows both: Maruyama now and Baba's own assault later [shincho] [koyo] [nsenshi].")
B.phase("08:00", "Tobigasu", "The forts fall behind the Takeda",
  "At the hour of the dragon Sakai's column, which has climbed onto the heights south of the castle in the dark, raises its banners, shouts its war cry, fires several hundred guns and storms the Tobigasu forts from behind; Kawakubo Nobuzane is killed, the garrison breaks out to join Sakai, and the Takeda siege huts are burned [shincho] [nsenshi]. At Shitaragahara the third wave (the Obata of West Kōzuke, in red, attacking mounted) and the fourth (Takeda Nobutoyo) go in and are shot down [shincho].",
  ("A threat to the rear", "With the forts behind them lost, the Takeda in front of the palisade could no longer simply wait or withdraw.", "rear-threat"), (34.9195, 137.5450), 6.0, day=2,
  arrows=[B.arrow("tok", "charge", (34.9065, 137.5615), (34.9192, 137.5650)), B.arrow("tak", "retreat", (34.9197, 137.5660), (34.9120, 137.5620)),
          B.arrow("tak", "charge", (34.9170, 137.5300), (34.9178, 137.5266)), B.arrow("tak", "charge", (34.9185, 137.5315), (34.9194, 137.5270)), B.arrow("oda", "fire", (34.9200, 137.5248), (34.9188, 137.5266))],
  events=[((34.9197, 137.5660), "Tobigasu stormed; Kawakubo Nobuzane killed [shincho] [nsenshi]", ["shincho", "nsenshi"]), ((34.9227, 137.5595), "The Nagashino garrison sorties [nsenshi]", ["nsenshi"])],
  conf="high", cite=["shincho", "nsenshi", "nsmap"])
B.phase("09:30", "The Sanada", "The right wing breaks on the palisade",
  "Baba holds Maruyama and tells the Sanada brothers and Tsuchiya Masatsugu to go forward and win the honours [nsenshi]. They break into the first palisade, but the guns cut them down and Shibata Katsuie and Hashiba Hideyoshi come round the north end into their flank; Sanada Nobutsuna, his brother Masateru and Tsuchiya are killed [nsenshi] [koyo]. Meanwhile Sakai's column and the garrison drive the castle watch from Arumi [nsenshi].",
  ("Combined arms", "Guns behind the palisade stopped the attack; spearmen coming round the flank finished it.", "combined-arms"), (34.9265, 137.5265), 2.2, day=2,
  arrows=[B.arrow("tak", "charge", (34.9282, 137.5300), (34.9272, 137.5268)), B.arrow("tak", "charge", (34.9240, 137.5293), (34.9227, 137.5268)), B.arrow("oda", "charge", (34.9296, 137.5200), (34.9300, 137.5258)), B.arrow("oda", "charge", (34.9268, 137.5160), (34.9310, 137.5240)),
          B.arrow("oda", "fire", (34.9282, 137.5235), (34.9272, 137.5262)), B.arrow("tok", "charge", (34.9192, 137.5650), (34.9195, 137.5510))],
  events=[((34.9221, 137.5250), "Tsuchiya Masatsugu killed at the palisade [sites] [koyo]", ["sites", "koyo"]), ((34.9272, 137.5262), "The Sanada brothers break one palisade and are killed [koyo] [nsenshi]", ["koyo", "nsenshi"])],
  conf="medium", cite=["nsenshi", "koyo", "sites"])
B.phase("11:00", "Fifth wave", "Baba's own attack; Yamagata falls",
  "Baba Mino-no-kami now leads his own men forward with drums beating, the fifth wave in Shinchō kōki, and loses many like the others [shincho]. In the south Yamagata Masakage is shot through the body and killed; one of his men carries his head back to Kai [koyo] [nsenshi]. Katsuyori commits his reserve, but the attackers melt away under the guns [nsenshi] [shincho].",
  ("Committing the reserve", "Feeding the reserve into an attack that has already failed adds casualties, not weight.", "reserve-commitment"), (34.9205, 137.5275), 2.6, day=2,
  arrows=[B.arrow("tak", "charge", (34.9252, 137.5268), (34.9242, 137.5262)), B.arrow("tak", "charge", (34.9207, 137.5292), (34.9205, 137.5268)), B.arrow("oda", "fire", (34.9218, 137.5242), (34.9230, 137.5262)), B.arrow("tok", "fire", (34.9163, 137.5235), (34.9168, 137.5262))],
  events=[((34.9168, 137.5264), "Yamagata Masakage shot dead; his grave marker [koyo] [sites]", ["koyo", "sites"]), ((34.9240, 137.5262), "Baba leads the fifth wave [shincho]", ["shincho"])],
  conf="low", cite=["shincho", "koyo", "nsenshi", "sites"])
B.phase("13:00", "Collapse", "The allies come out of the palisade",
  "The Takeda line comes apart. Atobe's men run first, and Anayama withdraws without having fought [nsenshi] [koyo]. Sassa Narimasa tells Nobunaga the enemy banners are wavering, and the whole allied army comes out of the palisade, the Oda in front and the Tokugawa on the Takeda left [nsenshi]. Baba sends word urging Katsuyori to withdraw [nsenshi].",
  ("Pursuit", "Once a beaten army turns its back, the pursuit does most of the killing.", "pursuit"), (34.9230, 137.5310), 3.0, day=2,
  arrows=[B.arrow("oda", "charge", (34.9240, 137.5228), (34.9240, 137.5290)), B.arrow("oda", "charge", (34.9205, 137.5248), (34.9205, 137.5300)), B.arrow("tok", "charge", (34.9150, 137.5235), (34.9160, 137.5290)),
          B.arrow("tak", "retreat", (34.9218, 137.5310), (34.9300, 137.5360))],
  events=[((34.9245, 137.5345), "Katsuyori begins to withdraw north [nsenshi]", ["nsenshi"])],
  conf="medium", cite=["nsenshi", "koyo", "shincho"])
B.phase("14:00", "Rearguard", "Baba and Naitō cover the retreat",
  "The Takeda flee north towards Hōraiji, many drowning or falling at the river crossings [shincho] [nsenshi]. Naitō Masatoyo stands to cover Katsuyori and is killed near Miyawaki [nsenshi]. Baba, still unwounded with a few score men, refuses to leave until Katsuyori's standard is safely away [koyo] [nsenshi]. Kasai Higo gives Katsuyori his own horse and is killed [koyo] [sites].",
  ("Rearguard", "A few hundred men who stand and die can buy the time for their commander to escape.", "rearguard"), (34.9310, 137.5350), 3.6, day=2,
  arrows=[B.arrow("tak", "retreat", (34.9245, 137.5345), (34.9300, 137.5360), (34.9400, 137.5400)), B.arrow("oda", "charge", (34.9265, 137.5290), (34.9300, 137.5320)), B.arrow("tok", "charge", (34.9195, 137.5508), (34.9215, 137.5450))],
  events=[((34.9233, 137.5303), "Naitō Masatoyo killed near Miyawaki [nsenshi]", ["nsenshi"]), ((34.9320, 137.5332), "Baba covers the retreat [koyo] [nsenshi]", ["koyo", "nsenshi"]), ((34.94613, 137.54456), "Kasai Higo killed here after giving Katsuyori his horse (marker) [sites] [koyo]", ["sites", "koyo"])],
  conf="medium", cite=["shincho", "nsenshi", "koyo", "sites"])
B.phase("15:00", "Idesawa", "Baba's last stand",
  "Once Katsuyori is out of sight, Baba turns back on a knoll at Idesawa above the Kansa river, calls out his name and is killed; Kōyō gunkan says he would not draw his sword [nsenshi] [koyo]. Ōta Gyūichi lists him among the Takeda dead and writes that his conduct was 'beyond compare' [shincho]. The fighting ends about 15:00; the Takeda have lost about 10,000 men by Shinchō kōki's count, including Baba, Yamagata, Naitō, Hara, Tsuchiya and both Sanada brothers [nsenshi] [shincho] [wpja].",
  ("Rearguard", "Baba's stand let Katsuyori cross the Kansa river and escape; the Takeda lost their senior generals in a single day.", "rearguard"), (34.9420, 137.5420), 2.8, day=2,
  arrows=[B.arrow("tak", "retreat", (34.9400, 137.5400), (34.9448, 137.5456), (34.9520, 137.5510)), B.arrow("oda", "charge", (34.9300, 137.5330), (34.9395, 137.5385))],
  events=[((34.94436, 137.5443), "Baba Nobuharu killed at Idesawa (marker) [nsenshi] [sites]", ["nsenshi", "sites"]), ((34.92367, 137.5544), "Baba's grave near the castle; Kōyō gunkan puts his death at the Nagashino bridge site [koyo] [sites]", ["koyo", "sites"])],
  conf="medium", cite=["nsenshi", "koyo", "shincho", "sites", "wpja"],
  debate="Where Baba died: the 1903 history and a Shinshiro marker put it at Idesawa on the Kansa river; Kōyō gunkan says the Nagashino bridge site, near which his grave stands. How: Kōyō gunkan has him speared by four or five men without drawing his sword; later accounts have him offer his head to Kawai Sanjūrō, a man of Ban Naomasa [nsenshi] [koyo] [sites] [wpja].")

B.export()
