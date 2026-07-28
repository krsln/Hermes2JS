from hermes_decompiler.handlers import OpcodeHandler, REG, UINT8, UINT32, sequence
from hermes_decompiler.ir.expressions import CallExpression, Identifier
from hermes_decompiler.opcode import OpcodeEntry, OpcodeResult
from hermes_decompiler.runtime import HermesAnalysis


# DEFINE_OPCODE_4(CacheNewObject, Reg8, Reg8, UInt32, UInt8)
#   [confirmed, hermes-dec table -- bytecode version 98]
#
#   "Perform a lookup on the new object cache.
#    Arg1 = the 'this' value to lookup.
#    Arg2 = the new target to determine whether it is a constructor call.
#    Arg3 = the index in the shape table.
#    Arg4 = the cache index within the current function."
#
# CORRECTION vs. earlier draft: the previous version of this handler
# was written before this opcode could be located anywhere and guessed
# a single Reg8 operand with no destination. The real signature is
# Reg8, Reg8, UInt32, UInt8 -- four operands, not one -- and BOTH
# Reg8 operands (Arg1 `this`, Arg2 new.target) are *inputs* being
# looked up in the cache, not a destination being written. There is no
# separate output register at all: this is a pure inline-cache
# hint/lookup for the object-shape machinery (paired with
# CreateThisForNew/CreateThisForSuper's "cache index" operands), not a
# value-producing instruction.
#
# No JS-visible effect -- rendered as an inert pseudo-call for
# traceability, same convention as ThrowIfThisInitialized/
# GetParentEnvironment for other opaque VM-internal opcodes.
class CacheNewObject(OpcodeHandler):
    """Runtime hint: look up/cache the hidden-class shape for a `this`/new.target pair. No JS-visible effect."""

    _PATTERN = sequence(REG, REG, UINT32, UINT8)

    def handle(self, analysis: HermesAnalysis, entry: OpcodeEntry) -> OpcodeResult:
        match = self._PATTERN.match(entry.args.strip())
        if not match:
            return self.build_invalid_args_result(
                analysis, entry, "Expected Reg8, Reg8, UInt32, UInt8 arguments"
            )

        this_reg, new_target_reg, _shape_idx, _cache_idx = map(int, match.groups())

        this_value = self.get_register_value(analysis, this_reg)
        new_target = self.get_register_value(analysis, new_target_reg)

        expression = CallExpression(
            callee=Identifier(name="__cacheNewObject__"),
            arguments=(this_value, new_target),
        )

        # No destination register -- this opcode doesn't produce a value.
        result = OpcodeResult(entry, value=expression, dest_reg=None)
        analysis.add_result(result)

        return result
