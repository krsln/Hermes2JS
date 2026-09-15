from hermes_decompiler.frontend.handlers import OpcodeHandler, OpcodeContext, ArgsPattern, sequence, REG, UINT8, UINT32
from hermes_decompiler.frontend.opcode import OpcodeResult
from hermes_decompiler.ir.expressions import Identifier


# Reg8, UInt8 (total size 2)
# DEFINE_OPCODE_2(LoadParam, Reg8, UInt8)
# Example: <LoadParam>: <Reg8: 6, UInt8: 2>
class LoadParam(OpcodeHandler):
    """Load function parameter (including this at index 0)."""

    ARGUMENTS = ArgsPattern(sequence(REG, UINT8), "Reg8, UInt8 (total size 2)")

    def handle(self, ctx: OpcodeContext) -> OpcodeResult:
        match = self.match_arguments(ctx)
        if isinstance(match, OpcodeResult):
            return match

        dest_reg, param_index = map(int, match.groups())

        # Load a function parameter by index. Starts at 0 with 'this'.
        name = "this" if param_index == 0 else f"param{param_index}"
        expression = Identifier(name=name)

        result = OpcodeResult(ctx.entry, value=expression, dest_reg=dest_reg)
        ctx.analysis.add_result(result)

        return result


# Reg8, UInt32 (total size 5)
# DEFINE_OPCODE_2(LoadParamLong, Reg8, UInt32)
# Example:
class LoadParamLong(LoadParam):
    """Like LoadParam, but allows accessing arguments >= 255."""

    ARGUMENTS = ArgsPattern(sequence(REG, UINT32), "Reg8, UInt32 (total size 5)")
