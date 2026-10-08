# HANDOFF: read this first

**Project:** Battle Atlas, Osprey-style 3D phase-by-phase battle maps. It lives at `~/battle-maps/` on Nathan's Mac, and the library is published at https://claude.ai/artifact/Gbh8cmwciTY9jRqqHbMX54 .

**Current state:** v1 is published (Austerlitz 1805 and Rossbach 1757). The v2 work is planned in `tasks/plan-v2.md`, with 0 of 28 steps done. Git checkpoint: `fa7b547` (v1).

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
