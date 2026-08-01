from hermes_decompiler.handlers import REG, STRING_ID, sequence
from hermes_decompiler.ir.Operators import AssignmentOperator
from hermes_decompiler.ir.expressions import AssignmentExpression, Identifier, MemberExpression, ObjectExpression, \
    ObjectProperty, PropertyKind
from hermes_decompiler.opcode import OpcodeEntry, OpcodeResult
from hermes_decompiler.runtime import HermesAnalysis
from .PutById import PutById


class PutNewOwnByIdX(PutById):
    """Base class for PutNewOwnById* variants."""

    _PATTERN = sequence(REG, REG, STRING_ID)

    def handle(self, analysis: HermesAnalysis, entry: OpcodeEntry) -> OpcodeResult:
        match = self._PATTERN.match(entry.args.strip())
        if not match:
            return self.build_invalid_args_result(analysis, entry)

        obj_reg, value_reg, string_id = map(int, match.groups())

        property_name = entry.identifier_name or f"string_{string_id}"

        obj_value = self.get_register_expression(analysis, obj_reg)
        right = self.get_register_expression(analysis, value_reg)

        # Special Case
        if isinstance(obj_value, ObjectExpression):
            new_prop = ObjectProperty(
                key=Identifier(name=property_name), value=right, kind=PropertyKind.INIT,
                computed=False, method=False, shorthand=False
            )

            updated_obj = ObjectExpression(properties=obj_value.properties + (new_prop,))

            result = OpcodeResult(entry, value=updated_obj, dest_reg=obj_reg)
            analysis.add_result(result)

            return result

        # Normal Case
        left = MemberExpression(receiver=obj_value, member=Identifier(name=property_name), computed=False)
        expression = AssignmentExpression(left=left, operator=AssignmentOperator.ASSIGN, right=right)

        result = OpcodeResult(entry, value=expression, dest_reg=None)
        analysis.add_result(result)

        return result


# Reg8, Reg8, UInt8 (string_id) (total size 3)
# DEFINE_OPCODE_3(PutNewOwnByIdShort, Reg8, Reg8, UInt8)
# Example: <PutNewOwnByIdShort>: <Reg8: 1, Reg8: 0, string_id: 249>  # String: 'value' (Identifier)
class PutNewOwnByIdShort(PutNewOwnByIdX):
    """Set an existing own property identified at a slot index."""
    pass


# Reg8, Reg8, UInt16 (string_id) (total size 4)
# DEFINE_OPCODE_3(PutNewOwnById, Reg8, Reg8, UInt16)
# Example: <PutNewOwnById>: <Reg8: 15, Reg8: 2, string_id: 19648>  # String: 'silentJSONParsing' (Identifier)
class PutNewOwnById(PutNewOwnByIdX):
    """Set an existing own property identified at a slot index."""
    pass


# Reg8, Reg8, UInt32 (string_id) (total size 6)
# DEFINE_OPCODE_3(PutNewOwnByIdLong, Reg8, Reg8, UInt32)
# Example:
class PutNewOwnByIdLong(PutNewOwnByIdX):
    """Set an existing own property identified at a slot index."""
    pass
