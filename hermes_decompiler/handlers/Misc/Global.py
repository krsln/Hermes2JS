import re

from hermes_decompiler.models.HermesAnalysis import HermesAnalysis
from hermes_decompiler.models.OpcodeResult import OpcodeResult
from hermes_decompiler.models.JSVariable import JSVariable
from hermes_decompiler.models.OpcodeEntry import OpcodeEntry
from hermes_decompiler.models.OpcodeHandler import OpcodeHandler

from hermes_decompiler.handlers._shared_patterns import REG, STRING_ID, sequence


# DEFINE_OPCODE_1(GetGlobalObject, Reg8)
# Example: <GetGlobalObject>: <Reg8: 2>
class GetGlobalObject(OpcodeHandler):
    """Get the global object (global scope)."""
    _PATTERN = sequence(REG)

    def handle(self, analysis: HermesAnalysis, entry: OpcodeEntry) -> OpcodeResult:
        handler = self.__class__.__name__

        match = self._PATTERN.match(entry.args.strip())
        if not match:
            return self.build_invalid_args_result(analysis, entry)

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

        analysis.add_result(entry, variable)
        return OpcodeResult(entry, variable)


# DEFINE_OPCODE_1(DeclareGlobalVar, UInt32)
# Example: <DeclareGlobalVar>: <string_id: 4522>  # String: 'myGlobal' (Identifier)
class DeclareGlobalVar(OpcodeHandler):
    """
    Side-effect-only opcode — no destination register, so the resulting
    statement is recorded under an empty register key (same convention as
    Ret/Throw/PutByVal for statements with no downstream chainable value).
    """
    _PATTERN = sequence(STRING_ID)

    def handle(self, analysis: HermesAnalysis, entry: OpcodeEntry) -> OpcodeResult:
        handler = self.__class__.__name__

        match = self._PATTERN.match(entry.args.strip())
        if not match:
            return self.build_invalid_args_result(analysis, entry, "Expected a single string_id argument")

        string_id = int(match.group(1))
        prop_name = self.resolve_property_name(analysis, entry, string_id)
        if prop_name is None:
            error = f'/* Error: string_id {string_id} not found in stringTable */ undefined'
            return self.build_exception_result(analysis, entry, error)

        variable = JSVariable(handler, entry.address, "", f"var {prop_name};")
        analysis.add_result(entry, variable)

        return OpcodeResult(entry, variable)
