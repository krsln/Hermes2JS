from hermes_decompiler.handlers import OpcodeHandler, REG, UINT16, sequence
from hermes_decompiler.ir.Operators import BinaryOperator, UnaryOperator
from hermes_decompiler.ir.expressions import BinaryExpression, StringLiteral, UnaryExpression
from hermes_decompiler.opcode import OpcodeEntry, OpcodeResult
from hermes_decompiler.runtime import HermesAnalysis


# Reg8, Reg8, UInt16 (total size 4)
# DEFINE_OPCODE_3(TypeOfIs, Reg8, Reg8, UInt16)
# Example: <TypeOfIs>: <Reg8: 1, Reg8: 4, UInt16: 258>
class TypeOfIs(OpcodeHandler):
    """
    Arg1 = typeof Arg2 is one of the types encoded in the Arg3 bitmask.

    Bit-to-type mapping is GUESSED (Typeof.h not available to verify)
    -- only the single-bit case is decoded to a plain `typeof x ===
    "type"` check; multi-bit masks fall back to a raw placeholder.
    """

    _PATTERN = sequence(REG, REG, UINT16)

    # GUESSED bit assignments -- NOT sourced from Typeof.h. Placeholder
    # ordering based on common typeof-result enumeration; each bit
    # assumed to represent one typeof() result string.
    _TYPE_BITS = {
        1 << 0: "undefined",
        1 << 1: "object",
        1 << 2: "boolean",
        1 << 3: "number",
        1 << 4: "string",
        1 << 5: "symbol",
        1 << 6: "function",
        1 << 7: "bigint",
    }

    def handle(self, analysis: HermesAnalysis, entry: OpcodeEntry) -> OpcodeResult:
        match = self._PATTERN.match(entry.args.strip())
        if not match:
            return self.build_invalid_args_result(analysis, entry, "Expected Reg8, Reg8, UInt16 arguments")

        dest_reg, value_reg, type_mask = map(int, match.groups())

        operand = self.get_register_value(analysis, value_reg)
        type_of_expr = UnaryExpression(operator=UnaryOperator.TYPEOF, operand=operand)

        type_name = self._TYPE_BITS.get(type_mask)

        if type_name is not None:
            # Exactly one recognized bit set -- render as a plain
            # single-type check.
            expression = BinaryExpression(
                left=type_of_expr,
                operator=BinaryOperator.STRICT_EQUAL,
                right=StringLiteral(value=type_name),
            )
        else:
            # Zero, multiple, or unrecognized bits -- don't guess an OR
            # chain without knowing the real bit->type mapping. Surface
            # the raw mask plainly instead of producing a plausible-
            # looking but potentially wrong boolean expression.
            expression = BinaryExpression(
                left=type_of_expr,
                operator=BinaryOperator.STRICT_EQUAL,
                right=StringLiteral(value=f"<unresolved_typeof_mask_0x{type_mask:04x}>"),
            )

        result = OpcodeResult(entry, value=expression, dest_reg=dest_reg)
        analysis.add_result(result)

        return result
