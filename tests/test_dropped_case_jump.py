"""A `case` test left to the `switch` pass keeps its jump when no `switch` comes out of it (F-179).

`tag === 27` and `tag === 5` jump to one body. `_absorb_residual_conditional` dropped the second jump into the
sibling arm on the promise that `SwitchStructurer` builds a `switch`; with two bodies behind a residual that is
not a pure chain it does not, and the path was lost: `if (27 === t) { X } else if (5 !== t) { ... }` ran nothing
for `5`. The dropped jump is recorded and `restore_dropped_case_jumps` makes it `if (27 === t || 5 === t) { X }`
when no `switch` took the chain.

    98/2633  `commitLayoutEffectOnFiber`
    98/2628  `safelyAttachRef`: 26 and 27 share the body
"""

from pathlib import Path

from hermes_decompiler.Decompiler import Decompiler

_DATA = Path(__file__).parent / "data"


def _render(name: str, function_id: int) -> str:
    hasm = (_DATA / name).read_text(encoding="utf-8")
    out = Decompiler.render(Decompiler.build_context(hasm, function_id, strict=False), verbose=False, raw=False)

    return "\n".join(line for line in out.split("\n") if not line.strip().startswith("//"))


def test_both_tests_reach_the_shared_body():
    out = _render("dropped_case_jump_98_2633.hasm", 2633)

    assert "if (27 === r9 || 5 === r9) {" in out
    assert "5 !== r9" not in out


def test_the_second_label_is_not_an_else_if():
    out = _render("dropped_case_jump_98_2628.hasm", 2628)

    assert "if (26 === r6 || 27 === r6) {" in out
    assert "27 !== r6" not in out
