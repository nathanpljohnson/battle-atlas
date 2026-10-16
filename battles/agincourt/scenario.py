"""Agincourt, 25 October 1415.

The site itself is debated (see brief.md), so positions are measured from Azincourt, Tramecourt
and Maisoncelle using the chroniclers' distances, the 1899 sketch map (georeferenced, 175 m) and
the modern schematic. All coordinates are low confidence; the relative order is the claim.
"""
import os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "..", "tools"))
os.chdir(HERE)
from battlekit import Battle

B = Battle("agincourt", HERE)
AX = 2.1395  # the field's north-south axis, midway between the villages

B.source("nic", "N. Harris Nicolas, History of the Battle of Agincourt (2nd ed., London, 1833), with translated passages from Le Fèvre de Saint-Remy, Monstrelet, Elmham, Titus Livius and the Gesta Henrici Quinti", "https://archive.org/details/historyofbattl00nico", "eyewitness and near-contemporary accounts: the distances between the armies, the French waiting until nine or ten, the stakes, the denial of the hidden-archer story", "primary")
B.source("wp", "Wikipedia, 'Battle of Agincourt' (after Curry 2005, Barker 2005, Sumption 2015, Rogers 2008, Mortimer 2009, Keegan 1976, Sutherland 2015)", "https://en.wikipedia.org/wiki/Battle_of_Agincourt", "the French order of battle, the course of the fighting, losses, and the numbers and site debates", "reference")
B.source("mon", "Enguerrand de Monstrelet, Chronicles, tr. T. Johnes (London, 1840), book I, chs. 146-147", "https://deremilitari.org/RESOURCES/SOURCES/agincourt.htm", "Burgundian chronicler: French order of battle and commanders, the mounted wing reduced to seven score, the Marle-Fauquembergue charge, the raiders, English dead about 1,600", "primary")
B.source("frwp", "Wikipédia, 'Bataille d'Azincourt'", "https://fr.wikipedia.org/wiki/Bataille_d%27Azincourt", "French-language cross-check of the order of battle and commanders", "reference")
B.source("fbb", "Famous British Battles from Crécy to Assye (London, 1899), 'Battle of Azincourt' map", "https://commons.wikimedia.org/wiki/File:Image_taken_from_page_152_of_%27Famous_British_Battles,_from_Cr%C3%A9cy_to_Assye_..._With_original_plans_and_maps._And_illustrations_by_R._Caton_Woodville%27_(11248468233).jpg", "north-up sketch of villages, woods and the two armies; georeferenced on five villages (RMSE 175 m)", "period-map")
B.source("wpmap", "Wikimedia Commons, 'Map Agincort.svg' (schematic)", "https://commons.wikimedia.org/wiki/File:Map_Agincort.svg", "relative order of the battles, archers and French lines; no scale", "staff-map")
B.source("hardy", "E. Hardy, plan of the battle of Azincourt (19th century)", "https://commons.wikimedia.org/wiki/File:Position_troupes_bataille_d%27Azincourt.jpg", "dissenting French plan placing the French around and west of Azincourt; recorded, not followed", "period-map")
B.source("data", "AWS Terrain Tiles; OpenStreetMap and Wikidata (village positions)", "https://registry.opendata.aws/terrain-tiles/", "modern elevation and place coordinates", "data")

B.meta = {
    "title": "Agincourt", "year": "1415", "era": "medieval", "war": "Hundred Years' War",
    "eyebrow": "25 October 1415 · Artois · Hundred Years' War",
    "subtitle": "A sick, outnumbered English army lets the French come to it across a muddy field between two woods.",
    "sides": {
        "en": {"name": "English", "top": "#b23a2e", "side": "#7a241c", "mark": "#f6efe2", "arrow": "#d9573f", "flag": "#b23a2e"},
        "fr": {"name": "French", "top": "#2a3f8f", "side": "#1b2a60", "mark": "#e9c75a", "arrow": "#5577d0", "flag": "#2a3f8f"},
    },
    "belligerents": [
        {"name": "English army", "short": "English", "commander": "Henry V", "sides": ["en"], "code": "letters"},
        {"name": "French army", "short": "French", "commander": "Constable d'Albret and Marshal Boucicaut", "sides": ["fr"], "code": "numbers"},
    ],
    "forces": {
        "start": [{"label": "English", "n": 8000, "segs": [["en", 1]]}, {"label": "French", "n": 20500, "segs": [["fr", 1]]}],
        "end": [{"label": "English", "n": 135, "segs": [["en", 1]]}, {"label": "French", "n": 7600, "segs": [["fr", 1]]}],
    },
    "sun": {"lat": 50.46, "decl": -15.2, "note": "25 October 1415 in the Julian calendar is 3 November in ours; sunrise about 07:15 local solar time. Times are approximate: the chroniclers give only 'nine or ten' and 'about three hours' of fighting [nic] [wp]."},
    "view": {"az": 0.0, "el": 0.9}, "unitScale": 1.3, "unitLabelDist": 7,
    "ground": {"season": "autumn", "relief": 60},
    "strengthNote": "English about 8,000 (Curry, from pay records) against Barker's, Sumption's and Rogers's 6,000; French about 10,000 men-at-arms and 4,500 missile troops plus a mounted rearguard of unknown size (about 5,000 shown), against Curry's 12,000 and Rogers's 24,000 [wp] [mon]. The French lost about 6,000 dead and 700-2,200 captured [wp]. English dead: at least 112 are named in the records; Monstrelet gives about 1,600 [wp] [mon]; the chart shows roughly the record minimum. Losses per moment are estimates following the narrative.",
    "method": "The exact field is debated, so positions are measured from Azincourt, Tramecourt and Maisoncelle using the chroniclers' distances between the armies [nic], the order of battle reconstructed by modern historians [wp], and an 1899 sketch map georeferenced on five villages [fbb]. Woods are drawn schematically where the maps show them, not from today's woodland. Treat every coordinate as approximate; the relative positions and sequence are the firmer claim.",
    "notes": "The traditional site between the Azincourt and Tramecourt woods is shown; Sutherland (2005) and Livingston (2023) have argued for a field west of Azincourt [wp]. No historical-map overlay is offered. The modern terrain is used as is. The wind is not recorded; drifting dust is illustrative. Per-moment losses are estimates.",
}

B.place("Azincourt", size=0.8); B.place("Tramecourt", size=0.8); B.place("Maisoncelle", size=0.7)
B.place("Ruisseauville", size=0.7); B.place("Canlers", size=0.5)
B.woods = [[50.4585, 2.1265, 480, 750], [50.4600, 2.1530, 520, 850], [50.4655, 2.1245, 260, 300], [50.4670, 2.1545, 300, 320]]
B.roads = [["Azincourt", (50.4634, 2.1395), "Tramecourt"], ["Ruisseauville", (50.4700, 2.1350), (50.4600, 2.1395), "Maisoncelle"], ["Canlers", "Tramecourt"]]
B.hill("Calvaire (French grave pits)", (50.4652, 2.1406))

def U(uid, side, typ, name, strength, frontage, keys, note, conf, men, cite, via=None):
    u = B.unit(uid, side, typ, name, strength, frontage, note=note, conf=conf, men=men, cite=cite)
    for phase, (pos, facing, form, *bend) in keys.items():
        u.at(phase, pos, facing, form, via=(via or {}).get(phase), bend=bend[0] if bend else 0)
    return u

# Lines follow the 1899 map's placement (English arrows end ~50.459-50.463, French ~50.466-50.470) and
# OSM's calvary (grave pits) at 50.4652; the English array is ~870 m, inside the gap between the woods.
E0, E1 = 50.4560, 50.4630   # English line at dawn, and after the advance to within bowshot
F0 = 50.4660                # French vanguard front at dawn, north of the Azincourt-Tramecourt road
# ---- English: three battles of men-at-arms four deep, archers on the flanks behind stakes
for uid, name, dx, men, cmd in [("camoys", "Left battle (Lord Camoys)", -0.0021, {0: 500, 4: 495, 5: 490}, "Thomas, Lord Camoys, an old soldier, held the left by the Azincourt wood [wp]."),
                                ("henry", "Centre battle (Henry V)", 0.0, {0: 500, 4: 490, 5: 480}, "Henry fought in the front rank; he stood over his wounded brother Gloucester, and a blow struck a fleuron from his crown [wp] [nic]."),
                                ("york", "Right battle (Duke of York)", 0.0021, {0: 500, 4: 470, 5: 440}, "Edward, Duke of York, commanded the right and was killed in the press [wp] [mon].")]:
    U(uid, "en", "hi", name, f"~{men[0]} men-at-arms", 150,
      {0: ((E0, AX + dx), 0, "L"), 1: ((E1, AX + dx), 0, "L"), 3: ((E1, AX + dx), 0, "F"), 4: ((E1 - 0.0003, AX + dx), 0, "F")},
      note=cmd, conf="medium", men=men, cite=["wp", "nic", "mon", "wpmap"])
U("archers_l", "en", "arc", "Archers of the left wing", "~2,900 archers", 160,
  {0: ((E0 + 0.0004, AX - 0.0050), 20, "L"), 1: ((E1 + 0.0004, AX - 0.0050), 20, "L"), 2: ((E1 + 0.0004, AX - 0.0050), 20, "F"), 4: ((E1 + 0.0007, AX - 0.0046), 60, "F")},
  "Several deep behind sharpened stakes, anchored on the Azincourt wood; at the crisis they left the stakes with hatchets and mallets [wp].", "medium", {0: 2900, 4: 2890, 5: 2885}, ["wp", "nic", "wpmap"])
U("archers_r", "en", "arc", "Archers of the right wing", "~2,900 archers", 160,
  {0: ((E0 + 0.0004, AX + 0.0050), 340, "L"), 1: ((E1 + 0.0004, AX + 0.0050), 340, "L"), 2: ((E1 + 0.0004, AX + 0.0050), 340, "F"), 4: ((E1 + 0.0007, AX + 0.0046), 300, "F")},
  "The mirror of the left wing, on the Tramecourt wood; Sir Thomas Erpingham gave the archers the signal to shoot [wp].", "medium", {0: 2900, 4: 2890, 5: 2885}, ["wp", "nic", "wpmap"])
U("archers_c", "en", "arc", "Archers between the battles (disputed)", "~600 archers", 60,
  {0: ((E0 + 0.0004, AX - 0.00105), 0, "L"), 1: ((E1 + 0.0004, AX - 0.00105), 0, "L"), 2: ((E1 + 0.0004, AX - 0.00105), 0, "F")},
  "Whether archers also stood in wedges between the battles is a long-running debate; shown small and low-confidence [wp].", "low", {0: 600, 4: 595}, ["wp"])
U("baggage", "en", "hi", "Baggage, camp and its guard", "~200 guards and servants", 200,
  {0: ("Maisoncelle", 0, "L"), 6: ((50.4478, 2.1430), 300, "F")},
  "The baggage was left at Maisoncelle with a small guard [wp].", "low", {0: 200, 6: 190}, ["wp"])

# ---- French (facing south: their left is the east, Tramecourt side)
for uid, name, dx, men in [("van_w", "Vanguard, west (d'Albret, Boucicaut, Orléans)", -0.0030, {0: 1600, 4: 900, 5: 300, 6: 150}),
                           ("van_c", "Vanguard, centre (d'Albret, Boucicaut, Bourbon)", 0.0, {0: 1600, 4: 800, 5: 250, 6: 150}),
                           ("van_e", "Vanguard, east (Eu, Richemont)", 0.0030, {0: 1600, 4: 900, 5: 300, 6: 150})]:
    U(uid, "fr", "hi", name, f"~{men[0]:,} men-at-arms on foot", 280,
      {0: ((F0, AX + dx), 180, "L"), 2: ((F0 - 0.0004, AX + dx * 0.9), 180, "L"), 3: ((E1 + 0.0016, AX + dx * 0.75), 180, "L", -0.05), 4: ((E1 + 0.0007, AX + dx * 0.75), 180, "F", -0.08), 6: ((F0 + 0.0020, AX + dx), 0, "R")},
      note="The vanguard, with almost all the great lords; it converged on the three English banners and jammed. About 4,800 men-at-arms in the Somme battle plan, about 8,000 in Monstrelet [wp] [mon].",
      conf="medium", men=men, cite=["wp", "mon", "nic", "wpmap"])
U("vendome", "fr", "hi", "Vendôme's wing (French left, east)", "~1,500 men-at-arms on foot", 220,
  {0: ((F0 + 0.0008, AX + 0.0060), 200, "L"), 3: ((E1 + 0.0020, AX + 0.0050), 200, "L"), 4: ((E1 + 0.0012, AX + 0.0045), 200, "F"), 5: ((F0 + 0.0015, AX + 0.0055), 20, "R")},
  "The Count of Vendôme's wing was to fall on the English right flank (Monstrelet gives 1,500; the battle plan 600) [mon] [wp].", "low", {0: 1500, 4: 900, 5: 600}, ["mon", "wp", "frwp"])
U("clignet", "fr", "kn", "Mounted wing (Clignet de Brabant and Louis de Bosredon)", "800 planned, ~140 charged", 200,
  {0: ((F0 - 0.0006, AX - 0.0060), 180, "L"), 2: ((E1 + 0.0013, AX - 0.0048), 170, "F"), 3: ((F0 + 0.0060, AX - 0.0045), 0, "R")},
  "Eight hundred picked horsemen meant to ride down the archers on the English left; Monstrelet says they were 'reduced to seven score' when they charged, and Sir William de Saveuse, riding ahead, was shot dead [mon] [wp].", "low", {0: 800, 1: 140, 3: 80}, ["mon", "wp", "nic"], {3: [(F0 - 0.0002, AX - 0.0062)]})
for uid, name, dx in [("main_w", "Main battle, west (Duke of Alençon)", -0.0020), ("main_e", "Main battle, east (Duke of Bar)", 0.0020)]:
    U(uid, "fr", "hi", name, "~1,500 men-at-arms on foot", 300,
      {0: ((F0 + 0.0028, AX + dx), 180, "L"), 4: ((F0 + 0.0010, AX + dx), 180, "L"), 5: ((E1 + 0.0016, AX + dx), 180, "F", -0.05), 6: ((F0 + 0.0040, AX + dx * 1.5), 0, "R")},
      note="The second line, a bowshot behind the vanguard; it joined the press and was swallowed by it. Alençon was killed [wp] [mon].",
      conf="medium", men={0: 1500, 5: 900, 6: 750}, cite=["wp", "mon", "frwp"])
for uid, name, dx in [("missile_w", "Archers and crossbowmen, west", -0.0045), ("missile_e", "Archers and crossbowmen, east", 0.0045)]:
    U(uid, "fr", "arc", name, "~2,250 archers and crossbowmen", 250,
      {0: ((F0 + 0.0050, AX + dx), 180, "L"), 7: ((F0 + 0.0100, AX + dx), 0, "R")},
      note="Monstrelet gives the vanguard 4,000 archers and 1,500 crossbowmen; put behind the men-at-arms, they played almost no part [mon] [wp].",
      conf="low", men={0: 2250, 6: 2200}, cite=["mon", "wp"])
U("rearguard", "fr", "kn", "Rearguard (Marle, Dammartin, Fauquembergue, Louvroy)", "~5,000 mounted men (a guess)", 600,
  {0: ((F0 + 0.0080, AX), 180, "L"), 6: ((F0 + 0.0070, AX), 180, "L"), 7: ((50.4800, AX - 0.0020), 0, "R")},
  "Largely armed servants on their masters' horses, with few leaders left once the lords went forward; its size is unknown (Rogers's 10,000 gros valets would be the upper bound) [mon] [wp].", "low", {0: 5000, 6: 4400}, ["mon", "wp"])
U("marle", "fr", "kn", "Marle and Fauquembergue's last charge", "~600 men-at-arms", 220,
  {0: ((F0 + 0.0075, AX + 0.0010), 180, "L"), 6: ((E1 + 0.0010, AX + 0.0010), 180, "F"), 7: ((E1 + 0.0010, AX + 0.0010), 180, "R")},
  "The Counts of Marle and Fauquembergue rallied about 600 men-at-arms from the rearguard and charged; all were killed or taken [mon].", "low", {0: 600, 6: 300, 7: 30}, ["mon", "frwp"])
U("brabant", "fr", "hi", "Duke of Brabant's late arrival", "~200 men", 120,
  {0: ((50.4840, 2.1450), 200, "C"), 4: ((50.4760, 2.1430), 200, "C"), 5: ((E1 + 0.0018, AX + 0.0030), 190, "F")},
  "Antoine of Brabant was still marching that morning; he rode ahead of his troops, improvised a coat of arms from a trumpet banner, charged in and was killed [wp].", "low", {0: 200, 5: 40}, ["wp", "frwp"])
U("raiders", "fr", "lt", "Ysembart d'Azincourt's raiders", "~600 peasants with a few men-at-arms", 250,
  {0: ("Azincourt", 120, "X"), 5: ((50.4520, 2.1270), 120, "C"), 6: ((50.4486, 2.1410), 120, "F"), 7: ((50.4445, 2.1300), 250, "R")},
  "Local men under Ysembart d'Azincourt, Robinet de Bournonville and Riflart de Clamasse raided the English baggage; planned or opportunist, and when, are disputed [mon] [wp].", "low", {0: 650}, ["mon", "wp"], {5: [(50.4560, 2.1250)], 6: [(50.4495, 2.1350)]})

B.commander("henry_hq", "en", "Henry V", {0: (E0 - 0.0003, AX), 1: (E1 - 0.0003, AX)}, "The king fought with the centre battle [wp].")
B.commander("albret", "fr", "d'Albret", {0: (F0 + 0.0003, AX), 3: (E1 + 0.0019, AX), 4: (E1 + 0.0010, AX)}, "The Constable led the vanguard and was killed in it [wp].")
B.commander("alencon", "fr", "Alençon", {0: (F0 + 0.0031, AX - 0.0020), 5: (E1 + 0.0019, AX - 0.0012)}, "Alençon led the main battle and was killed close to Henry [wp].")

B.phase("07:30", "Dawn", "Two armies between two woods",
  "Henry's sick and hungry army, about 8,000 strong and mostly archers, draws up in three battles across the field north of Maisoncelle, archers on the flanks [wp]. The French block the road to Calais between the woods of Azincourt and Tramecourt: a dense dismounted vanguard, a main battle a bowshot behind, cavalry on the flanks, missile troops and a mounted rearguard at the back [wp]. Between the two camps the night before, the chroniclers give anything from a quarter of a mile to four bowshots [nic] [mon]; the dawn gap of about a kilometre shown here is a modern estimate.",
  ("Waiting on the defensive", "Period manuals held that the side which advances on foot against a standing enemy loses; both sides knew it and waited [wp].", "defensive-waiting"), (50.4588, AX), 3.6,
  events=[((50.4634, AX), "The French stand across the road to Calais [wp]", ["wp"]), ("Maisoncelle", "The English camped at Maisoncelle overnight in rain and silence [wp]", ["wp"])],
  conf="medium", cite=["wp", "nic", "mon", "fbb", "wpmap"],
  debate="The site itself is disputed: the traditional field between the woods is shown, but Sutherland (2005) and Livingston (2023) argue for ground west of Azincourt [wp]. Strengths range from Curry's 8,700 English against 12,000 French to Rogers's 6,000 against 24,000 [wp].")
B.phase("10:30", "Henry advances", "Banners forward, stakes replanted",
  "The French wait for reinforcements; by Le Fèvre's account they stood eating, drinking and making peace with one another until nine or ten [nic]. Henry cannot wait, so he moves the whole army forward to within long bowshot, and the archers pull up their stakes, carry them and drive them in again [wp].",
  ("Provoking the attack", "Moving close enough to hurt the enemy can force a waiting opponent to attack on your terms.", "provoke-attack"), (50.4605, AX), 3.0,
  arrows=[B.arrow("en", "move", (E0 + 0.0005, AX), (E1 - 0.0004, AX)), B.arrow("en", "move", (E0 + 0.0008, AX - 0.0050), (E1, AX - 0.0050)), B.arrow("en", "move", (E0 + 0.0008, AX + 0.0050), (E1, AX + 0.0050))],
  events=[((E1 + 0.0004, AX - 0.0050), "Archers re-plant their stakes within bowshot [wp]", ["wp"])], conf="medium", cite=["nic", "wp"])
B.phase("11:00", "The cavalry charge", "The horns break on the stakes",
  "The arrow storm provokes the French. The mounted wing meant to ride down the archers on the English left has dwindled from 800 to about seven score; Sir William de Saveuse, riding ahead, is shot dead [mon]. The woods prevent any outflanking and the stakes stop the rest; wounded horses bolt back through the advancing vanguard [wp] [nic].",
  ("Field obstacles", "Stakes, pits or carts in front of missile troops break a mounted charge and leave the riders to the archers.", "field-obstacles"), (50.4612, AX), 2.6,
  arrows=[B.arrow("en", "fire", (E1 + 0.0004, AX - 0.0050), (F0 - 0.0002, AX - 0.0040)), B.arrow("en", "fire", (E1 + 0.0004, AX + 0.0050), (F0 - 0.0002, AX + 0.0040)),
          B.arrow("fr", "charge", (F0 - 0.0006, AX - 0.0060), (E1 + 0.0010, AX - 0.0049))],
  events=[((E1 + 0.0010, AX - 0.0049), "Horses fall on the stakes; the survivors flee back through their own men [wp] [mon]", ["wp", "mon"])], conf="low", cite=["wp", "nic", "mon"])
B.phase("11:15", "The vanguard advances", "Through the mud, into the funnel",
  "The French vanguard advances on foot through newly ploughed, rain-soaked ground, visors down under the arrows. The field narrows towards the English, and the mass converges on the three English banners until, as Monstrelet puts it, all but the front rank could not raise their hands [wp] [mon].",
  ("Crowding on a narrow front", "Too many men on too little ground cannot use their numbers; the press itself becomes the enemy.", "narrow-front"), (50.4612, AX), 2.4,
  arrows=[B.arrow("fr", "move", (F0 - 0.0004, AX - 0.0032), (E1 + 0.0016, AX - 0.0024)), B.arrow("fr", "move", (F0 - 0.0004, AX), (E1 + 0.0016, AX)), B.arrow("fr", "move", (F0 - 0.0004, AX + 0.0032), (E1 + 0.0016, AX + 0.0024)),
          B.arrow("en", "fire", (E1 + 0.0004, AX - 0.0050), (E1 + 0.0016, AX - 0.0025)), B.arrow("en", "fire", (E1 + 0.0004, AX + 0.0050), (E1 + 0.0016, AX + 0.0025))],
  events=[((E1 + 0.0020, AX), "Men sink to the knees in the mud before they reach the enemy (monk of Saint-Denis) [wp]", ["wp"])], conf="medium", cite=["wp", "mon"])
B.phase("11:30", "The press", "Heaps of dead at the three banners",
  "The French front reaches the English men-at-arms and pushes them back, but the dead and fallen pile up and the living are pressed onto them from behind. The archers come out from the stakes with hatchets, swords and mallets against the flanks of the jammed mass [wp]. York is killed; Henry stands over his wounded brother Gloucester [wp].",
  ("Combined arms", "Archers who can also fight hand to hand, beside steady men-at-arms, turn a stalled attack into a massacre.", "combined-arms"), (50.4605, AX), 2.0,
  arrows=[B.arrow("en", "charge", (E1 + 0.0007, AX - 0.0046), (E1 + 0.0009, AX - 0.0030)), B.arrow("en", "charge", (E1 + 0.0007, AX + 0.0046), (E1 + 0.0009, AX + 0.0030))],
  events=[((E1 + 0.0006, AX), "The Gesta describes heaps of slain higher than a man around the three English standards [wp]", ["wp"]), ((E1 + 0.0004, AX + 0.0021), "The Duke of York is killed [wp]", ["wp"])],
  conf="medium", cite=["wp", "nic"],
  debate="Historians debate how many the arrows killed, against how many died in the crush, the mud and close combat; modern accounts (Keegan, Rogers, Barker) give the arrows chiefly a disordering and funnelling role [wp].")
B.phase("12:30", "The main battle", "The second line is swallowed",
  "The French main battle comes up into the same press and is engulfed. The Duke of Alençon is killed close to Henry, and the Duke of Brabant, arriving late with a borrowed banner for a coat of arms, charges in and is killed [wp].",
  ("Committing the reserve", "Feeding a second line into a front that has already jammed adds victims, not weight.", "reserve-commitment"), (50.4610, AX), 2.2,
  arrows=[B.arrow("fr", "move", (F0 + 0.0010, AX - 0.0020), (E1 + 0.0018, AX - 0.0020)), B.arrow("fr", "move", (F0 + 0.0010, AX + 0.0020), (E1 + 0.0018, AX + 0.0020)), B.arrow("fr", "charge", (50.4760, 2.1430), (E1 + 0.0020, AX + 0.0030))],
  events=[((E1 + 0.0010, AX - 0.0010), "Alençon killed close to the king [wp]", ["wp"]), ((E1 + 0.0018, AX + 0.0030), "Brabant arrives and is killed [wp]", ["wp"])], conf="low", cite=["wp", "frwp"])
B.phase("13:30", "Alarm in the rear", "The prisoners are killed",
  "Ysembart d'Azincourt's raiders fall on the baggage at Maisoncelle and carry off some of the king's treasures, including a crown [wp] [mon]. In front, the Counts of Marle and Fauquembergue rally about 600 men-at-arms from the rearguard and charge; all are killed or taken [mon]. With thousands of prisoners behind his weary men and the rest of the rearguard still on the field, Henry orders all but the most valuable prisoners killed [wp].",
  ("A threat to the rear", "A real or apparent threat behind the line can force a commander into drastic measures to keep his army intact.", "rear-threat"), (50.4545, AX), 3.6,
  arrows=[B.arrow("fr", "charge", (50.4520, 2.1270), (50.4495, 2.1350), (50.4486, 2.1410)), B.arrow("fr", "charge", (F0 + 0.0072, AX + 0.0010), (E1 + 0.0012, AX + 0.0010))],
  events=[((50.4486, 2.1420), "Raid on the English baggage at Maisoncelle [wp] [mon]", ["wp", "mon"]), ((E1 + 0.0012, AX + 0.0010), "Marle and Fauquembergue's charge is destroyed [mon]", ["mon"]), ((E1 - 0.0010, AX), "Henry orders the prisoners killed [wp]", ["wp"])], conf="low", cite=["wp", "nic", "mon"],
  debate="Barker, following the Gesta (whose author was with the baggage), puts the raid at the start of the battle; Le Fèvre and Monstrelet place it during the later fighting, where it helps explain the killing of the prisoners. This map follows the later timing [wp] [nic] [mon].")
B.phase("14:30", "The rearguard leaves", "The French give up the field",
  "Apart from the doomed charge, most of the rearguard does not attack; it leaves northward with the remaining missile troops, and the English hold the field [wp] [mon]. The French have lost about 6,000 dead, including the Constable, three dukes and nine counts, and 700 to 2,200 prisoners [wp].",
  ("Decisive battle", "A defeat that destroys a generation of leaders can matter more politically than the ground won.", "decisive-battle"), (50.4630, AX), 3.8,
  arrows=[B.arrow("fr", "retreat", (F0 + 0.0065, AX), (50.4790, AX - 0.0020))],
  events=[((50.4652, 2.1406), "The French dead were later buried in great pits; a calvary marks the traditional site [wp]", ["wp"])], conf="low", cite=["wp", "mon"])

B.export()
