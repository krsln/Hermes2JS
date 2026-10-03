from hermes_decompiler.frontend.handlers import OpcodeHandler, OpcodeContext, ArgsPattern, sequence, REG, UINT8, UINT32
from hermes_decompiler.frontend.handlers.shared import fold_slot_value, property_access, slot_key
from hermes_decompiler.frontend.opcode import OpcodeResult
from hermes_decompiler.ir.Operators import AssignmentOperator
from hermes_decompiler.ir.expressions import AssignmentExpression


# Reg8, Reg8, UInt8 (total size 3)
# DEFINE_OPCODE_3(PutOwnBySlotIdx, Reg8, Reg8, UInt8)
# Example: <PutOwnBySlotIdx>: <Reg8: 3, Reg8: 4, UInt8: 0>
class PutOwnBySlotIdx(OpcodeHandler):
    """Write an own property by hidden-class slot index: `obj.<key at slot N> = value`."""

    ARGUMENTS = ArgsPattern(sequence(REG, REG, UINT8), "Reg8, Reg8, UInt8 (total size 3)")

    def handle(self, ctx: OpcodeContext) -> OpcodeResult:
        match = self.match_arguments(ctx)
        if isinstance(match, OpcodeResult):
            return match

        obj_reg, value_reg, slot_idx = map(int, match.groups())

        # Resolve the value first (see `fold_into_literal`).
        right = self.get_register_expression(ctx.analysis, value_reg)

        # The opcode carries only a hidden-class slot index; the property
        # NAME is the slot's key in the object literal being built (see
        # `slot_key`). The compiler leaves a `null` placeholder for it in the
        # `NewObjectWithBuffer` literal, so filling the placeholder folds the
        # store into the literal: `{ "start": null }` -> `{ "start": start }`.
        folded = fold_slot_value(ctx, obj_reg, slot_idx, right)

        if folded is not None:
            return folded

        # Not foldable: a statement `obj.<name> = value`, with the real name
        # whenever the slot resolves (`slot_N` only as a last resort).
        property_name = ctx.entry.identifier_name or slot_key(ctx, obj_reg, slot_idx) or f"slot_{slot_idx}"

        left = property_access(self.get_register_expression(ctx.analysis, obj_reg), property_name)
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
