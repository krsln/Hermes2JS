from hermes_decompiler.handlers import OpcodeHandler, REG, sequence
from hermes_decompiler.ir.expressions import MemberExpression
from hermes_decompiler.opcode import OpcodeEntry, OpcodeResult
from hermes_decompiler.runtime import HermesAnalysis


# Reg8, Reg8, Reg8 (total size 3)
# DEFINE_OPCODE_3(SelectObject, Reg8, Reg8, Reg8)
# Example: <SelectObject>: <Reg8: 6, Reg8: 7, Reg8: 4>
class SelectObject(OpcodeHandler):
    """Select a property by dynamic key: obj[key]"""

    _PATTERN = sequence(REG, REG, REG)

    def handle(self, analysis: HermesAnalysis, entry: OpcodeEntry) -> OpcodeResult:
        match = self._PATTERN.match(entry.args.strip())
        if not match:
            return self.build_invalid_args_result(analysis, entry)

        dest_reg, obj_reg, selector_reg = map(int, match.groups())

        obj = self.get_register_value(analysis, obj_reg)
        selector = self.get_register_value(analysis, selector_reg)

        expression = MemberExpression(receiver=obj, member=selector, computed=True)

        result = OpcodeResult(entry, value=expression, dest_reg=dest_reg)
        analysis.add_result(result)

        return result
