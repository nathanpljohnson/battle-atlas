"""Synthetic two-day fixture for testing the multi-day timeline (not a real battle; never add to library.json)."""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, "..", "..", "tools")); os.chdir(HERE)
from battlekit import Battle
B = Battle("fixture_multiday", HERE)
B.source("none", "Synthetic test data", None, "not historical", "data")
B.meta = {"title": "Test Fixture", "year": "0000", "era": "early-modern", "war": "Test", "eyebrow": "TEST · two days", "subtitle": "Synthetic data for testing the multi-day timeline.",
          "sides": {"a": {"name": "Blue", "top": "#2b4f93", "side": "#1d3767", "mark": "#fff", "arrow": "#3c6fd8"}, "b": {"name": "Red", "top": "#b5432f", "side": "#7f2d20", "mark": "#fff", "arrow": "#d4513a"}},
          "belligerents": [{"name": "Blue", "commander": "A", "sides": ["a"], "code": "letters"}, {"name": "Red", "commander": "B", "sides": ["b"], "code": "numbers"}],
          "forces": {"start": [{"label": "Blue", "n": 5000, "segs": [["a", 1]]}, {"label": "Red", "n": 5000, "segs": [["b", 1]]}]},
          "sun": {"lat": 51.25, "decl": 20, "note": ""}, "method": "Test.", "days": ["1 July", "2 July", "3 July"]}
B.place("Rossbach", (51.2607, 11.8922)); B.place("Lunstädt", (51.2601, 11.9092))
u = B.unit("u1", "a", "inf", "Blue brigade", "5 bns", 600, cite=["none"], men=5000, conf="high")
v = B.unit("v1", "b", "inf", "Red brigade", "5 bns", 600, cite=["none"], men=5000, conf="high")
for i, (day, t) in enumerate([(1, "14:00"), (1, "18:00"), (2, "06:00"), (2, "12:00"), (3, "09:00")]):
    u.at(i, ("Rossbach", 0, 300 * i), 90, "L", men=5000 - 600 * i); v.at(i, ("Lunstädt", 0, 300 * i), 270, "L" if i < 4 else "R", men=5000 - 900 * i)
    B.phase(t, f"D{day} {t}", f"Day {day} at {t}", f"Test text [none].", ("Test", "Test.", None), "Rossbach", 6, day=day, conf="high", cite=["none"])
B.export()
