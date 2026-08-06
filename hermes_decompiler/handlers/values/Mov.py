from hermes_decompiler.frontend.opcode import OpcodeResult
from hermes_decompiler.handlers import OpcodeHandler, OpcodeContext, sequence, REG


# Reg8, Reg8 (total size 2)
# DEFINE_OPCODE_2(Mov, Reg8, Reg8)
# Example: <Mov>: <Reg8: 1, Reg8: 6>
class Mov(OpcodeHandler):
    """Move value between registers: rX = rY"""

    _PATTERN = sequence(REG, REG)

    def handle(self, ctx: OpcodeContext) -> OpcodeResult:
        match = self._PATTERN.match(ctx.entry.args.strip())
        if not match:
            return self.build_invalid_args_result(ctx.analysis, ctx.entry)

        dest_reg, src_reg = map(int, match.groups())

        expression = self.get_register_expression(ctx.analysis, src_reg)

        result = OpcodeResult(ctx.entry, value=expression, dest_reg=dest_reg)
        ctx.analysis.add_result(result)

        return result


# Reg32, Reg32 (total size 8)
# DEFINE_OPCODE_2(MovLong, Reg32, Reg32)
# Example:
class MovLong(Mov):
    pass
