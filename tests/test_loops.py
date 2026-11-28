"""Loops: conditions, latches, exits, carried definitions, rewritten parameters and counters.

Merged from: test_bare_break_shadow, test_class_table_register_overwritten, test_conditional_continue, test_conditional_continue_latch, test_conditional_continue_while_true, test_continue_to_a_second_back_edge_stub, test_get_by_val_key_redefines_object, test_inner_loop_register_tested_by_the_outer_loop, test_loop_advance_kept_with_the_folded_test, test_loop_alias_symbolic_copy, test_loop_around_a_try_that_leaves_by_a_jump, test_loop_body_short_circuit, test_loop_break_forwarded_exit, test_loop_breaks_inside_if_arms_do_not_stop_the_if, test_loop_carried_definition, test_loop_condition_merge_analysis, test_loop_counter_rewritten_before_an_if_test, test_loop_exit_body_of_several_blocks, test_loop_exit_join, test_loop_exit_shared_return, test_loop_guard_initializer, test_loop_header_ordinary_if, test_loop_jumping_into_the_other_arm, test_loop_latch_terminal_exit, test_loop_sibling_exits, test_loop_update_alias_rewritten_on_exit_path, test_loop_with_the_latch_test_inside_an_if, test_param_copy_rewritten_in_loop, test_param_rewritten_in_loop, test_parameter_copy_rewritten_by_the_loop.
"""

import re
import shutil
import subprocess
from pathlib import Path
from types import SimpleNamespace

import pytest

from hermes_decompiler.Decompiler import Decompiler
from hermes_decompiler.backend.analysis.cfg import BasicBlock
from hermes_decompiler.backend.regions import IfRegion, SequenceRegion
from hermes_decompiler.backend.transforms.region_passes.InductionVariableNamingPass import InductionVariableNamingPass
from hermes_decompiler.frontend.batch_pipeline import BatchContext, BatchPipeline
from hermes_decompiler.frontend.batch_pipeline.stages import (
    ClassEnvironmentTableStage,
    CreatorTableStage,
    EnvironmentOriginTableStage,
    PrivateNameTableStage,
)
from hermes_decompiler.ir.expressions import Identifier


# ----------------------------------------------------------------------------------------------------
# bare_break_shadow
#
# A jump to a loop block's address finds the block, not the bare `break` split off it (F-229, 98/14187).
#
#     do {
#         if (typeof cb !== "function") goto INC;  ...  if (cb == null) goto INC;  cb.call(...);
#         INC: r0 = r0 + 1; r4 = ...; if (!(r0 < r4)) break; ...
#     } while (...)
#
# `LoopBreakStructurer` (shape D) turns the block's own test into `if (c) { break; }` and gives the new block that
# block's address, so the address lookup of `_DominanceIfBuilder` found the `break` for the target `INC` of both
# guards: the join it saw was a block with no way in, and neither guard became an `if`. The lookup now prefers the
# real block.
# ----------------------------------------------------------------------------------------------------

_DATA = Path(__file__).parent / "data"


def test_the_two_guards_of_the_loop_body_nest():
    hasm = (_DATA / "bare_break_shadow_98_14187.hasm").read_text(encoding="utf-8")
    out = Decompiler.render(Decompiler.build_context(hasm, 14187, strict=False), verbose=False, raw=False)
    code = "\n".join(line for line in out.split("\n") if not line.strip().startswith("//"))

    assert "goto" not in code
    assert 'if (typeof r11 === "function") {' in code
    assert "if (r11 != null) {" in code


# ----------------------------------------------------------------------------------------------------
# class_table_register_overwritten
#
# A register that no longer holds the class factory does not name a slot (98/570, `downloadAsync` of expo-asset).
#
# `ClassEnvironmentTable` follows `CreateClosure r1, <helper>` -> `Call r1, r1` -> `StoreToEnvironment slot, r1`. It
# kept `r1` as the helper after `LoadParam r1` and `GetByIndex r1` had overwritten it, so the module's slot 0
# (`requireNativeModule("ExpoAsset")`) was named after the class `?anon_0_downloadAsync` and 98/12943 read
# `r7 = ?anon_0_downloadAsync; r7.downloadAsync(...)`: not valid JavaScript, and the wrong object.
# ----------------------------------------------------------------------------------------------------

def _render() -> str:
    sections = [
        (570, (_DATA / "native_module_slot_98_570.hasm").read_text(encoding="utf-8")),
        (5052, (_DATA / "native_module_slot_98_570_5052.hasm").read_text(encoding="utf-8")),
        (10540, (_DATA / "native_module_slot_98_570_10540.hasm").read_text(encoding="utf-8")),
        (12943, (_DATA / "native_module_slot_98_570_12943.hasm").read_text(encoding="utf-8")),
    ]
    tables = BatchPipeline([
        CreatorTableStage(), EnvironmentOriginTableStage(), PrivateNameTableStage(), ClassEnvironmentTableStage(),
    ]).run(BatchContext(sections=sections)).to_batch_tables()

    return Decompiler.render(Decompiler.build_context(sections[3][1], 12943, batch_tables=tables), verbose=False)


def test_the_native_module_is_not_named_after_a_class():
    out = _render()

    assert "?anon_" not in out
    assert "anon_0_downloadAsync;" not in out


def test_the_slot_is_read_from_the_environment():
    assert "r7 = r5[0];" in _render()


# ----------------------------------------------------------------------------------------------------
# conditional_continue
#
# `if (c) continue;` compiled as a conditional branch back to the loop (96/5924,
# an `assign`-like `for (k in src) { if (src[k] == null) continue; dst[k] = src[k]; }`):
#
#     JEqual r8, r1 -> header      # taken: next iteration
#     <rest of the body>
#     Jmp -> header
#
# No structurer took a conditional BACKWARD branch (`IfStructurer` leaves them to
# the loop guard, `LoopContinueRegionPass` only knows unconditional jumps), so the
# function printed `if (r8 == null) goto label_19;` and was not valid JavaScript.
# ----------------------------------------------------------------------------------------------------

_ASSIGN = r"""

=> [Function #5924 "" of 51 bytes]: 3 params, frame size=10, strict=1, exc handler=0, debug info=0  @ offset 0x00191c56

Bytecode listing:

==> 00000000: <LoadParam>: <Reg8: 0, UInt8: 1>
==> 00000003: <LoadParam>: <Reg8: 7, UInt8: 2>
==> 00000006: <Mov>: <Reg8: 5, Reg8: 7>
==> 00000009: <LoadConstNull>: <Reg8: 1>
==> 0000000b: <GetPNameList>: <Reg8: 6, Reg8: 5, Reg8: 4, Reg8: 3>
==> 00000010: <JmpUndefined>: <Addr8: 33, Reg8: 6>  # Address: 00000031
==> 00000013: <GetNextPName>: <Reg8: 2, Reg8: 6, Reg8: 5, Reg8: 4, Reg8: 3>
==> 00000019: <JmpUndefined>: <Addr8: 24, Reg8: 2>  # Address: 00000031
==> 0000001c: <Mov>: <Reg8: 9, Reg8: 2>
==> 0000001f: <GetByVal>: <Reg8: 8, Reg8: 7, Reg8: 9>
==> 00000023: <JEqual>: <Addr8: -16, Reg8: 8, Reg8: 1>  # Address: 00000013
==> 00000027: <GetByVal>: <Reg8: 8, Reg8: 7, Reg8: 9>
==> 0000002b: <PutByVal>: <Reg8: 0, Reg8: 9, Reg8: 8>
==> 0000002f: <Jmp>: <Addr8: -28>  # Address: 00000013
==> 00000031: <Ret>: <Reg8: 0>
"""


def _render_2() -> str:
    context = Decompiler.build_context(_ASSIGN, 5924, strict=False)

    return Decompiler.render(context, verbose=False, raw=False)


def test_conditional_branch_back_to_the_loop_is_a_continue():
    js = _render_2()

    assert "goto" not in js
    assert "if (r8 == null) {\n            continue;\n        }" in js
    assert js.index("continue;") < js.index("param1[r9] = param2[r9];")


# ----------------------------------------------------------------------------------------------------
# conditional_continue_latch
#
# F-10 (non-return targets): `if (c) continue;` compiled as a branch to a second, empty back edge.
#
#     96/8548  `cloneObjectProperties`: `if (k === "__initData") { v = o.__initData; if (v !== undefined) continue; }`
#              then the body. The branch targets an empty latch block, not the loop header, and the
#              else arm of the first test also falls into the body.
# ----------------------------------------------------------------------------------------------------

def test_a_branch_to_an_empty_latch_is_a_continue_and_the_body_still_follows():
    hasm = (_DATA / "conditional_continue_empty_latch_96_8548.hasm").read_text(encoding="utf-8")
    out = Decompiler.render(Decompiler.build_context(hasm, 8548, strict=False), verbose=False, raw=False)

    assert "goto" not in out
    # The second test reloads `r13` (`r13 = r0.__initData; if (r13 !== undefined) continue`) - not the same value as the
    # first test's `r13`, so the two are not a `case` chain and the crossed fold takes them (F-244):
    # the body runs unless `k === "__initData" && v !== undefined`.
    assert 'if (r13 !== "__initData" || r0.__initData === undefined) {' in out
    assert out.index("if (r13 !== ") < out.index("r15[r14] = r13;")
    assert "} else {" not in out


# ----------------------------------------------------------------------------------------------------
# conditional_continue_while_true
#
# `if (c) continue;` in a loop with no test and no update of its own (F-200).
#
#     while (true) { r22 = it.next(); if (r22 === undefined) ...; if (!hasOwn(k)) goto HEADER; ... }
#
# The loop over a `for-in`'s `GetNextPName` has no continue target (the header IS the body's first block),
# so `ConditionalContinueRegionPass` skipped it and the branch back to the header stayed
# `if (!r27) goto label_286` (98/2493 `recomputePluginOrdering`). The header is the next iteration.
# ----------------------------------------------------------------------------------------------------

def _render_3(name: str, function_id: int) -> str:
    hasm = (_DATA / name).read_text(encoding="utf-8")
    out = Decompiler.render(Decompiler.build_context(hasm, function_id, strict=False), verbose=False, raw=False)

    return "\n".join(line for line in out.split("\n") if not line.strip().startswith("//"))


def test_a_for_in_filter_is_a_continue():
    out = _render_3("conditional_continue_while_true_98_2493.hasm", 2493)

    assert "goto" not in out
    assert "if (!r27) {\n                                    continue;\n                                }" in out


def test_a_second_while_true_loop_has_no_goto():
    out = _render_3("conditional_continue_while_true_98_2143.hasm", 2143)

    assert "goto" not in out


# ----------------------------------------------------------------------------------------------------
# continue_to_a_second_back_edge_stub
#
# `if (c) continue;` whose branch targets a second copy of the back edge (98/4271 `VirtualizedList.render`).
#
# The compiler ends the loop body with two blocks that are nothing but `Jmp header`: the normal latch and a second
# one only the spacer test (`if (disableVirtualization) <next item>`) jumps to. `ConditionalContinueRegionPass` only
# knew a copy that had already been emptied, so the branch stayed `if (r20) goto label_991;`.
# ----------------------------------------------------------------------------------------------------

def _render_4() -> str:
    hasm = (_DATA / "continue_to_a_second_back_edge_stub_98_4271.hasm").read_text(encoding="utf-8")
    out = Decompiler.render(Decompiler.build_context(hasm, 0, strict=False), verbose=False, raw=False)

    return "\n".join(line for line in out.split("\n") if not line.strip().startswith("//"))


def test_no_goto_is_left():
    assert "goto" not in _render_4()


def test_the_virtualization_test_continues_with_the_next_item():
    out = _render_4()

    assert "r20 = r20.disableVirtualization;\n                if (r20) {\n                    continue;\n                }" in out


# ----------------------------------------------------------------------------------------------------
# get_by_val_key_redefines_object
#
# `GetByVal` reads its key by name, which keeps the key register's own
# definition in the output. The object expression is inlined, so it has to see
# that rewrite (96/13659):
#
#     r1 = env[0];  r0 = env[1];  r0 = r1[r0]      is `r1[r0]`, not `r0[0][r0]`
# ----------------------------------------------------------------------------------------------------

_HASM = r"""
=> [Function #13659 "get" of 17 bytes]: 1 params, frame size=2, strict=1, exc handler=0, debug info=0  @ offset 0x00220e98

Bytecode listing:

==> 00000000: <GetEnvironment>: <Reg8: 0, UInt8: 0>
==> 00000003: <LoadFromEnvironment>: <Reg8: 1, Reg8: 0, UInt8: 0>
==> 00000007: <LoadFromEnvironment>: <Reg8: 0, Reg8: 0, UInt8: 1>
==> 0000000b: <GetByVal>: <Reg8: 0, Reg8: 1, Reg8: 0>
==> 0000000f: <Ret>: <Reg8: 0>
"""


def test_inlined_object_is_not_read_through_the_redefined_key_register():
    js = Decompiler.render(Decompiler.build_context(_HASM, 13659, strict=False), verbose=False, raw=False)

    assert "r1 = r0[0];" in js
    assert "return r1[r0];" in js
    assert "r0[0][r0]" not in js


# ----------------------------------------------------------------------------------------------------
# inner_loop_register_tested_by_the_outer_loop
#
# An inner `for` keeps the register name the enclosing loop still tests (98/2632 `commitBeforeMutationEffects`).
#
# `do { ... for (r1 = r9[267]; null !== r1; r1 = r12.return) { ... r1 = r10; break } } while (null !== r1)`: the
# induction register was renamed `i`, so the outer test read an `r1` that no path of the inner loop wrote any more.
# ----------------------------------------------------------------------------------------------------

def test_the_inner_for_keeps_the_register_the_outer_loop_tests():
    hasm = (_DATA / "switch_join_after_a_throwing_default_98_2632.hasm").read_text(encoding="utf-8")
    out = Decompiler.render(Decompiler.build_context(hasm, 0, strict=False), verbose=False, raw=False)

    assert "} while (null !== r1);" in out
    assert "for (r1 = r9[267]; null !== r1; r1 = r12.return)" in out


# ----------------------------------------------------------------------------------------------------
# loop_advance_kept_with_the_folded_test
#
# The loop advance is printed when the loop test folded into the condition (98/8694 `saveSnapshot`).
#
# `r2 = r6.parentElement` at the bottom of the body feeds `Mov r6, r2` at the top. The condition reads the member again
# (`while (r6.parentElement)`), the copy was inlined into it and the assignment vanished, so the loop never advanced.
# ----------------------------------------------------------------------------------------------------

def _render_5() -> str:
    hasm = (_DATA / "parameter_copy_rewritten_by_the_loop_98_8694.hasm").read_text(encoding="utf-8")

    return Decompiler.render(Decompiler.build_context(hasm, 0, strict=False), verbose=False, raw=False)


def test_the_advance_is_printed_before_the_condition():
    out = _render_5()

    assert "r2 = r6.parentElement;" in out
    assert out.index("r2 = r6.parentElement;") < out.index("} while (r6.parentElement)")


@pytest.mark.skipif(shutil.which("node") is None, reason="node is not installed")
def test_the_output_parses(tmp_path: Path):
    path = tmp_path / "out.js"
    path.write_text(_render_5(), encoding="utf-8")

    assert subprocess.run(["node", "--check", str(path)], capture_output=True, text=True).returncode == 0


# ----------------------------------------------------------------------------------------------------
# loop_alias_symbolic_copy
#
# The per-iteration copy of a `for` loop's counter (`Mov r1, r0` ... `i = r1 + 1`)
# is merged into the counter even when loop-safety kept its read symbolic, so
# the Mov carries `r0` itself rather than the initializer's literal
# (`areInputsEqual`, 98/4378).
# ----------------------------------------------------------------------------------------------------

_HASM_2 = """
=> [Function #4378 "areInputsEqual" of 113 bytes]: 3 params, frame size=22, strict=1, exc handler=0, debug info=0  @ offset 0x001a1d77

Bytecode listing:

==> 00000000: <GetParentEnvironment>: <Reg8: 10, UInt8: 0>
==> 00000003: <LoadParam>: <Reg8: 9, UInt8: 1>
==> 00000006: <LoadParam>: <Reg8: 8, UInt8: 2>
==> 00000009: <GetByIdShort>: <Reg8: 11, Reg8: 9, UInt8: 0, string_id: 177>  # String: 'length' (Identifier)
==> 0000000e: <GetByIdShort>: <Reg8: 7, Reg8: 8, UInt8: 0, string_id: 177>  # String: 'length' (Identifier)
==> 00000013: <JStrictNotEqual>: <Addr8: 90, Reg8: 11, Reg8: 7>  # Address: 0000006d
==> 00000017: <GetByIdShort>: <Reg8: 7, Reg8: 9, UInt8: 0, string_id: 177>  # String: 'length' (Identifier)
==> 0000001c: <LoadConstZero>: <Reg8: 0>
==> 0000001e: <Less>: <Reg8: 3, Reg8: 0, Reg8: 7>
==> 00000022: <LoadConstUInt8>: <Reg8: 2, UInt8: 1>
==> 00000025: <LoadConstTrue>: <Reg8: 4>
==> 00000027: <LoadConstUndefined>: <Reg8: 5>
==> 00000029: <LoadConstFalse>: <Reg8: 6>
==> 0000002b: <JmpFalse>: <Addr8: 64, Reg8: 3>  # Address: 0000006b
==> 0000002e: <GetByVal>: <Reg8: 12, Reg8: 9, Reg8: 0>
==> 00000032: <GetByVal>: <Reg8: 11, Reg8: 8, Reg8: 0>
==> 00000036: <Mov>: <Reg8: 1, Reg8: 0>
==> 00000039: <LoadConstTrue>: <Reg8: 3>
==> 0000003b: <JStrictEqual>: <Addr8: 30, Reg8: 12, Reg8: 11>  # Address: 00000059
==> 0000003f: <LoadFromEnvironment>: <Reg8: 7, Reg8: 10, UInt8: 0>
==> 00000043: <Call2>: <Reg8: 12, Reg8: 7, Reg8: 5, Reg8: 12>
==> 00000048: <LoadConstFalse>: <Reg8: 3>
==> 0000004a: <JmpFalse>: <Addr8: 15, Reg8: 12>  # Address: 00000059
==> 0000004d: <Call2>: <Reg8: 7, Reg8: 7, Reg8: 5, Reg8: 11>
==> 00000052: <LoadConstFalse>: <Reg8: 3>
==> 00000054: <JmpFalse>: <Addr8: 5, Reg8: 7>  # Address: 00000059
==> 00000057: <LoadConstTrue>: <Reg8: 3>
==> 00000059: <JmpTrue>: <Addr8: 5, Reg8: 3>  # Address: 0000005e
==> 0000005c: <Ret>: <Reg8: 6>
==> 0000005e: <AddN>: <Reg8: 0, Reg8: 1, Reg8: 2>
==> 00000062: <GetByIdShort>: <Reg8: 7, Reg8: 9, UInt8: 0, string_id: 177>  # String: 'length' (Identifier)
==> 00000067: <JLess>: <Addr8: -57, Reg8: 0, Reg8: 7>  # Address: 0000002e
==> 0000006b: <Ret>: <Reg8: 4>
==> 0000006d: <LoadConstFalse>: <Reg8: 4>
==> 0000006f: <Ret>: <Reg8: 4>


"""


def test_symbolic_counter_copy_is_merged_into_the_counter():
    js = Decompiler.render(Decompiler.build_context(_HASM_2, 4378, strict=False), verbose=False, raw=False)

    assert "for (i = 0; i < param1.length; i++) {" in js
    assert "r1 = i;" not in js
    assert not re.search(r"\br1\b", js)


# ----------------------------------------------------------------------------------------------------
# loop_around_a_try_that_leaves_by_a_jump
#
# The body of `while (true) { try { ... } catch { ... } }` stays inside the loop and leaves it by `break` (96/2139).
#
# The edge from a protected block to the `catch` is implicit, so the natural loop was only the header and the catch's
# back edge: the rest of the `try` body was printed behind the loop (an exception in it was not caught) and the arms
# that left the body kept `goto`s. `LoopAnalysis.include_protected_blocks` adds the protected blocks to the loop and
# `LoopExitBreakRegionPass` turns the ways out into `break` (copying the small shared exit block into each arm).
# ----------------------------------------------------------------------------------------------------

def _render_6() -> str:
    hasm = (_DATA / "loop_around_a_try_that_leaves_by_a_jump_96_2139.hasm").read_text(encoding="utf-8")

    return Decompiler.render(Decompiler.build_context(hasm, 0, strict=False), verbose=False, raw=False)


def test_no_goto_is_left_2():
    assert "goto" not in _render_6()


def test_the_body_is_inside_the_try_inside_the_loop():
    out = _render_6()
    loop = out.index("while (true)")
    try_at = out.index("try {", loop)
    catch_at = out.index("} catch", try_at)

    assert "break;" in out[try_at:catch_at]


# ----------------------------------------------------------------------------------------------------
# loop_body_short_circuit
#
# Short-circuit tests inside a loop body fold like any others (F-169).
#
# `ShortCircuitConditionCfgPass` left EVERY block of a loop alone, so a `for-in` body's
#
#     if (!a || typeof a !== "object") { init }
#
# stayed `if (!a) { init } else { ...; if (typeof a === "object") goto J }` and, worse, dropped the fall from the
# second test into `init`. Only the loop's own tests (header, latches) are off limits now, and a fold may end on
# a latch when nothing has to be copied onto the edge into it. Case labels keep their own tests in a body (the
# `switch` wants them).
#
#     96/11027  the `||` in a `for-in` body (the old output lost a path)
#     98/2211   `processTransformOrigin`: a `switch` in a loop body stays a `switch`
#     96/2026   `refreshCache`: two tests that leave the loop are still one `||`
# ----------------------------------------------------------------------------------------------------

def _render_7(name: str, function_id: int) -> str:
    hasm = (_DATA / name).read_text(encoding="utf-8")
    out = Decompiler.render(Decompiler.build_context(hasm, function_id, strict=False), verbose=False, raw=False)

    return "\n".join(line for line in out.split("\n") if not line.strip().startswith("//"))


def test_the_second_test_falls_into_the_init():
    out = _render_7("loop_body_crossed_or_96_11027.hasm", 11027)

    assert "goto" not in out
    assert 'if (!r9 || typeof r2[2][r1[0]] !== "object") {\n            r9 = {  };' in out


def test_a_switch_in_a_loop_body_stays_a_switch():
    out = _render_7("loop_body_case_chain_98_2211.hasm", 2211)

    assert "goto" not in out
    assert "switch (r30) {" in out


def test_two_tests_that_leave_the_loop_are_one_or():
    out = _render_7("loop_body_leave_loop_or_96_2026.hasm", 2026)

    assert "goto" not in out
    assert "if (24 === r4 || 3 === r4) {" in out


# ----------------------------------------------------------------------------------------------------
# loop_break_forwarded_exit
#
# A `break` out of a loop that closes an `else` arm: the loop's way out only jumps on (F-198).
#
#     else { ...; do { ...; if (c) goto MERGE; ... } while (d); }     MERGE: code after the whole `if`
#
# The latch falls into a lone `jmp MERGE` and the break jumps to MERGE itself, which the arms of the other
# `if` reach as well. `LoopBreakStructurer` took MERGE for a join the loop does not own and left
# `if (!(r26 > r18)) goto label_616` (98/10142 `BezierEasing`). A `break` lands right behind the loop, on that
# jump, so it is the same way out. The `break` block is synthetic (address -1) so the `if` that jumps over the
# block it splits still finds that block.
# ----------------------------------------------------------------------------------------------------

def _render_8(name: str, function_id: int) -> str:
    hasm = (_DATA / name).read_text(encoding="utf-8")
    out = Decompiler.render(Decompiler.build_context(hasm, function_id, strict=False), verbose=False, raw=False)

    return "\n".join(line for line in out.split("\n") if not line.strip().startswith("//"))


def test_a_break_to_the_join_behind_a_forwarding_exit_is_a_break():
    out = _render_8("loop_break_forwarded_exit_98_10142.hasm", 10142)

    assert "goto" not in out
    assert "if (!(r26 > r18)) {\n                            break;\n                        }" in out
    # the `if` in front of it keeps its own join
    assert "if (0 < r12) {\n                            r5 = r0;\n                            r6 = r10;\n                        }" in out


# ----------------------------------------------------------------------------------------------------
# loop_breaks_inside_if_arms_do_not_stop_the_if
#
# An `if/else` inside a loop whose arms leave the loop with `if (c) break;` kept its `goto`s (98/10170
# `useAnimatedPropsMemo`).
#
# `LoopBreakStructurer` replaces an exit branch by a block holding a `break`; that block keeps the address of the
# branch's block, so `_DominanceIfBuilder._convert` took it for an item of neither arm, ended the arms there and bailed
# with an empty `else`: `if (r17 === "style") goto label_259`, `goto label_251`, `goto label_274`. The block now follows
# the item before it, as an address-less one does.
# ----------------------------------------------------------------------------------------------------

def test_arms_that_break_out_of_the_loop_still_form_an_if_else():
    hasm = (_DATA / "loop_breaks_in_if_arms_98_10170.hasm").read_text(encoding="utf-8")
    out = Decompiler.render(Decompiler.build_context(hasm, 10170, strict=False), verbose=False, raw=False)

    assert "goto label" not in out
    assert 'if (r17 === "style") {' in out
    assert out.count("break;") == 4
    assert "continue;" not in out


# ----------------------------------------------------------------------------------------------------
# loop_carried_definition
#
# A register a loop overwrites and the code after the loop reads by name
# (`makeSafeRegex`, 96/9342):
#
#     r0 = param1;  for (const x of xs) { r0 = r17.join(...); }  return r0;
#
# The `LoadParam` alias was folded into its readers and never printed, so when the
# loop ran zero times (or skipped the write) `return r0` read a register nothing
# had assigned. `LoopCarriedDefinitionPass` prints the pre-loop definition.
# ----------------------------------------------------------------------------------------------------

_MAKE_SAFE_REGEX = r"""

=> [Function #9342 "makeSafeRegex" of 232 bytes]: 2 params, frame size=31, strict=1, exc handler=1, debug info=0  @ offset 0x001dc3c3
  [Exception handlers: [start=0x42, end=0xda, target=0xdf] ]

Bytecode listing:

==> 00000000: <LoadParam>: <Reg8: 0, UInt8: 1>
==> 00000003: <GetEnvironment>: <Reg8: 14, UInt8: 0>
==> 00000006: <LoadFromEnvironment>: <Reg8: 1, Reg8: 14, UInt8: 8>
==> 0000000a: <Mov>: <Reg8: 13, Reg8: 1>
==> 0000000d: <IteratorBegin>: <Reg8: 2, Reg8: 13>
==> 00000010: <LoadConstUndefined>: <Reg8: 12>
==> 00000012: <LoadConstUInt8>: <Reg8: 11, UInt8: 2>
==> 00000015: <LoadConstZero>: <Reg8: 10>
==> 00000017: <LoadConstUInt8>: <Reg8: 9, UInt8: 1>
==> 0000001a: <GetGlobalObject>: <Reg8: 8>
==> 0000001c: <LoadConstString>: <Reg8: 7, string_id: 7163>  # String: '' (Identifier)
==> 00000020: <LoadConstString>: <Reg8: 6, string_id: 1490>  # String: '*' (String)
==> 00000024: <LoadConstString>: <Reg8: 5, string_id: 4455>  # String: '{0,' (String)
==> 00000028: <LoadConstString>: <Reg8: 4, string_id: 599>  # String: '}' (String)
==> 0000002c: <LoadConstString>: <Reg8: 3, string_id: 316>  # String: '+' (String)
==> 00000030: <LoadConstString>: <Reg8: 1, string_id: 1924>  # String: '{1,' (String)
==> 00000034: <IteratorNext>: <Reg8: 16, Reg8: 2, Reg8: 13>
==> 00000038: <Mov>: <Reg8: 15, Reg8: 2>
==> 0000003b: <JStrictEqualLong>: <Addr32: 171, Reg8: 15, Reg8: 12>  # Address: 000000e6
==> 00000042: <LoadFromEnvironment>: <Reg8: 15, Reg8: 14, UInt8: 0>
==> 00000046: <Call3>: <Reg8: 15, Reg8: 15, Reg8: 12, Reg8: 16, Reg8: 11>
==> 0000004c: <GetByVal>: <Reg8: 19, Reg8: 15, Reg8: 10>
==> 00000050: <GetByVal>: <Reg8: 18, Reg8: 15, Reg8: 9>
==> 00000054: <Mov>: <Reg8: 17, Reg8: 0>
==> 00000057: <GetByIdShort>: <Reg8: 16, Reg8: 17, UInt8: 1, string_id: 229>  # String: 'split' (Identifier)
==> 0000005c: <TryGetById>: <Reg8: 15, Reg8: 8, UInt8: 2, string_id: 14>  # String: 'HermesInternal' (Identifier)
==> 00000062: <GetByIdShort>: <Reg8: 15, Reg8: 15, UInt8: 3, string_id: 96>  # String: 'concat' (Identifier)
==> 00000067: <Call3>: <Reg8: 15, Reg8: 15, Reg8: 7, Reg8: 19, Reg8: 6>
==> 0000006d: <Call2>: <Reg8: 17, Reg8: 16, Reg8: 17, Reg8: 15>
==> 00000072: <GetByIdShort>: <Reg8: 16, Reg8: 17, UInt8: 4, string_id: 165>  # String: 'join' (Identifier)
==> 00000077: <TryGetById>: <Reg8: 15, Reg8: 8, UInt8: 2, string_id: 14>  # String: 'HermesInternal' (Identifier)
==> 0000007d: <GetByIdShort>: <Reg8: 15, Reg8: 15, UInt8: 3, string_id: 96>  # String: 'concat' (Identifier)
==> 00000082: <Mov>: <Reg8: 24, Reg8: 7>
==> 00000085: <Mov>: <Reg8: 23, Reg8: 19>
==> 00000088: <Mov>: <Reg8: 22, Reg8: 5>
==> 0000008b: <Mov>: <Reg8: 21, Reg8: 18>
==> 0000008e: <Mov>: <Reg8: 20, Reg8: 4>
==> 00000091: <Call>: <Reg8: 15, Reg8: 15, UInt8: 5>
==> 00000095: <Call2>: <Reg8: 17, Reg8: 16, Reg8: 17, Reg8: 15>
==> 0000009a: <GetByIdShort>: <Reg8: 16, Reg8: 17, UInt8: 1, string_id: 229>  # String: 'split' (Identifier)
==> 0000009f: <TryGetById>: <Reg8: 15, Reg8: 8, UInt8: 2, string_id: 14>  # String: 'HermesInternal' (Identifier)
==> 000000a5: <GetByIdShort>: <Reg8: 15, Reg8: 15, UInt8: 3, string_id: 96>  # String: 'concat' (Identifier)
==> 000000aa: <Call3>: <Reg8: 15, Reg8: 15, Reg8: 7, Reg8: 19, Reg8: 3>
==> 000000b0: <Call2>: <Reg8: 17, Reg8: 16, Reg8: 17, Reg8: 15>
==> 000000b5: <GetByIdShort>: <Reg8: 16, Reg8: 17, UInt8: 4, string_id: 165>  # String: 'join' (Identifier)
==> 000000ba: <TryGetById>: <Reg8: 15, Reg8: 8, UInt8: 2, string_id: 14>  # String: 'HermesInternal' (Identifier)
==> 000000c0: <GetByIdShort>: <Reg8: 15, Reg8: 15, UInt8: 3, string_id: 96>  # String: 'concat' (Identifier)
==> 000000c5: <Mov>: <Reg8: 24, Reg8: 7>
==> 000000c8: <Mov>: <Reg8: 23, Reg8: 19>
==> 000000cb: <Mov>: <Reg8: 22, Reg8: 1>
==> 000000ce: <Mov>: <Reg8: 21, Reg8: 18>
==> 000000d1: <Call>: <Reg8: 15, Reg8: 15, UInt8: 5>
==> 000000d5: <Call2>: <Reg8: 0, Reg8: 16, Reg8: 17, Reg8: 15>
==> 000000da: <JmpLong>: <Addr32: -166>  # Address: 00000034
==> 000000df: <Catch>: <Reg8: 1>
==> 000000e1: <IteratorClose>: <Reg8: 2, UInt8: 1>
==> 000000e4: <Throw>: <Reg8: 1>
==> 000000e6: <Ret>: <Reg8: 0>
"""


def test_definition_before_a_loop_prints_when_read_after_it():
    context = Decompiler.build_context(_MAKE_SAFE_REGEX, 9342, strict=False)
    js = Decompiler.render(context, verbose=False, raw=False)

    assert "r0 = param1;" in js
    assert js.index("r0 = param1;") < js.index("return r0;")


# ----------------------------------------------------------------------------------------------------
# loop_condition_merge_analysis
#
# Two loop tests that both leave the loop are merged into one `||` (F-129). The test
# block that merged away used to stay a member of the loop (and a node of the dominator
# trees) the earlier analyses had found, and the structurer failed on it with an
# `IndexError` (96/2075, 2264, 2581, 2590, 13786; 98/2617).
#
# The analyses are recomputed once the merge pass has changed the graph.
# ----------------------------------------------------------------------------------------------------

def test_a_loop_test_merged_away_does_not_stay_in_the_loop_analysis():
    """96/2264 `pop` (a heap sift-down): rendering used to raise."""
    hasm = (_DATA / "loop_tests_merged_stale_analysis_96_2264.hasm").read_text(encoding="utf-8")

    out = Decompiler.render(Decompiler.build_context(hasm, 2264, strict=False), verbose=False, raw=False)

    assert out.startswith("function pop(param1)")


def test_a_merged_away_test_block_leaves_the_try_blocks_of_its_handler():
    """96/2146 `throwAndUnwindWorkLoop`: the handler still listed the merged block, so the
    dominator tree computed again afterwards looked it up and raised a `KeyError`."""
    hasm = (_DATA / "loop_tests_merged_in_try_96_2146.hasm").read_text(encoding="utf-8")

    out = Decompiler.render(Decompiler.build_context(hasm, 2146, strict=False), verbose=False, raw=False)

    assert out.startswith("function throwAndUnwindWorkLoop(")


# ----------------------------------------------------------------------------------------------------
# loop_counter_rewritten_before_an_if_test
#
# A loop's counter register is not renamed when the body rewrites it and an `if` test reads it afterwards (96/1931
# `reconcileChildFibersImpl`: `r7 = r3.type; if (r7 === r8) {...}` in a loop that counts with r7).
#
# The test of an `if` belongs to the `IfRegion`, no instruction reads it any more, so `_body_writes` saw the write but
# no later read and the pass renamed every `r7` it could reach to `i`, the test included: `i === r8` read the counter
# where the code meant the type. The tests of the `if`s now count as reads, placed right after the block they replaced.
# ----------------------------------------------------------------------------------------------------

def _instruction(dest_reg: int, value):
    return SimpleNamespace(name=f"r{dest_reg}", value=value, statement=None, terminator=None)


def _loop(test_reads: str):
    head = BasicBlock(0, 10)
    head.instructions.append(_instruction(7, Identifier("param2")))  # `r7 = <type>`, a write that is no update

    arm = BasicBlock(1, 20)
    arm.instructions.append(_instruction(3, Identifier("r8")))

    test = IfRegion()
    test.condition = Identifier(test_reads)
    test.source_block = head
    test.then_body.append(arm)

    body = SequenceRegion()
    body.append(head)
    body.append(test)

    return SimpleNamespace(body=body, update=None, initializer=None)


def test_a_test_that_reads_the_rewritten_counter_keeps_the_register_name():
    assert InductionVariableNamingPass._body_writes(_loop("r7"), "r7") is True


def test_a_test_that_reads_something_else_changes_nothing():
    assert InductionVariableNamingPass._body_writes(_loop("r9"), "r7") is False


# ----------------------------------------------------------------------------------------------------
# loop_exit_body_of_several_blocks
#
# A loop's `found` exit whose body is several blocks and only ends the function moves into the loop (96/2662).
#
#     for (; r10 !== null; r10 = r10.return) {
#         ...
#         if (1 === r11 && (A || B && (C || D))) goto BODY;     // BODY is laid out behind the loop
#     }
#     BODY: r9 = ...; r8 = ...; if (null !== r6) { ... }        // and returns
#
# `LoopBreakStructurer` knew single-block exit bodies only, so the branch stayed a `goto`. A body entered only
# through that branch, with no edge back into the loop or on to shared code, is spliced in as `if (cond) { ... }`
# (Shape E).
# ----------------------------------------------------------------------------------------------------

def test_the_found_body_moves_into_the_loop():
    hasm = (_DATA / "loop_exit_body_of_several_blocks_96_2662.hasm").read_text(encoding="utf-8")
    code = Decompiler.render(Decompiler.build_context(hasm, 2662, strict=False), verbose=False, raw=False)

    assert "goto" not in code

    loop = code.split("for (; null !== r10;")[1]
    arm = loop.split("r9 = r0[266].call(undefined, param3, param1);")[0]

    assert 'getDerivedStateFromError' in arm.split("\n")[-2] or "getDerivedStateFromError" in arm
    assert "if (null !== r6) {" in loop
    assert loop.count("return undefined;") == 2


# ----------------------------------------------------------------------------------------------------
# loop_exit_join
#
# A join block that is also an inner loop's latch, behind an `if` whose arm
# carves out a `break`.
#
#     if (i === 2 && j === 2) break outer;   // 0x3d / 0x41
#     hits = ...;                            // 0x45, the latch: runs on every path
#
# `IfStructurer` classified the `break` marker region (synthetic block, not in
# the dominator tree) as belonging to neither arm, bailed, and a later pass left
# the latch's `Mov r13, r4` inside the `if`. It must print after it.
# ----------------------------------------------------------------------------------------------------

_FIXTURES = Path(__file__).resolve().parent.parent / "apps" / "demo" / "fixtures"


def _render_9(fixture: str, index: int, name: str) -> str:
    hasm = (_FIXTURES / fixture / "sections" / f"function_{index}_{name}.hasm").read_text(encoding="utf-8")
    return Decompiler.render(Decompiler.build_context(hasm, index), verbose=False)


def test_the_latch_runs_after_a_conditional_break():
    out = _render_9("96", 15068, "tripleNestedLabeledTest")

    assert re.search(
        r"if \(i === 2 && j === 2\) \{\s*break loop_1;\s*\}\s*r13 = r4;", out
    ), out


def test_the_same_shape_in_the_other_bundle():
    out = _render_9("98", 9459, "tripleNestedLabeledTest")

    assert re.search(
        r"if \(i === 2 && j === 2\) \{\s*break loop_1;\s*\}\s*r0 = r3;", out
    ), out


# ----------------------------------------------------------------------------------------------------
# loop_exit_shared_return
#
# Exits of a loop body that jump to a shared `return` behind the loop (96/4123 `parseHost`,
# the IPv4 part loop):
#
#     for (i = 0; i < n - 1; i++) { ...; if (part < 0 || part > 255) return null; ... }
#     <code after the loop>
#
# Two things went wrong while the `return` was one block with many predecessors:
#
# - `if (part < 0) goto RET; rest` became `if (part >= 0) { rest }`: the body just ended and the
#   loop went on (`return null` was gone);
# - a zero-trip guard `if (0 < n) { loop }` whose loop ends into the code the guard jumps to
#   (the part after the loop) put that code in the other arm only: after the loop it never ran.
# ----------------------------------------------------------------------------------------------------

def _render_10(name: str, function_id: int) -> str:
    hasm = (_DATA / name).read_text(encoding="utf-8")
    return Decompiler.render(Decompiler.build_context(hasm, function_id, strict=False), verbose=False, raw=False)


def test_loop_exits_to_a_shared_return_stay_exits():
    out = _render_10("loop_exit_shared_return_96_4123.hasm", 4123)

    loop = out[out.index("for (i = 0; i < r7 - 1; i++) {"):]
    body = loop[:loop.index("r2 = r7 - 1;")]

    assert "goto" not in out
    assert body.count("return null;") == 2


def test_the_code_after_a_zero_trip_loop_runs_after_the_loop_too():
    out = _render_10("loop_exit_shared_return_96_4123.hasm", 4123)

    loop_at = out.index("for (i = 0; i < r7 - 1; i++) {")

    assert out.count("r0 = r3 + r2;") == 1
    assert out.index("r0 = r3 + r2;") > loop_at


# ----------------------------------------------------------------------------------------------------
# loop_guard_initializer
#
# A counting-down loop's entry guard repeats the loop's own test, so the
# counter's first value (`r0 = n - 1`) sits in front of the guard and the loop
# used to print `for (; 0 <= i; ...)` with `i` never assigned
# (`_ensureClosestStickyHeader`, 98/4260).
# `LoopGuardInitializerPass` moves it into the header and drops the guard.
# ----------------------------------------------------------------------------------------------------

_HASM_3 = """
=> [Function #4260 "_ensureClosestStickyHeader" of 98 bytes]: 5 params, frame size=19, strict=1, exc handler=0, debug info=0  @ offset 0x0019de06

Bytecode listing:

==> 00000000: <LoadParam>: <Reg8: 7, UInt8: 2>
==> 00000003: <LoadParam>: <Reg8: 8, UInt8: 1>
==> 00000006: <GetById>: <Reg8: 8, Reg8: 8, UInt8: 0, string_id: 11193>  # String: 'ListHeaderComponent' (Identifier)
==> 0000000c: <LoadConstZero>: <Reg8: 4>
==> 0000000e: <LoadConstZero>: <Reg8: 2>
==> 00000010: <JmpFalse>: <Addr8: 6, Reg8: 8>  # Address: 00000016
==> 00000013: <LoadConstUInt8>: <Reg8: 2, UInt8: 1>
==> 00000016: <LoadParam>: <Reg8: 8, UInt8: 4>
==> 00000019: <LoadConstUInt8>: <Reg8: 3, UInt8: 1>
==> 0000001c: <Sub>: <Reg8: 0, Reg8: 8, Reg8: 3>
==> 00000020: <JNotLessEqualN>: <Addr8: 62, Reg8: 4, Reg8: 0>  # Address: 0000005e
==> 00000024: <GetByIdShort>: <Reg8: 8, Reg8: 7, UInt8: 1, string_id: 11>  # String: 'has' (Identifier)
==> 00000029: <AddN>: <Reg8: 1, Reg8: 0, Reg8: 2>
==> 0000002d: <Call2>: <Reg8: 8, Reg8: 8, Reg8: 7, Reg8: 1>
==> 00000032: <Mov>: <Reg8: 1, Reg8: 0>
==> 00000035: <JmpTrue>: <Addr8: 13, Reg8: 8>  # Address: 00000042
==> 00000038: <SubN>: <Reg8: 0, Reg8: 1, Reg8: 3>
==> 0000003c: <JLessEqualN>: <Addr8: -24, Reg8: 4, Reg8: 0>  # Address: 00000024
==> 00000040: <Jmp>: <Addr8: 30>  # Address: 0000005e
==> 00000042: <LoadParam>: <Reg8: 9, UInt8: 3>
==> 00000045: <GetById>: <Reg8: 8, Reg8: 9, UInt8: 2, string_id: 8963>  # String: 'addCells' (Identifier)
==> 0000004b: <NewObjectWithBuffer>: <Reg8: 7, UInt16: 1108, UInt16: 17356>  # Object: {'first': null, 'last': null}
==> 00000051: <PutOwnBySlotIdx>: <Reg8: 7, Reg8: 1, UInt8: 0>
==> 00000055: <PutOwnBySlotIdx>: <Reg8: 7, Reg8: 1, UInt8: 1>
==> 00000059: <Call2>: <Reg8: 7, Reg8: 8, Reg8: 9, Reg8: 7>
==> 0000005e: <LoadConstUndefined>: <Reg8: 6>
==> 00000060: <Ret>: <Reg8: 6>


"""


def test_guarded_countdown_loop_gets_its_initializer():
    js = Decompiler.render(Decompiler.build_context(_HASM_3, 4260, strict=False), verbose=False, raw=False)

    assert "for (i = param4 - 1; 0 <= i; i--) {" in js
    assert "if (0 <= r0)" not in js
    assert not re.search(r"\br0\b", js)
    assert not re.search(r"\br1 = i;", js)


# ----------------------------------------------------------------------------------------------------
# loop_header_ordinary_if
#
# A bottom-tested loop's header branch is an ordinary `if` in the body (F-172).
#
# `labeledBreakTest` (`do { if (r5 === 1 && j === 1) { log; break outer } log } while (...)`) had its header's test
# treated as a loop test, so the `&&` was never folded and the output lost the `log` of the `r5 === 1 && j !== 1`
# path. A header that branches only inside the loop, of a loop whose latch carries the test, is folded like any
# other in-body test, and a crossed fold may end on a latch.
#
#     96/15065  labeledBreakTest
#     98/9456   labeledBreakTest
# ----------------------------------------------------------------------------------------------------

def _render_11(name: str, function_id: int) -> str:
    hasm = (_DATA / name).read_text(encoding="utf-8")
    out = Decompiler.render(Decompiler.build_context(hasm, function_id, strict=False), verbose=False, raw=False)

    return "\n".join(line for line in out.split("\n") if not line.strip().startswith("//"))


def _check(out: str, outer: str):
    assert "goto" not in out
    assert f"if ({outer} === 1 && j === 1) {{" in out
    assert "break loop_1;" in out
    # the log after the test runs on every path that did not break
    assert out.index("break loop_1;") < out.index(f"console.log({outer}, j);")


def test_labeled_break_96():
    _check(_render_11("loop_header_ordinary_if_96_15065.hasm", 15065), "r5")


def test_labeled_break_98():
    _check(_render_11("loop_header_ordinary_if_98_9456.hasm", 9456), "i")


# ----------------------------------------------------------------------------------------------------
# loop_jumping_into_the_other_arm
#
# A jump from one arm of an `if` onto the first block of the other arm prints as a labeled block (F-314, 98/2775).
#
#     if (null === task) { A } else { loop { ... if (null === task) goto A; ... } }
#
# The loop in the `else` arm leaves into the code of the `then` arm. No sibling follows the jump, so the last resort
# of the retry ladder wraps the two arms (`label_A_end: { label_A: { if (!c) { else arm; break label_A_end; } } A }`)
# and the jumps become `break label_A;`. Without it the function printed five raw `goto`s.
# ----------------------------------------------------------------------------------------------------

def _render_12() -> str:
    hasm = (_DATA / "loop_jumping_into_the_other_arm_98_2775.hasm").read_text(encoding="utf-8")

    return Decompiler.render(Decompiler.build_context(hasm, 2775, strict=False), verbose=False, raw=False)


def test_the_jumps_into_the_other_arm_become_labeled_breaks():
    out = _render_12()

    assert "goto label_" not in out
    assert "label_433_end: {" in out
    assert out.count("break label_433;") == 3


@pytest.mark.skipif(shutil.which("node") is None, reason="node is not installed")
def test_the_labeled_output_parses(tmp_path: Path):
    path = tmp_path / "out.js"
    path.write_text(_render_12(), encoding="utf-8")

    done = subprocess.run(["node", "--check", str(path)], capture_output=True, text=True)

    assert done.returncode == 0, done.stderr


# ----------------------------------------------------------------------------------------------------
# loop_latch_terminal_exit
#
# A bottom-tested loop whose way out ends in a `return`/`throw` of its own, with another exit elsewhere (F-149).
#
#     do {                                    // 96/11086 `useHandler`
#         r4 = it.next();
#         if (r4 === undefined) break;        // -> the code after the throw
#         ...
#     } while (isWorklet(...));
#     throw new ReanimatedError(...);         // the latch's exit
#
# `LoopConditionRegionPass` made the latch the loop's `while (c)` and left the `throw` behind the loop, so
# the bare `break` on `undefined` ran the `throw` too: every function that found only worklets threw.
# The latch's exit is now moved into the loop (`if (!c) { throw }`, Shape B) and the loop keeps its one
# real way out, the `break`. A bare `break` also needs the loop's own completion to reach the same block.
# ----------------------------------------------------------------------------------------------------

def _code(name: str, function_id: int) -> str:
    hasm = (_DATA / name).read_text(encoding="utf-8")

    return Decompiler.render(Decompiler.build_context(hasm, function_id, strict=False), verbose=False, raw=False)


def test_a_throw_behind_the_loop_moves_into_it_and_the_loop_is_a_for_in():
    code = _code("loop_latch_throw_exit_96_11086.hasm", 11086)

    assert "for (const r4 in r10) {" in code
    assert "if (!r2) {" in code
    assert code.index("throw new r8(") < code.index("r4 = r2.buildDependencies")
    assert "HermesPropertyIterator" not in code
    assert "do {" not in code
    assert "goto" not in code


def test_the_code_after_the_loop_is_reached_by_the_break_only():
    """98/9880 `finish`: the search loop `break`s on a match; running out returns `undefined`."""
    code = _code("loop_latch_return_exit_98_9880.hasm", 9880)

    # the found branch is several blocks and only returns, so it moves into the loop (Shape E); running out of
    # the loop is the end of the function (`undefined`)
    assert "goto" not in code
    assert "break;" not in code
    assert code.index("if (r6 === param1) {") < code.index("return r5[11];")
    assert code.rstrip().endswith("}\n    }\n}")


# ----------------------------------------------------------------------------------------------------
# loop_sibling_exits
#
# Several ways out of one loop onto the same block are all `break`s (F-245, 98/2609 `updateSimpleMemoComponent`).
#
# An inlined `shallowEqual` leaves its `do { ... } while (i < keys.length)` from two tests (`!hasOwnProperty`,
# `!Object.is`) onto the code after the loop, where the loop's own completion lands as well. Each exit saw the other as
# "some other way onto the block" and none was converted: one stayed a raw `goto`, the other became an
# `if (c) { rest of the body }` whose else path fell into the loop test (the loop ran on after a failed test).
#
# Only on the last retry rung (`cfg.sibling_loop_exits`): the same rule on the first attempt structured
# 98/10170 worse.
# ----------------------------------------------------------------------------------------------------

def test_both_exits_are_breaks_and_nothing_else_is_left():
    hasm = (_DATA / "loop_sibling_exits_98_2609.hasm").read_text(encoding="utf-8")
    out = Decompiler.render(Decompiler.build_context(hasm, 2609, strict=False), verbose=False, raw=False)

    assert "goto" not in out
    assert "if (!r20) {\n                                            break;" in out
    assert "if (!r18) {\n                                            break;" in out
    assert "} while (r1 < r15.length);" in out


# ----------------------------------------------------------------------------------------------------
# loop_update_alias_rewritten_on_exit_path
#
# A `for` update keeps reading the induction register when the alias copy is rewritten only on an exit path.
#
# `r5 = r1; if (r6 === param1) { r1 = r4.completion; r5 = r1.type; ...; return r0 } ... r1 = r5 - 1`: the exit arm
# rewrites both `r5` and `r1`, so `LoopInductionAliasPass` refused to fold the alias and the update printed
# `r1 = r5 - 1`. The update only runs on paths that reach a latch, and neither register is written on those
# (96/3146 `catch`, 8596 `cloneRecursive`; regression of F-266 which made the exit arm structure).
# ----------------------------------------------------------------------------------------------------

def test_update_reads_the_induction_register():
    hasm = (_DATA / "loop_update_alias_rewritten_on_exit_path_96_3146.hasm").read_text(encoding="utf-8")
    out = Decompiler.render(Decompiler.build_context(hasm, 3146, strict=False), verbose=False, raw=False)

    assert "r1 >= 0; r1--)" in out
    assert "r1 = r5 - 1" not in out
    assert 'r5 === "throw"' in out


# ----------------------------------------------------------------------------------------------------
# loop_with_the_latch_test_inside_an_if
#
# A loop whose back-edge test sits inside an `if` of its body is not a `do { } while (test)` (F-263).
#
# `for (; 1 <= s && 0 <= c && l[s] !== a[c]; c--) {}` is lowered as a guard plus a loop whose latch test is only
# reached when both bound checks passed; the paths that skip it leave the loop. Printing the latch's test as the
# `while (...)` of the loop evaluated it, with stale registers, on those paths too
# (98/2474 `describeNativeComponentFrame`: `} while (r9 !== r14[r8]);`).
# ----------------------------------------------------------------------------------------------------

def test_the_latch_test_in_an_if_stays_a_branch_and_the_exit_is_a_break():
    hasm = (_DATA / "loop_latch_inside_if_98_2474.hasm").read_text(encoding="utf-8")
    out = Decompiler.render(Decompiler.build_context(hasm, 2474, strict=False), verbose=False, raw=False)

    assert "} while (r9 !== r14[r8]);" not in out
    assert "} while (r9 !== r11[r12]);" not in out
    assert "if (r9 !== r8) {\n" in out and "continue;" in out


# ----------------------------------------------------------------------------------------------------
# param_copy_rewritten_in_loop
#
# A register that holds a parameter on entry to a loop that rewrites it reads as the register inside the loop.
#
# `r2 = param1; do { r4.push(r2); r2 = getParent(r2) } while (r2)`: the push and the call read `r2`, which is
# `param1` on the first turn only. `resolve_get_by_argument`, `resolve_call_argument` and
# `resolve_condition_argument` inlined the parameter's name without the loop check `get_register_reference` has
# (96/1822 `traverseTwoPhase$1`, 96/2158 `captureCommitPhaseError`: `r11 = param2.tag` for `r10.tag`).
# ----------------------------------------------------------------------------------------------------

def test_the_loop_reads_the_register_not_the_parameter():
    hasm = (_DATA / "param_copy_rewritten_in_loop_96_1822.hasm").read_text(encoding="utf-8")
    out = Decompiler.render(Decompiler.build_context(hasm, 1822, strict=False), verbose=False, raw=False)

    assert "r3 = r4.push(r2);" in out
    assert re.search(r"r2 = .*\(undefined, r2\);", out)
    assert "(param1);" not in out.split("do {")[1].split("} while")[0]
    assert "r4.push(param1)" not in out


# ----------------------------------------------------------------------------------------------------
# param_rewritten_in_loop
#
# A register that holds a parameter on entry is not the parameter once a loop rewrites it (F-175).
#
# `LoadParam r11, 2` makes a read of `r11` print as `param2`, and that holds for as long as nothing writes `r11`
# again. 96/4846 `binarySubdivide` ends its body with `Mov r11, r15; Mov r10, r14` and reads both at the top of the
# next iteration, so `r0 = param3 - param2` was only right on the first one. A register written again inside a
# loop that holds the read keeps its name; the `LoadParam` line prints, and the later writes mean something.
#
#     96/4846  `binarySubdivide`
# ----------------------------------------------------------------------------------------------------

def _render_13(name: str, function_id: int) -> str:
    hasm = (_DATA / name).read_text(encoding="utf-8")
    out = Decompiler.render(Decompiler.build_context(hasm, function_id, strict=False), verbose=False, raw=False)

    return "\n".join(line for line in out.split("\n") if not line.strip().startswith("//"))


def test_the_loop_reads_the_registers_it_rewrites():
    out = _render_13("loop_carried_arm_copy_96_4846.hasm", 4846)

    assert "r11 = param2;" in out
    assert "r10 = param3;" in out
    assert "r0 = r10 - r11;" in out
    assert "r11 = r15;" in out
    assert "param3 - param2" not in out


def test_a_member_read_before_the_loop_and_rewritten_in_it_keeps_its_register():
    """F-176: the same hazard for a property read. `r11 = q.memoizedState` before a loop whose body ends
    `Mov r11, r3` is the reducer's running state, not `q.memoizedState` again (98/2738 `useState`)."""
    out = _render_13("member_rewritten_in_loop_98_2738.hasm", 2738)

    assert "r13 = r11;" in out
    assert "r13 = r7.memoizedState;" not in out


def test_a_chain_walk_reads_the_register_it_advances():
    """96/12564 `getNavigateAction`: `r8.initial = ...; r8 = r8.params` walks a chain; the write went to
    `r6.params.initial` on every turn."""
    out = _render_13("member_rewritten_in_loop_96_12564.hasm", 12564)

    assert "r8.initial = r10;" in out
    assert "r6.params.initial = r10;" not in out


# ----------------------------------------------------------------------------------------------------
# parameter_copy_rewritten_by_the_loop
#
# A copy of a parameter that the loop rewrites is read as the register, not as the parameter (98/8694 `saveSnapshot`).
#
# `Mov r2, r1` (the parameter) before the loop, `r2 = r6.parentElement` at the bottom of the body, `Mov r6, r2` and
# `r2.scrollTop` at the top. The copy kept the parameter's name for every read, so each iteration read `param1` again
# and the loop never advanced (`r6 = param1`, 98/9777 `reconcileChildFibersImpl`: `r21 = param2`).
# ----------------------------------------------------------------------------------------------------

def _render_14() -> str:
    hasm = (_DATA / "parameter_copy_rewritten_by_the_loop_98_8694.hasm").read_text(encoding="utf-8")

    return Decompiler.render(Decompiler.build_context(hasm, 0, strict=False), verbose=False, raw=False)


def test_the_loop_reads_the_register():
    out = _render_14()

    assert "r2 = param1;" in out
    assert "r7 = r2.scrollTop;" in out
    assert "r6 = r2;" in out
    assert "r6 = param1;" not in out


@pytest.mark.skipif(shutil.which("node") is None, reason="node is not installed")
def test_the_output_parses_2(tmp_path: Path):
    path = tmp_path / "out.js"
    path.write_text(_render_14(), encoding="utf-8")

    done = subprocess.run(["node", "--check", str(path)], capture_output=True, text=True)

    assert done.returncode == 0, done.stderr


# ----------------------------------------------------------------------------------------------------
# loop_guard_reads_the_moved_initializer
#
# `Mov r2, param1; if (null !== r2) { for (r2 = param1; null !== r2; ...) }` (loop inversion): the copy moves into the
# `for` header and the guard in front of the loop kept reading `r2`, which nothing assigned before it
# (`if (null !== r2)`). The guard reads the initializer's value (96/1957 `findFirstSuspended`, 96/1872, 98/2541).
# ----------------------------------------------------------------------------------------------------


def _render_loop_guard() -> str:
    hasm = (_DATA / "loop_guard_reads_the_moved_initializer_96_1957.hasm").read_text(encoding="utf-8")

    return Decompiler.render(Decompiler.build_context(hasm, 0, strict=False), verbose=False, raw=False)


def test_the_guard_reads_the_parameter_the_loop_starts_from():
    out = _render_loop_guard()

    assert "if (null !== param1) {" in out
    assert "for (i = param1; null !== i;" in out
    assert "r2" not in out.split("for (")[0]


# ----------------------------------------------------------------------------------------------------
# switch_discriminant_on_the_loop_register
#
# The `for` induction register is renamed to i/j/k last; the `switch` discriminant read it (`switch (r6.tag)`) and kept
# the old name (96/2111, 2112, 2615, 2616, 98/2642, 2643).
# ----------------------------------------------------------------------------------------------------


def test_the_switch_discriminant_follows_the_induction_rename():
    hasm = (_DATA / "switch_discriminant_on_the_loop_register_96_2111.hasm").read_text(encoding="utf-8")
    out = Decompiler.render(Decompiler.build_context(hasm, 0, strict=False), verbose=False, raw=False)

    assert "switch (i.tag) {" in out
    assert "r6.tag" not in out
