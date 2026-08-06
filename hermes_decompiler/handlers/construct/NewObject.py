from hermes_decompiler.frontend.opcode import OpcodeResult
from hermes_decompiler.handlers import OpcodeHandler, OpcodeContext, sequence, REG
from hermes_decompiler.ir.expressions import ObjectExpression


# Reg8 (total size 1)
# DEFINE_OPCODE_1(NewObject, Reg8)
# Example: <NewObject>: <Reg8: 7>
class NewObject(OpcodeHandler):
    """Create a new empty object: {}"""

    _PATTERN = sequence(REG)

    def handle(self, ctx: OpcodeContext) -> OpcodeResult:
        match = self._PATTERN.match(ctx.entry.args.strip())
        if not match:
            return self.build_invalid_args_result(ctx.analysis, ctx.entry)

        dest_reg = int(match.group(1))

        expression = ObjectExpression(properties=())

        result = OpcodeResult(ctx.entry, value=expression, dest_reg=dest_reg)
        ctx.analysis.add_result(result)

        return result
