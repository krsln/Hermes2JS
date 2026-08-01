from hermes_decompiler.handlers import OpcodeHandler, REG, sequence
from hermes_decompiler.ir.expressions import CallExpression, Identifier
from hermes_decompiler.opcode import OpcodeEntry, OpcodeResult
from hermes_decompiler.runtime import HermesAnalysis


# /// Get the list of properties from an object to implement for..in loop.
# /// Returns Arg1, which is the register that holds array of properties.
# /// Returns Undefined if the object is null/undefined.
# /// Arg2 is the register that holds the object.
# /// Arg3 is the register that holds the iterating index.
# /// Arg4 is the register that holds the size of the property list.
# DEFINE_OPCODE_4(GetPNameList, Reg8, Reg8, Reg8, Reg8)

# Reg8, Reg8, Reg8, Reg8 (total size 4)
# DEFINE_OPCODE_4(GetPNameList, Reg8, Reg8, Reg8, Reg8)
# Example: <GetPNameList>: <Reg8: 6, Reg8: 5, Reg8: 0, Reg8: 1>
class GetPNameList(OpcodeHandler):
    _PATTERN = sequence(REG, REG, REG, REG)

    def handle(self, analysis: HermesAnalysis, entry: OpcodeEntry) -> OpcodeResult:
        match = self._PATTERN.match(entry.args.strip())
        if not match:
            return self.build_invalid_args_result(analysis, entry, "Expected four Reg8 arguments")

        dest_reg, obj_reg, _index_reg, _size_reg = map(int, match.groups())
        obj = self.get_register_reference(analysis, obj_reg)

        # for-in property list
        expression = CallExpression(callee=Identifier(name="HermesPropertyIterator"), arguments=(obj,))

        result = OpcodeResult(entry, value=expression, dest_reg=dest_reg)
        analysis.add_result(result)

        return result
