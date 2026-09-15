from hermes_decompiler.frontend.handlers import OpcodeHandler, OpcodeContext, ArgsPattern, sequence, STRING_ID
from hermes_decompiler.frontend.opcode import OpcodeResult
from hermes_decompiler.ir.Operators import VariableKind
from hermes_decompiler.ir.expressions import Identifier
from hermes_decompiler.ir.statements import VariableDeclaration, VariableDeclarator


# UInt32 (string_id) (total size 4)
# DEFINE_OPCODE_1(DeclareGlobalVar, UInt32)
# Example: <DeclareGlobalVar>: <string_id: 209>  # String: 'process' (Identifier)
class DeclareGlobalVar(OpcodeHandler):
    """
    Side-effect-only opcode - no destination register, so the resulting
    statement is recorded under an empty register key (same convention as
    Ret/Throw/PutByVal for statements with no downstream chainable value).
    """

    ARGUMENTS = ArgsPattern(sequence(STRING_ID), "UInt32 (string_id) (total size 4)")

    def handle(self, ctx: OpcodeContext) -> OpcodeResult:
        match = self.match_arguments(ctx)
        if isinstance(match, OpcodeResult):
            return match

        string_id = int(match.group(1))
        prop_name = ctx.entry.identifier_name or f"string_{string_id}"

        # A real `var` declaration statement, not an Expression - this is
        # the `ir.statements.VariableDeclaration`, distinct from the old
        # legacy `ir.Values.VariableDeclaration` (which was mistakenly a
        # Value/Expression subclass despite having no meaningful value).
        declaration = VariableDeclaration(
            kind=VariableKind.VAR,
            declarations=(VariableDeclarator(id=Identifier(name=prop_name)),),
        )

        result = OpcodeResult(ctx.entry, value=None, statement=declaration, dest_reg=None)
        ctx.analysis.add_result(result)

        return result
