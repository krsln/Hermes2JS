from hermes_decompiler.frontend.opcode import OpcodeEntry, OpcodeResult
from hermes_decompiler.handlers import sequence, REG
from hermes_decompiler.handlers.OpcodeHandler import OpcodeHandler
from hermes_decompiler.ir.expressions import MemberExpression, NewExpression
from hermes_decompiler.runtime import HermesAnalysis


# Reg8, Reg8, Reg8 (total size 3)
# DEFINE_OPCODE_3(SelectObject, Reg8, Reg8, Reg8)
# Example: <SelectObject>: <Reg8: 6, Reg8: 7, Reg8: 4>
class SelectObject(OpcodeHandler):
    """
    Selects between the newly created 'this' object or the return value of a constructor.
    In JS decompilation, this usually unwraps directly to the created object (NewExpression).
    """

    _PATTERN = sequence(REG, REG, REG)

    def handle(self, analysis: HermesAnalysis, entry: OpcodeEntry) -> OpcodeResult:
        match = self._PATTERN.match(entry.args.strip())
        if not match:
            return self.build_invalid_args_result(analysis, entry)

        dest_reg, obj_reg, selector_reg = map(int, match.groups())

        obj = self.get_register_expression(analysis, obj_reg)
        selector = self.get_register_expression(analysis, selector_reg)

        # Eğer taraflardan biri NewExpression ise, SelectObject katmanını kaldırıp
        # doğrudan NewExpression'ı döndür (JS 'new' Semantiği).
        if isinstance(selector, NewExpression):
            expression = selector
        elif isinstance(obj, NewExpression):
            expression = obj
        else:
            # Standart computed member access (fallback)
            expression = MemberExpression(receiver=obj, member=selector, computed=True)

        result = OpcodeResult(entry, value=expression, dest_reg=dest_reg)
        analysis.add_result(result)

        return result
