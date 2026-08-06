from hermes_decompiler.frontend.opcode import OpcodeResult
from hermes_decompiler.handlers import OpcodeHandler, OpcodeContext, sequence, REG
from hermes_decompiler.ir.expressions import AwaitExpression, YieldExpression, Identifier


# /// Resume generator by performing one of the following user-requested actions:
# /// - next(val): Set Arg1 to val, Arg2 to false, run next instruction
# /// - return(val): Set Arg1 to val, Arg2 to true, run next instruction
# /// - throw(val): Throw val as an error
# /// Arg1 is the result provided by the user.
# /// Arg2 is a boolean which is true if the user requested a return().
# DEFINE_OPCODE_2(ResumeGenerator, Reg8, Reg8)

# Reg8, Reg8 (total size 2)
# DEFINE_OPCODE_2(ResumeGenerator, Reg8, Reg8)
# Example: <ResumeGenerator>: <Reg8: 0, Reg8: 2>
class ResumeGenerator(OpcodeHandler):
    """Resume a suspended generator."""

    _PATTERN = sequence(REG, REG)

    def handle(self, ctx: OpcodeContext) -> OpcodeResult:
        match = self._PATTERN.match(ctx.entry.args.strip())
        if not match:
            return self.build_invalid_args_result(ctx.analysis, ctx.entry)

        dest_reg, flag_reg = map(int, match.groups())

        # value = await yield;   (normal next / return value)
        expression = AwaitExpression(argument=YieldExpression())

        result = OpcodeResult(ctx.entry, value=expression, dest_reg=dest_reg)
        ctx.analysis.add_result(result)

        # Track the generator return flag for subsequent conditional jumps.
        flag_result = OpcodeResult(ctx.entry, value=Identifier(name=f"__resumeIsReturn"), dest_reg=flag_reg)
        ctx.analysis.add_result(flag_result)

        return result
