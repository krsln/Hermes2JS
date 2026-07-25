from hermes_decompiler.handlers._shared_patterns import REG, UINT16, sequence
from hermes_decompiler.ir import ArrayExpression, python_literal
from hermes_decompiler.models.HermesAnalysis import HermesAnalysis
from hermes_decompiler.models.OpcodeEntry import OpcodeEntry
from hermes_decompiler.models.OpcodeHandler import OpcodeHandler
from hermes_decompiler.models.OpcodeResult import OpcodeResult


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


class NewArrayWithBuffer(OpcodeHandler):
    """Create a new array from a static buffer."""

    _PATTERN = sequence(REG, UINT16, UINT16, UINT16)

    def handle(self, analysis: HermesAnalysis, entry: OpcodeEntry) -> OpcodeResult:

        match = self._PATTERN.match(entry.args.strip())
        if not match:
            return self.build_invalid_args_result(analysis, entry)

        dest_reg = int(match.group(1))

        if entry.array_literal is None:
            return self.build_exception_result(analysis, entry, "// Warning: No array data in comment")

        elements = tuple(
            python_literal(v)
            for v in entry.array_literal
        )

        expression = ArrayExpression(elements=elements)

        result = OpcodeResult(entry, value=expression, dest_reg=dest_reg)
        analysis.add_result(result)

        return result


class NewArrayWithBufferLong(NewArrayWithBuffer):
    """Long variant."""

    pass
