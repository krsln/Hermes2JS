from hermes_decompiler.frontend.handlers import OpcodeHandler, OpcodeContext, ArgsPattern, sequence, REG
from hermes_decompiler.frontend.opcode import OpcodeResult
from hermes_decompiler.ir.expressions import Identifier, MemberExpression


# Reg8, Reg8 (total size 2)
# DEFINE_OPCODE_2(GetArgumentsLength, Reg8, Reg8)
# Example: <GetArgumentsLength>: <Reg8: 1, Reg8: 0>
class GetArgumentsLength(OpcodeHandler):
    """Get the length of the 'arguments' array."""

    ARGUMENTS = ArgsPattern(sequence(REG, REG), "Reg8, Reg8")

    def handle(self, ctx: OpcodeContext) -> OpcodeResult:
        match = self.match_arguments(ctx)
        if isinstance(match, OpcodeResult):
            return match

        dest_reg, _lazy_reg = map(int, match.groups())

        expression = MemberExpression(obj=Identifier(name="arguments"), prop=Identifier(name="length"))

        result = OpcodeResult(ctx.entry, value=expression, dest_reg=dest_reg)
        ctx.analysis.add_result(result)

        return result


# Reg8, Reg8, Reg8 (total size 3)
# DEFINE_OPCODE_3(GetArgumentsPropByVal, Reg8, Reg8, Reg8)
# Example: <GetArgumentsPropByVal>: <Reg8: 2, Reg8: 1, Reg8: 0>
class GetArgumentsPropByVal(OpcodeHandler):
    """Get a property of the 'arguments' array by value."""

    ARGUMENTS = ArgsPattern(sequence(REG, REG, REG), "Reg8, Reg8, Reg8")

    def handle(self, ctx: OpcodeContext) -> OpcodeResult:
        match = self.match_arguments(ctx)
        if isinstance(match, OpcodeResult):
            return match

        dest_reg, index_reg, _lazy_reg = map(int, match.groups())
        index_value = self.get_register_expression(ctx.analysis, index_reg)

        # `ComputedMemberExpression` was a separate legacy class for
        # `obj[x]`; the new IR unifies dot/bracket access into one
        # `MemberExpression` via `computed=`.
        expression = MemberExpression(obj=Identifier(name="arguments"), prop=index_value, computed=True)

        result = OpcodeResult(ctx.entry, value=expression, dest_reg=dest_reg)
        ctx.analysis.add_result(result)

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
