from hermes_decompiler.frontend.opcode import OpcodeEntry, OpcodeResult
from hermes_decompiler.handlers import sequence
from hermes_decompiler.handlers.OpcodeHandler import OpcodeHandler
from hermes_decompiler.runtime import HermesAnalysis


# (total size 0)
# DEFINE_OPCODE_0(Unreachable)
class Unreachable(OpcodeHandler):
    """Placeholder opcode that should never occur in valid, reachable bytecode."""

    _PATTERN = sequence()

    def handle(self, analysis: HermesAnalysis, entry: OpcodeEntry) -> OpcodeResult:
        error = "// Unreachable opcode encountered - see handlers/controlflow/Unreachable.py"
        return self.build_exception_result(analysis, entry, error)
