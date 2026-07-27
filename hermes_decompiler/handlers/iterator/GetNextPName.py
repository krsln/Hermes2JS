from hermes_decompiler.handlers import OpcodeHandler, REG, sequence
from hermes_decompiler.ir.expressions import CallExpression, Identifier, MemberExpression
from hermes_decompiler.opcode import OpcodeEntry, OpcodeResult
from hermes_decompiler.runtime import HermesAnalysis


# DEFINE_OPCODE_5(GetNextPName, Reg8, Reg8, Reg8, Reg8, Reg8)
class GetNextPName(OpcodeHandler):
    _PATTERN = sequence(REG, REG, REG, REG, REG)

    def handle(self, analysis: HermesAnalysis, entry: OpcodeEntry) -> OpcodeResult:
        match = self._PATTERN.match(entry.args.strip())
        if not match:
            return self.build_invalid_args_result(analysis, entry, "Expected five Reg8 arguments")

        dest_reg, list_reg, _obj_reg, _index_reg, _size_reg = map(int, match.groups())
        list_val = self.get_register_value(analysis, list_reg)

        callee = MemberExpression(list_val, Identifier(name="next"))
        # for-in step
        expression = CallExpression(callee=callee, arguments=())

        result = OpcodeResult(entry, value=expression, dest_reg=dest_reg)
        analysis.add_result(result)

        return result
