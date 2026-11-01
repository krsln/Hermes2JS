"""
A tree without a `goto` that lost a path gets the shared-return/-tail retries too.

98/12551: `if ("readable" !== state) goto TAIL; ...; r1 = r3[98].call(...); TAIL: r3[105].call(...); throw p`.
The first attempt printed the `else` arm without the `TAIL` it falls into (the function returned
`undefined` where it had to call and throw). `flow_audit.count_lost_edges` sees the lost path, so the
retries run, and one that has no `goto` and loses fewer paths is the output. 96/2602 is the same
mechanism (the `6 === tag` test's edge to the shared body, F-148).
"""

from pathlib import Path

from hermes_decompiler.Decompiler import Decompiler

_DATA = Path(__file__).parent / "data"


def _render(name: str, function_id: int) -> str:
    hasm = (_DATA / name).read_text(encoding="utf-8")
    return Decompiler.render(Decompiler.build_context(hasm, function_id, strict=False), verbose=False, raw=False)


def test_the_fall_through_arm_still_runs_the_shared_throw_tail():
    out = _render("lost_throw_tail_98_12551.hasm", 12551)

    assert "goto" not in out
    assert out.count("throw param1;") == 2
    assert out.count("r3[105]") == 2


def test_the_edge_of_a_case_test_to_the_shared_body_is_kept():
    out = _render("lost_case_edge_96_2602.hasm", 2602)

    assert "goto" not in out
    assert "case 6:" in out or "6 === r4" in out
