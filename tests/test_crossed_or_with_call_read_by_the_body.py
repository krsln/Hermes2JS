"""A crossed `||` whose second test is a call the body reads again stays one condition (F-273).

`if (a == null || (r19 = f(x)) == null) { scalar } else { recursion(r19) }` compiles to a first test that jumps
to the second test's fall-through; the second test's call result is read again on the way to the `else`
(96/1561 `accumulateDifferences`). The call stays in the condition as an assignment; the register copy
`r22 = r19` that only the test reads is dropped (the exits copy `r22` on into `r1`, which nobody reads).
"""

from pathlib import Path

from hermes_decompiler.Decompiler import Decompiler

_DATA = Path(__file__).parent / "data"


def test_the_second_call_is_part_of_the_condition_and_its_result_is_kept():
    hasm = (_DATA / "crossed_or_with_call_read_by_the_body_96_1561.hasm").read_text(encoding="utf-8")
    out = Decompiler.render(Decompiler.build_context(hasm, 1561, strict=False), verbose=False, raw=False)

    assert "goto" not in out
    assert "if (r20 != null && (r19 = " in out
    assert "r30 = r19;" in out
