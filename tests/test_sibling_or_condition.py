"""A test in the else arm that jumps to the entry of the then arm is an `||` of the `if` (F-185).

    if (A) { X } else { if (C) goto X; REST }          ->   if (A || C) { X } else { REST }

The residual test is the FIRST thing of the else arm, nothing that prints stands in front of it, and its target is
the entry of the then arm: `C` is only read when `A` failed, and both lead to `X`. The fold used to leave the jump
(`_sits_in_sibling_arm`: it must stay when the target is in the sibling arm), which printed `goto label_75`.

Not for a test behind a statement (96/12298 `populateParams`: `r2 = r1.length` stands in front of `r2 === 0`; moving
the test up read `r2` before it was set) and not for a `case` chain (98/2541: the tests of one `revealOrder` keep
being joined by `restore_dropped_case_jumps`).

    98/7633  `resolveTransition`   98/3265 `dispatchEvent`   98/2541 `findFirstSuspended`
"""

from pathlib import Path

from hermes_decompiler.Decompiler import Decompiler

_DATA = Path(__file__).parent / "data"


def _render(name: str, function_id: int) -> str:
    hasm = (_DATA / name).read_text(encoding="utf-8")
    out = Decompiler.render(Decompiler.build_context(hasm, function_id, strict=False), verbose=False, raw=False)

    return "\n".join(line for line in out.split("\n") if not line.strip().startswith("//"))


def test_the_second_test_joins_the_condition_of_the_arm_it_jumps_to():
    out = _render("sibling_or_condition_98_7633.hasm", 7633)

    assert "goto" not in out
    assert '} else if (param1 || typeof param2 !== "number") {' in out
    assert out.count("Prop \\\"fadeDuration\\\" is deprecated") == 1


def test_a_type_check_after_a_null_check_is_one_condition():
    out = _render("sibling_or_condition_98_3265.hasm", 3265)

    # The rest of the function left a `goto` once, so the first attempt (with the `||`) was kept. F-218 lets the
    # last rung copy a longer tail that a fall-through enters too; the whole function is `goto`-free at that rung,
    # and the shared `throw` is written once per test instead of once for the `||`.
    assert "goto" not in out
    assert 'if (param1 == null) {\n        throw new TypeError(' in out
    assert '} else if (typeof param1.type !== "string") {' in out


def test_a_case_chain_is_not_taken_by_the_fold():
    out = _render("sibling_or_condition_98_2541.hasm", 2541)

    assert "goto" not in out
    assert '"unstable_legacy-backwards" === r7 || "together" === r7' in out
