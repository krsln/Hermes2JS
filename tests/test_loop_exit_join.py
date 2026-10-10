"""
A join block that is also an inner loop's latch, behind an `if` whose arm
carves out a `break`.

    if (i === 2 && j === 2) break outer;   // 0x3d / 0x41
    hits = ...;                            // 0x45, the latch: runs on every path

`IfStructurer` classified the `break` marker region (synthetic block, not in
the dominator tree) as belonging to neither arm, bailed, and a later pass left
the latch's `Mov r13, r4` inside the `if`. It must print after it.
"""

import re
from pathlib import Path

from hermes_decompiler.Decompiler import Decompiler

_FIXTURES = Path(__file__).resolve().parent.parent / "apps" / "demo" / "fixtures"


def _render(fixture: str, index: int, name: str) -> str:
    hasm = (_FIXTURES / fixture / "sections" / f"function_{index}_{name}.hasm").read_text(encoding="utf-8")
    return Decompiler.render(Decompiler.build_context(hasm, index), verbose=False)


def test_the_latch_runs_after_a_conditional_break():
    out = _render("96", 15068, "tripleNestedLabeledTest")

    assert re.search(
        r"if \(r8 === 2 && r11 === 2\) \{\s*break loop_1;\s*\}\s*r13 = r4;", out
    ), out


def test_the_same_shape_in_the_other_bundle():
    out = _render("98", 9459, "tripleNestedLabeledTest")

    assert re.search(
        r"if \(r11 === 2 && r7 === 2\) \{\s*break loop_1;\s*\}\s*r0 = r3;", out
    ), out
