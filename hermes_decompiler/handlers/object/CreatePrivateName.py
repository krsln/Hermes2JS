from hermes_decompiler.handlers import OpcodeHandler, REG, UINT8, STRING_ID, sequence
from hermes_decompiler.ir.expressions import CallExpression, Identifier, NewExpression, Literal, StringLiteral
from hermes_decompiler.opcode import OpcodeEntry, OpcodeResult
from hermes_decompiler.runtime import HermesAnalysis


# DEFINE_OPCODE_2(CreatePrivateName, Reg8, UInt32 string_id)   [confirmed, hermes-dec table]
#
#   "Create a new primitive symbol, taking in a string description as
#    input... Arg1 = new Symbol(Arg2)"
#
# Backs `#privateField` class members. Rendered as `Symbol(name)` (no
# `new`, matching real JS Symbol() semantics -- the doc's "new Symbol"
# phrasing is describing bytecode intent, not actual constructible JS).
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
