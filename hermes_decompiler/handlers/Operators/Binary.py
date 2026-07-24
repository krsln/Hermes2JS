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
        BinaryOperator.LT,
        BinaryOperator.LTE,
        BinaryOperator.GT,
        BinaryOperator.GTE,
        BinaryOperator.EQ,
        BinaryOperator.STRICT_EQ,
        BinaryOperator.NOT_EQ,
        BinaryOperator.STRICT_NOT_EQ,
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
class Sub(BaseBinaryOperator): operator = BinaryOperator.SUB
class SubN(Sub): pass
class Mul(BaseBinaryOperator): operator = BinaryOperator.MUL
class MulN(Mul): pass
class Div(BaseBinaryOperator): operator = BinaryOperator.DIV
class DivN(Div): pass
class Mod(BaseBinaryOperator): operator = BinaryOperator.MOD
class ModN(Mod): pass

class BitAnd(BaseBinaryOperator): operator = BinaryOperator.BIT_AND
class BitNot(BaseBinaryOperator): operator = UnaryOperator.BIT_NOT
class BitOr(BaseBinaryOperator): operator = BinaryOperator.BIT_OR
class BitOrN(BitOr): pass
class BitXor(BaseBinaryOperator): operator = BinaryOperator.BIT_XOR
class BitXorN(BitXor): pass

class LShift(BaseBinaryOperator): operator = BinaryOperator.SHL
class RShift(BaseBinaryOperator): operator = BinaryOperator.SHR
class URshift(BaseBinaryOperator): operator = BinaryOperator.USHR

class Less(BaseBinaryOperator): operator = BinaryOperator.LT
class LessEq(BaseBinaryOperator): operator = BinaryOperator.LTE
class Greater(BaseBinaryOperator): operator = BinaryOperator.GT
class GreaterEq(BaseBinaryOperator): operator = BinaryOperator.GTE

class Eq(BaseBinaryOperator): operator = BinaryOperator.EQ
class Neq(BaseBinaryOperator): operator = BinaryOperator.NOT_EQ
class StrictEq(BaseBinaryOperator): operator = BinaryOperator.STRICT_EQ
class StrictNeq(BaseBinaryOperator): operator = BinaryOperator.STRICT_NOT_EQ
# @formatter:on

class InstanceOf(BaseBinaryOperator):
    """instanceof operator."""
    operator = BinaryOperator.INSTANCEOF


class IsIn(BaseBinaryOperator):
    """`in` operator: Arg1 = (Arg2 in Arg3)."""
    operator = BinaryOperator.IN
