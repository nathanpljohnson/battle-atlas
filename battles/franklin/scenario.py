"""Franklin, Tennessee, 30 November 1864.

Brigade-level reconstruction. Positions are read off Hal Jespersen's two Franklin maps
(georeferenced: jesp1600 by five control points, RMSE 16 m; the 4:30-dark sheet by its
scale bar from the Carter House), checked against the 1864 "Field works at Franklin" survey
and Cox's 1897 monograph. See brief.md.
"""
import json, math, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "..", "tools"))
os.chdir(HERE)
from battlekit import Battle
from georef import Georef

_g = Georef(HERE)("jesp1600")
def j(tx, ty):  # thumbnail pixel on the 4-4:30 sheet (1136 px wide) -> lat, lon
    return _g(tx * 2400 / 1136, ty * 2400 / 1136)

_CH = (35.91703, -86.87353)
def k(tx, ty):  # thumbnail pixel on the 4:30-dark sheet (1286 px wide), north-up, 1.266 m/px from the Carter House
    e, s = (tx - 631) * 1.266, (ty - 662) * 1.266
    return (_CH[0] - s / 111200, _CH[1] + e / (111200 * math.cos(math.radians(_CH[0]))))

B = Battle("franklin", HERE)

B.source("cox", "Jacob D. Cox, The Battle of Franklin, Tennessee, November 30, 1864 (New York: Scribner, 1897)", "https://archive.org/details/battleoffranklin00coxj", "commander of the Union line; dispositions, timings, sunset, strengths (pp. 209-211) and losses (pp. 211-216) from the Official Records", "primary")
B.source("or", "War of the Rebellion: Official Records, Ser. I, vol. 45, pt 1 (Schofield, Thomas, Hood reports)", "https://archive.org/details/warofrebellion451unit", "full text (archive.org warofrebellion451unit): Forrest p. 754, Lee pp. 687-688, Stanley pp. 115-116, Hatch pp. 576-577, Cockerill p. 432, losses pp. 343-344", "official-history")
B.source("hood", "John B. Hood, Advance and Retreat (New Orleans, 1880), pp. 292-295", "https://archive.org/details/advanceretreatpe00hood", "the Confederate commander's account: 4 p.m. advance, artillery withheld, Johnson's division before dark, fighting until 9 p.m.", "primary")
B.source("wp", "Wikipedia, 'Battle of Franklin' (after Jacobson & Rupp 2006, Sword 1992, McDonough & Connelly 1983, Eicher 2001)", "https://en.wikipedia.org/wiki/Battle_of_Franklin", "brigade-level sequence of the breakthrough, Opdycke, Stewart's attacks, Bate, Johnson and the cavalry fight", "reference")
B.source("abt", "American Battlefield Trust, 'Franklin'", "https://www.battlefields.org/learn/civil-war/battles/franklin", "4 p.m. step-off, about 20,000 attackers, Wagner's collapse, Opdycke, the Hughes's Ford fight, losses 2,326 and 6,252", "reference")
B.source("tnenc", "Patrick Craddock, 'Battle of Franklin', Tennessee Encyclopedia (Tennessee Historical Society, 2017)", "https://tennesseeencyclopedia.net/entries/battle-of-franklin/", "alternative 4:30 step-off and strength figures; fighting to about 10 p.m.; officer losses", "reference")
B.source("jesp", "Hal Jespersen, 'Battle of Franklin: Hood's approach, 4-4:30 p.m.' and '4:30 p.m.-dark' (CC BY 3.0)", "https://commons.wikimedia.org/wiki/File:Franklin_battle_1630.png", "modern brigade-position maps after Jacobson; georeferenced, RMSE 16 m", "staff-map")
B.source("fw", "'Field works at Franklin, Tenn., occupied by the 23d and 4th corps during engagement of Nov. 30th 1864' (Library of Congress 2003627083)", "https://www.loc.gov/item/2003627083/", "1864 survey of the works, Fort Granger, Winstead Hill and the Confederate deployment; south-up", "period-map")
B.source("jacobson", "Eric A. Jacobson with Richard A. Rupp, For Cause & for Country: A Study of the Affair at Spring Hill and the Battle of Franklin (2006)", None, "the standard modern study; used through the Jespersen maps and Wikipedia, not read directly", "scholarly")
B.source("data", "AWS Terrain Tiles; OpenStreetMap (Harpeth River, landmarks)", "https://registry.opendata.aws/terrain-tiles/", "modern elevation, river course and place coordinates", "data")

B.meta = {
    "title": "Franklin", "year": "1864", "era": "industrial", "war": "American Civil War",
    "eyebrow": "30 November 1864 · Tennessee · American Civil War",
    "subtitle": "Hood hurls the Army of Tennessee across two miles of open ground at Schofield's entrenched arc south of the Harpeth.",
    "sides": {
        "us": {"name": "Union", "top": "#2b3f6e", "side": "#1b2a4b", "mark": "#eef0f4", "arrow": "#4c74c9", "flag": "#2b3f6e"},
        "cs": {"name": "Confederate", "top": "#8d8a80", "side": "#5f5c55", "mark": "#2a2622", "arrow": "#c4533d", "flag": "#9a3a2c", "chart": "#8d8a80"},
    },
    "belligerents": [
        {"name": "Army of the Ohio, with the IV Corps and Wilson's cavalry", "short": "Union", "commander": "John M. Schofield", "sides": ["us"], "code": "letters"},
        {"name": "Army of Tennessee", "short": "Confederates", "commander": "John Bell Hood", "sides": ["cs"], "code": "numbers"},
    ],
    "forces": {
        "start": [{"label": "Union", "n": 29234, "segs": [["us", 1]]}, {"label": "Confederates", "n": 27000, "segs": [["cs", 1]]}],
        "end": [{"label": "Union", "n": 2326, "segs": [["us", 1]]}, {"label": "Confederates", "n": 6252, "segs": [["cs", 1]]}],
    },
    "sun": {"lat": 35.92, "decl": -21.6, "note": "Professor J. G. Porter computed sunset at Franklin that day as 4:59 p.m. local time; the low western hills made it look earlier [cox]."},
    "wind": 200, "view": {"az": 0.0, "el": 0.85}, "unitScale": 1.1, "unitLabelDist": 6,
    "ground": {"season": "autumn", "relief": 70},
    "days": {"1": "30 November 1864"},
    "strengthNote": "Union: 29,234 of all arms, including about 5,500 cavalry [cox]. Confederate: 27,000-31,000 in the army [wp]; about 20,000 in the main assault [abt] [wp] (Cox and the Tennessee Encyclopedia give up to 24,000 [cox] [tnenc]), plus Johnson's division after dark. Union losses 2,326 [cox] [or]. Confederate losses 6,252 as counted when Franklin was reoccupied [cox] [or]; Hood reported 4,500 [hood]. Brigade strengths are estimates (only Cockrell's 696 is sourced [cox]), and losses per moment are an allocation of the sourced totals following the narrative.",
    "method": "Brigade positions are read off two modern maps based on Jacobson's study and georeferenced against the Carter House, Lotz House, Carnton, Fort Granger and the town square (16 m error) [jesp]. The Union works are checked against the 1864 field-works survey [fw] and Cox's description [cox]. Positions after dark, and the exact frontages of the compressed Confederate brigades at the works, are approximate.",
    "notes": "The Union earthworks themselves are not drawn: the units in the works mark the line. The terrain is modern; quarry and pond changes away from the field were masked or left as noted in terrain_config.json. No historical-map overlay is offered. Brigade strengths and losses per moment are estimates; see brief.md.",
}

B.place("Franklin", size=1.6); B.place("Carter House", size=0.5); B.place("Lotz House", size=0.4)
B.place("Carnton", size=0.6); B.place("Cotton gin", k(704, 750), size=0.35)
B.place("Everbright", j(380, 600), size=0.4); B.place("Merrill House", j(462, 768), size=0.4)
B.hill("Winstead Hill", B.geo["Winstead Hill"]); B.hill("Privet Knob", j(405, 742)); B.hill("Fort Granger", B.geo["Fort Granger"])
B.place("Hughes's Ford", j(1050, 950), size=0.4); B.place("McGavock's Ford", j(830, 690), size=0.4)

B.water["rivers"] = [{"p": [tuple(p) for p in json.load(open("harpeth.json"))], "w": 5}]
B.water["labels"] = {"Harpeth River": j(770, 560)}
B.crossing("Railroad bridge", j(700, 292)); B.crossing("Wagon and pontoon bridges", j(610, 270))
B.crossing("McGavock's Ford", j(830, 690)); B.crossing("Hughes's Ford", j(1050, 950))
B.roads = [
    [j(430, 1400), j(470, 960), j(495, 700), j(510, 540), j(560, 400), "Franklin"],                  # Columbia Pike
    [j(1100, 860), j(990, 830), j(800, 705), j(660, 480), "Franklin"],                               # Lewisburg Pike
    [j(60, 760), j(240, 690), j(380, 520), j(470, 420), "Franklin"],                                 # Carter's Creek Pike
    ["Franklin", j(620, 280), j(700, 150), j(760, 20)],                                              # Nashville Pike
    [j(640, 470), j(800, 500), j(1130, 540)],                                                        # Murfreesboro Road
]
B.woods = [[*k(470, 720), 70, 50], [*j(700, 740), 220, 140], [*j(560, 470), 110, 70]]

def U(uid, side, typ, name, strength, frontage, keys, note, conf, men, cite, via=None):
    u = B.unit(uid, side, typ, name, strength, frontage, note=note, conf=conf, men=men, cite=cite)
    for phase, (pos, facing, form, *bend) in keys.items():
        u.at(phase, pos, facing, form, via=(via or {}).get(phase), bend=bend[0] if bend else 0)
    return u

NORTH = j(640, 210)  # across the Harpeth after the withdrawal

# ---- Union: Wagner's division (IV Corps): two brigades forward, Opdycke in reserve
U("lane", "us", "inf", "Lane's brigade (Wagner)", "~1,500 infantry", 450,
  {0: (j(432, 598), 200, "F", 0.08), 2: (k(590, 560), 180, "R"), 3: (k(650, 470), 180, "R"), 5: (k(700, 430), 180, "L")},
  "West of the pike in Wagner's advanced position; Stanley says Lane, on the right, re-entered the works several hundred yards west of the pike [or] [wp] [cox].", "high", {0: 1500, 2: 980}, ["wp", "cox", "jesp", "or"], {2: [k(560, 680)]})
U("conrad", "us", "inf", "Conrad's brigade (Wagner)", "~1,500 infantry", 450,
  {0: (j(530, 640), 170, "F", 0.06), 2: (k(690, 560), 180, "R"), 3: (k(700, 480), 180, "R"), 5: (k(740, 440), 180, "L")},
  "East of the pike in the advanced position; most of Wagner's 670 missing came from Lane and Conrad [cox].", "high", {0: 1500, 2: 940}, ["wp", "cox", "jesp"], {2: [k(660, 720)]})
U("opdycke", "us", "inf", "Opdycke's brigade (Wagner)", "~2,000 infantry", 330,
  {0: (k(632, 460), 0, "C"), 3: (k(632, 520), 180, "L"), 4: (k(625, 650), 180, "F", -0.05), 8: (j(560, 170), 0, "C")},
  "Refused to stop in the advanced position and halted about 200 yards north of the Carter House; its charge sealed the breach [wp] [abt].", "high", {0: 2000, 4: 1880, 6: 1840}, ["wp", "abt", "jesp", "cox"], {8: [j(560, 400), j(610, 270)]})
# ---- Ruger's division (XXIII Corps), west of the pike
U("strickland", "us", "inf", "Strickland's brigade (Ruger)", "~1,700 infantry", 420,
  {0: (k(505, 575), 225, "F", -0.05), 3: (k(560, 520), 225, "R"), 4: (k(505, 575), 225, "F", -0.05), 8: (j(600, 160), 0, "C")},
  "From the pike to Locust Grove; its front regiments were driven back to the retrenchment at the Carter House and recovered with Opdycke [wp] [cox].", "high", {0: 1700, 3: 1450, 4: 1360, 6: 1350}, ["jesp", "wp", "cox"], {8: [j(540, 400), j(610, 270)]})
U("moore", "us", "inf", "Moore's brigade (Ruger)", "~1,600 infantry", 450,
  {0: (k(360, 420), 225, "F", -0.05), 8: (j(640, 170), 0, "C")},
  "Held the works from Locust Grove to the Carter's Creek Pike; Cox calls its missing trifling [cox] [jesp].", "high", {0: 1600, 5: 1520, 6: 1460}, ["jesp", "cox"], {8: [j(470, 420), j(610, 270)]})
U("strickland_res", "us", "inf", "44th Missouri and 183rd Ohio (Strickland's second line)", "~1,100 infantry", 220,
  {0: (k(590, 610), 225, "L"), 3: (k(595, 615), 200, "F"), 8: (j(620, 170), 0, "C")},
  "Held the retrenchment by the Carter House when the front regiments were swept back; the 72nd Illinois rallied on the 183rd Ohio there [wp].", "medium", {0: 1100, 4: 1000, 6: 980}, ["wp", "jesp"], {8: [j(540, 400), j(610, 270)]})
# ---- Reilly's division (XXIII Corps), east of the pike
U("reilly", "us", "inf", "Reilly's brigade, front line", "~1,100 infantry", 260,
  {0: (k(690, 745), 180, "F"), 3: (k(700, 680), 180, "R"), 4: (k(690, 745), 180, "F"), 8: (j(680, 180), 0, "C")},
  "Held the pike to the cotton gin; the 100th Ohio was driven back in the breakthrough [wp] [jesp].", "high", {0: 1100, 3: 980, 6: 950}, ["jesp", "wp"], {8: [j(560, 400), j(610, 270)]})
U("reilly_res", "us", "inf", "Reilly's reserve: 12th and 16th Kentucky, 175th Ohio", "~1,000 infantry", 220,
  {0: (k(700, 640), 180, "L"), 3: (k(690, 660), 180, "F"), 8: (j(720, 190), 0, "C")},
  "Stood in the second line and became the rally point that sealed the breach east of the pike; the 12th Kentucky carried Henry repeaters [wp].", "high", {0: 1000, 4: 950, 6: 930}, ["wp", "jesp"], {8: [j(560, 400), j(610, 270)]})
U("casement", "us", "inf", "Casement's brigade (Reilly)", "~1,500 infantry", 300,
  {0: (k(840, 765), 180, "F"), 8: (j(580, 200), 0, "C")},
  "East of the cotton gin; its cross fire shattered Cleburne's and French's assaults [wp] [jesp].", "high", {0: 1500, 4: 1450, 6: 1440}, ["jesp", "wp", "cox"], {8: [j(600, 420), j(700, 292)]})
U("stiles", "us", "inf", "Stiles's brigade (Reilly)", "~1,400 infantry", 380,
  {0: (k(975, 690), 135, "F"), 8: (j(620, 205), 0, "C")},
  "Anchored the left on the railroad cut and the river behind an osage-orange abatis; repulsed Loring twice [wp] [jesp].", "high", {0: 1400, 3: 1370, 6: 1350}, ["jesp", "wp"], {8: [j(640, 440), j(700, 292)]})
# ---- Kimball's division (IV Corps), the right flank to the river
U("grose", "us", "inf", "Grose's brigade (Kimball)", "~1,300 infantry", 380, {0: (j(415, 410), 250, "F"), 8: (j(660, 215), 0, "C")},
  "Left brigade of Kimball's division, joining Ruger near the Carter's Creek Pike [jesp] [cox].", "high", {0: 1300, 6: 1260}, ["jesp", "cox"], {8: [j(470, 330), j(610, 270)]})
U("kirby", "us", "inf", "Kirby's brigade (Kimball)", "~1,300 infantry", 380, {0: (j(400, 335), 265, "F"), 8: (j(700, 225), 0, "C")},
  "Lightly engaged with Chalmers's dismounted cavalry [wp] [cox].", "high", {0: 1300, 6: 1290}, ["jesp", "wp", "cox"], {8: [j(470, 300), j(610, 270)]})
U("whitaker", "us", "inf", "Whitaker's brigade (Kimball)", "~1,300 infantry", 380, {0: (j(395, 268), 270, "F"), 8: (j(540, 190), 0, "C")},
  "Covered the right back to the Harpeth below the town [jesp] [cox].", "high", {0: 1300, 6: 1290}, ["jesp", "cox"], {8: [j(480, 250), j(610, 270)]})
# ---- North of the river
U("wood", "us", "inf", "Wood's division (IV Corps)", "~4,500 infantry", 600, {0: (j(830, 390), 200, "L")},
  "Held north of the river to cover the crossings and Fort Granger [jesp] [fw].", "medium", {0: 4500}, ["jesp", "fw"])
U("granger_art", "us", "art", "Battery D, 1st Ohio (Fort Granger)", "4 guns", 80, {0: (B.geo["Fort Granger"], 200, "F")},
  "The one battery in the fort; with Battery M, 4th U.S. it enfiladed Stewart's corps along the railroad cut [or] [cox].", "high", {0: 4}, ["or", "cox", "jesp"])
U("art_centre", "us", "art", "Batteries at the Carter House", "8 guns", 120, {0: (k(590, 645), 200, "F"), 3: (k(600, 600), 200, "R"), 4: (k(590, 645), 200, "F"), 8: (j(760, 200), 0, "C")},
  "Guns at the pike were briefly overrun and turned in the breakthrough [jesp] [hood].", "medium", {0: 8, 3: 6, 4: 6}, ["jesp", "hood", "cox"], {8: [j(560, 400), j(610, 270)]})
U("art_gin", "us", "art", "6th Ohio Battery at the cotton gin", "4 guns", 80, {0: (k(740, 725), 190, "F"), 8: (j(600, 235), 0, "C")},
  "Fired from the salient that Reilly chose as his headquarters [cox] [jesp].", "medium", {0: 4}, ["jesp", "cox"], {8: [j(600, 420), j(700, 292)]})
U("art_left", "us", "art", "Battery G 1st Ohio and Battery M 4th U.S.", "8 guns", 120, {0: (k(975, 560), 160, "F"), 8: (j(740, 230), 0, "C")},
  "Fired canister down the railroad cut on the far left [wp] [jesp].", "medium", {0: 8}, ["jesp", "wp"], {8: [j(640, 440), j(700, 292)]})
# ---- Wilson's cavalry
U("hatch", "us", "cav", "Hatch's cavalry division (Wilson)", "2,638 cavalry", 500,
  {0: (j(1050, 460), 180, "C"), 1: (j(1030, 800), 160, "F"), 6: (j(1060, 930), 160, "F"), 7: (j(1000, 760), 340, "L")},
  "Came south from the Brentwood road and charged Jackson's dismounted troopers; Hatch says they were over the river by 7 p.m. [wp] [abt] [or].", "medium", {0: 2638, 6: 2610}, ["wp", "abt", "cox"], {1: [j(1060, 640)]})
U("croxton", "us", "cav", "Croxton's brigade (Wilson)", "~1,500 cavalry", 350,
  {0: (j(850, 580), 120, "L"), 1: (j(1070, 860), 150, "F"), 7: (j(940, 690), 340, "L")},
  "Struck the flank of Jackson's division north of the river with Spencer carbines [wp] [or].", "medium", {0: 1500, 6: 1480}, ["wp", "jesp", "or"], {1: [j(990, 700)]})

# ---- Confederate: Stewart's corps, east of the pike
def CS(uid, name, men, p0, p1, p3, p4, face, note, conf="medium", cite=("jesp", "wp"), loss=(), extra=None):
    mid = ((p1[0] + p3[0]) / 2, (p1[1] + p3[1]) / 2)
    keys = {0: (p0, 0, "L"), 1: (p1, face, "L"), 2: (mid, face, "L"), 3: (p3, face, "F"), 4: (p4, face, "F")}
    if extra: keys.update(extra)
    m = {0: men}; m.update(dict(loss))
    return U(uid, "cs", "inf", name, f"~{men:,} infantry" if uid != "cockrell" else "696 infantry", 330, keys, note, conf, m, list(cite))

CS("scott", "Scott's brigade (Loring)", 1000, j(840, 975), j(835, 752), k(1100, 860), k(1060, 760), 315,
   "Loring's division twice assaulted Stiles near the railroad and river [wp].", loss={3: 850, 4: 740})
CS("featherston", "Featherston's brigade (Loring)", 1200, j(880, 975), j(795, 772), k(1120, 905), k(1080, 790), 320,
   "Fell back under fire when Loring rode out in front of it [wp].", loss={3: 1000, 4: 900})
CS("adams", "Adams's brigade (Loring)", 1100, j(860, 1010), j(825, 800), k(1000, 900), k(925, 790), 330,
   "Struck in front of Stiles's right and Casement's left; Adams was killed on the parapet trying to seize the 65th Illinois's colours [or] [wp].", loss={3: 900, 4: 820})
CS("quarles", "Quarles's brigade (Walthall)", 1000, j(705, 990), j(745, 772), k(900, 925), k(905, 800), 330,
   "Reached the works through the abatis and was pinned there; by the end a captain commanded it [wp].", loss={3: 800, 4: 680})
CS("reynolds", "Reynolds's brigade (Walthall)", 900, j(755, 990), j(705, 792), k(980, 950), k(980, 820), 330,
   "One of up to six waves Walthall threw at Casement and Reilly [wp].", loss={3: 780, 4: 700})
CS("shelley", "Shelley's brigade (Walthall)", 1000, j(745, 1040), j(735, 822), k(950, 895), k(950, 790), 330,
   "Intermixed with Loring's men in the narrowing ground between railroad and river [wp].", loss={3: 860, 4: 770})
CS("cockrell", "Cockrell's brigade (French)", 696, j(615, 1005), j(640, 820), k(790, 895), k(830, 805), 350,
   "Went in with 696 officers and men and lost 419 [cox].", conf="high", cite=("cox", "jesp", "wp"), loss={3: 450, 4: 300, 5: 277})
CS("sears", "Sears's brigade (French)", 1000, j(630, 1040), j(630, 858), k(795, 935), k(860, 840), 350,
   "French's second brigade; Ector's brigade was away guarding the pontoon train [cox].", cite=("jesp", "cox"), loss={3: 880, 4: 780})
# ---- Cheatham's corps: Cleburne, Brown, Bate
CS("granbury", "Granbury's brigade (Cleburne)", 1100, j(470, 1025), j(490, 830), k(670, 700), k(690, 785), 0,
   "Broke in east of the pike beside Gordon; Granbury was killed and a captain led the brigade afterwards [wp] [tnenc].", cite=("jesp", "wp", "tnenc"), loss={3: 800, 4: 600, 5: 540})
CS("govan", "Govan's brigade (Cleburne)", 1200, j(515, 1025), j(560, 840), k(740, 865), k(760, 800), 0,
   "Struck the cotton-gin salient; Cleburne was killed in this attack [wp] [hood].", cite=("jesp", "wp", "hood"), loss={3: 950, 4: 750, 5: 700})
CS("lowrey", "Lowrey's brigade (Cleburne)", 1300, j(490, 1060), j(540, 865), k(695, 900), k(730, 830), 0,
   "Cleburne's second line; Hood recalls Cleburne asking to form in two, or perhaps three, lines [hood] [jesp].", cite=("jesp", "hood", "wp"), loss={3: 1100, 4: 900, 5: 820})
CS("gordon", "Gordon's brigade (Brown)", 1000, j(400, 1005), j(420, 800), k(640, 700), k(635, 745), 10,
   "Angled right in the advance, crossed the pike and broke in with Cleburne; Gordon was captured [wp].", cite=("jesp", "wp"), loss={3: 750, 4: 520, 5: 500})
CS("strahl", "Strahl's brigade (Brown)", 1000, j(380, 1030), j(400, 830), k(575, 690), k(560, 705), 20,
   "Fought in the ditch west of the pike for hours; Strahl was killed [wp] [hood].", cite=("jesp", "wp", "hood"), loss={3: 800, 4: 620, 5: 560, 6: 540})
CS("carter", "Carter's brigade (Brown)", 1000, j(340, 1005), j(335, 790), k(420, 805), k(450, 625), 40,
   "Struck Strickland and Moore west of Locust Grove; Carter was mortally wounded [wp] [jesp].", cite=("jesp", "wp"), loss={3: 900, 4: 750, 5: 680})
CS("gist", "Gist's brigade (Brown)", 1000, j(355, 980), j(330, 752), k(440, 775), k(480, 650), 35,
   "Brown's left front brigade; Gist was killed [wp] [hood].", cite=("jesp", "wp", "hood"), loss={3: 880, 4: 760, 5: 700})
U("smith_bate", "cs", "inf", "Smith's (Tyler's) brigade (Bate)", "~800 infantry", 330,
  {0: (j(185, 960), 0, "L"), 1: (j(210, 705), 30, "L"), 5: (k(200, 430), 45, "F"), 6: (k(130, 560), 45, "L")},
  "Bate's long march round the left reached the works near the Carter's Creek Pike only at dusk [wp].", "medium", {0: 800, 5: 700, 6: 680}, ["jesp", "wp"])
U("jackson_bate", "cs", "inf", "Jackson's brigade (Bate)", "~900 infantry", 330,
  {0: (j(250, 970), 0, "L"), 1: (j(270, 730), 30, "L"), 5: (k(255, 500), 45, "F"), 6: (k(190, 620), 45, "L")},
  "Swept past Everbright and stalled against Moore and Grose [wp] [jesp].", "medium", {0: 900, 5: 780, 6: 760}, ["jesp", "wp"])
U("bullock", "cs", "inf", "Florida brigade (Bullock) (Bate)", "~700 infantry", 300,
  {0: (j(210, 1025), 0, "L"), 1: (j(220, 757), 20, "L"), 5: (k(150, 470), 60, "F"), 6: (k(90, 600), 45, "L")},
  "Moved from reserve to cover Bate's open left flank, leaving no second line [wp].", "medium", {0: 700, 5: 640, 6: 620}, ["wp", "jesp"])
# ---- Lee's corps: Johnson's division, the only one up in time
for uid, name, men, p5, p6, loss in [
    ("deas", "Deas's brigade (Johnson)", 900, k(330, 880), k(460, 690), 800),
    ("manigault", "Manigault's brigade (Johnson)", 700, k(260, 880), k(400, 680), 600),
    ("sharp", "Sharp's brigade (Johnson)", 900, k(210, 800), k(330, 640), 800),
    ("brantley", "Brantley's brigade (Johnson)", 800, k(200, 830), k(300, 670), 720)]:
    U(uid, "cs", "inf", name, f"~{men} infantry", 280,
      {0: (j(450, 1180), 0, "C"), 4: (j(440, 1000), 0, "C"), 5: (j(435, 900), 0, "C"), 6: (p6, 40, "F"), 7: (p5, 30, "L")},
      "Johnson's division attacked west of the pike about an hour after dark, lost its alignment and was repulsed in one assault [or] [wp].", "low", {0: men, 6: loss}, ["wp", "or", "jesp"],
      {6: [j(430, 800), p5]})
# ---- Forrest's cavalry
U("chalmers", "cs", "cav", "Chalmers's cavalry division (Forrest)", "~1,800 cavalry", 450,
  {0: (j(110, 760), 20, "L"), 1: (j(140, 650), 30, "L"), 5: (j(320, 420), 70, "F"), 6: (j(240, 470), 70, "L")},
  "Fought dismounted against Kirby and Whitaker; Bate did not know it was engaged [wp].", "low", {0: 1800, 6: 1760}, ["wp", "jesp"])
U("buford", "cs", "cav", "Buford's cavalry division (Forrest)", "~2,000 cavalry", 450,
  {0: (j(965, 1060), 0, "C"), 1: (j(885, 745), 330, "F"), 5: (j(895, 760), 330, "L")},
  "Fought dismounted on Stewart's right between the Lewisburg Pike and the river and drove the Union cavalry back across the Harpeth; it did not cross [or].", "medium", {0: 2000, 3: 1950}, ["or", "jesp"], {1: [j(940, 900)]})
U("jackson_cav", "cs", "cav", "W. H. Jackson's cavalry division (Forrest)", "~2,000 cavalry", 450,
  {0: (j(1000, 1060), 0, "C"), 1: (j(1110, 900), 320, "F"), 6: (j(1040, 1040), 200, "R"), 7: (j(1000, 1090), 340, "L")},
  "Crossed at Hughes's Ford to protect Forrest's right and held Wilson until night, then recrossed [or]; Croxton's Spencer carbines told heavily [wp] [abt].", "medium", {0: 2000, 6: 1900}, ["or", "wp", "abt", "jesp"], {1: [j(1050, 950)], 6: [j(1050, 950)]})
U("guibor", "cs", "art", "Guibor's battery (Stewart)", "6 guns", 100, {0: (j(690, 1030), 0, "C"), 1: (j(690, 900), 340, "F")},
  "Served in sections in the intervals of Stewart's line; one of only two Confederate batteries Cox found in action, though Hood says he withheld his artillery to spare the town [cox] [hood].", "low", {0: 6}, ["cox", "hood"])
U("presstman", "cs", "art", "Presstman's battery (Cheatham)", "6 guns", 100, {0: (j(405, 742), 0, "F"), 5: (j(300, 640), 30, "F")},
  "First on Privet Knob, later on the knoll at Bostick's near the Carter's Creek Pike [cox].", "low", {0: 6}, ["cox"])

B.commander("schofield", "us", "Schofield", {0: B.geo["Fort Granger"]}, "Directed the battle from Fort Granger across the river [jesp] [cox].")
B.commander("cox", "us", "Cox", {0: k(660, 650)}, "Commanded the line from his station on the pike by the Carter House [cox].")
B.commander("hood", "cs", "Hood", {0: B.geo["Winstead Hill"]}, "Watched from Winstead Hill, two miles south [fw] [wp].")
B.commander("cheatham", "cs", "Cheatham", {0: j(405, 742)}, "Corps headquarters on Privet Knob [wp].")

PIKE_W, PIKE_E = k(600, 700), k(680, 700)
B.phase("15:00", "Hood deploys", "Two armies face each other across two miles",
  "Schofield's infantry holds an arc of earthworks south of Franklin, both flanks on the Harpeth, while the trains cross north towards Nashville [cox] [jesp]. Wagner has left two brigades half a mile out on a rise across the Columbia Pike [wp] [cox]. Below Winstead Hill, Stewart's corps forms east of the pike and Cheatham's west of it; Lee's corps is still on the road [hood] [jesp] [fw].",
  ("Strongpoint defence", "An entrenched line with clear fields of fire and both flanks on obstacles forces an attacker to come straight at it.", "strongpoint-defence"), j(520, 760), 5.5,
  arrows=[B.arrow("cs", "move", j(470, 1250), j(480, 1040)), B.arrow("cs", "move", j(640, 1200), j(700, 1020)), B.arrow("cs", "move", j(380, 1200), j(220, 980))],
  events=[(B.geo["Winstead Hill"], "Hood's headquarters on Winstead Hill [fw]", ["fw"]), (j(480, 620), "Wagner's two brigades stand exposed in front of the main line [cox]", ["cox"])],
  conf="high", cite=["cox", "jesp", "hood", "fw"])
B.phase("16:00", "The advance", "A two-mile line steps off",
  "About 20,000 Confederates of Stewart's and Cheatham's corps advance in parade order across open ground, with almost no artillery support [abt] [hood] [cox]. On the right Buford's dismounted cavalry drives the Union cavalry pickets back across the Harpeth, while Jackson's division crosses at Hughes's Ford to protect the army's flank [or].",
  ("Frontal assault", "Attacking an entrenched enemy head-on over open ground trades the attacker's numbers for the defender's fire.", "frontal-assault"), j(560, 820), 5.0,
  arrows=[B.arrow("cs", "move", j(490, 1030), j(490, 840)), B.arrow("cs", "move", j(740, 1000), j(745, 790)), B.arrow("cs", "move", j(340, 1000), j(330, 760)), B.arrow("cs", "move", j(1000, 1040), j(1050, 950), j(1100, 890))],
  events=[(j(1050, 950), "Jackson's cavalry crosses at Hughes's Ford [or]", ["or"])],
  conf="medium", debate="Hood, the American Battlefield Trust and Jespersen give about 4 p.m.; the Tennessee Encyclopedia gives 4:30. This map follows 4 p.m. [hood] [abt] [tnenc].", cite=["abt", "hood", "or", "cox", "tnenc"])
B.phase("16:15", "Wagner overrun", "\"Go into the works with them\"",
  "The Confederate line overlaps Lane and Conrad, who fire one volley and break. Nearly 700 are captured; the rest run up the pike with Cleburne's and Brown's men at their heels, and the defenders in the works cannot fire without hitting them [wp] [abt] [cox].",
  ("Exposed advanced position", "An advanced force caught in front of the main line masks that line's fire as it falls back.", "exposed-outpost"), j(505, 640), 3.2,
  arrows=[B.arrow("us", "retreat", j(470, 600), k(560, 690)), B.arrow("us", "retreat", j(530, 630), PIKE_E), B.arrow("cs", "charge", j(490, 800), k(650, 760))],
  events=[(j(495, 620), "Wagner's men flee towards the works; about 700 are taken [wp]", ["wp"])],
  conf="high", cite=["wp", "abt", "cox"])
B.phase("16:30", "Breakthrough at the Carter House", "The line breaks at the pike",
  "Cleburne, Brown and French converge on the gap at the pike. The 100th Ohio and Strickland's front regiments are driven back and Confederates penetrate about 50 yards into the line, turning captured guns [wp] [hood]. East of the railroad Stewart's corps, squeezed against the river, stalls in the osage-orange abatis under fire from Fort Granger; Adams dies on the parapet [wp]. Across the river Jackson's troopers are fighting Wilson's [or].",
  ("Penetration", "A break-in at a single point is only decisive if reserves can widen it before the defender's reserves seal it.", "reserve-commitment"), k(660, 700), 2.2,
  arrows=[B.arrow("cs", "charge", k(650, 860), k(640, 660)), B.arrow("cs", "charge", k(740, 880), k(740, 760)), B.arrow("cs", "charge", k(1080, 880), k(1000, 720)), B.arrow("us", "fire", B.geo["Fort Granger"], k(1060, 820))],
  events=[(k(650, 660), "Confederates break 50 yards into the line at the Carter House [wp]", ["wp"]), (k(915, 765), "Adams killed on the parapet at the Stiles-Casement junction [or] [wp]", ["or", "wp"]), (k(720, 790), "Cleburne killed near the cotton gin [wp] [hood]", ["wp", "hood"])],
  conf="medium", cite=["wp", "hood", "abt", "jesp", "or"])
B.phase("16:45", "Opdycke's counterattack", "The breach is sealed",
  "Opdycke deploys his veterans astride the pike and charges into the breach on his own initiative; Stanley, arriving, urges the nearest regiment on but gives Opdycke no orders, and is wounded [or]. West of the pike the 44th Missouri and 183rd Ohio hold the retrenchment at the Carter House; east of it Reilly's reserve regiments rally the fugitives. Hand-to-hand fighting in the Carter garden restores the line, and the Confederates are pinned in the outer ditch [wp] [abt] [hood].",
  ("Reserve commitment", "A reserve held close behind the threatened point can counterattack before a break-in becomes a breakthrough.", "reserve-commitment"), k(650, 680), 1.8,
  arrows=[B.arrow("us", "charge", k(632, 520), k(625, 650)), B.arrow("us", "charge", k(700, 640), k(690, 720))],
  events=[(k(625, 640), "Opdycke's brigade retakes the works at the pike [wp]", ["wp"]), (k(645, 600), "Close combat in the Carter house garden [wp] [hood]", ["wp", "hood"])],
  conf="high", debate="Cox credits Opdycke's initiative and Reilly's reserves; Stanley's supporters later credited Stanley, who wrote that he called a regiment to charge but gave Opdycke no order. Jacobson's later work stresses the 44th Missouri, 175th and 183rd Ohio at the breach [wp] [cox] [or].", cite=["wp", "abt", "hood", "cox", "or"])
B.phase("17:00", "Sunset", "The flanks fail as the light goes",
  "The sun sets at about five [cox]. On the Union right Bate's division finally reaches the works past Everbright, without the support it expected from Chalmers, whose dismounted troopers are fighting Kimball out of Bate's sight; both are repulsed [wp]. At the centre the Confederates renew their assaults again and again from the ditch [cox] [tnenc].",
  ("Envelopment", "A flank attack needs time and coordination; started late and unsupported, it becomes just another frontal assault.", "envelopment"), k(450, 560), 3.6,
  arrows=[B.arrow("cs", "charge", k(130, 560), k(250, 430)), B.arrow("cs", "charge", j(240, 470), j(380, 380))],
  events=[(j(380, 600), "Bate sweeps past Everbright [wp]", ["wp"]), (k(300, 380), "Bate's single line is stopped at the works [wp]", ["wp"])],
  conf="medium", cite=["wp", "cox", "tnenc"])
B.phase("18:00", "Johnson's attack", "Lee's one division goes in after dark",
  "Hood commits Edward Johnson's division, the only one of Lee's corps to have arrived. Guideless in the dark, it loses its alignment around Privet Knob and attacks the works west of the Carter House in a single assault, which is repulsed with heavy loss [wp] [hood]. Lee says it was not felt by the enemy until about an hour after dark [or]. Across the river, Hatch and Croxton finally drive Jackson's troopers back over the Harpeth [or] [wp].",
  ("Reserve commitment", "Committing a reserve piecemeal and in darkness against an intact line adds losses without changing the result.", "reserve-commitment"), k(420, 650), 2.6,
  arrows=[B.arrow("cs", "charge", k(260, 880), k(400, 690)), B.arrow("cs", "charge", k(210, 800), k(330, 650)), B.arrow("us", "charge", j(1040, 820), j(1060, 930))],
  events=[(k(380, 660), "Johnson's division repulsed in one assault [wp]", ["wp"]), (j(1050, 950), "Jackson's cavalry recrosses the Harpeth [or]", ["or"])],
  conf="medium", debate="Hood has Johnson moving 'just before dark'; Lee and Cox put the blow about an hour after dark (about 6 p.m.); Wikipedia, after Jacobson, gives about 7 p.m. This map follows Lee [hood] [or] [cox] [wp].", cite=["wp", "hood", "or", "cox"])
B.phase("21:00", "Stalemate at the works", "Firing dies down",
  "Effective fire ends about nine o'clock, though the Tennessee Encyclopedia has fighting until ten [cox] [hood] [tnenc]. Union troops hold the inside of the works and Confederates the outer ditch, a few feet apart [tnenc].",
  ("Strongpoint defence", "Once the attacker's momentum is spent at the parapet, the defender's line wins by simply holding.", "strongpoint-defence"), k(650, 720), 2.4,
  events=[(k(700, 760), "The dead lie five or six deep in the ditch [tnenc]", ["tnenc"])], conf="medium", fog=0.25, cite=["cox", "hood", "tnenc"])
B.phase("23:00", "Withdrawal", "Schofield crosses the Harpeth",
  "Schofield issued his withdrawal order between six and seven, passed on by the Fourth Corps at 7:15; near midnight the infantry leaves the works and crosses the river towards Nashville, leaving dead and wounded on the field [cox] [hood]. Hood, claiming the field, has lost 6,252 men by Schofield's count, including six generals killed or mortally wounded [cox] [or].",
  ("Rearguard", "A defender who has won the fight can still decline the next one, slipping away under cover of darkness.", "rearguard"), j(560, 420), 4.0,
  arrows=[B.arrow("us", "move", j(560, 440), j(610, 270), j(640, 200))],
  events=[(j(610, 270), "Union infantry crosses the Harpeth bridges [cox]", ["cox"]), (B.geo["Carnton"], "Carnton becomes a Confederate field hospital [tnenc]", ["tnenc"])],
  conf="medium", fog=0.3,
  debate="Schofield's count of 6,252 Confederate losses was made after Franklin was reoccupied in December; Hood reported 4,500, and Cox estimated about 8,000 including the lightly wounded. The chart follows 6,252 [cox] [hood] [or].", cite=["cox", "hood", "or"])

B.export()
