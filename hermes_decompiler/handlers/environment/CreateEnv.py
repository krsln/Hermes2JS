from hermes_decompiler.frontend.opcode import OpcodeEntry, OpcodeResult
from hermes_decompiler.handlers import sequence, REG, UINT32
from hermes_decompiler.handlers.OpcodeHandler import OpcodeHandler
from hermes_decompiler.ir.expressions import CallExpression, Identifier
from hermes_decompiler.runtime import HermesAnalysis


# Reg8, Reg8, UInt32 (total size 6)
# DEFINE_OPCODE_3(CreateEnvironment, Reg8, Reg8, UInt32)
# DEFINE_OPCODE_1(CreateEnvironment, Reg8)
# Example: <CreateEnvironment>: <Reg8: 3, Reg8: 2, UInt32: 1>
class CreateEnvironment(OpcodeHandler):
    """
    Allocate a new lexical environment.

    Hermes uses environment objects to store variables
    captured by nested closures.
    """

    _PATTERN = sequence(REG, REG, UINT32)
    _PATTERN_OLD = sequence(REG)  # DEFINE_OPCODE_1

    def handle(self, analysis: HermesAnalysis, entry: OpcodeEntry) -> OpcodeResult:
        match = (
                self._PATTERN.match(entry.args.strip())
                or self._PATTERN_OLD.match(entry.args.strip())
        )
        if not match:
            return self.build_invalid_args_result(analysis, entry)

        dest_reg = int(match.group(1))

        expression = CallExpression(callee=Identifier(name="createEnvironment"), arguments=())

        result = OpcodeResult(entry, value=expression, dest_reg=dest_reg)
        analysis.add_result(result)

        return result
