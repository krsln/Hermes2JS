from hermes_decompiler.ir.Values import ReturnValue
from hermes_decompiler.models.HermesAnalysis import HermesAnalysis
from hermes_decompiler.models.OpcodeResult import OpcodeResult, ControlFlowType
from hermes_decompiler.models.JSVariable import JSVariable
from hermes_decompiler.models.OpcodeEntry import OpcodeEntry
from hermes_decompiler.models.OpcodeHandler import OpcodeHandler

from hermes_decompiler.handlers._shared_patterns import REG, sequence


# DEFINE_OPCODE_1(Ret, Reg8)
# Example: <Ret>: <Reg8: 1>
class Ret(OpcodeHandler):
    """Return a value from the current function."""
    _PATTERN = sequence(REG)

    def handle(self, analysis: HermesAnalysis, entry: OpcodeEntry) -> OpcodeResult:
        handler = self.__class__.__name__

        match = self._PATTERN.match(entry.args.strip())

        if match:
            reg = int(match.group(1))
            value = self.get_register_value_new(analysis, reg)
            return_value = ReturnValue(value)
        else:
            return_value = ReturnValue()

        variable = JSVariable(
            handler,
            entry.address,
            "",
            return_value,
        )

        analysis.add_result(entry, variable)

        return OpcodeResult(
            entry,
            variable,
            control_flow=ControlFlowType.RETURN,
        )
