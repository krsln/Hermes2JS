from hermes_decompiler.handlers import OpcodeHandler, REG, sequence
from hermes_decompiler.ir.Operators import BinaryOperator
from hermes_decompiler.ir.expressions import BinaryExpression
from hermes_decompiler.opcode import OpcodeEntry, OpcodeResult
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

    _PATTERN = sequence(REG, REG, REG)

    operator = BinaryOperator.ADD

    def handle(self, analysis: HermesAnalysis, entry: OpcodeEntry) -> OpcodeResult:
        match = self._PATTERN.match(entry.args.strip())
        if not match:
            return self.build_invalid_args_result(analysis, entry, "Expected three Reg8 arguments")

        dest_reg, lhs, rhs = map(int, match.groups())

        lhs_val = self.get_register_value(analysis, lhs)
        rhs_val = self.get_register_value(analysis, rhs)

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
class ModN(Mod): pass

class BitAnd(BaseBinaryOperator): operator = BinaryOperator.BITWISE_AND
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


# DEFINE_OPCODE_4(PrivateIsIn, Reg8, Reg8, Reg8, Reg8)
#   [confirmed, facebook/hermes BytecodeList.def, tag hermes-v260318099.0.1]
#
#   "Arg1 = Arg2 in Arg3 (JS relational 'in' for private names.)
#    Arg2 must be a symbol.
#    Arg4 is a private name cache index used to speed up the above
#    operation.
#    Note that this performs different logic than a normal `in` check.
#    This instruction does not consult the prototype chain or trigger
#    any proxy traps. It is a direct check on the own properties of
#    the input object."
#
# Backs the ergonomic private-field brand check `#x in obj` (used to
# test class membership without triggering getters/Proxy traps).
# Rendered as the same `in` BinaryExpression as plain IsIn -- the
# distinction (own-property-only, no prototype/proxy involvement) is a
# semantic guarantee `#x in obj` already has in real JS syntax by
# virtue of `#x` being a private name, so no separate rendering is
# needed. Arg2 (the private-name symbol register) takes the LHS slot
# exactly like a regular IsIn's property-key operand.
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

        private_name = self.get_register_value(analysis, private_name_reg)
        obj = self.get_register_value(analysis, obj_reg)

        expression = BinaryExpression(left=private_name, operator=self.operator, right=obj)

        result = OpcodeResult(entry, value=expression, dest_reg=dest_reg)
        analysis.add_result(result)

        return result


# DEFINE_OPCODE_3(AddS, Reg8, Reg8, Reg8)   [confirmed, hermes-dec table]
#
#   "This is a variant of Add which is used when the compiler can prove
#    that at least one of the operands is a string, so the result must
#    be a string concatenation (as opposed to Add's more general
#    numeric-or-string behavior). Arg1 = Arg2 + Arg3, guaranteed
#    string-concat semantics."
#
# Rendered identically to Add (`+`) -- the distinction is a compiler-
# side proof/optimization about *which* runtime path Add would take,
# not a different JS operator; `"a" + "b"` and the proven-string fast
# path both surface as the same `+` in source.
class AddS(BaseBinaryOperator):
    """String-concatenation-proven variant of Add."""

    operator = BinaryOperator.ADD
