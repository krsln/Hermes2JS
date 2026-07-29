from hermes_decompiler.handlers import OpcodeHandler, REG, UINT8, sequence
from hermes_decompiler.ir.expressions import CallExpression, Identifier, NumericLiteral
from hermes_decompiler.opcode import OpcodeEntry, OpcodeResult
from hermes_decompiler.runtime import HermesAnalysis


# Reg8, UInt8 (total size 2)
# DEFINE_OPCODE_2(GetParentEnvironment, Reg8, UInt8)
# Example: <GetParentEnvironment>: <Reg8: 2, UInt8: 0>
class GetParentEnvironment(OpcodeHandler):
    """Fetch an environment N levels up the *enclosing* scope chain."""

    _PATTERN = sequence(REG, UINT8)

    def handle(self, analysis: HermesAnalysis, entry: OpcodeEntry) -> OpcodeResult:
        match = self._PATTERN.match(entry.args.strip())
        if not match:
            return self.build_invalid_args_result(analysis, entry, "Expected Reg8, UInt8 arguments")

        dest_reg, levels = map(int, match.groups())

        expression = CallExpression(
            callee=Identifier(name="getParentEnvironment"),
            arguments=(NumericLiteral(value=levels),),
        )

        result = OpcodeResult(entry, value=expression, dest_reg=dest_reg)
        analysis.add_result(result)

        return result
