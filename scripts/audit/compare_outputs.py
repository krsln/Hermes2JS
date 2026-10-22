"""Compare two decompiled output directories (decompile_sections.py -o).

usage: python3 scripts/audit/compare_outputs.py <base-dir> <new-dir>

Counts changed files, files with goto before/after, files that gained or lost every
goto, and files where the rough definite-assignment check found more unassigned reads.
"""
import os
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import definite_assignment as defcheck  # noqa: E402

if len(sys.argv) != 3:
    sys.exit(__doc__)

base, new = sys.argv[1:3]
newg, fixed, worse, better, changed = [], [], [], 0, 0
for f in sorted(os.listdir(new)):
    a = Path(base, f).read_text()
    b = Path(new, f).read_text()
    if a == b:
        continue
    changed += 1
    ga, gb = a.count("goto "), b.count("goto ")
    if ga == 0 and gb > 0:
        newg.append(f)
    if ga > 0 and gb == 0:
        fixed.append(f)
    try:
        ca, cb = len(defcheck.check(a)), len(defcheck.check(b))
    except Exception:
        continue
    if cb > ca:
        worse.append((f, ca, cb, ga, gb))
    better += cb < ca


def goto_files(directory):
    return sum(1 for f in os.listdir(directory) if "goto " in Path(directory, f).read_text())


print(f"changed {changed}; files with goto {goto_files(base)} -> {goto_files(new)}; "
      f"newly goto {len(newg)}; goto-free now {len(fixed)}; unassigned reads better {better} worse {len(worse)}")
for w in worse:
    print("  WORSE", w)
