# Rossbach, 5 November 1757: research brief (v2)

## Overview
- **Place:** Saxony, between Mücheln and Weissenfels, west of the Saale. The field is the plateau around Rossbach, Lunstädt and Reichardtswerben, with the low Janus and Pölzen hills.
- **Prussians:** Frederick II. 22,000 men: 27 battalions (17,000), 43 squadrons (5,000) and 79 guns [wiki]. The French staff plan gives 27 battalions, 45 squadrons and 21,600 [gal].
- **Allies:** Soubise (French) and Saxe-Hildburghausen (Reichsarmee). 41,110 men: 62 battalions, 84 squadrons and 109–114 guns; about 30,200 French and 10,900 Imperial [wiki]. The French plan gives 64,080 [gal]; see disagreement 1.
- **Losses:**
  - Prussians: about 550 (Bodart: 169–170 killed, 379–430 wounded); regimental studies give fewer [wiki].
  - Allies: about 10,000 (6,600 French and 3,552 Imperial), about 5,000 of them prisoners, with 72 guns and 21 standards lost [wiki].

## Sources
| id | source | kind | used for | reliability |
|---|---|---|---|---|
| gal | French staff plan 1:50,000, *Bataille de Rossbach le 5 novembre 1757* (19th century, BnF GE D-1165) | staff map | the **main positional source**: lettered positions (camps F, march P, battery L, Seydlitz N and M, infantry Q, Allied columns and rout S/O, Saint-Germain's rearguard H); georeferenced on 14 villages, RMSE 227 m, 8.5 m per pixel (its scale bar gives about 8) | high for the large-scale picture |
| planc | *Plan der Bataille ... bey Rossbach* No. 14 (1757), contemporary engraving | period map | the legend: Allied camp; Saint-Germain's corps; the march of the Imperial army in three columns; the Prussian camp, march and battle position | medium; geometrically distorted, so **not georeferenced** |
| plana | Nuremberg plan (1757) | period map | an independent picture of the movements | medium |
| eb | Atkinson, *Encyclopaedia Britannica* 11th ed. (1911), article and map | reference | camps; plan; march routes; 38 squadrons; Moller at 15:15; rally near Tagewerben; seven battalions engaged | medium-high |
| wiki | Wikipedia, "Battle of Rossbach" (citing Duffy, Showalter, Redman, Fuller, Bodart, Blanning, Clodfelter) | reference | strengths and losses; minute-by-minute sequence; Seydlitz's two lines (20 + 18); the rally; 7 squadrons left at Rossbach | medium-high |
| millar | Millar, *Rossbach and Leuthen 1757* (Osprey, 2002), bird's-eye plate (a screenshot supplied by Nathan) | scholarly | times 12:00–16:45; regiment-level order of battle with battalion and squadron counts | medium-high; only one plate seen |
| wpm | USMA map, "Maneuver for position, 2–4 Nov" | staff map | context before the battle | high, but outside the battle day |
| data | AWS Terrain Tiles; OSM place nodes and Overpass; Wikidata and Wikipedia | data | terrain; villages; mining features | high |

**Consulted but not usable:**
- The Prussian Great General Staff, *Der siebenjährige Krieg* vol. 5 (1903, archive.org `dersiebenjhrige00abtegoog`). The OCR of the blackletter text is unreadable.
- Kronoskaf. Its site answers with a robot check, which was not bypassed.

**Not consulted (not freely available):** Duffy, *Prussia's Glory* (2003) and *Frederick the Great: A Military Life*; Showalter; Redman. They reach this map only through Wikipedia, which is the main remaining gap in the scholarship.

## Phases
| # | time | summary | conf |
|---|---|---|---|
| 0 | 09:00 | The Prussian camp between Rossbach and Bedra faces west; the Allied camp runs from Branderoda to Mücheln; Saint-Germain holds the Schortau heights [wiki] [eb] [gal]. | high |
| 1 | 12:00 | The Allies march south by Zeuchfeld; Frederick watches from the manor roof [millar] [wiki]. | medium (11:00 or 12:00) |
| 2 | 14:30 | Gaudi's report; Frederick sees the Allies near Pettstädt; by 15:00 the camp is struck; the march goes behind the Janus and Pölzen [wiki] [eb]. | high |
| 3 | 15:15 | Moller opens fire from the Janus; Seydlitz forms two lines behind the Pölzen (N on the plan) [wiki] [gal]. | medium |
| 4 | 15:30 | First charge with 20 squadrons; the second line of 18 follows; the Allied cavalry is broken within about 30 minutes [wiki]. | medium |
| 5 | 15:45 | The melee drifts south; Seydlitz rallies about 2 km away; the Prussian infantry forms in echelon [wiki]. | low (rally location) |
| 6 | 16:00 | The Allied columns attack with the bayonet; Prince Henry's volleys; about seven Prussian battalions fire [wiki] [eb]. | medium |
| 7 | 16:15 | The second charge with all 38 squadrons; the Franconian regiments break [wiki] [millar]. | medium |
| 8 | 16:30 | The rout goes south-west (S and O on the plan); the pursuit ends at dark [wiki] [gal]. | medium |
| 9 | 16:45 | Saint-Germain and Loudon cover the withdrawal (H) [millar] [gal]. | high |

## What changed from v1, and why
1. **Village positions.** The v1 geocoder (Nominatim) returned district centroids: **Reichardtswerben was 1.3 km and Tagewerben 1.7 km too far north-east,** and Gröst and Storkau about 1 km off. v2 uses OSM settlement nodes cross-checked with Wikidata (`tools/gazetteer.py`), confirmed by the georeferenced French plan. The cavalry clash, the rally and the Prussian line all moved with them.
2. **Positions read from a georeferenced period source** (the French 1:50,000 plan) instead of being placed by eye from a screenshot.
3. **Seydlitz's charge.** In v1 all 38 squadrons charged together. v2 has the first line of 20, then the second of 18 [wiki].
4. **The flank guard at Rossbach:** Mayr's battalion plus seven squadrons [wiki].
5. **The Allied march:** three columns (first line, second line, reserve) with Piémont and Mailly at the head and the Austrian cuirassiers and Imperial cavalry in front of the right column [wiki]; the reserve artillery stuck between the columns.
6. **Strengths and losses** are now carried per unit through the day.
7. **Terrain.**
   - Flooded pits are detected automatically: Großkaynaer See, Runstedter See, Hassesee, the **Geiseltalsee** (2,026 ha) and three unnamed pits.
   - The Leuna spoil heap is also detected.
   - Two spoil heaps north of Bedra are masked by hand: flagged by the elevation check, rectangular and flat-topped.
   - The Janus and Pölzen hills are positioned from the plan (Pölzen moved 1.2 km east of the v1 guess).
   - Compared with v1's hand masks, the automatic pass found every pit v1 had and more; only the heaps needed a human.
8. **Speed checks** caught v1-style impossible moves (2 km in 15 minutes) that are now fixed.

## Disagreements and the choices made
1. **Allied strength.** The French staff plan gives 64,080 (38 Imperial and 52 French battalions). The modern consensus (Duffy, via Wikipedia) is 41,110 present on the field. The plan's figure probably counts the whole army including detachments; **41,110 is used.**
2. **Start of the Allied march:** "after eleven" [wiki] against 12:00 [millar]. Noon is used, with a debate note.
3. **Where Seydlitz rallied:** a copse between Reichardtswerben and Obschütz [wiki, after Redman] against near Tagewerben [eb]. The two are about 1 km apart; the map places it between them, at low confidence.
4. **Prussian losses:** from "negligible" (Frederick) to about 600 (Bodart); about 550 is used, with a debate note.
5. **Regimental grouping and per-unit strengths** are estimates from Millar's battalion and squadron counts. The army totals are sourced.

## Validation
`BATTLEKIT_STRICT=1 python3 scenario.py` passes with 0 warnings.

## Review responses
(see review.md, after the independent review)
