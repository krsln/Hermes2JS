from hermes_decompiler.frontend.opcode import OpcodeEntry, OpcodeResult
from hermes_decompiler.handlers import OpcodeHandler, sequence, REG
from hermes_decompiler.ir.expressions import CallExpression, Identifier
from hermes_decompiler.runtime import HermesAnalysis


# Reg8, Reg8 (total size 2)
# DEFINE_OPCODE_2(<GetClosureEnvironment, Reg8>, Reg8)
# Example: <GetClosureEnvironment>: <Reg8: 3, Reg8: 2>
class GetClosureEnvironment(OpcodeHandler):
    """Fetch the environment/scope captured by an explicit closure register."""

    _PATTERN = sequence(REG, REG)

    def handle(self, analysis: HermesAnalysis, entry: OpcodeEntry) -> OpcodeResult:
        match = self._PATTERN.match(entry.args.strip())
        if not match:
            return self.build_invalid_args_result(analysis, entry, "Expected Reg8, Reg8 arguments")

        dest_reg, closure_reg = map(int, match.groups())

        closure = self.get_register_expression(analysis, closure_reg)

        expression = CallExpression(
            callee=Identifier(name="__getClosureEnvironment__"),
            arguments=(closure,),
        )

        result = OpcodeResult(entry, value=expression, dest_reg=dest_reg)
        analysis.add_result(result)

        return result
