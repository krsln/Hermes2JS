"""`if` arms: jumps into and out of arms, joins, tails, layouts.

Merged from: test_arm_falls_into_returning_region, test_arm_finish_join, test_arm_guard_constant_test, test_arm_join_after_throw, test_arm_join_tail, test_arm_jumps_into_join, test_arm_private_exits, test_arm_private_return, test_arm_runs_into_shared_return, test_arm_runs_into_tail, test_arm_throw_then_body, test_else_if_prefix, test_empty_if_arm, test_empty_value_is_an_expression, test_fall_through_layout, test_forward_jumps_print_as_labeled_blocks, test_if_arm_jump_to_following_if_with_a_synthetic_block, test_if_arm_jump_to_join, test_jump_into_the_middle_of_an_arm, test_jump_onto_an_arm_of_a_later_if.
"""

from __future__ import annotations

import re
import shutil
import subprocess
from pathlib import Path
from test_register_semantics import decompile
from types import SimpleNamespace

import pytest

from hermes_decompiler.Decompiler import Decompiler
from hermes_decompiler.backend.analysis.cfg import BasicBlock
from hermes_decompiler.backend.emit.printer._labeled_exits import LabeledExitPlan
from hermes_decompiler.backend.regions import IfRegion, SequenceRegion
from hermes_decompiler.backend.transforms.shared import prints_non_constant_statement
from hermes_decompiler.frontend.batch_pipeline import BatchContext, BatchPipeline
from hermes_decompiler.frontend.batch_pipeline.stages import (
    ClassEnvironmentTableStage,
    CreatorTableStage,
    EnvironmentOriginTableStage,
    PrivateNameTableStage,
)
from hermes_decompiler.ir.expressions import Identifier, Literal, MemberExpression, NumericLiteral
from hermes_decompiler.ir.terminators import TerminatorJump


# ----------------------------------------------------------------------------------------------------
# arm_falls_into_returning_region
#
# An arm that falls into the code a test before it skips to, after a test whose taken side is code of its own
# (F-222, 98/10919 `onAction`).
#
#     if (a) goto ARM; <mid>; if (r !== null) goto REST; ARM: <code>; return; REST: <rest of the function>; return
#
# `ARM` is entered from the first test and from the end of `<mid>`; `REST` is a whole region that only the second
# test reaches and that ends in `return`s. Only a lone `return` counted as such a taken side, so `ARM` stayed the
# `then` arm of the first test and the second test printed `if (r !== null) goto L` into `REST`.
# ----------------------------------------------------------------------------------------------------

_DATA = Path(__file__).parent / "data"


def test_the_arm_follows_the_if_that_runs_into_it():
    hasm = (_DATA / "arm_falls_into_returning_region_98_10919.hasm").read_text(encoding="utf-8")
    out = Decompiler.render(Decompiler.build_context(hasm, 10919, strict=False), verbose=False, raw=False)
    code = "\n".join(line for line in out.split("\n") if not line.strip().startswith("//"))

    assert "goto" not in code
    assert 'if (typeof param1.target !== "string" || param1.target === r7.key) {' in code
    assert "if (r8 !== null) {\n                r5 = r7 === r8;" in code


# ----------------------------------------------------------------------------------------------------
# arm_finish_join
#
# `if (c) goto T; REST` at the end of an arm, T what runs when the arm is done (F-199, now solved).
#
#     switch/if chain arm:   if (x === ",") { if (depth !== 0) goto T; push(...); jmp UPDATE }     T: cur = cur + x; UPDATE: ...
#
# T is no sibling of the arm's sequence (it follows the enclosing `if`s), so `_DominanceIfBuilder._convert` found no
# `else` and gave up (`if (r2 !== 0) goto label_122`). Finishing the arm runs T anyway, so the branch only skips REST:
# `if (r2 === 0) { REST }`. Not when REST itself jumps to T (those jumps stay `goto`s next to the `if`).
#
#     98/2186 `splitGradients`   96/9575 `splitByComma`
# ----------------------------------------------------------------------------------------------------

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


# ----------------------------------------------------------------------------------------------------
# arm_guard_constant_test
#
# An arm that leaves only through `return`s of its own and falls into the code its (constant) test skips to
# (F-220, 98/13851: the second iterator element).
#
#     if (r6 === undefined) { if (!x) return null; ...; if (optional) return null; }  <code both paths run>
#
# The test compares with `undefined`, which the arm-falls-into rule left to chains of case tests, so the code after
# the arm was printed as the `then` arm and the arm's last test became `if (r5) goto L; return null;`.
# ----------------------------------------------------------------------------------------------------

def test_the_code_after_the_arm_follows_the_if():
    hasm = (_DATA / "arm_guard_constant_test_98_13851.hasm").read_text(encoding="utf-8")
    out = Decompiler.render(Decompiler.build_context(hasm, 13851, strict=False), verbose=False, raw=False)
    code = "\n".join(line for line in out.split("\n") if not line.strip().startswith("//"))

    assert "goto" not in code
    assert "if (r6 === undefined) {" in code
    assert "if (r5) {\n                return null;\n            }" in code
    assert code.rindex("r4 = r4[0];") > code.index("if (r5) {")


# ----------------------------------------------------------------------------------------------------
# arm_join_after_throw
#
# Both arms of a test run on into one block although an arm also leaves through a `throw` (F-223, 98/8536
# `normalizeCSSTransitionProperties`).
#
#     if (a.length) { ...; if (some) throw ...; r12 = !r6 } else { r12 = values.some(f) }  if (r12) { ... }
#
# The post-dominator of the test is empty because of the `throw`, so the `else` arm ended in a `goto` to the `if (r12)`
# that follows the `if`. The block whose immediate dominator is the test and that both arms enter is the merge.
# ----------------------------------------------------------------------------------------------------

def test_the_join_after_a_throwing_arm_follows_the_if():
    hasm = (_DATA / "arm_join_after_throw_98_8536.hasm").read_text(encoding="utf-8")
    out = Decompiler.render(Decompiler.build_context(hasm, 8536, strict=False), verbose=False, raw=False)
    code = "\n".join(line for line in out.split("\n") if not line.strip().startswith("//"))

    assert "goto" not in code
    assert "r12 = r16.some(function_12106);\n    }\n    if (r12) {" in code


# ----------------------------------------------------------------------------------------------------
# arm_join_tail
#
# F-126: an `if` arm whose own test jumps to the code the outer branch skips to.
#
#     96/1333 `getValidLengthPercentageSizeOrNull`: the `"px"` arm falls through to the `"%"`
#     check when its number is invalid. The `"%"` check used to be printed inside the other
#     arm, so an invalid `"px"` value returned `undefined` instead of reaching `return null`.
# ----------------------------------------------------------------------------------------------------

def test_the_skipped_to_code_follows_the_if_instead_of_sitting_in_one_arm():
    hasm = (_DATA / "arm_test_joins_tail_96_1333.hasm").read_text(encoding="utf-8")
    out = Decompiler.render(Decompiler.build_context(hasm, 1333, strict=False), verbose=False, raw=False)

    assert "goto" not in out
    assert 'if (r2) {' in out
    # the "%" test is reached after the "px" arm, not only when "px" failed
    assert out.index('endsWith("%")') > out.index("return r2;")
    assert out.count("return null;") == 2


def test_an_arm_that_runs_on_into_a_shared_return_does_not_lose_it():
    """96/852 `_wrapNativeSuper`: `if (map.has(x)) return map.get(x); map.set(x, Wrapper);`
    runs on into the same `return` the `undefined === r5` test jumps to. That `return` was
    printed inside the other arm only, so after `map.set(...)` the function returned nothing."""
    hasm = (_DATA / "arm_falls_into_shared_return_96_852.hasm").read_text(encoding="utf-8")
    out = Decompiler.render(Decompiler.build_context(hasm, 852, strict=False), verbose=False, raw=False)

    assert "goto" not in out
    assert out.count("Wrapper.prototype = r5;") == 1
    assert out.index("r5 = r2.set(param1, Wrapper);") < out.index("Wrapper.prototype = r5;")


def test_an_arm_that_runs_on_into_a_long_shared_body_does_not_lose_it():
    """96/269: `if (signal !== undefined) { ...; if (aborted) return; signal.addEventListener(...) }`
    runs on into the very code the `undefined === signal` test jumps to (the whole pipe setup).
    That code was printed inside the other arm only, so with a signal the function stopped after
    `addEventListener` and never piped anything."""
    hasm = (_DATA / "arm_runs_into_shared_body_96_269.hasm").read_text(encoding="utf-8")
    out = Decompiler.render(Decompiler.build_context(hasm, 269, strict=False), verbose=False, raw=False)

    assert "goto" not in out
    assert out.count("r7 = P(r5, r4._closedPromise, function_285);") == 1
    assert out.index('addEventListener("abort", no)') < out.index("function_285")


# ----------------------------------------------------------------------------------------------------
# arm_jumps_into_join
#
# An arm whose last block jumps over what follows it still runs into the join (F-187).
#
#     if (!(a instanceof B)) { if (T) { return 0 } else { X; jmp J } }  J: ...
#
# The join `J` is reached by a `JmpTrue` (the `instanceof` test) and by the last block of the arm, which ends in a
# `Jmp` to it (not a fall-through). `_arm_runs_into` only counted fall-throughs, so the join was printed inside the
# `instanceof` arm and the other arm got a `goto`.
#
#     98/8188 `compare` (semver)
# ----------------------------------------------------------------------------------------------------

def test_the_arm_that_jumps_to_the_join_does_not_leave_a_goto():
    out = _render("arm_jumps_into_join_98_8188.hasm", 8188)

    assert "goto" not in out
    assert "r5 = new r4(r13, this.options);" in out
    assert out.index("r5 = new r4(r13, this.options);") < out.index("r4 = r5.version;")


# ----------------------------------------------------------------------------------------------------
# arm_private_exits
#
# An arm with SEVERAL private exits whose last test falls into the branch target (F-211, 96/13262
# `shouldUseHorizontalLabels`).
#
#     if (pos) { if (pos === "beside-icon") return true; if (pos === "below-icon") return false; }  <width logic>
#
# `_returns_privately` refused an arm with a second exit, so the width logic was printed as the `then` arm and the
# arm's last test as `if ("below-icon" === r4) goto L; r0 = false`. A further exit that is a `return` of its own
# is fine now, and `IfTailMergeRegionPass` keeps a `return` a pending test still jumps to (96/4144 `parseScheme`,
# `tests/test_arm_private_return.py`, lost its `return 0` with the first change alone).
# ----------------------------------------------------------------------------------------------------

def test_the_width_logic_follows_the_position_checks():
    hasm = (_DATA / "arm_private_exits_96_13262.hasm").read_text(encoding="utf-8")
    out = Decompiler.render(Decompiler.build_context(hasm, 13262, strict=False), verbose=False, raw=False)
    code = "\n".join(line for line in out.split("\n") if not line.strip().startswith("//"))

    assert "goto" not in code
    assert 'if ("below-icon" === r4) {\n            return false;\n        }\n    }\n    r4 = r0.width;' in code


# ----------------------------------------------------------------------------------------------------
# arm_private_return
#
# An arm whose only way out is a private `return`, tested past its first block (F-170).
#
#     if (a) { x = f(); if (x != null) return x.v; }  T: ...        a jumps to T
#
# The arm's test (`x?.key != null` is three blocks) falls into the branch target; its exit is a `return` nothing else
# reaches. The first attempt had no `if` for that: it printed `if (r2 != null) goto label_87; return param1.key;`,
# which returned the key on the path where it is `null`. Now the target follows the `if` and `GuardExitRegionPass`
# may fall on into an `if` whose test block its condition swallowed, so the `return` moves into the guard.
#
# An arm with more exits (96/4144: three returns) keeps the old route, which copies the returns.
#
#     96/5301  `keyExtractor`
#     96/5     `metroImportDefault`
#     96/4144  `parseScheme`  (must keep `return 0`)
# ----------------------------------------------------------------------------------------------------

def test_the_key_is_returned_only_when_it_is_not_null():
    out = _render("arm_private_return_96_5301.hasm", 5301)

    assert "goto" not in out
    assert "if (r2 != null) {\n            return param1.key;\n        }" in out
    assert out.count("return param1.key;") == 1
    assert out.index("return param1.key;") < out.index("r1 = param1.id;")


def test_a_cache_check_returns_inside_its_own_if():
    out = _render("arm_private_return_96_5.hasm", 5)

    assert "goto" not in out
    assert "if (r3 !== r1) {\n            r1 = r0[1];\n            r0 = r1.get(param1);\n            return r0.importedDefault;" in out


def test_an_arm_with_several_exits_keeps_its_returns():
    out = _render("arm_private_return_many_exits_96_4144.hasm", 4144)

    assert "if (r6 !== r4) {\n                return 0;\n            }" in out


# ----------------------------------------------------------------------------------------------------
# arm_runs_into_shared_return
#
# `updateSlot` (96/1925): `if (typeof x !== "object") goto RET; ...; <last else arm falls into RET>`
# with `RET: return null` placed after the arm. The shared `return null` became the *then* arm of
# the type test and the last `else` ended without it (the function returned undefined there).
# ----------------------------------------------------------------------------------------------------

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


# ----------------------------------------------------------------------------------------------------
# arm_runs_into_tail
#
# An arm that runs on into the branch target leaves the target AFTER the `if` (a retry with copied returns).
#
#     if (c) goto T;  <arm: ...; if (x) return ...; ...>  T: <tail>
#
# The first attempt took `T` for the `else` arm: the arm's own flow into it was dropped, or a `goto` stayed.
# With the shared returns copied, the arm's other exits are real `return`s, so `T` follows the `if`.
#
#     96/842    `handleException`: `if (handler) { if (handler(...)) return; }` then the rest.
#     96/10211  `isAnimationTerminatingCalculation`: the clamped branch returns `true` out of range and
#               otherwise runs on into the spring energy test.
#     96/11046  `areDependenciesEqual`: see `test_shared_return_widened.py` (the loop tail).
# ----------------------------------------------------------------------------------------------------

def test_the_code_after_an_early_return_arm_follows_the_if():
    out = _render("arm_runs_into_tail_96_842.hasm", 842)

    assert "goto" not in out
    assert out.count("try {") == 1
    # The early-return arm folds into the test: `if (!(handler && handler(...))) { <the rest> }`.
    assert "return undefined;" not in out
    assert "if (!(r7 && r3[0].RN$handleException(param1, param2, true))) {" in out


def test_a_clamped_branch_runs_on_into_the_energy_test():
    out = _render("arm_runs_into_tail_96_10211.hasm", 10211)

    assert "goto" not in out
    # both clamp tests leave for the same `return true`: one `||` (F-170), not two copies
    assert out.count("return true;") == 1
    assert "if (r0 < r5 || r0 > r4) {\n            return true;" in out
    assert out.index("return true;") < out.index("r4[0](")


def test_the_first_attempt_keeps_the_code_an_arm_falls_into():
    """96/890 `requireModule`: `if (a == null) goto T; r0 = f(); if (r0 != null) return r0; T: ...`.

    No return copies are needed: the arm's test leaves through a lone `return`, and its fall-through
    is the branch target, which therefore follows the `if` (it was dropped before)."""
    out = _render("arm_runs_into_tail_first_attempt_96_890.hasm", 890)

    assert "goto" not in out
    assert out.index("r1[2].call(") < out.index("r1[1][param1]")
    assert out.count("return r0;") == 1


def test_a_last_test_that_jumps_onto_the_tail_and_falls_into_a_return_leaves_the_tail_after_the_if():
    """96/8976 `processColorInitially`: `if (typeof p === "number") goto T; r = f(p); if (typeof r === "number")
    goto T; return r; T: <number code>; return`. The tail follows the `if` (it stayed a `goto`)."""
    out = _render("arm_tests_into_tail_past_return_96_8976.hasm", 8976)

    assert "goto" not in out
    assert out.count(">>> 0") == 1
    assert out.index("return r1;") < out.index(">>> 0")


# ----------------------------------------------------------------------------------------------------
# arm_throw_then_body
#
# An arm that throws unless its test jumps to the body the guard skips to (F-212, 98/9633 `Tr`).
#
#     if (signal !== undefined) { ...; if (!isAbortSignal(signal)) throw new TypeError(...); }  <build and return the object>
#
# The object-building body ends in a `return` of its own and is entered by the guard and by the arm's test. With no
# post-dominator, the body became the `then` arm of the guard and the arm's test a `goto` into it. The body follows
# the `if` now.
# ----------------------------------------------------------------------------------------------------

def test_the_body_follows_the_signal_check():
    hasm = (_DATA / "arm_throw_then_body_98_9633.hasm").read_text(encoding="utf-8")
    out = Decompiler.render(Decompiler.build_context(hasm, 9633, strict=False), verbose=False, raw=False)
    code = "\n".join(line for line in out.split("\n") if not line.strip().startswith("//"))

    assert "goto" not in code
    assert "if (undefined !== r5) {" in code
    assert code.count("return r4;") == 1


# ----------------------------------------------------------------------------------------------------
# else_if_prefix
#
# `else { <prefix>; if (c) {...} }` prints as a flat `else if (c)` only when the
# prefix is clutter. A prefix that DEFINES a register the nested condition reads
# (`r1 = param1.length`) must stay: dropping it leaves `else if (r1 === 1)` with
# no `r1`. Only constant loads (`r1 = 5`, the value is already embedded in the
# nested condition) may be looked past.
#
# Measured over the full hermes-96/98 bundles, this removes 79 of 261 (96) and
# 64 of 362 (98) dangling registers, with none introduced.
# ----------------------------------------------------------------------------------------------------

def _instruction(value, definition_used=False):
    return SimpleNamespace(value=value, definition_used=definition_used)


def test_non_constant_definition_is_a_printing_statement():
    member = MemberExpression(obj=Identifier(name="param1"), prop=Identifier(name="length"), computed=False)

    assert prints_non_constant_statement(_instruction(member))
    assert prints_non_constant_statement(_instruction(Identifier(name="r4")))


def test_constant_load_is_not():
    assert not prints_non_constant_statement(_instruction(NumericLiteral(value=5)))
    assert isinstance(NumericLiteral(value=5), Literal)


def test_folded_definition_prints_nothing():
    member = MemberExpression(obj=Identifier(name="param1"), prop=Identifier(name="length"), computed=False)

    assert not prints_non_constant_statement(_instruction(member, definition_used=True))
    assert not prints_non_constant_statement(_instruction(None))


def test_definition_read_by_the_nested_condition_is_kept():
    # `if (typeof s !== "string" || s.length !== 1) throw ...; return;` - the
    # second test is preceded by `r1 = param1.length`, a pure load both exits
    # overwrite, so it becomes part of ONE condition. (Kept as a nested
    # `else if` the throw was missing on the path where the length is not 1.)
    hasm = (_DATA / "else_if_prefix_definition.hasm").read_text(encoding="utf-8")
    out = Decompiler.render(Decompiler.build_context(hasm, 7547), verbose=False)
    out = "\n".join(line for line in out.split("\n") if not line.strip().startswith("//"))

    assert 'r2 !== "string" || param1.length !== 1' in out
    assert "else if (r1 === 1)" not in out
    assert out.count("throw") == 1


def test_generator_state_is_loaded_before_the_state_check():
    # The `catch` state check used to read r12 with its load gone (`else if (r12 === 3)` with no `r12 = r1[0]`).
    # 98/12484 folds into a `try` now (F-12 re-entry threading): the state is loaded right before the check.
    out = decompile("98", 12484)

    assert "r12 = r1[3];" in out
    assert "else if (r12" not in out
    assert out.index("r12 = r1[3];") < out.index("if (0 === r12)")


# ----------------------------------------------------------------------------------------------------
# empty_if_arm
#
# `if` arms that print nothing are removed (`EmptyIfArmRegionPass`).
#
# Structuring leaves an arm behind when a branch only skips code the earlier passes folded or dropped:
#
# - `if (c) { } else { X }` becomes `if (!c) { X }`    (98/1957 `setEventInitTimeStamp`)
# - `if (c) { X } else { }` becomes `if (c) { X }`     (96/8802 `timeoutCallback`)
# - `if (c) { }` is dropped when `c` cannot run anything (96/4724 `shouldUseTurboAnimatedModule`: both
#   branches `Ret r0`)
#
# An arm counts as empty the way `RegionPrinter._emit_block` decides it: a definition no reader folded
# away is a line of output, so an arm that holds one is kept.
# ----------------------------------------------------------------------------------------------------

def _code(name: str, function_id: int) -> str:
    hasm = (_DATA / name).read_text(encoding="utf-8")

    return Decompiler.render(Decompiler.build_context(hasm, function_id, strict=False), verbose=False, raw=False)


def test_an_empty_then_arm_turns_the_test_around():
    code = _code("empty_arm_inverted_98_1957.hasm", 1957)

    assert 'if (typeof param2 === "number") {' in code
    assert "else" not in code
    assert 'typeof param2 !== "number"' not in code


def test_an_empty_else_arm_is_dropped():
    code = _code("empty_else_96_8802.hasm", 8802)

    assert "if (r0) {" in code
    assert "else" not in code


def test_a_test_without_effect_and_without_arms_is_dropped():
    code = _code("empty_lone_if_96_4724.hasm", 4724)

    assert "if (" not in code
    assert "return false;" in code


# ----------------------------------------------------------------------------------------------------
# empty_value_is_an_expression
#
# Hermes' `empty` value (the uninitialized `this` of a derived constructor) prints as an expression (98/4214 `FlatList`).
#
# `LoadConstEmpty` printed a bare comment, so `__environment__[0] = /* empty */;` and `__throwIfThisInitialized__(/* empty */)`
# did not parse. The marker stays visible: `undefined /* empty */`.
# ----------------------------------------------------------------------------------------------------

def _render_2() -> str:
    hasm = (_DATA / "empty_value_in_a_derived_constructor_98_4214.hasm").read_text(encoding="utf-8")

    return Decompiler.render(Decompiler.build_context(hasm, 0, strict=False), verbose=False, raw=False)


def test_the_empty_marker_is_never_a_bare_comment():
    out = _render_2()

    assert "/* empty */" in out
    assert not re.search(r"(?<!undefined )/\* empty \*/", out)


def test_the_uninitialized_this_is_stored_and_checked_as_an_expression():
    out = _render_2()

    assert "__environment__[0] = undefined /* empty */;" in out
    assert "__throwIfThisInitialized__(undefined /* empty */);" in out


# ----------------------------------------------------------------------------------------------------
# fall_through_layout
#
# A branch's fall-through stays right behind it, and a long `return` tail is copied (F-12, 98/12903).
#
#     if (r8) goto AWAIT;                  // falls into T (the layout put T last: the topological order of the
#     T: requestPermission(...); return    //   generator dispatch)
#     AWAIT: await ...;  if (!c) goto T;
#
# `GeneratorStateDispatchCfgPass` orders the blocks by address under the topological order, so `T` (entered by
# two resume tests as well) came after all of them. The output printed `if (r8) goto label_325;` and then the
# await: the code for `!r8` was not behind the branch (wrong, not just a `goto`). On the last rungs the two
# resume tests get their own copy of `T` (ten instructions; the limit was nine) and `FallThroughLayoutCfgPass`
# moves the original behind the branch.
# ----------------------------------------------------------------------------------------------------

def _render_3() -> str:
    sections = [
        (10465, (_DATA / "generator_tail_layout_98_10465_creator.hasm").read_text(encoding="utf-8")),
        (12903, (_DATA / "generator_tail_layout_98_12903.hasm").read_text(encoding="utf-8")),
    ]
    tables = BatchPipeline([
        CreatorTableStage(), EnvironmentOriginTableStage(), PrivateNameTableStage(), ClassEnvironmentTableStage(),
    ]).run(BatchContext(sections=sections)).to_batch_tables()
    out = Decompiler.render(
        Decompiler.build_context(sections[1][1], 12903, batch_tables=tables), verbose=False,
    )

    return "\n".join(line for line in out.split("\n") if not line.strip().startswith("//"))


def test_the_test_of_r8_owns_both_arms():
    code = _render_3()

    assert "goto" not in code
    assert "if (r8) {\n        r7 = r7[1];" in code
    assert "} else {\n        r8 = r1[2][0];" in code or "} else {\n        r10 = r1[3][1];" in code


def test_every_exit_calls_request_permission():
    # the `!r8` path and the two failed resume tests all reach `requestPermission`
    assert _render_3().count("requestPermission(") == 3


# ----------------------------------------------------------------------------------------------------
# forward_jumps_print_as_labeled_blocks
#
# A forward jump no structurer could express prints as a labeled block with `break label_N;` (F-301).
#
# 98/10832: four tests in the arms of one `if` skip to the code behind it (`r6 = undefined; if (!r9[4]) ...`). Copying
# that code into every arm is not an option and `if`/`else` has no form for it, but JavaScript has: `label_276: { ... }`
# around the arm and `break label_276;` for the jump. It is the last resort of `generate_js`: only an attempt that still
# has a `goto` after every rung is printed this way.
# ----------------------------------------------------------------------------------------------------

def _render_4() -> str:
    hasm = (_DATA / "forward_jumps_out_of_nested_arms_98_10832.hasm").read_text(encoding="utf-8")

    return Decompiler.render(Decompiler.build_context(hasm, 0, strict=False), verbose=False, raw=False)


def test_the_jumps_become_labeled_breaks_and_no_goto_is_left():
    out = _render_4()

    assert "goto" not in out
    assert "NOT valid JavaScript" not in out
    assert "    label_276: {\n" in out
    assert "break label_276;" in out


def test_the_code_the_jumps_skip_to_follows_the_labeled_block():
    out = _render_4()
    block = out.split("label_276: {\n")[1]
    # the block is closed at the indentation of its label, and the skipped-to code comes right behind it
    closing = block.index("\n        }\n")

    assert block[closing + len("\n        }\n"):].lstrip().startswith("r6 = undefined;")


def test_blocks_that_only_overlap_in_part_are_nested():
    ranges = [[0, 2, "label_a", []], [1, 4, "label_b", []]]

    LabeledExitPlan._nest(ranges)

    assert ranges[1][:2] == [0, 4]
    assert ranges[0][:2] == [0, 2]


def test_a_jump_to_the_test_of_a_later_if_lands_in_front_of_that_if():
    # 98/5415 `getPatternParts`: the `default:` arm of a `switch` jumps to the test block of the `if (r27)` behind it,
    # which is not printed as a block of its own: the `if` itself is the later sibling the label closes in front of.
    hasm = (_DATA / "labeled_break_to_an_if_test_98_5415.hasm").read_text(encoding="utf-8")
    out = Decompiler.render(Decompiler.build_context(hasm, 0, strict=False), verbose=False, raw=False)

    assert "goto" not in out
    assert "if (r30) break label_737;" in out
    assert out.index("label_737: {") < out.index("switch (r31)")
    assert out.index("if (r27) {") > out.index("break label_737;")


# ----------------------------------------------------------------------------------------------------
# if_arm_jump_to_following_if_with_a_synthetic_block
#
# A jump at the end of an `if` arm to the `if` that follows stays a `goto` when that `if` holds a synthetic block (F-263 sampling, 96/2075).
#
# `updateSuspenseListComponent`: `if (13 === t) {...} else if (19 === t) { schedule(...); goto TAIL } else { ... continue }` followed by
# `if (r13 !== param2) {...}` (TAIL is its test block). `RedundantJumpRegionPass._leading_address` finds where an `if` begins from the
# lowest address among its blocks, and one of them was a `break` block made by a structurer (address -1): nothing lies below -1, so no
# address came back and the arm's jump to the following `if` was never recognised as redundant.
# ----------------------------------------------------------------------------------------------------

def test_the_jump_to_the_following_if_is_dropped():
    hasm = (_DATA / "if_arm_jump_to_next_if_with_synthetic_block_96_2075.hasm").read_text(encoding="utf-8")
    out = Decompiler.render(Decompiler.build_context(hasm, 2075, strict=False), verbose=False, raw=False)

    assert "goto label_" not in out


# ----------------------------------------------------------------------------------------------------
# if_arm_jump_to_join
#
# An `if` arm's trailing jump to the code that follows the whole `if` is dropped (F-163).
#
#     if (a) { ... } else if (b) { ...; goto J } else { ...; return }  J: <join>
#
# The inner `if` has no merge of its own (its `else` returns), so its first arm kept the jump to the outer join.
# Falling off the end of the arm reaches the same place.
#
#     96/3847  `setStyleAttributePreprocessor`
# ----------------------------------------------------------------------------------------------------

def test_the_arm_falls_through_to_the_join_without_a_goto():
    hasm = (_DATA / "if_arm_jump_to_join_96_3847.hasm").read_text(encoding="utf-8")
    out = Decompiler.render(Decompiler.build_context(hasm, 3847, strict=False), verbose=False, raw=False)
    out = "\n".join(line for line in out.split("\n") if not line.strip().startswith("//"))

    assert "goto" not in out
    assert out.count('r1["process"] = param2;') == 1
    assert out.rstrip().endswith("r0 = r0[0];\n    r0[param1] = r1;\n}")


# ----------------------------------------------------------------------------------------------------
# jump_into_the_middle_of_an_arm
#
# A jump that lands in the MIDDLE of the other arm of an `if`, or in the middle of an arm of a later `if` that has no
# `else`, prints as labeled blocks (F-322, 98/3523 `parseURL`: a URL-state machine whose `goto`s were left after every
# rung). The tests build the region trees by hand, the real function takes over a minute to render.
# ----------------------------------------------------------------------------------------------------

def _block(block_id: int, address: int, jumps_to: int | None = None) -> BasicBlock:
    block = BasicBlock(block_id, address)
    terminator = TerminatorJump(jumps_to) if jumps_to is not None else None
    block.instructions = [SimpleNamespace(statement=None, terminator=terminator)] if terminator else []

    return block


def _sequence(*children) -> SequenceRegion:
    sequence = SequenceRegion()

    for child in children:
        sequence.append(child)

    return sequence


def test_a_jump_into_the_middle_of_the_other_arm_is_a_labeled_break():
    # if (c) { A; B; C } else { goto C }   -- the `else` arm lands on C, the third block of the `then` arm
    jump = _block(3, 30, jumps_to=12)
    region = IfRegion()
    region.then_body = _sequence(_block(0, 10), _block(1, 11), _block(2, 12))
    region.else_body = _sequence(jump)

    root = _sequence(region)
    plan = LabeledExitPlan.build(root)

    assert plan.breaks[id(jump.instructions[0].terminator)] == "label_12"
    assert plan.crossed[id(region)][1:3] == ("label_12", "label_12_end")
    assert plan.crossed_at[id(region)] == 2
    # the two blocks in front of the landing are inside the labeled block, which the arm's sequence closes
    assert plan.closes[(id(region.then_body), 1)] == 1


def test_a_jump_into_the_middle_of_a_later_if_without_else_is_a_labeled_break():
    # goto C; ...; if (c) { A; B; C }   -- the code in front of the `if` jumps over its test onto C
    jump = _block(0, 5, jumps_to=22)
    region = IfRegion()
    region.then_body = _sequence(_block(1, 20), _block(2, 21), _block(3, 22))
    region.else_body = None

    root = _sequence(jump, region)
    plan = LabeledExitPlan.build(root)

    assert plan.breaks[id(jump.instructions[0].terminator)] == "label_22"
    assert plan.crossed[id(region)] == (False, "label_22", "label_22_end", True)
    assert plan.crossed_at[id(region)] == 2
    assert plan.opens[(id(root), 0)] == ["label_22_end", "label_22"]


# ----------------------------------------------------------------------------------------------------
# jump_onto_an_arm_of_a_later_if
#
# A jump that lands on the first block of one ARM of a later sibling `if` prints as a labeled block (F-314, 96/2141).
#
#     if (26 === tag) { ... } else if (5 !== tag && 27 !== tag) goto A;   // A: the arm of the `if (r16)` below
#     ...
#     if (r16) { ... } else { A: ... }
#
# The code that jumps and the test of the `if` go into `label_A: { ... }`, the other arm leaves the whole by
# `break label_A_end;`. A jump out of a loop from inside a `switch` (`goto 718`) is the plain sibling case.
# Without the split the function kept one `goto`.
# ----------------------------------------------------------------------------------------------------

def _render_5() -> str:
    hasm = (_DATA / "jump_onto_an_arm_of_a_later_if_96_2141.hasm").read_text(encoding="utf-8")

    return Decompiler.render(Decompiler.build_context(hasm, 2141, strict=False), verbose=False, raw=False)


def test_the_jump_onto_the_arm_of_a_later_if_is_a_labeled_break():
    out = _render_5()

    assert "goto label_" not in out
    assert "label_413_end: {" in out
    assert "break label_413;" in out
    assert "break label_413_end;" in out
    assert out.count("break label_718;") == 3


@pytest.mark.skipif(shutil.which("node") is None, reason="node is not installed")
def test_the_labeled_output_parses(tmp_path: Path):
    path = tmp_path / "out.js"
    path.write_text(_render_5(), encoding="utf-8")

    done = subprocess.run(["node", "--check", str(path)], capture_output=True, text=True)

    assert done.returncode == 0, done.stderr
