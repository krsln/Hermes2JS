from hermes_decompiler.frontend.opcode import OpcodeResult
from hermes_decompiler.handlers import OpcodeHandler, OpcodeContext, sequence, REG, UINT8
from hermes_decompiler.ir.expressions import Identifier


# Reg8, UInt8 (total size 2)
# DEFINE_OPCODE_2(GetBuiltinClosure, Reg8, UInt8)
# Example: <GetBuiltinClosure>: <Reg8: 9, UInt8: 1>  # Built-in function: [#1 Date.UTC]
class GetBuiltinClosure(OpcodeHandler):
    """Fetch a closure reference to one of Hermes's internal builtin functions."""

    _PATTERN = sequence(REG, UINT8)

    def handle(self, ctx: OpcodeContext) -> OpcodeResult:
        match = self._PATTERN.match(ctx.entry.args.strip())
        if not match:
            return self.build_invalid_args_result(ctx.analysis, ctx.entry, "Expected Reg8, UInt8 arguments")

        dest_reg, builtin_number = map(int, match.groups())

        builtin_name = getattr(ctx.entry, "builtin_name", None) or f"builtin_{builtin_number}"

        expression = Identifier(name=builtin_name)

        result = OpcodeResult(ctx.entry, value=expression, dest_reg=dest_reg)
        ctx.analysis.add_result(result)

        return result
