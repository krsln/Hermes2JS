from hermes_decompiler.handlers import OpcodeHandler, REG, UINT16, sequence
from hermes_decompiler.ir.expressions import ArrayExpression
from hermes_decompiler.opcode import OpcodeEntry, OpcodeResult
from hermes_decompiler.runtime import HermesAnalysis


# DEFINE_OPCODE_2(NewArray, Reg8, UInt16)
# Example: <NewArray>: <Reg8: 1, UInt16: 4>
class NewArray(OpcodeHandler):
    """Create a new, empty Array with a preallocation size hint."""

    _PATTERN = sequence(REG, UINT16)

    def handle(self, analysis: HermesAnalysis, entry: OpcodeEntry) -> OpcodeResult:
        match = self._PATTERN.match(entry.args.strip())
        if not match:
            return self.build_invalid_args_result(analysis, entry, "Expected Reg8 and UInt16 arguments")

        dest_reg, capacity_hint = map(int, match.groups())

        # NOTE: `capacity_hint` (Hermes' pre-allocation size) is dropped
        # here - `ArrayExpression` has no field for it, since it isn't
        # a JS-observable property. The raw UInt16 is still visible in
        # verbose mode via the `// CODE ->` bytecode comment.
        expression = ArrayExpression(elements=())

        result = OpcodeResult(entry, value=expression, dest_reg=dest_reg)
        analysis.add_result(result)

        return result
