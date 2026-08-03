from hermes_decompiler.frontend.opcode import OpcodeEntry, OpcodeResult
from hermes_decompiler.handlers import OpcodeHandler, REG, sequence
from hermes_decompiler.ir.Operators import BinaryOperator
from hermes_decompiler.ir.expressions import BinaryExpression
from hermes_decompiler.runtime import HermesAnalysis


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
    _PATTERN = sequence(REG, REG, REG)

    operator = BinaryOperator.ADD

    def handle(self, analysis: HermesAnalysis, entry: OpcodeEntry) -> OpcodeResult:
        match = self._PATTERN.match(entry.args.strip())
        if not match:
            return self.build_invalid_args_result(analysis, entry, "Expected three Reg8 arguments")

        dest_reg, lhs, rhs = map(int, match.groups())

        lhs_val = self.get_register_expression(analysis, lhs)
        rhs_val = self.get_register_expression(analysis, rhs)

        expression = BinaryExpression(left=lhs_val, operator=self.operator, right=rhs_val)

        result = OpcodeResult(entry, value=expression, dest_reg=dest_reg)
        analysis.add_result(result)

        return result


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
# class ModN(Mod): pass

class BitAnd(BaseBinaryOperator): operator = BinaryOperator.BITWISE_AND
class BitOr(BaseBinaryOperator): operator = BinaryOperator.BITWISE_OR
# class BitOrN(BitOr): pass
class BitXor(BaseBinaryOperator): operator = BinaryOperator.BITWISE_XOR
# class BitXorN(BitXor): pass

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

    _PATTERN = sequence(REG, REG, REG, REG)

    operator = BinaryOperator.IN

    def handle(self, analysis: HermesAnalysis, entry: OpcodeEntry) -> OpcodeResult:
        match = self._PATTERN.match(entry.args.strip())
        if not match:
            return self.build_invalid_args_result(
                analysis, entry, "Expected Reg8, Reg8, Reg8, Reg8 arguments"
            )

        dest_reg, private_name_reg, obj_reg, _cache = map(int, match.groups())

        private_name = self.get_register_expression(analysis, private_name_reg)
        obj = self.get_register_expression(analysis, obj_reg)

        expression = BinaryExpression(left=private_name, operator=self.operator, right=obj)

        result = OpcodeResult(entry, value=expression, dest_reg=dest_reg)
        analysis.add_result(result)

        return result
