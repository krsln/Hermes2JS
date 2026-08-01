from hermes_decompiler.handlers import OpcodeHandler, REG, UINT8, UINT32, sequence
from hermes_decompiler.ir.Operators import AssignmentOperator
from hermes_decompiler.ir.expressions import AssignmentExpression, Identifier, MemberExpression
from hermes_decompiler.opcode import OpcodeEntry, OpcodeResult
from hermes_decompiler.runtime import HermesAnalysis


# Reg8, Reg8, UInt8 (total size 3)
# DEFINE_OPCODE_3(PutOwnBySlotIdx, Reg8, Reg8, UInt8)
# Example: <PutOwnBySlotIdx>: <Reg8: 3, Reg8: 4, UInt8: 0>
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
            receiver=self.get_register_expression(analysis, obj_reg),
            member=Identifier(name=property_name),
            computed=False,
        )
        right = self.get_register_expression(analysis, value_reg)

        expression = AssignmentExpression(left=left, operator=AssignmentOperator.ASSIGN, right=right)

        result = OpcodeResult(entry, value=expression, dest_reg=None)
        analysis.add_result(result)

        return result


# Reg8, Reg8, UInt32 (total size 6)
# DEFINE_OPCODE_3(PutOwnBySlotIdxLong, Reg8, Reg8, UInt32)
# Example:
class PutOwnBySlotIdxLong(PutOwnBySlotIdx):
    """Set an existing own property identified at a slot index."""

    _PATTERN = sequence(REG, REG, UINT32)
