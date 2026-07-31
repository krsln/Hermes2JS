from hermes_decompiler.core.logging import get_logger
from hermes_decompiler.handlers import OpcodeHandler, REG, UINT8, sequence
from hermes_decompiler.ir.expressions import CallExpression, Identifier
from hermes_decompiler.opcode import OpcodeEntry, OpcodeResult
from hermes_decompiler.runtime import HermesAnalysis

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

    _PATTERN = sequence(REG, REG, UINT8)
    _PATTERN_OLD = sequence(REG, REG)

    def handle(self, analysis: HermesAnalysis, entry: OpcodeEntry) -> OpcodeResult:
        match = (
                self._PATTERN.match(entry.args.strip())
                or self._PATTERN_OLD.match(entry.args.strip())
        )
        if not match:
            return self.build_invalid_args_result(analysis, entry, "Expected Reg8, Reg8, UInt8 arguments")

        dest_reg = int(match.group(1))
        eval_text_reg = int(match.group(2))
        # strict_flag = int(match.group(3))
        # Caller-scope strictness has no separate JS-visible surface -
        # eval() is emitted the same way regardless; the VM applies the
        # flag internally when it actually evaluates the source.

        eval_text = self.get_register_expression(analysis, eval_text_reg)

        expression = CallExpression(
            callee=Identifier(name="eval"),
            arguments=(eval_text,),
        )

        result = OpcodeResult(entry, value=expression, dest_reg=dest_reg)
        analysis.add_result(result)

        return result
