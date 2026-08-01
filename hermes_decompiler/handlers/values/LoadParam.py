from hermes_decompiler.handlers import OpcodeHandler, REG, UINT8, UINT32, sequence
from hermes_decompiler.ir.expressions import Identifier
from hermes_decompiler.opcode import OpcodeEntry, OpcodeResult
from hermes_decompiler.runtime import HermesAnalysis


# Reg8, UInt8 (total size 2)
# DEFINE_OPCODE_2(LoadParam, Reg8, UInt8)
# Example: <LoadParam>: <Reg8: 6, UInt8: 2>
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


# Reg8, UInt32 (total size 5)
# DEFINE_OPCODE_2(LoadParamLong, Reg8, UInt32)
# Example:
class LoadParamLong(LoadParam):
    """Like LoadParam, but allows accessing arguments >= 255."""

    _PATTERN = sequence(REG, UINT32)
