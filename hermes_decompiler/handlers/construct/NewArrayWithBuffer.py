from hermes_decompiler.handlers import OpcodeHandler, REG, UINT16, sequence
from hermes_decompiler.ir.expressions import ArrayExpression, python_literal
from hermes_decompiler.opcode import OpcodeEntry, OpcodeResult
from hermes_decompiler.runtime import HermesAnalysis


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
