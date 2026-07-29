from hermes_decompiler.handlers import OpcodeHandler, REG, UINT32, sequence
from hermes_decompiler.ir.expressions import Identifier
from hermes_decompiler.opcode import OpcodeEntry, OpcodeResult
from hermes_decompiler.runtime import HermesAnalysis


# Reg8, UInt32 (total size 5)
# DEFINE_OPCODE_2(CreateTopLevelEnvironment, Reg8, UInt32)
# Example: <CreateTopLevelEnvironment>: <Reg8: 2, UInt32: 3>
class CreateTopLevelEnvironment(OpcodeHandler):
    """Allocate the parentless module/global-level environment record."""

    _PATTERN = sequence(REG, UINT32)

    def handle(self, analysis: HermesAnalysis, entry: OpcodeEntry) -> OpcodeResult:
        match = self._PATTERN.match(entry.args.strip())
        if not match:
            return self.build_invalid_args_result(analysis, entry, "Expected Reg8, UInt32 arguments")

        dest_reg, _size = map(int, match.groups())

        expression = Identifier(name="__environment__")

        result = OpcodeResult(entry, value=expression, dest_reg=dest_reg)
        analysis.add_result(result)

        return result
