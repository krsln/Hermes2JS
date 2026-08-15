from hermes_decompiler.frontend.opcode import OpcodeResult
from hermes_decompiler.handlers import OpcodeHandler, OpcodeContext, ArgsPattern, sequence, REG, STRING_ID
from hermes_decompiler.ir.expressions import CallExpression, Identifier, StringLiteral


# Reg8, UInt32 (string_id) (total size 5)
# DEFINE_OPCODE_2(CreatePrivateName, Reg8, UInt32)
# Example: <CreatePrivateName>: <Reg8: 4, string_id: 11468>  # String: '#code' (Identifier)
class CreatePrivateName(OpcodeHandler):
    """Create a private-name symbol: Symbol('#fieldName')."""

    ARGUMENTS = ArgsPattern(sequence(REG, STRING_ID), "Reg8, UInt32 (string_id)")

    def handle(self, ctx: OpcodeContext) -> OpcodeResult:
        match = self.match_arguments(ctx)
        if isinstance(match, OpcodeResult):
            return match

        dest_reg, string_id = map(int, match.groups())

        name = ctx.entry.identifier_name or f"string_{string_id}"

        expression = CallExpression(
            callee=Identifier(name="Symbol"),
            arguments=(StringLiteral(value=name),),
        )

        result = OpcodeResult(ctx.entry, value=expression, dest_reg=dest_reg)
        ctx.analysis.add_result(result)

        return result
