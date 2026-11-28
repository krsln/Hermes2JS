"""Guard exits and guards folded into conditions.

Merged from: test_guard_exit_loop_tail, test_guard_exit_orphan, test_guard_exit_region, test_guard_exit_same_sequence, test_guard_into_condition, test_guard_throw_arm.
"""

from pathlib import Path

from hermes_decompiler.Decompiler import Decompiler


# ----------------------------------------------------------------------------------------------------
# guard_exit_loop_tail
#
# The tail a `for-of` body jumps to when it finds its item becomes the body of the `if` (F-202).
#
#     for (x of xs) { if (a) continue; else { ...; if (found) goto TAIL } }   TAIL: ...; return r;   return undefined
#
# `GuardExitRegionPass._try_region_exit` moves such a tail into the guard, but only when the guard's other edge is
# "the next thing that runs". Here that edge enters a bare `continue` block of the other arm (the guard ends an `else`
# arm that ends the loop body), and the function's own last `return` (the loop's natural exit) is entered by another
# path than the guard's. Both now qualify; the natural exit stays where it is.
#
#     98/5429 `findInitialRoute`; 98/11278 (no loop: only the function's own last `return` stays out of the tail)
# ----------------------------------------------------------------------------------------------------

_DATA = Path(__file__).parent / "data"


def _render(name: str, function_id: int) -> str:
    hasm = (_DATA / name).read_text(encoding="utf-8")
    out = Decompiler.render(Decompiler.build_context(hasm, function_id, strict=False), verbose=False, raw=False)

    return "\n".join(line for line in out.split("\n") if not line.strip().startswith("//"))


def test_the_found_tail_of_a_for_of_is_the_body_of_its_if():
    out = _render("guard_exit_loop_tail_98_5429.hasm", 5429)

    assert "goto" not in out
    assert "if (r10) {\n                r1 = r3;" in out
    assert out.rstrip().endswith("}\n        }\n    }\n}")


def test_a_second_function_of_the_shape_has_no_goto():
    out = _render("guard_exit_loop_tail_98_11278.hasm", 11278)

    assert "goto" not in out


# ----------------------------------------------------------------------------------------------------
# guard_exit_orphan
#
# A guard whose exit block no sequence holds still becomes `if (c) { return }` (F-197).
#
#     if (r3) goto L;  ...  L: return undefined      (L has one way in; an earlier pass took it out of the tree)
#
# `GuardExitRegionPass` only moved an exit block that a sequence held. A bare `return undefined` no sequence held
# was left as `if (r3) goto label_213` (98/8283 `_handleAnimatedStylesUpdate`). Such a block is the guard's exit
# all the same: it is added to the then-body, nothing else prints it.
# ----------------------------------------------------------------------------------------------------

def test_a_guard_with_an_orphan_return_exit_has_no_goto():
    out = _render("guard_exit_orphan_98_8283.hasm", 8283)

    assert "goto" not in out
    # The guard's test and the call behind it are one condition (a function with a `for-of` handler no longer
    # keeps the fold off): the call still runs only after `r3` held.
    assert "if (r3 && isStyleAttached.call(0, param1[0])) {\n            return undefined;\n        } else {" in out


# ----------------------------------------------------------------------------------------------------
# guard_exit_region
#
# F-10 (non-return targets): `if (a) { ...; if (c) return x; } TAIL`, with the exit laid out after TAIL.
#
#     98/3552  `canParse`: when a base is given it is parsed first and `null == base` returns false;
#              both paths then run the same code that parses the url. The exit block lies after that
#              shared code, so the guard stayed `if (null == r5) goto label` and the tail was
#              duplicated into an else arm that dropped the fall-through.
# ----------------------------------------------------------------------------------------------------

def test_a_guard_whose_exit_follows_the_shared_tail_returns_inside_the_if():
    hasm = (_DATA / "guard_exit_after_tail_98_3552.hasm").read_text(encoding="utf-8")
    out = Decompiler.render(Decompiler.build_context(hasm, 3552, strict=False), verbose=False, raw=False)

    assert "goto" not in out
    assert "if (null == r5) {\n            return false;\n        }" in out
    # the url is parsed once, after the guard, for both paths
    assert out.count("r3[22](") == 2
    assert "} else {" not in out


def test_a_loops_exit_to_a_shared_return_is_not_absorbed_into_a_guarded_body():
    """98/8982 `checkEqual`: `do { r9 = it.next(); if (r9 === undefined) goto RETURN_TRUE; ...} while (r4)`.
    The residual branch was folded into `if (r9 !== undefined) { body }`, which dropped the exit:
    `return true` ended up after the loop where the walk never reaches it. The first attempt only
    looked fine because another goto in the function forced a retry that hid it."""
    hasm = (_DATA / "loop_exit_return_98_8982.hasm").read_text(encoding="utf-8")
    out = Decompiler.render(Decompiler.build_context(hasm, 8982, strict=False), verbose=False, raw=False)

    assert "goto" not in out
    assert "if (r9 !== undefined)" not in out
    # The loop's own exit is a `return false` inside it; the property list running out ends the
    # loop (`for ... in`), and `return true` follows it. Before the latch's terminal exit moved into
    # the loop (F-149), the `break` on `undefined` ran the code after the loop's own exit instead.
    assert "for (const r9 in r10) {" in out
    assert out.rstrip().endswith("return true;\n}")


def test_a_loop_break_to_a_function_ending_region_runs_that_region_inside_the_if():
    """96/2026 `refreshCache`: `for (n = fiber.return; n !== null; n = n.return) { if (tag === 24 || tag === 3) { ...; return } }`.

    The two tests jump out of the loop to the same code, which was printed after the loop's own
    `return undefined` (dead): a fiber with tag 24 never ran it, and tag 3 only by accident.
    The tests are one `||` condition and the code that follows ends the function, so it sits in the `if`.
    The loop counter register is reused for `getEnvironment(0)` inside it: it must keep its `rN` name.
    """
    hasm = (_DATA / "loop_two_exits_found_region_96_2026.hasm").read_text(encoding="utf-8")
    out = Decompiler.render(Decompiler.build_context(hasm, 2026, strict=False), verbose=False, raw=False)

    assert "goto" not in out
    assert "if (24 === r4 || 3 === r4) {\n            r3 = getEnvironment(0);" in out
    assert "r3[458].call(undefined, r6)" in out
    assert "i[458]" not in out
    assert out.index("r2.payload = r1;") < out.index("return undefined;")


# ----------------------------------------------------------------------------------------------------
# guard_exit_same_sequence
#
# `if (!c) goto T; BODY; T: tail` where BODY exits on every path and only this branch enters T (F-208,
# 98/12276 `validateType`).
#
# After the shared `throw` and the `Object.assign(...); return` were copied per jumper, the guard
# `if (!param1.extrapolateRight) goto T` still jumped to a tail in its own sequence, behind an if/else whose
# arms both exit. `GuardExitRegionPass` skipped every exit held by the guard's own sequence (the
# `IfStructurer`'s job) but that one never got built; with code between the two, the exit now moves into the `if`.
# ----------------------------------------------------------------------------------------------------

def _code() -> str:
    hasm = (_DATA / "guard_exit_same_sequence_98_12276.hasm").read_text(encoding="utf-8")

    return Decompiler.render(Decompiler.build_context(hasm, 12276, strict=False), verbose=False, raw=False)


def test_the_guard_takes_its_exit_into_the_if():
    code = _code()

    assert "goto" not in code
    assert "if (!param1.extrapolateRight) {\n                r5 = Object.assign(r2, param1);\n                return r2;\n            }" in code


# ----------------------------------------------------------------------------------------------------
# guard_into_condition
#
# `if (A) { if (B) goto NEXT; X }` NEXT: -> `if (A && !B) { X }` (96/1351 `processTransformOrigin`).
#
# `switch (key) { case "left": case "right": L ...; case "top": ...; }` inside a loop compiled to
# `if (key !== "left") { if (key === "right") goto L; <switch of the rest>; continue } L: ...`. The arm ends in a
# `continue`, so the structurer found no join for the guard and the shared label `L` stayed a raw `goto`. The last
# rung of the retry ladder folds a guard that is nothing but its test, first in the arm, into the arm's condition.
# ----------------------------------------------------------------------------------------------------

def _render_2(name, index):
    hasm = (_DATA / name).read_text(encoding="utf-8")

    return Decompiler.render(Decompiler.build_context(hasm, index, strict=False), verbose=False, raw=False)


def test_a_shared_label_guard_joins_the_condition():
    out = _render_2("guard_into_condition_96_1351.hasm", 1351)

    assert "goto label" not in out
    # Since F-293 the loop's `break`s are taken inside an `if` arm, so an earlier rung than the guard fold gets the
    # `switch` (`case "left": case "right":`) without a `goto`.
    assert 'case "left":\n                    case "right":' in out


# ----------------------------------------------------------------------------------------------------
# guard_throw_arm
#
# A guard that jumps past a `throw` inside an arm built a moment ago (F-182).
#
#     if (r2) { r9 = r2; if (typeof r9 === "function") goto T; throw ... }   T: if (r9) ...
#
# `if (r2)` came out of folding a residual test, and the `typeof` test inside its arm was never folded: it
# printed `if (typeof r2 === "function") goto label_200;`. The arm is folded now, but only when
#
#   - the jump's target is the code BEHIND the enclosing arms (`_target_follows_the_region`: not a `return`
#     printed elsewhere, 98/2202 `if (isNaN(x)) goto RETURN_UNDEFINED` inside an arm that goes on into a `switch`),
#   - the arm ends in a `throw`/`return` (nothing falls out of it), and
#   - nothing outside the arm jumps into it (98/2693: code behind a `throw` that other jumps reach),
#
# and never for a `case` test (98/2211: the chain `SwitchStructurer` reads). The fold stops at a target that sits
# later in the region (`if (C) goto T; A; T: B` is `if (!C) { A } B`).
#
#     98/2490  `accumulateDirectDispatchesSingle`   98/2202 `_getFilterAmount`
#     98/2211  `processTransformOrigin`            98/2693 `findHostInstance`
# ----------------------------------------------------------------------------------------------------

def test_the_type_check_guards_its_throw():
    out = _render("guard_throw_arm_98_2490.hasm", 2490)

    assert "goto" not in out
    assert 'if (typeof r2 !== "function") {\n' in out
    assert out.index('if (typeof r2 !== "function") {') < out.index("throw r2;")


def test_a_return_printed_elsewhere_is_not_where_the_arm_continues():
    out = _render("guard_throw_arm_98_2202.hasm", 2202)

    assert "if (!r5) {\n            return undefined;\n        }" in out
    assert "if (r7) {\n            return undefined;\n        }" in out


def test_a_case_test_keeps_its_chain():
    out = _render("guard_throw_arm_98_2211.hasm", 2211)

    assert '"left" !== r30 &&' not in out
    assert 'case "left":\n                    case "right":' in out


def test_code_other_jumps_reach_stays_behind_the_throw_guard():
    out = _render("guard_throw_arm_98_2693.hasm", 2693)

    assert "throw r19;\n                    r15" not in out
