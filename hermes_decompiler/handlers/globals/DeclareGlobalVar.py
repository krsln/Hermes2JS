from hermes_decompiler.handlers import OpcodeHandler, STRING_ID, sequence
from hermes_decompiler.ir.Operators import VariableKind
from hermes_decompiler.ir.expressions import Identifier
from hermes_decompiler.ir.statements import VariableDeclaration, VariableDeclarator
from hermes_decompiler.opcode import OpcodeEntry, OpcodeResult
from hermes_decompiler.runtime import HermesAnalysis


# UInt32 (string_id) (total size 4)
# DEFINE_OPCODE_1(DeclareGlobalVar, UInt32)
# Example: <DeclareGlobalVar>: <string_id: 209>  # String: 'process' (Identifier)
class DeclareGlobalVar(OpcodeHandler):
    """
    Side-effect-only opcode - no destination register, so the resulting
    statement is recorded under an empty register key (same convention as
    Ret/Throw/PutByVal for statements with no downstream chainable value).
    """

    _PATTERN = sequence(STRING_ID)

    def handle(self, analysis: HermesAnalysis, entry: OpcodeEntry) -> OpcodeResult:
        match = self._PATTERN.match(entry.args.strip())
        if not match:
            return self.build_invalid_args_result(analysis, entry, "Expected a single string_id argument")

        string_id = int(match.group(1))
        prop_name = entry.identifier_name or f"string_{string_id}"

        # A real `var` declaration statement, not an Expression - this is
        # the `ir.statements.VariableDeclaration`, distinct from the old
        # legacy `ir.Values.VariableDeclaration` (which was mistakenly a
        # Value/Expression subclass despite having no meaningful value).
        declaration = VariableDeclaration(
            kind=VariableKind.VAR,
            declarations=(VariableDeclarator(id=Identifier(name=prop_name)),),
        )

        result = OpcodeResult(entry, value=None, statement=declaration, dest_reg=None)
        analysis.add_result(result)

        return result
