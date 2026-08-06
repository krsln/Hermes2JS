from hermes_decompiler.frontend.opcode import OpcodeResult
from hermes_decompiler.handlers import OpcodeHandler, OpcodeContext, sequence, REG, UINT8, UINT32
from hermes_decompiler.ir.expressions import Identifier


# Reg8, UInt8 (total size 2)
# DEFINE_OPCODE_2(LoadParam, Reg8, UInt8)
# Example: <LoadParam>: <Reg8: 6, UInt8: 2>
class LoadParam(OpcodeHandler):
    """Load function parameter (including this at index 0)."""

    _PATTERN = sequence(REG, UINT8)

    def handle(self, ctx: OpcodeContext) -> OpcodeResult:
        match = self._PATTERN.match(ctx.entry.args.strip())
        if not match:
            return self.build_invalid_args_result(ctx.analysis, ctx.entry)

        dest_reg, param_index = map(int, match.groups())

        # param0 = this, others = paramN
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

    _PATTERN = sequence(REG, UINT32)
