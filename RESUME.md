Task: Battle Atlas: reusable 3D battle-map library (one page, tab per battle) + /battle-map command. First new battle: Austerlitz 1805.
Completed: engine, tools, Rossbach migrated, Austerlitz researched (brief.md), built, checked against West Point + Russian 1844 maps, verified in browser, published.
Library URL: https://claude.ai/artifact/Gbh8cmwciTY9jRqqHbMX54 (republish dist/index.html with files battles/*.json; same file path keeps the URL, or pass url=)
Next: nothing required. To add battles: /battle-map <name>. See README.md for layout, data contract, testing.
Files: README.md, library.json, engine/index.src.html, tools/{terrain,battlekit,build_library}.py, battles/{rossbach,austerlitz}/, dist/, ~/.claude/commands/battle-map.md
Notes:
- Nathan can't fact-check battles: cross-check sources, record disagreements/confidence in brief.md and data (conf, debate).
- Georeference source maps with control points (battles/austerlitz/georef.py) and author positions in map pixels.
- Python SSL broken -> curl. Hidden browser pane throttles rAF. Preview server 'battle-library' :8791.
