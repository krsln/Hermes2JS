from hermes_decompiler.handlers import OpcodeHandler, REG, UINT8, sequence
from hermes_decompiler.ir.Operators import BinaryOperator, UnaryOperator
from hermes_decompiler.ir.expressions import BinaryExpression, StringLiteral, UnaryExpression
from hermes_decompiler.opcode import OpcodeEntry, OpcodeResult
from hermes_decompiler.runtime import HermesAnalysis


# TypeOfIs -- ***SIGNATURE NOT CONFIRMED***
#
# Unlike every other opcode added so far, TypeOfIs could NOT be located
# in either source consulted:
#   - facebook/hermes main branch BytecodeList.def (grepped directly,
#     zero matches)
#   - the hermes-dec opcode table (searched multiple times, including
#     targeted queries; not found in the portions of the table that
#     were reachable)
#
# This means it's very likely specific to whatever fork/newer bytecode
# version your toolchain targets.
#
# The implementation below is a best-effort guess based on how other
# JS engines implement this exact optimization (e.g. V8's TestTypeOf):
# a fused `typeof x === "sometype"` check that avoids materializing the
# intermediate string, encoding which type to test for as a bitmask/
# immediate operand rather than a separate string comparison. Guessed
# shape: Reg8 dest, Reg8 value, UInt8 type_tag (index into a fixed set
# of JS type-tag strings, e.g. undefined/object/boolean/number/string/
# symbol/function/bigint).
#
# DO NOT TRUST THIS until you've checked it against:
#   1. Your actual BytecodeList.def / disassembler output for the
#      real operand count and widths.
#   2. What the type_tag values decode to (the TYPE_TAGS mapping below
#      is a guess at ES spec typeof-result ordering, not verified
#      against any Hermes source).
#
# FIX vs. earlier draft: UnaryExpression's real fields (per
# ir/expressions/Operations.py) are `operator: UnaryOperator, operand:
# Expression` -- there is no `argument`/`prefix` field (that shape
# belongs to UpdateExpression, e.g. `i++`/`--i`, not to unary ops like
# `typeof`/`!`/`-`). `operator` also has to be an actual `UnaryOperator`
# enum member, not the bare string "typeof".
#
# NOTE: `UnaryOperator.TYPEOF` is assumed to exist on that enum by
# analogy with JS's unary operator set (typeof/void/delete/-/+/!/~) --
# verify the exact member name in hermes_decompiler.ir.Operators.
class TypeOfIs(OpcodeHandler):
    """
    Arg1 = (typeof Arg2 === <type identified by Arg3>)

    UNVERIFIED opcode -- see module-level comment. Treat type_tag
    decoding and even the operand count/widths as provisional.
    """

    _PATTERN = sequence(REG, REG, UINT8)

    # Guessed mapping from an immediate tag to the typeof() result
    # string it represents. Order/values NOT confirmed against Hermes
    # source -- placeholder based on common typeof-result enumeration.
    _TYPE_TAGS = {
        0: "undefined",
        1: "object",
        2: "boolean",
        3: "number",
        4: "string",
        5: "symbol",
        6: "function",
        7: "bigint",
    }

    def handle(self, analysis: HermesAnalysis, entry: OpcodeEntry) -> OpcodeResult:
        match = self._PATTERN.match(entry.args.strip())
        if not match:
            return self.build_invalid_args_result(analysis, entry, "Expected Reg8, Reg8, UInt8 arguments")

        dest_reg, value_reg, type_tag = map(int, match.groups())

        operand = self.get_register_value(analysis, value_reg)
        type_of_expr = UnaryExpression(operator=UnaryOperator.TYPEOF, operand=operand)

        type_name = self._TYPE_TAGS.get(type_tag)
        if type_name is None:
            # Unknown tag value -- don't guess further, surface it
            # plainly so it's obvious in the decompiled output rather
            # than silently producing a wrong comparison.
            right = StringLiteral(value=f"<unknown_type_tag_{type_tag}>")
        else:
            right = StringLiteral(value=type_name)

        expression = BinaryExpression(
            left=type_of_expr,
            operator=BinaryOperator.STRICT_EQUAL,
            right=right,
        )

        result = OpcodeResult(entry, value=expression, dest_reg=dest_reg)
        analysis.add_result(result)

        return result
