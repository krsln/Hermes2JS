from hermes_decompiler.handlers._shared_patterns import REG, sequence
from hermes_decompiler.ir import ThrowStatement
from hermes_decompiler.models.HermesAnalysis import HermesAnalysis
from hermes_decompiler.models.OpcodeEntry import OpcodeEntry
from hermes_decompiler.models.OpcodeHandler import OpcodeHandler
from hermes_decompiler.models.OpcodeResult import OpcodeResult, ControlFlowType


# DEFINE_OPCODE_1(Throw, Reg8)
# Example: <Throw>: <Reg8: 2>
class Throw(OpcodeHandler):
    """Throw an exception."""

    _PATTERN = sequence(REG)

    def handle(self, analysis: HermesAnalysis, entry: OpcodeEntry) -> OpcodeResult:
        match = self._PATTERN.match(entry.args.strip())
        if not match:
            return self.build_invalid_args_result(analysis, entry)

        value_reg = int(match.group(1))

        expression = self.get_register_value(analysis, value_reg)
        statement = ThrowStatement(argument=expression)
        flow = ControlFlowType.THROW

        result = OpcodeResult(entry, value=expression, statement=statement, dest_reg=None, control_flow=flow)
        analysis.add_result(result)

        return result
