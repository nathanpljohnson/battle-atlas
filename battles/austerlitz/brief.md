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
| wp22/23/24 | U.S. Military Academy situation maps 22–24 (18:00 on 1 Dec; 09:00 and 14:00 on 2 Dec) | modern staff map | positions (georeferenced, RMSE 245 m) | high for the large-scale picture; schematic at brigade level; its column strengths follow an earlier numbering (see disagreement 1) |
| md1844 | Mikhailovsky-Danilevsky (1844), maps 6–8 | Russian official history maps | an independent check of Allied positions and the end state; map 7 is the historical-map overlay (2nd-order fit, RMSE 207 m) | high on the Allied side |
| md1846 | Mikhailovsky-Danilevsky, *Relation de la campagne de 1805: Austerlitz* (French translation, 1846), archive.org full text | Russian official history | the Allied plan; Uvarov's move to Bagration; Kamensky's brigade; times; the dyke and the ice | high; drawn from Russian records, defends Russian conduct |
| stut | Stutterheim, *A Detailed Account of the Battle of Austerlitz* (1807), archive.org full text | eyewitness (Austrian staff officer) | battalion and squadron counts per column; routes; the lake | high on Allied structure; partisan against the Russian command |
| burton | Burton, *From Boulogne to Austerlitz* (1912), archive.org | staff study | fog: by 07:00 the hilltops stood clear like islands while the valleys stayed fogged | medium-high |
| oob | Wikipedia order of battle (citing Duffy 1977 and Smith 1998) | reference compiled from scholarship | strengths per column and corps; brigade composition | medium-high |
| wiki | Wikipedia, "Battle of Austerlitz" | reference | ranges; sequence | medium-high |
| fn | Fondation Napoléon timeline | French institutional | times (07:00 Telnitz, 08:00, 08:30, 11:00) | high |
| wh | warhistory.org, parts I–II | narrative based on the standard works | brigade detail (Thiébault, Kamensky, Jurczik, Rottermund, the 4e Ligne, the 24e Léger); ≈200 drowned; last troops gone about 16:00 | medium |
| thi | Thiébault, *Memoirs* vol. 2 (1896), archive.org | eyewitness (St Hilaire's brigade commander) | Soult's "twenty minutes at most"; the fog; the brigade assignments; his guns breaking Kolowrat's attack; Kamensky driven back | high for his own sector; self-promoting |
| segur | Ségur, *An Aide-de-Camp of Napoleon* (1895), archive.org | eyewitness (headquarters) | 08:00 and "ten minutes" | medium-high |
| marbot | Marbot, *Memoirs* vol. 1 (1892), archive.org | eyewitness | Guard artillery firing on the ice; source of the "thousands drowned" exaggeration | low on numbers, medium on events |
| lgh / fraser | Wikipedia "Life Guard Horse Regiment"; Fraser, *War Drama of the Eagles* (1912) | reference / popular | the Life Guard Horse took the eagle of the 1/4e Ligne | medium |
| millar04 | S. Millar, Allied order of battle, Napoleon Series (2004) | scholarly (online) | 73,200–85,400 men; 131 guns lost per Kutuzov's report | medium-high |
| fnplaces | Fondation Napoléon places guide | reference | Napoleon at the Zuran, Staré Vinohrady and St Anthony's chapel | high |
| ice | Den of Geek (summarising the drainage evidence) | popular | 28–30 guns, about 150 horses and 2–3 bodies found | medium; it agrees with the modern consensus |

Not consulted directly (no free access): Duffy (1977), Goetz (2005), Castle (2002), Chandler (1966), Bowden (1997) and Mikaberidze's translations. Their figures reach this map only through the order of battle [oob] and Millar [millar04]. **This is the main remaining gap in the scholarship.** Consulted but not usable: Alombert & Colin, *La campagne de 1805 en Allemagne* (the French General Staff history). Vol. 4 stops in mid-November, before the battle, because the series never reached Austerlitz. Chandler (1966) is lending-only on archive.org.

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
1. **Column strengths.** West Point maps 22–23 put 13,800 on Przhebyshevsky's column and 8,500 on Dokhturov's. These figures match **Stutterheim's earlier march-order table**, in which the 3rd Column had 24 bns and 13,800 men and the 1st had 18 bns and 8,320. The brigades were renumbered before 1 December: Urusov's and Löwis's brigades went to Dokhturov's 1st Column, and Muller's and Strick's to Przhebyshevsky's 3rd (independent review, issue 2). So the West Point cartographer used the earlier numbering; it is not a typo. For the battle the data follow Stutterheim's battle-day dispositions (24 bns against 18) and the order of battle (13,240 against 7,700).
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

## Review responses (to review.md, 8 Oct 2026)
1. **Fixed.** `col1` at 15:30 now stands on the plain between Telnitz and the lake [stut] and escapes over the dyke. The water check in battlekit now flags routing units too, which is how this slipped through.
2. **Fixed.** Disagreement 1 is rewritten: West Point used Stutterheim's earlier column numbering.
3. **Fixed.** The Guard infantry drives back the 4e and 24e, and the Life Guard Horse take the 1/4e's eagle [lgh] [fraser]. The text now says "only eagle not recovered".
4. **Fixed.** The fire on the ponds is now credited to the French Guard artillery on Napoleon's order [marbot] [md1846]. Vandamme takes Aujezd.
5. **Fixed.** Kienmayer's cavalry no longer uses the dyke. It covers the retreat from the Telnitz–Menitz hill, and the hussars go round the lake [stut] [md1846].
6. **Fixed.** Buxhöwden escapes with a few battalions, and about 4,000 are taken at Aujezd [stut]. "Five of nine battalions" is removed.
7. **Fixed.** The debate now covers 08:00–09:00 [segur], and the quote is presented as an anecdote with both versions [thi] [segur].
8. **Fixed.** Napoleon is at Staré Vinohrady at 13:00 [fnplaces].
9. **Partly fixed.** The Pratzen, Kamensky and Kolowrat narrative is re-cited to Thiébault's eyewitness account, which also corrected it: his guns broke Kolowrat at close range, and he was not "low on ammunition". "Outnumbered two to one" is removed (Rottermund is now low confidence). "≈200 drowned" is kept but labelled a popular estimate. 25 warhistory citations remain; most are now paired with a primary source.
10. **Open.** Duffy, Goetz, Castle, Chandler and Bowden are not freely available and were not consulted directly. This is stated in the Sources section.
11. **Fixed.** "131–180 guns" [millar04] and "nearly half prisoners".
12. **Fixed.** `kie1` is now "Brod & Szekler Grenzer".
13. **Fixed.** `fri1` is now "108e Ligne, voltigeurs of the 15e Léger".
14. **Fixed.** The range for the Austrian squadrons (20, 32 or 40) is stated in the `lau` note.
15. **Fixed.** `uhl` names Essen II and Meller-Zakomelsky.
16. **Fixed.** A debate note on Kamensky's turn is added in phase 3.
17. **Fixed.** The Russian Guard Jäger at Blasowitz are added as a phase-4 event and in the Guard note [thi].
18. **Fixed.** Phase 0 now gives the arithmetic: three columns of ≈32,000 plus Kienmayer.
19. **Fixed.** Phases 0 and 1, `col1`, `col3`, `col2` and `leg2` are lowered to medium.
