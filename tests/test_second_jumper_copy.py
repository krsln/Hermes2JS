"""Two tests jumping to one short tail: the later one gets its own copy, on the last rung (F-194).

    if (kind !== 1) goto T; r4 = env[1]; if (r4 === undefined) goto T; ...; T: x; END:

`A || B` would be the natural reading, but `B` reads `r4`, set by a statement of the else arm in front of it, so
the test cannot move up into the condition (F-185 does that only when nothing prints in front of it) and the tail
is not a lone `return` (`SharedReturnDuplicationCfgPass`). `_copy_for_the_second_jumper` gives the later test a copy
of the tail (up to six instructions, only jumps reach it, it runs on into `END`) and leaves the original to the
first one. Only on the last rung, `per_predecessor`: on a function that structures without it the copy would break
an `||` chain apart.

    98/13588 `get` (reanimated mutables)   98/5905 `getNavigationConfig`
"""

from pathlib import Path

from hermes_decompiler.Decompiler import Decompiler

_DATA = Path(__file__).parent / "data"


def _render(name: str, function_id: int) -> str:
    hasm = (_DATA / name).read_text(encoding="utf-8")
    out = Decompiler.render(Decompiler.build_context(hasm, function_id, strict=False), verbose=False, raw=False)

    return "\n".join(line for line in out.split("\n") if not line.strip().startswith("//"))


def test_the_second_test_that_jumps_to_the_tail_has_its_own_copy():
    out = _render("second_jumper_copy_98_13588.hasm", 13588)

    assert "goto" not in out
    assert out.count("r3 = r4.getSync();") == 2
    assert "if (r4 === undefined) {" in out


def test_a_navigation_config_with_two_tests_to_one_tail_has_no_goto():
    out = _render("second_jumper_copy_98_5905.hasm", 5905)

    assert "goto" not in out
