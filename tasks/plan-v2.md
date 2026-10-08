# Battle Atlas v2: master plan

This file is the source of truth for the v2 work. If the session stops, a new agent should:
1. Read `HANDOFF.md`.
2. Read this file.
3. Run `git log --oneline` (every finished step is its own commit).
4. Continue from the first unchecked box.

Nathan asked for every item below to be done, autonomously, to a historian's standard, with handoff docs kept current. He can't fact-check the history himself.

Conventions: one commit per step (`git add -A && git commit -m "v2 <step id>: ..."`). After each step, tick the box here and update the "Current state" line in `HANDOFF.md`.

## Stage T: tooling and method (the /battle-map skill)
- [x] **T1 Map matching tool.** `tools/georef.py`, generic. Per battle, `maps.json` holds `{map_id: {file, gcps: {place: [x, y]}}}`. It fits a 1st- or 2nd-order transform, reports residuals, flags outliers (more than 600 m, or 3σ), writes `georef.json`, and warps each map into a bbox-aligned overlay JPG. battlekit gets `B.mapxy(map_id, x, y)`. Austerlitz is migrated off `georef.py`.
- [x] **T2 Historical gazetteer.** `tools/gazetteer.py <battle dir> names.json`:
  - Look up each historical (German, French, etc.) name in Wikidata (labels and aliases in all languages, P625 coordinates), and in Nominatim with the modern name.
  - Flag any disagreement over 1 km.
  - Write `places.json` plus `gazetteer_report.md`.
- [x] **T3 Modern change detection.** `tools/terrain.py --detect` queries OSM Overpass in the bbox for quarries, opencast mines, landfill, spoil heaps, reservoirs, basins and motorways, then:
  - Writes `terrain_suggestions.json` and auto-adds masks for mining, quarry, landfill and spoil areas over 2 ha. Water bodies are only suggested, because a historical lake must not be erased.
  - Also flags DEM anomalies: pits or heaps more than 12 m off a 600 m-blur surface.
  - Draws a preview with the flagged areas outlined.
- [x] **T4 battlekit v2:**
  - **Citations:** `sources = {id: {...}}`, `cite=[ids]` on units, phases and events, and inline `[id]` markers in text, all validated.
  - **Strength over time:** `men={phase: n}`, carried forward.
  - **Route waypoints:** `via=[pos, ...]` on keys.
  - **Multi-day:** `day=` on phases.
  - **Eras:** `era` in meta and the new unit types.
  - **Tactics:** an id on each phase's tactic.
  - **Overlays and fog:** an `overlays` list in meta; `fog` (0–1) on phases.
- [x] **T5 Physical sanity checks** in `battlekit.validate`, as warnings, plus `--strict` to fail on them:
  - movement speed between phases by unit type
  - unit centre inside a lake
  - overlapping hostile units with no F, R or charge
  - crossing a river away from a ford, bridge or causeway (`B.crossings`)
  - unit strengths summing to `forces.start` within 15%
  - every unit with a citation; every phase with a citation and a confidence level
- [x] **T6 Second-opinion review protocol.** `tools/review_prompt.md`, a template for an independent reviewer agent. It gets the brief, the scenario and the sources, and must return a list of issues with severity. The output is saved as `battles/<id>/review.md` and each issue is resolved or rebutted in `brief.md`.
- [x] **T7 Tactics glossary.** `tactics.json` maps each tactic id to `{name, summary, era}`; battles reference ids. `build_library.py` builds a cross-link index (tactic → battle and phase).
- [x] **T8 Update `~/.claude/commands/battle-map.md`** to use T1–T7, with stronger source requirements (scholarly works via the Internet Archive and Google Books, non-English sources, official histories).

## Stage E: engine (renderer)
- [x] **E1 Strength-driven blocks:**
  - Block count is men divided by men-per-block (inf 700, gd 600, cav 300, lc 250, art 6 guns per block, lt 400), clamped to 1–14.
  - Blocks disappear as `men` falls.
  - A small strength readout appears on the unit card.
- [x] **E2 Realistic movement:**
  - Moves follow `via` waypoints, falling back to a gentle curve.
  - Units in column snake: each block trails the leader along the path.
  - Lines advance rigidly but turn about their centre.
  - Arcs come from the authored arrows when no `via` is given (a nearest-arrow heuristic).
- [x] **E3 Fog and smoke:**
  - Fog is valley-hugging sprite layers with opacity from `phase.fog` and density set by low elevation.
  - Smoke from firing lines lingers and drifts downwind (`meta.wind`).
- [x] **E4 Overlays toggle:** "Historical map" drapes the warped source map (or a 19th-century survey) onto the terrain, with an opacity slider. There is one toggle per overlay in a dropdown.
- [x] **E5 Contour and scale toggles:**
  - Contours are 10 m lines painted onto a second canvas, blended over the terrain.
  - The scale bar is computed from the camera at the view centre and snaps to 250 m, 500 m, 1 km or 2 km.
- [x] **E6 Label collision:** a priority-based greedy declutter (events > selected > HQ > places > hills > units), with Osprey-style leader lines for events.
- [x] **E7 Proportional, multi-day timeline:**
  - Stops sit at their real times; gaps over 6 h are compressed and get a break mark.
  - Day dividers say "1 July", "2 July".
  - The clock shows the day.
- [x] **E8 Strength-over-time chart:**
  - A small SVG chart in the panel: one line per belligerent across the phases, with a marker for the current phase.
  - Losses are shaded.
  - The "Estimated" caveat comes from the data.
- [x] **E9 Citations UI:**
  - Inline `[id]` markers become numbered superscripts that link to the Sources tab.
  - The unit card lists its sources, and the Sources tab gives each source's number.
- [x] **E10 Tactics links:** the tactic box shows "Also seen at: <battle · time>" links that jump to that battle and phase. Deep links use `#<id>` or `#<id>.p<n>`.
- [x] **E11 Library home page:**
  - Opens when there is no hash, and from a "Library" button.
  - Cards for each battle (title, year, war, era, sides, a confidence summary).
  - Filters by era and war.
  - A timeline strip of the battles, and a tactics index.
- [x] **E12 Eras.** New unit types and symbols:
  - ancient and medieval: heavy infantry and phalanx (`hi`), archers and missile troops (`arc`), knights and heavy horse (`kn`), elephants (`ele`), chariots (`cha`)
  - modern: armour (`arm`), mechanised infantry (`mech`), machine guns (`mg`)

  Each has a symbol and a glossary text. Naval battles are documented as out of scope.

## Stage D: data
- [x] **D1 Austerlitz v2:**
  - `maps.json` and an overlay from the georeferenced Russian 1844 map (map 7 or 8) and West Point map 23.
  - Citations on every unit, phase and event, with inline `[id]` markers in the text.
  - `men` per phase, with losses estimated and marked as such.
  - Fog at 07:00–09:00; `via` routes for the columns; tactic ids; crossings declared.
  - Must pass the strict checks.
- [x] **D2 Rossbach rebuilt the Austerlitz way.** Done when it passes the strict checks and its review is resolved.
  - **Sources:** at least 3 independent ones plus maps, for example the West Point Seven Years' War maps, the Prussian General Staff *Die Kriege Friedrichs des Großen* plans, Kronoskaf, Wikipedia, and Duffy or Millar summaries.
  - **Groundwork:** gazetteer and map matching.
  - **Data:** a new `battles/rossbach/scenario.py` written with battlekit, plus `brief.md`, citations and strengths.
  - **Terrain:** detect and mask the mining pits automatically, then compare with the v1 hand-made masks.
  - **Retire:** the old `make.py`.
- [ ] **D3 Second opinion** on both battles: a reviewer agent per battle, then fixes applied and `review.md` saved.
- [ ] **D4 A third battle from another era**, to exercise eras, tactics links and the home page: Cannae, 216 BC (envelopment, which links to Austerlitz). The disputed site goes in a debate note with low confidence.
- [x] **D5 Multi-day test:** a small synthetic multi-day fixture (`tests/fixture_multiday.json`, not in the library) to check the E7 timeline. Optional: a real multi-day battle later.

## Stage S: ship
- [ ] **S1** Build, then test in the browser:
  - each battle, at desktop size and 375 px, in light and dark themes
  - the toggles (overlay, contours, scale, labels)
  - the home page and deep links
- [ ] **S2** Republish the library artifact at the same URL (`dist/index.html`, plus `battles/*.json` and overlay images as files).
- [ ] **S3** Update `README.md`, `HANDOFF.md`, `RESUME.md`, the memory note and `~/.claude/commands/battle-map.md`, then make the final commit.
