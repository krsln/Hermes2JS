from hermes_decompiler.models.HermesAnalysis import HermesAnalysis
from hermes_decompiler.models.OpcodeResult import OpcodeResult
from hermes_decompiler.models.JSVariable import JSVariable
from hermes_decompiler.models.OpcodeEntry import OpcodeEntry
from hermes_decompiler.models.OpcodeHandler import OpcodeHandler

from ._shared_patterns import REG, sequence


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
