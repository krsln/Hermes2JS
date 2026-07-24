from hermes_decompiler.ir.Expressions import ComparisonExpression, BinaryExpression
from hermes_decompiler.ir.Operators import BinaryOperator, UnaryOperator
from hermes_decompiler.models.HermesAnalysis import HermesAnalysis
from hermes_decompiler.models.OpcodeResult import OpcodeResult
from hermes_decompiler.models.JSVariable import JSVariable
from hermes_decompiler.models.OpcodeEntry import OpcodeEntry
from hermes_decompiler.models.OpcodeHandler import OpcodeHandler

from hermes_decompiler.handlers._shared_patterns import REG, sequence


class BaseBinaryOperator(OpcodeHandler):
    """Base class for binary register operations."""

    _PATTERN = sequence(REG, REG, REG)
    _COMPARISON_OPERATORS = {
        BinaryOperator.LESS_THAN,
        BinaryOperator.LESS_EQUAL,
        BinaryOperator.GREATER_THAN,
        BinaryOperator.GREATER_EQUAL,
        BinaryOperator.EQUAL,
        BinaryOperator.STRICT_EQUAL,
        BinaryOperator.NOT_EQUAL,
        BinaryOperator.STRICT_NOT_EQUAL,
        BinaryOperator.INSTANCEOF,
        BinaryOperator.IN,
    }

    operator = BinaryOperator.ADD

    def handle(self, analysis: HermesAnalysis, entry: OpcodeEntry) -> OpcodeResult:
        handler = self.__class__.__name__

        match = self._PATTERN.match(entry.args.strip())
        if not match:
            return self.build_invalid_args_result(analysis, entry, "Expected three Reg8 arguments")

        dest, lhs, rhs = map(int, match.groups())

        lhs_val = self.get_register_value_new(analysis, lhs)
        rhs_val = self.get_register_value_new(analysis, rhs)

        # value = f"{lhs_val} {self.operator} {rhs_val}"
        if self.operator in self._COMPARISON_OPERATORS:
            value = ComparisonExpression(left=lhs_val, operator=self.operator, right=rhs_val)
        else:
            value = BinaryExpression(left=lhs_val, operator=self.operator, right=rhs_val)

        variable = JSVariable(handler, entry.address, f"r{dest}", value)
        analysis.add_result(entry, variable)

        return OpcodeResult(entry, variable)


# @formatter:off
# @formatter:off
class Add(BaseBinaryOperator): operator = BinaryOperator.ADD
class AddN(Add): pass
class Sub(BaseBinaryOperator): operator = BinaryOperator.SUBTRACT
class SubN(Sub): pass
class Mul(BaseBinaryOperator): operator = BinaryOperator.MULTIPLY
class MulN(Mul): pass
class Div(BaseBinaryOperator): operator = BinaryOperator.DIVIDE
class DivN(Div): pass
class Mod(BaseBinaryOperator): operator = BinaryOperator.MODULO
class ModN(Mod): pass

class BitAnd(BaseBinaryOperator): operator = BinaryOperator.BITWISE_AND
class BitNot(BaseBinaryOperator): operator = UnaryOperator.BITWISE_NOT
class BitOr(BaseBinaryOperator): operator = BinaryOperator.BITWISE_OR
class BitOrN(BitOr): pass
class BitXor(BaseBinaryOperator): operator = BinaryOperator.BITWISE_XOR
class BitXorN(BitXor): pass

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

class InstanceOf(BaseBinaryOperator):
    """instanceof operator."""
    operator = BinaryOperator.INSTANCEOF


class IsIn(BaseBinaryOperator):
    """`in` operator: Arg1 = (Arg2 in Arg3)."""
    operator = BinaryOperator.IN
