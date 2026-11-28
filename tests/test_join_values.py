"""Registers merged at a join: copies, folds, defaults, merged tests.

Merged from: test_computed_join_copy, test_constant_register_copies_thread_to_a_lone_return, test_dead_mov_raw_branch, test_dead_register_copy, test_default_parameter_merge, test_join_copy_read_after_the_register_is_rewritten, test_join_read_keeps_folded_copy, test_join_value_condition, test_join_value_mov_read, test_merge_alias_readers, test_merge_value_register, test_merged_test_with_return_copy, test_nested_join_copy, test_rematerialized_constant_two_writes, test_unfolded_merge_default.
"""

import re
import shutil
import subprocess
from pathlib import Path

import pytest

from hermes_decompiler.Decompiler import Decompiler
from hermes_decompiler.backend.transforms.cfg_passes.ShortCircuitConditionCfgPass import ShortCircuitConditionCfgPass


# ----------------------------------------------------------------------------------------------------
# computed_join_copy
#
# A computed value written on ONE arm must not be inlined into a copy read on another (F-138, 96/1801
# `getComponentNameFromType`).
#
# `r3` is last written (in address order) by the `ForwardRef(...)` arm, and every other arm ends in
# `Mov r1, r3` reading `param1`. The join guard in `get_register_expression` only covered a bare register
# alias, so the arm's string concatenation was inlined into each of them
# (`r1 = r2 + (r2.displayName || r1.name || "") + ")"`). A join of three or more paths now keeps the
# register for a binary expression too.
#
# Not fixed (still open under F-138):
# - inside the `ForwardRef` arm itself, `BooleanChainRegionPass` copies `r2.displayName || r1.name || ""`
#   into a test that stands after `r1`/`r2` were redefined, so two such lines remain;
# - the last `Mov r1, r3; Ret r1` of that arm is a join of two paths, which the guard deliberately leaves
#   to the ternary fold (widening it to two paths broke 17 other tests).
#
# Other value shapes keep inlining on purpose: a constant or an environment value would leave a read of a
# register that prints nowhere (`reject.call(r0, ...)`, 96/2999), and a member read is left to the ternary
# fold (`tests/test_default_parameter_merge.py`).
# ----------------------------------------------------------------------------------------------------

_DATA = Path(__file__).parent / "data"

_GARBAGE = 'r2 + (r2.displayName || r1.name || "") + ")"'


def _code() -> str:
    hasm = (_DATA / "computed_join_copy_96_1801.hasm").read_text(encoding="utf-8")

    return Decompiler.render(Decompiler.build_context(hasm, 1801, strict=False), verbose=False, raw=False)


def test_a_copy_on_another_arm_reads_the_register_not_the_forward_ref_string():
    code = _code()

    # Seven arms read it before the fix; only the two inside the `ForwardRef` arm are left.
    assert code.count(_GARBAGE) <= 2
    # Each such arm ends in `r1 = r3; return r1`, or in `return r3` once the shared closing `return` is
    # copied into the jumpers (F-10(b)); the value is the register either way.
    assert code.count("r1 = r3;") + code.count("return r3;") >= 4


# ----------------------------------------------------------------------------------------------------
# constant_register_copies_thread_to_a_lone_return
#
# `r0 = r4; if (c) goto J` with `J: if (r0) return r0` kept two `goto`s (98/5730 `sortRoutes`).
#
# `ConstantEdgeThreadingCfgPass` (F-289) only threaded a literal load; here the edge carries a COPY of a register that
# holds one constant for the whole function (`r4 = 1` before the loop), and the side `J` decides is a lone `return r0`.
# The constant is looked up through its single definition, and the edge gets a return block of its own that returns it.
# ----------------------------------------------------------------------------------------------------

def test_the_edge_returns_the_constant_without_a_goto():
    hasm = (_DATA / "ternary_values_through_a_constant_register_98_5730.hasm").read_text(encoding="utf-8")
    out = Decompiler.render(Decompiler.build_context(hasm, 0, strict=False), verbose=False, raw=False)

    assert "goto label_" not in out
    assert "return r0;" in out  # the join that still computes the value
    assert out.count("return 1;") >= 3
    assert "return r1;" in out


# ----------------------------------------------------------------------------------------------------
# dead_mov_raw_branch
#
# `DeadMovEliminationPass` counts the condition of a branch that stayed raw as a read (F-224, 98/11466).
#
#     r12 = r18; r18 = r13; if (r18) goto BODY;  r18 = r12; if (r18) goto BODY;  <else arm: r18 = r16 ...>
#
# A `goto` the structurers could not remove prints its own condition, but the pass only looked at statements and
# values: the copy `r18 = r12` right before the test looked unread (`r18` is written again further on), was dropped,
# and `if (r18) goto` tested the value of the first test instead of `r12`.
# ----------------------------------------------------------------------------------------------------

def test_a_raw_branch_keeps_the_copy_it_reads(monkeypatch: pytest.MonkeyPatch):
    # The fold of F-225 turns this shape into one condition; without it the branch stays raw.
    monkeypatch.setattr(ShortCircuitConditionCfgPass, "_copy_feeds_the_test", lambda *a, **k: False)
    hasm = (_DATA / "dead_mov_raw_branch_98_11466.hasm").read_text(encoding="utf-8")
    out = Decompiler.render(Decompiler.build_context(hasm, 11466, strict=False), verbose=False, raw=False)
    code = "\n".join(line for line in out.split("\n") if not line.strip().startswith("//"))

    # The jump is a `goto` or, once the last resort labels it (F-314), a `break label_N`: either way it reads the copy.
    assert re.search(r"r18 = r12;\n\s+if \(r18\) (goto|break) ", code)


# ----------------------------------------------------------------------------------------------------
# dead_register_copy
#
# A register copy that nothing reads is removed (F-31), on every path and not only when the
# register is overwritten later in the same sequence (`DeadMovEliminationPass`).
#
# - 96/1982 `checkIfSnapshotChanged`: `Mov r0, r2 (param1)` in front of a `try`, overwritten
#   before anything reads it (the sequential check cannot see past the `try`).
# - 96/12298 `populateParams`: `r1 = param2` in front of `if (!param2)` is dead; without it the
#   nested `else { if }` becomes an `else if` chain.
#
# What must stay:
# - a copy a tail-merged instruction reads (96/4939: `Mov r16, r18` was copied after the flow
#   snapshot, the original is gone) and a write to a parameter's register, whose reads print as
#   `paramN` (96/4846, `tests/test_shared_return_widened.py`).
# ----------------------------------------------------------------------------------------------------

def _code_2(name: str, function_id: int) -> str:
    hasm = (_DATA / name).read_text(encoding="utf-8")

    return Decompiler.render(Decompiler.build_context(hasm, function_id, strict=False), verbose=False, raw=False)


def test_a_copy_that_nothing_reads_is_removed():
    code = _code_2("dead_copy_unread_96_1982.hasm", 1982)

    assert "r0 = param1;" not in code
    assert "r0 = param1.value;" in code


def test_a_dead_copy_in_front_of_a_test_no_longer_nests_the_else():
    code = _code_2("dead_copy_chain_96_12298.hasm", 12298)

    # The three tests are one `||` now (the dead copy fed the middle one): no `else` nest and no copy.
    assert "goto" not in code
    assert "if (!param1 || !param2 || Object.keys(param2).length === 0) {" in code
    assert "r1 = param2;" not in code


def test_a_copy_read_by_a_tail_merged_instruction_stays():
    code = _code_2("dead_copy_goto_96_4939.hasm", 4939)

    assert "r18 = r23;" in code
    assert "r16 = r18;" in code


# ----------------------------------------------------------------------------------------------------
# default_parameter_merge
#
# A9: a value merged at an `if` is read after it.
#
# - `defaultParameterTest`: the inner ternary fold handed the `Add` after the outer
#   `if` a COPY of its value (`(r3 === undefined) ? 10 : arguments[1]`), so on the
#   path that skips the outer `if` the parameter default was never read - and
#   `r3` is not even assigned there. The reader has to name `r5`.
# - `shouldFilter`: `UnfoldedMergeRepairPass` repointed every structural copy of an
#   arm's `r4[0]`, including the definition `r4 = r4[0]` of another arm, which
#   became `r4 = r6`.
# ----------------------------------------------------------------------------------------------------

_DEFAULT_PARAMETER_HASM = """
=> [Function #15154 "defaultParameterTest" of 121 bytes]: 2 params, frame size=16, strict=1, exc handler=0, debug info=0  @ offset 0x0026aa9c

Bytecode listing:

==> 00000000: <LoadConstUndefined>: <Reg8: 0>
==> 00000002: <LoadConstUndefined>: <Reg8: 2>
==> 00000004: <GetArgumentsLength>: <Reg8: 3, Reg8: 2>
==> 00000007: <LoadConstUInt8>: <Reg8: 1, UInt8: 1>
==> 0000000a: <Greater>: <Reg8: 3, Reg8: 3, Reg8: 1>
==> 0000000e: <LoadConstUInt8>: <Reg8: 4, UInt8: 10>
==> 00000011: <Mov>: <Reg8: 5, Reg8: 4>
==> 00000014: <JmpFalse>: <Addr8: 18, Reg8: 3>  # Address: 00000026
==> 00000017: <GetArgumentsPropByVal>: <Reg8: 3, Reg8: 1, Reg8: 2>
==> 0000001b: <Mov>: <Reg8: 5, Reg8: 4>
==> 0000001e: <JStrictEqual>: <Addr8: 8, Reg8: 3, Reg8: 0>  # Address: 00000026
==> 00000022: <GetArgumentsPropByVal>: <Reg8: 5, Reg8: 1, Reg8: 2>
==> 00000026: <GetArgumentsLength>: <Reg8: 3, Reg8: 2>
==> 00000029: <LoadConstUInt8>: <Reg8: 1, UInt8: 2>
==> 0000002c: <Greater>: <Reg8: 3, Reg8: 3, Reg8: 1>
==> 00000030: <LoadConstString>: <Reg8: 6, string_id: 7363>  # String: 'result' (Identifier)
==> 00000034: <Mov>: <Reg8: 4, Reg8: 6>
==> 00000037: <JmpFalse>: <Addr8: 18, Reg8: 3>  # Address: 00000049
==> 0000003a: <GetArgumentsPropByVal>: <Reg8: 3, Reg8: 1, Reg8: 2>
==> 0000003e: <Mov>: <Reg8: 4, Reg8: 6>
==> 00000041: <JStrictEqual>: <Addr8: 8, Reg8: 3, Reg8: 0>  # Address: 00000049
==> 00000045: <GetArgumentsPropByVal>: <Reg8: 4, Reg8: 1, Reg8: 2>
==> 00000049: <GetGlobalObject>: <Reg8: 1>
==> 0000004b: <TryGetById>: <Reg8: 6, Reg8: 1, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
==> 00000051: <GetByIdShort>: <Reg8: 3, Reg8: 6, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
==> 00000056: <LoadConstString>: <Reg8: 2, string_id: 4772>  # String: '__BC:Functions/DefaultParameterTests/defaultParameterTest/start' (String)
==> 0000005a: <Call2>: <Reg8: 2, Reg8: 3, Reg8: 6, Reg8: 2>
==> 0000005f: <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
==> 00000065: <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
==> 0000006a: <LoadParam>: <Reg8: 1, UInt8: 1>
==> 0000006d: <Add>: <Reg8: 1, Reg8: 1, Reg8: 5>
==> 00000071: <Call3>: <Reg8: 1, Reg8: 2, Reg8: 3, Reg8: 4, Reg8: 1>
==> 00000077: <Ret>: <Reg8: 0>
"""

_SHOULD_FILTER_HASM = """
=> [Function #10752 "shouldFilter" of 101 bytes]: 2 params, frame size=17, strict=1, exc handler=0, debug info=0  @ offset 0x0021dd62

Bytecode listing:

==> 00000000: <GetParentEnvironment>: <Reg8: 4, UInt8: 0>
==> 00000003: <LoadParam>: <Reg8: 5, UInt8: 1>
==> 00000006: <LoadFromEnvironment>: <Reg8: 3, Reg8: 4, UInt8: 1>
==> 0000000a: <GetById>: <Reg8: 2, Reg8: 3, UInt8: 0, string_id: 13492>  # String: 'skipNull' (Identifier)
==> 00000010: <JmpFalse>: <Addr8: 52, Reg8: 2>  # Address: 00000044
==> 00000013: <GetParentEnvironment>: <Reg8: 6, UInt8: 1>
==> 00000016: <LoadFromEnvironment>: <Reg8: 7, Reg8: 6, UInt8: 5>
==> 0000001a: <LoadFromEnvironment>: <Reg8: 6, Reg8: 4, UInt8: 0>
==> 0000001e: <GetByVal>: <Reg8: 6, Reg8: 6, Reg8: 5>
==> 00000022: <JmpTypeOfIs>: <Addr32: 16, Reg8: 7, UInt16: 128>  # Address: 00000032
==> 0000002a: <LoadConstString>: <Reg8: 8, string_id: 4299>  # String: 'Trying to call a non-function' (String)
==> 0000002e: <CallBuiltin>: <Reg8: 7, UInt8: 44, UInt8: 2>  # Built-in function: [#44 throwTypeError]
==> 00000032: <LoadConstNull>: <Reg8: 0>
==> 00000034: <StrictEq>: <Reg8: 0, Reg8: 6, Reg8: 0>
==> 00000038: <JmpTrue>: <Addr8: 9, Reg8: 0>  # Address: 00000041
==> 0000003b: <LoadConstUndefined>: <Reg8: 1>
==> 0000003d: <StrictEq>: <Reg8: 0, Reg8: 6, Reg8: 1>
==> 00000041: <Mov>: <Reg8: 2, Reg8: 0>
==> 00000044: <JmpTrue>: <Addr8: 31, Reg8: 2>  # Address: 00000063
==> 00000047: <GetById>: <Reg8: 3, Reg8: 3, UInt8: 1, string_id: 15748>  # String: 'skipEmptyString' (Identifier)
==> 0000004d: <JmpFalse>: <Addr8: 19, Reg8: 3>  # Address: 00000060
==> 00000050: <LoadFromEnvironment>: <Reg8: 4, Reg8: 4, UInt8: 0>
==> 00000054: <GetByVal>: <Reg8: 5, Reg8: 4, Reg8: 5>
==> 00000058: <LoadConstString>: <Reg8: 4, string_id: 6457>  # String: '' (Identifier)
==> 0000005c: <StrictEq>: <Reg8: 3, Reg8: 5, Reg8: 4>
==> 00000060: <Mov>: <Reg8: 2, Reg8: 3>
==> 00000063: <Ret>: <Reg8: 2>
"""


def _code_3(hasm, function_id):
    out = Decompiler.render(Decompiler.build_context(hasm, function_id), verbose=False)
    return "\n".join(line for line in out.splitlines() if not line.strip().startswith("//"))


def test_reader_after_the_if_names_the_register_not_a_copy_of_the_folded_arm():
    code = _code_3(_DEFAULT_PARAMETER_HASM, 15154)

    assert "r1 = param1 + r5;" in code
    assert "r5 = r3 === undefined ? 10 : arguments[1];" in code
    assert "param1 + ((r3" not in code


def test_definition_with_the_same_value_is_not_repointed_to_another_arms_register():
    code = _code_3(_SHOULD_FILTER_HASM, 10752)

    assert "r4 = r4[0];" in code
    assert "r4 = r6;" not in code


# ----------------------------------------------------------------------------------------------------
# join_copy_read_after_the_register_is_rewritten
#
# A copy of a join value is read by the copy's own register once the join register holds something else (96/5569 `render`).
#
# `r7` holds the header flag (0 or 1, a join), `Mov r11, r7` copies it, then `IteratorBegin r7, ...` reuses `r7` for the
# iterator. The repair that names the join register for its readers also repointed the later `Mov r13, r11` to `r7`, so
# the loop read the iterator, and the `GetIterator` line stayed because `r7` was still read by name. The copy now reads
# `r11`, which prints as `r11 = r7`.
# ----------------------------------------------------------------------------------------------------

def _render() -> str:
    hasm = (_DATA / "join_copy_read_after_the_register_is_rewritten_96_5569.hasm").read_text(encoding="utf-8")

    return Decompiler.render(Decompiler.build_context(hasm, 5569, strict=False), verbose=False, raw=False)


def test_the_copy_is_read_by_its_own_register():
    out = _render()

    assert "r11 = r7;" in out
    assert "r13 = r11;" in out
    assert "r13 = r7;" not in out
    assert "GetIterator" not in out
    assert "for (let r13 of r10)" in out


@pytest.mark.skipif(shutil.which("node") is None, reason="node is not installed")
def test_the_output_parses(tmp_path: Path):
    path = tmp_path / "out.js"
    path.write_text(_render(), encoding="utf-8")

    done = subprocess.run(["node", "--check", str(path)], capture_output=True, text=True)

    assert done.returncode == 0, done.stderr


# ----------------------------------------------------------------------------------------------------
# join_read_keeps_folded_copy
#
# A copy that a test consumed and a later join reads by name (96/5371):
#
#     r0 = this.context;  if (!r0) goto END;  …  r0 = a === b;  END: return !!r0
#
# `r0 = this.context` is folded into the `if (this.context)` test, so nothing
# defined `r0` on the path that skipped the arm and `return !!r0` read an
# undefined register.
# ----------------------------------------------------------------------------------------------------

_HASM = r"""
=> [Function #5371 "_isNestedWithSameOrientation" of 69 bytes]: 1 params, frame size=13, strict=1, exc handler=0, debug info=0  @ offset 0x00183c7c

Bytecode listing:

==> 00000000: <LoadParam>: <Reg8: 2, UInt8: 0>
==> 00000003: <GetByIdShort>: <Reg8: 1, Reg8: 2, UInt8: 1, string_id: 101>  # String: 'context' (Identifier)
==> 00000008: <Mov>: <Reg8: 0, Reg8: 1>
==> 0000000b: <JmpFalse>: <Addr8: 50, Reg8: 0>  # Address: 0000003d
==> 0000000e: <GetById>: <Reg8: 1, Reg8: 1, UInt8: 2, string_id: 12155>  # String: 'horizontal' (Identifier)
==> 00000014: <Not>: <Reg8: 1, Reg8: 1>
==> 00000017: <GetEnvironment>: <Reg8: 3, UInt8: 1>
==> 0000001a: <LoadFromEnvironment>: <Reg8: 3, Reg8: 3, UInt8: 15>
==> 0000001e: <GetById>: <Reg8: 4, Reg8: 3, UInt8: 3, string_id: 16767>  # String: 'horizontalOrDefault' (Identifier)
==> 00000024: <GetByIdShort>: <Reg8: 2, Reg8: 2, UInt8: 4, string_id: 204>  # String: 'props' (Identifier)
==> 00000029: <GetById>: <Reg8: 3, Reg8: 2, UInt8: 2, string_id: 12155>  # String: 'horizontal' (Identifier)
==> 0000002f: <LoadConstUndefined>: <Reg8: 2>
==> 00000031: <Call2>: <Reg8: 2, Reg8: 4, Reg8: 2, Reg8: 3>
==> 00000036: <Not>: <Reg8: 1, Reg8: 1>
==> 00000039: <StrictEq>: <Reg8: 0, Reg8: 1, Reg8: 2>
==> 0000003d: <Not>: <Reg8: 0, Reg8: 0>
==> 00000040: <Not>: <Reg8: 0, Reg8: 0>
==> 00000043: <Ret>: <Reg8: 0>
"""


def test_copy_folded_into_a_test_is_still_defined_for_the_join_read():
    js = Decompiler.render(Decompiler.build_context(_HASM, 5371, strict=False), verbose=False, raw=False)
    code = "\n".join(line for line in js.splitlines() if not line.strip().startswith("//"))

    assert "r0 = this.context;" in code
    assert code.index("r0 = this.context;") < code.index("return !!r0;")


# ----------------------------------------------------------------------------------------------------
# join_value_condition
#
# A conditional jump right after a join reads the register's MERGED value
# (`r0 = a; if (!r0) r0 = b; if (!r0) r0 = c`), not the last arm's write.
#
# - the jump used to inline the arm's value, and a negated test (`JmpFalse`) is a new
#   expression no fold could repoint, so a three-operand `||` chain was left as a
#   broken pair of ternaries over a register nothing assigned;
# - `BooleanChainRegionPass` now recognises an `if (!rN)` that tests the register
#   it just built, and the folds' "is the register read by name later" check sees
#   the tests the structurers already moved into `IfRegion`s.
# ----------------------------------------------------------------------------------------------------

_PRESS_HANDLER_HASM = """
=> [Function #6283 "_hasPressHandler" of 75 bytes]: 1 params, frame size=4, strict=1, exc handler=0, debug info=0  @ offset 0x0019a07d

Bytecode listing:

==> 00000000: <LoadParam>: <Reg8: 1, UInt8: 0>
==> 00000003: <GetByIdShort>: <Reg8: 0, Reg8: 1, UInt8: 1, string_id: 204>  # String: 'props' (Identifier)
==> 00000008: <GetByIdShort>: <Reg8: 0, Reg8: 0, UInt8: 2, string_id: 129>  # String: 'onPress' (Identifier)
==> 0000000d: <LoadConstNull>: <Reg8: 2>
==> 0000000f: <Neq>: <Reg8: 0, Reg8: 0, Reg8: 2>
==> 00000013: <JmpTrue>: <Addr8: 18, Reg8: 0>  # Address: 00000025
==> 00000016: <GetByIdShort>: <Reg8: 3, Reg8: 1, UInt8: 1, string_id: 204>  # String: 'props' (Identifier)
==> 0000001b: <GetById>: <Reg8: 3, Reg8: 3, UInt8: 3, string_id: 9702>  # String: 'onPressIn' (Identifier)
==> 00000021: <Neq>: <Reg8: 0, Reg8: 3, Reg8: 2>
==> 00000025: <JmpTrue>: <Addr8: 18, Reg8: 0>  # Address: 00000037
==> 00000028: <GetByIdShort>: <Reg8: 3, Reg8: 1, UInt8: 1, string_id: 204>  # String: 'props' (Identifier)
==> 0000002d: <GetById>: <Reg8: 3, Reg8: 3, UInt8: 4, string_id: 14963>  # String: 'onPressOut' (Identifier)
==> 00000033: <Neq>: <Reg8: 0, Reg8: 3, Reg8: 2>
==> 00000037: <JmpTrue>: <Addr8: 18, Reg8: 0>  # Address: 00000049
==> 0000003a: <GetByIdShort>: <Reg8: 1, Reg8: 1, UInt8: 1, string_id: 204>  # String: 'props' (Identifier)
==> 0000003f: <GetById>: <Reg8: 1, Reg8: 1, UInt8: 5, string_id: 14414>  # String: 'onLongPress' (Identifier)
==> 00000045: <Neq>: <Reg8: 0, Reg8: 1, Reg8: 2>
==> 00000049: <Ret>: <Reg8: 0>
"""

_STRIP_BASE_URL_HASM = """
=> [Function #5896 "stripBaseUrl" of 131 bytes]: 2 params, frame size=17, strict=1, exc handler=0, debug info=0  @ offset 0x001be280

Bytecode listing:

==> 00000000: <LoadParam>: <Reg8: 5, UInt8: 2>
==> 00000003: <LoadConstUndefined>: <Reg8: 0>
==> 00000005: <JStrictNotEqual>: <Addr8: 8, Reg8: 5, Reg8: 0>  # Address: 0000000d
==> 00000009: <LoadConstString>: <Reg8: 5, string_id: 6457>  # String: '' (Identifier)
==> 0000000d: <LoadParam>: <Reg8: 6, UInt8: 1>
==> 00000010: <JmpTrue>: <Addr8: 5, Reg8: 5>  # Address: 00000015
==> 00000013: <Ret>: <Reg8: 6>
==> 00000015: <GetParentEnvironment>: <Reg8: 2, UInt8: 0>
==> 00000018: <GetByIdShort>: <Reg8: 4, Reg8: 6, UInt8: 0, string_id: 217>  # String: 'replace' (Identifier)
==> 0000001d: <LoadConstString>: <Reg8: 3, string_id: 503>  # String: '/' (String)
==> 00000021: <CreateRegExp>: <Reg8: 1, string_id: 1677, string_id: 6578, UInt32: 110>  # String: '^\\/+' (String)  # String: 'g' (Identifier)
==> 0000002f: <Call3>: <Reg8: 4, Reg8: 4, Reg8: 6, Reg8: 1, Reg8: 3>
==> 00000035: <GetByIdShort>: <Reg8: 3, Reg8: 4, UInt8: 0, string_id: 217>  # String: 'replace' (Identifier)
==> 0000003a: <GetGlobalObject>: <Reg8: 1>
==> 0000003c: <TryGetById>: <Reg8: 6, Reg8: 1, UInt8: 1, string_id: 29>  # String: 'RegExp' (Identifier)
==> 00000042: <LoadFromEnvironment>: <Reg8: 2, Reg8: 2, UInt8: 0>
==> 00000046: <GetByIdShort>: <Reg8: 2, Reg8: 2, UInt8: 2, string_id: 115>  # String: 'default' (Identifier)
==> 0000004b: <Call2>: <Reg8: 5, Reg8: 2, Reg8: 0, Reg8: 5>
==> 00000050: <TryGetById>: <Reg8: 1, Reg8: 1, UInt8: 3, string_id: 10>  # String: 'HermesInternal' (Identifier)
==> 00000056: <GetByIdShort>: <Reg8: 2, Reg8: 1, UInt8: 4, string_id: 105>  # String: 'concat' (Identifier)
==> 0000005b: <LoadConstString>: <Reg8: 1, string_id: 1206>  # String: '^\\/?' (String)
==> 0000005f: <Call2>: <Reg8: 8, Reg8: 2, Reg8: 1, Reg8: 5>
==> 00000064: <CreateThisForNew>: <Reg8: 5, Reg8: 6, UInt8: 5>
==> 00000068: <LoadConstString>: <Reg8: 7, string_id: 6578>  # String: 'g' (Identifier)
==> 0000006c: <Mov>: <Reg8: 9, Reg8: 5>
==> 0000006f: <Construct>: <Reg8: 1, Reg8: 6, UInt8: 3>
==> 00000073: <LoadConstString>: <Reg8: 2, string_id: 6457>  # String: '' (Identifier)
==> 00000077: <SelectObject>: <Reg8: 1, Reg8: 5, Reg8: 1>
==> 0000007b: <Call3>: <Reg8: 1, Reg8: 3, Reg8: 4, Reg8: 1, Reg8: 2>
==> 00000081: <Ret>: <Reg8: 1>
"""

_BOX_SHADOW_HASM = """
=> [Function #9040 "parseBoxShadowString" of 60 bytes]: 2 params, frame size=11, strict=1, exc handler=0, debug info=0  @ offset 0x001d3f8f

Bytecode listing:

==> 00000000: <LoadParam>: <Reg8: 2, UInt8: 1>
==> 00000003: <LoadConstString>: <Reg8: 0, string_id: 7424>  # String: 'none' (Identifier)
==> 00000007: <JStrictEqual>: <Addr8: 47, Reg8: 2, Reg8: 0>  # Address: 00000036
==> 0000000b: <GetByIdShort>: <Reg8: 1, Reg8: 2, UInt8: 1, string_id: 171>  # String: 'match' (Identifier)
==> 00000010: <GetEnvironment>: <Reg8: 0, UInt8: 0>
==> 00000013: <LoadFromEnvironment>: <Reg8: 0, Reg8: 0, UInt8: 0>
==> 00000017: <Call2>: <Reg8: 2, Reg8: 1, Reg8: 2, Reg8: 0>
==> 0000001c: <JmpTrue>: <Addr8: 7, Reg8: 2>  # Address: 00000023
==> 0000001f: <NewArray>: <Reg8: 2, UInt16: 0>
==> 00000023: <GetByIdShort>: <Reg8: 1, Reg8: 2, UInt8: 2, string_id: 170>  # String: 'map' (Identifier)
==> 00000028: <CreateEnvironment>: <Reg8: 0>
==> 0000002a: <CreateClosure>: <Reg8: 0, Reg8: 0, function_id: 9041>  # Function: [#9041  of 66 bytes]: 2 params @ offset 0x001d3fcb
==> 0000002f: <Call2>: <Reg8: 0, Reg8: 1, Reg8: 2, Reg8: 0>
==> 00000034: <Ret>: <Reg8: 0>
==> 00000036: <NewArray>: <Reg8: 0, UInt16: 0>
==> 0000003a: <Ret>: <Reg8: 0>
"""


def _code_4(hasm, function_id):
    out = Decompiler.render(Decompiler.build_context(hasm, function_id), verbose=False)
    return "\n".join(line for line in out.splitlines() if not line.strip().startswith("//"))


def test_three_operand_or_chain_folds_into_one_expression():
    # hermes-96 `_hasPressHandler`: onPress || onPressIn || onPressOut || onLongPress.
    code = _code_4(_PRESS_HANDLER_HASM, 6283)

    for prop in ("onPress", "onPressIn", "onPressOut", "onLongPress"):
        assert f".{prop} != null" in code

    assert code.count("||") == 3
    assert "?" not in code
    # every register the chain reads is one the output assigns
    assert "r3" not in code


def test_default_folded_into_a_ternary_keeps_its_register_for_the_branch():
    # hermes-98 `stripBaseUrl`: `r5 = param2 ?? ""` is tested by name right after.
    code = _code_4(_STRIP_BASE_URL_HASM, 5896)

    assert 'r5 = param2 !== undefined ? param2 : "";' in code
    assert code.index('r5 = param2 !== undefined ? param2 : "";') < code.index("if (r5) {")


def test_register_tested_fold_does_not_repoint_an_unrelated_identical_literal():
    # hermes-96 `parseBoxShadowString`: folding `r2 = match(..) || []` must not
    # rewrite the OTHER `[]` (`r0 = []` of the `"none"` arm) into the fold.
    code = _code_4(_BOX_SHADOW_HASM, 9040)

    assert "r2 = param1.match(r0) || [];" in code
    assert "r0 = [];" in code
    assert code.rstrip().endswith("return r0;\n}")


# ----------------------------------------------------------------------------------------------------
# join_value_mov_read
#
# A `Mov` that reads a join value reads the register (`retryTimedOutBoundary`,
# 98/2683):
#
#     r3 = 2; if (c) { r4 = ...; r3 = r4; if (d) { ...; r3 = r4 } }; Mov r8, r3
#
# The arm's `Mov r3, r4` is not printed (inlined), so the reader after the `if`
# held the arm's value (`r8 = r4`) and was wrong on the path that skips the arm.
# ----------------------------------------------------------------------------------------------------

_HASM_2 = """
=> [Function #2683 "retryTimedOutBoundary" of 261 bytes]: 3 params, frame size=20, strict=1, exc handler=0, debug info=0  @ offset 0x0017b781

Bytecode listing:

==> 00000000: <GetParentEnvironment>: <Reg8: 6, UInt8: 0>
==> 00000003: <LoadParam>: <Reg8: 9, UInt8: 1>
==> 00000006: <LoadParam>: <Reg8: 8, UInt8: 2>
==> 00000009: <LoadConstZero>: <Reg8: 2>
==> 0000000b: <JStrictNotEqual>: <Addr8: 68, Reg8: 2, Reg8: 8>  # Address: 0000004f
==> 0000000f: <GetByIdShort>: <Reg8: 7, Reg8: 9, UInt8: 0, string_id: 185>  # String: 'mode' (Identifier)
==> 00000014: <LoadConstUInt8>: <Reg8: 0, UInt8: 1>
==> 00000017: <BitAnd>: <Reg8: 1, Reg8: 7, Reg8: 0>
==> 0000001b: <LoadConstUInt8>: <Reg8: 3, UInt8: 2>
==> 0000001e: <JStrictEqual>: <Addr8: 46, Reg8: 2, Reg8: 1>  # Address: 0000004c
==> 00000022: <LoadFromEnvironment>: <Reg8: 4, Reg8: 6, UInt8: 91>
==> 00000026: <LShift>: <Reg8: 1, Reg8: 4, Reg8: 0>
==> 0000002a: <StoreNPToEnvironment>: <Reg8: 6, UInt8: 91, Reg8: 1>
==> 0000002e: <LoadConstInt>: <Reg8: 0, Imm32: 62914560>
==> 00000034: <BitAnd>: <Reg8: 0, Reg8: 1, Reg8: 0>
==> 00000038: <Mov>: <Reg8: 3, Reg8: 4>
==> 0000003b: <JStrictNotEqual>: <Addr8: 17, Reg8: 2, Reg8: 0>  # Address: 0000004c
==> 0000003f: <LoadConstInt>: <Reg8: 0, Imm32: 4194304>
==> 00000045: <StoreNPToEnvironment>: <Reg8: 6, UInt8: 91, Reg8: 0>
==> 00000049: <Mov>: <Reg8: 3, Reg8: 4>
==> 0000004c: <Mov>: <Reg8: 8, Reg8: 3>
==> 0000004f: <LoadFromEnvironment>: <Reg8: 7, Reg8: 6, UInt8: 162>
==> 00000053: <Call3>: <Reg8: 7, Reg8: 7, Reg8: 2, Reg8: 9, Reg8: 8>
==> 00000059: <LoadConstNull>: <Reg8: 3>
==> 0000005b: <JStrictEqualLong>: <Addr32: 166, Reg8: 3, Reg8: 7>  # Address: 00000101
==> 00000062: <GetById>: <Reg8: 9, Reg8: 7, UInt8: 1, string_id: 13574>  # String: 'pendingLanes' (Identifier)
==> 00000068: <BitOr>: <Reg8: 9, Reg8: 9, Reg8: 8>
==> 0000006c: <PutByIdStrict>: <Reg8: 7, Reg8: 9, UInt8: 0, string_id: 13574>  # String: 'pendingLanes' (Identifier)
==> 00000072: <LoadConstInt>: <Reg8: 0, Imm32: 268435456>
==> 00000078: <JStrictEqual>: <Addr8: 22, Reg8: 0, Reg8: 8>  # Address: 0000008e
==> 0000007c: <PutByIdStrict>: <Reg8: 7, Reg8: 2, UInt8: 1, string_id: 13523>  # String: 'suspendedLanes' (Identifier)
==> 00000082: <PutByIdStrict>: <Reg8: 7, Reg8: 2, UInt8: 2, string_id: 15552>  # String: 'pingedLanes' (Identifier)
==> 00000088: <PutByIdStrict>: <Reg8: 7, Reg8: 2, UInt8: 3, string_id: 9441>  # String: 'warmLanes' (Identifier)
==> 0000008e: <LoadFromEnvironment>: <Reg8: 8, Reg8: 6, UInt8: 125>
==> 00000092: <StrictNeq>: <Reg8: 4, Reg8: 7, Reg8: 8>
==> 00000096: <JmpFalse>: <Addr8: 12, Reg8: 4>  # Address: 000000a2
==> 00000099: <GetByIdShort>: <Reg8: 8, Reg8: 7, UInt8: 2, string_id: 62>  # String: 'next' (Identifier)
==> 0000009e: <StrictEq>: <Reg8: 4, Reg8: 3, Reg8: 8>
==> 000000a2: <JmpFalse>: <Addr8: 31, Reg8: 4>  # Address: 000000c1
==> 000000a5: <LoadFromEnvironment>: <Reg8: 8, Reg8: 6, UInt8: 125>
==> 000000a9: <JStrictEqual>: <Addr8: 16, Reg8: 3, Reg8: 8>  # Address: 000000b9
==> 000000ad: <PutByIdStrict>: <Reg8: 8, Reg8: 7, UInt8: 4, string_id: 62>  # String: 'next' (Identifier)
==> 000000b3: <StoreToEnvironment>: <Reg8: 6, UInt8: 125, Reg8: 7>
==> 000000b7: <Jmp>: <Addr8: 10>  # Address: 000000c1
==> 000000b9: <StoreToEnvironment>: <Reg8: 6, UInt8: 125, Reg8: 7>
==> 000000bd: <StoreToEnvironment>: <Reg8: 6, UInt8: 124, Reg8: 7>
==> 000000c1: <LoadConstTrue>: <Reg8: 3>
==> 000000c3: <StoreNPToEnvironment>: <Reg8: 6, UInt8: 127, Reg8: 3>
==> 000000c7: <LoadFromEnvironment>: <Reg8: 4, Reg8: 6, UInt8: 126>
==> 000000cb: <JmpTrue>: <Addr8: 54, Reg8: 4>  # Address: 00000101
==> 000000ce: <StoreNPToEnvironment>: <Reg8: 6, UInt8: 126, Reg8: 3>
==> 000000d2: <LoadFromEnvironmentL>: <Reg8: 3, Reg8: 6, UInt16: 389>
==> 000000d7: <JmpTrue>: <Addr8: 25, Reg8: 3>  # Address: 000000f0
==> 000000da: <LoadFromEnvironment>: <Reg8: 9, Reg8: 6, UInt8: 72>
==> 000000de: <LoadFromEnvironment>: <Reg8: 8, Reg8: 6, UInt8: 77>
==> 000000e2: <LoadFromEnvironment>: <Reg8: 7, Reg8: 6, UInt8: 132>
==> 000000e6: <LoadConstUndefined>: <Reg8: 3>
==> 000000e8: <Call3>: <Reg8: 7, Reg8: 9, Reg8: 3, Reg8: 8, Reg8: 7>
==> 000000ee: <Jmp>: <Addr8: 19>  # Address: 00000101
==> 000000f0: <LoadFromEnvironmentL>: <Reg8: 7, Reg8: 6, UInt16: 390>
==> 000000f5: <LoadConstUndefined>: <Reg8: 3>
==> 000000f7: <CreateClosure>: <Reg8: 6, Reg8: 6, function_id: 9765>  # Function: [#9765  of 222 bytes]: 1 params @ offset 0x002087d0
==> 000000fc: <Call2>: <Reg8: 6, Reg8: 7, Reg8: 3, Reg8: 6>
==> 00000101: <LoadConstUndefined>: <Reg8: 3>
==> 00000103: <Ret>: <Reg8: 3>


"""


def test_mov_after_if_reads_the_merged_register():
    context = Decompiler.build_context(_HASM_2, 2683, strict=False)
    js = Decompiler.render(context, verbose=False, raw=False)

    assert re.search(r"\br8 = r3;", js)
    assert not re.search(r"\br8 = r4;\n\s*}\n\s*r7 = ", js)


# ----------------------------------------------------------------------------------------------------
# merge_alias_readers
#
# Readers after an `if` of the alias an arm's `Mov` made read the register
# (`useReducer`, 96/2215):
#
#     r2 = param2 (else) | r4 (then, and a nested `if`); store(r0, r2); store(r0, r2)
#
# Both `PutById`s held the arm's alias `r4`, which is not what `r2` holds on the
# path through the `else`. `UnfoldedMergeRepairPass` only repointed `Mov`
# readers; any other reader kept the copy, and a second read got a fresh copy
# the repair could not find.
# ----------------------------------------------------------------------------------------------------

_USE_REDUCER = r"""

=> [Function #2215 "useReducer" of 187 bytes]: 4 params, frame size=19, strict=1, exc handler=1, debug info=0  @ offset 0x0013333d
  [Exception handlers: [start=0x40, end=0x45, target=0xac] ]

Bytecode listing:

==> 00000000: <LoadParam>: <Reg8: 2, UInt8: 3>
==> 00000003: <LoadParam>: <Reg8: 5, UInt8: 2>
==> 00000006: <Mov>: <Reg8: 6, Reg8: 2>
==> 00000009: <GetEnvironment>: <Reg8: 1, UInt8: 0>
==> 0000000c: <LoadFromEnvironmentL>: <Reg8: 0, Reg8: 1, UInt16: 331>
==> 00000011: <LoadConstUndefined>: <Reg8: 3>
==> 00000013: <Call1>: <Reg8: 0, Reg8: 0, Reg8: 3>
==> 00000017: <JStrictNotEqual>: <Addr8: 9, Reg8: 3, Reg8: 2>  # Address: 00000020
==> 0000001b: <Mov>: <Reg8: 2, Reg8: 5>
==> 0000001e: <Jmp>: <Addr8: 53>  # Address: 00000053
==> 00000020: <Mov>: <Reg8: 7, Reg8: 6>
==> 00000023: <Mov>: <Reg8: 4, Reg8: 5>
==> 00000026: <Call2>: <Reg8: 4, Reg8: 7, Reg8: 3, Reg8: 4>
==> 0000002b: <LoadFromEnvironment>: <Reg8: 7, Reg8: 1, UInt8: 122>
==> 0000002f: <Mov>: <Reg8: 2, Reg8: 4>
==> 00000032: <JmpFalse>: <Addr8: 33, Reg8: 7>  # Address: 00000053
==> 00000035: <LoadFromEnvironment>: <Reg8: 8, Reg8: 1, UInt8: 237>
==> 00000039: <LoadConstTrue>: <Reg8: 7>
==> 0000003b: <Call2>: <Reg8: 7, Reg8: 8, Reg8: 3, Reg8: 7>
==> 00000040: <Call2>: <Reg8: 5, Reg8: 6, Reg8: 3, Reg8: 5>
==> 00000045: <LoadFromEnvironment>: <Reg8: 6, Reg8: 1, UInt8: 237>
==> 00000049: <LoadConstFalse>: <Reg8: 5>
==> 0000004b: <Call2>: <Reg8: 5, Reg8: 6, Reg8: 3, Reg8: 5>
==> 00000050: <Mov>: <Reg8: 2, Reg8: 4>
==> 00000053: <PutById>: <Reg8: 0, Reg8: 2, UInt8: 1, string_id: 70>  # String: 'baseState' (Identifier)
==> 00000059: <PutById>: <Reg8: 0, Reg8: 2, UInt8: 2, string_id: 173>  # String: 'memoizedState' (Identifier)
==> 0000005f: <NewObjectWithBuffer>: <Reg8: 4, UInt16: 5, UInt16: 3, UInt16: 647, UInt16: 28>  # Object: {'pending': null, 'lanes': 0, 'dispatch': null}
==> 00000069: <LoadConstNull>: <Reg8: 7>
==> 0000006b: <LoadParam>: <Reg8: 5, UInt8: 1>
==> 0000006e: <PutNewOwnById>: <Reg8: 4, Reg8: 5, string_id: 12727>  # String: 'lastRenderedReducer' (Identifier)
==> 00000073: <PutNewOwnById>: <Reg8: 4, Reg8: 2, string_id: 13876>  # String: 'lastRenderedState' (Identifier)
==> 00000078: <PutById>: <Reg8: 0, Reg8: 4, UInt8: 3, string_id: 208>  # String: 'queue' (Identifier)
==> 0000007e: <LoadFromEnvironmentL>: <Reg8: 6, Reg8: 1, UInt16: 366>
==> 00000083: <GetByIdShort>: <Reg8: 5, Reg8: 6, UInt8: 1, string_id: 71>  # String: 'bind' (Identifier)
==> 00000088: <LoadFromEnvironment>: <Reg8: 2, Reg8: 1, UInt8: 117>
==> 0000008c: <Call4>: <Reg8: 2, Reg8: 5, Reg8: 6, Reg8: 7, Reg8: 2, Reg8: 4>
==> 00000093: <PutById>: <Reg8: 4, Reg8: 2, UInt8: 4, string_id: 119>  # String: 'dispatch' (Identifier)
==> 00000099: <GetByIdShort>: <Reg8: 4, Reg8: 0, UInt8: 2, string_id: 173>  # String: 'memoizedState' (Identifier)
==> 0000009e: <NewArray>: <Reg8: 0, UInt16: 2>
==> 000000a2: <PutOwnByIndex>: <Reg8: 0, Reg8: 4, UInt8: 0>
==> 000000a6: <PutOwnByIndex>: <Reg8: 0, Reg8: 2, UInt8: 1>
==> 000000aa: <Ret>: <Reg8: 0>
==> 000000ac: <Catch>: <Reg8: 0>
==> 000000ae: <LoadFromEnvironment>: <Reg8: 2, Reg8: 1, UInt8: 237>
==> 000000b2: <LoadConstFalse>: <Reg8: 1>
==> 000000b4: <Call2>: <Reg8: 1, Reg8: 2, Reg8: 3, Reg8: 1>
==> 000000b9: <Throw>: <Reg8: 0>
"""


def _render_2(hasm: str, function_id: int) -> str:
    context = Decompiler.build_context(hasm, function_id, strict=False)

    return Decompiler.render(context, verbose=False, raw=False)


def test_stores_after_the_merge_read_the_merged_register():
    js = _render_2(_USE_REDUCER, 2215)

    assert re.search(r"\br0\.baseState = r2;", js)
    assert re.search(r"\br0\.memoizedState = r2;", js)


# ----------------------------------------------------------------------------------------------------
# merge_value_register
#
# Two `Mov`s in a row each carry a merged value one level on
# (`Mov r2, r0` at the end of an arm, then `Mov r1, r2` after it).
#
# `UnfoldedMergeRepairPass` repoints the readers of an arm's value to the
# register; the first repair hands the SAME replacement `r0` to both `Mov`s, and the
# second repair then took that shared object for an ambiguous constant and gave up,
# so `r1` kept an inlined `r5 != null` over a register reassigned on one path only.
# ----------------------------------------------------------------------------------------------------

_IS_PUBLIC_INSTANCE_HASM = """
=> [Function #4129 "isPublicInstance" of 91 bytes]: 2 params, frame size=7, strict=1, exc handler=0, debug info=0  @ offset 0x0019b16d

Bytecode listing:

==> 00000000: <LoadParam>: <Reg8: 5, UInt8: 1>
==> 00000003: <LoadConstNull>: <Reg8: 3>
==> 00000005: <Neq>: <Reg8: 1, Reg8: 5, Reg8: 3>
==> 00000009: <JmpFalse>: <Addr8: 80, Reg8: 1>  # Address: 00000059
==> 0000000c: <GetById>: <Reg8: 6, Reg8: 5, UInt8: 0, string_id: 10143>  # String: '__nativeTag' (Identifier)
==> 00000012: <Neq>: <Reg8: 2, Reg8: 6, Reg8: 3>
==> 00000016: <JmpTrue>: <Addr8: 64, Reg8: 2>  # Address: 00000056
==> 00000019: <Neq>: <Reg8: 0, Reg8: 5, Reg8: 3>
==> 0000001d: <JmpFalse>: <Addr8: 13, Reg8: 0>  # Address: 0000002a
==> 00000020: <GetById>: <Reg8: 6, Reg8: 5, UInt8: 1, string_id: 14991>  # String: '_internalInstanceHandle' (Identifier)
==> 00000026: <Neq>: <Reg8: 0, Reg8: 6, Reg8: 3>
==> 0000002a: <JmpFalse>: <Addr8: 18, Reg8: 0>  # Address: 0000003c
==> 0000002d: <GetById>: <Reg8: 6, Reg8: 5, UInt8: 1, string_id: 14991>  # String: '_internalInstanceHandle' (Identifier)
==> 00000033: <GetByIdShort>: <Reg8: 6, Reg8: 6, UInt8: 2, string_id: 233>  # String: 'stateNode' (Identifier)
==> 00000038: <Neq>: <Reg8: 0, Reg8: 6, Reg8: 3>
==> 0000003c: <JmpFalse>: <Addr8: 23, Reg8: 0>  # Address: 00000053
==> 0000003f: <GetById>: <Reg8: 5, Reg8: 5, UInt8: 1, string_id: 14991>  # String: '_internalInstanceHandle' (Identifier)
==> 00000045: <GetByIdShort>: <Reg8: 5, Reg8: 5, UInt8: 2, string_id: 233>  # String: 'stateNode' (Identifier)
==> 0000004a: <GetByIdShort>: <Reg8: 5, Reg8: 5, UInt8: 3, string_id: 98>  # String: 'canonical' (Identifier)
==> 0000004f: <Neq>: <Reg8: 0, Reg8: 5, Reg8: 3>
==> 00000053: <Mov>: <Reg8: 2, Reg8: 0>
==> 00000056: <Mov>: <Reg8: 1, Reg8: 2>
==> 00000059: <Ret>: <Reg8: 1>
"""


def _code_5(hasm, function_id):
    out = Decompiler.render(Decompiler.build_context(hasm, function_id), verbose=False)
    return "\n".join(line for line in out.splitlines() if not line.strip().startswith("//"))


def test_chained_movs_of_a_merged_value_name_the_registers_not_the_arm_value():
    # hermes-98 `isPublicInstance`
    code = _code_5(_IS_PUBLIC_INSTANCE_HASM, 4129)

    assert "r2 = r0;" in code
    assert "r1 = r2;" in code
    assert "r1 = r5 != null" not in code
    # the head definition the skipping path reads
    assert "r2 = param1.__nativeTag != null;" in code


# ----------------------------------------------------------------------------------------------------
# merged_test_with_return_copy
#
# A merged-away test block must not stay a predecessor of a private `return` copy (F-161).
#
# With the shared returns copied (a retry), `ShortCircuitConditionCfgPass` folded a test block into the one before
# it and left it listed as a predecessor of the copy the test jumped to; the dominator pass raised `KeyError`
# and the retry was silently dropped.
#
#     96/7449  `isValidElementType`-style chain of `||` tests (anonymous)
# ----------------------------------------------------------------------------------------------------

def test_the_retry_survives_a_folded_test_and_leaves_no_goto():
    hasm = (_DATA / "merged_test_with_return_copy_96_7449.hasm").read_text(encoding="utf-8")
    out = Decompiler.render(Decompiler.build_context(hasm, 7449, strict=False), verbose=False, raw=False)
    out = "\n".join(line for line in out.split("\n") if not line.strip().startswith("//"))

    assert "goto" not in out
    assert "while (true)" not in out
    assert out.rstrip().endswith("return true;\n}")


# ----------------------------------------------------------------------------------------------------
# nested_join_copy
#
# A copy read after a join of three paths must read the register (96/4775 `interpolate`).
#
#     r1 = param1;  if (r1 < min) { ...; r1 = min; if (mode !== "clamp") r1 = param1 }  r6 = r1;
#
# The last definition in address order is the inner `r1 = param1`, so `r6 = r1` printed
# `r6 = param1` (and every later `r6` read `param1`), although a clamped `r1 = min`
# reaches that read too. A join of two paths still folds into a `?:`.
# ----------------------------------------------------------------------------------------------------

def test_a_copy_read_after_a_three_path_join_keeps_the_register():
    hasm = (_DATA / "nested_join_copy_96_4775.hasm").read_text(encoding="utf-8")

    out = Decompiler.render(Decompiler.build_context(hasm, 4775, strict=False), verbose=False, raw=False)

    assert "goto" not in out
    assert "r6 = r1;" in out
    assert "r8 = -r6;" in out
    assert "r8 = r6 - param2;" in out
    assert "-param1" not in out


# ----------------------------------------------------------------------------------------------------
# rematerialized_constant_two_writes
#
# A test block that writes its register twice, the last write a constant END reads (96/3450 `onload`).
#
# `if (url.indexOf("file://") === 0 && (xhr.status < 200 || xhr.status > 599)) { status = 200 } else { status = xhr.status }`
# compiles to `X: if (r2 !== 0) goto S; Y: r2 = env[3]; r6 = r2.status; r2 = 200; if (r6 < 200) goto T; ...; S: ...; T: put(r5, r2)`.
# `_constants_for_the_end_edge` wanted the register written ONCE in the block, so the constant END reads (`r2 = 200`)
# was not given its own copy on the edge into END, the crossed fold failed, and the printed
# `if (r6 < 200 || ...) goto label_146; r5.status = 200;` set 200 on the not-out-of-range path too.
# The block's LAST write is what END reads; the earlier ones only feed the test.
# ----------------------------------------------------------------------------------------------------

def _render_3(name, index):
    hasm = (_DATA / name).read_text(encoding="utf-8")

    return Decompiler.render(Decompiler.build_context(hasm, index, strict=False), verbose=False, raw=False)


def test_the_status_test_is_one_condition_with_an_else():
    out = _render_3("rematerialized_constant_96_3450.hasm", 3450)

    assert "goto label" not in out
    assert "if (r2 === 0 && (r4[3].status < 200 || r4[3].status > 599)) {\n        r5.status = 200;\n    } else {" in out


# ----------------------------------------------------------------------------------------------------
# unfolded_merge_default
#
# A value written in only ONE arm of an `if` that stays an `if` (no fold pass could
# express it as `?:` / `||` / `??=`) leaves the register holding the DEFAULT on the
# path that skips the arm. Code after the `if` reads the register by name, so the
# default's own statement has to print - but a default that a condition consumed
# inline (`LoadConstUInt8 r3, 100` -> `param1 > 100`) is flagged `definition_used`
# and printed nowhere, so that path read a register nothing ever assigned.
# ----------------------------------------------------------------------------------------------------

_CLAMP_HASM = """
=> [Function #15070 "ternaryTest" of 137 bytes]: 2 params, frame size=14, strict=1, exc handler=0, debug info=0  @ offset 0x002685a6

Bytecode listing:

==> 00000000: <LoadParam>: <Reg8: 2, UInt8: 1>
==> 00000003: <GetGlobalObject>: <Reg8: 0>
==> 00000005: <TryGetById>: <Reg8: 4, Reg8: 0, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
==> 0000000b: <GetByIdShort>: <Reg8: 3, Reg8: 4, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
==> 00000010: <LoadConstString>: <Reg8: 1, string_id: 4641>  # String: '__BC:ControlFlow/TernaryTests/ternaryTest/start' (String)
==> 00000014: <Call2>: <Reg8: 1, Reg8: 3, Reg8: 4, Reg8: 1>
==> 00000019: <LoadConstZero>: <Reg8: 1>
==> 0000001b: <Greater>: <Reg8: 3, Reg8: 2, Reg8: 1>
==> 0000001f: <LoadConstString>: <Reg8: 5, string_id: 866>  # String: 'positive' (String)
==> 00000023: <JmpTrue>: <Addr8: 21, Reg8: 3>  # Address: 00000038
==> 00000026: <Less>: <Reg8: 4, Reg8: 2, Reg8: 1>
==> 0000002a: <LoadConstString>: <Reg8: 3, string_id: 615>  # String: 'zero' (String)
==> 0000002e: <JmpFalse>: <Addr8: 7, Reg8: 4>  # Address: 00000035
==> 00000031: <LoadConstString>: <Reg8: 3, string_id: 1323>  # String: 'negative' (String)
==> 00000035: <Mov>: <Reg8: 5, Reg8: 3>
==> 00000038: <TryGetById>: <Reg8: 4, Reg8: 0, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
==> 0000003e: <GetByIdShort>: <Reg8: 3, Reg8: 4, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
==> 00000043: <Call2>: <Reg8: 3, Reg8: 3, Reg8: 4, Reg8: 5>
==> 00000048: <LoadConstUInt8>: <Reg8: 3, UInt8: 100>
==> 0000004b: <Greater>: <Reg8: 4, Reg8: 2, Reg8: 3>
==> 0000004f: <JmpTrue>: <Addr8: 18, Reg8: 4>  # Address: 00000061
==> 00000052: <Less>: <Reg8: 4, Reg8: 2, Reg8: 1>
==> 00000056: <LoadConstZero>: <Reg8: 1>
==> 00000058: <JmpTrue>: <Addr8: 6, Reg8: 4>  # Address: 0000005e
==> 0000005b: <Mov>: <Reg8: 1, Reg8: 2>
==> 0000005e: <Mov>: <Reg8: 3, Reg8: 1>
==> 00000061: <TryGetById>: <Reg8: 2, Reg8: 0, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
==> 00000067: <GetByIdShort>: <Reg8: 1, Reg8: 2, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
==> 0000006c: <Call2>: <Reg8: 1, Reg8: 1, Reg8: 2, Reg8: 3>
==> 00000071: <TryGetById>: <Reg8: 2, Reg8: 0, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
==> 00000077: <GetByIdShort>: <Reg8: 1, Reg8: 2, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
==> 0000007c: <LoadConstString>: <Reg8: 0, string_id: 3481>  # String: '__BC:ControlFlow/TernaryTests/ternaryTest/end' (String)
==> 00000080: <Call2>: <Reg8: 0, Reg8: 1, Reg8: 2, Reg8: 0>
==> 00000085: <LoadConstUndefined>: <Reg8: 0>
==> 00000087: <Ret>: <Reg8: 0>
"""


def _code_6(hasm, function_id):
    out = Decompiler.render(Decompiler.build_context(hasm, function_id), verbose=False)
    return "\n".join(line for line in out.splitlines() if not line.strip().startswith("//"))


def test_default_consumed_by_the_condition_is_still_assigned_on_the_skipping_path():
    # `r3 = 100; if (param1 > 100) skip; ...; r3 = clamped; console.log(r3)`:
    # when param1 > 100 nothing else sets r3, so `r3 = 100` must print.
    code = _code_6(_CLAMP_HASM, 15070)

    assert "r3 = 100;" in code
    assert code.index("r3 = 100;") < code.index("if (param1 <= 100) {")
    assert code.index("if (param1 <= 100) {") < code.index("console.log(r3);")


def test_default_that_already_prints_is_not_printed_twice():
    # `r5 = "positive"` is not consumed inline, so it already prints once.
    code = _code_6(_CLAMP_HASM, 15070)

    assert code.count('r5 = "positive";') == 1


_ARM_NAMED_AFTER_IF_HASM = """
=> [Function #9643 "y" of 92 bytes]: 2 params, frame size=16, strict=1, exc handler=0, debug info=0  @ offset 0x00206171

Bytecode listing:

==> 00000000: <GetParentEnvironment>: <Reg8: 3, UInt8: 0>
==> 00000003: <GetGlobalObject>: <Reg8: 1>
==> 00000005: <GetById>: <Reg8: 2, Reg8: 1, UInt8: 0, string_id: 10621>  # String: 'queueMicrotask' (Identifier)
==> 0000000b: <JmpTypeOfIs>: <Addr32: 56, Reg8: 2, UInt16: 128>  # Address: 00000043
==> 00000013: <CreateFunctionEnvironment>: <Reg8: 2, UInt8: 1>
==> 00000016: <LoadFromEnvironment>: <Reg8: 6, Reg8: 3, UInt8: 3>
==> 0000001a: <CreateThisForNew>: <Reg8: 5, Reg8: 6, UInt8: 1>
==> 0000001e: <CreateTopLevelEnvironment>: <Reg8: 4, UInt32: 1>
==> 00000024: <CreateClosure>: <Reg8: 7, Reg8: 4, function_id: 12507>  # Function: [#12507  of 19 bytes]: 2 params @ offset 0x00210ffa
==> 00000029: <Mov>: <Reg8: 8, Reg8: 5>
==> 0000002c: <Construct>: <Reg8: 4, Reg8: 6, UInt8: 2>
==> 00000030: <SelectObject>: <Reg8: 4, Reg8: 5, Reg8: 4>
==> 00000034: <StoreToEnvironment>: <Reg8: 2, UInt8: 0, Reg8: 4>
==> 00000038: <CreateClosure>: <Reg8: 2, Reg8: 2, function_id: 12552>  # Function: [#12552 y of 47 bytes]: 2 params @ offset 0x00245474
==> 0000003d: <StoreToEnvironment>: <Reg8: 3, UInt8: 12, Reg8: 2>
==> 00000041: <Jmp>: <Addr8: 15>  # Address: 00000050
==> 00000043: <TryGetById>: <Reg8: 1, Reg8: 1, UInt8: 0, string_id: 10621>  # String: 'queueMicrotask' (Identifier)
==> 00000049: <StoreToEnvironment>: <Reg8: 3, UInt8: 12, Reg8: 1>
==> 0000004d: <Mov>: <Reg8: 2, Reg8: 1>
==> 00000050: <LoadParam>: <Reg8: 1, UInt8: 1>
==> 00000053: <LoadConstUndefined>: <Reg8: 0>
==> 00000055: <Call2>: <Reg8: 1, Reg8: 2, Reg8: 0, Reg8: 1>
==> 0000005a: <Ret>: <Reg8: 1>
"""


def test_an_arm_write_the_code_after_the_if_names_still_prints():
    # `r2` is written on BOTH paths (`queueMicrotask` / the `y` closure) and is
    # read by name after the `if` (`r2.call(...)`). The else arm's `r2 = y` is
    # also inlined into `r3[12] = y` inside the arm; that used to be taken as
    # "used" and left that path calling an `r2` nothing had assigned.
    code = _code_6(_ARM_NAMED_AFTER_IF_HASM, 9643)

    assert "r2 = queueMicrotask;" in code
    assert "r2 = y;" in code
    assert code.index("r2 = y;") < code.index("r2.call(")


_NESTED_IF_CONST_HASM = """

=> [Function #13356 "" of 74 bytes]: 2 params, frame size=15, strict=1, exc handler=0, debug info=0  @ offset 0x00257d42

Bytecode listing:

==> 00000000: <GetParentEnvironment>: <Reg8: 3, UInt8: 0>
==> 00000003: <LoadParam>: <Reg8: 5, UInt8: 1>
==> 00000006: <LoadFromEnvironment>: <Reg8: 4, Reg8: 3, UInt8: 0>
==> 0000000a: <JmpTypeOfIs>: <Addr32: 34, Reg8: 5, UInt16: 128>  # Address: 0000002c
==> 00000012: <LoadConstUndefined>: <Reg8: 0>
==> 00000014: <LoadConstNull>: <Reg8: 1>
==> 00000016: <LoadConstUndefined>: <Reg8: 2>
==> 00000018: <JStrictEqual>: <Addr8: 27, Reg8: 5, Reg8: 1>  # Address: 00000033
==> 0000001c: <LoadConstUndefined>: <Reg8: 2>
==> 0000001e: <JStrictEqual>: <Addr8: 21, Reg8: 5, Reg8: 0>  # Address: 00000033
==> 00000022: <PutByIdStrict>: <Reg8: 5, Reg8: 4, UInt8: 0, string_id: 57>  # String: 'current' (Identifier)
==> 00000028: <LoadConstUndefined>: <Reg8: 2>
==> 0000002a: <Jmp>: <Addr8: 9>  # Address: 00000033
==> 0000002c: <LoadConstUndefined>: <Reg8: 0>
==> 0000002e: <Call2>: <Reg8: 2, Reg8: 5, Reg8: 0, Reg8: 4>
==> 00000033: <LoadFromEnvironment>: <Reg8: 0, Reg8: 3, UInt8: 1>
==> 00000037: <JmpTrue>: <Addr8: 17, Reg8: 0>  # Address: 00000048
==> 0000003a: <JmpTypeOfIs>: <Addr32: 14, Reg8: 2, UInt16: 383>  # Address: 00000048
==> 00000042: <LoadConstTrue>: <Reg8: 0>
==> 00000044: <StoreNPToEnvironment>: <Reg8: 3, UInt8: 1, Reg8: 0>
==> 00000048: <Ret>: <Reg8: 2>
"""


def test_a_printed_constant_between_nested_ifs_is_not_looked_past():
    # `if (p !== null) { r2 = undefined; if (p !== undefined) {...} }`: the
    # `r2 = undefined` between the two tests is a printed definition later code
    # reads by name, so the ifs must not be folded into one `&&` that drops it.
    code = _code_6(_NESTED_IF_CONST_HASM, 13356)

    assert "param1 !== null && param1 !== undefined" not in code
    assert "if (param1 !== undefined) {" in code
    assert code.index("if (param1 !== null) {") < code.index("if (param1 !== undefined) {")
