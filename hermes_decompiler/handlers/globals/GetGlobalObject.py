from hermes_decompiler.frontend.opcode import OpcodeResult
from hermes_decompiler.handlers import OpcodeHandler, OpcodeContext, ArgsPattern, sequence, REG
from hermes_decompiler.ir.expressions import Identifier


# Reg8 (total size 1)
# DEFINE_OPCODE_1(GetGlobalObject, Reg8)
# Example: <GetGlobalObject>: <Reg8: 2>
class GetGlobalObject(OpcodeHandler):
    """Get the global object (global scope)."""

    ARGUMENTS = ArgsPattern(sequence(REG), "Reg8 (total size 1)")

    def handle(self, ctx: OpcodeContext) -> OpcodeResult:
        match = self.match_arguments(ctx)
        if isinstance(match, OpcodeResult):
            return match

        dest_reg = int(match.group(1))

        # Track global object register in analysis
        ctx.analysis.globalObjects = dest_reg

        expression = Identifier(name="globalThis")

        result = OpcodeResult(ctx.entry, value=expression, dest_reg=dest_reg)
        ctx.analysis.add_result(result)

        return result
