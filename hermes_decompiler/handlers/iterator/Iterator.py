from hermes_decompiler.handlers import OpcodeHandler, REG, sequence, UINT8
from hermes_decompiler.ir.expressions import CallExpression, Identifier, MemberExpression
from hermes_decompiler.opcode import OpcodeEntry, OpcodeResult
from hermes_decompiler.runtime import HermesAnalysis


# Reg8, Reg8 (total size 2)
# DEFINE_OPCODE_2(IteratorBegin, Reg8, Reg8)
# Example: <IteratorBegin>: <Reg8: 1, Reg8: 2>
class IteratorBegin(OpcodeHandler):
    """Begin iteration over an iterable."""

    _PATTERN = sequence(REG, REG)

    def handle(self, analysis: HermesAnalysis, entry: OpcodeEntry) -> OpcodeResult:
        match = self._PATTERN.match(entry.args.strip())
        if not match:
            return self.build_invalid_args_result(analysis, entry)

        iterator_reg, iterable_reg = map(int, match.groups())
        iterable = self.get_register_expression(analysis, iterable_reg)

        # Named pseudo-call, same convention as getEnvironment()/
        # HermesPropertyIterator() elsewhere - GetIterator() is not
        # real JS syntax but a VM-level operation.
        expression = CallExpression(callee=Identifier(name="GetIterator"), arguments=(iterable,))

        result = OpcodeResult(entry, value=expression, dest_reg=iterator_reg)
        analysis.add_result(result)

        return result


# Reg8, Reg8, Reg8 (total size 3)
# DEFINE_OPCODE_3(IteratorNext, Reg8, Reg8, Reg8)
# Example: <IteratorNext>: <Reg8: 9, Reg8: 2, Reg8: 9>
class IteratorNext(OpcodeHandler):
    """Advance iterator."""

    _PATTERN = sequence(REG, REG, REG)

    def handle(self, analysis: HermesAnalysis, entry: OpcodeEntry) -> OpcodeResult:
        match = self._PATTERN.match(entry.args.strip())
        if not match:
            return self.build_invalid_args_result(analysis, entry)

        result_reg, iterator_reg, _ = map(int, match.groups())
        iterator = self.get_register_expression(analysis, iterator_reg)

        callee = MemberExpression(iterator, Identifier(name="next"))
        expression = CallExpression(callee=callee, arguments=())

        result = OpcodeResult(entry, value=expression, dest_reg=result_reg)
        analysis.add_result(result)

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

    _PATTERN = sequence(REG, UINT8)

    def handle(self, analysis: HermesAnalysis, entry: OpcodeEntry) -> OpcodeResult:
        match = self._PATTERN.match(entry.args.strip())
        if not match:
            return self.build_invalid_args_result(analysis, entry)

        iterator_reg = int(match.group(1))
        # match.group(2) is the ignore-inner-exception flag - not
        # needed for rendering `.return()` itself.
        iterator = self.get_register_expression(analysis, iterator_reg)

        callee = MemberExpression(iterator, Identifier(name="return"))
        expression = CallExpression(callee=callee, arguments=())

        result = OpcodeResult(entry, value=expression, dest_reg=None)
        analysis.add_result(result)

        return result
