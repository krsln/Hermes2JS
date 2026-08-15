from hermes_decompiler.frontend.opcode import OpcodeResult
from hermes_decompiler.handlers import (
    OpcodeHandler, OpcodeContext, ArgsPattern, OperandMode, sequence, REG,
)
from hermes_decompiler.ir.Operators import BinaryOperator
from hermes_decompiler.ir.expressions import BinaryExpression


class BaseBinaryOperator(OpcodeHandler):
    """
    Base class for binary register operations.

    Comparison operators (<, ===, instanceof, ...) render through the
    same BinaryExpression node as arithmetic/bitwise ones - the old
    separate ComparisonExpression node added no information that
    `operator` doesn't already carry, and `Operators.precedence()`
    already handles comparison operators correctly.
    """
    _abstract = True

    operator = BinaryOperator.ADD

    ARGUMENTS = ArgsPattern(sequence(REG, REG, REG), "Reg8, Reg8, Reg8")

    # Per-operand override points, mirroring BaseUnaryOperator.SOURCE_MODE.
    # Default is EXPRESSION for both sides (constant folding / inlining),
    # matching prior behavior for every opcode that doesn't need special
    # treatment. Subclasses whose lhs is a loop/accumulator register that
    # gets redefined on a back-edge (AddN/SubN desugared from i++/i--)
    # should flip the relevant side to REFERENCE - see AddN/SubN below.
    LHS_MODE: OperandMode = OperandMode.EXPRESSION
    RHS_MODE: OperandMode = OperandMode.EXPRESSION

    def handle(self, ctx: OpcodeContext) -> OpcodeResult:
        match = self.match_arguments(ctx)
        if isinstance(match, OpcodeResult):
            return match

        dest_reg, lhs, rhs = map(int, match.groups())

        lhs_val = self.resolve_operand(ctx.analysis, lhs, self.LHS_MODE)
        rhs_val = self.resolve_operand(ctx.analysis, rhs, self.RHS_MODE)

        expression = BinaryExpression(left=lhs_val, operator=self.operator, right=rhs_val)

        result = OpcodeResult(ctx.entry, value=expression, dest_reg=dest_reg)
        ctx.analysis.add_result(result)

        return result


# @formatter:off
# /// Arg1 = Arg2 + Arg3 (JS addition/concatenation)
# DEFINE_OPCODE_3(Add, Reg8, Reg8, Reg8)
class Add(BaseBinaryOperator): operator = BinaryOperator.ADD

# /// Arg1 = Arg2 + Arg3 (Numeric addition, skips number check)
# DEFINE_OPCODE_3(AddN, Reg8, Reg8, Reg8)
class AddN(Add):
    """
    Numeric-only fast-path Add. Hermes emits this for `i++` / `i += 1`
    style loop increments as `AddN i_next, i, 1`. The lhs operand (`i`)
    must stay symbolic: it's the loop counter and gets reassigned every
    iteration via a back-edge Mov, so substituting its traced value here
    would bake a single iteration's snapshot into the expression (e.g.
    `r0 = 0 + 1` instead of `r0 = r1 + 1`), producing a non-advancing
    counter and a potential infinite loop in the decompiled output.
    """
    LHS_MODE = OperandMode.REFERENCE


class Sub(BaseBinaryOperator): operator = BinaryOperator.SUBTRACT


class SubN(Sub):
    """Numeric-only fast-path Sub. Same accumulator concern as AddN."""
    LHS_MODE = OperandMode.REFERENCE


class Mul(BaseBinaryOperator): operator = BinaryOperator.MULTIPLY
class MulN(Mul): pass
class Div(BaseBinaryOperator): operator = BinaryOperator.DIVIDE
class DivN(Div): pass
class Mod(BaseBinaryOperator): operator = BinaryOperator.MODULO

class BitAnd(BaseBinaryOperator): operator = BinaryOperator.BITWISE_AND
class BitOr(BaseBinaryOperator): operator = BinaryOperator.BITWISE_OR
class BitXor(BaseBinaryOperator): operator = BinaryOperator.BITWISE_XOR

class LShift(BaseBinaryOperator): operator = BinaryOperator.LEFT_SHIFT
class RShift(BaseBinaryOperator): operator = BinaryOperator.RIGHT_SHIFT
class URshift(BaseBinaryOperator): operator = BinaryOperator.UNSIGNED_RIGHT_SHIFT

class Less(BaseBinaryOperator): operator = BinaryOperator.LESS_THAN
class LessEq(BaseBinaryOperator): operator = BinaryOperator.LESS_EQUAL
class Greater(BaseBinaryOperator): operator = BinaryOperator.GREATER_THAN
class GreaterEq(BaseBinaryOperator): operator = BinaryOperator.GREATER_EQUAL

class Eq(BaseBinaryOperator): operator = BinaryOperator.EQUAL
class Neq(BaseBinaryOperator): operator = BinaryOperator.NOT_EQUAL
class StrictEq(BaseBinaryOperator): operator = BinaryOperator.STRICT_EQUAL
class StrictNeq(BaseBinaryOperator): operator = BinaryOperator.STRICT_NOT_EQUAL
# @formatter:on


# Reg8, Reg8, Reg8 (total size 3)
# DEFINE_OPCODE_3(AddS, Reg8, Reg8, Reg8)
# Example: <AddS>: <Reg8: 9, Reg8: 6, Reg8: 1>
class AddS(BaseBinaryOperator):
    """String-concatenation-proven variant of Add."""

    operator = BinaryOperator.ADD


# Reg8, Reg8, Reg8 (total size 3)
# DEFINE_OPCODE_3(InstanceOf, Reg8, Reg8, Reg8)
# Example: <InstanceOf>: <Reg8: 8, Reg8: 11, Reg8: 18>
class InstanceOf(BaseBinaryOperator):
    """instanceof operator."""

    operator = BinaryOperator.INSTANCEOF


# Reg8, Reg8, Reg8 (total size 3)
# DEFINE_OPCODE_3(IsIn, Reg8, Reg8, Reg8)
# Example: <IsIn>: <Reg8: 0, Reg8: 4, Reg8: 5>
class IsIn(BaseBinaryOperator):
    """`in` operator: Arg1 = (Arg2 in Arg3)."""

    operator = BinaryOperator.IN


# Reg8, Reg8, Reg8, Reg8 (total size 4)
# DEFINE_OPCODE_4(PrivateIsIn, Reg8, Reg8, Reg8, Reg8)
# Example: <PrivateIsIn>: <Reg8: 0, Reg8: 5, Reg8: 4, Reg8: 0>
class PrivateIsIn(OpcodeHandler):
    """`#x in obj` brand-check operator: Arg1 = (Arg2 in Arg3), own-properties only, symbol-keyed."""

    operator = BinaryOperator.IN
    ARGUMENTS = ArgsPattern(sequence(REG, REG, REG, REG), "Reg8, Reg8, Reg8, Reg8")

    def handle(self, ctx: OpcodeContext) -> OpcodeResult:
        match = self.match_arguments(ctx)
        if isinstance(match, OpcodeResult):
            return match

        dest_reg, private_name_reg, obj_reg, _cache = map(int, match.groups())

        private_name = self.get_register_expression(ctx.analysis, private_name_reg)
        obj = self.get_register_expression(ctx.analysis, obj_reg)

        expression = BinaryExpression(left=private_name, operator=self.operator, right=obj)

        result = OpcodeResult(ctx.entry, value=expression, dest_reg=dest_reg)
        ctx.analysis.add_result(result)

        return result
