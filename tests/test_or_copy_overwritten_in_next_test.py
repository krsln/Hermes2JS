"""A copy that the next test overwrites before reading does not keep `&&` from folding (96/1998 `updateActionStateImpl`).

`r6 = 'function'` in the following test rewrites the register the folded setup copy wrote, so the copy is private to
the block that reads it; the scan used to treat the later write as a reader and left a goto.
"""

from pathlib import Path

from hermes_decompiler.Decompiler import Decompiler

_DATA = Path(__file__).parent / "data"


def test_the_type_guard_is_one_condition():
    hasm = (_DATA / "or_copy_overwritten_in_next_test_96_1998.hasm").read_text(encoding="utf-8")
    out = Decompiler.render(Decompiler.build_context(hasm, 1998, strict=False), verbose=False, raw=False)

    assert "goto label" not in out
    assert 'if ("object" === r5 && null !== r4 && "function" === typeof r4.then) {' in out
