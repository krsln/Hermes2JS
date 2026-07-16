import re

from hermes_decompiler.models.HermesAnalysis import HermesAnalysis
from hermes_decompiler.models.OpcodeResult import OpcodeResult
from hermes_decompiler.models.JSVariable import JSVariable
from hermes_decompiler.models.OpcodeEntry import OpcodeEntry
from hermes_decompiler.models.OpcodeHandler import OpcodeHandler

from hermes_decompiler.handlers._shared_patterns import REG, STRING_ID, sequence

_IDENTIFIER_COMMENT_PATTERN = re.compile(r"String:\s*'([^']*)'\s*\(Identifier\)")


# Get the global object (the object in which global variables are stored).
# DEFINE_OPCODE_1(GetGlobalObject, Reg8)
# Example: <GetGlobalObject>: <Reg8: 2>
class GetGlobalObject(OpcodeHandler):
    """Get the global object (global scope)."""
    _PATTERN = sequence(REG)

    def Handle(self, analysis: HermesAnalysis, entry: OpcodeEntry) -> OpcodeResult:
        handler = self.__class__.__name__

        match = self._PATTERN.match(entry.args.strip())
        if not match:
            return self.InvalidArgs(analysis, entry)

        global_reg = int(match.group(1))

        # Track global object register in analysis
        if hasattr(analysis, 'globalObjects'):
            analysis.globalObjects = global_reg
        else:
            # Fallback if the attribute doesn't exist yet
            setattr(analysis, 'globalObjects', global_reg)

        # In JavaScript, global-object is usually represented as `globalThis`
        # or `this` at top-level. Using `globalThis` is more accurate.
        variable = JSVariable(handler, entry.address, f'r{global_reg}', f"globalThis")

        analysis.AddResult(entry, variable)
        return OpcodeResult(entry, variable)


# /// Declare (hoist) a global variable by name, with no initial value —
# /// equivalent to `var name;` at the top level. Emitted once per `var`
# /// declaration found in global/eval scope during hoisting.
# DEFINE_OPCODE_1(DeclareGlobalVar, UInt32)
# OPERAND_STRING_ID(DeclareGlobalVar, 1)
# Example: <DeclareGlobalVar>: <string_id: 4522>  # String: 'myGlobal' (Identifier)
class DeclareGlobalVar(OpcodeHandler):
    """
    Side-effect-only opcode — no destination register, so the resulting
    statement is recorded under an empty register key (same convention as
    Ret/Throw/PutByVal for statements with no downstream chainable value).
    """
    _PATTERN = sequence(STRING_ID)

    def Handle(self, analysis: HermesAnalysis, entry: OpcodeEntry) -> OpcodeResult:
        handler = self.__class__.__name__

        match = self._PATTERN.match(entry.args.strip())
        if not match:
            return self.InvalidArgs(analysis, entry, "Expected a single string_id argument")

        string_id = int(match.group(1))
        var_name = self._resolve_name(analysis, entry, string_id)
        if var_name is None:
            error = f'/* Error: string_id {string_id} not found in stringTable */ undefined'
            return self.Exception(analysis, entry, error)

        variable = JSVariable(handler, entry.address, "", f"var {var_name};")
        analysis.AddResult(entry, variable)

        return OpcodeResult(entry, variable)

    @staticmethod
    def _resolve_name(analysis: HermesAnalysis, entry: OpcodeEntry, string_id: int):
        comment_match = _IDENTIFIER_COMMENT_PATTERN.search(entry.comment or "")
        if comment_match:
            return comment_match.group(1)

        string_table = getattr(analysis, "stringTable", None)
        if string_table is None:
            return None
        return string_table.get(str(string_id))