from hermes_decompiler.frontend.opcode import OpcodeResult
from hermes_decompiler.handlers import OpcodeHandler, OpcodeContext, ArgsPattern, sequence, REG
from hermes_decompiler.ir.expressions import CallExpression, Identifier


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
    ARGUMENTS = ArgsPattern(sequence(REG, REG, REG, REG), "Reg8, Reg8, Reg8, Reg8 (total size 4)")

    def handle(self, ctx: OpcodeContext) -> OpcodeResult:
        match = self.match_arguments(ctx)
        if isinstance(match, OpcodeResult):
            return match

        dest_reg, obj_reg, _index_reg, _size_reg = map(int, match.groups())
        obj = self.get_register_reference(ctx.analysis, obj_reg)

        # for-in property list
        expression = CallExpression(callee=Identifier(name="HermesPropertyIterator"), arguments=(obj,))

        result = OpcodeResult(ctx.entry, value=expression, dest_reg=dest_reg)
        ctx.analysis.add_result(result)

        return result
