from hermes_decompiler.frontend.opcode import OpcodeEntry, OpcodeResult
from hermes_decompiler.handlers import sequence, REG, STRING_ID
from hermes_decompiler.handlers.OpcodeHandler import OpcodeHandler
from hermes_decompiler.ir.expressions import CallExpression, Identifier, StringLiteral
from hermes_decompiler.runtime import HermesAnalysis


# Reg8, UInt32 (string_id) (total size 5)
# DEFINE_OPCODE_2(CreatePrivateName, Reg8, UInt32)
# Example: <CreatePrivateName>: <Reg8: 4, string_id: 11468>  # String: '#code' (Identifier)
class CreatePrivateName(OpcodeHandler):
    """Create a private-name symbol: Symbol('#fieldName')."""

    _PATTERN = sequence(REG, STRING_ID)

    def handle(self, analysis: HermesAnalysis, entry: OpcodeEntry) -> OpcodeResult:
        match = self._PATTERN.match(entry.args.strip())
        if not match:
            return self.build_invalid_args_result(analysis, entry, "Expected Reg8, string_id arguments")

        dest_reg, string_id = map(int, match.groups())

        name = entry.identifier_name or f"string_{string_id}"

        expression = CallExpression(
            callee=Identifier(name="Symbol"),
            arguments=(StringLiteral(value=name),),
        )

        result = OpcodeResult(entry, value=expression, dest_reg=dest_reg)
        analysis.add_result(result)

        return result
