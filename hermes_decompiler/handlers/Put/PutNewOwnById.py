from hermes_decompiler.handlers._shared_patterns import (
    REG,
    STRING_ID,
    sequence,
)
from hermes_decompiler.ir import AssignmentExpression, Identifier, MemberExpression, ObjectExpression, ObjectProperty
from hermes_decompiler.ir.Operators import AssignmentOperator
from hermes_decompiler.ir.expressions.Collections import PropertyKind
from hermes_decompiler.models.HermesAnalysis import HermesAnalysis
from hermes_decompiler.models.OpcodeEntry import OpcodeEntry
from hermes_decompiler.models.OpcodeResult import OpcodeResult
from .PutById import PutById

PUT_NEW_OWN_PATTERN = sequence(REG, REG, STRING_ID)


class PutNewOwnByIdX(PutById):
    """Base class for PutNewOwnById* variants."""

    def handle(self, analysis: HermesAnalysis, entry: OpcodeEntry) -> OpcodeResult:
        match = PUT_NEW_OWN_PATTERN.match(entry.args.strip())
        if not match:
            return self.build_invalid_args_result(analysis, entry)

        obj_reg, value_reg, string_id = map(int, match.groups())

        property_name = entry.identifier_name or f"string_{string_id}"

        obj_value = self.get_register_value(analysis, obj_reg)
        right = self.get_register_value(analysis, value_reg)

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


class PutNewOwnByIdShort(PutNewOwnByIdX):
    pass


class PutNewOwnById(PutNewOwnByIdX):
    pass


class PutNewOwnByIdLong(PutNewOwnByIdX):
    pass
