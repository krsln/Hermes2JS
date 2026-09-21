"""
`has_side_effects` decides whether a fold may drop, move or make conditional
an expression. It is deep, and it knows a few calls that are not effects.
"""

from __future__ import annotations

import re

from hermes_decompiler.backend.transforms.shared import has_side_effects
from hermes_decompiler.Decompiler import Decompiler
from hermes_decompiler.ir.Operators import LogicalOperator
from hermes_decompiler.ir.expressions import (
    BinaryExpression,
    CallExpression,
    FunctionExpression,
    Identifier,
    MemberExpression,
    NumericLiteral,
)


def call(name: str, *arguments) -> CallExpression:
    return CallExpression(callee=Identifier(name=name), arguments=tuple(arguments))


def user_call(name: str, *arguments) -> CallExpression:
    # A user function is called as `f.call(this, ...)`: a member callee.
    return CallExpression(
        callee=MemberExpression(obj=Identifier(name=name), prop=Identifier(name="call")),
        arguments=tuple(arguments),
    )


def test_reads_and_literals_have_no_side_effects():
    assert not has_side_effects(Identifier(name="r1"))
    assert not has_side_effects(NumericLiteral(value=3))


def test_a_user_call_has_side_effects():
    assert has_side_effects(user_call("f", Identifier(name="r1")))


def test_environment_plumbing_and_exponentiation_are_not_effects():
    assert not has_side_effects(call("getEnvironment", NumericLiteral(value=0)))
    assert not has_side_effects(call("getParentEnvironment", NumericLiteral(value=1)))
    assert not has_side_effects(call("createEnvironment"))
    assert not has_side_effects(call("exponentiationOperator", Identifier(name="r9"), Identifier(name="r8")))


def test_a_pure_callee_is_still_an_effect_if_an_argument_is():
    assert has_side_effects(call("exponentiationOperator", user_call("f"), NumericLiteral(value=3)))


def test_other_builtins_are_effects():
    # They mutate their arguments or run user code.
    for name in ("copyDataProperties", "arraySpread", "apply", "iteratorNext"):
        assert has_side_effects(call(name, Identifier(name="r1"))), name


def test_the_check_is_deep():
    nested = BinaryExpression(
        left=Identifier(name="r1"), operator=LogicalOperator.OR, right=user_call("f")
    )

    assert has_side_effects(nested)


def test_a_function_expression_only_creates_a_value():
    fn = FunctionExpression(name="g", parameters=(), body=user_call("f"))

    assert not has_side_effects(fn)


# hbc96 function #12962 of apps/testy/96 (color-convert's Lab -> XYZ). Hermes
# computes the three `x ** 3` calls BEFORE the conditionals that use them:
#
#   r2 = exponentiationOperator(...)                 // unconditional
#   if (!(r2 > 0.008856)) r2 = (r7 - 0.138) / 7.787
#
# which is the source's `x > 0.008856 ? x ** 3 : (x - 16/116) / 7.787`. The
# call has no effect, so ConditionalExpressionRegionPass may fold it back.
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


def test_hoisted_exponentiation_is_folded_back_into_the_source_ternary():
    out = Decompiler.render(Decompiler.build_context(LAB_TO_XYZ, 12962), verbose=False)

    # The three assignments, one per Lab channel. (The `return` line repeats
    # the same expressions, which is why this matches assignments only.)
    assignments = [
        line
        for line in out.split("\n")
        if re.match(r"\s*r\d+ = \(r\d+ > 0\.008856\) \? exponentiationOperator\(", line)
    ]

    assert len(assignments) == 3, out
