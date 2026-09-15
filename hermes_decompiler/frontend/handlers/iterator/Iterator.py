from hermes_decompiler.frontend.handlers import OpcodeHandler, OpcodeContext, ArgsPattern, sequence, REG, UINT8
from hermes_decompiler.frontend.opcode import OpcodeResult
from hermes_decompiler.ir.expressions import CallExpression, Identifier, MemberExpression


# Reg8, Reg8 (total size 2)
# DEFINE_OPCODE_2(IteratorBegin, Reg8, Reg8)
# Example: <IteratorBegin>: <Reg8: 1, Reg8: 2>
class IteratorBegin(OpcodeHandler):
    """Begin iteration over an iterable."""

    ARGUMENTS = ArgsPattern(sequence(REG, REG), "Reg8, Reg8")

    def handle(self, ctx: OpcodeContext) -> OpcodeResult:
        match = self.match_arguments(ctx)
        if isinstance(match, OpcodeResult):
            return match

        iterator_reg, iterable_reg = map(int, match.groups())
        iterable = self.get_register_reference(ctx.analysis, iterable_reg)

        # Named pseudo-call, same convention as getEnvironment()/
        # HermesPropertyIterator() elsewhere - GetIterator() is not
        # real JS syntax but a VM-level operation.
        expression = CallExpression(callee=Identifier(name="GetIterator"), arguments=(iterable,))

        result = OpcodeResult(ctx.entry, value=expression, dest_reg=iterator_reg)
        ctx.analysis.add_result(result)

        return result


# Reg8, Reg8, Reg8 (total size 3)
# DEFINE_OPCODE_3(IteratorNext, Reg8, Reg8, Reg8)
# Example: <IteratorNext>: <Reg8: 9, Reg8: 2, Reg8: 9>
class IteratorNext(OpcodeHandler):
    """Advance iterator."""

    ARGUMENTS = ArgsPattern(sequence(REG, REG, REG), "Reg8, Reg8, Reg8")

    def handle(self, ctx: OpcodeContext) -> OpcodeResult:
        match = self.match_arguments(ctx)
        if isinstance(match, OpcodeResult):
            return match

        result_reg, iterator_reg, _ = map(int, match.groups())
        iterator = self.get_register_expression(ctx.analysis, iterator_reg)

        callee = MemberExpression(iterator, Identifier(name="next"))
        expression = CallExpression(callee=callee, arguments=())

        result = OpcodeResult(ctx.entry, value=expression, dest_reg=result_reg)
        ctx.analysis.add_result(result)

        return result


# Reg8, UInt8 (total size 2)
# DEFINE_OPCODE_2(IteratorClose, Reg8, UInt8)
# Example: <IteratorClose>: <Reg8: 2, UInt8: 1>
class IteratorClose(OpcodeHandler):
    """
    Close iterator.

    NOTE (fix): pattern was `sequence(REG, REG)` but the real operand
    layout is `Reg8, UInt8` - the second operand is a flag (e.g.
    "ignoreInnerException"), not a register. The mismatched pattern
    made every IteratorClose fail to match, so the actual `.return()`
    call was never emitted - only an inline error comment was, and the
    real cleanup call silently vanished from the generated JS.
    """

    ARGUMENTS = ArgsPattern(sequence(REG, UINT8), "Reg8, UInt8")

    def handle(self, ctx: OpcodeContext) -> OpcodeResult:
        match = self.match_arguments(ctx)
        if isinstance(match, OpcodeResult):
            return match

        iterator_reg = int(match.group(1))
        # match.group(2) is the ignore-inner-exception flag - not
        # needed for rendering `.return()` itself.
        iterator = self.get_register_expression(ctx.analysis, iterator_reg)

        callee = MemberExpression(iterator, Identifier(name="return"))
        expression = CallExpression(callee=callee, arguments=())

        result = OpcodeResult(ctx.entry, value=expression, dest_reg=None)
        ctx.analysis.add_result(result)

        return result
