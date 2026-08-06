from hermes_decompiler.frontend.opcode import OpcodeResult
from hermes_decompiler.handlers import OpcodeHandler, OpcodeContext, sequence, REG
from hermes_decompiler.ir.expressions import Identifier


# Reg8 (total size 1)
# DEFINE_OPCODE_1(ReifyArguments, Reg8)
# Example: <ReifyArguments>: <Reg8: 0>
class ReifyArguments(OpcodeHandler):
    _PATTERN = sequence(REG)

    def handle(self, ctx: OpcodeContext) -> OpcodeResult:
        match = self._PATTERN.match(ctx.entry.args.strip())
        if not match:
            return self.build_invalid_args_result(ctx.analysis, ctx.entry, "Expected Reg8 argument")

        dest_reg = int(match.group(1))

        expression = Identifier(name="arguments")

        result = OpcodeResult(ctx.entry, value=expression, dest_reg=dest_reg)
        ctx.analysis.add_result(result)

        return result


# Reg8 (total size 1)
# DEFINE_OPCODE_1(ReifyArgumentsStrict, Reg8)
# Example: <ReifyArgumentsStrict>: <Reg8: 1>
class ReifyArgumentsStrict(ReifyArguments):
    pass


# Reg8 (total size 1)
# DEFINE_OPCODE_1(ReifyArgumentsLoose, Reg8)
# Example: <ReifyArgumentsLoose>: <Reg8: 4>
class ReifyArgumentsLoose(ReifyArguments):
    pass
