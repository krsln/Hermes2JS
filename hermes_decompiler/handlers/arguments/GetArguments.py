from hermes_decompiler.handlers import OpcodeHandler, REG, sequence
from hermes_decompiler.ir.expressions import Identifier, MemberExpression
from hermes_decompiler.frontend.opcode import OpcodeEntry, OpcodeResult
from hermes_decompiler.runtime import HermesAnalysis


# Reg8, Reg8 (total size 2)
# DEFINE_OPCODE_2(GetArgumentsLength, Reg8, Reg8)
# Example: <GetArgumentsLength>: <Reg8: 1, Reg8: 0>
class GetArgumentsLength(OpcodeHandler):
    """Get the length of the 'arguments' array."""

    _PATTERN = sequence(REG, REG)

    def handle(self, analysis: HermesAnalysis, entry: OpcodeEntry) -> OpcodeResult:
        match = self._PATTERN.match(entry.args.strip())
        if not match:
            return self.build_invalid_args_result(analysis, entry, "Expected two Reg8 arguments")

        dest_reg, _lazy_reg = map(int, match.groups())

        expression = MemberExpression(receiver=Identifier(name="arguments"), member=Identifier(name="length"))

        result = OpcodeResult(entry, value=expression, dest_reg=dest_reg)
        analysis.add_result(result)

        return result


# Reg8, Reg8, Reg8 (total size 3)
# DEFINE_OPCODE_3(GetArgumentsPropByVal, Reg8, Reg8, Reg8)
# Example: <GetArgumentsPropByVal>: <Reg8: 2, Reg8: 1, Reg8: 0>
class GetArgumentsPropByVal(OpcodeHandler):
    """Get a property of the 'arguments' array by value."""

    _PATTERN = sequence(REG, REG, REG)

    def handle(self, analysis: HermesAnalysis, entry: OpcodeEntry) -> OpcodeResult:
        match = self._PATTERN.match(entry.args.strip())
        if not match:
            return self.build_invalid_args_result(analysis, entry, "Expected three Reg8 arguments")

        dest_reg, index_reg, _lazy_reg = map(int, match.groups())
        index_value = self.get_register_expression(analysis, index_reg)

        # `ComputedMemberExpression` was a separate legacy class for
        # `obj[x]`; the new IR unifies dot/bracket access into one
        # `MemberExpression` via `computed=`.
        expression = MemberExpression(receiver=Identifier(name="arguments"), member=index_value, computed=True)

        result = OpcodeResult(entry, value=expression, dest_reg=dest_reg)
        analysis.add_result(result)

        return result


# Reg8, Reg8, Reg8 (total size 3)
# DEFINE_OPCODE_3(GetArgumentsPropByValLoose, Reg8, Reg8, Reg8)
# Example: <GetArgumentsPropByValLoose>: <Reg8: 3, Reg8: 0, Reg8: 4>
class GetArgumentsPropByValLoose(GetArgumentsPropByVal):
    pass


# Reg8, Reg8, Reg8 (total size 3)
# DEFINE_OPCODE_3(GetArgumentsPropByValStrict, Reg8, Reg8, Reg8)
# Example: <GetArgumentsPropByValStrict>: <Reg8: 12, Reg8: 1, Reg8: 10>
class GetArgumentsPropByValStrict(GetArgumentsPropByVal):
    pass
