from hermes_decompiler.frontend.opcode import OpcodeResult
from hermes_decompiler.handlers import OpcodeHandler, OpcodeContext, ArgsPattern, sequence, REG, UINT8, UINT32
from hermes_decompiler.ir.Operators import AssignmentOperator
from hermes_decompiler.ir.expressions import AssignmentExpression, Identifier, MemberExpression


# Reg8, Reg8, UInt8 (total size 3)
# DEFINE_OPCODE_3(PutOwnBySlotIdx, Reg8, Reg8, UInt8)
# Example: <PutOwnBySlotIdx>: <Reg8: 3, Reg8: 4, UInt8: 0>
class PutOwnBySlotIdx(OpcodeHandler):
    """Write an own property by hidden-class slot index: obj.slot_N = value."""

    ARGUMENTS = ArgsPattern(sequence(REG, REG, UINT8), "Reg8, Reg8, UInt8 (total size 3)")

    def handle(self, ctx: OpcodeContext) -> OpcodeResult:
        match = self.match_arguments(ctx)
        if isinstance(match, OpcodeResult):
            return match

        obj_reg, value_reg, slot_idx = map(int, match.groups())

        property_name = ctx.entry.identifier_name or f"slot_{slot_idx}"

        left = MemberExpression(
            receiver=self.get_register_expression(ctx.analysis, obj_reg),
            member=Identifier(name=property_name),
            computed=False,
        )
        right = self.get_register_expression(ctx.analysis, value_reg)

        expression = AssignmentExpression(left=left, operator=AssignmentOperator.ASSIGN, right=right)

        result = OpcodeResult(ctx.entry, value=expression, dest_reg=None)
        ctx.analysis.add_result(result)

        return result


# Reg8, Reg8, UInt32 (total size 6)
# DEFINE_OPCODE_3(PutOwnBySlotIdxLong, Reg8, Reg8, UInt32)
# Example:
class PutOwnBySlotIdxLong(PutOwnBySlotIdx):
    """Set an existing own property identified at a slot index."""

    ARGUMENTS = ArgsPattern(sequence(REG, REG, UINT32), "Reg8, Reg8, UInt32 (total size 6)")
