"""
`updateSlot` (96/1925): `if (typeof x !== "object") goto RET; ...; <last else arm falls into RET>`
with `RET: return null` placed after the arm. The shared `return null` became the *then* arm of
the type test and the last `else` ended without it (the function returned undefined there).
"""

from pathlib import Path

from hermes_decompiler.Decompiler import Decompiler

_DATA = Path(__file__).parent / "data"


def test_last_arm_still_returns_null():
    hasm = (_DATA / "arm_runs_into_shared_return_96_1925.hasm").read_text(encoding="utf-8")
    out = Decompiler.render(Decompiler.build_context(hasm, 1925, strict=False), verbose=False, raw=False)
    lines = [line.strip() for line in out.splitlines()]
    assert "return null;" in lines
    assert "goto" not in out


def test_loop_exits_to_a_shared_return_are_not_joined():
    """98/4137: the `return false` exits of a `for` loop stay in the loop, `r4 = true` follows it."""
    hasm = (_DATA / "loop_exit_return_after_if_98_4137.hasm").read_text(encoding="utf-8")
    out = Decompiler.render(Decompiler.build_context(hasm, 4137, strict=False), verbose=False, raw=False)
    assert "break;" not in out
    assert out.count("return false;") >= 4
