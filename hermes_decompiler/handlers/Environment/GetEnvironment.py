from hermes_decompiler.models.HermesAnalysis import HermesAnalysis
from hermes_decompiler.models.OpcodeResult import OpcodeResult
from hermes_decompiler.models.JSVariable import JSVariable
from hermes_decompiler.models.OpcodeEntry import OpcodeEntry
from hermes_decompiler.models.OpcodeHandler import OpcodeHandler

from hermes_decompiler.handlers._shared_patterns import REG, UINT8, sequence


# /// Get an environment (scope) from N levels up the stack.
# /// 0 is the current environment, 1 is the caller's environment, etc.
# DEFINE_OPCODE_2(GetEnvironment, Reg8, UInt8)
# Example: <GetEnvironment>: <Reg8: 1, UInt8: 4>
class GetEnvironment(OpcodeHandler):
    """Get environment from N levels up the scope chain."""
    _PATTERN = sequence(REG, UINT8)

    def Handle(self, analysis: HermesAnalysis, entry: OpcodeEntry) -> OpcodeResult:
        handler = self.__class__.__name__

        match = self._PATTERN.match(entry.args.strip())
        if not match:
            return self.InvalidArgs(analysis, entry, "Expected Reg8, UInt8 arguments")

        dest_reg, env_level = map(int, match.groups())

        variable = JSVariable(handler, entry.address, f'r{dest_reg}', f"getEnvironment({env_level})")
        analysis.AddResult(entry, variable)

        return OpcodeResult(entry, variable)
