from hermes_decompiler.frontend.opcode import OpcodeResult
from hermes_decompiler.handlers import OpcodeHandler, OpcodeContext, sequence, REG
from hermes_decompiler.ir.expressions import CallExpression, Identifier, MemberExpression


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

    def handle(self, ctx: OpcodeContext) -> OpcodeResult:
        match = self._PATTERN.match(ctx.entry.args.strip())
        if not match:
            return self.build_invalid_args_result(ctx.analysis, ctx.entry, "Expected five Reg8 arguments")

        dest_reg, list_reg, _obj_reg, _index_reg, _size_reg = map(int, match.groups())
        list_val = self.get_register_reference(ctx.analysis, list_reg)

        callee = MemberExpression(list_val, Identifier(name="next"))

        # for-in step
        expression = CallExpression(callee=callee, arguments=())

        result = OpcodeResult(ctx.entry, value=expression, dest_reg=dest_reg)
        ctx.analysis.add_result(result)

        return result
