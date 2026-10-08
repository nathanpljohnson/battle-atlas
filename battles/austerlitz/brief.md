# Austerlitz, 2 December 1805: research brief (v2)

## Overview
- **Place:** Moravia, between Brünn (Brno) and Austerlitz (Slavkov u Brna). The battle was fought around the Pratzen plateau and the Goldbach brook. Places are identified with `tools/gazetteer.py` (Bosenitz is Tvarožná, not Podolí).
- **French:** Napoleon. About 73,000 men and 139–157 guns. The order of battle (Duffy and Smith) gives 73,000 [oob]; Wikipedia's range is 65,000–75,000 [wiki].
- **Allies:** Kutuzov, with Alexander I and Francis II present. About 85,400 men and 278 guns [oob]; the range is 73,000–89,000 [wiki].
- **Losses:**
  - French: about 9,000 (8,569–9,288) [wiki].
  - Allies: about 27,000 (27,000–36,000, including 11–20,000 prisoners) and 180–186 guns [wiki].
  - The lower, most-cited figures are used.

## Sources
| id | source | kind | used for | reliability |
|---|---|---|---|---|
| wp22/23/24 | U.S. Military Academy situation maps 22–24 (18:00 on 1 Dec; 09:00 and 14:00 on 2 Dec) | modern staff map | positions (georeferenced, RMSE 245 m) | high for the large-scale picture; schematic at brigade level; **one label error, see D2** |
| md1844 | Mikhailovsky-Danilevsky (1844), maps 6–8 | Russian official history maps | an independent check of Allied positions and the end state; map 7 is the historical-map overlay (2nd-order fit, RMSE 207 m) | high on the Allied side |
| md1846 | Mikhailovsky-Danilevsky, *Relation de la campagne de 1805: Austerlitz* (French translation, 1846), archive.org full text | Russian official history | the Allied plan; Uvarov's move to Bagration; Kamensky's brigade; times; the dyke and the ice | high; drawn from Russian records, defends Russian conduct |
| stut | Stutterheim, *A Detailed Account of the Battle of Austerlitz* (1807), archive.org full text | eyewitness (Austrian staff officer) | battalion and squadron counts per column; routes; the lake | high on Allied structure; partisan against the Russian command |
| burton | Burton, *From Boulogne to Austerlitz* (1912), archive.org | staff study | fog: by 07:00 the hilltops stood clear like islands while the valleys stayed fogged | medium-high |
| oob | Wikipedia order of battle (citing Duffy 1977 and Smith 1998) | reference compiled from scholarship | strengths per column and corps; brigade composition | medium-high |
| wiki | Wikipedia, "Battle of Austerlitz" | reference | ranges; sequence | medium-high |
| fn | Fondation Napoléon timeline | French institutional | times (07:00 Telnitz, 08:00, 08:30, 11:00) | high |
| wh | warhistory.org, parts I–II | narrative based on the standard works | brigade detail (Thiébault, Kamensky, Jurczik, Rottermund, the 4e Ligne, the 24e Léger); ≈200 drowned; last troops gone about 16:00 | medium |
| ice | Den of Geek (summarising the drainage evidence) | popular | 28–30 guns, about 150 horses and 2–3 bodies found | medium; it agrees with the modern consensus |

Consulted but not usable: Alombert & Colin, *La campagne de 1805 en Allemagne* (the French General Staff history). Vol. 4 stops in mid-November, before the battle, because the series never reached Austerlitz. Chandler (1966) is lending-only on archive.org.

## Phases and confidence
| # | time | summary | conf |
|---|---|---|---|
| 0 | 07:00 | Fog in the valleys, clear hilltops [burton]. Kienmayer attacks Telnitz [fn]. Columns 1–3 descend. Liechtenstein crosses the columns and delays Langeron [wiki]. Soult is hidden. | high |
| 1 | 08:00 | Telnitz falls to Dokhturov, is retaken by Friant's lead brigade, then lost again to hussars [wiki]. Sokolnitz and the castle change hands repeatedly. | high |
| 2 | 09:00 | Soult's attack on the Pratzen [wp23] [fn]. The emperors reach Kutuzov about 09:00 [md1846]. In the north, Lannes, Murat and Bernadotte advance. | high |
| 3 | 10:00 | Fight for the Pratzeberg: Kamensky and Jurczik against St Hilaire; Thiébault's bayonet charge [wh] [md1846]. The Uhlans' charge is broken by Kellermann and Caffarelli [wh]. Bagration is checked at the Santon [wh]. | medium |
| 4 | 11:00 | The plateau is taken from end to end; the Allies are cut in two [wh] [fn]. | high |
| 5 | 13:00 | The Russian Guard counterattacks; the 4e Ligne loses its eagle; Rapp's charge [wh] [wiki]. | medium |
| 6 | 14:00 | Soult wheels south; Przhebyshevsky is cut off; the Allied centre re-forms on the Littawa [wp24]. | high |
| 7 | 15:30 | Retreat over the dyke between the ponds; the ice breaks; Przhebyshevsky surrenders [md1846] [stut] [wh]. | medium |
| 8 | 16:30 | Nightfall; retreat towards Austerlitz and Raussnitz [md1844]. | high |

## Order of battle: what changed in v2, and why
- **Allied structure** follows Stutterheim and the Russian official history:
  - 1st Column: 24 battalions.
  - 2nd Column: 18 battalions, Kamensky's brigade (Fanagoria Grenadiers and Ryazhsk) included.
  - 3rd Column: 18 battalions.
  - 4th Column: 27 battalions, 12 of them Russian.
  - Kienmayer: 22 Austrian and 10 Cossack squadrons plus 5 Grenz battalions.
  - Bagration: 12 battalions and 40 squadrons.
  - Guard: 10 battalions and 18 squadrons.
- **The 5th Column is split as the Russian history describes.** Uvarov's dragoons and hussars went to Bagration's left the evening before. The rest was 32 Austrian squadrons plus the Grand Duke Constantine Uhlans; the Uhlans are the "Russian cavalry" that charged at Blasowitz [md1846] [oob].
- **Strengths** come from the order of battle [oob]. Brigades are split by regiment counts where only divisions are given (marked medium).
- **Losses through the day** are estimates that spread the sourced totals across units following the narrative. This is stated in the strength chart caption.

## Disagreements and the choices made
1. **Column strengths.** West Point maps 22–23 label Przhebyshevsky's column 13,800 and Dokhturov's 8,500. Stutterheim (24 battalions against 18) and the order of battle (13,240 against 7,700) both say the reverse, so **the West Point labels are treated as swapped.** The 2-to-1 agreement of independent sources decides it.
2. **Time of the first attack.** The Fondation Napoléon and French accounts give 07:00; the Russian official history says the columns left at 08:00. 07:00 is used, as in most modern accounts, and noted as a debate in phase 0.
3. **Time of Soult's attack.** Sources give 08:30–09:00. 09:00 is used, as on West Point map 23.
4. **The ice.** Napoleon's bulletin and Marbot spoke of thousands drowned; Stutterheim and the Russian history confirm that men died on the ice; the drainage finds were 2–3 bodies and about 150 horses. The map shows modest losses on the ice and gives all three positions in the debate note.
5. **Time of the Guard counterattack.** Sources range from late morning to 13:00. 13:00 is used; confidence medium.
6. **Bernadotte's passivity** is a common criticism in the scholarship. It is mentioned but not dramatised.

## Terrain
- The ponds (Satschan, Menitz, Kobelnitz and one near Austerlitz) were drained in the 19th century and are drawn from West Point map 23.
- Two small modern ponds near Jiříkovice are smoothed out.
- Crossings are declared at the village bridges, mill dams and fords, and at the dyke between the ponds that is described in both period sources.

## Validation
`BATTLEKIT_STRICT=1 python3 scenario.py` passes with 0 warnings. The French units sum to 62,600 against 73,000, which is within 15%; the unmodelled cavalry divisions and artillery are listed in the notes.

## Review responses
(to be filled after the independent review: see review.md)
