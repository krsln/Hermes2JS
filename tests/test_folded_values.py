"""Folded values: ternaries, `typeof` tests, optional chains, literal folding.

Merged from: test_array_literal_folding, test_condition_before_constant_write, test_conditional_expression_pass_caches, test_entry_undefined_read_only_in_if_condition, test_folded_chain_does_not_rewrite_a_store_target, test_folded_ternary_join_copy, test_folded_ternary_stale_test, test_folded_value_test_inside_a_loop, test_join_folded_undefined, test_object_literal_folding, test_slot_and_define_folding, test_ternary_not_moved_above_its_test, test_ternary_test_parens, test_typeof_guard_join, test_typeof_mask, test_typeof_register_join, test_value_diamond_with_call, test_value_fold_optional_chain.
"""

from __future__ import annotations

import importlib
import re
from pathlib import Path
from test_register_semantics import dangling_registers, decompile
from types import SimpleNamespace

import pytest

from hermes_decompiler.Decompiler import Decompiler
from hermes_decompiler.backend.emit.printer.ExpressionPrinter import ExpressionPrinter
from hermes_decompiler.frontend.handlers.shared import build_typeof_condition
from hermes_decompiler.ir.expressions import (
    BinaryExpression,
    ConditionalExpression,
    Identifier,
    NullLiteral,
    UndefinedLiteral,
)
from hermes_decompiler.ir.expressions.Operations import LogicalOperator


# ----------------------------------------------------------------------------------------------------
# array_literal_folding
#
# `NewArray` + `PutOwnByIndex` build an array literal. The element stores used
# to be printed as a chained assignment that was ALSO published as a definition
# of the array register - `r0 = (r0[0] = param1)[1] = "Woof"` - so the register
# ended up holding the LAST ELEMENT ("Woof"), not the array. They now fold into
# `r0 = [param1, "Woof"]`, or - when that is not provably equivalent - print as
# a plain `r0[i] = v` statement that defines nothing.
#
# The two inputs under tests/data are single sections cut out of a real React
# Native hermes-96 bundle (function ids 10215 and 9241).
# ----------------------------------------------------------------------------------------------------

_DATA = Path(__file__).parent / "data"
_FIXTURES = Path(__file__).resolve().parents[1] / "apps" / "demo" / "fixtures"


def _decompile(hasm: str, function_id: int) -> str:
    context = Decompiler.build_context(hasm, function_id)
    out = Decompiler.render(context, verbose=False)

    return "\n".join(line for line in out.split("\n") if not line.strip().startswith("//"))


def _fixture(version: str, function_id: int) -> str:
    path = next((_FIXTURES / version / "sections").glob(f"function_{function_id}_*.hasm"))

    return _decompile(path.read_text(encoding="utf-8"), function_id)


_CHAIN = re.compile(r"\(+\s*r\d+\[\d+\] = [^=]")  # `(rN[k] = v)`


def test_elements_fold_into_one_literal():
    # NewArray r0,2 / PutOwnByIndex r0,param1,0 / PutOwnByIndex r0,"Woof",1
    out = _fixture("96", 15202)  # Dog

    assert 'r0 = [param1, "Woof"]' in out
    assert not _CHAIN.search(out)


def test_array_register_is_never_defined_by_an_element_store():
    # `x = (arr[0] = v)` evaluates to v. The old chain made the array
    # register hold the element.
    for function_id in (15045, 15201, 15105, 15189):
        out = _fixture("96", function_id)

        assert not _CHAIN.search(out), function_id
        assert not re.search(r"\br\d+ = r\d+\[\d+\] = ", out), function_id


def test_unfoldable_store_stays_a_plain_statement():
    # The second element's value is a printed statement between the literal
    # and its second store, so folding would reorder it: `r1 = [r6]` then a
    # separate `r1[1] = r9`.
    out = _fixture("96", 15189)

    assert re.search(r"r1 = \[r6\];\n", out)
    assert re.search(r"\n\s*r1\[1\] = r9;\n", out)


def test_ternary_default_keeps_the_array_not_the_element():
    # `Array.isArray(p) ? p : [p]`: NewArray r0,1 / PutOwnByIndex r0,r1,0 /
    # Mov r3,r0. r3 must be the ARRAY - it used to be `r3 = r0[0] = param2`,
    # i.e. param2 itself, so `.reduce` ran on a non-array.
    out = _decompile((_DATA / "array_literal_resolvePath.hasm").read_text(encoding="utf-8"), 10215)

    assert "r0 = [param2]" in out
    assert "r3 = r0;\n" in out
    assert "r3 = r0[0]" not in out


def test_conditional_arm_defining_an_array_is_not_folded_into_a_ternary():
    # The if-arm builds `r7 = [-x, -y, -z]` and the merge write reads
    # `r7[r2]`. ConditionalExpressionRegionPass used to absorb such an arm
    # into `cond ? a : b`, deleting the statement that creates the array.
    out = _decompile((_DATA / "array_literal_in_conditional_arm.hasm").read_text(encoding="utf-8"), 9241)

    # `r0` is reassigned (`r0 = r2`) before the arm runs, so the operands are
    # read from the registers that still hold them, not re-read through `r0`.
    assert "r7 = [r6];" in out and "r7[1] = r5;" in out
    assert "r0 = r7[r2]" in out
    assert "(r8 !== r7) ?" not in out


# ----------------------------------------------------------------------------------------------------
# condition_before_constant_write
#
# A test whose operand register is overwritten by a constant between the
# compare and its jump must be evaluated BEFORE that write (98/11177):
#
#     r4 = r5.params == null;  r5 = undefined;  if (r4 == false) ...
#
# It used to print `r5 = undefined; if (r5.params != null)`, which reads the
# member of `undefined`.
# ----------------------------------------------------------------------------------------------------

_HASM = """
=> [Function #11177 "" of 186 bytes]: 2 params, frame size=20, strict=1, exc handler=0, debug info=0  @ offset 0x002252ac

Bytecode listing:

==> 00000000: <GetParentEnvironment>: <Reg8: 5, UInt8: 0>
==> 00000003: <LoadParam>: <Reg8: 6, UInt8: 1>
==> 00000006: <GetByIdShort>: <Reg8: 8, Reg8: 6, UInt8: 0, string_id: 232>  # String: 'startsWith' (Identifier)
==> 0000000b: <LoadConstString>: <Reg8: 7, string_id: 4447>  # String: '[...' (String)
==> 0000000f: <Call2>: <Reg8: 7, Reg8: 8, Reg8: 6, Reg8: 7>
==> 00000014: <JmpTrue>: <Addr8: 91, Reg8: 7>  # Address: 0000006f
==> 00000017: <GetByIdShort>: <Reg8: 8, Reg8: 6, UInt8: 0, string_id: 232>  # String: 'startsWith' (Identifier)
==> 0000001c: <LoadConstString>: <Reg8: 7, string_id: 1103>  # String: '[' (String)
==> 00000020: <Call2>: <Reg8: 7, Reg8: 8, Reg8: 6, Reg8: 7>
==> 00000025: <JmpFalse>: <Addr8: 20, Reg8: 7>  # Address: 00000039
==> 00000028: <GetByIdShort>: <Reg8: 8, Reg8: 6, UInt8: 1, string_id: 135>  # String: 'endsWith' (Identifier)
==> 0000002d: <LoadConstString>: <Reg8: 7, string_id: 1218>  # String: ']' (String)
==> 00000031: <Call2>: <Reg8: 7, Reg8: 8, Reg8: 6, Reg8: 7>
==> 00000036: <JmpTrue>: <Addr8: 5, Reg8: 7>  # Address: 0000003b
==> 00000039: <Ret>: <Reg8: 6>
==> 0000003b: <LoadFromEnvironment>: <Reg8: 7, Reg8: 5, UInt8: 0>
==> 0000003f: <GetByIdShort>: <Reg8: 9, Reg8: 7, UInt8: 2, string_id: 196>  # String: 'params' (Identifier)
==> 00000044: <LoadConstNull>: <Reg8: 2>
==> 00000046: <Eq>: <Reg8: 2, Reg8: 9, Reg8: 2>
==> 0000004a: <LoadConstUndefined>: <Reg8: 7>
==> 0000004c: <JmpTrue>: <Addr8: 27, Reg8: 2>  # Address: 00000067
==> 0000004f: <GetByIdShort>: <Reg8: 8, Reg8: 6, UInt8: 3, string_id: 120>  # String: 'slice' (Identifier)
==> 00000054: <LoadConstInt>: <Reg8: 0, Imm32: -1>
==> 0000005a: <LoadConstUInt8>: <Reg8: 1, UInt8: 1>
==> 0000005d: <Call3>: <Reg8: 8, Reg8: 8, Reg8: 6, Reg8: 1, Reg8: 0>
==> 00000063: <GetByVal>: <Reg8: 7, Reg8: 9, Reg8: 8>
==> 00000067: <JmpTrue>: <Addr8: 6, Reg8: 7>  # Address: 0000006d
==> 0000006a: <Mov>: <Reg8: 7, Reg8: 6>
==> 0000006d: <Ret>: <Reg8: 7>
==> 0000006f: <LoadFromEnvironment>: <Reg8: 5, Reg8: 5, UInt8: 0>
==> 00000073: <GetByIdShort>: <Reg8: 8, Reg8: 5, UInt8: 2, string_id: 196>  # String: 'params' (Identifier)
==> 00000078: <LoadConstNull>: <Reg8: 2>
==> 0000007a: <Eq>: <Reg8: 4, Reg8: 8, Reg8: 2>
==> 0000007e: <LoadConstUndefined>: <Reg8: 5>
==> 00000080: <JmpTrue>: <Addr8: 50, Reg8: 4>  # Address: 000000b2
==> 00000083: <GetByIdShort>: <Reg8: 7, Reg8: 6, UInt8: 3, string_id: 120>  # String: 'slice' (Identifier)
==> 00000088: <LoadConstInt>: <Reg8: 0, Imm32: -1>
==> 0000008e: <LoadConstUInt8>: <Reg8: 1, UInt8: 4>
==> 00000091: <Call3>: <Reg8: 7, Reg8: 7, Reg8: 6, Reg8: 1, Reg8: 0>
==> 00000097: <GetByVal>: <Reg8: 9, Reg8: 8, Reg8: 7>
==> 0000009b: <Eq>: <Reg8: 2, Reg8: 9, Reg8: 2>
==> 0000009f: <LoadConstUndefined>: <Reg8: 5>
==> 000000a1: <JmpTrue>: <Addr8: 17, Reg8: 2>  # Address: 000000b2
==> 000000a4: <GetByIdShort>: <Reg8: 8, Reg8: 9, UInt8: 4, string_id: 167>  # String: 'join' (Identifier)
==> 000000a9: <LoadConstString>: <Reg8: 7, string_id: 503>  # String: '/' (String)
==> 000000ad: <Call2>: <Reg8: 5, Reg8: 8, Reg8: 9, Reg8: 7>
==> 000000b2: <JmpTrue>: <Addr8: 6, Reg8: 5>  # Address: 000000b8
==> 000000b5: <Mov>: <Reg8: 5, Reg8: 6>
==> 000000b8: <Ret>: <Reg8: 5>


"""


def test_condition_is_computed_before_the_constant_overwrites_its_operand():
    js = Decompiler.render(Decompiler.build_context(_HASM, 11177, strict=False), verbose=False, raw=False)

    assert re.search(r"r4 = r5\.params == null;\s*r5 = undefined;\s*if \(!r4\) \{", js)
    assert "if (r5.params != null)" not in js


# ----------------------------------------------------------------------------------------------------
# conditional_expression_pass_caches
#
# `ConditionalExpressionRegionPass` keeps the reach of a block, the owner of an instruction and the writers of a register
# instead of recomputing them for every reader it asks about (F-320; 98/2619 `beginWork` spent two thirds of its render
# time rebuilding them, 180 000 times). The tests check the helpers against a plain scan.
# ----------------------------------------------------------------------------------------------------

_PASS = importlib.import_module(
    "hermes_decompiler.backend.transforms.region_passes.ConditionalExpressionRegionPass"
).ConditionalExpressionRegionPass


class _Block:
    def __init__(self, name, instructions=()):
        self.name = name
        self.instructions = list(instructions)
        self.successors = []
        self.predecessors = []


class _Instruction:
    def __init__(self, dest_reg):
        self.dest_reg = dest_reg


def _block(name, instructions=()):
    return _Block(name, instructions)


def _link(a, b):
    a.successors.append(b)
    b.predecessors.append(a)


def _instruction(dest_reg):
    return _Instruction(dest_reg)


def _pass(blocks):
    instance = object.__new__(_PASS)
    instance.cfg = SimpleNamespace(blocks=blocks)

    return instance


def test_reach_follows_successors_and_predecessors():
    a, b, c, d = (_block(n) for n in "abcd")
    _link(a, b)
    _link(b, c)
    _link(c, b)  # a loop
    _link(a, d)
    instance = _pass([a, b, c, d])

    assert instance._reach(a, forward=True) == {a, b, c, d}
    assert instance._reach(c, forward=True) == {b, c}
    assert instance._reach(c, forward=False) == {a, b, c}
    assert instance._reach(d, forward=False) == {a, d}


def test_owner_and_writers_are_rebuilt_when_an_instruction_is_added():
    first, second = _instruction(1), _instruction(2)
    block = _block("a", [first])
    instance = _pass([block])

    assert instance._instruction_owner() == {first: block}
    assert instance._writers_of(1) == [(first, block)]
    assert instance._writers_of(2) == []

    block.instructions.append(second)

    assert instance._instruction_owner() == {first: block, second: block}
    assert instance._writers_of(2) == [(second, block)]


# ----------------------------------------------------------------------------------------------------
# entry_undefined_read_only_in_if_condition
#
# An entry `rN = undefined;` is dead when the only reads of `rN` that nothing writes before are in later `if` conditions.
#
# `DeadUndefinedStorePass` treated every register read by an expression living on a region object as live
# everywhere, so `r1 = undefined;` at the top of 96/9291 `parseRange` survived although `r1 = new Map()` runs
# before the only reads (`if (r5 > 1 && r1.has(""))`). An `if` condition is evaluated at the end of the block whose
# branch the region replaced, so its registers are reads there.
# ----------------------------------------------------------------------------------------------------

def test_entry_undefined_before_an_if_condition_read_is_dropped():
    hasm = (_DATA / "entry_undefined_read_only_in_if_condition_96_9291.hasm").read_text(encoding="utf-8")
    out = Decompiler.render(Decompiler.build_context(hasm, 9291, strict=False), verbose=False, raw=False)

    assert "r1 = new Map();" in out
    assert 'r1.has("")' in out
    assert "r1 = undefined;" not in out


# ----------------------------------------------------------------------------------------------------
# folded_chain_does_not_rewrite_a_store_target
#
# `this.mode = a.mode || this.mode || null;` keeps its store target (96/3440 and 98/9908 `Request`).
#
# Folding `a.mode || this.mode` repoints every structural copy of the arm's value `this.mode`, and the member the
# statement WRITES prints the same, so the store became `a.mode || this.mode = ...` (not valid JavaScript).
# ----------------------------------------------------------------------------------------------------

def _render() -> str:
    hasm = (_DATA / "folded_chain_must_not_rewrite_a_store_target_96_3440.hasm").read_text(encoding="utf-8")

    return Decompiler.render(Decompiler.build_context(hasm, 0, strict=False), verbose=False, raw=False)


def test_the_store_keeps_its_target():
    assert "this.mode = r1.mode || this.mode || null;" in _render()


def test_no_assignment_has_a_logical_expression_as_its_target():
    for line in _render().split("\n"):
        if " = " not in line or line.strip().startswith(("if ", "} else if ", "while ", "for ")):
            continue

        left = line.split(" = ")[0].strip()

        assert " || " not in left and " && " not in left, line


# ----------------------------------------------------------------------------------------------------
# folded_ternary_join_copy
#
# A ternary folded inside the arm of an outer `if` must not turn the join's
# copy (`Mov r0, r1`, read after the `if`) into a copy of the ternary: on the
# path that skips the arm `r1` still holds its earlier value (96/1853):
#
#     r1 = 8;  if (8 < r3) { ... r1 = c ? a : b; }  r0 = r1;
# ----------------------------------------------------------------------------------------------------

_HASM_2 = r"""
=> [Function #1853 "lanesToEventPriority" of 57 bytes]: 2 params, frame size=5, strict=1, exc handler=0, debug info=0  @ offset 0x001228e0

Bytecode listing:

==> 00000000: <LoadParam>: <Reg8: 1, UInt8: 1>
==> 00000003: <Negate>: <Reg8: 0, Reg8: 1>
==> 00000006: <BitAnd>: <Reg8: 3, Reg8: 1, Reg8: 0>
==> 0000000a: <LoadConstUInt8>: <Reg8: 0, UInt8: 2>
==> 0000000d: <JNotLess>: <Addr8: 42, Reg8: 0, Reg8: 3>  # Address: 00000037
==> 00000011: <LoadConstUInt8>: <Reg8: 1, UInt8: 8>
==> 00000014: <JNotLess>: <Addr8: 32, Reg8: 1, Reg8: 3>  # Address: 00000034
==> 00000018: <LoadConstInt>: <Reg8: 2, Imm32: 134217727>
==> 0000001e: <BitAnd>: <Reg8: 4, Reg8: 3, Reg8: 2>
==> 00000022: <LoadConstInt>: <Reg8: 2, Imm32: 268435456>
==> 00000028: <LoadConstZero>: <Reg8: 3>
==> 0000002a: <JStrictEqual>: <Addr8: 7, Reg8: 3, Reg8: 4>  # Address: 00000031
==> 0000002e: <LoadConstUInt8>: <Reg8: 2, UInt8: 32>
==> 00000031: <Mov>: <Reg8: 1, Reg8: 2>
==> 00000034: <Mov>: <Reg8: 0, Reg8: 1>
==> 00000037: <Ret>: <Reg8: 0>
"""


def test_join_copy_after_a_folded_ternary_still_reads_the_register():
    js = Decompiler.render(Decompiler.build_context(_HASM_2, 1853, strict=False), verbose=False, raw=False)

    assert "r1 = 8;" in js
    assert "r0 = r1;" in js
    assert "r0 = (r3 === r4)" not in js


# ----------------------------------------------------------------------------------------------------
# folded_ternary_stale_test
#
# A folded ternary is not copied into a test that reads after its register changed (F-140, 96/1595 `deepDiffer`).
#
#     r1 = arguments[2] ... r5 === undefined ? -1 : arguments[2]   # the defaulted `maxDepth`
#     r5 = arguments.length <= 3 ? undefined : arguments[3]        # `r5` now holds something else
#     if (typeof r1 === "number") ...                              # the test reads the merge
#
# `repoint_references` gave terminators and region conditions the ternary unconditionally, so the
# tests printed `typeof (r5 === undefined ? -1 : arguments[2])` with the stale `r5`. They now take the
# same per-reader decision as an instruction does (the register when the ternary's test was reassigned).
# ----------------------------------------------------------------------------------------------------

def _code() -> str:
    hasm = (_DATA / "folded_ternary_stale_test_96_1595.hasm").read_text(encoding="utf-8")

    return Decompiler.render(Decompiler.build_context(hasm, 1595, strict=False), verbose=False, raw=False)


def test_a_test_after_the_ternary_register_changed_reads_the_register():
    code = _code()

    assert code.count('if (typeof r1 === "number") {') == 2
    assert "typeof (r5 === undefined" not in code


def test_a_copy_in_a_loop_is_not_read_by_a_branch_the_write_cannot_reach():
    # F-140: `r17 = r6` (the recursive call's argument, in the loops) made `r6 != null` in the
    # `typeof function` branch print `r17 != null`; nothing sets `r17` on that path.
    code = _code()

    assert "r17 != null" not in code
    assert "if (r6 != null) {" in code


def test_a_merge_repair_does_not_touch_an_identical_value_in_the_other_arm():
    # F-150, 96/2065 `updateClassComponent`: the update path's chain contains the mount path's
    # `A && B` as an inner part; repairing the mount path's merge turned it into `r19`, a register
    # the update path never sets.
    hasm = (_DATA / "merge_repair_other_arm_96_2065.hasm").read_text(encoding="utf-8")
    code = Decompiler.render(Decompiler.build_context(hasm, 2065, strict=False), verbose=False, raw=False)

    assert "UNSAFE_componentWillReceiveProps && r19;" not in code
    # F-151: the chain is `A && B`, not `A && (A && B)` (the other copy's fold had rewritten this
    # copy's right operand before this one folded).
    assert code.count(
        'r11 = "function" !== typeof r10.UNSAFE_componentWillReceiveProps'
        ' && "function" !== typeof r10.componentWillReceiveProps;'
    ) == 2


def test_the_merge_check_builds_one_dominator_tree_per_pass():
    # F-143, 98/2619 `beginWork`: `_register_holds_merge` built a tree on every call (170 times,
    # minutes). The CFG's edges do not change while the pass runs, so one tree serves all calls.
    from hermes_decompiler.backend.analysis.dominance.DominatorTree import DominatorTree
    from hermes_decompiler.backend.transforms.region_passes.ConditionalExpressionRegionPass import (
        ConditionalExpressionRegionPass,
    )

    trees = []
    original_check = ConditionalExpressionRegionPass._register_holds_merge

    def counting_check(self, *args, **kwargs):
        before = DominatorTree.compute
        calls = []

        def compute(tree):
            calls.append(1)
            return before(tree)

        DominatorTree.compute = compute

        try:
            return original_check(self, *args, **kwargs)
        finally:
            DominatorTree.compute = before
            trees.append(len(calls))

    ConditionalExpressionRegionPass._register_holds_merge = counting_check

    try:
        _code()
    finally:
        ConditionalExpressionRegionPass._register_holds_merge = original_check

    # (the generator may run the pass again for a retry: one tree per pass, not per call)
    assert len(trees) >= 6, "the function no longer exercises the check"
    assert sum(trees) * 3 <= len(trees)


# ----------------------------------------------------------------------------------------------------
# folded_value_test_inside_a_loop
#
# A value test folded away inside a loop leaves no stale block behind (96/1927 `reconcileChildrenArray`).
#
# `ValueConditionFoldCfgPass` removes the blocks of an `a && b && c` that is only tested. The loop and dominator
# analyses were redone only when the LATER short-circuit pass removed blocks, so the folded-away `r16 = r15` block was
# still a member of the loop: it was printed as a statement of its own (`r16 = r23[0] && param2; r16 = param2;`, a wrong
# test) and the loop kept four `goto`s.
# ----------------------------------------------------------------------------------------------------

def _render_2() -> str:
    hasm = (_DATA / "folded_value_test_inside_a_loop_96_1927.hasm").read_text(encoding="utf-8")

    return Decompiler.render(Decompiler.build_context(hasm, 0, strict=False), verbose=False, raw=False)


def test_no_goto_is_left():
    assert "goto" not in _render_2()


def test_the_folded_test_is_not_followed_by_its_dead_copy():
    out = _render_2()

    assert "r16 = r23[0] && r15 && null === r25.alternate" in out
    assert "r16 = param2;" not in out
    assert "r16 = r15;" not in out


# ----------------------------------------------------------------------------------------------------
# join_folded_undefined
#
# A join read that names its register keeps the `undefined` an earlier test folded away (F-137, 98/9611 `dt`).
#
#     r4 = undefined                  # 0x58
#     if (undefined === r8) goto END  # JStrictEqual r4, r8: the test took `r4` as `undefined`
#     ...
#     r4 = <closure>                  # the other arm
#     END: r3.size = r4               # PutOwnBySlotIdx r3, r4
#
# The test inlined the constant and nothing printed `r4 = undefined`, so `r3.size = r4` read the
# `highWaterMark` value `r4` still held on the path that jumps. `get_register_expression` now prints the
# folded `undefined` definitions of the register when the join guard answers with `rN`.
# ----------------------------------------------------------------------------------------------------

def _code_2() -> str:
    hasm = (_DATA / "join_folded_undefined_98_9611.hasm").read_text(encoding="utf-8")

    return Decompiler.render(Decompiler.build_context(hasm, 9611, strict=False), verbose=False, raw=False)


def test_the_undefined_a_test_folded_is_printed_before_the_join_reads_it():
    code = _code_2()

    assert code.index('r3 = { "highWaterMark": r4, "size": null };\n        r4 = undefined;') >= 0
    # the tail both arms share (`r3.size = r4`) follows the `if`, so the test reads `!==` (F-187)
    assert code.index("r4 = undefined;\n        if (undefined !== r8) {") >= 0
    assert "r3.size = r4;" in code


# ----------------------------------------------------------------------------------------------------
# object_literal_folding
#
# `NewObject` + `PutNewOwnById` build an object literal one property at a
# time. They fold into `r0 = { "k": v, ... }` when that is exactly equivalent
# (see `frontend/handlers/construct/_literal_fold.py`) and otherwise print as
# plain `rN.k = v` statements, which define nothing.
#
# Inputs are real hermes-96 fixture sections, a few of them edited (the
# property name lives in the opcode's `# String: '...'` comment) to reach
# cases the fixtures don't contain.
# ----------------------------------------------------------------------------------------------------

_FIXTURES_2 = Path(__file__).resolve().parents[1] / "apps" / "demo" / "fixtures" / "96" / "sections"


def _section(function_id: int) -> str:
    return next(_FIXTURES_2.glob(f"function_{function_id}_*.hasm")).read_text(encoding="utf-8")


def _decompile_text(hasm: str, function_id: int) -> str:
    out = Decompiler.render(Decompiler.build_context(hasm, function_id), verbose=False)

    return "\n".join(line for line in out.split("\n") if not line.strip().startswith("//"))


def test_properties_fold_into_one_literal():
    # NewObject r0 / PutNewOwnByIdShort x3 -> one literal, then `return r0`.
    out = decompile("96", 15146)  # makeCounter

    assert 'r0 = { "increment": increment, "decrement": decrement, "value": value }' in out
    assert not re.search(r"\br0\.(increment|decrement|value) = ", out)
    assert dangling_registers(out) == []


def test_single_property_literal_in_a_branch():
    out = decompile("96", 15102)  # _interopDefault: param1 ? param1 : { default: param1 }

    assert 'r1 = { "default": param1 }' in out


def test_a_property_whose_value_is_a_printed_definition_stays_a_statement():
    # `{ a: 1, d: <another literal built before the store> }`: the inner
    # literal is a printed statement between the outer one and its store,
    # so the store is not folded (it would reorder the inner literal).
    out = decompile("96", 15095)  # objectLiteralTest

    assert re.search(r"r3 = \{[^\n]*\};\n(?:.*\n)*?\s*r2\.d = r3;\n", out)
    assert dangling_registers(out) == []


def test_proto_key_folds_only_as_a_computed_key():
    # In a literal `{ "__proto__": v }` SETS THE PROTOTYPE, but the opcode
    # defines an own data property of that name - and only the computed form
    # `{ ["__proto__"]: v }` does that. (Never the plain-key form.)
    hasm = _section(15102).replace("'default'", "'__proto__'")
    out = _decompile_text(hasm, 15102)

    assert 'r1 = { ["__proto__"]: param1 }' in out
    assert '{ "__proto__"' not in out


def test_repeated_key_keeps_the_later_store_as_a_statement():
    # increment, increment(again), value: the duplicate is not folded, and
    # once a store had to stay a statement the register has been read, so the
    # rest stay statements too - order is preserved either way.
    hasm = _section(15146).replace("'decrement'", "'increment'")
    out = _decompile_text(hasm, 15146)

    assert re.search(r'r0 = \{ "increment": \w+ \}', out)
    assert re.search(r"\n\s*r0\.increment = \w+;\n", out)
    assert re.search(r"\n\s*r0\.value = \w+;\n", out)


def test_literal_definition_in_a_boolean_chain_arm_is_not_dropped():
    # `cond && { color }`: the arm builds `r7 = { "color": ... }` and a later
    # store reads `r7` by name. BooleanChainRegionPass used to absorb the
    # arm ("only pure instructions") and delete the statement building r7,
    # leaving `r5[1] = cond && r7` with no `r7` anywhere.
    hasm = (_DATA / "object_literal_in_boolean_chain_arm.hasm").read_text(encoding="utf-8")
    out = _decompile_text(hasm, 13197)

    # The property read happened before the calls in between, so it is named
    # (`r8 = param1.tintColor`) rather than re-read at the literal.
    assert re.search(r'r7 = \{ "color": (param1\.tintColor|r8) \}', out)
    assert "&& r7" not in out


# ----------------------------------------------------------------------------------------------------
# slot_and_define_folding
#
# The remaining literal-building stores: hermes-98's `PutOwnBySlotIdx`,
# `DefineOwnById`, `DefineOwnByVal`, `DefineOwnInDenseArray`, and hermes-96's
# `PutOwnByVal`. Small hand-written sections exercise each rule; one real
# section covers the printer's else-if flattening.
#
# `PutOwnBySlotIdx` carries only a hidden-class slot; the property name is that
# slot's key in the `NewObjectWithBuffer` literal being built.
# ----------------------------------------------------------------------------------------------------

def _section_2(*instructions: str) -> str:
    body = "\n".join(f"==> {i * 4:08x}: {text}" for i, text in enumerate(instructions))

    return (
            '\n=> [Function #1 "f" of 99 bytes]: 3 params, frame size=20, strict=1, exc handler=0, '
            "debug info=0  @ offset 0x00000000\n\nBytecode listing:\n\n" + body + "\n\n"
    )


def _out(*instructions: str) -> str:
    out = Decompiler.render(Decompiler.build_context(_section_2(*instructions), 1), verbose=False)

    return "\n".join(line for line in out.split("\n") if not line.strip().startswith("//"))


_PARAM = "<LoadParam>: <Reg8: 1, UInt8: 1>"
_RET = "<Ret>: <Reg8: 0>"
_BUFFER = "<NewObjectWithBuffer>: <Reg8: 0, UInt16: 1, UInt16: 2>  # Object: {%s}"
_SLOT0 = "<PutOwnBySlotIdx>: <Reg8: 0, Reg8: 1, UInt8: 0>"


def test_slot_store_fills_the_buffer_placeholder():
    out = _out(_PARAM, _BUFFER % "'value': null, 'done': true", _SLOT0, _RET)

    assert 'r0 = { "value": param1, "done": true }' in out
    assert "slot_" not in out


def test_slot_name_resolves_even_when_the_store_cannot_fold():
    # `Mov r3, r0` reads the literal first, so the store stays a statement -
    # but it is `r0.value`, not `r0.slot_0`.
    out = _out(_PARAM, _BUFFER % "'value': null, 'done': true", "<Mov>: <Reg8: 3, Reg8: 0>", _SLOT0, _RET)

    assert "r0.value = param1" in out
    assert "slot_" not in out


def test_only_a_null_placeholder_is_replaced():
    out = _out(_PARAM, _BUFFER % "'value': 5, 'done': true", _SLOT0, _RET)

    assert '"value": 5' in out
    assert "r0.value = param1" in out


def test_index_like_keys_make_the_slot_order_unreliable():
    out = _out(_PARAM, _BUFFER % "'0': null, 'a': true", _SLOT0, _RET)

    assert "r0.slot_0 = param1" in out


def test_define_own_by_id_folds():
    out = _out(
        _PARAM, "<NewObject>: <Reg8: 0>",
        "<DefineOwnById>: <Reg8: 0, Reg8: 1, UInt8: 0, UInt16: 5>  # String: 'name' (Identifier)", _RET,
    )

    assert 'r0 = { "name": param1 }' in out


def test_define_own_by_id_resolves_the_name_from_a_string_id_operand():
    # hermes_disassembler tags the name operand `string_id` (hermes-dec leaves
    # it as a bare `UInt16`). The handler must accept the tagged form, or the
    # property degrades to `string_<id>`.
    out = _out(
        _PARAM, "<NewObject>: <Reg8: 0>",
        "<DefineOwnById>: <Reg8: 0, Reg8: 1, UInt8: 0, string_id: 140>  # String: 'error' (Identifier)", _RET,
    )

    assert 'r0 = { "error": param1 }' in out
    assert "string_" not in out


def test_define_own_by_id_long_resolves_the_name_from_a_string_id_operand():
    # DefineOwnByIdLong used to inherit the short form's UInt16-only pattern,
    # so it matched neither `UInt32` nor `string_id`.
    for operand in ("string_id: 70000", "UInt32: 70000"):
        out = _out(
            _PARAM, "<NewObject>: <Reg8: 0>",
            f"<DefineOwnByIdLong>: <Reg8: 0, Reg8: 1, UInt8: 0, {operand}>  # String: 'error' (Identifier)", _RET,
        )

        assert 'r0 = { "error": param1 }' in out, operand
        assert "string_" not in out, operand


def test_define_own_by_id_without_a_comment_falls_back_to_the_string_id():
    # Bare hermes-dec form, no `# String:` comment: still accepted, named by id.
    out = _out(
        _PARAM, "<NewObject>: <Reg8: 0>",
        "<DefineOwnById>: <Reg8: 0, Reg8: 1, UInt8: 0, UInt16: 140>", _RET,
    )

    assert 'r0 = { "string_140": param1 }' in out


def test_non_identifier_property_name_is_written_as_a_string_key():
    # `obj.aria-hidden = v` is not valid JavaScript.
    out = _out(
        "<LoadParam>: <Reg8: 0, UInt8: 1>", _PARAM,
        "<DefineOwnById>: <Reg8: 0, Reg8: 1, UInt8: 0, UInt16: 5>  # String: 'aria-hidden' (Identifier)", _RET,
    )

    assert '["aria-hidden"] = ' in out
    assert ".aria-hidden" not in out


def test_enumerable_define_by_value_folds_into_a_computed_property():
    out = _out(
        _PARAM, "<NewObject>: <Reg8: 0>", "<LoadConstString>: <Reg8: 2, string_id: 6>  # String: 'k' (String)",
        "<DefineOwnByVal>: <Reg8: 0, Reg8: 1, Reg8: 2, UInt8: 1>", _RET,
    )

    assert 'r0 = { "k": param1 }' in out


def test_non_enumerable_define_is_never_folded_into_a_literal():
    # enumerable == 0 (class methods: 1,136 of 1,278 in the hermes-98
    # bundle) would become an enumerable literal property if folded.
    out = _out(
        _PARAM, "<NewObject>: <Reg8: 0>", "<LoadConstString>: <Reg8: 2, string_id: 6>  # String: 'k' (String)",
        "<DefineOwnByVal>: <Reg8: 0, Reg8: 1, Reg8: 2, UInt8: 0>", _RET,
    )

    assert '"k": param1' not in out
    # `r0["k"] = param1` would make it enumerable (and run a setter).
    assert 'Object.defineProperty(r0, "k", { value: param1, writable: true, enumerable: false, configurable: true });' in out, out


def test_dense_array_elements_fold_into_one_literal():
    out = _out(
        _PARAM, "<NewArray>: <Reg8: 0, UInt16: 2>",
        "<DefineOwnInDenseArray>: <Reg8: 0, Reg8: 1, UInt8: 0>",
        "<DefineOwnInDenseArray>: <Reg8: 0, Reg8: 1, UInt8: 1>", _RET,
    )

    assert "r0 = [param1, param1]" in out


def test_printed_literal_definition_before_a_nested_if_is_not_skipped():
    # The else-branch starts with `r4 = ...; r9 = { ... }; r8 = ...` and then
    # an `if`. The printer flattened such a branch to `else if` and dropped
    # the prefix, because a block of "pure" definitions counted as skippable
    # - leaving `r5[115] = r9` with no `r9`. (Earlier the stores into the
    # literal, being assignments, had hidden this.)
    hasm = (_DATA / "literal_def_before_nested_if.hasm").read_text(encoding="utf-8")
    out = Decompiler.render(Decompiler.build_context(hasm, 2600), verbose=False)

    assert 'r9 = { "context": r8, "memoizedValue": r8._currentValue2, "next": null }' in out
    assert "r4 = r5[114]" in out


def test_define_own_by_id_name_is_resolved_in_98():
    # hermes-98 `spreadObjectTest`: `{...x, z: 3}`. The short `DefineOwnById`
    # was the only `*ById` opcode without a `string_id` tag, so the property
    # printed as `r5.string_6711`.
    from tests.test_register_semantics import decompile

    out = decompile("98", 9493)

    assert "r5.z = 3" in out
    assert "string_6711" not in out


def test_no_98_fixture_prints_an_unresolved_property_name():
    from pathlib import Path

    results = Path(__file__).resolve().parents[1] / "apps" / "demo" / "fixtures" / "98" / "results"

    for path in results.glob("function_*.js"):
        assert "string_" not in "".join(
            line for line in path.read_text(encoding="utf-8").splitlines(True) if not line.lstrip().startswith("//")
        ).replace("string_id", ""), path.name


def test_non_enumerable_put_own_by_value_is_a_define_too():
    # `PutOwnByVal` obj, VALUE, KEY, enumerable: operand order differs from `PutByVal`.
    out = _out(
        _PARAM, "<NewObject>: <Reg8: 0>", "<LoadConstString>: <Reg8: 2, string_id: 6>  # String: 'k' (String)",
        "<PutOwnByVal>: <Reg8: 0, Reg8: 1, Reg8: 2, UInt8: 0>", _RET,
    )

    assert 'Object.defineProperty(r0, "k", { value: param1, writable: true, enumerable: false, configurable: true });' in out, out
    assert 'r0["k"] = param1' not in out


def test_enumerable_put_own_by_value_stays_an_assignment_or_literal_property():
    out = _out(
        _PARAM, "<NewObject>: <Reg8: 0>", "<LoadConstString>: <Reg8: 2, string_id: 6>  # String: 'k' (String)",
        "<PutOwnByVal>: <Reg8: 0, Reg8: 1, Reg8: 2, UInt8: 1>", _RET,
    )

    assert "defineProperty" not in out, out


# ----------------------------------------------------------------------------------------------------
# ternary_not_moved_above_its_test
#
# A ternary folded onto an EARLIER definition must not be printed there when its
# test reads a register that is only set later (`useScrollOffset`, 96/11152):
#
#     r1 = closure; ...; r4 = r4.IS_WEB; if (!r4) r1 = other; store(r1)
#
# `ConditionalExpressionRegionPass` takes the register's last write in the block
# as the ternary's default and prints the fold where that write stands, so
# `r1 = !r4 ? ... : ...` ended up above the line that sets `r4`.
#
# A fold the reader swallows is a different case: the ternary is read where the
# reader stands, which is after the test (`toString`, 96/3602).
# ----------------------------------------------------------------------------------------------------

_USE_SCROLL_OFFSET = r"""

=> [Function #11152 "" of 230 bytes]: 8 params, frame size=22, strict=1, exc handler=0, debug info=0  @ offset 0x002079cf

Bytecode listing:

==> 00000000: <CreateEnvironment>: <Reg8: 2>
==> 00000002: <LoadParam>: <Reg8: 6, UInt8: 2>
==> 00000005: <LoadParam>: <Reg8: 9, UInt8: 6>
==> 00000008: <LoadParam>: <Reg8: 7, UInt8: 7>
==> 0000000b: <CreateClosure>: <Reg8: 3, Reg8: 2, function_id: 11153>  # Function: [#11153 useScrollOffsetWeb of 166 bytes]: 3 params @ offset 0x00207ab5
==> 00000010: <CreateClosure>: <Reg8: 1, Reg8: 2, function_id: 11159>  # Function: [#11159 useScrollOffsetNative of 145 bytes]: 3 params @ offset 0x00207cbd
==> 00000015: <CreateClosure>: <Reg8: 0, Reg8: 2, function_id: 11165>  # Function: [#11165 getWebScrollableElement of 42 bytes]: 2 params @ offset 0x00207e5a
==> 0000001a: <StoreToEnvironment>: <Reg8: 2, UInt8: 9, Reg8: 0>
==> 0000001e: <GetGlobalObject>: <Reg8: 4>
==> 00000020: <TryGetById>: <Reg8: 11, Reg8: 4, UInt8: 1, string_id: 24>  # String: 'Object' (Identifier)
==> 00000026: <GetByIdShort>: <Reg8: 10, Reg8: 11, UInt8: 2, string_id: 108>  # String: 'defineProperty' (Identifier)
==> 0000002b: <NewObject>: <Reg8: 8>
==> 0000002d: <LoadConstTrue>: <Reg8: 0>
==> 0000002f: <PutNewOwnByIdShort>: <Reg8: 8, Reg8: 0, string_id: 205>  # String: 'value' (Identifier)
==> 00000033: <LoadConstString>: <Reg8: 5, string_id: 48>  # String: '__esModule' (Identifier)
==> 00000037: <Call4>: <Reg8: 5, Reg8: 10, Reg8: 11, Reg8: 9, Reg8: 5, Reg8: 8>
==> 0000003e: <TryGetById>: <Reg8: 8, Reg8: 4, UInt8: 1, string_id: 24>  # String: 'Object' (Identifier)
==> 00000044: <GetByIdShort>: <Reg8: 5, Reg8: 8, UInt8: 2, string_id: 108>  # String: 'defineProperty' (Identifier)
==> 00000049: <NewObject>: <Reg8: 4>
==> 0000004b: <PutNewOwnByIdShort>: <Reg8: 4, Reg8: 0, string_id: 133>  # String: 'enumerable' (Identifier)
==> 0000004f: <CreateClosure>: <Reg8: 0, Reg8: 2, function_id: 11166>  # Function: [#11166 get of 9 bytes]: 1 params @ offset 0x00106b41
==> 00000054: <PutNewOwnByIdShort>: <Reg8: 4, Reg8: 0, string_id: 50>  # String: 'get' (Identifier)
==> 00000058: <LoadConstString>: <Reg8: 0, string_id: 11724>  # String: 'useScrollOffset' (Identifier)
==> 0000005c: <Call4>: <Reg8: 0, Reg8: 5, Reg8: 8, Reg8: 9, Reg8: 0, Reg8: 4>
==> 00000063: <LoadConstZero>: <Reg8: 0>
==> 00000065: <GetByVal>: <Reg8: 4, Reg8: 7, Reg8: 0>
==> 00000069: <LoadConstUndefined>: <Reg8: 0>
==> 0000006b: <Call2>: <Reg8: 4, Reg8: 6, Reg8: 0, Reg8: 4>
==> 00000070: <StoreToEnvironment>: <Reg8: 2, UInt8: 0, Reg8: 4>
==> 00000074: <LoadConstUInt8>: <Reg8: 4, UInt8: 1>
==> 00000077: <GetByVal>: <Reg8: 4, Reg8: 7, Reg8: 4>
==> 0000007b: <Call2>: <Reg8: 4, Reg8: 6, Reg8: 0, Reg8: 4>
==> 00000080: <StoreToEnvironment>: <Reg8: 2, UInt8: 1, Reg8: 4>
==> 00000084: <LoadConstUInt8>: <Reg8: 5, UInt8: 2>
==> 00000087: <GetByVal>: <Reg8: 5, Reg8: 7, Reg8: 5>
==> 0000008b: <Call2>: <Reg8: 5, Reg8: 6, Reg8: 0, Reg8: 5>
==> 00000090: <StoreToEnvironment>: <Reg8: 2, UInt8: 2, Reg8: 5>
==> 00000094: <LoadConstUInt8>: <Reg8: 5, UInt8: 3>
==> 00000097: <GetByVal>: <Reg8: 5, Reg8: 7, Reg8: 5>
==> 0000009b: <Call2>: <Reg8: 5, Reg8: 6, Reg8: 0, Reg8: 5>
==> 000000a0: <StoreToEnvironment>: <Reg8: 2, UInt8: 3, Reg8: 5>
==> 000000a4: <LoadConstString>: <Reg8: 5, string_id: 5127>  # String: 'animatedRef is not initialized in useScrollOffset. Make sure to pass the animated ref to the scrollable component to get scroll offset updates.' (String)
==> 000000a8: <StoreToEnvironment>: <Reg8: 2, UInt8: 4, Reg8: 5>
==> 000000ac: <NewArrayWithBuffer>: <Reg8: 5, UInt16: 5, UInt16: 5, UInt16: 20715>  # Array: ['onScroll', 'onScrollBeginDrag', 'onScrollEndDrag', 'onMomentumScrollBegin', 'onMomentumScrollEnd']
==> 000000b4: <StoreToEnvironment>: <Reg8: 2, UInt8: 5, Reg8: 5>
==> 000000b8: <GetById>: <Reg8: 4, Reg8: 4, UInt8: 3, string_id: 9473>  # String: 'IS_WEB' (Identifier)
==> 000000be: <JmpFalse>: <Addr8: 6, Reg8: 4>  # Address: 000000c4
==> 000000c1: <Mov>: <Reg8: 1, Reg8: 3>
==> 000000c4: <StoreToEnvironment>: <Reg8: 2, UInt8: 6, Reg8: 1>
==> 000000c8: <NewObject>: <Reg8: 1>
==> 000000ca: <LoadConstString>: <Reg8: 3, string_id: 6258>  # String: 'function reactNativeReanimated_useScrollOffsetTs1(){const{animatedRef,getWebScrollableElement,offset}=this.__closure;var _animatedRef;if((_animatedRef=animatedRef)!==null&&_animatedRef!==void 0&&_animatedRef.current){const element=getWebScrollableElement(animatedRef.current);offset.value=element.scrollLeft===0?element.scrollTop:element.scrollLeft;}}' (String)
==> 000000ce: <PutNewOwnByIdShort>: <Reg8: 1, Reg8: 3, string_id: 92>  # String: 'code' (Identifier)
==> 000000d2: <StoreToEnvironment>: <Reg8: 2, UInt8: 7, Reg8: 1>
==> 000000d6: <NewObject>: <Reg8: 1>
==> 000000d8: <LoadConstString>: <Reg8: 3, string_id: 6260>  # String: 'function reactNativeReanimated_useScrollOffsetTs2(event){const{offset}=this.__closure;offset.value=event.contentOffset.x===0?event.contentOffset.y:event.contentOffset.x;}' (String)
==> 000000dc: <PutNewOwnByIdShort>: <Reg8: 1, Reg8: 3, string_id: 92>  # String: 'code' (Identifier)
==> 000000e0: <StoreToEnvironment>: <Reg8: 2, UInt8: 8, Reg8: 1>
==> 000000e4: <Ret>: <Reg8: 0>
"""

_TO_STRING = r"""

=> [Function #3602 "toString" of 91 bytes]: 1 params, frame size=13, strict=1, exc handler=0, debug info=0  @ offset 0x0015b9c7

Bytecode listing:

==> 00000000: <LoadParam>: <Reg8: 0, UInt8: 0>
==> 00000003: <GetById>: <Reg8: 2, Reg8: 0, UInt8: 1, string_id: 15380>  # String: '_searchParamsInstance' (Identifier)
==> 00000009: <LoadConstNull>: <Reg8: 1>
==> 0000000b: <JStrictEqual>: <Addr8: 72, Reg8: 2, Reg8: 1>  # Address: 00000053
==> 0000000f: <GetById>: <Reg8: 2, Reg8: 0, UInt8: 1, string_id: 15380>  # String: '_searchParamsInstance' (Identifier)
==> 00000015: <GetByIdShort>: <Reg8: 1, Reg8: 2, UInt8: 2, string_id: 33>  # String: 'toString' (Identifier)
==> 0000001a: <Call1>: <Reg8: 2, Reg8: 1, Reg8: 2>
==> 0000001e: <GetById>: <Reg8: 4, Reg8: 0, UInt8: 3, string_id: 12484>  # String: '_url' (Identifier)
==> 00000024: <GetByIdShort>: <Reg8: 1, Reg8: 4, UInt8: 4, string_id: 162>  # String: 'indexOf' (Identifier)
==> 00000029: <LoadConstString>: <Reg8: 3, string_id: 1885>  # String: '?' (String)
==> 0000002d: <Call2>: <Reg8: 4, Reg8: 1, Reg8: 4, Reg8: 3>
==> 00000032: <LoadConstInt>: <Reg8: 1, Imm32: -1>
==> 00000038: <Greater>: <Reg8: 1, Reg8: 4, Reg8: 1>
==> 0000003c: <JmpFalse>: <Addr8: 7, Reg8: 1>  # Address: 00000043
==> 0000003f: <LoadConstString>: <Reg8: 3, string_id: 1103>  # String: '&' (String)
==> 00000043: <GetById>: <Reg8: 1, Reg8: 0, UInt8: 3, string_id: 12484>  # String: '_url' (Identifier)
==> 00000049: <Add>: <Reg8: 1, Reg8: 1, Reg8: 3>
==> 0000004d: <Add>: <Reg8: 1, Reg8: 1, Reg8: 2>
==> 00000051: <Ret>: <Reg8: 1>
==> 00000053: <GetById>: <Reg8: 0, Reg8: 0, UInt8: 3, string_id: 12484>  # String: '_url' (Identifier)
==> 00000059: <Ret>: <Reg8: 0>
"""


def _render_3(hasm: str, function_id: int) -> str:
    context = Decompiler.build_context(hasm, function_id, strict=False)

    return Decompiler.render(context, verbose=False, raw=False)


def test_ternary_that_would_print_above_its_test_stays_an_if():
    js = _render_3(_USE_SCROLL_OFFSET, 11152)

    assert "!r4 ?" not in js
    assert js.index("r4 = r4.IS_WEB;") < js.index("if (r4) {")
    assert re.search(r"r1 = useScrollOffsetNative;", js)
    assert re.search(r"\br2\[6\] = r1;", js)


def test_ternary_read_where_its_reader_stands_still_folds():
    js = _render_3(_TO_STRING, 3602)

    assert '(r4 <= -1 ? "?" : "&")' in js


# ----------------------------------------------------------------------------------------------------
# ternary_test_parens
#
# The test of a `? :` is printed without parentheses of its own when it is a comparison or a logical
# expression (F-32): `a == null ? x : y`, not `(a == null) ? x : y`. A ternary, an assignment or a sequence
# as the test, and a ternary used as an operand, keep their grouping.
# ----------------------------------------------------------------------------------------------------

def _print(node) -> str:
    return ExpressionPrinter().print(node)


def _ident(name):
    return Identifier(name=name)


def test_a_comparison_test_has_no_parentheses():
    test = BinaryExpression(left=_ident("a"), operator="==", right=NullLiteral())
    node = ConditionalExpression(test=test, consequent=UndefinedLiteral(), alternate=_ident("b"))

    assert _print(node) == "a == null ? undefined : b"


def test_a_logical_test_has_no_parentheses():
    test = BinaryExpression(left=_ident("a"), operator=LogicalOperator.AND, right=_ident("b"))
    node = ConditionalExpression(test=test, consequent=_ident("x"), alternate=_ident("y"))

    assert _print(node) == "a && b ? x : y"


def test_a_ternary_test_keeps_its_parentheses():
    inner = ConditionalExpression(test=_ident("a"), consequent=_ident("b"), alternate=_ident("c"))
    node = ConditionalExpression(test=inner, consequent=_ident("x"), alternate=_ident("y"))

    assert _print(node) == "(a ? b : c) ? x : y"


def test_a_ternary_as_an_operand_keeps_its_parentheses():
    inner = ConditionalExpression(test=_ident("a"), consequent=_ident("b"), alternate=_ident("c"))
    node = BinaryExpression(left=inner, operator="===", right=_ident("d"))

    assert _print(node) == "(a ? b : c) === d"


# ----------------------------------------------------------------------------------------------------
# typeof_guard_join
#
# The code a `typeof` test jumps to is the join when the arm's own test falls into it (F-183).
#
#     if (typeof x !== "object") goto T;
#     ...; if (r != null) return r;          // taken edge: a lone `return`; the fall goes on into T
#     T: <the next test>
#
# `_DominanceIfBuilder` kept a constant comparison (`typeof x ...`) away from the rule that makes the branch target
# the join (a `case` chain needs `has_else` at every link), so `T` stayed the `else` arm and the fall of the arm's
# test went to `return r` instead of into `T`: `if (r3 != null) goto label_86; return param1.key;` returned the key
# where the bytecode goes on to the second `typeof`. A `typeof` kind test is never a `case` label, so it now takes
# the rule when the arm's test is of anything else.
#
# Only `typeof` tests: widening it to every constant comparison turned a `return` copy into an assignment plus a
# shared `return` for 98/6630 `getInitialURL` (`IfTailMergeRegionPass` hoisted the `return` of a block a guard
# still jumped to) and was dropped.
#
#     98/4239  `keyExtractor`
#     98/2147  `processColor`
# ----------------------------------------------------------------------------------------------------

def _render_4(name: str, function_id: int) -> str:
    hasm = (_DATA / name).read_text(encoding="utf-8")
    out = Decompiler.render(Decompiler.build_context(hasm, function_id, strict=False), verbose=False, raw=False)

    return "\n".join(line for line in out.split("\n") if not line.strip().startswith("//"))


def test_the_second_type_test_follows_the_first_one():
    out = _render_4("typeof_guard_join_98_4239.hasm", 4239)

    assert "goto" not in out
    assert out.count('if (typeof param1 === "object") {') == 2
    assert out.count("return param1.key;") == 1
    assert out.index("return param1.key;") < out.index("return param1.id;")
    assert out.rstrip().endswith("return r3;\n}")


def test_a_null_result_goes_on_to_the_number_test():
    out = _render_4("typeof_guard_join_98_2147.hasm", 2147)

    assert "goto" not in out
    assert "if (r6 != null) {\n                    return r6;\n                }" in out
    assert out.index("return r6;") < out.index('if (typeof r7 !== "number") {')


# ----------------------------------------------------------------------------------------------------
# typeof_mask
#
# `TypeOfIs` / `JmpTypeOfIs` decode their `TypeOfIsTypes` bitmask with the bit
# assignment `hermesc` itself uses (bytecode 98). The masks below are what
# `hermesc -dump-bytecode` printed for the matching source:
#
#     typeof x === "undefined" -> 1       typeof x === "bigint"   -> 64
#     typeof x === "string"    -> 4       typeof x === "function" -> 128
#     typeof x === "symbol"    -> 8       typeof x === "object"   -> 258 (null | object)
#     typeof x === "boolean"   -> 16      typeof x !== "object"   -> 253
#     typeof x === "number"    -> 32
#
# The old tables were guesses: `4` read as boolean, `16` as string, `64` as
# `function`, `128` as `bigint` (`TypeOfIs`), and `258` stayed unresolved
# (98/9594, F-02).
# ----------------------------------------------------------------------------------------------------

def _print_2(mask: int) -> str:
    return ExpressionPrinter().visit(build_typeof_condition(Identifier("x"), mask))


@pytest.mark.parametrize(
    ("mask", "expected"),
    [
        (1, 'typeof x === "undefined"'),
        (4, 'typeof x === "string"'),
        (8, 'typeof x === "symbol"'),
        (16, 'typeof x === "boolean"'),
        (32, 'typeof x === "number"'),
        (64, 'typeof x === "bigint"'),
        (128, 'typeof x === "function"'),
        (258, 'typeof x === "object"'),
    ],
)
def test_single_type_masks_are_the_ones_hermesc_emits(mask, expected):
    assert _print_2(mask) == expected


@pytest.mark.parametrize(
    ("mask", "expected"),
    [
        (253, 'typeof x !== "object"'),
        (495, 'typeof x !== "boolean"'),
        (383, 'typeof x !== "function"'),
    ],
)
def test_a_mask_covering_most_types_is_written_as_its_complement(mask, expected):
    assert _print_2(mask) == expected


def test_a_few_types_stay_a_positive_chain_in_bit_order():
    assert _print_2(4 | 32) == 'typeof x === "string" || typeof x === "number"'
    assert _print_2(258 | 128) == 'typeof x === "function" || typeof x === "object"'


def test_one_half_of_object_is_not_a_plain_typeof_test():
    assert _print_2(2) == "x === null"
    assert _print_2(256) == 'typeof x === "object" && x !== null'


@pytest.mark.parametrize("mask", [0, 512, 1 << 12])
def test_unknown_masks_stay_visibly_unresolved(mask):
    assert "<unresolved_typeof_mask_" in _print_2(mask)


# ----------------------------------------------------------------------------------------------------
# typeof_register_join
#
# `if (r5 !== "object") { <typeof checks> } else { ...; if (r2 != null) return r2; }` where the else arm's test falls
# into the very `typeof` checks the branch jumps to (F-210, 96/1139 `processColor`).
#
# `r5 = typeof r6` stays in a register (the target tests `r5 !== "number"` again), so the branch condition was no
# `typeof x` test and `_arm_retests_constant` did not see that the arm's other test runs on into the branch
# target. The target was printed as the `then` arm, the arm's test as `if (r2 != null) goto L; return r2`
# (the fall-through into the checks lost). The target is now the join after `if (r5 === "object") { ... }`.
# ----------------------------------------------------------------------------------------------------

def _code_3() -> str:
    hasm = (_DATA / "typeof_register_join_96_1139.hasm").read_text(encoding="utf-8")
    out = Decompiler.render(Decompiler.build_context(hasm, 1139, strict=False), verbose=False, raw=False)

    return "\n".join(line for line in out.split("\n") if not line.strip().startswith("//"))


def test_the_typeof_checks_follow_the_object_branch():
    code = _code_3()

    assert "goto" not in code
    assert 'if (r5 === "object") {' in code
    assert "if (r2 != null) {\n                    return r2;\n                }\n            }\n            if (r5 !== \"number\") {" in code


# ----------------------------------------------------------------------------------------------------
# value_diamond_with_call
#
# A value diamond with ONE call in an arm, tested as the next link of an `&&` chain (98/12704 `_initBody`).
#
# `else if (support.arrayBuffer && support.blob && isDataView(body))` compiles to
# `X: if (!arrayBuffer || !blob) goto T; r7 = body && DataView.prototype.isPrototypeOf(body) [a diamond]; M: if (r7) goto DVARM; T: ...`.
# `ValueConditionFoldCfgPass` only folded diamonds whose arms were all pure, so the diamond stayed three blocks and
# `T` was entered from X and from M's fall-through: the printed `if (r7) goto label_442;` jumped to the very code below
# it and the not-DataView path (`T`) was lost. A call evaluated inside the value runs on the same path as in the arm,
# so ONE of them is allowed when the diamond is that link of a chain (`_crossed_into`); the receiver the call keeps by
# name (`r9 = DataView.prototype; r9.isPrototypeOf(p)`) goes into the value.
# ----------------------------------------------------------------------------------------------------

def _render_5(name, index):
    hasm = (_DATA / name).read_text(encoding="utf-8")

    return Decompiler.render(Decompiler.build_context(hasm, index, strict=False), verbose=False, raw=False)


def test_the_dataview_test_joins_the_and_chain():
    out = _render_5("value_diamond_with_call_98_12704.hasm", 12704)

    assert "goto" not in out
    assert "r5.arrayBuffer && r5.blob && (param1 && DataView.prototype.isPrototypeOf(param1))" in out


def test_a_guarded_call_in_the_condition_reads_the_right_register():
    out = _render_5("value_diamond_with_call_98_9957.hasm", 9957)

    assert "param1 === r3 && (r1[0] && r1[0].onDismiss)" in out
    assert "r4 = r1[0];\n            r3 = r4.onDismiss();" in out


# ----------------------------------------------------------------------------------------------------
# value_fold_optional_chain
#
# `a?.b || a?.c` used as a test folds into one condition (F-221, 98/7639 `resolveSource`).
#
#     r6 = undefined; if (a == null) goto M; r6 = a.b; M: if (r6) goto BODY
#
# The jump to `M` itself keeps the value the head block just wrote. `ValueConditionFoldCfgPass` only followed jumps
# through arm blocks, so the diamond stayed, and the second test printed `if (r6) goto L` into the body.
# ----------------------------------------------------------------------------------------------------

def test_the_optional_chain_tests_fold_into_one_condition():
    hasm = (_DATA / "value_fold_optional_chain_98_7639.hasm").read_text(encoding="utf-8")
    out = Decompiler.render(Decompiler.build_context(hasm, 7639, strict=False), verbose=False, raw=False)
    code = "\n".join(line for line in out.split("\n") if not line.strip().startswith("//"))

    assert "goto" not in code
    assert 'typeof param1 === "object" && ((param1 == null ? undefined : param1.blurhash) || ' in code
