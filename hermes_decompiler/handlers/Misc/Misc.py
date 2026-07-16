from hermes_decompiler.models.HermesAnalysis import HermesAnalysis
from hermes_decompiler.models.OpcodeResult import OpcodeResult
from hermes_decompiler.models.JSVariable import JSVariable
from hermes_decompiler.models.OpcodeEntry import OpcodeEntry
from hermes_decompiler.models.OpcodeHandler import OpcodeHandler

from hermes_decompiler.handlers._shared_patterns import REG, sequence

# Pre-compiled patterns
_BINARY_REG_PATTERN = sequence(REG, REG, REG)
_UNARY_REG_PATTERN = sequence(REG, REG)


# /// Arg1 = delete Arg2[Arg3].
# DEFINE_OPCODE_3(DelByVal, Reg8, Reg8, Reg8)
# Example: <DelByVal>: <Reg8: 2, Reg8: 0, Reg8: 1>
class DelByVal(OpcodeHandler):
    """delete obj[prop]"""

    def Handle(self, analysis: HermesAnalysis, entry: OpcodeEntry) -> OpcodeResult:
        handler = self.__class__.__name__

        match = _BINARY_REG_PATTERN.match(entry.args.strip())
        if not match:
            return self.InvalidArgs(analysis, entry, "Expected three Reg8 arguments")

        dest_reg, obj_reg, prop_reg = map(int, match.groups())

        obj_val = self.GetValueByReg(analysis.results, obj_reg) or f"r{obj_reg}"
        prop_val = self.GetValueByReg(analysis.results, prop_reg) or f"r{prop_reg}"

        variable = JSVariable(handler, entry.address, f'r{dest_reg}', f"delete {obj_val}[{prop_val}]")
        analysis.AddResult(entry, variable)

        return OpcodeResult(entry, variable)

# TODOs:
# Negate SwitchImm DelById CallBuiltin
