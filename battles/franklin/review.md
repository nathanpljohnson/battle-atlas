# Independent review (general-purpose reviewer agent, 2026-10-16)

## Verdict

This is not fit to publish yet, though it is close. The Union side is solid. The Kimball, Ruger and Reilly brigade order, the Wagner and Opdycke story, the Union and Confederate losses, the sunset time and Cockrell's figures all check out against Cox and the Official Records. Hood is quoted accurately. The weak points are on the Confederate side and the flanks, and all of them rest on Wikipedia rather than on primary reports the author could have read:

- **Forrest:** Buford's division is put on the wrong side of the Harpeth.
- **Cavalry timing:** Forrest is driven back across the river about two and a half hours too early.
- **Johnson's attack:** it is timed an hour late, and the time is cited to Hood, who says something different.
- **Attacking strength:** the "chosen" figure in the brief disagrees with both the narrative and the unit totals.
- **The rally at the breach:** the account gives Reilly's reserve all the credit and leaves out the regiments west of the pike that recent scholarship emphasises.

Volume 45 part 1 of the Official Records is freely available as full text on archive.org (`warofrebellion451unit`). The brief says it was read only through Cox's quotations. Reading the reports of Forrest, S. D. Lee, Hatch, Stanley and Cockerill, plus French's casualty return, would fix most of the issues below. After those fixes, I would rate it reliable for a public atlas at brigade level for the first hour, and approximate after dark.

## Issues

1. **High. Unit `buford`, phases 1–5; phase 1 narrative "Forrest's Buford and Jackson push across Hughes's Ford"; brief phase 1.**
   - **Problem:** Buford did not cross at Hughes's Ford. Forrest's own report says only Jackson's division crossed. Buford dismounted on Stewart's right, "covering the ground from the Lewisburg pike to Harpeth River", and drove the Union cavalry back across the river. Wikipedia's "two divisions… crossed the Harpeth at Hughes Ford" conflates the two. Hatch says both divisions appeared in his front, but that is a Union impression; Forrest's report is the authority for where Forrest put his own divisions.
   - **Evidence:** Forrest's report, O.R. Ser. I vol. 45 pt 1, p. 754 (https://archive.org/details/warofrebellion451unit). A Franklin historical marker also has Buford moving up the Lewisburg Pike and pushing Croxton's troopers back across the river at McGavock's Ford. I only saw that marker quoted in a search summary because HMDB blocked direct access, so it is not verified.
   - **Fix:** Put Buford dismounted south of the river, between the Lewisburg Pike and the Harpeth on Loring's right, near McGavock's Ford. Keep only `jackson_cav` crossing at Hughes's Ford. Rewrite the phase 1 narrative and the brief to match. Re-check whether `croxton` starts on the south bank.

2. **High. Phase 3 (16:30) narrative "Wilson's cavalry drives Forrest back across the Harpeth"; units `buford` and `jackson_cav` phase 3 "R"; `hatch` phase 3.**
   - **Problem:** The repulse came at nightfall, not at 16:30.
   - **Evidence:** Hatch reports that "at 7 o'clock in the evening we had driven them over Harpeth River" (O.R. 45/1 pp. 576–577). Forrest says Jackson "held him in check until night" and then recrossed (p. 754).
   - **Fix:** Move the cavalry repulse to phases 5–6 (about 17:00–19:00) and keep Jackson north of the river until then. Lower the confidence for the cavalry in phase 3.

3. **Medium. Phase 6 "19:00 Johnson's attack" and the Johnson brigade notes "about 7 p.m. … [wp] [hood]".**
   - **Problem:** Hood does not support 7 p.m. He says "just before dark Johnston's Division … moved" (Advance and Retreat, p. 294). Lee says the attack "was not felt by the enemy till about one hour after dark" (Lee's report, O.R. 45/1 pp. 687–688). Cox also says "an hour after dark". With sunset at 4:59, that means about 6:00–6:30 p.m. The 19:00 figure comes from Wikipedia.
   - **Fix:** Re-time the phase to about 18:00–18:30, cited to Lee and Cox. Add a debate note: Hood says "before dark", Lee and Cox "an hour after dark", Wikipedia and Jacobson about 7 p.m. Remove [hood] as support for 7 p.m.

4. **Medium. Brief, "Chosen: about 23,000 engaged"; phase 1 narrative "About 20,000"; the Confederate brigade strengths in `scenario.py`.**
   - **Problem:** The three figures do not agree. Stewart's and Cheatham's brigades in the scenario add up to about 17,900 (Stewart about 7,900, Cheatham about 10,000), or about 21,200 with Johnson. Wikipedia, citing Jacobson, gives "about 19–20,000". So the brief's chosen figure matches neither the narrative nor the data.
   - **Fix:** Pick one figure, about 20,000 in the assault, and say so in the brief, the narrative and `strengthNote`. Scale the brigade estimates to it, or state plainly that they do not sum to the headline figure.

5. **Medium. Phase 4 narrative and the brief's "Who saved the centre".**
   - **Problem:** The rally is credited only to Opdycke and Reilly's reserve east of the pike. The Wikipedia text the author used also names the 44th Missouri and the 183rd Ohio (Strickland's second line at the retrenchment) as holding west of the pike. Jacobson's *Baptism of Fire* (2011) is a whole study of the 44th Missouri, 175th Ohio and 183rd Ohio at the breach. The 112th Illinois was sent to reinforce Strickland (Cox p. 147). The scenario has no unit for Strickland's reserve line.
   - **Fix:** Add a unit or note for the 44th Missouri and 183rd Ohio at the Carter House retrenchment, and mention them in the phase 4 text.

6. **Medium. Phase 4 narrative "Stanley, arriving, gives no orders".**
   - **Problem:** Stanley's report says "I rode quickly to the left regiment and called to them to charge", and only then "I gave the colonel no order" (O.R. 45/1 pp. 115–116). So he gave Opdycke no order, but he did call a regiment forward. The debate note quotes him correctly; the narrative overstates it.
   - **Fix:** "Stanley, arriving, urges the nearest regiment on but gives Opdycke no orders, and is wounded."

7. **Medium. Wagner's forward position: brief phase 0 "about 800 m south of the Carter House" against `lane` j(432,598) and `conrad` j(530,640).**
   - **Problem:** Converted to the ground, the data puts Lane about 445 m and Conrad about 550 m from the Carter House. Sources differ: Stanley says "about 300 yards in front of the main line" (O.R. 45/1 p. 115), while Cox and ABT say half a mile. The brief, the data and the sources disagree, and none of this is acknowledged.
   - **Fix:** Make the brief match the data (Jespersen, about 450–650 m). Add the Stanley vs Cox distance disagreement as a debate note.

8. **Medium. Unit `granger_art` "Fort Granger batteries, 8 guns".**
   - **Problem:** Only one battery was in the fort, Battery D, 1st Ohio (3-inch rifles). It fired 160 shells and 3 case-shot. The rest of the corps artillery was parked north of the river. Cox adds that batteries were "nearly all reduced to four guns".
   - **Evidence:** Cockerill's report, O.R. 45/1 p. 432; Cox p. 58 and p. 124n.
   - **Fix:** Rename it "Battery D, 1st Ohio (Fort Granger)", give it about 4–6 guns, and cite [or] [cox].

9. **Medium. Phase 3 event "Adams killed on the parapet" at k(1040,770), and `adams` phase 4 at k(1040,800).**
   - **Problem:** This puts Adams's death towards Stiles's left, by the river. Cox's official report places it "in front of Stiles' right and Casement's left". Casement's report puts the 65th Illinois (whose colours Adams grabbed at) in the centre of Casement's brigade.
   - **Evidence:** O.R. 45/1 p. 353 (Cox) and p. 425 (Casement).
   - **Fix:** Move the event and Adams's phase 4 position to the Stiles–Casement junction, about k(900–950, 760).

10. **Low. Unit `cs_art` on the Columbia Pike at j(470,880), "8 guns".**
    - **Problem:** Cox names the two batteries: Guibor's, in sections in the intervals between Stewart's divisions and between French and Cheatham; and Presstman's, first on Privet Knob and then at the Bostick knoll near the Carter's Creek Pike. Both were six-gun batteries (Cox pp. 88–89).
    - **Fix:** Show them as two units placed as Cox describes, about 12 guns.

11. **Low. Unit `lowrey` "Cleburne's third line, formed at his request in depth [hood]".**
    - **Problem:** Hood says Cleburne asked to form "in two, or, if I remember correctly, three lines". That is not firm support for a third line.
    - **Fix:** Use "second line", or quote Hood's uncertainty.

12. **Low. French's division, `cockrell` and `sears` side by side at phase 0.**
    - **Problem:** Cox says French went in "with one brigade in front and one in second line" (Ector's being absent).
    - **Fix:** Stagger the two brigades.

13. **Low. Brief phase 8, "Schofield's order is issued at 7:15 p.m."**
    - **Problem:** Cox says 7:15 p.m. was the Fourth Corps order passing Schofield's on, and that Schofield issued his own "between six and seven" (p. 159n).
    - **Fix:** Correct the wording.

14. **Low. Brief table, generals: "6 killed or mortally wounded … 6 or 7 wounded".**
    - **Problem:** This counts Carter twice. Schofield and Thomas give 6 killed, 6 wounded, 1 captured, with Carter among the wounded (O.R. 45/1 pp. 35 and 344). The Tennessee Encyclopedia gives 6 killed, 5 wounded, 1 captured.
    - **Fix:** Use "6 killed or mortally wounded, 5 others wounded, 1 captured".

15. **Low. Internal inconsistencies in labels and text.**
    - The brief puts Cleburne's death in phase 4; the data has it as a phase 3 event.
    - The brief rates phase 3 "high"; the data says "medium".
    - The brief rates Bate's brigades "low"; the data has `smith_bate`, `jackson_bate` and `bullock` as "medium".
    - Phase 1 is "high" despite the debated step-off time and the Forrest error. Lower it to medium.
    - Hughes's Ford is "4.5 km ESE" in the brief, but about 3.3 km SE in the data. Wikipedia says 3 miles; the IV Corps journal says "two miles above Franklin" (O.R. 45/1 p. 103).
    - Fort Granger is "1.2 km NE"; in the data it is about 1.4–1.5 km.

16. **Low. `lane` note "Left forward on the rise…".** This reads as though Lane was the left brigade. Stanley has Lane "on the right" and Conrad on the left of the pike. Reword it. Stanley also says Lane re-entered the line "several hundred yards to the right of the pike", not at the pike, so the phase 2 arrow to `PIKE_W` should end further west.

17. **Low. `opdycke` phase 0 facing 180.** Wikipedia (after Jacobson) says it was in column of regiments "facing north". Stanley says it was "lying down about 100 yards in rear of the works". Set the facing to about 0.

18. **Low. Georeferencing and per-moment losses.**
    - Fort Granger is used as a georeference control point at its Wikidata coordinates, which are 174 m from OSM. Its leave-one-out error is 68 m. Check which point the georeference really used.
    - The allocated losses for Wagner's division (Lane −600, Conrad −650, Opdycke −170, about 1,420 in total) are higher than the O.R. return of 1,241 for the whole division.

## Verified

- **Union losses** of 189 killed, 1,033 wounded and 1,104 missing (2,326): Thomas's report, O.R. 45/1 p. 35.
- **Confederate losses** of 6,252 (1,750 buried, 3,800 in hospital, 702 prisoners), counted after Franklin was reoccupied: Schofield's report, O.R. 45/1 p. 344.
- **Cockrell's figures:** 696 engaged ("Eighty-two officers and 614 men") and 419 casualties. French says his loss was "over one-third" of the troops engaged and that Ector's brigade was detached. French's division return, O.R. 45/1 p. 716.
- **Wagner's division** lost 1,241, of whom 670 were missing. This supports the "nearly 700 captured" figure. IV Corps casualty return, O.R. 45/1 p. 117.
- **Stanley's quotation** "I gave the colonel no order" is accurate, though with the qualification in issue 6. Stanley also confirms the 4 p.m. advance and that Conrad broke first. O.R. 45/1 pp. 115–116.
- **Stewart's attack on the left:** Fort Granger's guns and Battery M, 4th U.S. enfiladed the railroad cut, and the osage-orange hedge stopped Stewart's men. Cox's report, O.R. 45/1 p. 353.
- **Kimball's order** from left to right was Grose, Kirby, Whitaker (Cox p. 141). The scenario has it right.
- **Sunset:** Porter's computed sunset of 4:59 local time and the "true sunset… almost exactly five o'clock" are correctly reported (Cox p. 147 and note).
- **Hood's memoir:** the 3 p.m. deployment, the 4 p.m. advance, the order to keep the artillery out of the fight, fighting until 9 p.m. and the enemy leaving about 3 a.m. are all quoted correctly (*Advance and Retreat* pp. 293–295).
- **Henry rifles:** the 12th Kentucky's Henry rifles are supported by the Wikipedia source, which cites Jacobson pp. 286–287. I confirmed only that the citation exists.

## Sources the author should add

- *War of the Rebellion: Official Records*, Ser. I, vol. 45, pt 1 (1894), full text at https://archive.org/details/warofrebellion451unit. Read directly:
  - Forrest, pp. 752–756
  - S. D. Lee, pp. 686–688
  - Stanley, pp. 113–117
  - Schofield, pp. 340–345
  - Cox, pp. 348–356
  - Casement, pp. 424–425
  - Cockerill, p. 432
  - Hatch, pp. 575–577
  - French's return, p. 716
  - Bate's report, p. 743
- Eric A. Jacobson with Richard A. Rupp, *For Cause & for Country* (Franklin, TN: O'More, 2006). Read it directly; it is the standard modern study.
- Eric A. Jacobson, *Baptism of Fire: The 44th Missouri, 175th Ohio, and 183rd Ohio at the Battle of Franklin* (Franklin, TN: O'More, 2011).
- Wiley Sword, *The Confederacy's Last Hurrah: Spring Hill, Franklin, and Nashville* (Lawrence: University Press of Kansas, 1993; first published 1992 as *Embrace an Angry Wind*). Archive.org lending copy `confederacyslast0000swor`. Note: the Tennessee Encyclopedia lists the original as by "Wiley Ford".
- James Lee McDonough and Thomas L. Connelly, *Five Tragic Hours: The Battle of Franklin* (Knoxville: University of Tennessee Press, 1983). Archive.org `fivetragichoursb0000mcdo`.
- James Lee McDonough, *Nashville: The Western Confederacy's Final Gamble* (Knoxville: University of Tennessee Press, 2004).
- Stephen M. Hood, *John Bell Hood: The Rise, Fall, and Resurrection of a Confederate General* (El Dorado Hills, CA: Savas Beatie, 2013), and Stephen M. Hood, ed., *The Lost Papers of Confederate General John Bell Hood* (Savas Beatie, 2015). These are needed to present the "Hood's motive" debate, and the challenge to Sword's reading of Hood, fairly.
- Jonathan M. Steplyk, *Fighting Means Killing: Civil War Soldiers and the Nature of Combat* (Lawrence: University Press of Kansas, 2018). Wikipedia cites it as 2016 for the close-combat material; check the year.
- Larry J. Daniel, *Conquered: Why the Army of Tennessee Failed* (Chapel Hill: University of North Carolina Press, 2019).