Task: Add Franklin 1864 to Battle Atlas (/battle-map skill).
Completed: steps 1-6 and 8 (sources, brief, places/georef, terrain, scenario, strict validation, library build and browser check). Commit ac43495.
Next: step 7. Save the reviewer agent's reply to battles/franklin/review.md, answer every issue in brief.md under "Review responses", fix and rebuild. Then step 9: redeploy (the ChatGPT Site is deployed from the ChatGPT side; dist/battle-atlas-offline.html is current).
Files written: battles/franklin/*, tactics.json (frontal-assault, exposed-outpost), library.json
Notes: positions are j()/k() pixel helpers on the two Jespersen maps (see scenario.py docstring). Brigade strengths are estimates; losses are reconciled to 2,326 / 6,252.
