from hermes_decompiler.handlers._shared_patterns import REG, STRING_ID, sequence
from hermes_decompiler.ir import Identifier, VariableDeclaration, VariableDeclarator
from hermes_decompiler.ir.Operators import VariableKind
from hermes_decompiler.models.HermesAnalysis import HermesAnalysis
from hermes_decompiler.models.OpcodeEntry import OpcodeEntry
from hermes_decompiler.models.OpcodeHandler import OpcodeHandler
from hermes_decompiler.models.OpcodeResult import OpcodeResult


# DEFINE_OPCODE_1(GetGlobalObject, Reg8)
# Example: <GetGlobalObject>: <Reg8: 2>
class GetGlobalObject(OpcodeHandler):
    """Get the global object (global scope)."""

    _PATTERN = sequence(REG)

    def handle(self, analysis: HermesAnalysis, entry: OpcodeEntry) -> OpcodeResult:
        match = self._PATTERN.match(entry.args.strip())
        if not match:
            return self.build_invalid_args_result(analysis, entry)

        dest_reg = int(match.group(1))

        # Track global object register in analysis
        analysis.globalObjects = dest_reg

        expression = Identifier(name="globalThis")

        result = OpcodeResult(entry, value=expression, dest_reg=dest_reg)
        analysis.add_result(result)

        return result


# DEFINE_OPCODE_1(DeclareGlobalVar, UInt32)
# Example: <DeclareGlobalVar>: <string_id: 4522>  # String: 'myGlobal' (Identifier)
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
