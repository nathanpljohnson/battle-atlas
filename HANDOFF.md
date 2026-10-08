# HANDOFF: read this first

**Project:** Battle Atlas, Osprey-style 3D phase-by-phase battle maps. It lives at `~/battle-maps/` on Nathan's Mac, and the library is published at https://claude.ai/artifact/Gbh8cmwciTY9jRqqHbMX54 .

**Current state:** v1 is published (Austerlitz 1805 and Rossbach 1757). The v2 work is planned in `tasks/plan-v2.md`; ticked boxes there are done, and the progress log at the bottom of this file says what each step left behind. Git checkpoint for v1: `fa7b547`. Mark a step done with `python3 tools/tick.py <step> "note"`, which ticks it, logs it here and commits.

## How to resume
1. `cd ~/battle-maps && git log --oneline | head` shows which v2 steps are committed.
2. Open `tasks/plan-v2.md` and do the first unchecked step. Commit it, tick its box, and update **Current state** above.
3. Read `README.md` for the layout, data contract and commands.

## What Nathan wants (his words, condensed)
Rebuild Rossbach the Austerlitz way, and make moves feel realistic:
- snaking columns
- block size and losses driven by strength
- fog and smoke
- a historical-map ground toggle
- decluttered labels
- a proportional timeline
- scale bar and contours as toggles
- a strength-over-time chart
- more scholarly sources
- every claim cited
- a second opinion
- a standard map-matching tool
- physical sanity checks
- proper historical place lookup
- automatic detection of modern changes to the ground
- other eras
- multi-day and large battles
- links between battles and tactics
- a library home page

All of it should be done autonomously, with handoff docs kept current. He can't fact-check the history: the work should be judged as a PhD military historian would judge it.

## Environment facts
- Python 3.13 with numpy and Pillow, but **no scipy**. Python's SSL certificates are broken, so all network calls go through `curl` via `subprocess`. Don't install packages without asking.
- Preview server `battle-library` in `~/.claude/launch.json` serves `dist/` on port 8791; open `/preview.html#<id>`.
- A hidden browser pane throttles `requestAnimationFrame` to about 1 fps, so wait before taking screenshots. Changing only the `#hash` doesn't reload the page.
- Artifact publishing: `dist/index.html` with `files` `{ "battles/<id>.json": "dist/battles/<id>.json", ... }`. Only scripts from cdnjs, jsdelivr and unpkg are allowed; everything else (data, images) must be published files or inline.
- Wikimedia API: send a User-Agent and don't hammer it (sleep 1 s between calls).
- Nominatim: no more than 1 request per second, with a User-Agent.

## Progress log (newest last)
- **T1**: tools/georef.py (generic, leave-one-out outlier flags, 1st/2nd order, overlay warping to .webp). Austerlitz has maps.json (wp23, ru7) -> georef.json, georef_report.md, overlay_wp23.webp, overlay_ru7.webp; scenario uses Georef(HERE)("wp23"). Old battles/austerlitz/georef.py renamed georef_v1_legacy.py.
- 2026-10-08 02:37 **T2**: tools/gazetteer.py: Wikidata aliases + bbox-filtered Wikipedia full-text + Nominatim cross-check, >1km flags; needs a URL-style User-Agent (Wikipedia rate-limits generic ones) and retries. Tested on 11 Austerlitz names: all resolved (Bosenitz->Tvarožná). Sub-locality picks (e.g. 'Sokolnice - Cihelna') can be ~500 m off: check report.
- 2026-10-08 02:41 **T3**: tools/terrain.py --detect: OSM Overpass (cached in battles/<id>/osm_cache.json, --refetch to refresh) -> auto-masks quarries/landfill/spoil and water >8 m below surroundings (flooded pits), grown to exact pit shape saved as terrain_automask.png (raster mask); suggests other water + motorways; reports top-8 DEM heaps/pits (often natural, report-only). Masks now support poly/raster/ellipse. Rossbach: terrain_config.json created, mining pits auto-filled; the spoil heap N of the field (51.285, 11.912) still needs a manual mask in D2.
- 2026-10-08 02:42 **T4**: battlekit v2: B.source + cite=[ids] + inline [id] markers (validated), men={phase:n} via unit(..., men=) or at(..., men=), via=[...] waypoints, phase(day=, fog=, cite=, tactic=(name, body, tactic_id)), B.crossing, B.overlay (exports meta.overlays with file battles/<id>.<ovid>.webp), meta.era/wind, new unit types hi arc kn ele cha arm mech mg; validation.md written each export. Legacy meta.sources list still accepted (Austerlitz until D1).
- 2026-10-08 02:43 **T5**: Sanity checks in battlekit.sanity(): SPEED (per-type km/h incl. via path), CROSSING (river segments not ford=True, needs B.crossing within 450 m), WATER (centre in lake unless R), OVERLAP (hostile <150 m without F/R/charge), STRENGTH (phase-0 men vs forces.start ±15%), missing cite/men/conf. export(strict=True) or BATTLEKIT_STRICT=1 fails on warnings. Austerlitz currently: kie2 sits in Satschan pond 10:00-14:00 and jur in the Austerlitz pond (real bugs to fix in D1), many Goldbach/Littawa crossings need B.crossing at village bridges.
- 2026-10-08 02:44 **T6**: tools/review_prompt.md: template for an independent reviewer agent (general-purpose) -> battles/<id>/review.md; author answers each issue in brief.md 'Review responses' (fixed/rebutted/open).
