# Rossbach 1757 interactive map

Goal: one HTML page, Osprey-style tilted 3D terrain slab of the Rossbach battlefield, step through timed phases with unit blocks (inf/cav/art), movement arrows, numbered notes, order of battle. Publish as an Artifact.

- [x] Geocode villages/landmarks (Nominatim) -> data/places.json
- [x] Download DEM tiles (AWS terrarium), build heightmap grid -> data/height.json (fill modern mining pits)
- [x] Write scenario: data/scenario.py -> data/scenario.json (27 units, 10 phases; 2D check in data/phases_check.png)
- [x] Build page: three.js terrain + painted texture, units, arrows, labels, timeline UI -> rossbach.html
- [x] Check locally (preview server "rossbach" on :8790 in ~/.claude/launch.json; pane throttles rAF when hidden)
- [x] Publish artifact: https://claude.ai/artifact/GAeKCZLkA7N42DBGvjmEXk
