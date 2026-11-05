"""`if (c) goto T; REST` at the end of an arm, T what runs when the arm is done (F-199, now solved).

    switch/if chain arm:   if (x === ",") { if (depth !== 0) goto T; push(...); jmp UPDATE }     T: cur = cur + x; UPDATE: ...

T is no sibling of the arm's sequence (it follows the enclosing `if`s), so `_DominanceIfBuilder._convert` found no
`else` and gave up (`if (r2 !== 0) goto label_122`). Finishing the arm runs T anyway, so the branch only skips REST:
`if (r2 === 0) { REST }`. Not when REST itself jumps to T (those jumps stay `goto`s next to the `if`).

    98/2186 `splitGradients`   96/9575 `splitByComma`
"""

from pathlib import Path

from hermes_decompiler.Decompiler import Decompiler

_DATA = Path(__file__).parent / "data"


def _render(name: str, function_id: int) -> str:
    hasm = (_DATA / name).read_text(encoding="utf-8")
    out = Decompiler.render(Decompiler.build_context(hasm, function_id, strict=False), verbose=False, raw=False)

    return "\n".join(line for line in out.split("\n") if not line.strip().startswith("//"))


def test_a_guard_that_skips_the_rest_of_an_arm_is_an_if():
    out = _render("arm_finish_join_98_2186.hasm", 2186)

    assert "goto" not in out
    assert "if (r2 === 0) {" in out


def test_the_same_shape_in_96_has_no_goto():
    out = _render("arm_finish_join_96_9575.hasm", 9575)

    assert "goto" not in out
