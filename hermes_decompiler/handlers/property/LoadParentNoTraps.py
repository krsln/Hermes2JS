from hermes_decompiler.frontend.opcode import OpcodeResult
from hermes_decompiler.handlers import OpcodeHandler, OpcodeContext, sequence, REG
from hermes_decompiler.ir.expressions import CallExpression, Identifier


# Reg8, Reg8 (total size 2)
# DEFINE_OPCODE_2(LoadParentNoTraps, Reg8, Reg8)
# Example: <LoadParentNoTraps>: <Reg8: 3, Reg8: 3>
class LoadParentNoTraps(OpcodeHandler):
    """Get an object's ordinary [[GetPrototypeOf]], bypassing Proxy traps."""

    _PATTERN = sequence(REG, REG)

    def handle(self, ctx: OpcodeContext) -> OpcodeResult:
        match = self._PATTERN.match(ctx.entry.args.strip())
        if not match:
            return self.build_invalid_args_result(ctx.analysis, ctx.entry, "Expected Reg8, Reg8 arguments")

        dest_reg, obj_reg = map(int, match.groups())

        obj = self.get_register_expression(ctx.analysis, obj_reg)

        expression = CallExpression(
            callee=Identifier(name="__getPrototypeOfNoTraps__"),
            arguments=(obj,),
        )

        result = OpcodeResult(ctx.entry, value=expression, dest_reg=dest_reg)
        ctx.analysis.add_result(result)

        return result
