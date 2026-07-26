from hermes_decompiler.handlers import OpcodeHandler, REG, sequence
from hermes_decompiler.opcode import OpcodeEntry, OpcodeResult
from hermes_decompiler.runtime import HermesAnalysis


class Mov(OpcodeHandler):
    """Move value between registers: rX = rY"""

    _PATTERN = sequence(REG, REG)

    def handle(self, analysis: HermesAnalysis, entry: OpcodeEntry) -> OpcodeResult:
        match = self._PATTERN.match(entry.args.strip())
        if not match:
            return self.build_invalid_args_result(analysis, entry)

        dest_reg, src_reg = map(int, match.groups())

        expression = self.get_register_value(analysis, src_reg)

        result = OpcodeResult(entry, value=expression, dest_reg=dest_reg)
        analysis.add_result(result)

        return result
