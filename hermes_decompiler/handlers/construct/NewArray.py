from hermes_decompiler.frontend.opcode import OpcodeResult
from hermes_decompiler.handlers import OpcodeHandler, OpcodeContext, sequence, REG, UINT16, UINT32
from hermes_decompiler.ir.expressions import ArrayExpression, python_literal


# Reg8, UInt16 (total size 3)
# DEFINE_OPCODE_2(NewArray, Reg8, UInt16)
# Example: <NewArray>: <Reg8: 1, UInt16: 4>
class NewArray(OpcodeHandler):
    """Create a new, empty Array with a preallocation size hint."""

    _PATTERN = sequence(REG, UINT16)

    def handle(self, ctx: OpcodeContext) -> OpcodeResult:
        match = self._PATTERN.match(ctx.entry.args.strip())
        if not match:
            return self.build_invalid_args_result(ctx.analysis, ctx.entry, "Expected Reg8 and UInt16 arguments")

        dest_reg, capacity_hint = map(int, match.groups())

        # NOTE: `capacity_hint` (Hermes' pre-allocation size) is dropped
        # here - `ArrayExpression` has no field for it, since it isn't
        # a JS-observable property. The raw UInt16 is still visible in
        # verbose mode via the `// CODE ->` bytecode comment.
        expression = ArrayExpression(elements=())

        result = OpcodeResult(ctx.entry, value=expression, dest_reg=dest_reg)
        ctx.analysis.add_result(result)

        return result


# Reg8, UInt16, UInt16, UInt16 (total size 7)
# DEFINE_OPCODE_4(NewArrayWithBuffer, Reg8, UInt16, UInt16, UInt16)
# Example: <NewArrayWithBuffer>: <Reg8: 4, UInt16: 4, UInt16: 4, UInt16: 42610>  # Array: ['0.83', '0.84', '0.85', '0.86']
class NewArrayWithBuffer(OpcodeHandler):
    """Create a new array from a static buffer."""

    _PATTERN = sequence(REG, UINT16, UINT16, UINT16)

    def handle(self, ctx: OpcodeContext) -> OpcodeResult:

        match = self._PATTERN.match(ctx.entry.args.strip())
        if not match:
            return self.build_invalid_args_result(ctx.analysis, ctx.entry)

        dest_reg = int(match.group(1))

        if ctx.entry.array_literal is None:
            return self.build_exception_result(ctx.analysis, ctx.entry, "// Warning: No array data in comment")

        elements = tuple(
            python_literal(v)
            for v in ctx.entry.array_literal
        )

        expression = ArrayExpression(elements=elements)

        result = OpcodeResult(ctx.entry, value=expression, dest_reg=dest_reg)
        ctx.analysis.add_result(result)

        return result


# Reg8, UInt16, UInt16, UInt32 (total size 9)
# DEFINE_OPCODE_4(NewArrayWithBufferLong, Reg8, UInt16, UInt16, UInt32)
class NewArrayWithBufferLong(NewArrayWithBuffer):
    """Long variant."""
    _PATTERN = sequence(REG, UINT16, UINT16, UINT32)
