from hermes_decompiler.handlers import OpcodeHandler, REG, sequence
from hermes_decompiler.opcode import OpcodeEntry, OpcodeResult
from hermes_decompiler.runtime import HermesAnalysis


# ToPropertyKey, Reg8, Reg8
#
# NOT found in either source consulted; not in the checked
# BytecodeList.def, and the hermes-dec table lookup was truncated
# before reaching the "T" opcodes, so this signature is inferred purely
# from ES spec naming convention (ECMA-262 ToPropertyKey abstract
# operation) and Hermes's existing Reg8,Reg8 unary-conversion pattern
# (compare ToNumber, ToNumeric, ToInt32 above). Recommend verifying
# against your BytecodeList.def / disassembler output before relying on
# this in production -- specifically confirm operand count and whether
# there's a UInt8 cache operand like other property-access opcodes.
#
# Semantically: Arg1 = ToPropertyKey(Arg2), i.e. converts a value to a
# valid property key (string or symbol) per ES2015+ semantics, used
# ahead of computed member expressions/class private fields where the
# key type isn't statically known.
class ToPropertyKey(OpcodeHandler):
    """Arg1 = ToPropertyKey(Arg2) -- coerce a value to a valid property key."""

    _PATTERN = sequence(REG, REG)

    def handle(self, analysis: HermesAnalysis, entry: OpcodeEntry) -> OpcodeResult:
        match = self._PATTERN.match(entry.args.strip())
        if not match:
            return self.build_invalid_args_result(analysis, entry, "Expected Reg8, Reg8 arguments")

        dest_reg, value_reg = map(int, match.groups())

        # No-op passthrough at the JS-source level: `obj[key]` already
        # implies ToPropertyKey coercion, so there's nothing additional
        # to render -- just forward the source value to the destination.
        value = self.get_register_value(analysis, value_reg)

        result = OpcodeResult(entry, value=value, dest_reg=dest_reg)
        analysis.add_result(result)

        return result
