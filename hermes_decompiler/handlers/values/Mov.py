from hermes_decompiler.frontend.opcode import OpcodeEntry, OpcodeResult
from hermes_decompiler.handlers import OpcodeHandler, sequence, REG
from hermes_decompiler.runtime import HermesAnalysis


# Reg8, Reg8 (total size 2)
# DEFINE_OPCODE_2(Mov, Reg8, Reg8)
# Example: <Mov>: <Reg8: 1, Reg8: 6>
class Mov(OpcodeHandler):
    """Move value between registers: rX = rY"""

    _PATTERN = sequence(REG, REG)

    def handle(self, analysis: HermesAnalysis, entry: OpcodeEntry) -> OpcodeResult:
        match = self._PATTERN.match(entry.args.strip())
        if not match:
            return self.build_invalid_args_result(analysis, entry)

        dest_reg, src_reg = map(int, match.groups())

        expression = self.get_register_expression(analysis, src_reg)

        result = OpcodeResult(entry, value=expression, dest_reg=dest_reg)
        analysis.add_result(result)

        return result


# Reg32, Reg32 (total size 8)
# DEFINE_OPCODE_2(MovLong, Reg32, Reg32)
# Example:
class MovLong(Mov):
    pass
