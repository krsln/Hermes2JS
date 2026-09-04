from hermes_decompiler.frontend.opcode import OpcodeResult
from frontend.handlers import OpcodeHandler, OpcodeContext, sequence


# (total size 0)
# DEFINE_OPCODE_0(Unreachable)
class Unreachable(OpcodeHandler):
    """Placeholder opcode that should never occur in valid, reachable bytecode."""

    _PATTERN = sequence()

    def handle(self, ctx: OpcodeContext) -> OpcodeResult:
        error = "// Unreachable opcode encountered - see handlers/controlflow/Unreachable.py"
        return self.build_exception_result(ctx.analysis, ctx.entry, error)
