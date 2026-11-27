"""A value test folded away inside a loop leaves no stale block behind (96/1927 `reconcileChildrenArray`).

`ValueConditionFoldCfgPass` removes the blocks of an `a && b && c` that is only tested. The loop and dominator
analyses were redone only when the LATER short-circuit pass removed blocks, so the folded-away `r16 = r15` block was
still a member of the loop: it was printed as a statement of its own (`r16 = r23[0] && param2; r16 = param2;`, a wrong
test) and the loop kept four `goto`s.
"""

from pathlib import Path

from hermes_decompiler.Decompiler import Decompiler

_DATA = Path(__file__).parent / "data"


def _render() -> str:
    hasm = (_DATA / "folded_value_test_inside_a_loop_96_1927.hasm").read_text(encoding="utf-8")

    return Decompiler.render(Decompiler.build_context(hasm, 0, strict=False), verbose=False, raw=False)


def test_no_goto_is_left():
    assert "goto" not in _render()


def test_the_folded_test_is_not_followed_by_its_dead_copy():
    out = _render()

    assert "r16 = r23[0] && r15 && null === r25.alternate" in out
    assert "r16 = param2;" not in out
    assert "r16 = r15;" not in out
