from hermes_decompiler.frontend.handlers import OpcodeHandler, OpcodeContext, ArgsPattern, sequence, REG
from hermes_decompiler.frontend.opcode import OpcodeResult
from hermes_decompiler.ir.expressions import Identifier


# Reg8 (total size 1)
# DEFINE_OPCODE_1(LoadThisNS, Reg8)
# Example: <LoadThisNS>: <Reg8: 3>
class LoadThisNS(OpcodeHandler):
    """Load and coerce `this` value."""

    ARGUMENTS = ArgsPattern(sequence(REG), "Reg8 (total size 1)")

    def handle(self, ctx: OpcodeContext) -> OpcodeResult:
        match = self.match_arguments(ctx)
        if isinstance(match, OpcodeResult):
            return match

        dest_reg = int(match.group(1))

        expression = Identifier(name="this")

        result = OpcodeResult(ctx.entry, value=expression, dest_reg=dest_reg)
        ctx.analysis.add_result(result)

        return result
