from hermes_decompiler.frontend.opcode import OpcodeEntry, OpcodeResult
from hermes_decompiler.handlers import OpcodeHandler, sequence, REG, UINT8
from hermes_decompiler.ir.expressions import Identifier
from hermes_decompiler.runtime import HermesAnalysis


# Reg8, UInt8 (total size 2)
# DEFINE_OPCODE_2(CreateFunctionEnvironment, Reg8, UInt8)
# Example: <CreateFunctionEnvironment>: <Reg8: 7, UInt8: 1>
class CreateFunctionEnvironment(OpcodeHandler):
    """Allocate a new function-local environment/scope record."""

    _PATTERN = sequence(REG, UINT8)

    def handle(self, analysis: HermesAnalysis, entry: OpcodeEntry) -> OpcodeResult:
        match = self._PATTERN.match(entry.args.strip())
        if not match:
            return self.build_invalid_args_result(analysis, entry, "Expected Reg8, UInt8 arguments")

        dest_reg, _size = map(int, match.groups())

        expression = Identifier(name="__environment__")

        result = OpcodeResult(entry, value=expression, dest_reg=dest_reg)
        analysis.add_result(result)

        return result
