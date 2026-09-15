from hermes_decompiler.frontend.handlers import OpcodeHandler, OpcodeContext, ArgsPattern, sequence, REG, UINT8
from hermes_decompiler.frontend.opcode import OpcodeResult
from hermes_decompiler.ir.expressions import Identifier


# Reg8, UInt8 (total size 2)
# DEFINE_OPCODE_2(GetBuiltinClosure, Reg8, UInt8)
# Example: <GetBuiltinClosure>: <Reg8: 9, UInt8: 1>  # Built-in function: [#1 Date.UTC]
class GetBuiltinClosure(OpcodeHandler):
    """Fetch a closure reference to one of Hermes's internal builtin functions."""

    ARGUMENTS = ArgsPattern(sequence(REG, UINT8), "Reg8, UInt8")

    def handle(self, ctx: OpcodeContext) -> OpcodeResult:
        match = self.match_arguments(ctx)
        if isinstance(match, OpcodeResult):
            return match

        dest_reg, builtin_number = map(int, match.groups())

        builtin_name = f"builtin_{builtin_number}"
        if ctx.entry.builtin_function is not None:
            builtin_name = ctx.entry.builtin_function.name

        expression = Identifier(name=builtin_name)

        result = OpcodeResult(ctx.entry, value=expression, dest_reg=dest_reg)
        ctx.analysis.add_result(result)

        return result
