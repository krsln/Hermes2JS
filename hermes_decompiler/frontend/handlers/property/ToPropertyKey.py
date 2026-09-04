from hermes_decompiler.frontend.opcode import OpcodeResult
from frontend.handlers import OpcodeHandler, OpcodeContext, ArgsPattern, sequence, REG


# Reg8, Reg8 (total size 2)
# DEFINE_OPCODE_2(ToPropertyKey, Reg8, Reg8)
# Example: <ToPropertyKey>: <Reg8: 6, Reg8: 6>
class ToPropertyKey(OpcodeHandler):
    """Arg1 = ToPropertyKey(Arg2) -- coerce a value to a valid property key."""

    ARGUMENTS = ArgsPattern(sequence(REG, REG), "Reg8, Reg8 (total size 2)")

    def handle(self, ctx: OpcodeContext) -> OpcodeResult:
        match = self.match_arguments(ctx)
        if isinstance(match, OpcodeResult):
            return match

        dest_reg, value_reg = map(int, match.groups())

        # No-op passthrough at the JS-source level: `obj[key]` already
        # implies ToPropertyKey coercion, so there's nothing additional
        # to render -- just forward the source value to the destination.
        value = self.get_register_expression(ctx.analysis, value_reg)

        result = OpcodeResult(ctx.entry, value=value, dest_reg=dest_reg)
        ctx.analysis.add_result(result)

        return result
