from hermes_decompiler.frontend.opcode import OpcodeEntry, OpcodeResult
from hermes_decompiler.handlers import sequence, REG
from hermes_decompiler.handlers.OpcodeHandler import OpcodeHandler
from hermes_decompiler.ir.expressions import ObjectExpression
from hermes_decompiler.runtime import HermesAnalysis


# Reg8 (total size 1)
# DEFINE_OPCODE_1(NewObject, Reg8)
# Example: <NewObject>: <Reg8: 7>
class NewObject(OpcodeHandler):
    """Create a new empty object: {}"""

    _PATTERN = sequence(REG)

    def handle(self, analysis: HermesAnalysis, entry: OpcodeEntry) -> OpcodeResult:
        match = self._PATTERN.match(entry.args.strip())
        if not match:
            return self.build_invalid_args_result(analysis, entry)

        dest_reg = int(match.group(1))

        expression = ObjectExpression(properties=())

        result = OpcodeResult(entry, value=expression, dest_reg=dest_reg)
        analysis.add_result(result)

        return result
