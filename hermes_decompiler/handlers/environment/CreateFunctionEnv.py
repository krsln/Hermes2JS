from hermes_decompiler.handlers import OpcodeHandler, REG, UINT8, sequence
from hermes_decompiler.ir.expressions import Identifier
from hermes_decompiler.opcode import OpcodeEntry, OpcodeResult
from hermes_decompiler.runtime import HermesAnalysis


# DEFINE_OPCODE_2(CreateFunctionEnvironment, Reg8, UInt8)   [confirmed, hermes-dec table]
#
#   "Create a new environment, using the current function's enclosing
#    environment as the parent. Arg1 is the destination. Arg2 is the
#    size of the new environment."
#
# This is purely an internal scope-allocation instruction -- it has no
# direct JS surface syntax (it backs closures/`let`/`const` scoping
# machinery). Treated as opaque, like CreateEnvironment presumably
# already is in this codebase: it produces a value for its destination
# register but doesn't correspond to a JS expression the user wrote, so
# it's modeled as a call to an internal helper for downstream renderer
# consistency rather than emitting nothing.
class CreateFunctionEnvironment(OpcodeHandler):
    """Allocate a new function-local environment/scope record."""

    _PATTERN = sequence(REG, UINT8)

    def handle(self, analysis: HermesAnalysis, entry: OpcodeEntry) -> OpcodeResult:
        match = self._PATTERN.match(entry.args.strip())
        if not match:
            return self.build_invalid_args_result(analysis, entry, "Expected Reg8, UInt8 arguments")

        dest_reg, _size = map(int, match.groups())

        expression = Identifier(name="__environment__")

        result = OpcodeResult(entry, value=expression, dest_reg=dest_reg)
        analysis.add_result(result)

        return result
