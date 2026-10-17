# Independent review (general-purpose reviewer agent, 2026-10-16)

## Verdict

It can be published once a small number of corrections are made. I would not publish it as it stands. The overall design is honest. The traditional reading is labelled as tradition throughout. The revisionist case (Shiramine, Takahashi, and Turnbull's summary) appears in the brief, the `notes`, `method` and the phase debate fields. The camp markers are correctly described as a Meiji identification. The Ishikawa–Hikosaka letter of the 17th is quoted fairly as evidence against the noon timetable. The order of battle follows the General Staff table in ja.wikipedia closely; I checked every strength figure against that table. The faults are of three kinds:

- **Citation and bibliography errors.** The Kasaya book is wrong, Takahashi's book title is wrong, and the second Shiramine paper is incomplete.
- **Factual slips copied from old or misread sources.** Nangū-san is said to be "9 km" away, the executions are dated "1 November", Toyohisa's death place is called "Karasugashira", and sunrise is given as "about 06:00".
- **Two places where the drawn positions contradict the brief.** Toyohisa's "forward battle" is drawn behind Yoshihiro, and Ishida's "signal" is moved two hours earlier than its only source puts it.

None of these changes the story, but readers of a public atlas will notice several of them.

## Issues

1. **High. Wrong distance to Nangū-san.** Brief phase 0 says "9 km east". Phase 0 narrative says "some 30,000 sits nine kilometres back on Nangū-san".
   - **What is wrong:** The figure comes from Murdoch's "ten miles or so" (murdoch_sekigahara.txt line 345), which is badly wrong. The author's own coordinates contradict it. Nangū-san summit (Wikidata/OSM 35.3468, 136.5098) is about 5.4 km from Sasaoyama and about 2.4 km from Momokubariyama. `hidemoto` is placed at (35.3490, 136.5120), about 4.8 km east of Ishida.
   - **Evidence:** places.json; the Mōri Hidemoto camp is just below the summit, reached from Nangū Taisha on the north foot (https://www.kankou-gifu.jp/spot/detail_6879.html).
   - **Fix:** Say "about 5 km east (2–3 km south of Ieyasu's line of march)". Add a note that Murdoch's mileages are unreliable.

2. **High. Wrong source given for Kasaya.** Source `kasaya` reads "Sekigahara kassen (Kōdansha, 1994; rev. 2022), pp. 209-227".
   - **What is wrong:** The page references in ja.wikipedia (pp. 209, 211, 213, 216, 227) are to 笠谷 2022, which is a different book: *Ronsō Sekigahara kassen* (Shinchō sensho, 2022). wp_ja_clean.txt line 1507 cites it as 『論争 関ヶ原合戦』 新潮選書 2022. The 1994 Kōdansha book was never "revised 2022". This matters because the 2022 book is Kasaya's direct rebuttal of Shiramine and Takahashi, which strengthens the author's case.
   - **Evidence:** https://www.shinchosha.co.jp/book/603887/ (published 27 July 2022).
   - **Fix:** Cite Kasaya Kazuhiko, *Ronsō Sekigahara kassen* (Shinchōsha, 2022), pp. 209–227, still "via ja.wikipedia". Better still, consult it directly.

3. **Medium. Takahashi's book is misnamed.** Source `takahashi`, the brief and NOTES give "Atarashii Sekigahara".
   - **What is wrong:** The book is 『シン・関ヶ原』 (*Shin Sekigahara*, Kōdansha Gendai shinsho, October 2025). "シン" is not "atarashii".
   - **Evidence:** https://www.kinokuniya.co.jp/f/dsg-01-9784065416174; https://gendai.media/articles/-/159156.
   - **Fix:** Correct the title and date in all three places.

4. **Medium. Wrong execution date.** Unit `ankokuji` says "executed in Kyoto on 1 November".
   - **What is wrong:** The executions of Ishida, Konishi and Ankokuji at Rokujō-gawara took place on Keichō 5.10.1, which is **6 November 1600**. The author has carried the lunar day over as a Gregorian date.
   - **Evidence:** wp_en_clean.txt line 155 ("On November 6…"); wp_ja line 812 (10月1日); Konishi's death date is given as 慶長5年10月1日 (1600年11月6日) in https://www.historist.jp/articles/entry/themes/life/048969/.
   - **Fix:** Change to "6 November (Keichō 5.10.1)".

5. **Medium. Toyohisa's death place is misread, placed in the wrong town, and stated too firmly.** Phase 8, `toyohisa` note, brief phase 8: "killed near Karasugashira (marker 1.5 km SE of Sekigahara)".
   - **What is wrong:**
     - 烏頭坂 is read **Utōzaka**, not "Karasugashira".
     - It lies in Ōgaki city (Kamiishizu-chō Makita 741), not Sekigahara town, even though the town's open-data list includes the marker.
     - Where Toyohisa died is disputed. The Gifu tourist authority says only that he held the rearguard there. Other local traditions put his death at Shirabyōshi-dani or Kamitara (the Shimazu-zuka at Rurikō-ji).
   - **Evidence:** https://www.kankou-gifu.jp/spot/detail_6780.html; https://www.kankou-gifu.jp/spot/detail_6886.html.
   - **Fix:** Use "Utōzaka". Say "fought the rearguard at Utōzaka, where a memorial stands; where he died is disputed". Mark the event `low`.

6. **Medium. Toyohisa is drawn behind his parent unit.** Unit `toyohisa`, phase 0–7 position wp(907, 705).
   - **What is wrong:** That pixel converts to (35.3671, 136.4582). This is about 90 m *west* of `yoshihiro` (35.3671, 136.4592), which faces east. So the "forward battle" is drawn behind the main body. The brief says "~250 m ahead (E)" and the Shimazu memoirs (s1) put Toyohisa in front. The note's "about 160 m to the right of Ishida's men" matches neither the brief nor the drawing.
   - **Fix:** Move Toyohisa about 200–250 m east of Yoshihiro and reconcile the note with the brief.

7. **Medium. Ishida's signal is placed two hours earlier than its source.** Phase 4 (10:30): "Ishida signals for Kobayakawa and the Nangū-san force… [murdoch]"; event marker at Ishida.
   - **What is wrong:** Murdoch puts the signal "at noon" and mentions only Kobayakawa (murdoch_sekigahara.txt around lines 300–310). Nothing in the cited sources supports the 10:30 hour or the signal to Nangū-san.
   - **Fix:** Either move the signal to phase 5, or cite a source for a late-morning beacon (the *Nihon senshi* tradition) and drop "[murdoch]" from the Nangū-san part.

8. **Medium. Shimazu survivor figure is cited to a source that says something else.** Phase 8 says "Of perhaps 1,500, about 80 reach Satsuma [wpja]"; the `yoshihiro` note says the same.
   - **What is wrong:** ja.wikipedia (wp_ja_clean.txt line 874) says the Shimazu escaped the field with about **50**. en.wikipedia says 200. Murdoch says 70 horsemen. The figure of 80 reaching Satsuma is a popular tradition and is not in the cited text.
   - **Fix:** Give the range: "50–200 got clear of the field; tradition says about 80 reached Satsuma". Cite each figure correctly and drop [jinseki] from the note.

9. **Medium. Gamō Yorisato's death is stated as fact on weak evidence.** Unit `gamo` says "killed in the collapse [jinseki] [fujii] [wpen]".
   - **What is wrong:** jinseki and fujii cannot support a death. The ja.wikipedia article on 蒲生頼郷 rests his death on a single late text (『豪雄言行録』) that is flagged as needing a citation. The battle article's own summary (wp_ja line 874) reads "蒲生以外諸士が討ち死に", which implies he survived. His identity with 蒲生郷舎 is also unsettled.
   - **Fix:** "Said in later accounts to have been killed; fate uncertain." Set confidence to `low`.

10. **Medium. "No surviving camp markers" on Nangū-san is wrong, and the drawn positions miss the markers.** Brief phase 0 has "no surviving camp markers used; low" for the Nangū-san group; units `kikkawa` and `ikeda`.
    - **What is wrong:** Tarui town has marked camp sites for Kikkawa, Ankokuji, Natsuka and Ikeda, all in Miyashiro around Nangū Taisha (35.3607, 136.5254 via Nominatim). Ikeda's marker is at the Shunō/Annō graves. Chōsokabe's is at Kurihara. The Gifu Sekigahara Battlefield Memorial Museum ran a 2026 exhibition on how Kamiya identified exactly these sites. In the scenario, Kikkawa sits about 1.2 km west of Miyashiro and Ikeda about 1.3 km west.
    - **Evidence:** https://www.kankou-gifu.jp/spot/detail_6872.html; https://www.kankou-gifu.jp/spot/detail_6868.html; https://www.pref.gifu.lg.jp/site/pressrelease/478376.html.
    - **Fix:** Place these units at the Tarui markers, with the same "Meiji identification" caveat used for the main field. Correct the brief.

11. **Medium. Sunrise time is wrong.** `meta.sun.note` says "sunrise about 06:00 local solar time".
    - **What is wrong:** At latitude 35.36° and declination −10.9°, cos H = 0.137, which puts sunrise at about **06:27** local apparent time once refraction is included. Phase 0 at "06:30, Fog" is therefore at sunrise, not after it. This also shifts the conversion of the unequal temporal hours (辰, 巳, 午) slightly.
    - **Fix:** Say "about 06:30".

12. **Medium. Source details for `shiramine2` are incomplete.**
    - **What is wrong:** The paper is 『関ヶ原の戦いの布陣図に関する考察』, *Beppu daigaku daigakuin kiyō* 15 (2013), pp. 55–86. The `shiramine` paper runs pp. 151–**163**, and its subtitle is 「なぜ大谷吉継だけが戦死したのか」. The 2013 date also means "Since 2014" in the brief and notes understates how long the critique has been running.
    - **Evidence:** https://beppu-u.repo.nii.ac.jp/records/2001668; https://beppu-u.repo.nii.ac.jp/records/2002278.
    - **Fix:** Correct both entries. Say "since 2013–14".

13. **Low. Phase 6 cites the Ishikawa letter for more than it says.** Phase 6 text and the phase 6 confidence.
    - **What is wrong:** The letter names only Kobayakawa, Wakisaka and Ogawa father and son ("此四人"), not Kutsuki or Akaza. It also places the turn "as the lines engaged", which contradicts the 12:30 timing it is being used to support.
    - **Fix:** Limit [ishikawa] to the names and the deaths. Add "(the letter puts this at the start of the battle)".

14. **Low. Phase 5 confidence is too high.**
    - **What is wrong:** `conf="medium"`, but the hour is the central dispute and the "twice repulsed" detail comes from Murdoch alone.
    - **Fix:** Set it to `low` to match the brief's "hour low". Likewise, `kobayakawa` and `kob_van` carry `medium`/`low` across phases 5–7, which the brief calls `low`.

15. **Low. Myths stated more firmly than the evidence allows.**
    - **Meckel anecdote:** Myth 2 states as fact that it was "invented by Shiba Ryōtarō". That is Takahashi's claim (gendai.media 159156), and nobody has published a search for its first appearance. Write "according to Takahashi, an invention of Shiba".
    - **Probing shots:** Phase 5 says they are "rejected by most scholars", which is uncited. Kasaya 2022 (p. 216) actively defends them. Write "doubted by Shiramine, Fujimoto, Goza and others".

16. **Low. The split of Ukita's strength is unstated.** Unit `akashi`/`ukita`: the 8,000 / 9,220 division of Ukita's 17,220 is the author's own estimate but, unlike the Ishida and Kobayakawa splits, is not declared as one. Add "split is an estimate".

17. **Low. Small naming and strength points.**
    - `otani2`: the General Staff table and en.wikipedia call him Ōtani **Yoshiharu** (吉治). Give both names.
    - `kyogoku`: the 3,000 comes from en.wikipedia; the General Staff table has "不明" (unknown). Say so.
    - Mōri Katsunobu, marked as present on the field in the General Staff table, is not mentioned among the omitted contingents.

18. **Low. The brief's unit count is wrong.** It says "23 Western, 5 defecting and 22 Eastern contingents". The scenario has 17 Western, 6 defecting (including `kob_van`) and 22 Eastern.

19. **Low. The Ōtani group's front is drawn across the stream.** Phase 3 positions for `hiratsuka` (35.3592, 136.4572) and `toda` (35.3598, 136.4556) are on or east of the Fujikogawa. The camp-tradition position is on the Fujikawa plateau, west of the stream (Hiratsuka memorial at 35.3609, 136.4539). This is defensible as a sortie, but the text never says the West crossed. Either say so or keep them on the west bank.

20. **Low. The opening clash is away from the official marker.** Phase 2 puts Ii's first clash at (35.3630, 136.4640)–(35.3618, 136.4610). The national-site "開戦地" (start of battle) marker is at (35.3655, 136.4585), in front of Tenmayama (linkdata_sites.json). Since the map follows the camp markers elsewhere, either use this marker or explain why not.

## Verified

1. **Western withdrawal from Ōgaki on the night of the 14th, and the vanguard and turncoats named in the Ishikawa–Hikosaka letter.** The text matches the quoted original (wp_ja line 836, from Nakano 2017 p. 462): the letter says the West fired Ōgaki's outer bailey and left at 五ツ時分, about 20:00.
2. **Kasaya's position (fighting from about 08:00, fog lifting about 10:00, "several hours" before the defection, "crushed at once" as a stock victory phrase).** This is correctly reported, but the source is *Ronsō Sekigahara kassen* (2022), not the 1994 book: https://www.shinchosha.co.jp/book/603887/ and wp_ja lines 1381–1417.
3. **Takahashi said Kobayakawa had defected the day before (2015) and that the Meckel anecdote is Shiba's.** Confirmed: https://gendai.media/articles/-/159156; the book itself is https://www.kinokuniya.co.jp/f/dsg-01-9784065416174.
4. **The marked camp sites go back to Kamiya's Meiji-era identification.** Supported by the Gifu Sekigahara Battlefield Memorial Museum's 2026 exhibition on how Kamiya identified the camp sites: https://www.pref.gifu.lg.jp/site/pressrelease/478376.html.
5. **Mōri Hidemoto on Nangū-san just below the summit, Natsuka at Miyashiro, Chōsokabe at Kurihara, and none of them fought.** Confirmed by the Gifu prefectural tourism pages: https://www.kankou-gifu.jp/spot/detail_6879.html, https://www.kankou-gifu.jp/spot/detail_6872.html. The location details partly correct the scenario (issues 1 and 10).
6. **The Shimazu rearguard fought at Utōzaka on the Ise road SE of Sekigahara.** The route is right; the name is wrong (issue 5): https://www.kankou-gifu.jp/spot/detail_6780.html.
7. **Executions of Ishida, Konishi and Ankokuji at Rokujō-gawara on Keichō 5.10.1, which is 6 November 1600.** This confirms the error in issue 4: https://www.historist.jp/articles/entry/themes/life/048969/.
8. **Shiramine's two papers exist as described, with corrected bibliographic details.** https://beppu-u.repo.nii.ac.jp/records/2002278 and https://beppu-u.repo.nii.ac.jp/records/2001668.
9. **Strengths.** Every unit strength matches the General Staff table as given in ja.wikipedia (Konishi 6,000; Ōtani 1,500; Toda 300; Takenaka 200; Hidemoto 16,000 including Kikkawa). This is not independent of the author's sources.

## Sources the author should add

- Kasaya Kazuhiko, *Ronsō Sekigahara kassen* 論争 関ヶ原合戦 (Shinchō sensho, Shinchōsha, 2022). Consult it directly; it is the main traditionalist rebuttal.
- Takahashi Yōsuke, *Shin Sekigahara* シン・関ヶ原 (Kōdansha Gendai shinsho, 2025).
- Shiramine Jun, 「関ヶ原の戦いの布陣図に関する考察」, *Beppu daigaku daigakuin kiyō* 15 (2013), 55–86.
- Shiramine Jun, *Shinkai Sekigahara kassen no shinjitsu* 新解 関ヶ原合戦の真実 (Miyaobi shuppansha, 2014). This is the book-length statement of the revisionist case. I recalled this reference rather than checking it; confirm it before citing.
- Nakano Hitoshi, *Ishida Mitsunari den* 石田三成伝 (Yoshikawa Kōbunkan, 2017). The source of the letter of the 17th; cite it directly. Bibliographic details are from memory; check them.
- Mitsunari Junji, *Sekigahara zen'ya* 関ヶ原前夜 (NHK Books 2009; Kadokawa Sophia bunko 2018), and Watanabe Daimon, *Sekigahara kassen zenshi* (Sōgensha, 2021). Both are cited only second-hand through en.wikipedia at present. Details from memory; check them.
- Anthony J. Bryant, *Sekigahara 1600: The Final Struggle for Power* (Osprey Campaign 40, 1995). Cited only through en.wikipedia; it is the standard English campaign study.
- Gifu Sekigahara Battlefield Memorial Museum, exhibition 「関ケ原の陣跡は、どのように比定されたのか〜南宮山周辺に及ぶ神谷道一の業績〜」 (17 Feb – 26 Apr 2026): https://www.pref.gifu.lg.jp/site/pressrelease/478376.html.
- Gifu prefectural tourism pages on the Tarui and Ōgaki camp sites and the "Shimazu no nokiguchi" sites: https://www.kankou-gifu.jp/spot/detail_6780.html, https://www.kankou-gifu.jp/spot/detail_6886.html, https://www.kankou-gifu.jp/spot/detail_6868.html, https://www.kankou-gifu.jp/spot/detail_6872.html, https://www.kankou-gifu.jp/spot/detail_6879.html.

I did not edit any files. The two web pages I tried to load that failed (tabi-mag.jp returned 403, and a Nominatim lookup for the Kikkawa marker found no match) did not affect any of the conclusions above.