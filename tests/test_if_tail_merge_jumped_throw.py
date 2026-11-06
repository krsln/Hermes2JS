"""
`IfTailMergeRegionPass` leaves a `throw` that something jumps to where it is (F-209, 98/2798 `mark`).

An arm's last block that other code JUMPS to is not the arm's end just because it is the last item: the
pass hoisted its trailing `throw r3` into one `throw` after the `if`, so the jumper printed
`r3 = new TypeError(...)` and fell on into the code behind it. Twenty-one files (96 and 98) printed a
`throw` as an assignment this way (`BottomTabBar`, `commitRoot`, `createChild`, ...).
"""

from pathlib import Path

from hermes_decompiler.Decompiler import Decompiler

_DATA = Path(__file__).parent / "data"


def _code() -> str:
    hasm = (_DATA / "if_tail_merge_jumped_throw_98_2798.hasm").read_text(encoding="utf-8")
    out = Decompiler.render(Decompiler.build_context(hasm, 2798, strict=False), verbose=False, raw=False)

    return "\n".join(line for line in out.split("\n") if not line.strip().startswith("//"))


def test_each_error_is_thrown_where_it_is_made():
    code = _code()

    assert code.count("throw new TypeError(") == 4
    assert "r3 = new TypeError" not in code


def test_no_throw_is_left_for_the_end_of_the_function():
    assert "throw r3;" not in _code()
