from hermes_decompiler.handlers._shared_patterns import REG, UINT8, sequence
from hermes_decompiler.ir import Identifier
from hermes_decompiler.models.HermesAnalysis import HermesAnalysis
from hermes_decompiler.models.OpcodeEntry import OpcodeEntry
from hermes_decompiler.models.OpcodeHandler import OpcodeHandler
from hermes_decompiler.models.OpcodeResult import OpcodeResult


# DEFINE_OPCODE_2(LoadParam, Reg8, UInt8)
# Example: <LoadParam>: <Reg8: 1, UInt8: 1>
class LoadParam(OpcodeHandler):
    """Load function parameter (including this at index 0)."""

    _PATTERN = sequence(REG, UINT8)

    def handle(self, analysis: HermesAnalysis, entry: OpcodeEntry) -> OpcodeResult:

        match = self._PATTERN.match(entry.args.strip())
        if not match:
            return self.build_invalid_args_result(analysis, entry)

        dest_reg, param_index = map(int, match.groups())

        # param0 = this, others = paramN
        name = "this" if param_index == 0 else f"param{param_index}"
        expression = Identifier(name=name)

        result = OpcodeResult(entry, value=expression, dest_reg=dest_reg)
        analysis.add_result(result)

        return result
