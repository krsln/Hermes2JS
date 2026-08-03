from hermes_decompiler.handlers import OpcodeHandler, REG, sequence
from hermes_decompiler.ir.expressions import CallExpression, Identifier, MemberExpression
from hermes_decompiler.frontend.opcode import OpcodeEntry, OpcodeResult
from hermes_decompiler.runtime import HermesAnalysis


# /// Get the next property in the for..in iterator.
# /// Returns Arg1, which is the next property. Undefined if unavailable.
# /// Arg2 is the register that holds array of properties.
# /// Arg3 is the register that holds the object.
# /// Arg4 is the register that holds the iterating index.
# /// Arg5 is the register that holds the size of the property list.
# DEFINE_OPCODE_5(GetNextPName, Reg8, Reg8, Reg8, Reg8, Reg8)

# Reg8, Reg8, Reg8, Reg8, Reg8 (total size 5)
# DEFINE_OPCODE_5(GetNextPName, Reg8, Reg8, Reg8, Reg8, Reg8)
# Example: <GetNextPName>: <Reg8: 7, Reg8: 9, Reg8: 8, Reg8: 0, Reg8: 1>
class GetNextPName(OpcodeHandler):
    _PATTERN = sequence(REG, REG, REG, REG, REG)

    def handle(self, analysis: HermesAnalysis, entry: OpcodeEntry) -> OpcodeResult:
        match = self._PATTERN.match(entry.args.strip())
        if not match:
            return self.build_invalid_args_result(analysis, entry, "Expected five Reg8 arguments")

        dest_reg, list_reg, _obj_reg, _index_reg, _size_reg = map(int, match.groups())
        list_val = self.get_register_reference(analysis, list_reg)

        callee = MemberExpression(list_val, Identifier(name="next"))

        # for-in step
        expression = CallExpression(callee=callee, arguments=())

        result = OpcodeResult(entry, value=expression, dest_reg=dest_reg)
        analysis.add_result(result)

        return result
