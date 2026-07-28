from hermes_decompiler.handlers import OpcodeHandler, REG, UINT16, sequence
from hermes_decompiler.ir.Operators import BinaryOperator, UnaryOperator
from hermes_decompiler.ir.expressions import BinaryExpression, StringLiteral, UnaryExpression
from hermes_decompiler.opcode import OpcodeEntry, OpcodeResult
from hermes_decompiler.runtime import HermesAnalysis


# DEFINE_OPCODE_3(TypeOfIs, Reg8, Reg8, UInt16)
#   [confirmed, facebook/hermes BytecodeList.def, tag hermes-v260318099.0.1]
#
#   "Arg1 = typeof Arg2 is in Arg3 (TypeOfIsTypes, see Typeof.h)"
#
# CORRECTION vs. earlier draft: this is a COMPLETE REWRITE. The
# previous version guessed a single UInt8 "type_tag" operand mapping to
# exactly one typeof-result string (`typeof x === "sometype"`). The
# real opcode takes a UInt16 *bitmask* ("TypeOfIsTypes", defined in
# Hermes's Typeof.h, which is NOT available to check from here) and
# tests whether `typeof Arg2` is any one of potentially SEVERAL types
# encoded in that mask -- i.e. this can represent `typeof x === "a" ||
# typeof x === "b" || ...` fused into one instruction, not just a
# single equality check.
#
# Since Typeof.h's actual bit-to-typeof-string mapping isn't available
# in this session, the bitmask can't be decoded into the right set of
# type-name strings here. Two honest options:
#   (a) render a placeholder that preserves the raw mask for the reader
#       to cross-reference, or
#   (b) if the mask has exactly one bit set, render the single-type
#       check other engines do (best-effort, common case).
# This handler does (b) with a documented, EXPLICITLY GUESSED bit
# ordering (see _TYPE_BITS below -- not sourced from Typeof.h, just a
# plausible guess at typeof-result ordering) as a best-effort single-
# type case, and falls back to (a) -- a literal mask placeholder -- for
# anything with zero or multiple bits set, rather than silently
# guessing which OR-combination was intended.
#
# VERIFY the actual bit assignments against
# include/hermes/VM/Typeof.h (or wherever TypeOfIsTypes is defined) in
# your Hermes source tree before trusting the single-bit case below.
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
