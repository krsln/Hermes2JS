from hermes_decompiler.handlers import OpcodeHandler, REG, UINT8, sequence
from hermes_decompiler.ir.Operators import AssignmentOperator
from hermes_decompiler.ir.expressions import AssignmentExpression, Identifier, MemberExpression
from hermes_decompiler.opcode import OpcodeEntry, OpcodeResult
from hermes_decompiler.runtime import HermesAnalysis


# DEFINE_OPCODE_3(PutOwnBySlotIdx, Reg8, Reg8, UInt8)
# DEFINE_OPCODE_3(PutOwnBySlotIdxLong, Reg8, Reg8, UInt32)
#
# NOT present in the checked BytecodeList.def; inferred by symmetry
# with GetOwnBySlotIdx, which IS confirmed in the hermes-dec table:
#
#   GetOwnBySlotIdx: Reg8, Reg8, UInt8
#   "Get an existing own property at a given slot index.
#    Arg1 is the result register. Arg2 is the object.
#    Arg3 is the hidden class slot index."
#
# PutOwnBySlotIdx is the mirror-image write: instead of addressing the
# property by string ID (as PutById does), it addresses it directly by
# its position ("slot") in the object's hidden class -- an internal
# Hermes optimization for properties whose shape is already known at
# compile time. There's no separate JS syntax for "write by slot" vs.
# "write by name": both compile down to the same `obj.prop = value`
# (or `obj[prop] = value` if the property name isn't statically known
# from context/debug info). Since no property *name* is available
# without a shape/hidden-class table lookup that this decompiler layer
# doesn't have access to, we fall back to a synthetic slot_N
# placeholder name, similar to how string_N is used elsewhere when a
# string_id can't be resolved to an identifier_name.
class PutOwnBySlotIdx(OpcodeHandler):
    """Write an own property by hidden-class slot index: obj.slot_N = value."""

    _PATTERN = sequence(REG, REG, UINT8)

    def handle(self, analysis: HermesAnalysis, entry: OpcodeEntry) -> OpcodeResult:
        match = self._PATTERN.match(entry.args.strip())
        if not match:
            return self.build_invalid_args_result(analysis, entry, "Expected Reg8, Reg8, UInt8 arguments")

        obj_reg, value_reg, slot_idx = map(int, match.groups())

        property_name = entry.identifier_name or f"slot_{slot_idx}"

        left = MemberExpression(
            receiver=self.get_register_value(analysis, obj_reg),
            member=Identifier(name=property_name),
            computed=False,
        )
        right = self.get_register_value(analysis, value_reg)

        expression = AssignmentExpression(left=left, operator=AssignmentOperator.ASSIGN, right=right)

        result = OpcodeResult(entry, value=expression, dest_reg=None)
        analysis.add_result(result)

        return result


class PutOwnBySlotIdxLong(PutOwnBySlotIdx):
    pass
