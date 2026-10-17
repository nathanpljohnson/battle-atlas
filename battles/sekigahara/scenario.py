"""Sekigahara, 21 October 1600 (Keichō 5, 9th month, 15th day). A traditional reconstruction.

Western and Eastern positions start from the camp sites marked on the ground (Sekigahara town open data, OSM),
checked against Fujii Jizaemon's 1926 situation map (georeferenced, 227 m) and a plot from the bakufu compilation
Chōya kyūbun hōkō on the 1894 survey (114 m). Advanced positions are read off the Fujii map with wp(x, y).
The timetable is the traditional one (fighting from ~08:00, Kobayakawa about noon); the revisionist reading
(Shiramine, Takahashi: defection at the outset, ~10:00) is given in the phase text and debate fields.
"""
import json, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "..", "tools"))
os.chdir(HERE)
from battlekit import Battle
from georef import Georef

B = Battle("sekigahara", HERE)
wp = lambda x, y: Georef(HERE).xy("fujii", x, y)

B.source("ishikawa", "Ishikawa Yasumichi and Hikosaka Motomasa to Matsudaira Ienori, Keichō 5.9.17 (two days after the battle); text in Nakano Hitoshi (2017) p. 462, quoted in ja.wikipedia and Shiramine (2016)", "https://ja.wikipedia.org/wiki/%E9%96%A2%E3%83%B6%E5%8E%9F%E3%81%AE%E6%88%A6%E3%81%84", "primary letter: Ieyasu engaged at Sekigahara at the hour of the snake (~10:00); Ii and Fukushima as vanguard; Kobayakawa, Wakisaka and Ogawa father and son 'turned' as the lines met; Ōtani, Shima Sakon, Shimazu Toyohisa, Toda and Hiratsuka killed", "primary")
B.source("ieyasu", "Tokugawa Ieyasu to Date Masamune, Keichō 5.9.15 (the day of the battle), as summarised in ja/en.wikipedia", "https://en.wikipedia.org/wiki/Battle_of_Sekigahara", "primary letter: the fighting was over by the hour of the horse (~noon)", "primary")
B.source("shimazu", "Memoirs of Shimazu retainers (Kanbe Gobei, Kuroki Sakon and Hirayama Kurōzaemon, Yamada Ansai and others) in Kyūki zatsuroku kōhen 3, in modern Japanese in Shiramine (2016)", "https://beppu-u.repo.nii.ac.jp/records/2002278", "participants' memoirs: Ōtani attacked first; six or seven clashes before Kobayakawa came down 'from the hill above'; Ukita, then Ishida broken; a pond between Ukita and the Shimazu; Shimazu Yoshihiro in the second line", "primary")
B.source("shiramine", "Shiramine Jun, 'Sekigahara no tatakai ni okeru Ishida Mitsunari-gata gunzei no fujin ichi ni tsuite no shinkaishaku', Shigaku ronsō 46 (Beppu University, 2016), 151-160", "https://beppu-u.repo.nii.ac.jp/records/2002278", "revisionist, built on letters and memoirs: Western main body packed tightly at Yamanaka; Ishida not on Sasaoyama; Ōtani destroyed first; the marked camp sites were fixed by Gifu officials after Kamiya Dōichi's 1892 Sekigahara kassen zushi", "scholarly")
B.source("shiramine2", "Shiramine Jun, 'Sekigahara no tatakai no fujinzu ni kansuru kōsatsu', Beppu daigaku kiyō", "https://beppu-u.repo.nii.ac.jp/records/2001668", "the 1893 General Staff deployment map is a Meiji creation; Furuta Shigekatsu on it is an error for Furuta Shigenari (Oribe); Terazawa's presence is not confirmed by primary sources; Ii and Fukushima should stand together as joint vanguard", "scholarly")
B.source("kasaya", "Kasaya Kazuhiko, Sekigahara kassen (Kōdansha, 1994; rev. 2022), pp. 209-227, as summarised with page references in ja.wikipedia (not consulted directly)", "https://ja.wikipedia.org/wiki/%E9%96%A2%E3%83%B6%E5%8E%9F%E3%81%AE%E6%88%A6%E3%81%84", "traditionalist: skirmishing from ~08:00 in fog, general attack ~10:00 when it lifted; 'several hours' of fighting before Kobayakawa turned about noon (Shimazu diary, Chōsa memoir); 'crushed at once' is a stock victory phrase", "scholarly")
B.source("takahashi", "Takahashi Yōsuke, 'Atarashii Sekigahara' (Kōdansha Gendai shinsho, 2025), extract on gendai.media", "https://gendai.media/articles/-/159156", "revisionist overview: the standard story comes from the General Staff's Nihon senshi; the probing shots and the Meckel anecdote are later inventions; Kobayakawa had defected by the day before", "scholarly")
B.source("turnbull", "Stephen Turnbull, 'The battle of Sekigahara – what went right?', Osprey blog (2019)", "https://www.ospreypublishing.com/uk/osprey-blog/2019/the-battle-of-sekigahara-what-went-right", "specialist's English summary of Shiramine: early reports name Yamanaka; all modern maps derive from Nihon senshi (1893); defection at the start; the probing shots a myth", "secondary")
B.source("murdoch", "James Murdoch, A History of Japan, vol. 2 (Kobe, 1903), ch. XIV 'Sekigahara', following the General Staff's Nihon senshi", "https://archive.org/details/historyofjapan02murd", "the traditional narrative in English: night march, fog, Ii's thirty spearmen, Fukushima against Ukita, stalemate to noon, Kobayakawa's attack and the four defectors, the Shimazu breakout, 8,000 Western dead", "secondary")
B.source("wpja", "ja.wikipedia, '関ヶ原の戦い' and '関ヶ原本戦の配置' (General Staff strength table; deployments in Kuroda kafu, Sekigahara gunki taisei, Naifukō gunki, Sekigahara shimatsuki)", "https://ja.wikipedia.org/wiki/%E9%96%A2%E3%83%B6%E5%8E%9F%E6%9C%AC%E6%88%A6%E3%81%AE%E9%85%8D%E7%BD%AE", "strengths (3 men per 100 koku), the Edo accounts' variants, scholarly debates", "reference")
B.source("wpen", "en.wikipedia, 'Battle of Sekigahara' (after Bryant 1995, Davis 1999, Watanabe 2021, Mitsunari 2016)", "https://en.wikipedia.org/wiki/Battle_of_Sekigahara", "narrative, Ii's red-armoured troops, Hiratsuka's 360, the Shimazu escape, the dispute over Kobayakawa's timing", "reference")
B.source("fujii", "Fujii Jizaemon, situation map of the morning of the 15th (1926), National Diet Library, via Wikimedia Commons", "https://commons.wikimedia.org/wiki/File:Map_of_battle-of-Sekigahara(midmorning).jpg", "unit symbols at their camps and advanced positions on a Taishō survey base; georeferenced on nine points (RMSE 227 m)", "period-map")
B.source("hi", "Deployment after Chōya kyūbun hōkō, plotted on the 1894 1:20,000 survey sheet 'Sekihara' (Wikimedia Commons, user HI)", "https://commons.wikimedia.org/wiki/File:Sekigaharahonsen(sekigaharahoumen).jpg", "an Edo-compilation tradition independent of the 1893 staff map: Ōtani's main body at Yamanaka, Ieyasu's forward command post; georeferenced on six points (RMSE 114 m)", "staff-map")
B.source("nsmap", "General Staff (Sanbō honbu), Nihon senshi: Sekigahara-eki,附図 (1893), as redrawn on Wikimedia Commons", "https://commons.wikimedia.org/wiki/File:Sekigahara.png", "the canonical 08:00 deployment; used only for cross-checking", "staff-map")
B.source("jinseki", "Sekigahara town open data, 'Sekigahara ichi jōhō list' (2013, LinkData) and OpenStreetMap memorials", "https://linkdata.org/work/rdf1s884i", "coordinates of the camp sites marked on the battlefield (a Meiji-era identification)", "data")
B.source("data", "AWS Terrain Tiles; OpenStreetMap (streams, ponds, villages); Wikidata", "https://registry.opendata.aws/terrain-tiles/", "modern elevation and geography", "data")

B.meta = {
    "title": "Sekigahara", "year": "1600", "era": "early-modern", "war": "Sekigahara campaign (Sengoku period)",
    "eyebrow": "21 October 1600 · Mino province · Sekigahara campaign",
    "subtitle": "Tokugawa Ieyasu's army meets Ishida Mitsunari's coalition in a foggy mountain basin, and the battle turns when Western contingents change sides.",
    "sides": {
        "w": {"name": "Western army", "top": "#a8322d", "side": "#6e1f1b", "mark": "#f3e7cf", "arrow": "#d2503f", "flag": "#a8322d"},
        "t": {"name": "Defectors", "top": "#7b4fa0", "side": "#4e2f68", "mark": "#f3e7cf", "arrow": "#9b6fc4", "flag": "#7b4fa0"},
        "e": {"name": "Eastern army", "top": "#2c4f86", "side": "#1b3358", "mark": "#efe6c8", "arrow": "#4f7cc4", "flag": "#2c4f86"},
    },
    "belligerents": [
        {"name": "Eastern army", "short": "East", "commander": "Tokugawa Ieyasu", "sides": ["e"], "code": "letters"},
        {"name": "Western army", "short": "West", "commander": "Ishida Mitsunari (for Mōri Terumoto and Toyotomi Hideyori)", "sides": ["w"], "code": "numbers"},
        {"name": "Western contingents that changed sides", "short": "Defectors", "commander": "Kobayakawa Hideaki", "sides": ["t"], "code": "numbers"},
    ],
    "forces": {
        "start": [{"label": "East", "n": 88900, "segs": [["e", 1]]}, {"label": "West", "n": 63100, "segs": [["w", 1]]}, {"label": "Defectors", "n": 20000, "segs": [["t", 1]]}],
        "end": [{"label": "East", "n": 4000, "segs": [["e", 1]]}, {"label": "West", "n": 8000, "segs": [["w", 1]]}, {"label": "Defectors", "n": 800, "segs": [["t", 1]]}],
    },
    "sun": {"lat": 35.36, "decl": -10.9, "note": "21 October 1600 (Gregorian); sunrise about 06:00 local solar time. Japanese sources give the old two-hour 'hours' (snake ~09-11, horse ~11-13), so every time here is approximate [wpja]."},
    "view": {"az": 0.25, "el": 0.85}, "unitScale": 1.0, "unitLabelDist": 9,
    "ground": {"season": "autumn", "relief": 55},
    "wind": 270,
    "strengthNote": "Strengths are the General Staff's estimates at three men per hundred koku, not musters; the General Staff itself said the true numbers are unknown [wpja]. Other totals: West 79,000-82,000 and East 70,000-89,000 [murdoch] [wpen]; a letter of the 20th gives Ieyasu about 50,000 and the West about 50,000 [wpja]. Western dead about 8,000 (32,600 in the 1713 Gunki taisei; 4-5,000 in the Konoe letter), Eastern dead unknown (about 4,000 often quoted) [wpja] [murdoch]. Per-moment losses are estimates following the narrative; after a rout, a contingent's strength counts the men still with the colours, not the survivors.",
    "method": "A traditional reconstruction. Units start on the camp sites marked on the battlefield [jinseki], checked against Fujii's 1926 situation map [fujii] (georeferenced on nine points, 227 m) and an Edo-compilation plot on the 1894 survey [hi] (114 m); advanced positions are read off the Fujii map. Those marked camps were fixed in the late Meiji era and the familiar layout descends from the 1893 General Staff map, which modern scholars criticise [shiramine] [shiramine2], so positions show where tradition puts the armies, to within a few hundred metres.",
    "notes": "The timetable follows the traditional account as defended by Kasaya (fighting from about 08:00, Kobayakawa about noon) [kasaya] [murdoch]. Since 2014 Shiramine, Takahashi and others have argued from letters written days after the battle that Kobayakawa turned as soon as the main lines met, about 10:00, and that the Western main body fought packed together at Yamanaka; that reading is given wherever it applies [shiramine] [takahashi] [turnbull]. Contingents of a few hundred men (Oda Nobutaka, Kawajiri Hidenaga, Ishikawa Sadakiyo; Hachisuka with Ikeda) are not drawn separately. The streams are shallow and treated as fordable. The Ikedera and Jūkujo ponds are shown as on the 1926 map; whether they had their modern size in 1600 is unknown. No historical-map overlay is offered. Per-moment losses are estimates.",
}

# ---- geography
osm = json.load(open("sources/osm_water.json"))["elements"]
def stitch(name):
    segs = [[(round(g["lat"], 5), round(g["lon"], 5)) for g in e["geometry"]] for e in osm if e["tags"].get("name") == name]
    line = segs.pop(0)
    while segs:
        for i, s in enumerate(segs):
            if s[0] == line[-1]: line += s[1:]; break
            if s[-1] == line[0]: line = s[:-1] + line; break
        else: break
        segs.pop(i)
    return line[::3] + [line[-1]]
B.water["rivers"] = [{"p": stitch("藤古川"), "w": 8, "ford": True}, {"p": stitch("黒血川"), "w": 4, "ford": True},
                     {"p": stitch("相川"), "w": 6, "ford": True}, {"p": stitch("梨木川"), "w": 3, "ford": True}]
cache = json.load(open("osm_cache.json"))
B.water["lakes"] = [[(round(g["lat"], 5), round(g["lon"], 5)) for g in e["geometry"]][::4] for e in cache if e.get("tags", {}).get("name") in ("池寺池", "十九女池")]
B.water["labels"] = {"Fujikogawa": (35.3560, 136.4585), "Aikawa": (35.3700, 136.4850), "Ikedera pond": (35.3690, 136.4535)}

for n, s in [("Sekigahara", 0.9), ("Koike", 0.5), ("Fujishita", 0.5), ("Matsuo", 0.5), ("Yamanaka", 0.6), ("Nojō", 0.6), ("Tarui", 0.8), ("Makita", 0.5), ("Kurihara", 0.5)]:
    B.place(n, size=s)
B.place("Koseki", wp(894, 640), size=0.5)
B.hill("Sasaoyama", "Sasaoyama"); B.hill("Tenmayama", "Tenmayama"); B.hill("Matsuoyama", "Matsuoyama summit")
B.hill("Momokubariyama", "Ieyasu first camp (Momokubariyama)"); B.hill("Nangū-san", "Nangūsan"); B.hill("Maruyama", "Maruyama")
B.hill("Kurihara-yama", (35.3390, 136.5370))
B.roads = [[(35.3586, 136.4300), "Yamanaka", (35.3600, 136.4545), "Fuwa barrier", "Sekigahara crossroads", "Ieyasu first camp (Momokubariyama)", "Nojō", "Tarui"],
           ["Sekigahara crossroads", "Koike", (35.3710, 136.4555), (35.3800, 136.4480)],
           ["Ise road junction", (35.3560, 136.4750), (35.3513, 136.4811), "Makita"]]

def U(uid, side, typ, name, men, w, keys, note, conf, cite, via=None):
    m0 = men[0] if isinstance(men, dict) else men
    u = B.unit(uid, side, typ, name, f"~{m0:,} men", w, note=note, conf=conf, men=men if isinstance(men, dict) else {0: men}, cite=cite)
    for ph, (pos, facing, form, *bend) in keys.items():
        u.at(ph, pos, facing, form, via=(via or {}).get(ph), bend=bend[0] if bend else 0)
    return u

R = (35.3700, 136.4440)  # rally / flight area in the hills west of Koseki, toward Ibuki
# ================= WEST
U("ishida", "w", "inf", "Ishida Mitsunari", {0: 2820, 3: 2700, 5: 2500, 7: 1200, 8: 300}, 260,
  {0: ((35.3716, 136.4590), 115, "L"), 3: ((35.3714, 136.4594), 115, "F"), 7: ((35.3770, 136.4535), 300, "R"), 8: ((35.3810, 136.4490), 315, "R")},
  "Mitsunari's own troops on Sasaoyama (his camp marker); 5,820 in the General Staff table, divided here between Ishida, Shima Sakon and Gamō Yorisato. Mitsunari fled into the Ibuki hills and was caught days later [jinseki] [wpja] [murdoch].", "medium", ["jinseki", "fujii", "wpja", "murdoch"])
U("shima", "w", "inf", "Shima Sakon (Ishida's vanguard)", {0: 1500, 3: 1100, 5: 900, 7: 300, 8: 80}, 200,
  {0: ((35.3708, 136.4602), 115, "L"), 2: (wp(1112, 550), 115, "F"), 3: ((35.3700, 136.4615), 115, "F"), 7: ((35.3745, 136.4560), 300, "R")},
  "Mitsunari's chief retainer, in front of the double palisade; shot down by Kuroda arquebusiers firing from the flank. 'Over 3,000' in Kuroda kafu [jinseki] [fujii] [wpen] [wpja].", "medium", ["jinseki", "fujii", "wpen", "wpja"])
U("gamo", "w", "inf", "Gamō Yorisato (Ishida's vanguard)", {0: 1500, 3: 1300, 5: 1100, 7: 300, 8: 100}, 200,
  {0: (wp(975, 495), 120, "L"), 3: ((35.3697, 136.4605), 120, "F"), 7: ((35.3750, 136.4545), 300, "R")},
  "Ishida's second vanguard commander beside Shima Sakon; killed in the collapse [jinseki] [fujii] [wpen].", "medium", ["jinseki", "fujii", "wpen"])
U("toyohisa", "w", "inf", "Shimazu Toyohisa (forward battle)", {0: 700, 7: 600, 8: 60}, 140,
  {0: (wp(907, 705), 100, "L"), 3: (wp(907, 705), 100, "F"), 8: ((35.3513, 136.4811), 140, "R")},
  "Yoshihiro's nephew led the Shimazu front line about 160 m to the right of Ishida's men; killed covering the breakout near Karasugashira, where a marker stands [shimazu] [jinseki] [wpen].", "medium", ["shimazu", "jinseki", "fujii", "wpen"],
  {8: [(35.3645, 136.4635), (35.3618, 136.4690), (35.3565, 136.4745)]})
U("yoshihiro", "w", "inf", "Shimazu Yoshihiro", {0: 1000, 7: 950, 8: 250}, 160,
  {0: ((35.3671, 136.4592), 100, "L"), 3: ((35.3671, 136.4592), 100, "F"), 8: ((35.3440, 136.4880), 140, "R")},
  "About 1,500-1,700 Satsuma men with Toyohisa's; they held their ground in the second line and fired on anyone who came near, then cut their way out to the east. Around 80 reached Satsuma [shimazu] [jinseki] [wpja] [wpen].", "medium", ["shimazu", "jinseki", "wpja", "wpen"],
  {8: [(35.3650, 136.4630), (35.3620, 136.4695), (35.3560, 136.4750), (35.3513, 136.4811)]})
U("konishi", "w", "inf", "Konishi Yukinaga", {0: 6000, 3: 5600, 5: 5000, 7: 2000, 8: 500}, 380,
  {0: ((35.3652, 136.4580), 105, "L"), 3: (wp(875, 875), 105, "F"), 7: ((35.3690, 136.4520), 290, "R"), 8: (R, 300, "R")},
  "On north Tenmayama (camp marker); 4,000-6,000. Murdoch has his men give way first under weight of numbers [jinseki] [fujii] [wpja] [murdoch].", "medium", ["jinseki", "fujii", "wpja", "murdoch"])
U("ukita", "w", "inf", "Ukita Hideie (main body)", {0: 9220, 3: 8800, 5: 8000, 7: 3000, 8: 800}, 480,
  {0: ((35.3626, 136.4552), 100, "L"), 3: ((35.3622, 136.4560), 100, "F"), 7: ((35.3650, 136.4470), 280, "R"), 8: (R, 290, "R")},
  "The largest Western division (17,220 in all) on south Tenmayama, including many new hires after the Ukita household split [jinseki] [wpja] [wpen].", "medium", ["jinseki", "fujii", "wpja", "wpen"])
U("akashi", "w", "inf", "Ukita vanguard (Akashi Takenori)", {0: 8000, 3: 7400, 5: 6800, 7: 2500, 8: 600}, 420,
  {0: (wp(875, 1040), 100, "L"), 2: (wp(875, 1040), 100, "F"), 3: ((35.3612, 136.4600), 95, "F"), 5: ((35.3615, 136.4585), 95, "F"), 7: ((35.3640, 136.4490), 280, "R"), 8: (R, 290, "R")},
  "Ukita's forward battle toward the Nakasendō; it pushed Fukushima back several hundred metres before the collapse [fujii] [murdoch] [wpen].", "medium", ["fujii", "murdoch", "wpen", "wpja"])
U("toda", "w", "inf", "Toda Katsushige", {0: 300, 3: 280, 5: 250, 6: 40}, 100,
  {0: (wp(695, 1140), 95, "L"), 3: ((35.3598, 136.4556), 95, "F"), 6: ((35.3605, 136.4520), 290, "R")},
  "Ōtani's ally, killed after the defection [fujii] [ishikawa] [wpen].", "medium", ["fujii", "ishikawa", "wpen"])
U("hiratsuka", "w", "inf", "Hiratsuka Tamehiro", {0: 360, 3: 330, 5: 300, 6: 40}, 100,
  {0: (wp(835, 1195), 95, "L"), 3: ((35.3592, 136.4572), 95, "F"), 6: ((35.3609, 136.4538), 290, "R")},
  "360 men on the Fujikawa plateau; fought off Kobayakawa's troops for a time and was killed [fujii] [ishikawa] [wpen].", "medium", ["fujii", "ishikawa", "wpen"])
U("otani", "w", "inf", "Ōtani Yoshitsugu", {0: 1500, 5: 1300, 6: 300, 7: 100}, 180,
  {0: ((35.3599, 136.4505), 140, "L"), 5: ((35.3590, 136.4508), 160, "F"), 6: ((35.3620, 136.4490), 320, "R")},
  "On the hill above Yamanaka (camp marker), part of his force facing Matsuoyama; he killed himself when his command broke [jinseki] [hi] [murdoch] [ishikawa].", "medium", ["jinseki", "hi", "fujii", "murdoch", "ishikawa"])
U("otani2", "w", "inf", "Ōtani Yoshikatsu and Kinoshita Yoritsugu", {0: 4250, 3: 4000, 5: 3700, 6: 1200, 7: 500}, 320,
  {0: ((35.3585, 136.4530), 110, "L"), 3: ((35.3585, 136.4542), 95, "F"), 5: ((35.3572, 136.4532), 160, "F"), 6: ((35.3612, 136.4505), 320, "R"), 7: ((35.3650, 136.4450), 300, "R")},
  "Ōtani's son and Kinoshita, at the front of the Ōtani command (3,500 and 750 in the General Staff table); the plot after Chōya kyūbun hōkō puts Ōtani's main body at Yamanaka [wpja] [hi] [fujii].", "low", ["wpja", "hi", "fujii"])
# ---- the defectors (shown as their own colour from the start; they were nominally Western)
for uid, name, men, px, lim in [("akaza", "Akaza Naoyasu", 600, (870, 1355), (35.3590, 136.4560)), ("ogawa", "Ogawa Suketada and Suketsugu", 2100, (920, 1415), (35.3584, 136.4549)),
                                 ("kutsuki", "Kutsuki Mototsuna", 600, (965, 1480), (35.3577, 136.4540)), ("wakisaka", "Wakisaka Yasuharu", 990, (1025, 1550), (35.3570, 136.4552))]:
    U(uid, "t", "inf", name, {0: men, 6: int(men * 0.92)}, max(100, men // 12),
      {0: (wp(*px), 45, "L"), 5: (wp(*px), 45, "L"), 6: (lim, 300, "F"), 7: ((lim[0] + 0.0010, lim[1] - 0.0020), 300, "F")},
      f"Posted along the foot of Matsuoyama on the Western side; already in touch with Tōdō Takatora, it turned on Hiratsuka and Toda after Kobayakawa [fujii] [wpen] [murdoch]{' [ishikawa]' if uid in ('ogawa', 'wakisaka') else ''}.",
      "medium" if uid == "wakisaka" else "low", ["fujii", "wpen", "murdoch", "hi"] + (["ishikawa", "jinseki"] if uid in ("ogawa", "wakisaka") else []))
U("kob_van", "t", "inf", "Kobayakawa vanguard", {0: 3000, 5: 2700, 6: 2400}, 260,
  {0: (wp(728, 1630), 350, "L"), 5: ((35.3570, 136.4512), 340, "F"), 6: ((35.3588, 136.4500), 340, "F"), 7: ((35.3615, 136.4495), 20, "F")},
  "The leading troops off Matsuoyama; driven back twice by Ōtani before the four contingents below joined in (Murdoch has a first wave of 600) [murdoch] [shimazu] [fujii]. Division of Kobayakawa's 15,675 between vanguard and main body is an estimate.", "low", ["murdoch", "shimazu", "fujii", "wpja"],
  {5: [(35.3540, 136.4530)]})
U("kobayakawa", "t", "inf", "Kobayakawa Hideaki", {0: 12675, 6: 12500, 7: 12300}, 420,
  {0: ((35.3480, 136.4543), 350, "L"), 5: ((35.3525, 136.4530), 350, "C"), 6: ((35.3560, 136.4525), 340, "F"), 7: ((35.3600, 136.4528), 30, "F")},
  "On Matsuoyama, the old castle site, flanking the Western right. 15,675 in the General Staff table, 8,000 in Murdoch. Whether he hesitated until noon or came down as soon as the lines met is the battle's central dispute [jinseki] [wpja] [murdoch] [ishikawa].", "medium", ["jinseki", "hi", "wpja", "murdoch", "ishikawa"])
# ---- Nangū-san and Kurihara-yama: present, never engaged
U("hidemoto", "w", "inf", "Mōri Hidemoto", {0: 13000}, 400,
  {0: ((35.3490, 136.5120), 340, "L"), 8: ((35.3440, 136.5250), 160, "C")},
  "High on Nangū-san, below the summit (Mōri forces 16,000 with Kikkawa); blocked by Kikkawa in front of him; withdrew after the battle [murdoch] [wpja] [wpen].", "low", ["murdoch", "wpja", "wpen"], {8: [(35.3470, 136.5180)]})
U("kikkawa", "w", "inf", "Kikkawa Hiroie", {0: 3000}, 220,
  {0: ((35.3572, 136.5125), 340, "L")},
  "At the north foot of Nangū-san; had given hostages and a promise that the Mōri would not fight on the 14th, and kept the force above him from coming down [wpja] [murdoch] [wpen].", "low", ["wpja", "murdoch", "wpen"])
U("ankokuji", "w", "inf", "Ankokuji Ekei", {0: 1800}, 160,
  {0: ((35.3545, 136.5262), 330, "L"), 8: ((35.3470, 136.5390), 160, "C")},
  "Near the Nangū shrine at the east foot of the mountain; did not fight and fled; executed in Kyoto on 1 November [wpja] [murdoch].", "low", ["wpja", "murdoch"])
U("natsuka", "w", "inf", "Natsuka Masaie", {0: 1500}, 150,
  {0: ((35.3505, 136.5292), 330, "L"), 8: ((35.3430, 136.5410), 160, "C")},
  "Toyotomi commissioner; urged an attack on the Tokugawa rear and could not make one; retreated toward Ōmi [wpja] [murdoch].", "low", ["wpja", "murdoch"])
U("chosokabe", "w", "inf", "Chōsokabe Morichika", {0: 6660}, 300,
  {0: ((35.3388, 136.5395), 330, "L"), 8: ((35.3310, 136.5440), 180, "C")},
  "On Kurihara-yama at the rear of the Nangū-san group; never engaged [murdoch] [wpja].", "low", ["murdoch", "wpja"])

# ================= EAST (column on the Nakasendō at dawn, then the positions on the Fujii map)
def EU(uid, name, men, w, col, dep, adv, more, note, conf, cite, typ="inf"):
    keys = {0: (col, 270, "C"), 1: (dep, 265, "L")}
    if adv: keys[3] = (adv, 255, "F")
    keys.update(more)
    return U(uid, "e", typ, name, men, w, keys, note, conf, cite)

EU("fukushima", "Fukushima Masanori", {0: 6000, 3: 5600, 5: 5300, 7: 5100}, 380, (35.3602, 136.4640), (35.3593, 136.4612), None,
   {2: ((35.3596, 136.4605), 285, "F"), 3: ((35.3598, 136.4630), 285, "F"), 5: (wp(960, 1090), 285, "F"), 7: ((35.3615, 136.4565), 290, "F")},
   "Head of the Eastern van; ran into Ukita's rearguard in the fog, opened fire on Ukita and was pushed back before the defection turned the fight [jinseki] [murdoch] [ishikawa].", "medium", ["jinseki", "fujii", "murdoch", "ishikawa", "wpen"])
EU("ii", "Ii Naomasa ('red devils')", {0: 3600, 3: 3450, 7: 3300, 8: 3200}, 220, (35.3637, 136.4760), (35.3642, 136.4688), wp(1085, 825),
   {2: ((35.3630, 136.4640), 250, "F"), 7: ((35.3660, 136.4605), 260, "F"), 8: ((35.3555, 136.4745), 150, "F")},
   "Ieyasu's field commander, in red armour; went ahead of Fukushima to open the battle, and was wounded by a Shimazu bullet in the pursuit [ishikawa] [wpen] [murdoch].", "medium", ["jinseki", "fujii", "ishikawa", "wpen", "murdoch"])
EU("tadayoshi", "Matsudaira Tadayoshi", {0: 3000, 3: 2850, 7: 2750}, 200, (35.3633, 136.4790), (35.3634, 136.4686), wp(1040, 875),
   {2: ((35.3624, 136.4640), 250, "F")},
   "Ieyasu's fourth son, with his father-in-law Ii; wounded in the fighting [jinseki] [wpja] [murdoch].", "medium", ["jinseki", "fujii", "wpja", "murdoch"])
EU("honda", "Honda Tadakatsu", {0: 500, 8: 450}, 100, (35.3640, 136.4830), (35.3602, 136.4730), None,
   {5: ((35.3612, 136.4660), 270, "L"), 7: ((35.3612, 136.4620), 270, "F"), 8: ((35.3585, 136.4720), 330, "F")},
   "Only about 500 men; moved up through the centre in the late fighting and met the Shimazu as they broke out [jinseki] [wpja] [wpen].", "medium", ["jinseki", "fujii", "wpja", "wpen"])
EU("todo", "Tōdō Takatora", {0: 2490, 3: 2300, 6: 2150}, 200, (35.3615, 136.4705), (35.3595, 136.4645), wp(905, 1175),
   {6: ((35.3592, 136.4560), 260, "F"), 7: ((35.3597, 136.4540), 270, "F")},
   "Faced Ōtani's front; he had arranged the defection of Wakisaka, Kutsuki, Ogawa and Akaza [jinseki] [wpen] [murdoch].", "medium", ["jinseki", "fujii", "wpen", "murdoch"])
EU("kyogoku", "Kyōgoku Takatomo", {0: 3000, 3: 2800, 6: 2700}, 220, (35.3610, 136.4722), (35.3586, 136.4650), wp(905, 1240),
   {6: ((35.3581, 136.4560), 260, "F"), 7: ((35.3586, 136.4530), 270, "F")},
   "Beside Tōdō against Ōtani's command [jinseki] [murdoch] [wpen].", "medium", ["jinseki", "fujii", "murdoch", "wpen"])
EU("terazawa", "Terazawa Hirotaka", {0: 2400, 3: 2300}, 180, (35.3620, 136.4740), (35.3607, 136.4686), (35.3605, 136.4618),
   {7: ((35.3610, 136.4585), 270, "F")},
   "Placed behind Fukushima in the traditional order of battle; his presence is not confirmed by primary sources [shiramine2] [murdoch].", "low", ["shiramine2", "murdoch", "fujii"])
EU("kuroda", "Kuroda Nagamasa", {0: 5400, 3: 5100, 7: 4900}, 300, (35.3650, 136.4800), (35.3688, 136.4697), wp(1215, 522),
   {7: ((35.3712, 136.4612), 260, "F")},
   "On Maruyama, the Eastern right; his arquebusiers, sent round on the high ground, shot down Shima Sakon. He had negotiated Kobayakawa's defection [jinseki] [fujii] [wpen] [murdoch].", "medium", ["jinseki", "fujii", "wpen", "murdoch"])
EU("takenaka", "Takenaka Shigekado", {0: 200, 3: 190}, 80, (35.3655, 136.4810), (35.3697, 136.4705), wp(1215, 480),
   {7: ((35.3720, 136.4615), 260, "F")},
   "Local lord of Bodaiyama, with Kuroda on Maruyama; missing from the 1893 staff map [jinseki] [fujii] [shiramine2].", "medium", ["jinseki", "fujii", "shiramine2"])
EU("hosokawa", "Hosokawa Tadaoki", {0: 5100, 3: 4850, 7: 4700}, 300, (35.3645, 136.4820), (35.3683, 136.4679), wp(1200, 580),
   {7: ((35.3702, 136.4610), 260, "F")},
   "Attacked Ishida's front from the south-east (camp marker) [jinseki] [fujii] [murdoch].", "medium", ["jinseki", "fujii", "murdoch", "wpja"])
EU("kato", "Katō Yoshiaki", {0: 3000, 3: 2850}, 220, (35.3642, 136.4840), (35.3677, 136.4692), wp(1180, 622),
   {7: ((35.3695, 136.4605), 260, "F")},
   "In the line against Ishida [fujii] [murdoch].", "low", ["fujii", "murdoch", "wpja"])
EU("tsutsui", "Tsutsui Sadatsugu", {0: 2850, 3: 2750}, 200, (35.3639, 136.4860), (35.3671, 136.4683), (35.3681, 136.4650),
   {7: ((35.3686, 136.4625), 260, "F")},
   "Second line behind Katō in the traditional order [fujii] [wpja].", "low", ["fujii", "wpja"])
EU("tanaka", "Tanaka Yoshimasa", {0: 3000, 3: 2850, 7: 2750}, 220, (35.3636, 136.4880), (35.3652, 136.4663), wp(1095, 695),
   {7: ((35.3680, 136.4580), 260, "F")},
   "Attacked Ishida; his men caught Mitsunari in the hills days later [jinseki] [fujii] [wpja].", "medium", ["jinseki", "fujii", "wpja"])
EU("ikoma", "Ikoma Kazumasa", {0: 1830, 3: 1750}, 150, (35.3634, 136.4900), (35.3657, 136.4728), wp(1120, 762),
   {}, "With the attack on Ishida's left [fujii] [wpja].", "low", ["fujii", "wpja"])
EU("kanamori", "Kanamori Nagachika", {0: 1140, 3: 1080}, 120, (35.3631, 136.4920), (35.3666, 136.4728), wp(1145, 660),
   {}, "An old general of Nobunaga's, in the centre [fujii] [wpja].", "low", ["fujii", "wpja"])
EU("oda", "Oda Urakusai (Nagamasu)", {0: 450, 3: 420, 6: 400}, 80, (35.3629, 136.4940), (35.3675, 136.4727), wp(900, 980),
   {6: ((35.3602, 136.4565), 250, "F")}, "Nobunaga's younger brother; with Honda's men he killed Toda Katsushige's forces in the late fighting [fujii] [wpen].", "low", ["fujii", "wpen"])
EU("furuta", "Furuta Shigenari (Oribe)", {0: 1020, 3: 980}, 100, (35.3627, 136.4960), (35.3684, 136.4727), wp(960, 900),
   {}, "The tea master; the 1893 map wrongly gives Furuta Shigekatsu, who was then besieged in Matsusaka [shiramine2] [fujii].", "low", ["shiramine2", "fujii", "wpen"])
U("ieyasu", "e", "gd", "Tokugawa Ieyasu (household troops)", {0: 30000, 7: 29800}, 600,
  {0: ((35.3650, 136.4880), 270, "L"), 4: (wp(1926, 955), 270, "L"), 7: ((35.3657, 136.4705), 270, "L")},
  "About 30,000 Tokugawa retainers under Ieyasu, first on Momokubariyama, then forward to near the village; barely engaged [jinseki] [fujii] [hi] [wpja].", "medium", ["jinseki", "fujii", "hi", "wpja"])
for uid, name, men, pos, f, note in [("ikeda", "Ikeda Terumasa", 4500, (35.3622, 136.5110), 190, "Watching Nangū-san at its north-west foot"),
                                     ("asano", "Asano Yoshinaga", 6510, (35.3700, 136.5150), 200, "At Tarui (camp marker by the milestone mound), facing Nangū-san"),
                                     ("yamauchi", "Yamauchi Kazutoyo", 2058, (35.3669, 136.4925), 170, "Behind Ieyasu on the Nakasendō (camp marker), guarding the rear"),
                                     ("arima", "Arima Toyouji", 900, (35.3652, 136.5010), 175, "With Yamauchi on the road behind Ieyasu")]:
    U(uid, "e", "inf", name, {0: men}, max(120, men // 15), {0: (pos, f, "L")}, f"{note}; never engaged [murdoch] [wpja] [jinseki].", "low" if uid in ("ikeda", "arima") else "medium", ["murdoch", "wpja", "jinseki"])

B.commander("ieyasu_hq", "e", "Tokugawa Ieyasu", {0: "Ieyasu first camp (Momokubariyama)", 4: wp(1926, 955), 7: wp(1360, 790)},
            "First on Momokubariyama; the traditional account moves him forward in the late morning, and the head inspection was held on the ground marked as his last camp [jinseki] [fujii] [hi].")
B.commander("ishida_hq", "w", "Ishida Mitsunari", {0: "Ishida camp (Sasaoyama)", 7: (35.3780, 136.4525)}, "Directed the Western army from Sasaoyama [jinseki].")
B.commander("kob_hq", "t", "Kobayakawa Hideaki", {0: "Kobayakawa camp (Matsuoyama)"}, "Watched from the Matsuoyama fort [jinseki].")

# ================= PHASES
FOG0 = (35.3640, 136.4650)
B.phase("06:30", "Fog", "Two armies in the fog",
  "After a night march from Ōgaki in pouring rain, the Western divisions stand across the Sekigahara basin: Ishida on Sasaoyama, the Shimazu by Koike, Konishi and Ukita on Tenmayama, Ōtani's command above Yamanaka, Kobayakawa on Matsuoyama to the south [murdoch] [jinseki] [ishikawa]. A second Western force of some 30,000 sits nine kilometres back on Nangū-san, behind the Eastern line of march [murdoch]. The Eastern van, marching from Akasaka since 03:00, comes up the Nakasendō in fog so thick that Fukushima's leading troops run into Ukita's rearguard [murdoch]. Ieyasu halts on Momokubariyama [jinseki].",
  ("Blocking a pass", "An army holding the hills on both sides of a road forces the enemy to attack uphill into a funnel; it works only if every contingent fights.", "strongpoint-defence"), FOG0, 7.5,
  arrows=[B.arrow("e", "move", (35.3655, 136.4930), (35.3632, 136.4760), (35.3605, 136.4655))],
  events=[(wp(960, 1090), "Fukushima's van stumbles into Ukita's rearguard in the fog [murdoch]", ["murdoch"]), ((35.3500, 136.5150), "30,000 Westerners on Nangū-san, behind the Eastern army [murdoch]", ["murdoch"])],
  conf="low", cite=["murdoch", "jinseki", "ishikawa", "fujii", "hi"], fog=0.95,
  debate="Where the Western army stood is disputed. The markers on the field were fixed in the Meiji era; Shiramine, Takahashi and Noji deny that Ishida was on Sasaoyama and put the Western main body packed together at Yamanaka, the place named in the earliest letters [shiramine] [turnbull].")
B.phase("07:30", "Deployment", "The East deploys blind",
  "The Eastern van turns off the road into line: Kuroda and Takenaka on Maruyama facing Ishida; Hosokawa, Katō, Tsutsui, Tanaka, Ikoma, Kanamori, Oda and Furuta in an arc to their south; Ii and Matsudaira Tadayoshi by the village; Fukushima south of the road facing Ukita; Tōdō and Kyōgoku facing Ōtani [murdoch] [fujii] [hi]. Ikeda, Asano, Yamauchi and Arima stay back on the road to watch Nangū-san [murdoch] [wpja].",
  ("A threat to the rear", "Ieyasu marched past an undefeated enemy force on his flank, trusting secret promises that it would not move.", "rear-threat"), FOG0, 6.0,
  arrows=[B.arrow("e", "move", (35.3650, 136.4800), (35.3688, 136.4697)), B.arrow("e", "move", (35.3615, 136.4705), (35.3595, 136.4645))],
  events=[((35.3688, 136.4697), "Kuroda and Takenaka on Maruyama [jinseki]", ["jinseki"])],
  conf="medium", cite=["murdoch", "fujii", "hi", "jinseki", "wpja"], fog=0.85)
B.phase("08:00", "First shots", "Ii Naomasa opens the battle",
  "Ii Naomasa, Ieyasu's field commander, with Matsudaira Tadayoshi, goes forward past Fukushima's front with a small party (thirty spearmen in one account, about 300 men in Kuroda kafu) and draws first blood; Fukushima's arquebusiers open fire on Ukita [murdoch] [wpja] [wpen]. Kasaya reads it as a reconnaissance in the fog that let a Tokugawa house strike first without breaking the ban on going ahead [kasaya].",
  ("Frontal assault", "With no room to manoeuvre in the basin, the East attacked straight into the Western line along its whole length.", "frontal-assault"), (35.3620, 136.4615), 3.2,
  arrows=[B.arrow("e", "charge", (35.3642, 136.4688), (35.3630, 136.4640), (35.3618, 136.4610)), B.arrow("e", "fire", (35.3596, 136.4605), (35.3612, 136.4585))],
  events=[((35.3630, 136.4640), "Ii's party goes ahead of Fukushima [wpja]", ["wpja"])],
  conf="medium", cite=["murdoch", "wpja", "wpen", "kasaya", "ishikawa"], fog=0.6,
  debate="When did the fighting start? Edo accounts say the hour of the dragon (~08:00) and one Shimazu memoir says 'at dawn'; the letter of the 17th says Ieyasu engaged at the hour of the snake (~10:00). Kasaya reconciles them: skirmishing from 08:00, the general attack when the fog lifted about 10:00 [kasaya] [ishikawa] [shimazu].")
B.phase("09:00", "General action", "Arquebus and spear along the whole line",
  "The battle becomes general. Kuroda, Takenaka, Hosokawa, Katō, Tanaka and Ikoma attack Ishida's palisaded front; Shima Sakon is shot down by Kuroda arquebusiers firing from the flank [wpen] [murdoch]. Ukita's men push Fukushima back several hundred metres; Tōdō and Kyōgoku fight Hiratsuka, Toda and Ōtani's front [murdoch]. The Shimazu hold their ground and fire on anyone who comes near [shimazu] [wpja].",
  ("Combined arms", "Massed arquebuses behind palisades, long spears and mounted samurai fought together; fire from a flank broke Ishida's vanguard.", "combined-arms"), (35.3650, 136.4610), 3.6,
  arrows=[B.arrow("e", "fire", (35.3720, 136.4640), (35.3702, 136.4615)), B.arrow("e", "charge", (35.3688, 136.4645), (35.3700, 136.4618)), B.arrow("w", "charge", (35.3612, 136.4590), (35.3598, 136.4625)),
          B.arrow("e", "charge", (35.3594, 136.4600), (35.3592, 136.4575)), B.arrow("w", "fire", (35.3671, 136.4600), (35.3665, 136.4625))],
  events=[((35.3700, 136.4615), "Shima Sakon is shot down [wpen]", ["wpen"]), ((35.3598, 136.4630), "Ukita drives Fukushima back [murdoch]", ["murdoch"])],
  conf="medium", cite=["wpen", "murdoch", "shimazu", "wpja", "fujii"], fog=0.3)
B.phase("10:30", "Deadlock", "The Mōri do not come",
  "The fog has lifted [kasaya] [shimazu]. The line sways back and forth [murdoch]. Ishida signals for Kobayakawa and the Nangū-san force to attack; neither moves [murdoch]. Kikkawa Hiroie, who had pledged on the 14th that the Mōri would not fight, sits at the foot of Nangū-san and blocks the way for Mōri Hidemoto and the contingents behind him [wpja] [wpen] [murdoch]. Ieyasu moves his headquarters forward from Momokubariyama toward the village [fujii] [hi].",
  ("A reserve that never comes", "Half the Western army stood idle on the hills; a reserve only matters if it can and will be committed.", "reserve-commitment"), (35.3580, 136.4880), 9.0,
  arrows=[B.arrow("e", "move", (35.3650, 136.4880), (35.3649, 136.4784))],
  events=[((35.3572, 136.5125), "Kikkawa blocks the road down from Nangū-san [wpja]", ["wpja"]), ((35.3716, 136.4590), "Ishida signals for Kobayakawa and the Mōri [murdoch]", ["murdoch"])],
  conf="low", cite=["kasaya", "shimazu", "murdoch", "wpja", "wpen", "fujii", "hi"],
  debate="The tale that Kikkawa held Mōri Hidemoto back by claiming he was eating lunch is a later anecdote, and the Kikkawa family later reshaped the record of his role [wpja].")
B.phase("12:00", "The defection", "Kobayakawa comes down",
  "Kobayakawa Hideaki's troops descend Matsuoyama onto Ōtani's flank. Ōtani, who had kept part of his force facing the hill, drives them back twice [murdoch] [wpen]. A Shimazu memoir describes Ōtani and the Eastern troops pushing each other back and forth 'two or three times' before Kobayakawa came 'straight down from the hill' [shimazu].",
  ("Pre-arranged defection", "Kobayakawa had been in contact with Kuroda and Ieyasu for weeks; the question was only when he would act.", "defection"), (35.3560, 136.4540), 3.0,
  arrows=[B.arrow("t", "charge", (35.3500, 136.4540), (35.3540, 136.4530), (35.3575, 136.4512)), B.arrow("t", "move", (35.3480, 136.4543), (35.3525, 136.4530))],
  events=[((35.3575, 136.4512), "Kobayakawa's men strike Ōtani's flank; twice thrown back [murdoch]", ["murdoch"])],
  conf="medium", cite=["murdoch", "wpen", "shimazu", "ishikawa"],
  debate="The hour is the battle's great dispute. Traditional (General Staff, Murdoch, Kasaya): about noon, after hours of fighting; Kasaya cites a Shimazu diary ('several hours') and a Shimazu memoir ('the hour of the horse'). Revisionist (Shiramine, Takahashi): the letter of the 17th has Kobayakawa turn as the lines met about 10:00, and Ieyasu wrote that all was over by noon. The famous 'probing shots' Ieyasu is said to have fired at Matsuoyama first appear in print in 1663 and are rejected by most scholars; Kasaya keeps a version [kasaya] [ishikawa] [ieyasu] [shiramine] [takahashi] [wpja].")
B.phase("12:30", "The four turn", "Ōtani's command is destroyed",
  "Wakisaka, Kutsuki, Ogawa and Akaza, posted below Matsuoyama and already in contact with Tōdō Takatora, turn on Hiratsuka and Toda [wpen] [murdoch] [ishikawa]. Struck from three sides, Ōtani's command breaks; Ōtani kills himself, and Hiratsuka and Toda are killed [ishikawa] [wpen].",
  ("Envelopment", "A flank that turns against its own army collapses the line from the end.", "envelopment"), (35.3585, 136.4540), 2.6,
  arrows=[B.arrow("t", "charge", (35.3560, 136.4580), (35.3585, 136.4560)), B.arrow("t", "charge", (35.3560, 136.4525), (35.3592, 136.4510)), B.arrow("e", "charge", (35.3592, 136.4578), (35.3600, 136.4550))],
  events=[((35.3605, 136.4500), "Ōtani Yoshitsugu kills himself [ishikawa] [wpen]", ["ishikawa", "wpen"]), ((35.3606, 136.4538), "Hiratsuka and Toda killed [ishikawa]", ["ishikawa"])],
  conf="medium", cite=["wpen", "murdoch", "ishikawa", "shimazu"])
B.phase("13:00", "Collapse", "The Western line goes down like dominoes",
  "With its right gone, the Western line unravels: Konishi's men give way, Kobayakawa's troops swing round Ukita's flank and the great division breaks; Ishida's men, who had fought hard, go next [murdoch] [wpja]. Shimazu memoirs describe Ukita's fugitives streaming past a pond toward the Shimazu ranks, who threatened to cut down even friends who broke into them [shimazu]. Mitsunari escapes into the Ibuki hills [wpja].",
  ("Pursuit", "Once a line breaks, the winner's pursuit does most of the killing.", "pursuit"), (35.3640, 136.4580), 3.4,
  arrows=[B.arrow("w", "retreat", (35.3622, 136.4560), (35.3650, 136.4470)), B.arrow("w", "retreat", (35.3714, 136.4594), (35.3770, 136.4535)), B.arrow("t", "charge", (35.3560, 136.4525), (35.3600, 136.4528)),
          B.arrow("e", "charge", (35.3615, 136.4590), (35.3620, 136.4560)), B.arrow("e", "charge", (35.3700, 136.4625), (35.3712, 136.4605))],
  events=[((35.3740, 136.4560), "Ishida's army breaks; Mitsunari flees toward Ibuki [wpja]", ["wpja"]), ((35.3678, 136.4549), "Ukita's fugitives flee past the pond [shimazu]", ["shimazu"])],
  conf="medium", cite=["murdoch", "wpja", "shimazu"],
  debate="Shiramine reads the Shimazu memoirs as showing the Western main body crushed 'in a moment' by the Eastern frontal attack, before Kobayakawa's men reached it [shiramine]; the traditional account has the defection roll up the line from the south [murdoch].")
B.phase("14:00", "The breakout", "The Shimazu charge through the enemy",
  "Surrounded, Shimazu Yoshihiro's men charge not west but east, through the Eastern army, past Ieyasu's position and down the Ise road. Toyohisa is killed covering them near Karasugashira; Ii Naomasa, pursuing, is wounded by a Shimazu bullet; Honda's men meet them on the way [wpen] [wpja] [murdoch]. Of perhaps 1,500, about 80 reach Satsuma [wpja]. On Nangū-san the Mōri, Ankokuji, Natsuka and Chōsokabe march away without having fought [murdoch] [wpja]. About 8,000 Westerners lie dead [murdoch].",
  ("Breakout", "Ieyasu's camp was the last place the East expected an attack; the Shimazu used rearguards that stood and died so the rest could get clear.", "breakout"), (35.3560, 136.4750), 4.8,
  arrows=[B.arrow("w", "retreat", (35.3670, 136.4598), (35.3645, 136.4635), (35.3618, 136.4692), (35.3565, 136.4745), (35.3513, 136.4811), (35.3440, 136.4880)),
          B.arrow("e", "charge", (35.3640, 136.4620), (35.3555, 136.4745)), B.arrow("w", "retreat", (35.3490, 136.5120), (35.3440, 136.5250))],
  events=[((35.3513, 136.4811), "Shimazu Toyohisa killed near Karasugashira [jinseki] [wpen]", ["jinseki", "wpen"]), ((35.3555, 136.4745), "Ii Naomasa wounded in the pursuit [wpen]", ["wpen"])],
  conf="medium", cite=["wpen", "wpja", "murdoch", "jinseki", "shimazu"],
  debate="When the battle ended is uncertain: by noon in Ieyasu's letter and in Sekigahara shimatsuki, about 14:00 in the 1713 Gunki taisei; revisionists think the whole battle took about two hours [ieyasu] [wpja] [wpen].")

B.export()
