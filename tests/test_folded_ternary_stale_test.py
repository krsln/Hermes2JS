"""
A folded ternary is not copied into a test that reads after its register changed (F-140, 96/1595 `deepDiffer`).

    r1 = arguments[2] ... r5 === undefined ? -1 : arguments[2]   # the defaulted `maxDepth`
    r5 = arguments.length <= 3 ? undefined : arguments[3]        # `r5` now holds something else
    if (typeof r1 === "number") ...                              # the test reads the merge

`repoint_references` gave terminators and region conditions the ternary unconditionally, so the
tests printed `typeof (r5 === undefined ? -1 : arguments[2])` with the stale `r5`. They now take the
same per-reader decision as an instruction does (the register when the ternary's test was reassigned).
"""

from pathlib import Path

from hermes_decompiler.Decompiler import Decompiler

_DATA = Path(__file__).parent / "data"


def _code() -> str:
    hasm = (_DATA / "folded_ternary_stale_test_96_1595.hasm").read_text(encoding="utf-8")

    return Decompiler.render(Decompiler.build_context(hasm, 1595, strict=False), verbose=False, raw=False)


def test_a_test_after_the_ternary_register_changed_reads_the_register():
    code = _code()

    assert code.count('if (typeof r1 === "number") {') == 2
    assert "typeof (r5 === undefined" not in code


def test_a_copy_in_a_loop_is_not_read_by_a_branch_the_write_cannot_reach():
    # F-140: `r17 = r6` (the recursive call's argument, in the loops) made `r6 != null` in the
    # `typeof function` branch print `r17 != null`; nothing sets `r17` on that path.
    code = _code()

    assert "r17 != null" not in code
    assert "if (r6 != null) {" in code
