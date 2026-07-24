from typing import ClassVar

from hermes_decompiler.ir.Expressions import UnaryExpression, BinaryExpression, Expression
from hermes_decompiler.ir.Operators import UnaryOperator, BinaryOperator
from hermes_decompiler.ir.Values import Value, ConstantValue
from hermes_decompiler.models.HermesAnalysis import HermesAnalysis
from hermes_decompiler.models.OpcodeResult import OpcodeResult
from hermes_decompiler.models.JSVariable import JSVariable
from hermes_decompiler.models.OpcodeEntry import OpcodeEntry
from hermes_decompiler.models.OpcodeHandler import OpcodeHandler

from hermes_decompiler.handlers._shared_patterns import REG, sequence


class BaseUnaryOperator(OpcodeHandler):
    """Base class for unary register operations."""

    _PATTERN: ClassVar = sequence(REG, REG)

    def expression(self, value: Value) -> Expression:
        """
        Return the JavaScript expression for the unary operation.
        Subclasses should override this method.
        """
        pass

    def handle(
            self,
            analysis: HermesAnalysis,
            entry: OpcodeEntry,
    ) -> OpcodeResult:
        handler = self.__class__.__name__

        match = self._PATTERN.match(entry.args.strip())
        if not match:
            return self.build_invalid_args_result(analysis, entry, "Expected two Reg8 arguments")

        dest_reg, src_reg = map(int, match.groups())

        src_val = self.get_register_value_new(analysis, src_reg)

        variable = JSVariable(handler, entry.address, f"r{dest_reg}", self.expression(src_val))
        analysis.add_result(entry, variable)

        return OpcodeResult(entry, variable)


class Not(BaseUnaryOperator):
    def expression(self, value):
        return UnaryExpression(UnaryOperator.NOT, value)


class TypeOf(BaseUnaryOperator):
    def expression(self, value):
        return UnaryExpression(UnaryOperator.TYPEOF, value)


class ToInt32(BaseUnaryOperator):
    def expression(self, value: Value):
        return BinaryExpression(left=value, operator=BinaryOperator.BIT_OR, right=ConstantValue(0))


class ToNumeric(BaseUnaryOperator):
    def expression(self, value):
        return UnaryExpression(operator=UnaryOperator.PLUS, operand=value)


class ToNumber(BaseUnaryOperator):
    def expression(self, value):
        return UnaryExpression(UnaryOperator.PLUS, value)


class Inc(BaseUnaryOperator):
    def expression(self, value: Value):
        return BinaryExpression(left=value, operator=BinaryOperator.ADD, right=ConstantValue(1))


class Dec(BaseUnaryOperator):
    def expression(self, value: Value):
        return BinaryExpression(left=value, operator=BinaryOperator.SUB, right=ConstantValue(1))


class Negate(BaseUnaryOperator):
    def expression(self, value):
        return UnaryExpression(UnaryOperator.NEGATE, value)


class AddEmptyString(BaseUnaryOperator):
    def expression(self, value: Value):
        return BinaryExpression(left=ConstantValue(""), operator=BinaryOperator.ADD, right=value)
