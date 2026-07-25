from hermes_decompiler.models.HermesAnalysis import HermesAnalysis
from hermes_decompiler.models.OpcodeResult import OpcodeResult
from hermes_decompiler.models.OpcodeEntry import OpcodeEntry
from hermes_decompiler.models.OpcodeHandler import OpcodeHandler
from hermes_decompiler.ir import AssignmentExpression, MemberExpression
from hermes_decompiler.ir.Operators import AssignmentOperator

from hermes_decompiler.handlers._shared_patterns import REG, sequence


# DEFINE_OPCODE_3(PutByVal, Reg8, Reg8, Reg8)
# Example: <PutByVal>: <Reg8: 98, Reg8: 2, Reg8: 0>
class PutByVal(OpcodeHandler):
    _PATTERN = sequence(REG, REG, REG)

    def handle(self, analysis: HermesAnalysis, entry: OpcodeEntry) -> OpcodeResult:
        match = self._PATTERN.match(entry.args.strip())
        if not match:
            return self.build_invalid_args_result(analysis, entry, "Expected three Reg8 arguments")

        obj_reg, key_reg, value_reg = map(int, match.groups())

        left = MemberExpression(
            receiver=self.get_register_value(analysis, obj_reg),
            member=self.get_register_value(analysis, key_reg),
            computed=True,
        )
        right = self.get_register_value(analysis, value_reg)

        expression = AssignmentExpression(left=left, operator=AssignmentOperator.ASSIGN, right=right)

        result = OpcodeResult(entry, value=expression, dest_reg=None)
        analysis.add_result(result)

        return result
