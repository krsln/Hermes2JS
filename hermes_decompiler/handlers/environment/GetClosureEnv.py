from hermes_decompiler.handlers import OpcodeHandler, REG, sequence
from hermes_decompiler.ir.expressions import CallExpression, Identifier
from hermes_decompiler.opcode import OpcodeEntry, OpcodeResult
from hermes_decompiler.runtime import HermesAnalysis


# DEFINE_OPCODE_2(GetClosureEnvironment, Reg8, Reg8)
#   [confirmed, hermes-dec table -- bytecode versions 97/98/99]
#
#   "Get the environment from a closure.
#    Arg1 is the destination.
#    Arg2 is the closure from which to read."
#
# Confirms the earlier guess (Reg8 dest, Reg8 closure) was correct.
# Distinguishing detail vs. the confirmed GetParentEnvironment (Reg8
# dest, UInt8 levels -- walks up N levels from the *currently
# executing* function's own environment): this one takes an explicit
# closure register as input, i.e. "get the environment captured by
# THIS OTHER closure value" rather than the current function's own.
#
# Same "no JS-visible expression" treatment as the other environment
# opcodes -- rendered as a named pseudo-call for traceability.
class GetClosureEnvironment(OpcodeHandler):
    """Fetch the environment/scope captured by an explicit closure register."""

    _PATTERN = sequence(REG, REG)

    def handle(self, analysis: HermesAnalysis, entry: OpcodeEntry) -> OpcodeResult:
        match = self._PATTERN.match(entry.args.strip())
        if not match:
            return self.build_invalid_args_result(analysis, entry, "Expected Reg8, Reg8 arguments")

        dest_reg, closure_reg = map(int, match.groups())

        closure = self.get_register_value(analysis, closure_reg)

        expression = CallExpression(
            callee=Identifier(name="__getClosureEnvironment__"),
            arguments=(closure,),
        )

        result = OpcodeResult(entry, value=expression, dest_reg=dest_reg)
        analysis.add_result(result)

        return result
