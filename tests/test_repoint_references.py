"""
`repoint_references` makes every reader of a folded expression see the
fold's result instead. Readers live in more places than the instruction
list (block terminators, `IfRegion.condition`, ...), and a stale
`definition_used` flag can make the fold's own result vanish from the
output. See `hermes_decompiler/backend/transforms/shared/_repoint.py`.
"""

from __future__ import annotations

import dataclasses

from hermes_decompiler.Decompiler import Decompiler
from hermes_decompiler.backend.transforms.shared._repoint import (
    MAX_INLINED_CONDITION_NODES,
    _node_count,
    repoint_node,
)
from hermes_decompiler.ir.expressions import (
    BinaryExpression,
    CallExpression,
    ConditionalExpression,
    Identifier,
    NullLiteral,
    NumericLiteral,
    UndefinedLiteral,
)
from hermes_decompiler.ir.Operators import LogicalOperator


def call(name: str) -> CallExpression:
    return CallExpression(callee=Identifier(name=name), arguments=())


def render(hasm: str, index: int) -> str:
    out = Decompiler.render(Decompiler.build_context(hasm, index), verbose=False)

    return "\n".join(line for line in out.split("\n") if not line.strip().startswith("//"))


# ---------------------------------------------------------------------------
# repoint_node
# ---------------------------------------------------------------------------


def test_replaces_by_identity_at_the_top_level():
    old, new = Identifier(name="r1"), call("f")

    result, changed = repoint_node(old, old, new)

    assert changed
    assert result is new


def test_replaces_by_identity_nested_inside_a_binary_expression():
    old, new = call("f"), NumericLiteral(value=1)
    tree = BinaryExpression(left=Identifier(name="a"), operator=LogicalOperator.AND, right=old)

    result, changed = repoint_node(tree, old, new)

    assert changed
    assert result.right is new
    assert result.left is tree.left  # untouched siblings are not rebuilt


def test_replaces_every_occurrence_in_a_tuple_field():
    old, new = Identifier(name="x"), Identifier(name="y")
    tree = CallExpression(callee=Identifier(name="f"), arguments=(old, NumericLiteral(value=1), old))

    result, changed = repoint_node(tree, old, new)

    assert changed
    # IR nodes compare by identity (`eq=False`), so check that shape and
    # identity directly rather than with `==`.
    a, b, c = result.arguments
    assert a is new and c is new
    assert isinstance(b, NumericLiteral) and b.value == 1 and b is not old


def test_leaves_the_tree_alone_when_the_target_does_not_occur():
    tree = BinaryExpression(left=Identifier(name="a"), operator=LogicalOperator.AND, right=Identifier(name="b"))

    result, changed = repoint_node(tree, Identifier(name="c"), NumericLiteral(value=1))

    assert not changed
    assert result is tree


def test_a_trivial_node_is_matched_only_by_identity_not_by_equal_value():
    # Two UNRELATED `null` literals must never be conflated - only the
    # exact object that was folded may be replaced (this was a real bug:
    # every `null` in a function was rewritten by structural equality).
    target = NullLiteral()
    other_null = NullLiteral()
    tree = BinaryExpression(left=other_null, operator=LogicalOperator.OR, right=Identifier(name="a"))

    result, changed = repoint_node(tree, target, Identifier(name="replaced"))

    assert not changed
    assert result is tree


def test_a_nontrivial_node_may_be_matched_structurally_as_well_as_by_identity():
    # A `Mov`-introduced COPY of the folded expression (same shape, not the
    # same object) is still a real duplicate and should be caught.
    old = ConditionalExpression(
        test=Identifier(name="c"), consequent=NumericLiteral(value=1), alternate=NumericLiteral(value=2)
    )
    copy = dataclasses.replace(old)  # equal shape, different object
    new = Identifier(name="folded")

    result, changed = repoint_node(copy, old, new)

    assert changed
    assert result is new


# ---------------------------------------------------------------------------
# _node_count (drives the MAX_INLINED_CONDITION_NODES size bound)
# ---------------------------------------------------------------------------


def test_node_count_of_a_leaf_is_one():
    assert _node_count(Identifier(name="a"), limit=10) == 1


def test_node_count_adds_up_children():
    tree = BinaryExpression(left=Identifier(name="a"), operator=LogicalOperator.AND, right=Identifier(name="b"))

    assert _node_count(tree, limit=10) == 3


def test_node_count_stops_once_the_limit_is_reached():
    # A long chain of the same shape must not be walked past `limit` -
    # this bound is what keeps a chain of folds from inlining an
    # exponentially growing expression into every condition.
    tree = UndefinedLiteral()

    for _ in range(50):
        tree = BinaryExpression(left=tree, operator=LogicalOperator.AND, right=Identifier(name="x"))

    assert _node_count(tree, limit=5) >= 5


# ---------------------------------------------------------------------------
# End-to-end: the register-read resolution bugs this module fixes
# ---------------------------------------------------------------------------

# hbc96 function #12962 (color-convert's Lab -> XYZ). Hermes computes each
# `x ** 3` unconditionally, BEFORE the ternary that conditionally uses it:
#
#   r2 = exponentiationOperator(r9, r8, r7)          // unconditional
#   if (!(r2 > 0.008856)) r2 = (r7 - 0.138) / 7.787   // then overwritten
#
# `ConditionalExpressionRegionPass` folds this back into the source's
# `x > 0.008856 ? x ** 3 : ...`. Structural equality without the trivial-
# literal fix, or a `condition_replacement` without the size bound, both
# broke this function - the first by rewriting the WRONG `null`s elsewhere
# in the codebase, the second by exploding the output as the fold chained.
LAB_TO_XYZ = r"""
=> [Function #12962 "" of 248 bytes]: 2 params, frame size=17, strict=0, exc handler=0, debug info=0  @ offset 0x002348c2

Bytecode listing:

==> 00000000: <LoadParam>: <Reg8: 1, UInt8: 1>
==> 00000003: <LoadConstZero>: <Reg8: 0>
==> 00000005: <GetByVal>: <Reg8: 3, Reg8: 1, Reg8: 0>
==> 00000009: <LoadConstUInt8>: <Reg8: 0, UInt8: 1>
==> 0000000c: <GetByVal>: <Reg8: 2, Reg8: 1, Reg8: 0>
==> 00000010: <LoadConstUInt8>: <Reg8: 0, UInt8: 2>
==> 00000013: <GetByVal>: <Reg8: 1, Reg8: 1, Reg8: 0>
==> 00000017: <LoadConstUInt8>: <Reg8: 0, UInt8: 16>
==> 0000001a: <Add>: <Reg8: 3, Reg8: 3, Reg8: 0>
==> 0000001e: <LoadConstUInt8>: <Reg8: 0, UInt8: 116>
==> 00000021: <Div>: <Reg8: 7, Reg8: 3, Reg8: 0>
==> 00000025: <LoadConstInt>: <Reg8: 0, Imm32: 500>
==> 0000002b: <Div>: <Reg8: 0, Reg8: 2, Reg8: 0>
==> 0000002f: <AddN>: <Reg8: 6, Reg8: 0, Reg8: 7>
==> 00000033: <LoadConstUInt8>: <Reg8: 0, UInt8: 200>
==> 00000036: <Div>: <Reg8: 0, Reg8: 1, Reg8: 0>
==> 0000003a: <SubN>: <Reg8: 4, Reg8: 7, Reg8: 0>
==> 0000003e: <LoadConstUInt8>: <Reg8: 0, UInt8: 3>
==> 00000041: <Mov>: <Reg8: 9, Reg8: 7>
==> 00000044: <Mov>: <Reg8: 8, Reg8: 0>
==> 00000047: <CallBuiltin>: <Reg8: 2, UInt8: 49, UInt8: 3>  # Built-in function: [#49 exponentiationOperator]
==> 0000004b: <Mov>: <Reg8: 9, Reg8: 6>
==> 0000004e: <CallBuiltin>: <Reg8: 3, UInt8: 49, UInt8: 3>  # Built-in function: [#49 exponentiationOperator]
==> 00000052: <Mov>: <Reg8: 9, Reg8: 4>
==> 00000055: <CallBuiltin>: <Reg8: 1, UInt8: 49, UInt8: 3>  # Built-in function: [#49 exponentiationOperator]
==> 00000059: <LoadConstDouble>: <Reg8: 0, Double: 0.008856>
==> 00000063: <JGreater>: <Addr8: 32, Reg8: 2, Reg8: 0>  # Address: 00000083
==> 00000067: <LoadConstDouble>: <Reg8: 5, Double: 0.13793103448275862>
==> 00000071: <SubN>: <Reg8: 7, Reg8: 7, Reg8: 5>
==> 00000075: <LoadConstDouble>: <Reg8: 5, Double: 7.787>
==> 0000007f: <DivN>: <Reg8: 2, Reg8: 7, Reg8: 5>
==> 00000083: <JGreater>: <Addr8: 32, Reg8: 3, Reg8: 0>  # Address: 000000a3
==> 00000087: <LoadConstDouble>: <Reg8: 5, Double: 0.13793103448275862>
==> 00000091: <SubN>: <Reg8: 6, Reg8: 6, Reg8: 5>
==> 00000095: <LoadConstDouble>: <Reg8: 5, Double: 7.787>
==> 0000009f: <DivN>: <Reg8: 3, Reg8: 6, Reg8: 5>
==> 000000a3: <JGreater>: <Addr8: 32, Reg8: 1, Reg8: 0>  # Address: 000000c3
==> 000000a7: <LoadConstDouble>: <Reg8: 0, Double: 0.13793103448275862>
==> 000000b1: <SubN>: <Reg8: 4, Reg8: 4, Reg8: 0>
==> 000000b5: <LoadConstDouble>: <Reg8: 0, Double: 7.787>
==> 000000bf: <DivN>: <Reg8: 1, Reg8: 4, Reg8: 0>
==> 000000c3: <LoadConstDouble>: <Reg8: 0, Double: 95.047>
==> 000000cd: <Mul>: <Reg8: 3, Reg8: 3, Reg8: 0>
==> 000000d1: <LoadConstUInt8>: <Reg8: 0, UInt8: 100>
==> 000000d4: <Mul>: <Reg8: 2, Reg8: 2, Reg8: 0>
==> 000000d8: <LoadConstDouble>: <Reg8: 0, Double: 108.883>
==> 000000e2: <Mul>: <Reg8: 1, Reg8: 1, Reg8: 0>
==> 000000e6: <NewArray>: <Reg8: 0, UInt16: 3>
==> 000000ea: <PutOwnByIndex>: <Reg8: 0, Reg8: 3, UInt8: 0>
==> 000000ee: <PutOwnByIndex>: <Reg8: 0, Reg8: 2, UInt8: 1>
==> 000000f2: <PutOwnByIndex>: <Reg8: 0, Reg8: 1, UInt8: 2>
==> 000000f6: <Ret>: <Reg8: 0>


"""


def test_hoisted_pure_call_folds_back_into_the_source_ternary():
    out = render(LAB_TO_XYZ, 12962)

    import re

    # The three assignments, one per Lab channel (the `return` line repeats
    # the same three expressions, which is why this matches assignments only).
    assignments = [
        line for line in out.split("\n")
        if re.match(r"\s*r\d+ = \(r\d+ > 0\.008856\) \? exponentiationOperator\(", line)
    ]

    assert len(assignments) == 3, out


# hbc96 function #13033 (React Navigation's `Header`). A three-way OR chain
# (`this && this.__importStar || function_12268()`) folds in two steps; the
# SECOND fold's condition must see the FIRST fold's merged value, not the
# stale single-arm value the bytecode originally read - otherwise
# `BooleanChainRegionPass` fails to recognise the chain and the call inside
# it is silently dropped from the output.
HEADER = r"""
=> [Function #13033 "Header" of 2558 bytes]: 2 params, frame size=100, strict=1, exc handler=1, debug info=0  @ offset 0x002367b1
  [Exception handlers: [start=0x413, end=0x446, target=0x448] ]

Bytecode listing:

==> 00000000: <LoadParam>: <Reg8: 4, UInt8: 1>
==> 00000003: <CreateEnvironment>: <Reg8: 14>
==> 00000005: <LoadConstUndefined>: <Reg8: 3>
==> 00000007: <LoadConstUndefined>: <Reg8: 9>
==> 00000009: <LoadConstUndefined>: <Reg8: 41>
==> 0000000b: <GetEnvironment>: <Reg8: 10, UInt8: 0>
==> 0000000e: <LoadFromEnvironment>: <Reg8: 0, Reg8: 10, UInt8: 7>
==> 00000012: <GetById>: <Reg8: 0, Reg8: 0, UInt8: 1, string_id: 18542>  # String: 'useSafeAreaInsets' (Identifier)
==> 00000018: <Call1>: <Reg8: 28, Reg8: 0, Reg8: 3>
==> 0000001c: <LoadFromEnvironment>: <Reg8: 0, Reg8: 10, UInt8: 9>
==> 00000020: <GetById>: <Reg8: 2, Reg8: 0, UInt8: 2, string_id: 14424>  # String: 'useFrameSize' (Identifier)
==> 00000026: <CreateClosure>: <Reg8: 1, Reg8: 14, function_id: 13034>  # Function: [#13034  of 5 bytes]: 2 params @ offset 0x000f81fc
==> 0000002b: <LoadConstTrue>: <Reg8: 0>
==> 0000002d: <Call3>: <Reg8: 1, Reg8: 2, Reg8: 3, Reg8: 1, Reg8: 0>
==> 00000033: <LoadFromEnvironment>: <Reg8: 0, Reg8: 10, UInt8: 3>
==> 00000037: <GetById>: <Reg8: 0, Reg8: 0, UInt8: 3, string_id: 15138>  # String: 'useTheme' (Identifier)
==> 0000003d: <Call1>: <Reg8: 0, Reg8: 0, Reg8: 3>
==> 00000041: <GetById>: <Reg8: 0, Reg8: 0, UInt8: 4, string_id: 7462>  # String: 'colors' (Identifier)
==> 00000047: <LoadFromEnvironment>: <Reg8: 2, Reg8: 10, UInt8: 3>
==> 0000004b: <GetById>: <Reg8: 2, Reg8: 2, UInt8: 5, string_id: 14985>  # String: 'useNavigation' (Identifier)
==> 00000051: <Call1>: <Reg8: 25, Reg8: 2, Reg8: 3>
==> 00000055: <LoadFromEnvironment>: <Reg8: 6, Reg8: 10, UInt8: 5>
==> 00000059: <GetByIdShort>: <Reg8: 5, Reg8: 6, UInt8: 6, string_id: 249>  # String: 'useContext' (Identifier)
==> 0000005e: <LoadFromEnvironment>: <Reg8: 2, Reg8: 10, UInt8: 16>
==> 00000062: <GetById>: <Reg8: 2, Reg8: 2, UInt8: 7, string_id: 14195>  # String: 'HeaderShownContext' (Identifier)
==> 00000068: <Call2>: <Reg8: 7, Reg8: 5, Reg8: 6, Reg8: 2>
==> 0000006d: <LoadFromEnvironment>: <Reg8: 5, Reg8: 10, UInt8: 5>
==> 00000071: <GetByIdShort>: <Reg8: 2, Reg8: 5, UInt8: 8, string_id: 252>  # String: 'useState' (Identifier)
==> 00000076: <LoadConstFalse>: <Reg8: 38>
==> 00000078: <Call2>: <Reg8: 5, Reg8: 2, Reg8: 5, Reg8: 38>
==> 0000007d: <LoadFromEnvironment>: <Reg8: 2, Reg8: 10, UInt8: 2>
==> 00000081: <GetByIdShort>: <Reg8: 2, Reg8: 2, UInt8: 9, string_id: 107>  # String: 'default' (Identifier)
==> 00000086: <LoadConstUInt8>: <Reg8: 42, UInt8: 2>
==> 00000089: <Call3>: <Reg8: 2, Reg8: 2, Reg8: 3, Reg8: 5, Reg8: 42>
==> 0000008f: <LoadConstZero>: <Reg8: 44>
==> 00000091: <GetByVal>: <Reg8: 17, Reg8: 2, Reg8: 44>
==> 00000095: <LoadConstUInt8>: <Reg8: 39, UInt8: 1>
==> 00000098: <GetByVal>: <Reg8: 2, Reg8: 2, Reg8: 39>
==> 0000009c: <StoreToEnvironment>: <Reg8: 14, UInt8: 0, Reg8: 2>
==> 000000a0: <LoadFromEnvironment>: <Reg8: 5, Reg8: 10, UInt8: 5>
==> 000000a4: <GetByIdShort>: <Reg8: 2, Reg8: 5, UInt8: 8, string_id: 252>  # String: 'useState' (Identifier)
==> 000000a9: <Call2>: <Reg8: 5, Reg8: 2, Reg8: 5, Reg8: 3>
==> 000000ae: <LoadFromEnvironment>: <Reg8: 2, Reg8: 10, UInt8: 2>
==> 000000b2: <GetByIdShort>: <Reg8: 2, Reg8: 2, UInt8: 9, string_id: 107>  # String: 'default' (Identifier)
==> 000000b7: <Call3>: <Reg8: 2, Reg8: 2, Reg8: 3, Reg8: 5, Reg8: 42>
==> 000000bd: <GetByVal>: <Reg8: 24, Reg8: 2, Reg8: 44>
==> 000000c1: <GetByVal>: <Reg8: 2, Reg8: 2, Reg8: 39>
==> 000000c5: <StoreToEnvironment>: <Reg8: 14, UInt8: 1, Reg8: 2>
==> 000000c9: <GetByIdShort>: <Reg8: 40, Reg8: 4, UInt8: 10, string_id: 64>  # String: 'layout' (Identifier)
==> 000000ce: <JStrictNotEqual>: <Addr8: 7, Reg8: 40, Reg8: 3>  # Address: 000000d5
==> 000000d2: <Mov>: <Reg8: 40, Reg8: 1>
==> 000000d5: <GetById>: <Reg8: 1, Reg8: 4, UInt8: 11, string_id: 9381>  # String: 'modal' (Identifier)
==> 000000db: <LoadConstFalse>: <Reg8: 6>
==> 000000dd: <JStrictEqual>: <Addr8: 7, Reg8: 1, Reg8: 3>  # Address: 000000e4
==> 000000e1: <Mov>: <Reg8: 6, Reg8: 1>
==> 000000e4: <GetById>: <Reg8: 5, Reg8: 4, UInt8: 12, string_id: 7396>  # String: 'back' (Identifier)
==> 000000ea: <GetByIdShort>: <Reg8: 34, Reg8: 4, UInt8: 13, string_id: 241>  # String: 'title' (Identifier)
==> 000000ef: <GetById>: <Reg8: 27, Reg8: 4, UInt8: 14, string_id: 17795>  # String: 'headerTitle' (Identifier)
==> 000000f5: <GetById>: <Reg8: 1, Reg8: 4, UInt8: 15, string_id: 17796>  # String: 'headerTitleAlign' (Identifier)
==> 000000fb: <LoadConstString>: <Reg8: 37, string_id: 74>  # String: 'left' (Identifier)
==> 000000ff: <Mov>: <Reg8: 36, Reg8: 37>
==> 00000102: <JStrictEqual>: <Addr8: 7, Reg8: 1, Reg8: 3>  # Address: 00000109
==> 00000106: <Mov>: <Reg8: 36, Reg8: 1>
==> 00000109: <GetById>: <Reg8: 2, Reg8: 4, UInt8: 16, string_id: 17775>  # String: 'headerLeft' (Identifier)
==> 0000010f: <JStrictNotEqual>: <Addr8: 17, Reg8: 2, Reg8: 3>  # Address: 00000120
==> 00000113: <LoadConstUndefined>: <Reg8: 1>
==> 00000115: <JmpFalse>: <Addr8: 8, Reg8: 5>  # Address: 0000011d
==> 00000118: <CreateClosure>: <Reg8: 1, Reg8: 14, function_id: 13037>  # Function: [#13037  of 44 bytes]: 2 params @ offset 0x00237221
==> 0000011d: <Mov>: <Reg8: 2, Reg8: 1>
==> 00000120: <GetById>: <Reg8: 16, Reg8: 4, UInt8: 17, string_id: 17784>  # String: 'headerSearchBarOptions' (Identifier)
==> 00000126: <StoreToEnvironment>: <Reg8: 14, UInt8: 2, Reg8: 16>
==> 0000012a: <GetById>: <Reg8: 22, Reg8: 4, UInt8: 18, string_id: 17298>  # String: 'headerTransparent' (Identifier)
==> 00000130: <GetById>: <Reg8: 15, Reg8: 4, UInt8: 19, string_id: 17793>  # String: 'headerTintColor' (Identifier)
==> 00000136: <GetById>: <Reg8: 12, Reg8: 4, UInt8: 20, string_id: 17480>  # String: 'headerBackground' (Identifier)
==> 0000013c: <GetById>: <Reg8: 1, Reg8: 4, UInt8: 21, string_id: 17781>  # String: 'headerRight' (Identifier)
==> 00000142: <GetById>: <Reg8: 33, Reg8: 4, UInt8: 22, string_id: 9231>  # String: 'headerTitleAllowFontScaling' (Identifier)
==> 00000148: <GetById>: <Reg8: 31, Reg8: 4, UInt8: 23, string_id: 17799>  # String: 'headerTitleStyle' (Identifier)
==> 0000014e: <GetById>: <Reg8: 19, Reg8: 4, UInt8: 24, string_id: 17777>  # String: 'headerLeftContainerStyle' (Identifier)
==> 00000154: <GetById>: <Reg8: 26, Reg8: 4, UInt8: 25, string_id: 17783>  # String: 'headerRightContainerStyle' (Identifier)
==> 0000015a: <GetById>: <Reg8: 35, Reg8: 4, UInt8: 26, string_id: 17798>  # String: 'headerTitleContainerStyle' (Identifier)
==> 00000160: <GetById>: <Reg8: 8, Reg8: 4, UInt8: 27, string_id: 8486>  # String: 'headerBackButtonDisplayMode' (Identifier)
==> 00000166: <LoadConstString>: <Reg8: 48, string_id: 6745>  # String: 'minimal' (String)
==> 0000016a: <Mov>: <Reg8: 47, Reg8: 48>
==> 0000016d: <JStrictEqual>: <Addr8: 7, Reg8: 8, Reg8: 3>  # Address: 00000174
==> 00000171: <Mov>: <Reg8: 47, Reg8: 8>
==> 00000174: <GetById>: <Reg8: 23, Reg8: 4, UInt8: 28, string_id: 17274>  # String: 'headerBackTitleStyle' (Identifier)
==> 0000017a: <GetById>: <Reg8: 8, Reg8: 4, UInt8: 29, string_id: 17481>  # String: 'headerBackgroundContainerStyle' (Identifier)
==> 00000180: <GetById>: <Reg8: 13, Reg8: 4, UInt8: 30, string_id: 17789>  # String: 'headerStyle' (Identifier)
==> 00000186: <GetById>: <Reg8: 32, Reg8: 4, UInt8: 31, string_id: 17785>  # String: 'headerShadowVisible' (Identifier)
==> 0000018c: <GetById>: <Reg8: 30, Reg8: 4, UInt8: 32, string_id: 17778>  # String: 'headerPressColor' (Identifier)
==> 00000192: <GetById>: <Reg8: 29, Reg8: 4, UInt8: 33, string_id: 17780>  # String: 'headerPressOpacity' (Identifier)
==> 00000198: <GetById>: <Reg8: 11, Reg8: 4, UInt8: 34, string_id: 17788>  # String: 'headerStatusBarHeight' (Identifier)
==> 0000019e: <JStrictNotEqual>: <Addr8: 17, Reg8: 11, Reg8: 3>  # Address: 000001af
==> 000001a2: <LoadConstZero>: <Reg8: 4>
==> 000001a4: <JmpTrue>: <Addr8: 8, Reg8: 7>  # Address: 000001ac
==> 000001a7: <GetByIdShort>: <Reg8: 4, Reg8: 28, UInt8: 35, string_id: 73>  # String: 'top' (Identifier)
==> 000001ac: <Mov>: <Reg8: 11, Reg8: 4>
==> 000001af: <LoadFromEnvironment>: <Reg8: 4, Reg8: 10, UInt8: 10>
==> 000001b3: <GetById>: <Reg8: 4, Reg8: 4, UInt8: 36, string_id: 11476>  # String: 'getDefaultHeaderHeight' (Identifier)
==> 000001b9: <Call4>: <Reg8: 4, Reg8: 4, Reg8: 3, Reg8: 40, Reg8: 6, Reg8: 11>
==> 000001c0: <LoadFromEnvironment>: <Reg8: 6, Reg8: 10, UInt8: 6>
==> 000001c4: <GetByIdShort>: <Reg8: 7, Reg8: 6, UInt8: 37, string_id: 36>  # String: 'StyleSheet' (Identifier)
==> 000001c9: <GetById>: <Reg8: 6, Reg8: 7, UInt8: 38, string_id: 8232>  # String: 'flatten' (Identifier)
==> 000001cf: <JmpTrue>: <Addr8: 5, Reg8: 13>  # Address: 000001d4
==> 000001d2: <NewObject>: <Reg8: 13>
==> 000001d4: <Call2>: <Reg8: 89, Reg8: 6, Reg8: 7, Reg8: 13>
==> 000001d9: <GetByIdShort>: <Reg8: 21, Reg8: 89, UInt8: 39, string_id: 17>  # String: 'height' (Identifier)
==> 000001de: <JStrictNotEqual>: <Addr8: 7, Reg8: 21, Reg8: 3>  # Address: 000001e5
==> 000001e2: <Mov>: <Reg8: 21, Reg8: 4>
==> 000001e5: <GetById>: <Reg8: 7, Reg8: 89, UInt8: 40, string_id: 18154>  # String: 'maxHeight' (Identifier)
==> 000001eb: <GetById>: <Reg8: 20, Reg8: 89, UInt8: 41, string_id: 11463>  # String: 'minHeight' (Identifier)
==> 000001f1: <GetById>: <Reg8: 87, Reg8: 89, UInt8: 42, string_id: 13951>  # String: 'backfaceVisibility' (Identifier)
==> 000001f7: <GetByIdShort>: <Reg8: 86, Reg8: 89, UInt8: 43, string_id: 67>  # String: 'backgroundColor' (Identifier)
==> 000001fc: <GetById>: <Reg8: 85, Reg8: 89, UInt8: 44, string_id: 16725>  # String: 'borderBlockColor' (Identifier)
==> 00000202: <GetById>: <Reg8: 84, Reg8: 89, UInt8: 45, string_id: 16740>  # String: 'borderBlockEndColor' (Identifier)
==> 00000208: <GetById>: <Reg8: 83, Reg8: 89, UInt8: 46, string_id: 16742>  # String: 'borderBlockStartColor' (Identifier)
==> 0000020e: <GetById>: <Reg8: 82, Reg8: 89, UInt8: 47, string_id: 16746>  # String: 'borderBottomColor' (Identifier)
==> 00000214: <GetById>: <Reg8: 81, Reg8: 89, UInt8: 48, string_id: 9606>  # String: 'borderBottomEndRadius' (Identifier)
==> 0000021a: <GetById>: <Reg8: 80, Reg8: 89, UInt8: 49, string_id: 9652>  # String: 'borderBottomLeftRadius' (Identifier)
==> 00000220: <GetById>: <Reg8: 79, Reg8: 89, UInt8: 50, string_id: 10103>  # String: 'borderBottomRightRadius' (Identifier)
==> 00000226: <GetById>: <Reg8: 78, Reg8: 89, UInt8: 51, string_id: 14741>  # String: 'borderBottomStartRadius' (Identifier)
==> 0000022c: <GetById>: <Reg8: 77, Reg8: 89, UInt8: 52, string_id: 7425>  # String: 'borderBottomWidth' (Identifier)
==> 00000232: <GetById>: <Reg8: 76, Reg8: 89, UInt8: 53, string_id: 16748>  # String: 'borderColor' (Identifier)
==> 00000238: <GetById>: <Reg8: 75, Reg8: 89, UInt8: 54, string_id: 16750>  # String: 'borderCurve' (Identifier)
==> 0000023e: <GetById>: <Reg8: 74, Reg8: 89, UInt8: 55, string_id: 16751>  # String: 'borderEndColor' (Identifier)
==> 00000244: <GetById>: <Reg8: 73, Reg8: 89, UInt8: 56, string_id: 14744>  # String: 'borderEndEndRadius' (Identifier)
==> 0000024a: <GetById>: <Reg8: 72, Reg8: 89, UInt8: 57, string_id: 10130>  # String: 'borderEndStartRadius' (Identifier)
==> 00000250: <GetById>: <Reg8: 71, Reg8: 89, UInt8: 58, string_id: 12524>  # String: 'borderEndWidth' (Identifier)
==> 00000256: <GetById>: <Reg8: 70, Reg8: 89, UInt8: 59, string_id: 14390>  # String: 'borderLeftColor' (Identifier)
==> 0000025c: <GetById>: <Reg8: 69, Reg8: 89, UInt8: 60, string_id: 12641>  # String: 'borderLeftWidth' (Identifier)
==> 00000262: <GetById>: <Reg8: 68, Reg8: 89, UInt8: 61, string_id: 14745>  # String: 'borderRadius' (Identifier)
==> 00000268: <GetById>: <Reg8: 67, Reg8: 89, UInt8: 62, string_id: 16753>  # String: 'borderRightColor' (Identifier)
==> 0000026e: <GetById>: <Reg8: 66, Reg8: 89, UInt8: 63, string_id: 13748>  # String: 'borderRightWidth' (Identifier)
==> 00000274: <GetById>: <Reg8: 65, Reg8: 89, UInt8: 64, string_id: 16755>  # String: 'borderStartColor' (Identifier)
==> 0000027a: <GetById>: <Reg8: 64, Reg8: 89, UInt8: 65, string_id: 8007>  # String: 'borderStartEndRadius' (Identifier)
==> 00000280: <GetById>: <Reg8: 63, Reg8: 89, UInt8: 66, string_id: 14746>  # String: 'borderStartStartRadius' (Identifier)
==> 00000286: <GetById>: <Reg8: 62, Reg8: 89, UInt8: 67, string_id: 13752>  # String: 'borderStartWidth' (Identifier)
==> 0000028c: <GetById>: <Reg8: 61, Reg8: 89, UInt8: 68, string_id: 16757>  # String: 'borderStyle' (Identifier)
==> 00000292: <GetById>: <Reg8: 60, Reg8: 89, UInt8: 69, string_id: 13043>  # String: 'borderTopColor' (Identifier)
==> 00000298: <GetById>: <Reg8: 59, Reg8: 89, UInt8: 70, string_id: 14749>  # String: 'borderTopEndRadius' (Identifier)
==> 0000029e: <GetById>: <Reg8: 58, Reg8: 89, UInt8: 71, string_id: 14617>  # String: 'borderTopLeftRadius' (Identifier)
==> 000002a4: <GetById>: <Reg8: 57, Reg8: 89, UInt8: 72, string_id: 14754>  # String: 'borderTopRightRadius' (Identifier)
==> 000002aa: <GetById>: <Reg8: 56, Reg8: 89, UInt8: 73, string_id: 9542>  # String: 'borderTopStartRadius' (Identifier)
==> 000002b0: <GetById>: <Reg8: 55, Reg8: 89, UInt8: 74, string_id: 13753>  # String: 'borderTopWidth' (Identifier)
==> 000002b6: <GetById>: <Reg8: 54, Reg8: 89, UInt8: 75, string_id: 13758>  # String: 'borderWidth' (Identifier)
==> 000002bc: <GetById>: <Reg8: 53, Reg8: 89, UInt8: 76, string_id: 10591>  # String: 'boxShadow' (Identifier)
==> 000002c2: <GetById>: <Reg8: 52, Reg8: 89, UInt8: 77, string_id: 15656>  # String: 'elevation' (Identifier)
==> 000002c8: <GetByIdShort>: <Reg8: 51, Reg8: 89, UInt8: 78, string_id: 137>  # String: 'filter' (Identifier)
==> 000002cd: <GetById>: <Reg8: 50, Reg8: 89, UInt8: 79, string_id: 10651>  # String: 'mixBlendMode' (Identifier)
==> 000002d3: <GetByIdShort>: <Reg8: 6, Reg8: 89, UInt8: 80, string_id: 188>  # String: 'opacity' (Identifier)
==> 000002d8: <GetById>: <Reg8: 49, Reg8: 89, UInt8: 81, string_id: 8173>  # String: 'shadowColor' (Identifier)
==> 000002de: <GetById>: <Reg8: 46, Reg8: 89, UInt8: 82, string_id: 9916>  # String: 'shadowOffset' (Identifier)
==> 000002e4: <GetById>: <Reg8: 43, Reg8: 89, UInt8: 83, string_id: 8172>  # String: 'shadowOpacity' (Identifier)
==> 000002ea: <GetById>: <Reg8: 18, Reg8: 89, UInt8: 84, string_id: 10021>  # String: 'shadowRadius' (Identifier)
==> 000002f0: <GetByIdShort>: <Reg8: 4, Reg8: 89, UInt8: 85, string_id: 243>  # String: 'transform' (Identifier)
==> 000002f5: <GetById>: <Reg8: 13, Reg8: 89, UInt8: 86, string_id: 8351>  # String: 'transformOrigin' (Identifier)
==> 000002fb: <LoadFromEnvironment>: <Reg8: 45, Reg8: 10, UInt8: 1>
==> 000002ff: <GetByIdShort>: <Reg8: 88, Reg8: 45, UInt8: 9, string_id: 107>  # String: 'default' (Identifier)
==> 00000304: <LoadFromEnvironment>: <Reg8: 45, Reg8: 10, UInt8: 0>
==> 00000308: <Call3>: <Reg8: 45, Reg8: 88, Reg8: 3, Reg8: 89, Reg8: 45>
==> 0000030e: <NewObject>: <Reg8: 45>
==> 00000310: <PutNewOwnById>: <Reg8: 45, Reg8: 87, string_id: 13951>  # String: 'backfaceVisibility' (Identifier)
==> 00000315: <PutNewOwnByIdShort>: <Reg8: 45, Reg8: 86, string_id: 67>  # String: 'backgroundColor' (Identifier)
==> 00000319: <PutNewOwnById>: <Reg8: 45, Reg8: 85, string_id: 16725>  # String: 'borderBlockColor' (Identifier)
==> 0000031e: <PutNewOwnById>: <Reg8: 45, Reg8: 84, string_id: 16740>  # String: 'borderBlockEndColor' (Identifier)
==> 00000323: <PutNewOwnById>: <Reg8: 45, Reg8: 83, string_id: 16742>  # String: 'borderBlockStartColor' (Identifier)
==> 00000328: <PutNewOwnById>: <Reg8: 45, Reg8: 82, string_id: 16746>  # String: 'borderBottomColor' (Identifier)
==> 0000032d: <PutNewOwnById>: <Reg8: 45, Reg8: 81, string_id: 9606>  # String: 'borderBottomEndRadius' (Identifier)
==> 00000332: <PutNewOwnById>: <Reg8: 45, Reg8: 80, string_id: 9652>  # String: 'borderBottomLeftRadius' (Identifier)
==> 00000337: <PutNewOwnById>: <Reg8: 45, Reg8: 79, string_id: 10103>  # String: 'borderBottomRightRadius' (Identifier)
==> 0000033c: <PutNewOwnById>: <Reg8: 45, Reg8: 78, string_id: 14741>  # String: 'borderBottomStartRadius' (Identifier)
==> 00000341: <PutNewOwnById>: <Reg8: 45, Reg8: 77, string_id: 7425>  # String: 'borderBottomWidth' (Identifier)
==> 00000346: <PutNewOwnById>: <Reg8: 45, Reg8: 76, string_id: 16748>  # String: 'borderColor' (Identifier)
==> 0000034b: <PutNewOwnById>: <Reg8: 45, Reg8: 75, string_id: 16750>  # String: 'borderCurve' (Identifier)
==> 00000350: <PutNewOwnById>: <Reg8: 45, Reg8: 74, string_id: 16751>  # String: 'borderEndColor' (Identifier)
==> 00000355: <PutNewOwnById>: <Reg8: 45, Reg8: 73, string_id: 14744>  # String: 'borderEndEndRadius' (Identifier)
==> 0000035a: <PutNewOwnById>: <Reg8: 45, Reg8: 72, string_id: 10130>  # String: 'borderEndStartRadius' (Identifier)
==> 0000035f: <PutNewOwnById>: <Reg8: 45, Reg8: 71, string_id: 12524>  # String: 'borderEndWidth' (Identifier)
==> 00000364: <PutNewOwnById>: <Reg8: 45, Reg8: 70, string_id: 14390>  # String: 'borderLeftColor' (Identifier)
==> 00000369: <PutNewOwnById>: <Reg8: 45, Reg8: 69, string_id: 12641>  # String: 'borderLeftWidth' (Identifier)
==> 0000036e: <PutNewOwnById>: <Reg8: 45, Reg8: 68, string_id: 14745>  # String: 'borderRadius' (Identifier)
==> 00000373: <PutNewOwnById>: <Reg8: 45, Reg8: 67, string_id: 16753>  # String: 'borderRightColor' (Identifier)
==> 00000378: <PutNewOwnById>: <Reg8: 45, Reg8: 66, string_id: 13748>  # String: 'borderRightWidth' (Identifier)
==> 0000037d: <PutNewOwnById>: <Reg8: 45, Reg8: 65, string_id: 16755>  # String: 'borderStartColor' (Identifier)
==> 00000382: <PutNewOwnById>: <Reg8: 45, Reg8: 64, string_id: 8007>  # String: 'borderStartEndRadius' (Identifier)
==> 00000387: <PutNewOwnById>: <Reg8: 45, Reg8: 63, string_id: 14746>  # String: 'borderStartStartRadius' (Identifier)
==> 0000038c: <PutNewOwnById>: <Reg8: 45, Reg8: 62, string_id: 13752>  # String: 'borderStartWidth' (Identifier)
==> 00000391: <PutNewOwnById>: <Reg8: 45, Reg8: 61, string_id: 16757>  # String: 'borderStyle' (Identifier)
==> 00000396: <PutNewOwnById>: <Reg8: 45, Reg8: 60, string_id: 13043>  # String: 'borderTopColor' (Identifier)
==> 0000039b: <PutNewOwnById>: <Reg8: 45, Reg8: 59, string_id: 14749>  # String: 'borderTopEndRadius' (Identifier)
==> 000003a0: <PutNewOwnById>: <Reg8: 45, Reg8: 58, string_id: 14617>  # String: 'borderTopLeftRadius' (Identifier)
==> 000003a5: <PutNewOwnById>: <Reg8: 45, Reg8: 57, string_id: 14754>  # String: 'borderTopRightRadius' (Identifier)
==> 000003aa: <PutNewOwnById>: <Reg8: 45, Reg8: 56, string_id: 9542>  # String: 'borderTopStartRadius' (Identifier)
==> 000003af: <PutNewOwnById>: <Reg8: 45, Reg8: 55, string_id: 13753>  # String: 'borderTopWidth' (Identifier)
==> 000003b4: <PutNewOwnById>: <Reg8: 45, Reg8: 54, string_id: 13758>  # String: 'borderWidth' (Identifier)
==> 000003b9: <PutNewOwnById>: <Reg8: 45, Reg8: 53, string_id: 10591>  # String: 'boxShadow' (Identifier)
==> 000003be: <PutNewOwnById>: <Reg8: 45, Reg8: 52, string_id: 15656>  # String: 'elevation' (Identifier)
==> 000003c3: <PutNewOwnByIdShort>: <Reg8: 45, Reg8: 51, string_id: 137>  # String: 'filter' (Identifier)
==> 000003c7: <PutNewOwnById>: <Reg8: 45, Reg8: 50, string_id: 10651>  # String: 'mixBlendMode' (Identifier)
==> 000003cc: <PutNewOwnByIdShort>: <Reg8: 45, Reg8: 6, string_id: 188>  # String: 'opacity' (Identifier)
==> 000003d0: <PutNewOwnById>: <Reg8: 45, Reg8: 49, string_id: 8173>  # String: 'shadowColor' (Identifier)
==> 000003d5: <PutNewOwnById>: <Reg8: 45, Reg8: 46, string_id: 9916>  # String: 'shadowOffset' (Identifier)
==> 000003da: <PutNewOwnById>: <Reg8: 45, Reg8: 43, string_id: 8172>  # String: 'shadowOpacity' (Identifier)
==> 000003df: <PutNewOwnById>: <Reg8: 45, Reg8: 18, string_id: 10021>  # String: 'shadowRadius' (Identifier)
==> 000003e4: <PutNewOwnByIdShort>: <Reg8: 45, Reg8: 4, string_id: 243>  # String: 'transform' (Identifier)
==> 000003e8: <PutNewOwnById>: <Reg8: 45, Reg8: 13, string_id: 8351>  # String: 'transformOrigin' (Identifier)
==> 000003ed: <Mov>: <Reg8: 9, Reg8: 45>
==> 000003f0: <GetGlobalObject>: <Reg8: 43>
==> 000003f2: <TryGetById>: <Reg8: 18, Reg8: 43, UInt8: 87, string_id: 24>  # String: 'Object' (Identifier)
==> 000003f8: <GetByIdShort>: <Reg8: 13, Reg8: 18, UInt8: 88, string_id: 132>  # String: 'entries' (Identifier)
==> 000003fd: <Call2>: <Reg8: 45, Reg8: 13, Reg8: 18, Reg8: 45>
==> 00000402: <Mov>: <Reg8: 13, Reg8: 45>
==> 00000405: <IteratorBegin>: <Reg8: 18, Reg8: 13>
==> 00000408: <IteratorNext>: <Reg8: 46, Reg8: 18, Reg8: 13>
==> 0000040c: <Mov>: <Reg8: 45, Reg8: 18>
==> 0000040f: <JStrictEqual>: <Addr8: 64, Reg8: 45, Reg8: 3>  # Address: 0000044f
==> 00000413: <LoadFromEnvironment>: <Reg8: 45, Reg8: 10, UInt8: 2>
==> 00000417: <GetByIdShort>: <Reg8: 45, Reg8: 45, UInt8: 9, string_id: 107>  # String: 'default' (Identifier)
==> 0000041c: <Call3>: <Reg8: 45, Reg8: 45, Reg8: 3, Reg8: 46, Reg8: 42>
==> 00000422: <GetByVal>: <Reg8: 41, Reg8: 45, Reg8: 44>
==> 00000426: <GetByVal>: <Reg8: 45, Reg8: 45, Reg8: 39>
==> 0000042a: <JStrictNotEqual>: <Addr8: 28, Reg8: 45, Reg8: 3>  # Address: 00000446
==> 0000042e: <TryGetById>: <Reg8: 50, Reg8: 43, UInt8: 89, string_id: 11496>  # String: 'Reflect' (Identifier)
==> 00000434: <GetById>: <Reg8: 49, Reg8: 50, UInt8: 90, string_id: 8263>  # String: 'deleteProperty' (Identifier)
==> 0000043a: <Mov>: <Reg8: 46, Reg8: 9>
==> 0000043d: <Mov>: <Reg8: 45, Reg8: 41>
==> 00000440: <Call3>: <Reg8: 45, Reg8: 49, Reg8: 50, Reg8: 46, Reg8: 45>
==> 00000446: <Jmp>: <Addr8: -62>  # Address: 00000408
==> 00000448: <Catch>: <Reg8: 13>
==> 0000044a: <IteratorClose>: <Reg8: 18, UInt8: 1>
==> 0000044d: <Throw>: <Reg8: 13>
==> 0000044f: <NewObject>: <Reg8: 18>
==> 00000451: <Mov>: <Reg8: 13, Reg8: 22>
==> 00000454: <JmpFalse>: <Addr8: 16, Reg8: 22>  # Address: 00000464
==> 00000457: <NewObject>: <Reg8: 39>
==> 00000459: <LoadConstString>: <Reg8: 41, string_id: 10354>  # String: 'transparent' (Identifier)
==> 0000045d: <PutNewOwnByIdShort>: <Reg8: 39, Reg8: 41, string_id: 67>  # String: 'backgroundColor' (Identifier)
==> 00000461: <Mov>: <Reg8: 13, Reg8: 39>
==> 00000464: <Mov>: <Reg8: 92, Reg8: 18>
==> 00000467: <Mov>: <Reg8: 91, Reg8: 13>
==> 0000046a: <CallBuiltin>: <Reg8: 13, UInt8: 44, UInt8: 3>  # Built-in function: [#44 copyDataProperties]
==> 0000046e: <Mov>: <Reg8: 13, Reg8: 22>
==> 00000471: <JmpTrue>: <Addr8: 7, Reg8: 13>  # Address: 00000478
==> 00000474: <StrictEq>: <Reg8: 13, Reg8: 32, Reg8: 38>
==> 00000478: <JmpFalse>: <Addr8: 30, Reg8: 13>  # Address: 00000496
==> 0000047b: <NewObject>: <Reg8: 32>
==> 0000047d: <PutNewOwnById>: <Reg8: 32, Reg8: 44, string_id: 7425>  # String: 'borderBottomWidth' (Identifier)
==> 00000482: <NewObject>: <Reg8: 38>
==> 00000484: <PutNewOwnById>: <Reg8: 38, Reg8: 44, string_id: 15656>  # String: 'elevation' (Identifier)
==> 00000489: <Mov>: <Reg8: 92, Reg8: 32>
==> 0000048c: <Mov>: <Reg8: 91, Reg8: 38>
==> 0000048f: <CallBuiltin>: <Reg8: 38, UInt8: 44, UInt8: 3>  # Built-in function: [#44 copyDataProperties]
==> 00000493: <Mov>: <Reg8: 13, Reg8: 32>
==> 00000496: <Mov>: <Reg8: 92, Reg8: 18>
==> 00000499: <Mov>: <Reg8: 91, Reg8: 13>
==> 0000049c: <CallBuiltin>: <Reg8: 13, UInt8: 44, UInt8: 3>  # Built-in function: [#44 copyDataProperties]
==> 000004a0: <Mov>: <Reg8: 91, Reg8: 9>
==> 000004a3: <Mov>: <Reg8: 92, Reg8: 18>
==> 000004a6: <CallBuiltin>: <Reg8: 9, UInt8: 44, UInt8: 3>  # Built-in function: [#44 copyDataProperties]
==> 000004aa: <LoadConstNull>: <Reg8: 9>
==> 000004ac: <Mov>: <Reg8: 32, Reg8: 15>
==> 000004af: <JNotEqual>: <Addr8: 9, Reg8: 32, Reg8: 9>  # Address: 000004b8
==> 000004b3: <GetByIdShort>: <Reg8: 32, Reg8: 0, UInt8: 91, string_id: 102>  # String: 'text' (Identifier)
==> 000004b8: <LoadConstNull>: <Reg8: 13>
==> 000004ba: <JmpFalse>: <Addr8: 112, Reg8: 2>  # Address: 0000052a
==> 000004bd: <NewObject>: <Reg8: 0>
==> 000004bf: <PutNewOwnByIdShort>: <Reg8: 0, Reg8: 32, string_id: 240>  # String: 'tintColor' (Identifier)
==> 000004c3: <PutNewOwnById>: <Reg8: 0, Reg8: 30, string_id: 17071>  # String: 'pressColor' (Identifier)
==> 000004c8: <PutNewOwnById>: <Reg8: 0, Reg8: 29, string_id: 18349>  # String: 'pressOpacity' (Identifier)
==> 000004cd: <PutNewOwnById>: <Reg8: 0, Reg8: 47, string_id: 10994>  # String: 'displayMode' (Identifier)
==> 000004d2: <PutNewOwnById>: <Reg8: 0, Reg8: 24, string_id: 10690>  # String: 'titleLayout' (Identifier)
==> 000004d7: <PutNewOwnById>: <Reg8: 0, Reg8: 40, string_id: 17462>  # String: 'screenLayout' (Identifier)
==> 000004dc: <TryGetById>: <Reg8: 24, Reg8: 43, UInt8: 92, string_id: 8>  # String: 'Boolean' (Identifier)
==> 000004e2: <Call2>: <Reg8: 24, Reg8: 24, Reg8: 3, Reg8: 5>
==> 000004e7: <PutNewOwnById>: <Reg8: 0, Reg8: 24, string_id: 8740>  # String: 'canGoBack' (Identifier)
==> 000004ec: <LoadConstUndefined>: <Reg8: 24>
==> 000004ee: <JmpFalse>: <Addr8: 9, Reg8: 5>  # Address: 000004f7
==> 000004f1: <GetById>: <Reg8: 24, Reg8: 25, UInt8: 93, string_id: 8460>  # String: 'goBack' (Identifier)
==> 000004f7: <PutNewOwnByIdShort>: <Reg8: 0, Reg8: 24, string_id: 129>  # String: 'onPress' (Identifier)
==> 000004fb: <Eq>: <Reg8: 25, Reg8: 5, Reg8: 9>
==> 000004ff: <LoadConstUndefined>: <Reg8: 24>
==> 00000501: <JmpTrue>: <Addr8: 8, Reg8: 25>  # Address: 00000509
==> 00000504: <GetByIdShort>: <Reg8: 24, Reg8: 5, UInt8: 13, string_id: 241>  # String: 'title' (Identifier)
==> 00000509: <PutNewOwnById>: <Reg8: 0, Reg8: 24, string_id: 7671>  # String: 'label' (Identifier)
==> 0000050e: <PutNewOwnById>: <Reg8: 0, Reg8: 23, string_id: 8770>  # String: 'labelStyle' (Identifier)
==> 00000513: <Eq>: <Reg8: 24, Reg8: 5, Reg8: 9>
==> 00000517: <LoadConstUndefined>: <Reg8: 23>
==> 00000519: <JmpTrue>: <Addr8: 8, Reg8: 24>  # Address: 00000521
==> 0000051c: <GetByIdShort>: <Reg8: 23, Reg8: 5, UInt8: 94, string_id: 157>  # String: 'href' (Identifier)
==> 00000521: <PutNewOwnByIdShort>: <Reg8: 0, Reg8: 23, string_id: 157>  # String: 'href' (Identifier)
==> 00000525: <Call2>: <Reg8: 13, Reg8: 2, Reg8: 3, Reg8: 0>
==> 0000052a: <LoadConstNull>: <Reg8: 25>
==> 0000052c: <JmpFalse>: <Addr8: 40, Reg8: 1>  # Address: 00000554
==> 0000052f: <NewObject>: <Reg8: 0>
==> 00000531: <PutNewOwnByIdShort>: <Reg8: 0, Reg8: 32, string_id: 240>  # String: 'tintColor' (Identifier)
==> 00000535: <PutNewOwnById>: <Reg8: 0, Reg8: 30, string_id: 17071>  # String: 'pressColor' (Identifier)
==> 0000053a: <PutNewOwnById>: <Reg8: 0, Reg8: 29, string_id: 18349>  # String: 'pressOpacity' (Identifier)
==> 0000053f: <TryGetById>: <Reg8: 2, Reg8: 43, UInt8: 92, string_id: 8>  # String: 'Boolean' (Identifier)
==> 00000545: <Call2>: <Reg8: 2, Reg8: 2, Reg8: 3, Reg8: 5>
==> 0000054a: <PutNewOwnById>: <Reg8: 0, Reg8: 2, string_id: 8740>  # String: 'canGoBack' (Identifier)
==> 0000054f: <Call2>: <Reg8: 25, Reg8: 1, Reg8: 3, Reg8: 0>
==> 00000554: <TypeOf>: <Reg8: 1, Reg8: 27>
==> 00000557: <LoadConstString>: <Reg8: 0, string_id: 8218>  # String: 'function' (Identifier)
==> 0000055b: <JStrictEqual>: <Addr8: 9, Reg8: 1, Reg8: 0>  # Address: 00000564
==> 0000055f: <CreateClosure>: <Reg8: 27, Reg8: 14, function_id: 13038>  # Function: [#13038  of 44 bytes]: 2 params @ offset 0x0023724d
==> 00000564: <LoadFromEnvironment>: <Reg8: 0, Reg8: 10, UInt8: 18>
==> 00000568: <GetByIdShort>: <Reg8: 2, Reg8: 0, UInt8: 95, string_id: 123>  # String: 'jsxs' (Identifier)
==> 0000056d: <LoadFromEnvironment>: <Reg8: 0, Reg8: 10, UInt8: 6>
==> 00000571: <GetByIdShort>: <Reg8: 0, Reg8: 0, UInt8: 96, string_id: 4>  # String: 'Animated' (Identifier)
==> 00000576: <GetByIdShort>: <Reg8: 1, Reg8: 0, UInt8: 97, string_id: 44>  # String: 'View' (Identifier)
==> 0000057b: <NewObject>: <Reg8: 0>
==> 0000057d: <LoadConstString>: <Reg8: 24, string_id: 4109>  # String: 'box-none' (String)
==> 00000581: <PutNewOwnById>: <Reg8: 0, Reg8: 24, string_id: 18322>  # String: 'pointerEvents' (Identifier)
==> 00000586: <NewObject>: <Reg8: 5>
==> 00000588: <PutNewOwnByIdShort>: <Reg8: 5, Reg8: 21, string_id: 17>  # String: 'height' (Identifier)
==> 0000058c: <PutNewOwnById>: <Reg8: 5, Reg8: 20, string_id: 11463>  # String: 'minHeight' (Identifier)
==> 00000591: <PutNewOwnById>: <Reg8: 5, Reg8: 7, string_id: 18154>  # String: 'maxHeight' (Identifier)
==> 00000596: <PutNewOwnByIdShort>: <Reg8: 5, Reg8: 6, string_id: 188>  # String: 'opacity' (Identifier)
==> 0000059a: <PutNewOwnByIdShort>: <Reg8: 5, Reg8: 4, string_id: 243>  # String: 'transform' (Identifier)
==> 0000059e: <NewArray>: <Reg8: 4, UInt16: 1>
==> 000005a2: <PutOwnByIndex>: <Reg8: 4, Reg8: 5, UInt8: 0>
==> 000005a6: <PutNewOwnByIdShort>: <Reg8: 0, Reg8: 4, string_id: 172>  # String: 'style' (Identifier)
==> 000005aa: <LoadFromEnvironment>: <Reg8: 4, Reg8: 10, UInt8: 18>
==> 000005ae: <GetByIdShort>: <Reg8: 6, Reg8: 4, UInt8: 98, string_id: 122>  # String: 'jsx' (Identifier)
==> 000005b3: <LoadFromEnvironment>: <Reg8: 4, Reg8: 10, UInt8: 6>
==> 000005b7: <GetByIdShort>: <Reg8: 4, Reg8: 4, UInt8: 96, string_id: 4>  # String: 'Animated' (Identifier)
==> 000005bc: <GetByIdShort>: <Reg8: 5, Reg8: 4, UInt8: 97, string_id: 44>  # String: 'View' (Identifier)
==> 000005c1: <NewObject>: <Reg8: 4>
==> 000005c3: <PutNewOwnById>: <Reg8: 4, Reg8: 24, string_id: 18322>  # String: 'pointerEvents' (Identifier)
==> 000005c8: <LoadFromEnvironment>: <Reg8: 7, Reg8: 10, UInt8: 6>
==> 000005cc: <GetByIdShort>: <Reg8: 7, Reg8: 7, UInt8: 37, string_id: 36>  # String: 'StyleSheet' (Identifier)
==> 000005d1: <GetById>: <Reg8: 20, Reg8: 7, UInt8: 99, string_id: 10605>  # String: 'absoluteFill' (Identifier)
==> 000005d7: <NewArray>: <Reg8: 7, UInt16: 2>
==> 000005db: <PutOwnByIndex>: <Reg8: 7, Reg8: 20, UInt8: 0>
==> 000005df: <PutOwnByIndex>: <Reg8: 7, Reg8: 8, UInt8: 1>
==> 000005e3: <PutNewOwnByIdShort>: <Reg8: 4, Reg8: 7, string_id: 172>  # String: 'style' (Identifier)
==> 000005e7: <JmpTrue>: <Addr8: 104, Reg8: 12>  # Address: 0000064f
==> 000005ea: <LoadFromEnvironment>: <Reg8: 7, Reg8: 10, UInt8: 18>
==> 000005ee: <GetByIdShort>: <Reg8: 20, Reg8: 7, UInt8: 98, string_id: 122>  # String: 'jsx' (Identifier)
==> 000005f3: <LoadFromEnvironment>: <Reg8: 7, Reg8: 10, UInt8: 12>
==> 000005f7: <GetById>: <Reg8: 8, Reg8: 7, UInt8: 100, string_id: 14920>  # String: 'HeaderBackground' (Identifier)
==> 000005fd: <NewObject>: <Reg8: 7>
==> 000005ff: <LoadConstString>: <Reg8: 23, string_id: 8147>  # String: 'auto' (Identifier)
==> 00000603: <Mov>: <Reg8: 21, Reg8: 23>
==> 00000606: <JmpFalse>: <Addr8: 56, Reg8: 22>  # Address: 0000063e
==> 00000609: <GetByIdShort>: <Reg8: 38, Reg8: 18, UInt8: 43, string_id: 67>  # String: 'backgroundColor' (Identifier)
==> 0000060e: <LoadConstString>: <Reg8: 22, string_id: 10354>  # String: 'transparent' (Identifier)
==> 00000612: <JStrictEqual>: <Addr8: 40, Reg8: 38, Reg8: 22>  # Address: 0000063a
==> 00000616: <LoadFromEnvironment>: <Reg8: 22, Reg8: 10, UInt8: 4>
==> 0000061a: <GetByIdShort>: <Reg8: 38, Reg8: 22, UInt8: 9, string_id: 107>  # String: 'default' (Identifier)
==> 0000061f: <GetByIdShort>: <Reg8: 22, Reg8: 18, UInt8: 43, string_id: 67>  # String: 'backgroundColor' (Identifier)
==> 00000624: <Call2>: <Reg8: 38, Reg8: 38, Reg8: 3, Reg8: 22>
==> 00000629: <GetById>: <Reg8: 22, Reg8: 38, UInt8: 101, string_id: 8720>  # String: 'alpha' (Identifier)
==> 0000062f: <Call1>: <Reg8: 22, Reg8: 22, Reg8: 38>
==> 00000633: <Mov>: <Reg8: 21, Reg8: 23>
==> 00000636: <JStrictNotEqual>: <Addr8: 8, Reg8: 22, Reg8: 44>  # Address: 0000063e
==> 0000063a: <LoadConstString>: <Reg8: 21, string_id: 7424>  # String: 'none' (Identifier)
==> 0000063e: <PutNewOwnById>: <Reg8: 7, Reg8: 21, string_id: 18322>  # String: 'pointerEvents' (Identifier)
==> 00000643: <PutNewOwnByIdShort>: <Reg8: 7, Reg8: 18, string_id: 172>  # String: 'style' (Identifier)
==> 00000647: <Call3>: <Reg8: 7, Reg8: 20, Reg8: 3, Reg8: 8, Reg8: 7>
==> 0000064d: <Jmp>: <Addr8: 13>  # Address: 0000065a
==> 0000064f: <NewObject>: <Reg8: 8>
==> 00000651: <PutNewOwnByIdShort>: <Reg8: 8, Reg8: 18, string_id: 172>  # String: 'style' (Identifier)
==> 00000655: <Call2>: <Reg8: 7, Reg8: 12, Reg8: 3, Reg8: 8>
==> 0000065a: <PutNewOwnByIdShort>: <Reg8: 4, Reg8: 7, string_id: 89>  # String: 'children' (Identifier)
==> 0000065e: <Call3>: <Reg8: 5, Reg8: 6, Reg8: 3, Reg8: 5, Reg8: 4>
==> 00000664: <NewArray>: <Reg8: 4, UInt16: 3>
==> 00000668: <PutOwnByIndex>: <Reg8: 4, Reg8: 5, UInt8: 0>
==> 0000066c: <LoadFromEnvironment>: <Reg8: 5, Reg8: 10, UInt8: 18>
==> 00000670: <GetByIdShort>: <Reg8: 7, Reg8: 5, UInt8: 98, string_id: 122>  # String: 'jsx' (Identifier)
==> 00000675: <LoadFromEnvironment>: <Reg8: 5, Reg8: 10, UInt8: 6>
==> 00000679: <GetByIdShort>: <Reg8: 6, Reg8: 5, UInt8: 97, string_id: 44>  # String: 'View' (Identifier)
==> 0000067e: <NewObject>: <Reg8: 5>
==> 00000680: <LoadConstString>: <Reg8: 8, string_id: 7424>  # String: 'none' (Identifier)
==> 00000684: <PutNewOwnById>: <Reg8: 5, Reg8: 8, string_id: 18322>  # String: 'pointerEvents' (Identifier)
==> 00000689: <NewObject>: <Reg8: 8>
==> 0000068b: <PutNewOwnByIdShort>: <Reg8: 8, Reg8: 11, string_id: 17>  # String: 'height' (Identifier)
==> 0000068f: <PutNewOwnByIdShort>: <Reg8: 5, Reg8: 8, string_id: 172>  # String: 'style' (Identifier)
==> 00000693: <Call3>: <Reg8: 5, Reg8: 7, Reg8: 3, Reg8: 6, Reg8: 5>
==> 00000699: <PutOwnByIndex>: <Reg8: 4, Reg8: 5, UInt8: 1>
==> 0000069d: <LoadFromEnvironment>: <Reg8: 5, Reg8: 10, UInt8: 18>
==> 000006a1: <GetByIdShort>: <Reg8: 7, Reg8: 5, UInt8: 95, string_id: 123>  # String: 'jsxs' (Identifier)
==> 000006a6: <LoadFromEnvironment>: <Reg8: 5, Reg8: 10, UInt8: 6>
==> 000006aa: <GetByIdShort>: <Reg8: 6, Reg8: 5, UInt8: 97, string_id: 44>  # String: 'View' (Identifier)
==> 000006af: <NewObject>: <Reg8: 5>
==> 000006b1: <PutNewOwnById>: <Reg8: 5, Reg8: 24, string_id: 18322>  # String: 'pointerEvents' (Identifier)
==> 000006b6: <LoadFromEnvironment>: <Reg8: 8, Reg8: 10, UInt8: 19>
==> 000006ba: <GetById>: <Reg8: 11, Reg8: 8, UInt8: 102, string_id: 7730>  # String: 'content' (Identifier)
==> 000006c0: <NewArray>: <Reg8: 8, UInt16: 2>
==> 000006c4: <PutOwnByIndex>: <Reg8: 8, Reg8: 11, UInt8: 0>
==> 000006c8: <PutOwnByIndex>: <Reg8: 8, Reg8: 9, UInt8: 1>
==> 000006cc: <PutNewOwnByIdShort>: <Reg8: 5, Reg8: 8, string_id: 172>  # String: 'style' (Identifier)
==> 000006d0: <LoadFromEnvironment>: <Reg8: 8, Reg8: 10, UInt8: 18>
==> 000006d4: <GetByIdShort>: <Reg8: 12, Reg8: 8, UInt8: 98, string_id: 122>  # String: 'jsx' (Identifier)
==> 000006d9: <LoadFromEnvironment>: <Reg8: 8, Reg8: 10, UInt8: 6>
==> 000006dd: <GetByIdShort>: <Reg8: 8, Reg8: 8, UInt8: 96, string_id: 4>  # String: 'Animated' (Identifier)
==> 000006e2: <GetByIdShort>: <Reg8: 11, Reg8: 8, UInt8: 97, string_id: 44>  # String: 'View' (Identifier)
==> 000006e7: <NewObject>: <Reg8: 8>
==> 000006e9: <PutNewOwnById>: <Reg8: 8, Reg8: 24, string_id: 18322>  # String: 'pointerEvents' (Identifier)
==> 000006ee: <LoadFromEnvironment>: <Reg8: 18, Reg8: 10, UInt8: 19>
==> 000006f2: <GetByIdShort>: <Reg8: 20, Reg8: 18, UInt8: 103, string_id: 231>  # String: 'start' (Identifier)
==> 000006f7: <NewArray>: <Reg8: 18, UInt16: 4>
==> 000006fb: <PutOwnByIndex>: <Reg8: 18, Reg8: 20, UInt8: 0>
==> 000006ff: <Not>: <Reg8: 20, Reg8: 17>
==> 00000702: <JmpFalse>: <Addr8: 11, Reg8: 20>  # Address: 0000070d
==> 00000705: <LoadConstString>: <Reg8: 21, string_id: 8612>  # String: 'center' (Identifier)
==> 00000709: <StrictEq>: <Reg8: 20, Reg8: 36, Reg8: 21>
==> 0000070d: <JmpFalse>: <Addr8: 13, Reg8: 20>  # Address: 0000071a
==> 00000710: <LoadFromEnvironment>: <Reg8: 21, Reg8: 10, UInt8: 19>
==> 00000714: <GetById>: <Reg8: 20, Reg8: 21, UInt8: 104, string_id: 16523>  # String: 'expand' (Identifier)
==> 0000071a: <PutOwnByIndex>: <Reg8: 18, Reg8: 20, UInt8: 1>
==> 0000071e: <NewObject>: <Reg8: 20>
==> 00000720: <GetByIdShort>: <Reg8: 21, Reg8: 28, UInt8: 105, string_id: 74>  # String: 'left' (Identifier)
==> 00000725: <PutNewOwnById>: <Reg8: 20, Reg8: 21, string_id: 18131>  # String: 'marginStart' (Identifier)
==> 0000072a: <PutOwnByIndex>: <Reg8: 18, Reg8: 20, UInt8: 2>
==> 0000072e: <PutOwnByIndex>: <Reg8: 18, Reg8: 19, UInt8: 3>
==> 00000732: <PutNewOwnByIdShort>: <Reg8: 8, Reg8: 18, string_id: 172>  # String: 'style' (Identifier)
==> 00000736: <PutNewOwnByIdShort>: <Reg8: 8, Reg8: 13, string_id: 89>  # String: 'children' (Identifier)
==> 0000073a: <Call3>: <Reg8: 11, Reg8: 12, Reg8: 3, Reg8: 11, Reg8: 8>
==> 00000740: <NewArray>: <Reg8: 8, UInt16: 3>
==> 00000744: <PutOwnByIndex>: <Reg8: 8, Reg8: 11, UInt8: 0>
==> 00000748: <LoadConstNull>: <Reg8: 11>
==> 0000074a: <JmpTrueLong>: <Addr32: 548, Reg8: 17>  # Address: 0000096e
==> 00000750: <LoadFromEnvironment>: <Reg8: 12, Reg8: 10, UInt8: 18>
==> 00000754: <GetByIdShort>: <Reg8: 19, Reg8: 12, UInt8: 95, string_id: 123>  # String: 'jsxs' (Identifier)
==> 00000759: <LoadFromEnvironment>: <Reg8: 12, Reg8: 10, UInt8: 18>
==> 0000075d: <GetById>: <Reg8: 18, Reg8: 12, UInt8: 106, string_id: 7676>  # String: 'Fragment' (Identifier)
==> 00000763: <NewObject>: <Reg8: 12>
==> 00000765: <LoadFromEnvironment>: <Reg8: 20, Reg8: 10, UInt8: 18>
==> 00000769: <GetByIdShort>: <Reg8: 22, Reg8: 20, UInt8: 98, string_id: 122>  # String: 'jsx' (Identifier)
==> 0000076e: <LoadFromEnvironment>: <Reg8: 20, Reg8: 10, UInt8: 6>
==> 00000772: <GetByIdShort>: <Reg8: 20, Reg8: 20, UInt8: 96, string_id: 4>  # String: 'Animated' (Identifier)
==> 00000777: <GetByIdShort>: <Reg8: 21, Reg8: 20, UInt8: 97, string_id: 44>  # String: 'View' (Identifier)
==> 0000077c: <NewObject>: <Reg8: 20>
==> 0000077e: <PutNewOwnById>: <Reg8: 20, Reg8: 24, string_id: 18322>  # String: 'pointerEvents' (Identifier)
==> 00000783: <LoadFromEnvironment>: <Reg8: 23, Reg8: 10, UInt8: 19>
==> 00000787: <GetByIdShort>: <Reg8: 38, Reg8: 23, UInt8: 13, string_id: 241>  # String: 'title' (Identifier)
==> 0000078c: <NewArray>: <Reg8: 23, UInt16: 4>
==> 00000790: <PutOwnByIndex>: <Reg8: 23, Reg8: 38, UInt8: 0>
==> 00000794: <NewObject>: <Reg8: 38>
==> 00000796: <LoadConstString>: <Reg8: 39, string_id: 8612>  # String: 'center' (Identifier)
==> 0000079a: <JStrictEqual>: <Addr8: 58, Reg8: 36, Reg8: 39>  # Address: 000007d4
==> 0000079e: <GetByIdShort>: <Reg8: 41, Reg8: 40, UInt8: 107, string_id: 16>  # String: 'width' (Identifier)
==> 000007a3: <LoadConstUInt8>: <Reg8: 46, UInt8: 16>
==> 000007a6: <Mov>: <Reg8: 39, Reg8: 46>
==> 000007a9: <JmpFalse>: <Addr8: 6, Reg8: 13>  # Address: 000007af
==> 000007ac: <LoadConstUInt8>: <Reg8: 39, UInt8: 52>
==> 000007af: <JmpTrue>: <Addr8: 6, Reg8: 25>  # Address: 000007b5
==> 000007b2: <JmpFalse>: <Addr8: 6, Reg8: 16>  # Address: 000007b8
==> 000007b5: <LoadConstUInt8>: <Reg8: 46, UInt8: 52>
==> 000007b8: <GetByIdShort>: <Reg8: 45, Reg8: 28, UInt8: 105, string_id: 74>  # String: 'left' (Identifier)
==> 000007bd: <AddN>: <Reg8: 39, Reg8: 39, Reg8: 46>
==> 000007c1: <Add>: <Reg8: 45, Reg8: 39, Reg8: 45>
==> 000007c5: <GetByIdShort>: <Reg8: 39, Reg8: 28, UInt8: 108, string_id: 75>  # String: 'right' (Identifier)
==> 000007ca: <Sub>: <Reg8: 39, Reg8: 45, Reg8: 39>
==> 000007ce: <Sub>: <Reg8: 39, Reg8: 41, Reg8: 39>
==> 000007d2: <Jmp>: <Addr8: 83>  # Address: 00000825
==> 000007d4: <GetByIdShort>: <Reg8: 41, Reg8: 40, UInt8: 107, string_id: 16>  # String: 'width' (Identifier)
==> 000007d9: <LoadConstUInt8>: <Reg8: 45, UInt8: 16>
==> 000007dc: <Mov>: <Reg8: 40, Reg8: 45>
==> 000007df: <JmpFalse>: <Addr8: 16, Reg8: 13>  # Address: 000007ef
==> 000007e2: <LoadConstUInt8>: <Reg8: 46, UInt8: 32>
==> 000007e5: <JStrictEqual>: <Addr8: 7, Reg8: 47, Reg8: 48>  # Address: 000007ec
==> 000007e9: <LoadConstUInt8>: <Reg8: 46, UInt8: 80>
==> 000007ec: <Mov>: <Reg8: 40, Reg8: 46>
==> 000007ef: <JmpTrue>: <Addr8: 8, Reg8: 25>  # Address: 000007f7
==> 000007f2: <LoadConstZero>: <Reg8: 44>
==> 000007f4: <JmpFalse>: <Addr8: 6, Reg8: 16>  # Address: 000007fa
==> 000007f7: <Mov>: <Reg8: 44, Reg8: 45>
==> 000007fa: <TryGetById>: <Reg8: 47, Reg8: 43, UInt8: 109, string_id: 21>  # String: 'Math' (Identifier)
==> 00000800: <GetByIdShort>: <Reg8: 46, Reg8: 47, UInt8: 110, string_id: 126>  # String: 'max' (Identifier)
==> 00000805: <GetByIdShort>: <Reg8: 45, Reg8: 28, UInt8: 105, string_id: 74>  # String: 'left' (Identifier)
==> 0000080a: <GetByIdShort>: <Reg8: 43, Reg8: 28, UInt8: 108, string_id: 75>  # String: 'right' (Identifier)
==> 0000080f: <Call3>: <Reg8: 43, Reg8: 46, Reg8: 47, Reg8: 45, Reg8: 43>
==> 00000815: <AddN>: <Reg8: 40, Reg8: 40, Reg8: 44>
==> 00000819: <Add>: <Reg8: 40, Reg8: 40, Reg8: 43>
==> 0000081d: <Mul>: <Reg8: 40, Reg8: 40, Reg8: 42>
==> 00000821: <Sub>: <Reg8: 39, Reg8: 41, Reg8: 40>
==> 00000825: <PutNewOwnById>: <Reg8: 38, Reg8: 39, string_id: 17744>  # String: 'maxWidth' (Identifier)
==> 0000082a: <PutOwnByIndex>: <Reg8: 23, Reg8: 38, UInt8: 1>
==> 0000082e: <JStrictNotEqual>: <Addr8: 7, Reg8: 36, Reg8: 37>  # Address: 00000835
==> 00000832: <JmpTrue>: <Addr8: 15, Reg8: 13>  # Address: 00000841
==> 00000835: <NewObject>: <Reg8: 36>
==> 00000837: <LoadConstUInt8>: <Reg8: 37, UInt8: 16>
==> 0000083a: <PutNewOwnById>: <Reg8: 36, Reg8: 37, string_id: 18087>  # String: 'marginHorizontal' (Identifier)
==> 0000083f: <Jmp>: <Addr8: 15>  # Address: 0000084e
==> 00000841: <NewObject>: <Reg8: 37>
==> 00000843: <LoadConstUInt8>: <Reg8: 38, UInt8: 4>
==> 00000846: <PutNewOwnById>: <Reg8: 37, Reg8: 38, string_id: 18131>  # String: 'marginStart' (Identifier)
==> 0000084b: <Mov>: <Reg8: 36, Reg8: 37>
==> 0000084e: <PutOwnByIndex>: <Reg8: 23, Reg8: 36, UInt8: 2>
==> 00000852: <PutOwnByIndex>: <Reg8: 23, Reg8: 35, UInt8: 3>
==> 00000856: <PutNewOwnByIdShort>: <Reg8: 20, Reg8: 23, string_id: 172>  # String: 'style' (Identifier)
==> 0000085a: <NewObject>: <Reg8: 23>
==> 0000085c: <PutNewOwnByIdShort>: <Reg8: 23, Reg8: 34, string_id: 89>  # String: 'children' (Identifier)
==> 00000860: <PutNewOwnById>: <Reg8: 23, Reg8: 33, string_id: 10872>  # String: 'allowFontScaling' (Identifier)
==> 00000865: <PutNewOwnByIdShort>: <Reg8: 23, Reg8: 15, string_id: 240>  # String: 'tintColor' (Identifier)
==> 00000869: <CreateClosure>: <Reg8: 33, Reg8: 14, function_id: 13035>  # Function: [#13035 onTitleLayout of 54 bytes]: 2 params @ offset 0x002371af
==> 0000086e: <PutNewOwnByIdShort>: <Reg8: 23, Reg8: 33, string_id: 186>  # String: 'onLayout' (Identifier)
==> 00000872: <PutNewOwnByIdShort>: <Reg8: 23, Reg8: 31, string_id: 172>  # String: 'style' (Identifier)
==> 00000876: <Call2>: <Reg8: 23, Reg8: 27, Reg8: 3, Reg8: 23>
==> 0000087b: <PutNewOwnByIdShort>: <Reg8: 20, Reg8: 23, string_id: 89>  # String: 'children' (Identifier)
==> 0000087f: <Call3>: <Reg8: 21, Reg8: 22, Reg8: 3, Reg8: 21, Reg8: 20>
==> 00000885: <NewArray>: <Reg8: 20, UInt16: 2>
==> 00000889: <PutOwnByIndex>: <Reg8: 20, Reg8: 21, UInt8: 0>
==> 0000088d: <LoadFromEnvironment>: <Reg8: 21, Reg8: 10, UInt8: 18>
==> 00000891: <GetByIdShort>: <Reg8: 23, Reg8: 21, UInt8: 95, string_id: 123>  # String: 'jsxs' (Identifier)
==> 00000896: <LoadFromEnvironment>: <Reg8: 21, Reg8: 10, UInt8: 6>
==> 0000089a: <GetByIdShort>: <Reg8: 21, Reg8: 21, UInt8: 96, string_id: 4>  # String: 'Animated' (Identifier)
==> 0000089f: <GetByIdShort>: <Reg8: 22, Reg8: 21, UInt8: 97, string_id: 44>  # String: 'View' (Identifier)
==> 000008a4: <NewObject>: <Reg8: 21>
==> 000008a6: <PutNewOwnById>: <Reg8: 21, Reg8: 24, string_id: 18322>  # String: 'pointerEvents' (Identifier)
==> 000008ab: <LoadFromEnvironment>: <Reg8: 24, Reg8: 10, UInt8: 19>
==> 000008af: <GetById>: <Reg8: 27, Reg8: 24, UInt8: 111, string_id: 7508>  # String: 'end' (Identifier)
==> 000008b5: <NewArray>: <Reg8: 24, UInt16: 4>
==> 000008b9: <PutOwnByIndex>: <Reg8: 24, Reg8: 27, UInt8: 0>
==> 000008bd: <LoadFromEnvironment>: <Reg8: 27, Reg8: 10, UInt8: 19>
==> 000008c1: <GetById>: <Reg8: 27, Reg8: 27, UInt8: 104, string_id: 16523>  # String: 'expand' (Identifier)
==> 000008c7: <PutOwnByIndex>: <Reg8: 24, Reg8: 27, UInt8: 1>
==> 000008cb: <NewObject>: <Reg8: 27>
==> 000008cd: <GetByIdShort>: <Reg8: 28, Reg8: 28, UInt8: 108, string_id: 75>  # String: 'right' (Identifier)
==> 000008d2: <PutNewOwnById>: <Reg8: 27, Reg8: 28, string_id: 18125>  # String: 'marginEnd' (Identifier)
==> 000008d7: <PutOwnByIndex>: <Reg8: 24, Reg8: 27, UInt8: 2>
==> 000008db: <PutOwnByIndex>: <Reg8: 24, Reg8: 26, UInt8: 3>
==> 000008df: <PutNewOwnByIdShort>: <Reg8: 21, Reg8: 24, string_id: 172>  # String: 'style' (Identifier)
==> 000008e3: <NewArray>: <Reg8: 24, UInt16: 2>
==> 000008e7: <PutOwnByIndex>: <Reg8: 24, Reg8: 25, UInt8: 0>
==> 000008eb: <LoadConstNull>: <Reg8: 25>
==> 000008ed: <JmpFalse>: <Addr8: 101, Reg8: 16>  # Address: 00000952
==> 000008f0: <LoadFromEnvironment>: <Reg8: 26, Reg8: 10, UInt8: 18>
==> 000008f4: <GetByIdShort>: <Reg8: 28, Reg8: 26, UInt8: 98, string_id: 122>  # String: 'jsx' (Identifier)
==> 000008f9: <LoadFromEnvironment>: <Reg8: 26, Reg8: 10, UInt8: 13>
==> 000008fd: <GetById>: <Reg8: 27, Reg8: 26, UInt8: 112, string_id: 8267>  # String: 'HeaderButton' (Identifier)
==> 00000903: <NewObject>: <Reg8: 26>
==> 00000905: <PutNewOwnByIdShort>: <Reg8: 26, Reg8: 32, string_id: 240>  # String: 'tintColor' (Identifier)
==> 00000909: <PutNewOwnById>: <Reg8: 26, Reg8: 30, string_id: 17071>  # String: 'pressColor' (Identifier)
==> 0000090e: <PutNewOwnById>: <Reg8: 26, Reg8: 29, string_id: 18349>  # String: 'pressOpacity' (Identifier)
==> 00000913: <CreateClosure>: <Reg8: 29, Reg8: 14, function_id: 13039>  # Function: [#13039 onPress of 42 bytes]: 1 params @ offset 0x00237279
==> 00000918: <PutNewOwnByIdShort>: <Reg8: 26, Reg8: 29, string_id: 129>  # String: 'onPress' (Identifier)
==> 0000091c: <LoadFromEnvironment>: <Reg8: 29, Reg8: 10, UInt8: 18>
==> 00000920: <GetByIdShort>: <Reg8: 31, Reg8: 29, UInt8: 98, string_id: 122>  # String: 'jsx' (Identifier)
==> 00000925: <LoadFromEnvironment>: <Reg8: 29, Reg8: 10, UInt8: 14>
==> 00000929: <GetById>: <Reg8: 30, Reg8: 29, UInt8: 113, string_id: 12213>  # String: 'HeaderIcon' (Identifier)
==> 0000092f: <NewObject>: <Reg8: 29>
==> 00000931: <LoadFromEnvironment>: <Reg8: 33, Reg8: 10, UInt8: 8>
==> 00000935: <GetByIdShort>: <Reg8: 33, Reg8: 33, UInt8: 9, string_id: 107>  # String: 'default' (Identifier)
==> 0000093a: <PutNewOwnByIdShort>: <Reg8: 29, Reg8: 33, string_id: 228>  # String: 'source' (Identifier)
==> 0000093e: <PutNewOwnByIdShort>: <Reg8: 29, Reg8: 32, string_id: 240>  # String: 'tintColor' (Identifier)
==> 00000942: <Call3>: <Reg8: 29, Reg8: 31, Reg8: 3, Reg8: 30, Reg8: 29>
==> 00000948: <PutNewOwnByIdShort>: <Reg8: 26, Reg8: 29, string_id: 89>  # String: 'children' (Identifier)
==> 0000094c: <Call3>: <Reg8: 25, Reg8: 28, Reg8: 3, Reg8: 27, Reg8: 26>
==> 00000952: <PutOwnByIndex>: <Reg8: 24, Reg8: 25, UInt8: 1>
==> 00000956: <PutNewOwnByIdShort>: <Reg8: 21, Reg8: 24, string_id: 89>  # String: 'children' (Identifier)
==> 0000095a: <Call3>: <Reg8: 21, Reg8: 23, Reg8: 3, Reg8: 22, Reg8: 21>
==> 00000960: <PutOwnByIndex>: <Reg8: 20, Reg8: 21, UInt8: 1>
==> 00000964: <PutNewOwnByIdShort>: <Reg8: 12, Reg8: 20, string_id: 89>  # String: 'children' (Identifier)
==> 00000968: <Call3>: <Reg8: 11, Reg8: 19, Reg8: 3, Reg8: 18, Reg8: 12>
==> 0000096e: <PutOwnByIndex>: <Reg8: 8, Reg8: 11, UInt8: 1>
==> 00000972: <LoadConstNull>: <Reg8: 9>
==> 00000974: <JmpFalse>: <Addr8: 108, Reg8: 17>  # Address: 000009e0
==> 00000977: <LoadFromEnvironment>: <Reg8: 11, Reg8: 10, UInt8: 18>
==> 0000097b: <GetByIdShort>: <Reg8: 12, Reg8: 11, UInt8: 98, string_id: 122>  # String: 'jsx' (Identifier)
==> 00000980: <LoadFromEnvironment>: <Reg8: 10, Reg8: 10, UInt8: 15>
==> 00000984: <GetById>: <Reg8: 11, Reg8: 10, UInt8: 114, string_id: 8755>  # String: 'HeaderSearchBar' (Identifier)
==> 0000098a: <NewObject>: <Reg8: 10>
==> 0000098c: <Mov>: <Reg8: 92, Reg8: 10>
==> 0000098f: <Mov>: <Reg8: 91, Reg8: 16>
==> 00000992: <CallBuiltin>: <Reg8: 16, UInt8: 44, UInt8: 3>  # Built-in function: [#44 copyDataProperties]
==> 00000996: <LoadConstString>: <Reg8: 16, string_id: 13618>  # String: 'visible' (Identifier)
==> 0000099a: <PutOwnByVal>: <Reg8: 10, Reg8: 17, Reg8: 16, UInt8: 1>
==> 0000099f: <CreateClosure>: <Reg8: 16, Reg8: 14, function_id: 13040>  # Function: [#13040 onClose of 42 bytes]: 1 params @ offset 0x002372a3
==> 000009a4: <LoadConstString>: <Reg8: 14, string_id: 12672>  # String: 'onClose' (Identifier)
==> 000009a8: <PutOwnByVal>: <Reg8: 10, Reg8: 16, Reg8: 14, UInt8: 1>
==> 000009ad: <LoadConstString>: <Reg8: 14, string_id: 240>  # String: 'tintColor' (Identifier)
==> 000009b1: <PutOwnByVal>: <Reg8: 10, Reg8: 15, Reg8: 14, UInt8: 1>
==> 000009b6: <Not>: <Reg8: 13, Reg8: 13>
==> 000009b9: <JmpFalse>: <Addr8: 16, Reg8: 13>  # Address: 000009c9
==> 000009bc: <NewObject>: <Reg8: 14>
==> 000009be: <LoadConstUInt8>: <Reg8: 15, UInt8: 8>
==> 000009c1: <PutNewOwnById>: <Reg8: 14, Reg8: 15, string_id: 18131>  # String: 'marginStart' (Identifier)
==> 000009c6: <Mov>: <Reg8: 13, Reg8: 14>
==> 000009c9: <NewArray>: <Reg8: 14, UInt16: 1>
==> 000009cd: <PutOwnByIndex>: <Reg8: 14, Reg8: 13, UInt8: 0>
==> 000009d1: <LoadConstString>: <Reg8: 13, string_id: 172>  # String: 'style' (Identifier)
==> 000009d5: <PutOwnByVal>: <Reg8: 10, Reg8: 14, Reg8: 13, UInt8: 1>
==> 000009da: <Call3>: <Reg8: 9, Reg8: 12, Reg8: 3, Reg8: 11, Reg8: 10>
==> 000009e0: <PutOwnByIndex>: <Reg8: 8, Reg8: 9, UInt8: 2>
==> 000009e4: <PutNewOwnByIdShort>: <Reg8: 5, Reg8: 8, string_id: 89>  # String: 'children' (Identifier)
==> 000009e8: <Call3>: <Reg8: 5, Reg8: 7, Reg8: 3, Reg8: 6, Reg8: 5>
==> 000009ee: <PutOwnByIndex>: <Reg8: 4, Reg8: 5, UInt8: 2>
==> 000009f2: <PutNewOwnByIdShort>: <Reg8: 0, Reg8: 4, string_id: 89>  # String: 'children' (Identifier)
==> 000009f6: <Call3>: <Reg8: 0, Reg8: 2, Reg8: 3, Reg8: 1, Reg8: 0>
==> 000009fc: <Ret>: <Reg8: 0>


"""


def test_chained_or_fold_does_not_drop_the_inner_call():
    out = render(HEADER, 13033)

    assert out.count("function_13037(param1)") == 3
