from hermes_decompiler.frontend.handlers import OpcodeHandler, OpcodeContext, ArgsPattern, sequence, REG, UINT32
from hermes_decompiler.frontend.opcode import OpcodeResult
from hermes_decompiler.ir.expressions import CallExpression, Identifier


# Reg8, Reg8, UInt32 (total size 6)
# DEFINE_OPCODE_3(CreateEnvironment, Reg8, Reg8, UInt32)
# DEFINE_OPCODE_1(CreateEnvironment, Reg8)
# Example: <CreateEnvironment>: <Reg8: 3, Reg8: 2, UInt32: 1>
class CreateEnvironment(OpcodeHandler):
    """
    Allocate a new lexical environment.

    Hermes uses environment objects to store variables
    captured by nested closures.
    """

    ARGUMENTS = (
        ArgsPattern(sequence(REG, REG, UINT32), "Reg8, Reg8, UInt32"),
        ArgsPattern(sequence(REG), "Reg8"),  # DEFINE_OPCODE_1
    )

    def handle(self, ctx: OpcodeContext) -> OpcodeResult:
        match = self.match_arguments(ctx)
        if isinstance(match, OpcodeResult):
            return match

        dest_reg = int(match.group(1))

        expression = CallExpression(callee=Identifier(name="createEnvironment"), arguments=())

        result = OpcodeResult(ctx.entry, value=expression, dest_reg=dest_reg)
        ctx.analysis.add_result(result)

        return result
