from hermes_decompiler.frontend.opcode import OpcodeResult
from hermes_decompiler.handlers import OpcodeHandler, OpcodeContext, sequence, REG, UINT8
from hermes_decompiler.ir.expressions import Identifier


# Reg8, UInt8 (total size 2)
# DEFINE_OPCODE_2(CreateFunctionEnvironment, Reg8, UInt8)
# Example: <CreateFunctionEnvironment>: <Reg8: 7, UInt8: 1>
class CreateFunctionEnvironment(OpcodeHandler):
    """Allocate a new function-local environment/scope record."""

    _PATTERN = sequence(REG, UINT8)

    def handle(self, ctx: OpcodeContext) -> OpcodeResult:
        match = self._PATTERN.match(ctx.entry.args.strip())
        if not match:
            return self.build_invalid_args_result(ctx.analysis, ctx.entry, "Expected Reg8, UInt8 arguments")

        dest_reg, _size = map(int, match.groups())

        expression = Identifier(name="__environment__")

        result = OpcodeResult(ctx.entry, value=expression, dest_reg=dest_reg)
        ctx.analysis.add_result(result)

        return result
