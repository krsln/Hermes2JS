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

        obj = self.get_register_expression(ctx.analysis, obj_reg)
        selector = self.get_register_expression(ctx.analysis, selector_reg)

        # If either operand is a NewExpression, unwrap the SelectObject layer
        # and preserve the NewExpression directly, matching JavaScript's `new`
        # constructor semantics.
        if isinstance(selector, NewExpression):
            expression = selector
        elif isinstance(obj, NewExpression):
            expression = obj
        else:
            # Standard computed member access (fallback)
            expression = MemberExpression(obj=obj, prop=selector, computed=True)

        result = OpcodeResult(ctx.entry, value=expression, dest_reg=dest_reg)
        ctx.analysis.add_result(result)

        return result
