"""Short-circuit tests inside a loop body fold like any others (F-169).

`ShortCircuitConditionCfgPass` left EVERY block of a loop alone, so a `for-in` body's

    if (!a || typeof a !== "object") { init }

stayed `if (!a) { init } else { ...; if (typeof a === "object") goto J }` and, worse, dropped the fall from the
second test into `init`. Only the loop's own tests (header, latches) are off limits now, and a fold may end on
a latch when nothing has to be copied onto the edge into it. Case labels keep their own tests in a body (the
`switch` wants them).

    96/11027  the `||` in a `for-in` body (the old output lost a path)
    98/2211   `processTransformOrigin`: a `switch` in a loop body stays a `switch`
    96/2026   `refreshCache`: two tests that leave the loop are still one `||`
"""

from pathlib import Path

from hermes_decompiler.Decompiler import Decompiler

_DATA = Path(__file__).parent / "data"


def _render(name: str, function_id: int) -> str:
    hasm = (_DATA / name).read_text(encoding="utf-8")
    out = Decompiler.render(Decompiler.build_context(hasm, function_id, strict=False), verbose=False, raw=False)

    return "\n".join(line for line in out.split("\n") if not line.strip().startswith("//"))


def test_the_second_test_falls_into_the_init():
    out = _render("loop_body_crossed_or_96_11027.hasm", 11027)

    assert "goto" not in out
    assert 'if (!r9 || typeof r2[2][r1[0]] !== "object") {\n            r9 = {  };' in out


def test_a_switch_in_a_loop_body_stays_a_switch():
    out = _render("loop_body_case_chain_98_2211.hasm", 2211)

    assert "goto" not in out
    assert "switch (r30) {" in out


def test_two_tests_that_leave_the_loop_are_one_or():
    out = _render("loop_body_leave_loop_or_96_2026.hasm", 2026)

    assert "goto" not in out
    assert "if (24 === r4 || 3 === r4) {" in out
