from hermes_decompiler.frontend.opcode import OpcodeResult
from hermes_decompiler.handlers import OpcodeHandler, OpcodeContext, sequence, REG, UINT32
from hermes_decompiler.ir.expressions import Identifier


# Reg8, UInt32 (total size 5)
# DEFINE_OPCODE_2(CreateTopLevelEnvironment, Reg8, UInt32)
# Example: <CreateTopLevelEnvironment>: <Reg8: 2, UInt32: 3>
class CreateTopLevelEnvironment(OpcodeHandler):
    """Allocate the parentless module/global-level environment record."""

    _PATTERN = sequence(REG, UINT32)

    def handle(self, ctx: OpcodeContext) -> OpcodeResult:
        match = self._PATTERN.match(ctx.entry.args.strip())
        if not match:
            return self.build_invalid_args_result(ctx.analysis, ctx.entry, "Expected Reg8, UInt32 arguments")

        dest_reg, _size = map(int, match.groups())

        expression = Identifier(name="__environment__")

        result = OpcodeResult(ctx.entry, value=expression, dest_reg=dest_reg)
        ctx.analysis.add_result(result)

        return result
