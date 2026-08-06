from hermes_decompiler.frontend.opcode import OpcodeResult
from hermes_decompiler.handlers import OpcodeHandler, OpcodeContext, sequence, REG, UINT32
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

    _PATTERN = sequence(REG, REG, UINT32)
    _PATTERN_OLD = sequence(REG)  # DEFINE_OPCODE_1

    def handle(self, ctx: OpcodeContext) -> OpcodeResult:
        match = (
                self._PATTERN.match(ctx.entry.args.strip())
                or self._PATTERN_OLD.match(ctx.entry.args.strip())
        )
        if not match:
            return self.build_invalid_args_result(ctx.analysis, ctx.entry)

        dest_reg = int(match.group(1))

        expression = CallExpression(callee=Identifier(name="createEnvironment"), arguments=())

        result = OpcodeResult(ctx.entry, value=expression, dest_reg=dest_reg)
        ctx.analysis.add_result(result)

        return result
