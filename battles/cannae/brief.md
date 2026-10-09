# Cannae, 2 August 216 BC: research brief

## Scope and method

This is a tactical reconstruction of Cannae, not an attempt to locate every unit on a recoverable ancient grid. Polybius's account is the primary framework because it preserves the clearest sequence and order of the two armies. Livy is used both as an independent later narrative and to expose, rather than hide, the casualty disagreement. The available West Point and Rothert diagrams agree on the tactical geometry but are schematic, so they are not used as a georeferenced overlay.

The model anchors a low-confidence illustrative field north of the modern Ofanto near Canne della Battaglia. Mahaney's 2024 geomorphology confirms that the floodplain and terraces matter but does not settle the ancient river channel or exact field. Every coordinate-level placement is therefore low confidence; relative deployment and sequence are generally medium or high confidence.

## Sources

| id | source | kind | use | confidence |
|---|---|---|---|---|
| poly | Polybius, *Histories* 3.110-117 | primary | deployment, phases, numbers and losses | high for relative sequence; not a modern survey |
| livy | Livy, *Ab urbe condita* 22.44-54 | primary | later Roman account; casualty alternative | medium; later and more rhetorical |
| wp | U.S. Military Academy schematic, supplied locally | staff map | broad tactical relationship | medium; diagram, not coordinate evidence |
| roth | Rothert tactical diagram, supplied locally | period map | broad envelopment sequence | medium; diagram, not coordinate evidence |
| mahaney | Mahaney (2024), *Studia Quaternaria* 41, 37-42 | scholarly | Ofanto floodplain, terraces and landscape limits | medium-high for geomorphology |
| gold | Goldsworthy, *Cannae* (2001) | scholarly | identified bibliographically | medium; no map claim depends on it |
| data | AWS Terrain Tiles; OSM/Overpass | data | modern relief, waterway and change detection | high for present terrain only |

## Forces and losses

- **Romans:** Polybius gives about 80,000 infantry and a little more than 6,000 cavalry [poly]. The atlas uses 86,400 in the strength chart: 25,000 citizen heavy infantry, 30,000 allied heavy infantry, 15,000 light troops, 6,400 cavalry and a separately modelled 10,000-man camp garrison. Polybius says the camp garrison was captured after the field battle. This is a readable grouping, not an order of battle.
- **Carthaginians:** 50,000: 32,000 heavy infantry, 8,000 skirmishers and 10,000 cavalry [poly]. The centre, African wings and cavalry wings remain separate because their different tactical jobs are the point of the reconstruction.
- **Losses:** Polybius reports about 70,000 Roman dead and 5,700 Carthaginian dead; Livy reports 48,200 Roman and 8,000 Carthaginian dead [poly] [livy]. The chart adopts Polybius's totals only as an explicit illustrative allocation across phases.

## Phases

| # | time | reconstruction | confidence |
|---|---|---|---|
| 0 | 06:00 | Deployment: Romans face south; Hannibal's centre is advanced with African wings held back. | low spatial / medium tactical |
| 1 | 07:00 | Skirmishers fight without decision. | medium |
| 2 | 08:00 | Hasdrubal's Spanish and Celtic cavalry defeats the Roman right. | medium |
| 3 | 09:00 | Roman mass presses the yielding Spanish-Celtic centre. | medium |
| 4 | 10:00 | African wings turn inward; Hasdrubal helps the Numidians. | medium |
| 5 | 11:00 | Cavalry reaches the Roman rear; the ring closes. | medium |
| 6 | 12:00 | Destruction, camp captures and flight. | medium for outcome, low for exact duration |

## Disagreements and choices

1. **Battlefield location and river course — open.** The ancient Aufidus did not necessarily follow the modern Ofanto channel. The town of Cannae is a secure anchor, but the exact field is not. The map explicitly says this and sets coordinates low confidence [mahaney].
2. **Orientation — open.** Polybius says Romans faced south and Carthaginians north [poly]. Tactical diagrams differ in their page orientation and cannot resolve a modern-coordinate alignment. The map follows Polybius's relative facing only.
3. **Casualties — open.** Polybius and Livy diverge sharply. Both totals are cited; Polybius is used for the display because his unit totals also drive the model [poly] [livy].
4. **Clock time — fixed as illustrative.** Ancient sources give a sequence, not the exact hourly timestamps shown here. The labels are deliberately spaced to show causation and speed-checkable movement, not claims of a precise chronology.

## Terrain and modern change

The terrain pipeline ran on the current 240 × 205 grid. OSM detects a quarry at the south-east edge and masks it. The modern river and relief are useful orientation aids, not a restoration of 216 BC hydrology. No historical overlay is supplied because doing so from tactical diagrams would imply unjustified positional accuracy.

## Validation

Run `BATTLEKIT_STRICT=1 python3 scenario.py`. Expected: zero warnings. All groups carry sources and strength tracks; movements avoid the river and remain below the ancient-infantry/cavalry speed limits.

## Review responses

Pending independent review. The main known limitation is not a missing fact: it is the irreducible uncertainty of the battlefield's precise location and river channel, which this atlas presents as low confidence rather than resolving by guesswork.
