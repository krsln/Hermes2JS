from hermes_decompiler.core.logging import get_logger
from hermes_decompiler.frontend.opcode import OpcodeResult
from hermes_decompiler.handlers import OpcodeHandler, OpcodeContext, ArgsPattern, sequence, REG, UINT8
from hermes_decompiler.ir.expressions import CallExpression, Identifier

logger = get_logger(__name__)


# Reg8, Reg8, UInt8 (total size 3)
# DEFINE_OPCODE_3(DirectEval, Reg8, Reg8, UInt8)
# DEFINE_OPCODE_2(DirectEval, Reg8, Reg8)
# Example: <DirectEval>: <Reg8: 4, Reg8: 9, UInt8: 1>
class DirectEval(OpcodeHandler):
    """
    Performs a direct `eval(...)` call: evaluates the source string held
    in `evalText`, using the calling scope's strictness rather than
    eval's own (that's what makes it "direct" as opposed to indirect/
    global eval).
    """

    ARGUMENTS = (
        ArgsPattern(sequence(REG, REG, UINT8), "Reg8, Reg8, UInt8"),
        ArgsPattern(sequence(REG, REG), "Reg8, Reg8"),  # DEFINE_OPCODE_2
    )

    def handle(self, ctx: OpcodeContext) -> OpcodeResult:
        match = self.match_arguments(ctx)
        if isinstance(match, OpcodeResult):
            return match

        dest_reg = int(match.group(1))
        eval_text_reg = int(match.group(2))
        # strict_flag = int(match.group(3))
        # Caller-scope strictness has no separate JS-visible surface -
        # eval() is emitted the same way regardless; the VM applies the
        # flag internally when it actually evaluates the source.

        eval_text = self.get_register_expression(ctx.analysis, eval_text_reg)

        expression = CallExpression(callee=Identifier(name="eval"), arguments=(eval_text,))

        result = OpcodeResult(ctx.entry, value=expression, dest_reg=dest_reg)
        ctx.analysis.add_result(result)

        return result
