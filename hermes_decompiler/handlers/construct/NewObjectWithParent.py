from hermes_decompiler.frontend.opcode import OpcodeResult
from hermes_decompiler.handlers import OpcodeHandler, OpcodeContext, ArgsPattern, sequence, REG
from hermes_decompiler.ir.expressions import (
    CallExpression,
    Identifier,
    MemberExpression,
)


# Reg8, Reg8 (total size 2)
# DEFINE_OPCODE_2(NewObjectWithParent, Reg8, Reg8)
# Example: <NewObjectWithParent>: <Reg8: 1, Reg8: 14>
class NewObjectWithParent(OpcodeHandler):
    """Create a new object with the specified prototype."""

    ARGUMENTS = ArgsPattern(sequence(REG, REG), "Reg8, Reg8")

    def handle(self, ctx: OpcodeContext) -> OpcodeResult:
        match = self.match_arguments(ctx)
        if isinstance(match, OpcodeResult):
            return match

        dest_reg, parent_reg = map(int, match.groups())

        parent = self.get_register_expression(ctx.analysis, parent_reg)

        expression = CallExpression(
            callee=MemberExpression(
                Identifier(name="Object"),
                Identifier(name="create"),
            ),
            arguments=(parent,),
        )

        result = OpcodeResult(ctx.entry, value=expression, dest_reg=dest_reg)
        ctx.analysis.add_result(result)

        return result
