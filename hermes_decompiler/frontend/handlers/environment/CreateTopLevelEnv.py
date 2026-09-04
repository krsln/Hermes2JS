from hermes_decompiler.frontend.opcode import OpcodeResult
from frontend.handlers import OpcodeHandler, OpcodeContext, ArgsPattern, sequence, REG, UINT32
from hermes_decompiler.ir.expressions import Identifier


# Reg8, UInt32 (total size 5)
# DEFINE_OPCODE_2(CreateTopLevelEnvironment, Reg8, UInt32)
# Example: <CreateTopLevelEnvironment>: <Reg8: 2, UInt32: 3>
class CreateTopLevelEnvironment(OpcodeHandler):
    """Allocate the parentless module/global-level environment record."""

    ARGUMENTS = ArgsPattern(sequence(REG, UINT32), "Reg8, UInt32")

    def handle(self, ctx: OpcodeContext) -> OpcodeResult:
        match = self.match_arguments(ctx)
        if isinstance(match, OpcodeResult):
            return match

        dest_reg, _size = map(int, match.groups())

        expression = Identifier(name="__environment__")

        result = OpcodeResult(ctx.entry, value=expression, dest_reg=dest_reg)
        ctx.analysis.add_result(result)

        return result
