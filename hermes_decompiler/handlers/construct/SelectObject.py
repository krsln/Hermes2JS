from hermes_decompiler.frontend.opcode import OpcodeResult
from hermes_decompiler.handlers import OpcodeHandler, OpcodeContext, ArgsPattern, sequence, REG
from hermes_decompiler.ir.expressions import MemberExpression, NewExpression


# Reg8, Reg8, Reg8 (total size 3)
# DEFINE_OPCODE_3(SelectObject, Reg8, Reg8, Reg8)
# Example: <SelectObject>: <Reg8: 6, Reg8: 7, Reg8: 4>
class SelectObject(OpcodeHandler):
    """
    Selects between the newly created `this` object and the return value
    of a constructor. During decompilation, this can often be simplified
    to the underlying NewExpression.
    """

    ARGUMENTS = ArgsPattern(sequence(REG, REG, REG), "Reg8, Reg8, Reg8")

    def handle(self, ctx: OpcodeContext) -> OpcodeResult:

        match = self.match_arguments(ctx)
        if isinstance(match, OpcodeResult):
            return match

        dest_reg, obj_reg, selector_reg = map(int, match.groups())

        raw_obj = self._peek_raw(ctx.analysis, obj_reg)
        raw_selector = self._peek_raw(ctx.analysis, selector_reg)

        # If either operand is a NewExpression, unwrap the SelectObject layer
        # and preserve the NewExpression directly, matching JavaScript's `new`
        # constructor semantics.
        if isinstance(raw_selector, NewExpression):
            expression = raw_selector
            self._mark_used(ctx.analysis, selector_reg)
        elif isinstance(raw_obj, NewExpression):
            expression = raw_obj
            self._mark_used(ctx.analysis, obj_reg)
        else:
            # Standard computed member access (fallback)
            obj = self.get_register_expression(ctx.analysis, obj_reg)
            selector = self.get_register_expression(ctx.analysis, selector_reg)
            expression = MemberExpression(obj=obj, prop=selector, computed=True)

        result = OpcodeResult(ctx.entry, value=expression, dest_reg=dest_reg)
        ctx.analysis.add_result(result)

        return result

    @staticmethod
    def _peek_raw(analysis, reg):
        state = analysis.registers.get(f"r{reg}")
        return state.value if state and state.definition else None

    @staticmethod
    def _mark_used(analysis, reg):
        state = analysis.registers.get(f"r{reg}")
        if state and state.definition:
            state.reads += 1
            state.definition.definition_used = True
