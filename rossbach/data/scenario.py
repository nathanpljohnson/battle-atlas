import json, math

# Phase index -> (lat, lon, facing_deg, formation). Formation: L line, C column, R rout, F firing line, X camp.
# Missing phases carry the previous key forward.
PH = ["0900", "1200", "1430", "1515", "1530", "1545", "1600", "1615", "1630", "1645"]

def mv(p, bearing, meters):
    lat, lon = p
    b = math.radians(bearing)
    return (lat + math.cos(b) * meters / 111200, lon + math.sin(b) * meters / (111200 * math.cos(math.radians(lat))))

def echelon(lead, facing, n, spacing=430, setback=130):
    out = []
    p = lead
    for i in range(n):
        out.append(p)
        p = mv(mv(p, facing + 90, spacing), facing + 180, setback)
    return out

units = []
def U(id, side, type, name, strength, w, keys, note=""):
    units.append(dict(id=id, side=side, type=type, name=name, strength=strength, w=w, keys=keys, note=note))

# ---------- Prussian first line (left -> right). Facing west in camp.
camp_lon = 11.894
pi_names = [
    ("pi1", "Grenadier battalions", "Kremzow, Heyden, Wedell grenadiers · 3 bns", "Massed grenadier companies, the army's shock infantry. Led the echelon on the left."),
    ("pi2", "Garde & Itzenplitz", "IR 15 Garde, IR 13 Itzenplitz · 4 bns", "Frederick's own Foot Guards plus a line regiment."),
    ("pi3", "Forcade & Jung-Kleist", "IR 23, IR 9 · 4 bns", ""),
    ("pi4", "Alt-Braunschweig & Winterfeldt", "IR 5, IR 1 · 4 bns", ""),
    ("pi5", "Goltz & Hülsen", "IR 25, IR 21 · 3 bns", "Right wing; arrived last and saw little fighting."),
]
ech6 = echelon((51.2517, 11.9332), 220, 5)
ech7 = [mv(p, 215, 180) for p in ech6]
ech8 = [mv(p, 215, 520) for p in ech6]
ridge4 = echelon((51.2633, 11.9300), 215, 5, 420, 0)
ridge5 = [mv(p, 215, 300) for p in ridge4]
for i, (uid, nm, st, note) in enumerate(pi_names):
    lat_camp = 51.2632 + i * 0.0031
    marchA = mv((51.2712, 11.9185), 275, i * 650)
    marchB = mv((51.2705, 11.9405), 285, i * 520)
    U(uid, "pr", "inf", nm, st, 600, {
        0: (lat_camp, camp_lon, 270, "X"),
        2: (*marchA, 95, "C"),
        3: (*marchB, 110, "C"),
        4: (*ridge4[i], 215, "L"),
        5: (*ridge5[i], 215, "L"),
        6: (*ech6[i], 215, "F"),
        7: (*ech7[i], 215, "F"),
        8: (*ech8[i], 215, "L"),
    }, note)

# Prussian second line, barely engaged
for i, (uid, nm, st) in enumerate([("pj1", "Second line (left)", "Markgraf Karl, Meyerinck · 4 bns"),
                                    ("pj2", "Second line (centre)", "IR 19, IR 10 · 3 bns"),
                                    ("pj3", "Second line (right)", "Fusiliers & Lubath grenadiers · 2 bns")]):
    lat_camp = 51.2655 + i * 0.0048
    U(uid, "pr", "inf", nm, st, 560, {
        0: (lat_camp, 11.9015, 270, "X"),
        2: (*mv((51.2745, 11.9120), 275, i * 700), 95, "C"),
        3: (*mv((51.2735, 11.9330), 285, i * 650), 110, "C"),
        4: (*mv(mv(ridge4[i * 2], 35, 420), 0, 0), 215, "L"),
        6: (*mv(ech6[i * 2], 35, 520), 215, "L"),
        8: (*mv(ech8[i * 2], 35, 520), 215, "L"),
    }, "Reserve line. Most of these battalions never fired a shot.")

U("pmo", "pr", "art", "Moller's battery", "18 heavy guns (12-pdr 'Brummer')", 260, {
    0: (51.2690, 11.8985, 270, "X"),
    2: (51.2700, 11.9230, 95, "C"),
    3: (51.2652, 11.9327, 215, "F"),
    7: (51.2652, 11.9327, 215, "F"),
    8: (51.2600, 11.9300, 215, "L"),
}, "Colonel Karl Friedrich von Moller dragged the army's heavy guns onto the Janus Hill and fired over the heads of the Prussian infantry.")

cav = [("pc1", "Garde du Corps & Gendarmes", "Heavy cavalry · 8 sqns", "Elite heavy horse; first line of the charge."),
       ("pc2", "Leib & Seydlitz Cuirassiers", "Heavy cavalry · 10 sqns", "Armoured breastplates, big horses, straight swords."),
       ("pc3", "Czettritz & Meinicke Dragoons", "Medium cavalry · 10 sqns", "Second line of the charge."),
       ("pc4", "Driesen Cuirassiers", "Heavy cavalry · 5 sqns", "Second line."),
       ("ph1", "Szekely Hussars", "Light cavalry · 5 sqns", "Light horse for scouting and pursuit.")]
cav_keys = [
    # p0 camp, p2 march, p3 behind Polzen, p4 charge, p5 rally Tagewerben, p6 ready, p7 charge 2, p8 pursuit
    [(51.2630, 11.9085), (51.2752, 11.9390), (51.2748, 11.9555), (51.2560, 11.9370), (51.2478, 11.9590), (51.2482, 11.9560), (51.2462, 11.9300), (51.2400, 11.9180)],
    [(51.2670, 11.9085), (51.2756, 11.9300), (51.2745, 11.9640), (51.2545, 11.9440), (51.2452, 11.9640), (51.2455, 11.9610), (51.2440, 11.9250), (51.2370, 11.9110)],
    [(51.2710, 11.9085), (51.2766, 11.9470), (51.2772, 11.9500), (51.2590, 11.9425), (51.2500, 11.9650), (51.2505, 11.9625), (51.2482, 11.9345), (51.2425, 11.9230)],
    [(51.2750, 11.9085), (51.2770, 11.9220), (51.2770, 11.9600), (51.2578, 11.9495), (51.2470, 11.9695), (51.2475, 11.9665), (51.2452, 11.9330), (51.2390, 11.9260)],
    [(51.2790, 11.9085), (51.2780, 11.9550), (51.2790, 11.9665), (51.2610, 11.9520), (51.2425, 11.9530), (51.2430, 11.9520), (51.2420, 11.9200), (51.2340, 11.9050)],
]
for (uid, nm, st, note), k in zip(cav, cav_keys):
    U(uid, "pr", "lc" if uid == "ph1" else "cav", nm, st, 420, {
        0: (*k[0], 270, "X"), 2: (*k[1], 95, "C"), 3: (*k[2], 205, "L"), 4: (*k[3], 225, "L"),
        5: (*k[4], 280, "L"), 6: (*k[5], 290, "L"), 7: (*k[6], 290, "L"), 8: (*k[7], 225, "L"),
    }, note)

U("pfb", "pr", "lt", "Frei-Bataillon Mayr", "Light infantry · 1 bn", 260, {
    0: (51.2670, 11.8840, 270, "L"), 7: (51.2670, 11.8840, 270, "L"), 8: (51.2600, 11.8780, 240, "L"),
}, "A 'free battalion' of irregular light infantry left behind to watch St Germain.")

# ---------- Allies
fr_inf = [("fi1", "Piémont & Mailly", "French line infantry · 8 bns", "Head of the right column. Tried a bayonet attack in column and was shot down."),
          ("fi2", "Poitou & Provence", "French line infantry · 4 bns", ""),
          ("fi3", "St-Chamond & La Marck", "French line infantry · 4 bns", "La Marck was a German regiment in French service."),
          ("fi4", "Broglie's reserve", "French infantry · 8 bns", "")]
fr_keys = [
    #   p0 camp             p1 south            p2 past Pettstädt    p3                 p4                 p5                 p6                 p7                 p8 rout             p9 fled
    [(51.2600, 11.8240), (51.2520, 11.8270), (51.2412, 11.8670), (51.2440, 11.9050), (51.2470, 11.9140), (51.2492, 11.9200), (51.2502, 11.9265), (51.2498, 11.9255), (51.2420, 11.9080), (51.2310, 11.8930)],
    [(51.2660, 11.8240), (51.2540, 11.8345), (51.2372, 11.8630), (51.2410, 11.9005), (51.2440, 11.9095), (51.2468, 11.9155), (51.2482, 11.9215), (51.2478, 11.9210), (51.2400, 11.9020), (51.2285, 11.8880)],
    [(51.2720, 11.8240), (51.2600, 11.8270), (51.2335, 11.8590), (51.2380, 11.8965), (51.2412, 11.9050), (51.2442, 11.9105), (51.2460, 11.9170), (51.2455, 11.9165), (51.2378, 11.8970), (51.2262, 11.8830)],
    [(51.2780, 11.8240), (51.2620, 11.8345), (51.2410, 11.8500), (51.2415, 11.8890), (51.2425, 11.8990), (51.2455, 11.9040), (51.2470, 11.9110), (51.2470, 11.9110), (51.2398, 11.8920), (51.2290, 11.8790)],
]
fr_form = ["X", "C", "C", "C", "C", "C", "C", "F", "R", "R"]
fr_face = [90, 180, 75, 50, 50, 45, 40, 40, 225, 230]
for (uid, nm, st, note), k in zip(fr_inf, fr_keys):
    U(uid, "fr", "inf", nm, st, 600, {i: (*k[i], fr_face[i], fr_form[i]) for i in range(10)}, note)
units[-1]["keys"][7] = (*fr_keys[3][7], 40, "C")
units[-4]["keys"][7] = (*fr_keys[0][7], 40, "F")

re_inf = [("ri1", "Blau-Würzburg", "Reichsarmee infantry · 2 bns", "Contingents from the small states of the Holy Roman Empire, often poorly trained."),
          ("ri2", "Hessen-Darmstadt & Kur-Trier", "Reichsarmee infantry · 4 bns", "")]
ri_keys = [
    [(51.2630, 11.8150), (51.2650, 11.8270), (51.2370, 11.8445), (51.2385, 11.8860), (51.2400, 11.8945), (51.2425, 11.9000), (51.2440, 11.9060), (51.2440, 11.9060), (51.2362, 11.8880), (51.2240, 11.8770)],
    [(51.2720, 11.8150), (51.2680, 11.8345), (51.2330, 11.8410), (51.2350, 11.8810), (51.2365, 11.8900), (51.2392, 11.8960), (51.2410, 11.9020), (51.2410, 11.9020), (51.2335, 11.8840), (51.2215, 11.8720)],
]
for (uid, nm, st, note), k in zip(re_inf, ri_keys):
    U(uid, "re", "inf", nm, st, 520, {i: (*k[i], fr_face[i], ["X", "C", "C", "C", "C", "C", "C", "C", "R", "R"][i]) for i in range(10)}, note)

U("fart", "fr", "art", "Allied reserve artillery", "French & Imperial guns", 240, {
    0: (51.2690, 11.8300, 90, "X"), 1: (51.2580, 11.8300, 180, "C"), 2: (51.2390, 11.8540, 75, "C"),
    3: (51.2420, 11.8950, 50, "C"), 5: (51.2465, 11.9095, 45, "C"), 6: (51.2485, 11.9180, 40, "F"),
    8: (51.2470, 11.9150, 40, "R"),
}, "Most of these guns were abandoned in the rout.")

ac = [("ac1", "Austrian cuirassiers", "Bretlach & Trautmannsdorf · 14 sqns", "The best horsemen in the allied army; they met Seydlitz head-on and broke last.", "re"),
      ("ac2", "French horse (vanguard)", "FitzJames, Bourbon-Busset & others · 14 sqns", "", "fr"),
      ("ac3", "Reichsarmee & French horse", "La Reine, Bourbon, Rougrave & Imperial cavalry · 20 sqns", "", "fr")]
ac_keys = [
    [(51.2505, 11.8165), (51.2385, 11.8370), (51.2440, 11.8960), (51.2535, 11.9300), (51.2550, 11.9335), (51.2420, 11.9330), (51.2330, 11.9250), (51.2290, 11.9170), (51.2240, 11.9070), (51.2190, 11.8960)],
    [(51.2470, 11.8165), (51.2410, 11.8320), (51.2415, 11.8870), (51.2500, 11.9235), (51.2518, 11.9275), (51.2395, 11.9275), (51.2310, 11.9190), (51.2270, 11.9110), (51.2225, 11.9010), (51.2180, 11.8900)],
    [(51.2435, 11.8165), (51.2445, 11.8300), (51.2390, 11.8780), (51.2465, 11.9165), (51.2482, 11.9200), (51.2372, 11.9200), (51.2290, 11.9120), (51.2255, 11.9040), (51.2210, 11.8950), (51.2170, 11.8840)],
]
ac_form = ["X", "C", "C", "C", "L", "R", "R", "R", "R", "R"]
ac_face = [90, 160, 65, 50, 45, 195, 210, 220, 225, 230]
for (uid, nm, st, note, side), k in zip(ac, ac_keys):
    U(uid, side, "cav", nm, st, 420, {i: (*k[i], ac_face[i], ac_form[i]) for i in range(10)}, note)

U("sg", "fr", "inf", "St Germain's corps", "≈8,000 French foot & horse", 900, {
    0: (51.2700, 11.8470, 90, "L"), 7: (51.2700, 11.8470, 90, "L"),
    8: (51.2570, 11.8620, 150, "C"), 9: (51.2425, 11.8840, 70, "L"),
}, "Left on the heights to pin the Prussians. Covered the retreat at the end of the day.")
U("lou", "re", "lt", "Loudon's Croats", "Austrian light troops · 3 bns", 360, {
    0: (51.2590, 11.8560, 90, "L"), 7: (51.2590, 11.8560, 90, "L"),
    8: (51.2470, 11.8700, 120, "C"), 9: (51.2360, 11.8790, 70, "L"),
}, "Croatian Grenzer light infantry, skirmishers who fought in open order.")

hq = [
    dict(id="fred", side="pr", name="Frederick II", keys={0: (51.2607, 11.8922), 2: (51.2725, 11.9200), 3: (51.2680, 11.9318), 8: (51.2560, 11.9250)},
         note="Watched the allied march from the roof of the Rossbach manor house."),
    dict(id="soub", side="fr", name="Soubise & Hildburghausen", keys={0: (51.2690, 11.8200), 1: (51.2560, 11.8310), 2: (51.2400, 11.8600), 3: (51.2420, 11.8930),
         5: (51.2445, 11.9030), 8: (51.2350, 11.8880), 9: (51.2260, 11.8760)}, note="The two allied commanders shared command and disagreed throughout."),
]

def ll(*pts):
    return [list(p) for p in pts]

phases = [
    dict(t="09:00", label="Morning", title="Two camps, six kilometres apart",
         text="Frederick's army of about 22,000 is camped between Bedra and Rossbach, facing west. Across the valley, about 41,000 French and Imperial (Reichsarmee) troops under the Prince de Soubise and the Prince of Saxe-Hildburghausen hold the heights toward Mücheln. The allied commanders decide to march around the Prussian left and get between Frederick and the Saale crossings at Merseburg and Weissenfels.",
         tactic=("Turning movement", "Marching around an enemy's flank to threaten his supply lines and line of retreat. It needs speed and good scouting, and the allies had neither."),
         arrows=[], events=[[51.2607, 11.8922, "Frederick's headquarters in the Rossbach manor"]]),
    dict(t="12:00", label="Allies march", title="The allied army sets off south",
         text="Around noon the allied columns begin a long, slow march south toward Zeuchfeld, cavalry in the lead. St Germain stays behind on the heights with about 8,000 men to hold the Prussians' attention. Frederick, watching from the roof of the Rossbach manor, at first takes the movement for a retreat toward Freyburg and lets his men eat their midday meal.",
         tactic=("March column vs. line", "Troops in column move fast along roads but can barely fire. To fight, a column must first deploy into a firing line, which takes time. A column caught before it deploys is very vulnerable."),
         arrows=[dict(s="fr", k="move", p=ll((51.262, 11.826), (51.250, 11.829), (51.240, 11.835), (51.236, 11.852)))],
         events=[[51.2700, 11.8470, "St Germain stays to pin the Prussians"], [51.2385, 11.8370, "Cavalry vanguard turns east"]]),
    dict(t="14:30", label="Prussians move", title="Frederick strikes camp",
         text="By mid-afternoon it is clear the allies are swinging east past Pettstädt to get round his left. Frederick orders the camp struck; tents come down within minutes. The army marches east behind the Janus and Polzen hills, out of sight of the allies. All 38 squadrons of cavalry go ahead under Friedrich Wilhelm von Seydlitz, the army's youngest general. Seeing the tents fall, the allies conclude the Prussians are retreating and hurry on.",
         tactic=("Using dead ground", "Hills hide movement behind them. The Prussians moved along the far side of the ridge, so the allies could not see where they were going."),
         arrows=[dict(s="fr", k="move", p=ll((51.236, 11.845), (51.238, 11.870), (51.243, 11.895), (51.252, 11.925), (51.262, 11.945))),
                 dict(s="pr", k="move", p=ll((51.268, 11.897), (51.2725, 11.912), (51.2745, 11.935))),
                 dict(s="pr", k="move", p=ll((51.271, 11.910), (51.276, 11.935), (51.2765, 11.958)))],
         events=[[51.2700, 11.9000, "Camp struck in minutes"], [51.2410, 11.8600, "Allies hurry to cut off a 'retreat'"]]),
    dict(t="15:15", label="Guns open", title="Moller's battery opens fire",
         text="Colonel Moller hauls 18 heavy guns to the top of the Janus Hill and opens fire on the allied cavalry and the heads of the infantry columns. Behind the Polzen Hill, Seydlitz forms his squadrons in two lines, still out of sight.",
         tactic=("Heavy guns on high ground", "Prussian 12-pounders (nicknamed 'Brummer', growlers) could reach well over a kilometre. Firing down onto troops packed in columns did heavy damage."),
         arrows=[dict(s="pr", k="fire", p=ll((51.2652, 11.9327), (51.2560, 11.9300))),
                 dict(s="pr", k="fire", p=ll((51.2652, 11.9327), (51.2480, 11.9160))),
                 dict(s="fr", k="move", p=ll((51.244, 11.905), (51.252, 11.925), (51.258, 11.937)))],
         events=[[51.2652, 11.9327, "18 guns on the Janus Hill"], [51.2760, 11.9580, "Seydlitz forms behind the Polzen Hill"]]),
    dict(t="15:30", label="Seydlitz charges", title="Seydlitz's charge",
         text="Seydlitz brings his squadrons over the Polzen Hill and charges, in close order at full gallop, into the allied cavalry while it is still strung out in march column. The Austrian cuirassiers turn and fight, and French squadrons counter-attack, but within half an hour the whole allied cavalry is broken and fleeing south.",
         tactic=("Shock cavalry", "Heavy cavalry charging knee-to-knee at the gallop hits like a wall. Seydlitz trained his men to keep formation at speed, which few cavalry of the time could do."),
         arrows=[dict(s="pr", k="charge", p=ll((51.2750, 11.9580), (51.2640, 11.9500), (51.2560, 11.9380))),
                 dict(s="pr", k="charge", p=ll((51.2770, 11.9640), (51.2650, 11.9560), (51.2560, 11.9460))),
                 dict(s="pr", k="move", p=ll((51.2690, 11.9220), (51.2660, 11.9180)))],
         events=[[51.2550, 11.9340, "Cavalry clash north of Reichardtswerben"]]),
    dict(t="15:45", label="Cavalry routed", title="The allied cavalry breaks",
         text="The allied horse streams away south past Reichardtswerben. Instead of chasing it off the field, Seydlitz rallies his squadrons in the hollow near Tagewerben. On the ridge, the Prussian infantry has finished forming and starts down the slope. The allied infantry columns, still marching, crowd into one another.",
         tactic=("Rally and re-form", "Horses and riders are blown after a charge, and scattered cavalry is useless. Rallying quickly meant Seydlitz had a formed force ready to strike again."),
         arrows=[dict(s="fr", k="retreat", p=ll((51.2540, 11.9320), (51.2440, 11.9330), (51.2340, 11.9250))),
                 dict(s="pr", k="move", p=ll((51.2540, 11.9400), (51.2510, 11.9520), (51.2480, 11.9600)))],
         events=[[51.2480, 11.9620, "Seydlitz rallies near Tagewerben"]]),
    dict(t="16:00", label="Infantry fight", title="The Prussian infantry advances in echelon",
         text="The Prussian first line comes down from the Janus Hill in echelon, left wing first, and takes up position across the allied line of march. Only about seven battalions get into action. The leading French regiments try to deploy, and some attempt a bayonet charge while still in column, but they are met by steady platoon volleys and Moller's guns. The firefight lasts barely a quarter of an hour.",
         tactic=("Echelon and platoon fire", "In an echelon each battalion is set slightly back from the one beside it, so the line meets the enemy one unit at a time from the strong end. Prussian battalions fired by platoons in a rolling sequence, keeping up continuous fire."),
         arrows=[dict(s="pr", k="move", p=ll(mv(ech6[0], 35, 300), ech6[0])),
                 dict(s="pr", k="move", p=ll(mv(ech6[2], 35, 300), ech6[2])),
                 dict(s="pr", k="fire", p=ll(ech6[0], mv(ech6[0], 215, 420))),
                 dict(s="pr", k="fire", p=ll(ech6[1], mv(ech6[1], 215, 450)))],
         events=[[51.2510, 11.9280, "French column heads try to deploy"]]),
    dict(t="16:15", label="Second charge", title="Seydlitz strikes the infantry",
         text="With the allied infantry pinned by fire from the front, Seydlitz charges again from the Tagewerben hollow into its right flank and rear. Regiments jammed in column cannot turn to face him. The allied army begins to come apart.",
         tactic=("Combined arms", "Infantry holds the enemy in place with fire from the front while cavalry hits the flank. Neither arm alone would have broken the allied army so quickly."),
         arrows=[dict(s="pr", k="charge", p=ll((51.2482, 11.9560), (51.2470, 11.9420), (51.2465, 11.9310))),
                 dict(s="pr", k="charge", p=ll((51.2455, 11.9610), (51.2445, 11.9420), (51.2442, 11.9260))),
                 dict(s="pr", k="fire", p=ll(ech7[1], mv(ech7[1], 215, 380)))],
         events=[[51.2460, 11.9300, "Cavalry into the allied flank"]]),
    dict(t="16:30", label="Rout", title="The allied army dissolves",
         text="The allied infantry breaks and flees south-west toward Pettstädt, Storkau and Obschütz, abandoning guns and baggage. The Prussians follow, but the November sun is setting. St Germain finally marches south from the heights to try to cover the retreat.",
         tactic=("Pursuit", "A beaten army is most vulnerable in flight. Darkness at about half past four on a November afternoon is what saved most of the allied army."),
         arrows=[dict(s="fr", k="retreat", p=ll((51.2490, 11.9220), (51.2420, 11.9080), (51.2330, 11.8950))),
                 dict(s="fr", k="retreat", p=ll((51.2450, 11.9130), (51.2370, 11.8960), (51.2290, 11.8850))),
                 dict(s="re", k="retreat", p=ll((51.2420, 11.9040), (51.2330, 11.8860), (51.2240, 11.8760))),
                 dict(s="fr", k="move", p=ll((51.2700, 11.8470), (51.2570, 11.8620), (51.2470, 11.8780)))],
         events=[[51.2400, 11.9050, "Guns and baggage abandoned"]]),
    dict(t="16:45", label="Nightfall", title="St Germain and Loudon cover the withdrawal",
         text="St Germain's corps and Loudon's Croats form a rearguard just north-east of Pettstädt as darkness falls, and the wreck of the allied army streams away toward Freyburg and the Unstrut. The battle has lasted about ninety minutes. Prussian losses are roughly 550; the allies have lost about 10,000, about half of them prisoners, along with most of their artillery.",
         tactic=("Rearguard", "Fresh, formed troops at the rear slow a pursuer and let a beaten army escape. Here they mattered less than the coming of night."),
         arrows=[dict(s="fr", k="retreat", p=ll((51.2300, 11.8920), (51.2230, 11.8750), (51.2180, 11.8550))),
                 dict(s="re", k="retreat", p=ll((51.2220, 11.8760), (51.2180, 11.8600)))],
         events=[[51.2425, 11.8840, "Rearguard near Pettstädt"]]),
]

places = {
    "Rossbach": [51.2607, 11.8922], "Bedra": [51.2760, 11.8990], "Lunstädt": [51.2601, 11.9092],
    "Reichardtswerben": [51.2589, 11.9497], "Tagewerben": [51.2454, 11.9733], "Pettstädt": [51.2373, 11.8815],
    "Storkau": [51.2315, 11.9084], "Obschütz": [51.2268, 11.9125], "Schortau": [51.2758, 11.8735], "Leiha": [51.2644, 11.8759],
    "Almsdorf": [51.2594, 11.8619], "Branderoda": [51.2635, 11.8070], "Zeuchfeld": [51.2353, 11.8291],
    "Gröst": [51.2544, 11.8393], "Burgwerben": [51.2314, 11.9849], "Braunsbedra": [51.2860, 11.8855], "Großkayna": [51.2900, 11.9362],
}
hills = {"Janus Hill": [51.2666, 11.9333], "Polzen Hill": [51.2712, 11.9545]}
roads = [
    ["Branderoda", "Gröst", "Almsdorf", "Leiha", "Rossbach", "Lunstädt", "Reichardtswerben", "Tagewerben", "Burgwerben"],
    ["Zeuchfeld", "Pettstädt", "Storkau", "Obschütz"],
    ["Pettstädt", "Reichardtswerben"], ["Schortau", "Leiha"], ["Schortau", "Bedra", "Braunsbedra"], ["Rossbach", "Bedra"],
    ["Reichardtswerben", "Großkayna"], ["Storkau", "Tagewerben"], ["Gröst", "Zeuchfeld"], ["Rossbach", "Pettstädt"],
]
woods = [[51.2735, 11.9200, 380, 160], [51.2500, 11.8480, 300, 220], [51.2810, 11.8600, 420, 260]]

out = dict(phases=phases, units=units, hq=hq, places=places, hills=hills, roads=roads, woods=woods)
def rnd(o):
    if isinstance(o, float): return round(o, 5)
    if isinstance(o, (list, tuple)): return [rnd(x) for x in o]
    if isinstance(o, dict): return {k: rnd(v) for k, v in o.items()}
    return o
json.dump(rnd(out), open("scenario.json", "w"), ensure_ascii=False)
print(len(units), "units,", len(phases), "phases")
