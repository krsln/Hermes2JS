from hermes_decompiler.models.HermesAnalysis import HermesAnalysis
from hermes_decompiler.models.OpcodeResult import OpcodeResult
from hermes_decompiler.models.JSVariable import JSVariable
from hermes_decompiler.models.OpcodeEntry import OpcodeEntry
from hermes_decompiler.models.OpcodeHandler import OpcodeHandler
from hermes_decompiler.ir.Expressions import IndexExpression, MemberExpression
from hermes_decompiler.ir.Statements import AssignmentStatement

from hermes_decompiler.handlers._shared_patterns import REG, sequence


# DEFINE_OPCODE_3(PutByVal, Reg8, Reg8, Reg8)
# Example: <PutByVal>: <Reg8: 98, Reg8: 2, Reg8: 0>


class PutByVal(OpcodeHandler):
    _PATTERN = sequence(REG, REG, REG)

    def handle(self, analysis: HermesAnalysis, entry: OpcodeEntry) -> OpcodeResult:
        match = self._PATTERN.match(entry.args.strip())
        if not match:
            return self.build_invalid_args_result(
                analysis,
                entry,
                "Expected three Reg8 arguments",
            )

        obj_reg, key_reg, value_reg = map(int, match.groups())

        variable = JSVariable(
            self.__class__.__name__,
            entry.address,
            "",
            AssignmentStatement(
                left=MemberExpression(
                    object=self.get_register_value_new(analysis, obj_reg),
                    property=self.get_register_value_new(analysis, key_reg),
                    computed=True,
                ),
                right=self.get_register_value_new(analysis, value_reg),
            ),
        )

        analysis.add_result(entry, variable)

        return OpcodeResult(entry, variable)
