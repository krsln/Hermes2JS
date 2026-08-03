from hermes_decompiler.frontend.opcode import OpcodeEntry, OpcodeResult
from hermes_decompiler.handlers import sequence, REG
from hermes_decompiler.handlers.OpcodeHandler import OpcodeHandler
from hermes_decompiler.ir.expressions import Identifier
from hermes_decompiler.runtime import HermesAnalysis


# Reg8 (total size 1)
# DEFINE_OPCODE_1(ReifyArguments, Reg8)
# Example: <ReifyArguments>: <Reg8: 0>
class ReifyArguments(OpcodeHandler):
    _PATTERN = sequence(REG)

    def handle(self, analysis: HermesAnalysis, entry: OpcodeEntry) -> OpcodeResult:
        match = self._PATTERN.match(entry.args.strip())
        if not match:
            return self.build_invalid_args_result(analysis, entry, "Expected Reg8 argument")

        dest_reg = int(match.group(1))

        expression = Identifier(name="arguments")

        result = OpcodeResult(entry, value=expression, dest_reg=dest_reg)
        analysis.add_result(result)

        return result


# Reg8 (total size 1)
# DEFINE_OPCODE_1(ReifyArgumentsStrict, Reg8)
# Example: <ReifyArgumentsStrict>: <Reg8: 1>
class ReifyArgumentsStrict(ReifyArguments):
    pass


# Reg8 (total size 1)
# DEFINE_OPCODE_1(ReifyArgumentsLoose, Reg8)
# Example: <ReifyArgumentsLoose>: <Reg8: 4>
class ReifyArgumentsLoose(ReifyArguments):
    pass
