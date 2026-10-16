# Battle map library

Goal: a reusable system that turns a battle name into an Osprey-style 3D phase map, collected in one library page (tab per battle). First new battle: Austerlitz 1805. Standard: cross-check multiple sources like a PhD military historian; tag confidence.

## A. Engine + tooling
- [x] engine/index.src.html: generic renderer (battle JSON contract, battle switcher, water, camps, confidence, sources)
- [x] tools/terrain.py: DEM download + fill from battles/<id>/terrain_config.json (lat/lon masks + bumps)
- [x] tools/battlekit.py: authoring helpers (place anchors, units, phases, arrows), validation, export JSON, check plot
- [x] tools/build_library.py: dist/index.html (+ preview.html) + dist/battles/*.json
- [x] battles/rossbach/make.py: migrate Rossbach into the contract; verify identical-looking result

## B. Method
- [x] ~/.claude/commands/battle-map.md: research + extraction + verification protocol

## C. Austerlitz
- [x] Research: >=3 independent sources + West Point situation maps; write battles/austerlitz/brief.md (with disagreements + confidence)
- [x] Geocode places (places.json; Bosenitz=Tvarožná), georef.py (West Point maps), terrain (needs 2 small masks near Jiříkovice)
- [x] scenario.py -> austerlitz.json, check.png compared to West Point maps
- [x] Build library, verify in browser (desktop/mobile, both themes)

## D. Ship
- [x] Publish library artifact (multi-file), record URL
- [x] README.md for humans + agents, RESUME.md, memory note

## Follow-ups (optional)
- [ ] Phone-width check of Austerlitz (desktop verified; layout shared with Rossbach, which passed at 375px)

## Franklin 1864 (added 2026-10-16)
- [ ] 1 Sources: narratives, maps, scholarly/official (OR, Cox, Jacobson/Sword)
- [ ] 2 brief.md
- [ ] 3 places (gazetteer) + map matching
- [ ] 4 terrain
- [ ] 5 scenario.py
- [ ] 6 strict validation + check.png
- [ ] 7 independent review
- [ ] 8 library + browser test
- [ ] 9 publish + report
