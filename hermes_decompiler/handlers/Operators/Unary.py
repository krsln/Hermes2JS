from typing import ClassVar

from hermes_decompiler.handlers import OpcodeHandler, REG, sequence
from hermes_decompiler.ir.Operators import UnaryOperator, BinaryOperator
from hermes_decompiler.ir.expressions import (
    Expression,
    UnaryExpression,
    BinaryExpression,
    NumericLiteral,
    StringLiteral,
)
from hermes_decompiler.opcode import OpcodeEntry, OpcodeResult
from hermes_decompiler.runtime import HermesAnalysis


class BaseUnaryOperator(OpcodeHandler):
    """Base class for unary register operations."""

    _PATTERN: ClassVar = sequence(REG, REG)

    def expression(self, value: Expression) -> Expression:
        """
        Return the JavaScript expression for the unary operation.
        Subclasses must override this method.
        """
        raise NotImplementedError

    def handle(self, analysis: HermesAnalysis, entry: OpcodeEntry) -> OpcodeResult:
        match = self._PATTERN.match(entry.args.strip())
        if not match:
            return self.build_invalid_args_result(analysis, entry, "Expected two Reg8 arguments")

        dest_reg, src_reg = map(int, match.groups())

        src_val = self.get_register_value(analysis, src_reg)

        result = OpcodeResult(entry, value=self.expression(src_val), dest_reg=dest_reg)
        analysis.add_result(result)

        return result


class Not(BaseUnaryOperator):
    def expression(self, value):
        return UnaryExpression(UnaryOperator.LOGICAL_NOT, value)


class TypeOf(BaseUnaryOperator):
    def expression(self, value):
        return UnaryExpression(UnaryOperator.TYPEOF, value)


class ToInt32(BaseUnaryOperator):
    def expression(self, value: Expression):
        return BinaryExpression(left=value, operator=BinaryOperator.BITWISE_OR, right=NumericLiteral(0))


class ToNumeric(BaseUnaryOperator):
    def expression(self, value):
        return UnaryExpression(operator=UnaryOperator.PLUS, operand=value)


class ToNumber(BaseUnaryOperator):
    def expression(self, value):
        return UnaryExpression(UnaryOperator.PLUS, value)


class Inc(BaseUnaryOperator):
    def expression(self, value: Expression):
        return BinaryExpression(left=value, operator=BinaryOperator.ADD, right=NumericLiteral(1))


class Dec(BaseUnaryOperator):
    def expression(self, value: Expression):
        return BinaryExpression(left=value, operator=BinaryOperator.SUBTRACT, right=NumericLiteral(1))


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
