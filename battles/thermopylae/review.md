# Independent review (reviewer agent, 2026-10-17)

## Verdict

This should not be published in its current form. The narrative skeleton is sound and closely sourced: the day-by-day sequence, the contingents, the named individuals and the main Herodotean set pieces all check out against the text. The Kolonos and Kromayer "hill 2" identification is also correct. The weaknesses are in topography and historiography, which is where a map atlas will be judged.

Three problems matter most:
- **Phocian post and route.** The Phocian post and the dawn encounter use Kromayer's 1920s placement on the Sastani saddle. But the modern authorities the brief itself relies on for the route (Pritchett 1958/1982, MacKay 1963, Wallace 1980) put the Phocians on the hill near Nevropolis. The atlas's own route passes that hill at 01:00 in the dark, which no reading of Herodotus allows.
- **Width of the pass.** The drawn pass contradicts the brief's own figures. The text says 15–30 m; the geometry gives about 100–200 m between "sea" and slope at the wall. The battle strip also sits on a modern surface about 20 m above a sea that has been lowered to 0 m.
- **Order of battle.** The 1,000 Lacedaemonians recorded by Diodorus and Isocrates (usually read as perioikoi) are left out without comment.

There are also many smaller internal contradictions between brief, data and debate notes, and one misattribution to Diodorus. The newer scholarship the brief names (Lazenby, Green, Cartledge, Matthew and Trundle, Rop, Vouvalidis) was not read. Overall: reliable for the narrative, medium-to-low for the ground, and the confidence labels on the coastline and the mountain phases are too high.

## Issues

1. **Severity: high. Where:** unit `phocians` (phases 0, 6, 7); phase 6 ("Dawn on the summit"); brief, Disagreement 3; `SADDLE`/`SUMMIT`.
   - **What is wrong:** The Phocian post sits on Kromayer's Sastani saddle above Drakospilia. The modern alternative is credited only to "others" and a blog. In fact the standard modern placement is the hill near Nevropolis: Rop 2019, n. 26 says it "was the most likely location for the Phocian position, according to Pritchett (1958), 209–210 and (1982), 196 n. 50. Mackay (1963), 254–255 and Wallace (1980), 18 n. 22 agree". Kromayer's own map 5 also draws a dashed second "Stellung der Phoker" by Nevropolis (visible in `kv5.jpg`).
   - **Internal contradiction:** The brief follows the Pritchett/Wallace meadow route for the middle section. That route has the Immortals at `M1` (past Nevropoli) at 01:00, so they walk past the post those same scholars identify, in darkness and without contact. That contradicts Herodotus 7.217–218, where the encounter comes at dawn.
   - **Evidence:** J. Rop, "The Phocian Betrayal at Thermopylae", *Historia* 68 (2019) 413–435, n. 26, https://conservancy.umn.edu/items/a0255c6c-681f-4201-84e1-21c544728752 ; `sources/kv5.jpg` (dashed alternative position).
   - **Fix:** Pick one coherent scheme.
     - (a) Pritchett/Wallace throughout: the Phocians near Nevropolis, the dawn encounter there at about 05:00–05:15, then the descent by the saddle and the Alpenoi ravine. This also gives a more even march rate (see issue 8).
     - (b) Kromayer throughout: his Damasta–Alt-Drakospilia route and the saddle.
   - Either way, name the Nevropolis post as the majority modern view and cite Pritchett, MacKay and Wallace (through Rop if they are not read directly), not only the blog.

2. **Severity: high. Where:** `coast480.json` around the Middle Gate; `WALL_N`/`WALL_S`; the `meta.notes` "15–30 m" line; brief confidence summary ("High: … the general position of the 480 BC shore at the pass").
   - **What is wrong (width):** At the wall (lon 22.5352) the drawn coast is at 38.7963 and the slope steepens at about 38.7945. That is a strip of about 200 m, and the wall polyline is about 296 m long. At 22.5313 the strip is about 100 m. The brief and notes say 15–30 m and blame the 43 m grid. A 43 m grid cannot turn about 25 m into about 200 m; the coast line itself is placed differently.
   - **What is wrong (height):** The DEM height along the drawn coast at the Middle Gate is 18–26 m, while the "sea" polygon is lowered to 0 m. The 3D view will show the pass as a terrace on a 20 m bluff. The real cause is post-480 alluvium and travertine on top of the old ground. Stronk himself notes alluvium "at places up to 20 metres deep", and Kraft et al. attribute the present surface to later deposits.
   - **Evidence:** Kraft et al. 1987 gave the pass as "not more than 20–30 meters wide in 480", and Pritchett thought even that too wide (Reed College Humanities 110 notes, archived: https://web.archive.org/web/20201127012143/https://www.reed.edu/humanities/110Tech/Thermopylae.html). Livy 36.15.10 gives 60 passus (about 90 m) at the widest (via Stronk p. 167). Vouvalidis et al., *Geodinamica Acta* 23 (2010) 241–253, doi:10.3166/ga.23.241-253, is reported to put the battle ground wider. It was not read by the author and I could not reach the full text, which is itself a reason not to claim "high".
   - **Fix:**
     - Either move the 480 BC line at the Middle Gate to within about 20–50 m of the slope foot (Kraft), or keep Kromayer's 10 m line and say plainly that it gives about 100–200 m and conflicts with Kraft.
     - Lower the terrain inside the pass strip, or add a note on the buried surface.
     - Shorten the wall to the strip width.
     - Downgrade "shore at the pass" to medium.

3. **Severity: medium. Where:** order of battle (`forces.start`, unit `helots`, brief Overview).
   - **What is wrong:** Diodorus 11.4.5 ("of the Lacedaemonians one thousand, and with them three hundred Spartiates") and Isocrates, *Panegyricus* 90 ("a thousand picked soldiers of their own") both give 1,000 Lacedaemonians. Most modern reconstructions read these as perioikoi, and that reconciles the 3,100 of Herodotus 7.202 with the epigram's 4,000 Peloponnesians (7.228). The atlas's "standard" 7,100 is not the standard sum. The usual one adds both the 1,000 Lacedaemonians and the 900 helots (the author's own `wp_battle_of_thermopylae.txt`, line 64); the atlas swaps in 1,000 Locrians.
   - **Other gaps:** The unit name "Helots and Lacedaemonian light troops" blurs helots and perioikoi. Diodorus's 1,000 Malians are dropped without a note.
   - **Evidence:** Isocrates 4.90, tr. Norlin, https://cts.perseids.org/read/greekLit/tlg0010/tlg011/perseus-eng2/82-90 ; Diodorus 11.4.5–7 (local file).
   - **Fix:**
     - Add a "Lacedaemonians (perioikoi?)" unit of about 1,000, at low confidence, or explain why it is left out.
     - Rename the helot unit and keep the epigram/perioikoi reasoning separate from the helot reasoning.
     - Restate the total (about 8,100 with the Locrians at 1,000, or give the range).
     - Mention the Malians in the debate notes.

4. **Severity: medium. Where:** phase 3 narrative.
   - **What is wrong:** "Diodorus has picked men from every nation sent in, with whips at their backs [diod]." Diodorus 11.8.1–3 says the picked men were threatened with death and that the reserves blocked their flight. There are no whips. The whips are Herodotus 7.223, on day 3.
   - **Also:** Diodorus 11.8.2 says the Greek lines "which were wont to join in the battle by turns would not withdraw". That cuts against the rotation shown in this phase and belongs in the debate note.
   - **Evidence:** `sources/diodorus_11_4-11.txt`, line 44.
   - **Fix:** Change to "…threatened with death if they fled, with the reserves blocking their retreat [diod]" and add the no-rotation variant to the debate.

5. **Severity: medium. Where:** phase 1 narrative.
   - **What is wrong:** "Diodorus says … the Persians' light wicker shields". Diodorus 11.7.3 has "small round or irregularly shaped shields". "Wicker" (gerra) comes from Herodotus 7.61, which is not cited.
   - **Fix:** Quote Diodorus correctly, or cite Herodotus 7.61 for "wicker".

6. **Severity: medium. Where:** `SUMMIT` versus `SADDLE`.
   - **What is wrong:** On the project's own DEM (`terrain_raw.npy`), `SUMMIT` (38.7704, 22.5258) is at 993 m and `SADDLE` (38.7684, 22.5308) at 1,030 m. The Phocians flee "to the topmost peak" (Herodotus 7.218) but end up downhill and toward the pass. The highest ground within 800 m is about 1,124 m at about 38.7615, 22.5273, south of the saddle.
   - **Other inconsistency:** The brief says "summit S of it", but the data puts it west-north-west.
   - **Likely cause:** The kv5 georeference: RMSE 173 m, leave-one-out errors up to 582 m.
   - **Fix:** Snap `SUMMIT` to the DEM high point nearest Kromayer's "1048" spot height (or, under issue 1, to the Nevropolis hill), and correct the brief.

7. **Severity: medium. Where:** internal consistency across brief, scenario and data.
   - Wall to Kolonos: about 400 m in the brief; 190 m in the phase 0 debate; 199 m in the data. Kromayer's map 6 gives about 240 m between his GCPs.
   - Kolonos coordinates: 38.796, 22.539 in the brief versus 38.7958, 22.5371 used. That is about 170 m apart, and 22.539 is the Wikipedia point, not OSM or Wikidata.
   - Route length: "about 20 km" in the brief versus "about 18 km" in the phase 5 debate. Segment sums from the data are 11.7 km up plus 6.3 km down, before trail sinuosity.
   - Phase 6 time: 05:30 in the brief versus 05:45 in the data.
   - Greek dead or captured: "about 2,700" in the brief versus 7,100 − 4,675 = 2,425 implied by `forces`.
   - The day-3 sortie: "600–900 m W of the wall" versus `F3` at about 560 m.
   - **Fix:** Reconcile all of these to the data.

8. **Severity: medium. Where:** chronology, phases 5–9, `meta.sun`.
   - **Sunrise:** At latitude 38.8° N with declination +8°, sunrise is about 05:35 local apparent time and civil dawn about 05:08. "05:45 Dawn on the summit" is after sunrise. The phase 7 narrative (07:00) has Xerxes' sunrise libations, which belong about 1.5 h earlier.
   - **Immortals' pace:**
     - 20:00–01:00: about 9.5 km and a climb of about 1,000 m (about 1.9 km/h).
     - 01:00–05:45: 3.3 km (0.7 km/h).
     - 07:00–10:00: about 2.5 km.
     - 10:00–11:00: about 4.7 km, from Unter-Drakospilia by Alpenoi and the East Gate (a cart-track defile) to Kolonos. That is too fast for the head of a 10,000-man column, never mind deploying it.
   - **Fix:** Put dawn at 05:00–05:15 and smooth the march. Under issue 1(a), the Nevropolis encounter at dawn makes the timetable work naturally. Have the Immortals near Alpenoi by about 10:00 and arriving on the Greek rear at about 11:00–11:30.

9. **Severity: medium. Where:** historiography (brief "Disagreements"; phase 4 and 6 narratives; Myths section).
   - **What is wrong:** The narrative gives Herodotus's apologetic account as fact: Ephialtes revealing the path, and the Phocians surprised and simply standing aside. No modern challenge is mentioned. Rop (2019) argues the Persians knew of the Anopaea on arrival and that the Phocians deliberately stood aside, as a Delphic bid for control of the sanctuary.
   - **Overstated agreement:** The "near consensus" on the route hides a real split. Wallace (with Myres and Burn) favoured the Vardates ascent; Pritchett favoured the Kalkomata spring ascent (Reed notes, above).
   - **Not read directly:** Lazenby 1993, Green 1996, Cartledge 2006, Matthew and Trundle 2013, Kraft 1987 and Vouvalidis 2010 are all reached only through Wikipedia or Stronk.
   - **Fix:**
     - Add a debate note to phases 4 and 6 citing Rop, and Herodotus 7.213–214 on the rival informers (Onetes of Karystos and Korydallos of Antikyra).
     - Describe the route as "Kalkomata (Pritchett) or Vardates (Wallace) ascent".
     - Read at least Lazenby 1993, chapter 7, and Rapp's chapter in Matthew and Trundle 2013 before publishing.

10. **Severity: low. Where:** phase 9 narrative ("masses of arrowheads"); cited to `wp` only.
    - **What is wrong:** The finds are reported as "roughly 100 bronze and iron arrowheads and a few spearheads", and their attribution to Persians is not certain.
    - **Evidence:** A. R. Brown in Matthew and Trundle 2013, via https://scottmanning.com/content/these-weapons-killed-leonidas/ .
    - **Fix:** "Many (about 100) arrowheads", citing Brown 2013 or Marinatos's report rather than Wikipedia.

11. **Severity: low. Where:** `meta.sun` and brief Disagreement 8.
    - **What is wrong:** The date is given as "late August" while the sun is set for 1 September. Most scholars favour August (How and Wells; Burn; Hignett; Hammond; Lazenby 1993, 118–119). Sacks (1976), followed by Hammond (1988), argues for mid-September.
    - **Evidence:** Rop 2019, n. on the date.
    - **Fix:** Cite these and either set the sun for about 20 August or say why 1 September was chosen. The effect is only a few minutes.

12. **Severity: low. Where:** `strengthNote` and brief ("120,000 … the low end of modern estimates … only the low end fits the Malian plain's water and supply").
    - **What is wrong:** The author's own Wikipedia excerpt lists lower estimates (40,000 and 65,000), so 120,000 is not the low end. The water and supply reasoning has no source.
    - **Fix:** Call it "a commonly cited modern figure", give the range, and cite a logistics source or drop the claim.

13. **Severity: low. Where:** phase 4 narrative ("The path begins at the Asopus, where it flows out of its gorge").
    - **What is wrong:** Herodotus 7.216 says it begins "from the river Asopos, which flows through the cleft". Whether that means "where" is part of the route dispute (Reed notes).
    - **Fix:** Quote Herodotus and leave the gloss to the debate note.

14. **Severity: low. Where:** `meta.method` and scenario docstring ("checked against OSM's Phocian wall and Kolonos").
    - **What is wrong:** Both features are ground control points for the kv6 fit, so this is not an independent check. Anthele is a label centre with a 431 m leave-one-out error. The gazetteer's CHECK flags on Drakospilia and Damasta are never resolved in the brief. (The kv5 GCP is in fact Kromayer's *Ober*-Drakospilia.)
    - **Fix:** Reword as "georeferenced to"; drop Anthele or give it less weight; record the Ober-Drakospilia match.

15. **Severity: low. Where:** phase 0 narrative ("The Lacedaemonians are posted outside the wall").
    - **What is wrong:** Herodotus 7.208 describes this during the four waiting days, when the scout rode up, not on the first morning of fighting.
    - **Fix:** "When Xerxes' scout rode up during the wait, the Lacedaemonians happened to be posted outside the wall [hdt]."

16. **Severity: low. Where:** confidence labels.
    - Brief "High: … the general position of the 480 BC shore at the pass": should be medium (issue 2).
    - Unit `immortals`: labelled "medium", but its phase 5–8 positions are low. Split the label or mark it low.
    - Phase 9 "high for the place": acceptable, since Kolonos is Kromayer's hill 2 by the excavations. The coordinates still need fixing (issue 7).

## Verified

1. **The 1,000 Lacedaemonians.** Isocrates, *Panegyricus* 90 says the Lacedaemonians went to Thermopylae "with a thousand picked soldiers of their own". This independently supports Diodorus 11.4.5 and confirms that the atlas leaves out a well-attested contingent (issue 3). Source: https://cts.perseids.org/read/greekLit/tlg0010/tlg011/perseus-eng2/82-90
2. **Kolonos is Kromayer's hill 2.** Before Marinatos the last-stand hill was usually taken to be hill 1 by the Phocian wall; the arrowhead finds showed that "Kolonos Hill must be identified with Hill 2". This confirms the kv6 GCP choice and the brief's reading of Kromayer's "probably on hill 2". Source: Reed College Humanities 110, "Thermopylae" (archived), https://web.archive.org/web/20201127012143/https://www.reed.edu/humanities/110Tech/Thermopylae.html
3. **Kraft et al. 1987 on the pass width.** They concluded the pass was "not more than 20–30 meters wide in 480", and Pritchett judged even that too wide. This confirms the brief's figure, and with it the mismatch with the drawn coast (issue 2). Source: same Reed page; Kraft et al., *JFA* 14 (1987) 181–198.
4. **The Phocian post near Nevropolis.** This is the placement of Pritchett 1958 and 1982, MacKay 1963 and Wallace 1980. Confirmed; it contradicts the atlas's main choice (issue 1). Source: Rop, *Historia* 68 (2019) n. 26.
5. **The date.** Scholarly opinion is mostly August, with Sacks and Hammond arguing for mid-September. The brief's "August or September" is defensible. Source: Rop 2019, note on the date.
6. **Marinatos's 1939 finds on Kolonos.** About 100 bronze and iron arrowheads and a few spearheads; they moved the identification of the last-stand hill to Kolonos. The site is confirmed; the quantity is overstated in the atlas (issue 10). Source: Brown 2013, via https://scottmanning.com/content/these-weapons-killed-leonidas/
7. **Vouvalidis et al. 2010 exists as cited.** *Geodinamica Acta* 23: 241–253, doi:10.3166/ga.23.241-253 (checked on Crossref). It is a borehole study of more than 20 cores up to 35 m deep, and Stronk reports it as broadly confirming Herodotus. The author never read it.
8. **Internal checks against the listed sources:**
   - The "Oetaean mountains on the right, Trachinian on the left" (Herodotus 7.217) fits the drawn eastward plateau route.
   - The Greek unit strengths add up to 7,100.
   - The Persian blocks add up to 120,000.
   - Herodotus's compass rotation (Godley, via Stronk) is correctly stated.
   - The individuals check out against Herodotus: Demophilos, Leontiades, Dithyrambos, Abrocomes and Hyperanthes, Megistias, Eurytos, Aristodemos, Pantites, Tyrrhastiadas (Diodorus), and Ephialtes son of Eurydemos.

## Sources the author should add

- Isocrates, *Panegyricus* 90 (tr. G. Norlin, Loeb 1928).
- J. F. Lazenby, *The Defence of Greece 490–479 BC* (Warminster: Aris & Phillips, 1993), ch. 7, esp. 118–119 (date) and 134–148 (numbers, path, Phocians).
- P. Green, *The Greco-Persian Wars* (Berkeley: University of California Press, 1996), 113–149.
- P. Cartledge, *Thermopylae: The Battle That Changed the World* (London: Macmillan, 2006).
- C. A. Matthew and M. Trundle (eds.), *Beyond the Gates of Fire: New Perspectives on the Battle of Thermopylae* (Barnsley: Pen & Sword, 2013), especially G. Rapp on the topography of the pass and A. R. Brown on memory and the Kolonos finds.
- J. Rop, "The Phocian Betrayal at Thermopylae", *Historia* 68.4 (2019) 413–435, doi:10.25162/historia-2019-0022.
- K. Vouvalidis, G. Syrides, K. Pavlopoulos et al., "Palaeogeographical reconstruction of the battle terrain in Ancient Thermopylae, Greece", *Geodinamica Acta* 23 (2010) 241–253, doi:10.3166/ga.23.241-253.
- J. C. Kraft, G. Rapp, G. J. Szemler, C. Tziavos and E. W. Kase, "The Pass at Thermopylae, Greece", *Journal of Field Archaeology* 14.2 (1987) 181–198 (read directly, JSTOR 530139).
- W. K. Pritchett, "New Light on Thermopylai", *AJA* 62 (1958) 203–213; and *Studies in Ancient Greek Topography* IV (Berkeley, 1982) 176–210.
- P. W. Wallace, "The Anopaia Path at Thermopylai", *AJA* 84 (1980) 15–23.
- P. A. MacKay, "Procopius' *De Aedificiis* and the Topography of Thermopylai", *AJA* 67 (1963) 241–255.
- G. J. Szemler, W. J. Cherf and J. C. Kraft, *Thermopylai: Myth and Reality in 480 B.C.* (Chicago: Ares, 1996).
- M. A. Flower, "Simonides, Ephorus, and Herodotus on the Battle of Thermopylae", *Classical Quarterly* 48.2 (1998) 365–379 (on Diodorus's night attack).
- C. Hignett, *Xerxes' Invasion of Greece* (Oxford, 1963), 105–148 and 361–370.
- K. S. Sacks, "Herodotus and the Dating of the Battle of Thermopylae", *Classical Quarterly* 26 (1976) 232–248.
- W. W. How and J. Wells, *A Commentary on Herodotus*, vol. II (Oxford, 1912), notes on 7.175–233 and appendix on Thermopylae.
