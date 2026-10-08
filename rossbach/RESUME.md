Task: Interactive Osprey-style 3D map of the Battle of Rossbach (5 Nov 1757), stepping through timed phases; published as a claude.ai Artifact.
Completed: Built and published v1 -> https://claude.ai/artifact/GAeKCZLkA7N42DBGvjmEXk . Verified locally at desktop and phone widths, light and dark themes, no console errors.
Next: Nothing required. Possible follow-ups: more battles (reuse pipeline), finer unit granularity, Blender renders.
Files written:
- src.html            page template (three.js 0.147 + OrbitControls); placeholders /*SCENARIO*/null, /*HMETA*/null, /*HEIGHT*/
- build.py            inlines data -> rossbach.html (publish this) + preview.html (local test wrapper)
- data/scenario.py    ALL battle content: units, positions per phase, arrows, events, narrative, places, roads, woods -> data/scenario.json
- data/dem.py, data/fill.py  elevation download (AWS terrarium z13) + mining-pit fill + Janus/Polzen hill bumps -> data/height.json
- data/geocode.py, data/places.json  Nominatim lookups
- tasks/todo.md
Notes:
- To change content: edit data/scenario.py -> `python3 data/scenario.py` (run from data/) -> `python3 build.py` -> republish rossbach.html with the Artifact tool (same file path keeps URL; from a new session pass url=above).
- Unit keys: {phase_index: [lat, lon, facing_deg, form]} with carry-forward; form X camp, C column, L line, F firing (smoke), R rout.
- Local preview: preview server "rossbach" (port 8790) added to ~/.claude/launch.json; open /preview.html. Browser pane throttles rAF when hidden -> animations look frozen in screenshots; not a bug.
- Python SSL certs broken on this machine -> network calls go through curl.
- Positions are approximate reconstructions; timings follow Millar (Osprey Campaign 113).
