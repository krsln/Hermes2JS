from hermes_decompiler.handlers import OpcodeHandler, REG, UINT8, sequence
from hermes_decompiler.ir.Operators import AssignmentOperator
from hermes_decompiler.ir.expressions import AssignmentExpression, MemberExpression
from hermes_decompiler.frontend.opcode import OpcodeEntry, OpcodeResult
from hermes_decompiler.runtime import HermesAnalysis


# Reg8, Reg8, Reg8 (total size 3)
# DEFINE_OPCODE_3(PutByVal, Reg8, Reg8, Reg8)
# Example: <PutByVal>: <Reg8: 98, Reg8: 2, Reg8: 0>
class PutByVal(OpcodeHandler):
    """Set an existing own property identified at a slot index."""

    _PATTERN = sequence(REG, REG, REG)

    def handle(self, analysis: HermesAnalysis, entry: OpcodeEntry) -> OpcodeResult:
        match = self._PATTERN.match(entry.args.strip())
        if not match:
            return self.build_invalid_args_result(analysis, entry, "Expected three Reg8 arguments")

        obj_reg, key_reg, value_reg = map(int, match.groups())

        left = MemberExpression(
            receiver=self.get_register_expression(analysis, obj_reg),
            member=self.get_register_expression(analysis, key_reg),
            computed=True,
        )
        right = self.get_register_expression(analysis, value_reg)

        expression = AssignmentExpression(left=left, operator=AssignmentOperator.ASSIGN, right=right)

        result = OpcodeResult(entry, value=expression, dest_reg=None)
        analysis.add_result(result)

        return result


# Reg8, Reg8, Reg8 (total size 3)
# DEFINE_OPCODE_3(PutByValLoose, Reg8, Reg8, Reg8)
# Example: <PutByValLoose>: <Reg8: 3, Reg8: 2, Reg8: 4>
class PutByValLoose(PutByVal):
    """
    Set a property by value. Constant string values should instead use GetById
    (unless they are array indices according to ES5.1 section 15.4, in which
    case this is still the right opcode)
    """
    pass


# Reg8, Reg8, Reg8 (total size 3)
# DEFINE_OPCODE_3(PutByValStrict, Reg8, Reg8, Reg8)
# Example: <PutByValStrict>: <Reg8: 2, Reg8: 3, Reg8: 1>
class PutByValStrict(PutByVal):
    pass


# Reg8, Reg8, Reg8, Reg8, UInt8 (total size 5)
# DEFINE_OPCODE_5(PutByValWithReceiver, Reg8, Reg8, Reg8, Reg8, UInt8)
class PutByValWithReceiver(OpcodeHandler):
    """
    Property store with an explicit receiver (used by super/proxy semantics).

    Current IR does not distinguish receiver-based stores, therefore the
    receiver register and cache index are parsed but ignored.
    """

    _PATTERN = sequence(REG, REG, REG, REG, UINT8)

    def handle(self, analysis: HermesAnalysis, entry: OpcodeEntry) -> OpcodeResult:
        match = self._PATTERN.match(entry.args.strip())
        if not match:
            return self.build_invalid_args_result(
                analysis,
                entry,
                "Expected Reg8, Reg8, Reg8, Reg8, UInt8",
            )

        obj_reg, key_reg, value_reg, _receiver_reg, _cache_index = map(
            int, match.groups()
        )

        left = MemberExpression(
            receiver=self.get_register_expression(analysis, obj_reg),
            member=self.get_register_expression(analysis, key_reg),
            computed=True,
        )

        right = self.get_register_expression(analysis, value_reg)

        expression = AssignmentExpression(
            left=left,
            operator=AssignmentOperator.ASSIGN,
            right=right,
        )

        result = OpcodeResult(entry, value=expression, dest_reg=None)
        analysis.add_result(result)
        return result


# Reg8, Reg8, Reg8, UInt8 (total size 4)
# DEFINE_OPCODE_4(PutOwnByVal, Reg8, Reg8, Reg8, UInt8)
# Example: <PutOwnByVal>: <Reg8: 4, Reg8: 11, Reg8: 3, UInt8: 1>
class PutOwnByVal(OpcodeHandler):
    """
    Define or update an own property using a computed key.

    NOTE: unlike PutByVal (Arg1[Arg2] = Arg3), PutOwnByVal's operand order
    is Arg1[Arg3] = Arg2 - the *second* register is the value, the *third*
    is the property key. Naming both handlers' parameters the same way
    (obj_reg, key_reg, value_reg) silently swapped key and value here.

    The trailing UInt8 contains Hermes-specific flags (enumerable) and is
    currently ignored.
    """

    _PATTERN = sequence(REG, REG, REG, UINT8)

    def handle(self, analysis: HermesAnalysis, entry: OpcodeEntry) -> OpcodeResult:
        match = self._PATTERN.match(entry.args.strip())
        if not match:
            return self.build_invalid_args_result(
                analysis,
                entry,
                "Expected Reg8, Reg8, Reg8, UInt8",
            )

        obj_reg, value_reg, key_reg, _flags = map(int, match.groups())

        left = MemberExpression(
            receiver=self.get_register_reference(analysis, obj_reg),
            member=self.get_register_expression(analysis, key_reg),
            computed=True,
        )

        right = self.get_register_expression(analysis, value_reg)

        expression = AssignmentExpression(left=left, operator=AssignmentOperator.ASSIGN, right=right)

        result = OpcodeResult(entry, value=expression, dest_reg=None)
        analysis.add_result(result)
        return result
