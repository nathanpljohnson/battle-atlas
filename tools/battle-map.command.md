---
description: Research a historical battle and add it as a 3D phase-by-phase map to Nathan's Battle Atlas library
argument-hint: "<battle name and year, e.g. 'Leuthen 1757'>  [optional: notes, screenshots or sources to use]"
---

Add **$ARGUMENTS** to the Battle Atlas in `~/battle-maps/`. First read `~/battle-maps/README.md` (layout, data contract, tools) and `~/battle-maps/HANDOFF.md` (environment facts). The worked examples are `battles/austerlitz/` (napoleonic) and `battles/rossbach/` (18th century).

Nathan is not a specialist and cannot fact-check the result: **you are the historian.** Work as a PhD military historian would:
- Triangulate independent sources.
- Prefer modern scholarship built on archival work over older or popular accounts.
- Record disagreements openly.
- Cite every claim.
- Never present a guess as fact.
- Don't stop to ask for review. Decide, record your reasoning, and keep going.

## 0. Set up and keep a handoff trail
- Create `battles/<id>/sources/` (id: lowercase, no spaces).
- Append a checklist for this battle to `tasks/todo.md`.
- After each numbered step below, commit (`git add -A && git commit -m "<id>: step N ..."`) and update `RESUME.md`. An interruption must lose nothing.

## 1. Sources (minimum: 3 independent narrative sources, 2 map sources, and 1 scholarly or official work)
Save excerpts and notes to `battles/<id>/sources/` and register each one with `B.source(id, label, url, note, kind)`.

**Maps.** These matter most.
- West Point (USMA) atlas maps: search Wikimedia Commons for "<battle> situation at" or the Commons category "Maps of the Battle of X".
- Official-history map volumes, such as the Prussian Great General Staff, the French Archives de la Guerre, Russian official histories, and the British and US official histories.
- David Rumsey, the Library of Congress, Gallica and the Austrian State Archives.
- American Battlefield Trust maps for American wars.
- Download the images with curl and **look at them**.

**Scholarly and official works.** Full texts are on archive.org (`https://archive.org/advancedsearch.php?q=...&output=json`), Google Books, HathiTrust and Gallica. Aim for at least one modern monograph or official history; their bibliographies point to more.

**Non-English sources** for the belligerents' own accounts. Translate the relevant passages.

**Narratives.** Wikipedia (and the works it cites), Kronoskaf, napoleon-series.org, reputable battlefield sites and regimental histories. Use these to fill gaps, never as the only source for a claim.

**Network notes.** Use a URL-style User-Agent such as `BattleAtlas/0.2 (https://claude.ai/; personal non-commercial history project)`, never Nathan's email. Pause 1 s between Wikimedia, Nominatim and Overpass calls, and back off when rate-limited.

## 2. Brief: `battles/<id>/brief.md`
Write the brief before any code. It contains:
- **Overview:** strengths and losses, each with its range across sources.
- **Sources table:** each source's kind and reliability.
- **Phases:** 6–12 timed phases, with `day` for multi-day battles. For each phase:
  - what happens
  - unit positions as "<distance> <direction> of <landmark>, facing <bearing>, in <formation>"
  - source ids for every claim
- **Disagreements:** for each, the reading you chose and why (archival over memoir; independent agreement over a single account; terrain rules X out).
- **Myths:** popular claims that modern scholarship rejects.
- **Confidence per phase and per unit:**
  - high: the sources agree and the positions are mapped
  - medium: the sources broadly agree, but the position is placed from narrative
  - low: inferred or contested

## 3. Places
- **Historical names:** write `battles/<id>/names.json` with the historical names, languages and optional modern hints. Then run `python3 tools/gazetteer.py battles/<id>`, which cross-checks Wikidata aliases, Wikipedia and OSM. Resolve every flag in `gazetteer_report.md`.
- **Map matching:** write `battles/<id>/maps.json` with control-point pixels for each source map. Use crops to find village symbols precisely. Then run `python3 tools/georef.py battles/<id> --overlays`.
  - Read `georef_report.md`. A flagged point usually means a misidentified place: fix the name or drop the point.
  - Use `"order": 2` for hand-drawn period maps.
  - Use `"crop"` to cut away margins and legends.
  - At least one **period** map (or a 19th-century survey) should get `"overlay": true` for the historical-ground toggle.

## 4. Terrain
- Write `terrain_config.json` with the bbox (the action plus a margin, about 8–25 km a side).
- Run `python3 tools/terrain.py battles/<id> --detect`. This auto-masks mines, quarries and flooded pits via OSM, and suggests reservoirs and motorways for review.
- Review `terrain_detect.png`, `terrain_filled.png` and `terrain_suggestions.json`:
  - Keep historical water bodies.
  - Mask modern ones by hand only if the historical record says they weren't there.
  - Add `bumps` for vanished features. Every mask and bump needs a `why`.
- Water that has since vanished (drained ponds, moved rivers) goes in `B.water` from the georeferenced maps.

## 5. Scenario: `battles/<id>/scenario.py`
Build it with `tools/battlekit.py`, copying the Austerlitz structure.
- **Positions:** read them off georeferenced maps with `G = Georef(HERE); wp = G("map_id"); wp(x, y)`, or write them as landmark offsets such as `("Prace", 200, 900)`.
- **Unit size:** use the level the sources map consistently. Up to about 50,000 men per side, that is brigades or regiments; above that, divisions. Aim for about 60 units or fewer.
- **Every unit gets:**
  - a citation (`cite=[...]`)
  - `conf`
  - a one-line `note`
  - `men` at phase 0, plus later values as it takes losses. Distribute the sourced losses across phases following the narrative, and say in `meta.notes` that per-phase losses are estimates.
- **Moves:** add `via=[...]` waypoints so moves follow roads and arrows instead of cutting through villages, ponds or other units. Declare bridges, fords and causeways with `B.crossing`, and mark small brooks `ford: True`.
- **Every phase gets:**
  - `cite`, plus inline `[source_id]` markers after factual sentences
  - `conf`
  - `tactic=(name, body, tactic_id)`, using an id from `~/battle-maps/tactics.json` (add new tactics there with a summary)
  - `debate=` where historians differ
  - `fog=` where weather mattered
- **Meta:**
  - `era` and `war`
  - sides' colours (the real coat colours)
  - belligerents
  - forces (start and losses)
  - sun: latitude, plus the solar declination for the date
  - `wind`
  - `method` (2–3 sentences on how the map was built and its limits)
  - notes
- **Overlays:** add them with `B.overlay(...)`.
- **Other eras:**
  - Ancient and medieval unit types: `hi`, `arc`, `kn`, `ele`, `cha`. Modern: `arm`, `mech`, `mg`.
  - Naval battles are not supported.
- **Build:** run `cd battles/<id> && python3 scenario.py`. Errors fail. Warnings go to `validation.md`.

## 6. Verify
- Run `BATTLEKIT_STRICT=1 python3 scenario.py`. Every warning must be fixed or explained in the brief, and the strict run must pass, or each remaining warning must be justified in `brief.md`.
- Open `check.png` and compare it phase by phase with the source maps: sides of streams, villages and heights, facing, order. Fix and rebuild until it matches.

## 7. Second opinion
- Spawn an independent reviewer agent (`general-purpose`) with `tools/review_prompt.md`, with `<id>` filled in. Save its reply to `battles/<id>/review.md`.
- Answer every issue in `brief.md` under "Review responses" as fixed, rebutted (with evidence) or open.
- Apply the fixes and rebuild.

## 8. Library and test
- Add the id to `library.json` and run `python3 tools/build_library.py`.
- Preview with the `battle-library` server (port 8791) at `/preview.html#<id>`. Check:
  - every phase
  - the toggles: overlay, contours, scale bar, labels, fog
  - 375 px width
  - light and dark themes
  - no console errors
- A hidden pane throttles animation, so wait before screenshots. Changing only the hash doesn't reload the page.

## 9. Publish and report
- Republish the library artifact at the URL in `HANDOFF.md`, using `dist/index.html` with `files` taken from `dist/files.json`.
- Update `RESUME.md` and `tasks/todo.md`.
- Tell Nathan, in a few lines:
  - what was added
  - the overall confidence
  - the main disagreements and what you chose
  - what the reviewer found
  - what remains open
