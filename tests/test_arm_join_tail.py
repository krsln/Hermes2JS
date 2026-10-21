"""
F-126: an `if` arm whose own test jumps to the code the outer branch skips to.

    96/1333 `getValidLengthPercentageSizeOrNull`: the `"px"` arm falls through to the `"%"`
    check when its number is invalid. The `"%"` check used to be printed inside the other
    arm, so an invalid `"px"` value returned `undefined` instead of reaching `return null`.
"""

from pathlib import Path

from hermes_decompiler.Decompiler import Decompiler

_DATA = Path(__file__).parent / "data"


def test_the_skipped_to_code_follows_the_if_instead_of_sitting_in_one_arm():
    hasm = (_DATA / "arm_test_joins_tail_96_1333.hasm").read_text(encoding="utf-8")
    out = Decompiler.render(Decompiler.build_context(hasm, 1333, strict=False), verbose=False, raw=False)

    assert "goto" not in out
    assert 'if (r2) {' in out
    # the "%" test is reached after the "px" arm, not only when "px" failed
    assert out.index('endsWith("%")') > out.index("return r2;")
    assert out.count("return null;") == 2
