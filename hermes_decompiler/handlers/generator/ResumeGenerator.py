from hermes_decompiler.frontend.opcode import OpcodeEntry, OpcodeResult
from hermes_decompiler.handlers import OpcodeHandler, sequence, REG
from hermes_decompiler.ir.expressions import AwaitExpression, YieldExpression
from hermes_decompiler.runtime import HermesAnalysis


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

    def handle(self, analysis: HermesAnalysis, entry: OpcodeEntry) -> OpcodeResult:
        match = self._PATTERN.match(entry.args.strip())
        if not match:
            return self.build_invalid_args_result(analysis, entry)

        dest_reg, _flag_reg = map(int, match.groups())

        # `await yield` is real, expressible JS - modeled directly
        # instead of the previous comment-annotated string.
        expression = AwaitExpression(argument=YieldExpression())

        result = OpcodeResult(entry, value=expression, dest_reg=dest_reg)
        analysis.add_result(result)

        return result
