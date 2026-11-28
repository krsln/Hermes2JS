"""`&&`/`||` chains: crossed tests, copies, short-circuit setups, constant tests.

Merged from: test_and_chain_before_a_loop_handler, test_boolean_chain_copy_reads_register, test_boolean_chain_keeps_arm_writes, test_copy_test_fold, test_crossed_and_whose_setup_copy_is_already_substituted, test_crossed_and_whose_setup_repeats_the_copies_before_the_first_test, test_crossed_condition_constants, test_crossed_guards_join_register, test_crossed_guards_shared_exit, test_crossed_or_of_three_tag_tests_inside_a_loop, test_crossed_or_with_call_read_by_the_body, test_crossed_or_with_setup_overwritten_by_a_dead_copy, test_crossed_test_behind_a_copy_the_exits_overwrite, test_dead_copy_cycle_in_a_test_chain, test_decided_test_threading, test_doubled_operand, test_or_chain_shared_target, test_or_copy_overwritten_in_next_test, test_or_of_call_result_and_links_with_constants_on_the_jump_edges, test_or_of_calls_with_receiver_copy, test_or_of_two_length_tests_with_copies_in_try_function, test_or_with_private_key_copy, test_retested_constant, test_short_circuit_copied_load, test_short_circuit_env_load, test_short_circuit_pure_setup, test_short_circuit_reloaded_register, test_short_circuit_setup_liveness, test_sibling_or_condition, test_test_constant_sink.
"""

import importlib
import re
from pathlib import Path

from hermes_decompiler.Decompiler import Decompiler


# ----------------------------------------------------------------------------------------------------
# and_chain_before_a_loop_handler
#
# An `&&` chain with a `?:` value, in a function whose only handler guards a later `for-of` (96/12624).
#
# `const p = "params" in o && typeof o.params === "object" && o.params ? o.params : {}` before a `for (const k of keys)`:
# the three tests jump to the `{}` arm. Folding the second test's setup into the first test drops its writes, and
# `_fold_pure_setup` refused that in any function with an exception handler (the handler may read what the try body
# had set). The `for-of` handler guards the loop only and reads the iterator, which `IteratorBegin` sets after the
# tests, so it does not see those registers. The printed tail was a miscompile: the not-an-object path ran the
# `o.params` arm.
# ----------------------------------------------------------------------------------------------------

_DATA = Path(__file__).parent / "data"


def _render(name, index):
    hasm = (_DATA / name).read_text(encoding="utf-8")

    return Decompiler.render(Decompiler.build_context(hasm, index, strict=False), verbose=False, raw=False)


def test_the_value_tests_become_one_condition_with_an_else():
    out = _render("and_chain_value_ternary_96_12624.hasm", 12624)

    assert "goto label" not in out
    assert 'if ("params" in r2 && typeof r2.params === "object" && r4.params) {\n        r2 = r4;\n        r1 = r2.params;\n    } else {\n        r1 = {  };\n    }' in out


# ----------------------------------------------------------------------------------------------------
# boolean_chain_copy_reads_register
#
# A copy of a boolean chain that the code after the `if` holds reads the register
# the chain printed into, it does not repeat the chain (`isArrayish`, 96/12935):
#
#     r3 = f(x, r3); if (r3) { r3 = a !== b }; r2 = r3; r1 = r2; r0 = r1
#
# `BooleanChainRegionPass` repointed the `Mov` copies of the arm's value to the
# whole folded chain. The chain is printed as `r3 = f(x, r3) && ...`, so the copy
# called `f` a second time and read `r3` (and the callee's own register) after
# that statement had replaced them: `r0 = r5(param1, r3) && ...`.
# ----------------------------------------------------------------------------------------------------

_IS_ARRAYISH = r"""

=> [Function #12935 "isArrayish" of 156 bytes]: 2 params, frame size=17, strict=0, exc handler=0, debug info=0  @ offset 0x0023301c

Bytecode listing:

==> 00000000: <LoadParam>: <Reg8: 4, UInt8: 1>
==> 00000003: <JmpFalseLong>: <Addr32: 149, Reg8: 4>  # Address: 00000098
==> 00000009: <TypeOf>: <Reg8: 1, Reg8: 4>
==> 0000000c: <LoadConstString>: <Reg8: 0, string_id: 7961>  # String: 'string' (Identifier)
==> 00000010: <JStrictEqualLong>: <Addr32: 136, Reg8: 1, Reg8: 0>  # Address: 00000098
==> 00000017: <GetGlobalObject>: <Reg8: 3>
==> 00000019: <TryGetById>: <Reg8: 0, Reg8: 3, UInt8: 1, string_id: 6>  # String: 'Array' (Identifier)
==> 0000001f: <InstanceOf>: <Reg8: 0, Reg8: 4, Reg8: 0>
==> 00000023: <JmpTrue>: <Addr8: 19, Reg8: 0>  # Address: 00000036
==> 00000026: <TryGetById>: <Reg8: 2, Reg8: 3, UInt8: 1, string_id: 6>  # String: 'Array' (Identifier)
==> 0000002c: <GetByIdShort>: <Reg8: 1, Reg8: 2, UInt8: 2, string_id: 5>  # String: 'isArray' (Identifier)
==> 00000031: <Call2>: <Reg8: 0, Reg8: 1, Reg8: 2, Reg8: 4>
==> 00000036: <JmpTrue>: <Addr8: 96, Reg8: 0>  # Address: 00000096
==> 00000039: <GetByIdShort>: <Reg8: 2, Reg8: 4, UInt8: 3, string_id: 169>  # String: 'length' (Identifier)
==> 0000003e: <LoadConstZero>: <Reg8: 1>
==> 00000040: <GreaterEq>: <Reg8: 1, Reg8: 2, Reg8: 1>
==> 00000044: <JmpFalse>: <Addr8: 79, Reg8: 1>  # Address: 00000093
==> 00000047: <GetById>: <Reg8: 5, Reg8: 4, UInt8: 4, string_id: 13199>  # String: 'splice' (Identifier)
==> 0000004d: <TryGetById>: <Reg8: 2, Reg8: 3, UInt8: 5, string_id: 7500>  # String: 'Function' (Identifier)
==> 00000053: <InstanceOf>: <Reg8: 2, Reg8: 5, Reg8: 2>
==> 00000057: <JmpTrue>: <Addr8: 57, Reg8: 2>  # Address: 00000090
==> 0000005a: <TryGetById>: <Reg8: 6, Reg8: 3, UInt8: 6, string_id: 24>  # String: 'Object' (Identifier)
==> 00000060: <GetByIdShort>: <Reg8: 5, Reg8: 6, UInt8: 7, string_id: 150>  # String: 'getOwnPropertyDescriptor' (Identifier)
==> 00000065: <GetByIdShort>: <Reg8: 7, Reg8: 4, UInt8: 3, string_id: 169>  # String: 'length' (Identifier)
==> 0000006a: <LoadConstUInt8>: <Reg8: 3, UInt8: 1>
==> 0000006d: <Sub>: <Reg8: 3, Reg8: 7, Reg8: 3>
==> 00000071: <Call3>: <Reg8: 3, Reg8: 5, Reg8: 6, Reg8: 4, Reg8: 3>
==> 00000077: <JmpFalse>: <Addr8: 22, Reg8: 3>  # Address: 0000008d
==> 0000007a: <GetById>: <Reg8: 4, Reg8: 4, UInt8: 8, string_id: 9124>  # String: 'constructor' (Identifier)
==> 00000080: <GetByIdShort>: <Reg8: 5, Reg8: 4, UInt8: 9, string_id: 176>  # String: 'name' (Identifier)
==> 00000085: <LoadConstString>: <Reg8: 4, string_id: 34>  # String: 'String' (Identifier)
==> 00000089: <StrictNeq>: <Reg8: 3, Reg8: 5, Reg8: 4>
==> 0000008d: <Mov>: <Reg8: 2, Reg8: 3>
==> 00000090: <Mov>: <Reg8: 1, Reg8: 2>
==> 00000093: <Mov>: <Reg8: 0, Reg8: 1>
==> 00000096: <Ret>: <Reg8: 0>
==> 00000098: <LoadConstFalse>: <Reg8: 0>
==> 0000009a: <Ret>: <Reg8: 0>
"""


def _render_2(hasm: str, function_id: int) -> str:
    context = Decompiler.build_context(hasm, function_id, strict=False)

    return Decompiler.render(context, verbose=False, raw=False)


def test_chain_with_a_call_is_not_repeated_in_the_copy_after_the_if():
    js = _render_2(_IS_ARRAYISH, 12935)

    assert js.count("Object.getOwnPropertyDescriptor(") == 1
    assert not re.search(r"\br5\(", js)
    # The copy chain is `r0 = r1` (`Mov r0, r1`), r1 being the `length >= 0`
    # result on the path that skips the chain (`r0 = r3` read the global
    # object there: r3 was never written on that path).
    assert re.search(r"\br0 = r1;", js)
    assert not re.search(r"\br0 = r3;", js)


def test_every_path_into_the_merge_reads_the_register_it_wrote():
    """96/12935, the path where `splice instanceof Function` holds: `Mov r1, r2`
    after `r2 = splice instanceof Function` (that path) / `r2 = r3` (the chain
    path). The copy read `r3` (the global object there), and `r1 = len >= 0`,
    which the `if`'s own test inlined, was not assigned for `length < 0`."""
    js = _render_2(_IS_ARRAYISH, 12935)

    assert re.search(r"\br2 = param1\.splice instanceof Function;", js)
    assert re.search(r"\br2 = r3;", js)
    assert re.search(r"\br1 = r2;", js)
    assert re.search(r"\br1 = param1\.length >= 0;", js)
    assert not re.search(r"\br1 = r3;", js)


def test_a_ternary_copy_after_its_test_register_was_overwritten_reads_the_register():
    """96/9349 `cmp`: two ternaries in a row test the same register
    (`r3 = typeof a; r1 = r3 !== "object" ? a : a.version; r3 = typeof b; ...`),
    and `return r1 === r0` read a COPY of the first one that now tested the
    SECOND `typeof` (F-118). The reader reads the register the first ternary
    assigns; a reader that stands where its test still holds keeps the copy."""
    from pathlib import Path

    hasm = (Path(__file__).parent / "data" / "sequential_ternaries_96_9349.hasm").read_text(encoding="utf-8")
    js = _render_2(hasm, 9349)

    assert 'r1 = r3 !== "object" ? param1 : param1.version;' in js
    assert 'return r1 === (r3 !== "object" ? param3 : param3.version);' in js
    assert 'param1.version) ===' not in js


def test_a_write_folded_into_its_readers_does_not_make_the_ternary_copy_stale():
    """96/8499 `callGuardDEV`: `r3 = stack ?? ""` is merged by a `Mov r3, r1` that
    is folded into its readers (never printed). It is not a redefinition of the
    `r3` the second ternary's test names, so the readers keep the copy
    (`r17 = (r3 != null) ? caughtException.stack : ""`) instead of the register
    `r1`, which the NEXT merge overwrites."""
    from pathlib import Path

    hasm = (Path(__file__).parent / "data" / "merge_copy_after_absorbed_write_96_8499.hasm").read_text(
        encoding="utf-8")
    js = _render_2(hasm, 8499)

    assert 'r17 = r3 != null ? caughtException.stack : "";' in js
    assert 'r16 = r2 != null ? caughtException.name : "WorkletsError";' in js
    assert "r17 = r1;" not in js


# ----------------------------------------------------------------------------------------------------
# boolean_chain_keeps_arm_writes
#
# A value-producing `||` chain is folded away together with its arm. A write to
# ANOTHER register inside that arm (`r8 = r18`) goes with it, and code after
# the `if` that holds the arm's value inline (`StoreToEnvironment r8`) would
# then claim it on the path that skips the arm (98/4563, the iterator
# destructuring's `done` flag):
#
#     r8 = undefined;  if (!done) { r8 = r18; ... }  env[1] = r8
# ----------------------------------------------------------------------------------------------------

_ANALYSIS = importlib.import_module("hermes_decompiler.backend.runtime.HermesAnalysis")

_HASM = r"""
=> [Function #4563 "useWindowDimensions" of 125 bytes]: 1 params, frame size=20, strict=1, exc handler=0, debug info=0  @ offset 0x001a5143

Bytecode listing:

==> 00000000: <GetParentEnvironment>: <Reg8: 3, UInt8: 0>
==> 00000003: <LoadFromEnvironment>: <Reg8: 5, Reg8: 3, UInt8: 1>
==> 00000007: <GetByIdShort>: <Reg8: 4, Reg8: 5, UInt8: 0, string_id: 251>  # String: 'useState' (Identifier)
==> 0000000c: <LoadConstUndefined>: <Reg8: 1>
==> 0000000e: <CreateClosure>: <Reg8: 3, Reg8: 3, function_id: 10363>  # Function: [#10363  of 28 bytes]: 1 params @ offset 0x00216947
==> 00000013: <Call2>: <Reg8: 3, Reg8: 4, Reg8: 1, Reg8: 3>
==> 00000018: <Mov>: <Reg8: 8, Reg8: 3>
==> 0000001b: <IteratorBegin>: <Reg8: 6, Reg8: 8>
==> 0000001e: <Mov>: <Reg8: 3, Reg8: 8>
==> 00000021: <IteratorNext>: <Reg8: 4, Reg8: 6, Reg8: 3>
==> 00000025: <Mov>: <Reg8: 3, Reg8: 6>
==> 00000028: <StrictEq>: <Reg8: 0, Reg8: 3, Reg8: 1>
==> 0000002c: <LoadConstUndefined>: <Reg8: 3>
==> 0000002e: <JmpTrue>: <Addr8: 6, Reg8: 0>  # Address: 00000034
==> 00000031: <Mov>: <Reg8: 3, Reg8: 4>
==> 00000034: <CreateFunctionEnvironment>: <Reg8: 4, UInt8: 2>
==> 00000037: <StoreToEnvironment>: <Reg8: 4, UInt8: 0, Reg8: 3>
==> 0000003b: <LoadConstUndefined>: <Reg8: 7>
==> 0000003d: <JmpTrue>: <Addr8: 28, Reg8: 0>  # Address: 00000059
==> 00000040: <IteratorNext>: <Reg8: 8, Reg8: 6, Reg8: 8>
==> 00000044: <Mov>: <Reg8: 9, Reg8: 6>
==> 00000047: <StrictEq>: <Reg8: 2, Reg8: 9, Reg8: 1>
==> 0000004b: <LoadConstUndefined>: <Reg8: 7>
==> 0000004d: <Mov>: <Reg8: 0, Reg8: 2>
==> 00000050: <JmpTrue>: <Addr8: 9, Reg8: 2>  # Address: 00000059
==> 00000053: <Mov>: <Reg8: 7, Reg8: 8>
==> 00000056: <Mov>: <Reg8: 0, Reg8: 2>
==> 00000059: <StoreToEnvironment>: <Reg8: 4, UInt8: 1, Reg8: 7>
==> 0000005d: <JmpTrue>: <Addr8: 6, Reg8: 0>  # Address: 00000063
==> 00000060: <IteratorClose>: <Reg8: 6, UInt8: 0>
==> 00000063: <GetByIdShort>: <Reg8: 6, Reg8: 5, UInt8: 1, string_id: 249>  # String: 'useEffect' (Identifier)
==> 00000068: <NewArray>: <Reg8: 5, UInt16: 1>
==> 0000006c: <DefineOwnInDenseArray>: <Reg8: 5, Reg8: 3, UInt8: 0>
==> 00000070: <CreateClosure>: <Reg8: 4, Reg8: 4, function_id: 10364>  # Function: [#10364  of 142 bytes]: 1 params @ offset 0x00216963
==> 00000075: <Call3>: <Reg8: 4, Reg8: 6, Reg8: 1, Reg8: 4, Reg8: 5>
==> 0000007b: <Ret>: <Reg8: 3>
"""


def test_arm_write_read_after_the_if_is_not_folded_away(monkeypatch):
    # The destructuring pass now turns this input into one pattern (F-236); the subject here is the fold,
    # which still meets this shape in an iterator state machine that is left open-coded, so keep it that way.
    monkeypatch.setattr(_ANALYSIS, "ArrayDestructuringCfgPass", lambda cfg: type("Off", (), {"run": lambda self: 0})())

    js = Decompiler.render(Decompiler.build_context(_HASM, 4563, strict=False), verbose=False, raw=False)
    code = "\n".join(line for line in js.splitlines() if not line.strip().startswith("//"))

    assert "||" not in code
    assert "r7 = r8;" in code
    assert "__environment__[1] = r7;" in code


# ----------------------------------------------------------------------------------------------------
# copy_test_fold
#
# Two tests that copy their operand into one register fold into `a || b` (F-225, 98/11466).
#
#     r12 = r18; r18 = r13; if (r18) goto BODY;  r18 = r12; if (r18) goto BODY;  <else arm>
#
# The second block is a copy and its branch. A copy is not folded in general (the exits may read the register through
# another register's inlined value), but here the test before it reads the same register, so the copy exists to be
# tested; it took `_fold_pure_setup` out of the pair and left `if (r18) goto L` in the `else` arm of a `for...of` body.
# ----------------------------------------------------------------------------------------------------

def test_the_two_tests_of_one_register_are_one_condition():
    hasm = (_DATA / "dead_mov_raw_branch_98_11466.hasm").read_text(encoding="utf-8")
    out = Decompiler.render(Decompiler.build_context(hasm, 11466, strict=False), verbose=False, raw=False)
    code = "\n".join(line for line in out.split("\n") if not line.strip().startswith("//"))

    assert "goto" not in code
    assert "r12 = r18;\n        r18 = r13;\n        if (r18 || r12) {" in code


# ----------------------------------------------------------------------------------------------------
# crossed_and_whose_setup_copy_is_already_substituted
#
# `if (0 !== (x & 261930) && 0 !== (y & 42)) { ... } else { count = 0 }` kept a `goto` (F-263 sampling, 96/2153).
#
#     r1 = f.pendingLanes; r5 = r7 & 261930; if (0 === r5) goto ZERO;
#     r7 = r1; r5 = 42; r5 = r7 & r5; if (0 !== r5) goto NESTED; ZERO: count = 0 ...
#
# The second test's setup holds a copy (`r7 = r1`) that an earlier link of the same setup already substituted into the test
# (`r1 & 42`); the copy is dead on both exits, but the fold only accepted a copy the test still mentioned once, so the crossed
# `&&` was refused and the nested `if` printed `if (0 !== r5) goto label_505;`.
# ----------------------------------------------------------------------------------------------------

def test_the_two_tests_are_one_condition_without_a_goto():
    hasm = (_DATA / "crossed_and_after_dead_copy_setup_96_2153.hasm").read_text(encoding="utf-8")
    out = Decompiler.render(Decompiler.build_context(hasm, 2153, strict=False), verbose=False, raw=False)

    assert "if (0 !== r5 && 0 !== (r1 & 42)) {" in out
    assert "goto label_" not in out


def test_a_copy_into_the_value_register_of_a_ternary_keeps_the_chain_apart():
    """96/13916 `listener`: `typeof e === "object" && e != null && "message" in e ? e.message : e`; the copy `r6 = e` of the
    last test is one arm's value (both arms write r6): folding it half folded the chain and left a `goto`."""
    listener = (_DATA / "ternary_value_register_copy_96_13916.hasm").read_text(encoding="utf-8")
    out = Decompiler.render(Decompiler.build_context(listener, 13916, strict=False), verbose=False, raw=False)

    assert "goto label_" not in out


# ----------------------------------------------------------------------------------------------------
# crossed_and_whose_setup_repeats_the_copies_before_the_first_test
#
# `if (r9 && !(r26 === "after" && r7 && r6)) { arm }` kept `if (r6) goto label_N;` (98/4238 `computeWindowedRenderLimits`).
#
#     r0 = r3; r28 = r18; if (!r9) goto JOIN;
#     if (r26 !== "after") goto ARM; if (!r7) goto ARM;
#     r0 = r3; r28 = r18; if (r6) goto JOIN; ARM: ...
#
# The second test repeats the copies the path already made, with nothing written in between; they were treated as copies for
# the edge into JOIN (a loop latch, where no edge block may go), so the crossed `&&` was refused. A copy the path already made
# is simply dropped.
# ----------------------------------------------------------------------------------------------------

def test_the_three_tests_are_one_condition_without_a_goto():
    hasm = (_DATA / "crossed_and_after_repeated_copies_98_4238.hasm").read_text(encoding="utf-8")
    out = Decompiler.render(Decompiler.build_context(hasm, 4238, strict=False), verbose=False, raw=False)

    assert 'if (r9 && (r26 !== "after" || !r7 || !r6)) {' in out
    assert "goto label_" not in out


# ----------------------------------------------------------------------------------------------------
# crossed_condition_constants
#
# F-10 (non-return targets): `if (!a || b) { A } END` where the second test's setup
# loads a constant that END reads too.
#
#     96/9112  `parseTranslateX`: `len !== 1` jumps to `r0 = []`, `isLength(x) ||
#              isPercent(x)` jumps to the object build, which indexes with the very
#              register (`r1 = 0`) the tests loaded. The tests take the constant and
#              END gets its own load on the edge into it, so the whole thing is one
#              `if (len === 1 && (a || b)) { ... } else { r0 = [] }`.
#     96/4063  `handler`: `if (c === -1 && this.n !== 0)` then `if (c === -1)`; the
#              crossed form read an unassigned register for `this.n !== 0`.
# ----------------------------------------------------------------------------------------------------

def _render_3(name: str, function_id: int) -> str:
    hasm = (_DATA / name).read_text(encoding="utf-8")
    out = Decompiler.render(Decompiler.build_context(hasm, function_id, strict=False), verbose=False, raw=False)

    return "\n".join(line for line in out.split("\n") if not line.strip().startswith("//"))


def test_a_constant_both_tests_and_the_end_block_read_is_loaded_again_for_the_end_block():
    out = _render_3("crossed_condition_with_constant_96_9112.hasm", 9112)

    assert "goto" not in out
    assert (
        "if (r1 === 1 && (getEnvironment(0)[0].call(undefined, param1[0]) || "
        "getEnvironment(0)[1].call(undefined, param1[0]))) {"
    ) in out
    # END indexes with the register the load wrote, so the load is there.
    assert out.index("r1 = 0;") < out.index("param1[r1]")
    assert "} else {\n        r0 = [];" in out


def test_the_second_exit_of_a_crossed_pair_reads_the_property_not_a_dead_register():
    out = _render_3("crossed_condition_two_exits_96_4063.hasm", 4063)

    assert "if (param2 === -1 && this.utf8BytesNeeded !== 0) {" in out
    assert "} else if (param2 === -1) {" in out
    assert "r5 !== 0" not in out


# ----------------------------------------------------------------------------------------------------
# crossed_guards_join_register
#
# Crossed guards whose first test is skipped by a register join (98/2044):
#
#     if (typeof a === "undefined") goto NULL;
#     r14 = a;  if (typeof r14 === "object") goto END;
#     NULL: r14 = null;
#     END: use(r14)
#
# `r14 = a` is one arm of the join with `r14 = null`. Folding the two tests into
# one condition must not delete it with the second test's block, or the reader
# is left with `null` on the path that should see `a`.
# ----------------------------------------------------------------------------------------------------

_HASM_2 = r"""
=> [Function #2044 "join" of 40 bytes]: 2 params, frame size=3, strict=1, exc handler=0, debug info=0  @ offset 0x0015c6da

Bytecode listing:

==> 00000000: <LoadParam>: <Reg8: 1, UInt8: 1>
==> 00000003: <JmpTypeOfIs>: <Addr32: 19, Reg8: 1, UInt16: 1>  # Address: 00000016
==> 0000000b: <Mov>: <Reg8: 0, Reg8: 1>
==> 0000000e: <JmpTypeOfIs>: <Addr32: 10, Reg8: 0, UInt16: 495>  # Address: 00000018
==> 00000016: <LoadConstNull>: <Reg8: 0>
==> 00000018: <Ret>: <Reg8: 0>
"""


def test_join_write_removed_with_the_second_test_is_kept():
    js = Decompiler.render(Decompiler.build_context(_HASM_2, 2044, strict=False), verbose=False, raw=False)
    code = "\n".join(line for line in js.splitlines() if not line.strip().startswith("//"))

    assert "param1" in code.split("return", 1)[0] or "r0 = param1" in code
    assert "return null;" not in code


# ----------------------------------------------------------------------------------------------------
# crossed_guards_shared_exit
#
# Two guards that cross over a shared exit (98/11871):
#
#     if (!unit)  goto L;  if (unit !== "px") goto EXIT;  L: if (n < 0) goto EXIT;  return n;  EXIT: return null;
#
# The first test jumps into the middle of the second one's arm, so the pair is
# not a plain `||` chain. It is merged into one condition (`!a || b`) instead of
# being left as a `goto`, and neither exit may be dropped on the way.
# ----------------------------------------------------------------------------------------------------

_HASM_3 = r"""
=> [Function #11871 "reactNativeReanimated_filterTs2" of 38 bytes]: 2 params, frame size=5, strict=1, exc handler=0, debug info=0  @ offset 0x00231082

Bytecode listing:

==> 00000000: <LoadParam>: <Reg8: 3, UInt8: 1>
==> 00000003: <GetById>: <Reg8: 2, Reg8: 3, UInt8: 0, string_id: 12994>  # String: 'numberValue' (Identifier)
==> 00000009: <GetById>: <Reg8: 4, Reg8: 3, UInt8: 1, string_id: 7977>  # String: 'unit' (Identifier)
==> 0000000f: <JmpFalse>: <Addr8: 11, Reg8: 4>  # Address: 0000001a
==> 00000012: <LoadConstString>: <Reg8: 3, string_id: 307>  # String: 'px' (String)
==> 00000016: <JStrictNotEqual>: <Addr8: 12, Reg8: 4, Reg8: 3>  # Address: 00000022
==> 0000001a: <LoadConstZero>: <Reg8: 0>
==> 0000001c: <JLess>: <Addr8: 6, Reg8: 2, Reg8: 0>  # Address: 00000022
==> 00000020: <Ret>: <Reg8: 2>
==> 00000022: <LoadConstNull>: <Reg8: 1>
==> 00000024: <Ret>: <Reg8: 1>
"""


def test_crossed_guards_sharing_an_exit_have_no_goto_and_keep_both_exits():
    js = Decompiler.render(Decompiler.build_context(_HASM_3, 11871, strict=False), verbose=False, raw=False)
    code = "\n".join(line for line in js.splitlines() if not line.strip().startswith("//"))

    assert "goto" not in code
    assert "return r2;" in code
    assert "return null;" in code
    # both guards still reach the `null` exit
    assert 'r4 !== "px"' in code
    assert "r2 < 0" in code or "r2 >= 0" in code


# ----------------------------------------------------------------------------------------------------
# crossed_or_of_three_tag_tests_inside_a_loop
#
# `if (0 === t || 11 === t || 15 === t) { ... }` inside a `while (true)` (F-217, 98/2658).
#
#     if (0 === t) goto A; if (11 === t) goto A; if (15 !== t) goto END; A: ...
#
# The tests of a `case`-looking chain stay apart inside a loop, and a loop block's test is never folded; but here the last
# test falls into the first one's target (no `switch` has a body entered by a later test's fall-through) and no target of the
# tests leaves the loop, so they are one `||`. Left apart, the output was `if (0 === t || 11 === t) { ... } else {
# if (15 !== t) goto label_147; }`, a `goto` out of the `try`.
# ----------------------------------------------------------------------------------------------------

def test_the_three_tag_tests_are_one_condition_without_a_goto():
    hasm = (_DATA / "crossed_or_of_case_tests_in_loop_98_2658.hasm").read_text(encoding="utf-8")
    out = Decompiler.render(Decompiler.build_context(hasm, 2658, strict=False), verbose=False, raw=False)

    assert "0 === r10 || (11 === r10 || 15 === r10)" in out
    assert "goto label_" not in out


# ----------------------------------------------------------------------------------------------------
# crossed_or_with_call_read_by_the_body
#
# A crossed `||` whose second test is a call the body reads again stays one condition (F-273).
#
# `if (a == null || (r19 = f(x)) == null) { scalar } else { recursion(r19) }` compiles to a first test that jumps
# to the second test's fall-through; the second test's call result is read again on the way to the `else`
# (96/1561 `accumulateDifferences`). The call stays in the condition as an assignment; the register copy
# `r22 = r19` that only the test reads is dropped (the exits copy `r22` on into `r1`, which nobody reads).
# ----------------------------------------------------------------------------------------------------

def test_the_second_call_is_part_of_the_condition_and_its_result_is_kept():
    hasm = (_DATA / "crossed_or_with_call_read_by_the_body_96_1561.hasm").read_text(encoding="utf-8")
    out = Decompiler.render(Decompiler.build_context(hasm, 1561, strict=False), verbose=False, raw=False)

    assert "goto" not in out
    assert "if (r20 != null && (r19 = " in out
    assert "r30 = r19;" in out


# ----------------------------------------------------------------------------------------------------
# crossed_or_with_setup_overwritten_by_a_dead_copy
#
# A crossed `||` whose second test's setup is overwritten by a dead copy stays one condition (F-275).
#
# `if (typeof c.diff === "function" || typeof c.process === "function") { body }` compiles to a second test block
# `r19 = c.process; r22 = typeof r19; r19 = r20` (the last write is a loop-carried copy nobody reads) that jumps to END
# and falls into the shared body; the exits read `r19`, which the block overwrites, so the fold refused the setup and the
# second test stayed a `goto` (96/2339 `restoreDeletedValuesInNestedArray`).
# ----------------------------------------------------------------------------------------------------

def test_the_second_typeof_test_joins_the_first_with_or():
    hasm = (_DATA / "crossed_or_with_overwritten_setup_96_2339.hasm").read_text(encoding="utf-8")
    out = Decompiler.render(Decompiler.build_context(hasm, 2339, strict=False), verbose=False, raw=False)

    assert "goto" not in out
    assert '|| "function" === typeof r18.process' in out


# ----------------------------------------------------------------------------------------------------
# crossed_test_behind_a_copy_the_exits_overwrite
#
# `if (typeof v === "object") { r12 = r9; if (r12 !== null) goto B } A` kept two `goto`s (98/5401 `parse`).
#
# The second test of the crossed pair reads a copy `r12 = r9` that both exits overwrite before reading (`A` and `B` start
# with `r12 = r9` again), but the fold only took a copy when an effect in the pair was read by END (`relaxed`). A copy
# that global liveness shows dead on both exits is folded in every crossed pair: `typeof v === "object" && v !== null`.
# ----------------------------------------------------------------------------------------------------

def test_the_copy_is_folded_into_the_second_test():
    hasm = (_DATA / "crossed_test_after_a_dead_copy_98_5401.hasm").read_text(encoding="utf-8")
    out = Decompiler.render(Decompiler.build_context(hasm, 0, strict=False), verbose=False, raw=False)

    assert "goto label_" not in out
    assert 'typeof r12 === "object" && r9 !== null' in out or 'typeof r12 === "object" && (r9 !== null)' in out


# ----------------------------------------------------------------------------------------------------
# dead_copy_cycle_in_a_test_chain
#
# A loop-carried cycle of copies does not keep `&&` from folding, and the folded `if` keeps its tail (96/12510).
#
# `r11 = r3` (setup of the second test) only feeds `r6 = r11` -> `r3 = r6` -> `r11 = r3`, a cycle nothing
# reads before it is written again, so `if (A) { if (B) { call; if (r11) return } }` is one test. Once it is one
# test the arm's guard `if (r11) return r2` is already a loop exit, and the arm still runs on into the code after the
# `if` (the `r7 = r5 + 1` step); before the structurer knew that, the tail landed in an `else`.
# ----------------------------------------------------------------------------------------------------

def _render_4(name, index):
    hasm = (_DATA / name).read_text(encoding="utf-8")
    out = Decompiler.render(Decompiler.build_context(hasm, index, strict=False), verbose=False, raw=False)

    return "\n".join(line for line in out.split("\n") if not line.strip().startswith("//"))


def test_the_tests_fold_and_the_tail_follows_the_if():
    code = _render_4("dead_copy_cycle_and_loop_guard_96_12510.hasm", 12510)

    assert "goto" not in code
    # F-273: the call whose result END reads stays in the test as an assignment.
    assert "if (r12.notFound && r10.notFound && (r2 = r8[1].call(undefined, r12, r10))) {\n                                return r2;" in code
    assert "} else {\n                                r2 =" not in code
    assert "r7 = r5 + 1;" in code


def test_an_arm_with_a_stripped_guard_runs_into_the_target():
    code = _render_4("arm_with_stripped_guard_runs_into_target_96_2148.hasm", 2148)

    # the target is reached by `param2` and by a null sibling: it follows the `if`
    assert "if (!param2) {" in code
    assert "} else {" not in code.split("if (!param2) {")[1].split("} while")[0]
    assert code.index("r2[143] = r9;") > code.index("if (!param2) {")


# ----------------------------------------------------------------------------------------------------
# decided_test_threading
#
# A register test the way in already decided is skipped (98/8193 `compareIdentifiers`, 96/9366).
#
# `if (/\d/.test(a) && ...)` style flags: `r10 = re.test(a); r11 = re.test(b)`, then a chain of
# `if (!r10) goto B; r1 = -1; if (!r11) goto END; B: if (!r11) goto C; r3 = 1; if (!r10) goto E; C: ...`.
# The tail copy of the shared tail (rung 6) gives the fall-through its own run of blocks, and its second test of
# `r10` can only go one way. `DecidedTestThreadingCfgPass` replaces such a test with the jump it must take; before
# it, both functions kept `if (!r10) goto label_119;`.
#
# A test is left alone when dropping its dead side would leave a reader holding the dropped arm's value
# (`shared_tail_region_copy_98_8193.hasm`, see `test_shared_tail_region_copy_values.py`).
# ----------------------------------------------------------------------------------------------------

def test_98_8193_has_no_goto_and_keeps_every_path():
    out = _render("decided_test_threading_98_8193.hasm", 8193)

    assert "goto label" not in out
    # r10 true: r11 false -> -1, r11 true -> the comparison; r10 false: r11 true -> 1
    assert "r1 = !r11 ? -1 : r8 >= r9 ? 1 : -1;" in out
    assert "                } else {\n                    r3 = 1;\n                }\n                r1 = r3;" in out


def test_96_9366_has_no_goto_and_keeps_every_path():
    out = _render("decided_test_threading_96_9366.hasm", 9366)

    assert "goto label" not in out
    assert "                r3 = -1;\n                if (r4) {" in out
    assert "r3 = !r6 ? 1 : -1;" in out


# ----------------------------------------------------------------------------------------------------
# doubled_operand
#
# A source expression that occurs twice does not double its head in a chain (F-151).
#
# `a || b` appearing in two statements folds twice, and the second fold's structural match found the first
# fold's right operand and wrapped it again: `x = a || (a || b)`. For an operand without effects the repeat adds
# nothing, so a repoint that builds `A op (A op B)` leaves `A op B`.
#
#     98/2487   `recordTouchMove`: `previousTimeStamp = t || (t || (t || u))`
#     98/12615  `close`: `!this._closeRequested && (!this._closeRequested && ...)`
# ----------------------------------------------------------------------------------------------------

def _render_5(name: str, function_id: int) -> str:
    hasm = (_DATA / name).read_text(encoding="utf-8")
    out = Decompiler.render(Decompiler.build_context(hasm, function_id, strict=False), verbose=False, raw=False)

    return "\n".join(line for line in out.split("\n") if not line.strip().startswith("//"))


def test_a_repeated_or_head_is_dropped():
    out = _render_5("doubled_operand_98_2487.hasm", 2487)

    assert "param1.timeStamp || param1.timestamp" in out
    assert "param1.timeStamp || (param1.timeStamp" not in out


def test_a_repeated_and_head_is_dropped():
    out = _render_5("doubled_operand_98_12615.hasm", 12615)

    assert '!this._closeRequested && "readable" === r4._state' in out
    assert "(!this._closeRequested &&" not in out


# ----------------------------------------------------------------------------------------------------
# or_chain_shared_target
#
# An `||` of two tests whose second jumps away, with a constant the join reads set in between (96/474).
#
# `typeof D === "function" || typeof D === "object"` guards a block that sets `r2 = false` itself and runs a `try`;
# the second test block also loads `r2 = false` for the join (`if (r2)` after both paths). The crossed fold of
# `ShortCircuitConditionCfgPass` moves such a constant onto the edge into the join, but refused a function with an
# exception handler or a join with other ways in; both only matter when the test, the join or the arm lie inside a
# protected range. The printed `if (c) goto label;` jumped to the very code below it.
# ----------------------------------------------------------------------------------------------------

def test_the_two_tests_become_one_condition_with_an_else():
    out = _render("or_chain_shared_target_96_474.hasm", 474)

    assert "goto label" not in out
    assert 'if ("function" !== r2 && "object" !== typeof r4) {\n        r2 = false;\n    } else {' in out


# ----------------------------------------------------------------------------------------------------
# or_copy_overwritten_in_next_test
#
# A copy that the next test overwrites before reading does not keep `&&` from folding (96/1998 `updateActionStateImpl`).
#
# `r6 = 'function'` in the following test rewrites the register the folded setup copy wrote, so the copy is private to
# the block that reads it; the scan used to treat the later write as a reader and left a goto.
# ----------------------------------------------------------------------------------------------------

def test_the_type_guard_is_one_condition():
    hasm = (_DATA / "or_copy_overwritten_in_next_test_96_1998.hasm").read_text(encoding="utf-8")
    out = Decompiler.render(Decompiler.build_context(hasm, 1998, strict=False), verbose=False, raw=False)

    assert "goto label" not in out
    assert 'if ("object" === r5 && null !== r4 && "function" === typeof r4.then) {' in out


# ----------------------------------------------------------------------------------------------------
# or_of_call_result_and_links_with_constants_on_the_jump_edges
#
# `(f1(x) && a(x) > 0) || (f2(x) && b(x) > 0) || h(x) > 0` as a condition kept `r0 = true; if (c) goto J;` (96/155 `Pe`).
#
# The bytecode loads `true` into the join's register before each `&&` link's jump and `J` tests that register
# (`if (!r0)`), while the last link sets it to its own comparison. The constant edge goes straight to the decided side of
# `J` (`ConstantEdgeThreadingCfgPass`) and the three links fold into one `||` condition, calls in evaluation order.
# ----------------------------------------------------------------------------------------------------

def test_the_three_links_are_one_condition():
    hasm = (_DATA / "call_result_and_chain_with_constant_edges_96_155.hasm").read_text(encoding="utf-8")
    out = Decompiler.render(Decompiler.build_context(hasm, 155, strict=False), verbose=False, raw=False)

    assert "goto label_" not in out
    assert out.count("||") == 2
    assert "[115].call(undefined, param1) > 0)" in out


# ----------------------------------------------------------------------------------------------------
# or_of_calls_with_receiver_copy
#
# `a.includes("x") || a.includes("y")` behind receiver copies folds into one test (98/12172).
#
#     r12 = r10; r11 = r12.includes("translate"); if (r11) goto T;
#     r12 = r10; r11 = r12.includes("perspective"); if (!r11) goto PLAIN;
#     T: typeof r9 === "number" ...
#
# The second block's `r12 = r10` only feeds the receiver of its one call, so `_fold_pure_setup` takes `r10` for
# it; before, the copy kept the crossed `||` from folding and the function printed three `goto`s.
# ----------------------------------------------------------------------------------------------------

def test_the_or_of_two_calls_is_one_condition():
    hasm = (_DATA / "or_of_calls_with_receiver_copy_98_12172.hasm").read_text(encoding="utf-8")
    out = Decompiler.render(Decompiler.build_context(hasm, 12172, strict=False), verbose=False, raw=False)

    assert "goto label" not in out
    # Since F-297 the receiver copy is folded away on every crossed pair, so both tests and the `typeof` check make
    # one `if`.
    assert 'if ((r11 || r10.includes("perspective")) && typeof r9 === "number") {' in out


# ----------------------------------------------------------------------------------------------------
# or_of_two_length_tests_with_copies_in_try_function
#
# `a === x.length || b === y.length` whose second test re-copies the registers of the first (F-263, 98/2474).
#
#     r9 = r5; r8 = r7.length; if (r9 === r8) goto BODY; r9 = r12; r8 = r11.length; if (r9 !== r8) goto END; BODY:
#
# The `Mov r9 <- r12` copy of the second test is dead once the test is over, on both exits and in the
# `finally` handler, but the fold only trusted the copies a loop-free, handler-free function showed to be dead, so the
# `||` stayed a `goto label_573`. Folding it changes the layout of the loop behind it, and the break of a loop test whose
# block holds only copies (`r8 = r12` ahead of `if (!(0 <= r8)) break;`) shadowed that block's address: the first
# test then guarded the copy alone and the break ran on its own, outside it.
# ----------------------------------------------------------------------------------------------------

def _render_6() -> str:
    hasm = (_DATA / "loop_latch_inside_if_98_2474.hasm").read_text(encoding="utf-8")

    return Decompiler.render(Decompiler.build_context(hasm, 2474, strict=False), verbose=False, raw=False)


def test_the_or_of_the_two_length_tests_is_one_condition():
    out = _render_6()

    assert "if (r9 === r8 || r12 === r11.length) {" in out
    assert "goto label_573" not in out


def test_the_first_test_of_the_loop_guards_the_whole_body():
    out = _render_6()

    assert not re.search(r"if \(1 <= r8\) \{\s*r8 = r12;\s*\}", out)
    assert re.search(r"if \(1 <= r8\) \{\s*r8 = r12;\s*if \(!\(0 <= r8\)\) \{\s*break;", out)


# ----------------------------------------------------------------------------------------------------
# or_with_private_key_copy
#
# A copy only the second test reads no longer keeps `||` from folding (96/9613 `getNormalizedCSSTransitionConfigUpdates`).
#
#     for (key of keys) {
#         if (!(a.settings[key] && deepEqual(a.settings[key], b.settings[key]))) { r0.settings = b.settings; break; }
#     }
#
# compiles to `if (!r8) goto BREAK; ...; r11 = r7; ... r8[r11] ... r8[r11]; r8 = call; if (r8) goto CONTINUE; BREAK:`.
# The key copy `r11 = r7` is read twice by the test and by nothing else, so `_fold_pure_setup` folds it; before, the
# `||` stayed two blocks and the loop printed `if (r8) goto label_326; continue;`.
# ----------------------------------------------------------------------------------------------------

def test_the_break_condition_is_one_test():
    hasm = (_DATA / "or_with_private_key_copy_96_9613.hasm").read_text(encoding="utf-8")
    out = Decompiler.render(Decompiler.build_context(hasm, 9613, strict=False), verbose=False, raw=False)

    assert "goto label" not in out
    assert "if (!(r8 && r2[4].deepEqual.call(undefined, param1.settings[r7], param2.settings[r7]))) {" in out
    assert "r9.settings = r8;\n                break;" in out


# ----------------------------------------------------------------------------------------------------
# retested_constant
#
# A test the arm repeats on a recomputed value is not a `case` label (F-181).
#
#     if (0 !== r6) goto T;                 // T: the code after the `if`
#     if (a) { ...; r6 = f(); if (0 === r6) return x; }  falls into T
#     T: ...
#
# The branch compares a value with a constant, which `_DominanceIfBuilder` left to the `switch` builders: the
# arm's own test of the SAME constant, reached by falling into `T`, never made `T` the join. `T` was printed in
# the `if (0 !== r6) {..}` arm only, so the path of the second test that runs `T` returned `null` instead
# (`goto label_269`, a `return` printed nowhere).
#
#     98/2618  `bailoutOnAlreadyFinishedWork`
#     96/141   `fe`
# ----------------------------------------------------------------------------------------------------

def _render_7(name: str, function_id: int) -> str:
    hasm = (_DATA / name).read_text(encoding="utf-8")
    out = Decompiler.render(Decompiler.build_context(hasm, function_id, strict=False), verbose=False, raw=False)

    return "\n".join(line for line in out.split("\n") if not line.strip().startswith("//"))


def test_the_rest_follows_the_if_of_the_retested_value():
    out = _render_7("retested_constant_98_2618.hasm", 2618)

    assert "goto" not in out
    assert "if (0 === r6) {\n                return null;\n            }" in out
    # the code both tests reach is printed once, after the outer `if`
    assert out.count("Resuming work not yet implemented.") == 1
    assert out.index("if (0 === r6) {") < out.index("Resuming work not yet implemented.")
    assert "if (0 !== r6)" not in out


def test_a_second_function_of_the_shape_has_no_goto():
    out = _render_7("retested_constant_96_141.hasm", 141)

    assert "goto" not in out


# ----------------------------------------------------------------------------------------------------
# short_circuit_copied_load
#
# A later test of an `||`/`&&` chain whose setup copies a register and loads from the copy (F-216, 98/11306).
#
#     for (const item of items) { if (!item || item.type !== "menu" || !item.menu) continue; ... }
#
# Each test after the first sets its operand up with `r9 = r8; r9 = r9.type`. The fold of a test's pure setup into the
# condition refused every `Mov`, so the later tests stayed behind the first one as `goto`s to the loop's `continue`.
# A copy whose register the same block writes again is not seen by anything outside the block: `r9 = r8; r9 = r9.type`
# reads `r8.type`, and the fold takes it when the register is dead on both exits, as for any other pure load.
# ----------------------------------------------------------------------------------------------------

def test_the_tests_of_the_chain_are_one_condition():
    hasm = (_DATA / "short_circuit_copied_load_98_11306.hasm").read_text(encoding="utf-8")
    out = Decompiler.render(Decompiler.build_context(hasm, 11306, strict=False), verbose=False, raw=False)
    code = "\n".join(line for line in out.split("\n") if not line.strip().startswith("//"))

    assert "goto" not in code
    assert 'if (r9 && r8.type === "menu" && r8.menu) {' in code


# ----------------------------------------------------------------------------------------------------
# short_circuit_env_load
#
# `a || b` whose second test reads a register END reads too (F-203).
#
#     if (c1) goto A;  r10 = env[296];  if (r10 !== 0) goto END;  A: ...chain...;  jmp JOIN;   END: r8 = r10 & -r10
#
# The crossed fold takes the pure setup of the second test into the condition only when the register is dead
# afterwards; END reads it. A constant load got its own copy on the edge into END (96/1139); an environment slot is
# the same (nothing between the test and END writes it), so the test reads `r9[296]` itself and END reloads it:
#
#     if (0 !== r0 && 0 !== r9[296]) { r10 = r9[296]; r8 = r10 & -r10 } else { ...chain... }
#
# 98/2654 `requestUpdateLane` kept `if (0 !== r10) goto label_226` before.
# ----------------------------------------------------------------------------------------------------

def _render_8(name: str, function_id: int) -> str:
    hasm = (_DATA / name).read_text(encoding="utf-8")
    out = Decompiler.render(Decompiler.build_context(hasm, function_id, strict=False), verbose=False, raw=False)

    return "\n".join(line for line in out.split("\n") if not line.strip().startswith("//"))


def test_a_test_behind_an_environment_load_that_the_end_reads_is_one_condition():
    out = _render_8("short_circuit_env_load_98_2654.hasm", 2654)

    assert "goto" not in out
    assert "if (0 !== r0 && 0 !== r9[296]) {\n            r10 = r9[296];\n            r8 = r10 & -r10;" in out


# ----------------------------------------------------------------------------------------------------
# short_circuit_pure_setup
#
# A value test with a pure setup load in front of its second condition
# (`loop`, 96/5242, the default of a destructured parameter):
#
#     A: JNotGreater  len, 1  -> NEW          # taken: no argument at all
#     B: r0 = arguments[1]; JStrictNotEqual r0, undefined -> USE
#     NEW: r0 = {}                            # reached from A (taken) AND B (fall-through)
#     USE: r0 = arguments[1]
#
# `NEW` has two predecessors, the crossed `!a || b` shape, but `ShortCircuitCondition
# CfgPass` only accepted a setup block made of constants the condition had already
# inlined. `B`'s `GetArgumentsPropByVal` is a pure value that both exits overwrite,
# so it is substituted into the test and the two blocks become one condition.
# Before, the function printed `if (r0 !== undefined) goto label_26;`.
# ----------------------------------------------------------------------------------------------------

_LOOP = r"""

=> [Function #5242 "loop" of 45 bytes]: 2 params, frame size=4, strict=1, exc handler=0, debug info=0  @ offset 0x0017fffc

Bytecode listing:

==> 00000000: <LoadConstUndefined>: <Reg8: 3>
==> 00000002: <LoadConstUndefined>: <Reg8: 2>
==> 00000004: <GetArgumentsLength>: <Reg8: 0, Reg8: 2>
==> 00000007: <LoadConstUInt8>: <Reg8: 1, UInt8: 1>
==> 0000000a: <JNotGreater>: <Addr8: 12, Reg8: 0, Reg8: 1>  # Address: 00000016
==> 0000000e: <GetArgumentsPropByVal>: <Reg8: 0, Reg8: 1, Reg8: 2>
==> 00000012: <JStrictNotEqual>: <Addr8: 8, Reg8: 0, Reg8: 3>  # Address: 0000001a
==> 00000016: <NewObject>: <Reg8: 0>
==> 00000018: <Jmp>: <Addr8: 6>  # Address: 0000001e
==> 0000001a: <GetArgumentsPropByVal>: <Reg8: 0, Reg8: 1, Reg8: 2>
==> 0000001e: <GetById>: <Reg8: 0, Reg8: 0, UInt8: 1, string_id: 7391>  # String: 'iterations' (Identifier)
==> 00000024: <GetEnvironment>: <Reg8: 0, UInt8: 0>
==> 00000027: <LoadFromEnvironment>: <Reg8: 0, Reg8: 0, UInt8: 1>
==> 0000002b: <Ret>: <Reg8: 0>
"""


def test_pure_setup_in_front_of_the_second_test_is_folded():
    context = Decompiler.build_context(_LOOP, 5242, strict=False)
    js = Decompiler.render(context, verbose=False, raw=False)

    assert "goto" not in js
    assert "if (r0 > 1 && arguments[1] !== undefined) {" in js


# ----------------------------------------------------------------------------------------------------
# short_circuit_reloaded_register
#
# Two tests that load the same register again are not a `case` chain (F-244, 98/2621 `appendAllChildrenToContainer`).
#
#     r20 = r21.tag;           if (22 !== r20) goto CHILD
#     r20 = r21.memoizedState; if (null !== r20) goto HIDDEN       // else falls into CHILD
#     CHILD: ...
#
# The first test's target is the second one's fall-through: `22 !== tag || null === state` goes to CHILD (the crossed
# `||` fold). `_is_case_test` compared the subjects as expressions - both `r20` - and kept the tests apart as a
# `switch` chain although the second block writes `r20` again; the `||` stayed two raw branches and the function printed
# `goto label_146` (and ran the wrong arm).
# ----------------------------------------------------------------------------------------------------

def test_a_register_loaded_again_is_not_the_same_subject():
    hasm = (_DATA / "short_circuit_reloaded_register_98_2621.hasm").read_text(encoding="utf-8")
    out = Decompiler.render(Decompiler.build_context(hasm, 2621, strict=False), verbose=False, raw=False)

    assert "goto" not in out
    assert "if (22 === r20 && null !== r21.memoizedState) {" in out


# ----------------------------------------------------------------------------------------------------
# short_circuit_setup_liveness
#
# A pure setup load folded into the second test of a short-circuit pair
# (`ShortCircuitConditionCfgPass._fold_pure_setup`) is dropped with its block, so
# it is only exact when nothing reads what it wrote.
#
# - `getNavigateAction` (98/6009): the block `r7 = r4.type; r9 = "NAVIGATE"; if (r7 !==
#   "stack")` writes `r9`, which the code after the `if` reads (the `type` of the
#   action). Readers were inlined linearly, before control flow was known, so by
#   NAME the register looks dead; the bytecode operands say otherwise. Folding it
#   lost the whole `else { r9 = "NAVIGATE" }` arm and left `r9` unassigned.
# - `startTimespan` (96/3349): the folded `arguments[1] !== undefined` is the same
#   expression the `then` arm assigns to `r5`; a repair that repoints copies of
#   the arm's value must not rewrite the `if`'s OWN condition (it runs before the
#   arm), or the test reads `r5` before anything set it.
# ----------------------------------------------------------------------------------------------------

def _render_9(name: str, function_id: int) -> str:
    hasm = (_DATA / name).read_text(encoding="utf-8")
    out = Decompiler.render(Decompiler.build_context(hasm, function_id, strict=False), verbose=False, raw=False)

    return "\n".join(line for line in out.split("\n") if not line.strip().startswith("//"))


def test_register_read_after_the_pair_keeps_its_definition():
    out = _render_9("getNavigateAction_98_6009.hasm", 6009)

    # The write stays in the `else` arm, in front of the `stack` test (the shape changed with the larger tail
    # copy of F-217, which made the function goto-free: the test no longer fixes the indentation).
    assert re.search(r'\} else \{\n\s+r7 = r4\.type;\n\s+r9 = "NAVIGATE";\n\s+if \(r7 === "stack"\)', out)
    assert "goto" not in out


def test_if_condition_is_not_repointed_to_its_own_arms_register():
    out = _render_9("startTimespan_96_3349.hasm", 3349)

    assert "r4 > 1 && arguments[1] !== undefined" in out
    assert "r5 !== undefined" not in out


# ----------------------------------------------------------------------------------------------------
# sibling_or_condition
#
# A test in the else arm that jumps to the entry of the then arm is an `||` of the `if` (F-185).
#
#     if (A) { X } else { if (C) goto X; REST }          ->   if (A || C) { X } else { REST }
#
# The residual test is the FIRST thing of the else arm, nothing that prints stands in front of it, and its target is
# the entry of the then arm: `C` is only read when `A` failed, and both lead to `X`. The fold used to leave the jump
# (`_sits_in_sibling_arm`: it must stay when the target is in the sibling arm), which printed `goto label_75`.
#
# Not for a test behind a statement (96/12298 `populateParams`: `r2 = r1.length` stands in front of `r2 === 0`; moving
# the test up read `r2` before it was set) and not for a `case` chain (98/2541: the tests of one `revealOrder` keep
# being joined by `restore_dropped_case_jumps`).
#
#     98/7633  `resolveTransition`   98/3265 `dispatchEvent`   98/2541 `findFirstSuspended`
# ----------------------------------------------------------------------------------------------------

def _render_10(name: str, function_id: int) -> str:
    hasm = (_DATA / name).read_text(encoding="utf-8")
    out = Decompiler.render(Decompiler.build_context(hasm, function_id, strict=False), verbose=False, raw=False)

    return "\n".join(line for line in out.split("\n") if not line.strip().startswith("//"))


def test_the_second_test_joins_the_condition_of_the_arm_it_jumps_to():
    out = _render_10("sibling_or_condition_98_7633.hasm", 7633)

    assert "goto" not in out
    assert '} else if (param1 || typeof param2 !== "number") {' in out
    assert out.count("Prop \\\"fadeDuration\\\" is deprecated") == 1


def test_a_type_check_after_a_null_check_is_one_condition():
    out = _render_10("sibling_or_condition_98_3265.hasm", 3265)

    # One `||` and one `throw` (it was one per test while a function with a `for-of` handler kept the fold off).
    assert "goto" not in out
    assert 'if (param1 == null || typeof param1.type !== "string") {\n        throw new TypeError(' in out


def test_tests_of_one_value_read_again_each_time_are_one_condition():
    out = _render_10("sibling_or_condition_98_2541.hasm", 2541)

    # `r7` is the tag in the first test and `memoizedProps.revealOrder` in the next four: the program reads the
    # property again for every test, and that is what the condition says (F-244; it was a nest of `else` arms with
    # the loads repeated in front of every one before).
    assert "goto" not in out
    assert '"unstable_legacy-backwards" === r6.memoizedProps.revealOrder || "together" === r6.memoizedProps.revealOrder' in out


# ----------------------------------------------------------------------------------------------------
# test_constant_sink
#
# The constant a test loads for the join moves onto the edge that jumps there (F-190/F-227, 98/2304).
#
#     r5 = "focus";             if (p === 8)  goto L
#     r5 = "windowStateChange"; if (p === 32) goto L
#     r5 = "click";             if (p === 1)  goto L
#     r5 = "viewHoverEnter";    if (p === 128) goto L
#     <report, return>
#     L: ... r5 ...
#
# The bytecode hoists each constant in front of its test. The first output kept a `goto` AND printed only the last
# constant at `L` (`sendAccessibilityEvent(r3, "viewHoverEnter")`); with the load on the taken edge the tests become
# a `switch` and `L` reads the register.
# ----------------------------------------------------------------------------------------------------

def _render_11() -> str:
    hasm = (_DATA / "test_constant_sink_98_2304.hasm").read_text(encoding="utf-8")
    out = Decompiler.render(Decompiler.build_context(hasm, 2304, strict=False), verbose=False, raw=False)
    return "\n".join(line for line in out.split("\n") if not line.strip().startswith("//"))


def test_each_test_assigns_its_own_constant():
    code = _render_11()

    assert "goto" not in code
    for constant in ("focus", "windowStateChange", "click", "viewHoverEnter"):
        assert f'r5 = "{constant}";' in code


def test_the_join_reads_the_register_not_one_constant():
    code = _render_11()

    assert "sendAccessibilityEvent(r3, r5)" in code
    assert 'sendAccessibilityEvent(r3, "' not in code
