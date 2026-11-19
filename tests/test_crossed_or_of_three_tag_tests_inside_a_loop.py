"""`if (0 === t || 11 === t || 15 === t) { ... }` inside a `while (true)` (F-217, 98/2658).

    if (0 === t) goto A; if (11 === t) goto A; if (15 !== t) goto END; A: ...

The tests of a `case`-looking chain stay apart inside a loop, and a loop block's test is never folded; but here the last
test falls into the first one's target (no `switch` has a body entered by a later test's fall-through) and no target of the
tests leaves the loop, so they are one `||`. Left apart, the output was `if (0 === t || 11 === t) { ... } else {
if (15 !== t) goto label_147; }`, a `goto` out of the `try`.
"""

from pathlib import Path

from hermes_decompiler.Decompiler import Decompiler

_DATA = Path(__file__).parent / "data"


def test_the_three_tag_tests_are_one_condition_without_a_goto():
    hasm = (_DATA / "crossed_or_of_case_tests_in_loop_98_2658.hasm").read_text(encoding="utf-8")
    out = Decompiler.render(Decompiler.build_context(hasm, 2658, strict=False), verbose=False, raw=False)

    assert "0 === r10 || (11 === r10 || 15 === r10)" in out
    assert "goto label_" not in out
