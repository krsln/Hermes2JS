from hermes_decompiler.frontend.handlers import OpcodeHandler, OpcodeContext, ArgsPattern, sequence, REG
from hermes_decompiler.frontend.opcode import OpcodeResult
from hermes_decompiler.ir.expressions import MemberExpression


# Reg8, Reg8, Reg8 (total size 3)
# DEFINE_OPCODE_3(GetByVal, Reg8, Reg8, Reg8)
# Example: <GetByVal>: <Reg8: 3, Reg8: 7, Reg8: 0>
class GetByVal(OpcodeHandler):
    """Get property by dynamic value: obj[key]"""

    ARGUMENTS = ArgsPattern(sequence(REG, REG, REG), "Reg8, Reg8, Reg8")

    def handle(self, ctx: OpcodeContext) -> OpcodeResult:
        match = self.match_arguments(ctx)
        if isinstance(match, OpcodeResult):
            return match

        dest_reg, base_reg, prop_reg = map(int, match.groups())

        obj = self.get_register_expression(ctx.analysis, base_reg)
        index = self.get_register_reference(ctx.analysis, prop_reg)

        expression = MemberExpression(obj=obj, prop=index, computed=True)

        result = OpcodeResult(ctx.entry, value=expression, dest_reg=dest_reg)
        ctx.analysis.add_result(result)

        return result


# /// Get a property by value with a specified receiver.
# /// Arg1 = Arg2[Arg3]
# /// Arg1 is the destination register.
# /// Arg2 is the object to begin the property look up. It must be an object.
# /// Arg3 is the property key.
# /// Arg4 is the receiver.
# DEFINE_OPCODE_4(GetByValWithReceiver, Reg8, Reg8, Reg8, Reg8)


# Reg8, Reg8, Reg8, Reg8 (total size 4)
# DEFINE_OPCODE_4(GetByValWithReceiver, Reg8, Reg8, Reg8, Reg8)

class GetByValWithReceiver(OpcodeHandler):
    """Get property by dynamic value with an explicit receiver."""

    ARGUMENTS = ArgsPattern(sequence(REG, REG, REG, REG), "Reg8, Reg8, Reg8, Reg8")

    def handle(self, ctx: OpcodeContext) -> OpcodeResult:
        match = self.match_arguments(ctx)
        if isinstance(match, OpcodeResult):
            return match

        dest_reg, base_reg, prop_reg, receiver_reg = map(int, match.groups())

        obj = self.get_register_expression(ctx.analysis, base_reg)
        index = self.get_register_reference(ctx.analysis, prop_reg)
        receiver = self.get_register_expression(ctx.analysis, receiver_reg)

        expression = MemberExpression(obj=obj, prop=index, receiver=receiver, computed=True)

        result = OpcodeResult(ctx.entry, value=expression, dest_reg=dest_reg)
        ctx.analysis.add_result(result)

        return result
