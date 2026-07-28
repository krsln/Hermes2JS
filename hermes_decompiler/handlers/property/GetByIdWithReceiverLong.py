from hermes_decompiler.handlers import OpcodeHandler, REG, UINT8, UINT32, sequence
from hermes_decompiler.ir.expressions import CallExpression, Identifier, MemberExpression, StringLiteral
from hermes_decompiler.opcode import OpcodeEntry, OpcodeResult
from hermes_decompiler.runtime import HermesAnalysis


# DEFINE_OPCODE_5(GetByIdWithReceiverLong, Reg8, Reg8, UInt8, Reg8, UInt32)
#   [confirmed, hermes-dec table -- bytecode version 98]
#
#   "Get an object property by string table index, with a specified
#    receiver. Arg1 = Arg2[stringtable[Arg5]].
#    Arg1 is the destination.
#    Arg2 is the object to begin the property look up.
#    Arg3 is a cache index used to speed up the above operation.
#    Arg4 is receiver.
#    Arg5 is the string id."
#
# CORRECTION vs. earlier draft: operand order was guessed as
# (dest, obj, receiver, cache, string_id) -- WRONG. Real order is
# (dest, obj, cache, receiver, string_id), i.e. the receiver register
# comes *after* the cache index, not right after the object. Fixed
# below.
#
# Semantically: distinguishes the object a property lookup *starts*
# traversing the prototype chain from (Arg2, the lookup target) from
# the object `this` is bound to during a getter call (Arg4, the
# receiver) -- used for `super.prop` access, where lookup starts at the
# home object's prototype but `this` inside the getter must remain the
# original receiver. There's no plain member-access JS syntax for that
# distinction, so it's rendered via Reflect.get's 3-arg form:
# Reflect.get(obj, "prop", receiver).
class GetByIdWithReceiverLong(OpcodeHandler):
    """obj[prop] lookup with an explicit receiver, e.g. super.prop / Reflect.get semantics."""

    _PATTERN = sequence(REG, REG, UINT8, REG, UINT32)

    def handle(self, analysis: HermesAnalysis, entry: OpcodeEntry) -> OpcodeResult:
        match = self._PATTERN.match(entry.args.strip())
        if not match:
            return self.build_invalid_args_result(
                analysis, entry, "Expected Reg8, Reg8, UInt8, Reg8, string_id arguments"
            )

        dest_reg, obj_reg, _cache, receiver_reg, string_id = map(int, match.groups())

        prop_name = entry.identifier_name or f"string_{string_id}"
        obj = self.get_register_value(analysis, obj_reg)
        receiver = self.get_register_value(analysis, receiver_reg)

        callee = MemberExpression(
            receiver=Identifier(name="Reflect"),
            member=Identifier(name="get"),
            computed=False,
        )

        expression = CallExpression(
            callee=callee,
            arguments=(obj, StringLiteral(value=prop_name), receiver),
        )

        result = OpcodeResult(entry, value=expression, dest_reg=dest_reg)
        analysis.add_result(result)

        return result
