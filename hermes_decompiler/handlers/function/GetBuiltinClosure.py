from hermes_decompiler.handlers import OpcodeHandler, REG, UINT8, sequence
from hermes_decompiler.ir.expressions import Identifier
from hermes_decompiler.opcode import OpcodeEntry, OpcodeResult
from hermes_decompiler.runtime import HermesAnalysis


# DEFINE_OPCODE_2(GetBuiltinClosure, Reg8, UInt8)   [confirmed, facebook/hermes main BytecodeList.def]
#
#   "Get a closure from a builtin function.
#    Arg1 is the destination of the return value.
#    Arg2 is the builtin number."
#
# The "builtin number" (Arg2) is an index into Hermes's internal
# builtins table (see lib/VM/Builtins.def upstream) -- e.g. entries for
# Array.prototype.push, Object.keys, Math.max, etc. This decompiler
# doesn't have that table available here, so the builtin name can't be
# resolved to something like `Array.prototype.push` without it; falls
# back to an indexed placeholder identifier, matching the `string_N`/
# `slot_N` convention already used elsewhere in this codebase when a
# table lookup isn't available at this layer.
#
# TODO: if HermesAnalysis/OpcodeEntry exposes a builtins table (the
# same way it exposes `identifier_name` for string IDs), resolve
# `builtin_number` through that instead of the placeholder name.
class GetBuiltinClosure(OpcodeHandler):
    """Fetch a closure reference to one of Hermes's internal builtin functions."""

    _PATTERN = sequence(REG, UINT8)

    def handle(self, analysis: HermesAnalysis, entry: OpcodeEntry) -> OpcodeResult:
        match = self._PATTERN.match(entry.args.strip())
        if not match:
            return self.build_invalid_args_result(analysis, entry, "Expected Reg8, UInt8 arguments")

        dest_reg, builtin_number = map(int, match.groups())

        builtin_name = getattr(entry, "builtin_name", None) or f"builtin_{builtin_number}"

        expression = Identifier(name=builtin_name)

        result = OpcodeResult(entry, value=expression, dest_reg=dest_reg)
        analysis.add_result(result)

        return result
