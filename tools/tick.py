"""Mark a v2 plan step done: tick it in tasks/plan-v2.md, log it in HANDOFF.md, commit.
usage: python3 tools/tick.py T2 "what was done, anything the next agent must know"
"""
import datetime, os, re, subprocess, sys
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
step, note = sys.argv[1], sys.argv[2]
p = os.path.join(ROOT, "tasks", "plan-v2.md"); s = open(p).read()
s2 = re.sub(r"- \[ \] \*\*" + re.escape(step) + r"\b", f"- [x] **{step}", s)
if s2 == s and f"- [x] **{step}" not in s: raise SystemExit(f"step {step} not found")
open(p, "w").write(s2)
h = os.path.join(ROOT, "HANDOFF.md"); t = open(h).read()
if "## Progress log" not in t: t += "\n## Progress log (newest last)\n"
t += f"- {datetime.datetime.now():%Y-%m-%d %H:%M} **{step}**: {note}\n"
open(h, "w").write(t)
subprocess.run(["git", "add", "-A"], cwd=ROOT, check=True)
subprocess.run(["git", "commit", "-qm", f"v2 {step}: {note[:70]}\n\nCo-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>"], cwd=ROOT, check=True)
print("ticked + committed", step)
