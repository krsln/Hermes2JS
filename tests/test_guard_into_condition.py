"""`if (A) { if (B) goto NEXT; X }` NEXT: -> `if (A && !B) { X }` (96/1351 `processTransformOrigin`).

`switch (key) { case "left": case "right": L ...; case "top": ...; }` inside a loop compiled to
`if (key !== "left") { if (key === "right") goto L; <switch of the rest>; continue } L: ...`. The arm ends in a
`continue`, so the structurer found no join for the guard and the shared label `L` stayed a raw `goto`. The last
rung of the retry ladder folds a guard that is nothing but its test, first in the arm, into the arm's condition.
"""

from pathlib import Path

from hermes_decompiler.Decompiler import Decompiler

_DATA = Path(__file__).parent / "data"


def _render(name, index):
    hasm = (_DATA / name).read_text(encoding="utf-8")

    return Decompiler.render(Decompiler.build_context(hasm, index, strict=False), verbose=False, raw=False)


def test_a_shared_label_guard_joins_the_condition():
    out = _render("guard_into_condition_96_1351.hasm", 1351)

    assert "goto label" not in out
    assert 'if ("left" !== r32 && "right" !== r32) {' in out
