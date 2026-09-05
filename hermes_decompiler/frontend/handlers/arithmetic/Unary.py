from hermes_decompiler.frontend.handlers import (
    OpcodeHandler, OpcodeContext, ArgsPattern, OperandMode, sequence, REG,
)
from hermes_decompiler.frontend.opcode import OpcodeResult
from hermes_decompiler.ir.Operators import UnaryOperator, BinaryOperator
from hermes_decompiler.ir.expressions import (
    Expression,
    UnaryExpression,
    BinaryExpression,
    NumericLiteral,
    StringLiteral,
)


class BaseUnaryOperator(OpcodeHandler):
    """Base class for unary register operations."""

    _abstract = True

    ARGUMENTS = ArgsPattern(sequence(REG, REG), "Reg8, Reg8")

    # Per-class override point: how the single source register operand
    # is resolved. EXPRESSION (default) substitutes/folds the register's
    # current value; REFERENCE keeps it as a bare `rN` identifier.
    # See `OperandMode` in OpcodeHandler.py for the full rationale.
    SOURCE_MODE: OperandMode = OperandMode.EXPRESSION

    def handle(self, ctx: OpcodeContext) -> OpcodeResult:
        match = self.match_arguments(ctx)
        if isinstance(match, OpcodeResult):
            return match

        dest_reg, src_reg = map(int, match.groups())

        src_val = self.get_source_value(ctx, src_reg)

        result = OpcodeResult(ctx.entry, value=self.expression(src_val), dest_reg=dest_reg)
        ctx.analysis.add_result(result)

        return result

    def get_source_value(self, ctx: OpcodeContext, src_reg: int) -> Expression:
        return self.resolve_operand(ctx.analysis, src_reg, self.SOURCE_MODE)

    def expression(self, value: Expression) -> Expression:
        """
        Return the JavaScript expression for the unary operation.
        Subclasses must override this method.
        """
        raise NotImplementedError


class Not(BaseUnaryOperator):
    def expression(self, value):
        return UnaryExpression(UnaryOperator.LOGICAL_NOT, value)


class TypeOf(BaseUnaryOperator):
    def expression(self, value):
        return UnaryExpression(UnaryOperator.TYPEOF, value)


class ToInt32(BaseUnaryOperator):
    def expression(self, value: Expression):
        return BinaryExpression(left=value, operator=BinaryOperator.BITWISE_OR, right=NumericLiteral(0))


class ToUint32(BaseUnaryOperator):
    def expression(self, value: Expression):
        return BinaryExpression(left=value, operator=BinaryOperator.UNSIGNED_RIGHT_SHIFT, right=NumericLiteral(0))


class ToNumeric(BaseUnaryOperator):
    def expression(self, value):
        return UnaryExpression(operator=UnaryOperator.PLUS, operand=value)


class ToNumber(BaseUnaryOperator):
    def expression(self, value):
        return UnaryExpression(UnaryOperator.PLUS, value)


class Inc(BaseUnaryOperator):
    """
    x + 1. The source register is typically the loop/accumulator
    variable itself, reassigned on the next iteration via a back-edge
    Mov, so it must stay symbolic (REFERENCE) rather than being
    substituted with a traced snapshot value.
    """

    SOURCE_MODE = OperandMode.REFERENCE

    def expression(self, value: Expression):
        return BinaryExpression(left=value, operator=BinaryOperator.ADD, right=NumericLiteral(1))  # x +1
        # return UpdateExpression(operator=UpdateOperator.INCREMENT, argument=value, prefix=False) # x++


class Dec(BaseUnaryOperator):
    """x - 1. See `Inc` docstring - same symbolic-operand requirement."""

    SOURCE_MODE = OperandMode.REFERENCE

    def expression(self, value: Expression):
        return BinaryExpression(left=value, operator=BinaryOperator.SUBTRACT, right=NumericLiteral(1))  # x -1
        # return UpdateExpression(operator=UpdateOperator.DECREMENT, argument=value, prefix=True) # x--


class Negate(BaseUnaryOperator):
    def expression(self, value):
        return UnaryExpression(UnaryOperator.MINUS, value)


class AddEmptyString(BaseUnaryOperator):
    def expression(self, value: Expression):
        return BinaryExpression(left=StringLiteral(""), operator=BinaryOperator.ADD, right=value)


class BitNot(BaseUnaryOperator):
    """
    Bitwise NOT (~x). Moved here from Binary.py, where it was previously
    misclassified as a BaseBinaryOperator with a UnaryOperator assigned
    to a BinaryOperator-typed field - `~` is unary and takes a single
    Reg8 operand, not two.
    """

    def expression(self, value):
        return UnaryExpression(UnaryOperator.BITWISE_NOT, value)
