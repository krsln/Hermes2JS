from hermes_decompiler.frontend.opcode import OpcodeResult
from hermes_decompiler.handlers import OpcodeHandler, OpcodeContext, ArgsPattern, sequence, REG
from hermes_decompiler.ir.expressions import MemberExpression, NewExpression


# Reg8, Reg8, Reg8 (total size 3)
# DEFINE_OPCODE_3(SelectObject, Reg8, Reg8, Reg8)
# Example: <SelectObject>: <Reg8: 6, Reg8: 7, Reg8: 4>
class SelectObject(OpcodeHandler):
    """
    Selects between the newly created 'this' object or the return value of a constructor.
    In JS decompilation, this usually unwraps directly to the created object (NewExpression).
    """

    ARGUMENTS = ArgsPattern(sequence(REG, REG, REG), "Reg8, Reg8, Reg8")

    def handle(self, ctx: OpcodeContext) -> OpcodeResult:
        match = self.match_arguments(ctx)
        if isinstance(match, OpcodeResult):
            return match

        dest_reg, obj_reg, selector_reg = map(int, match.groups())

        obj = self.get_register_expression(ctx.analysis, obj_reg)
        selector = self.get_register_expression(ctx.analysis, selector_reg)

        # Eğer taraflardan biri NewExpression ise, SelectObject katmanını kaldırıp
        # doğrudan NewExpression'ı döndür (JS 'new' Semantiği).
        if isinstance(selector, NewExpression):
            expression = selector
        elif isinstance(obj, NewExpression):
            expression = obj
        else:
            # Standart computed member access (fallback)
            expression = MemberExpression(receiver=obj, member=selector, computed=True)

        result = OpcodeResult(ctx.entry, value=expression, dest_reg=dest_reg)
        ctx.analysis.add_result(result)

        return result
