from typing import ClassVar

from hermes_decompiler.ir.Expressions import UnaryExpression, BinaryExpression, Expression, PrefixUnaryExpression
from hermes_decompiler.ir.Values import Value, ConstantValue
from hermes_decompiler.models.HermesAnalysis import HermesAnalysis
from hermes_decompiler.models.OpcodeResult import OpcodeResult
from hermes_decompiler.models.JSVariable import JSVariable
from hermes_decompiler.models.OpcodeEntry import OpcodeEntry
from hermes_decompiler.models.OpcodeHandler import OpcodeHandler

from hermes_decompiler.handlers._shared_patterns import REG, sequence


class UnaryOperator(OpcodeHandler):
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


class Not(UnaryOperator):
    def expression(self, value):
        return PrefixUnaryExpression("!", value)


class TypeOf(UnaryOperator):
    def expression(self, value):
        return PrefixUnaryExpression("typeof", value)


class ToInt32(UnaryOperator):
    def expression(self, value: Value):
        return BinaryExpression(left=value, operator="|", right=ConstantValue(0))


class ToNumeric(UnaryOperator):
    def expression(self, value):
        return UnaryExpression(operator="+", operand=value)


class ToNumber(UnaryOperator):
    def expression(self, value):
        return PrefixUnaryExpression("+", value)


class Inc(UnaryOperator):
    def expression(self, value: Value):
        return BinaryExpression(left=value, operator="+", right=ConstantValue(1))


class Dec(UnaryOperator):
    def expression(self, value: Value):
        return BinaryExpression(left=value, operator="-", right=ConstantValue(1))


class Negate(UnaryOperator):
    def expression(self, value):
        return PrefixUnaryExpression("-", value)


class AddEmptyString(UnaryOperator):
    def expression(self, value: Value):
        return BinaryExpression(left=ConstantValue(""), operator="+", right=value)
