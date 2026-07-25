from hermes_decompiler.ir import AssignmentExpression, Identifier, MemberExpression
from hermes_decompiler.ir.Operators import AssignmentOperator

from hermes_decompiler.models.HermesAnalysis import HermesAnalysis
from hermes_decompiler.models.JSVariable import JSVariable
from hermes_decompiler.models.OpcodeEntry import OpcodeEntry
from hermes_decompiler.models.OpcodeResult import OpcodeResult

from hermes_decompiler.handlers._shared_patterns import (
    REG,
    STRING_ID,
    sequence,
)

from .PutById import PutById

PUT_NEW_OWN_PATTERN = sequence(REG, REG, STRING_ID)


class PutNewOwnByIdX(PutById):
    """Base class for PutNewOwnById* variants."""

    def handle(
        self,
        analysis: HermesAnalysis,
        entry: OpcodeEntry,
    ) -> OpcodeResult:

        match = PUT_NEW_OWN_PATTERN.match(entry.args.strip())
        if not match:
            return self.build_invalid_args_result(analysis, entry)

        obj_reg, value_reg, string_id = map(int, match.groups())

        property_name = (
            entry.identifier_name
            or f"string_{string_id}"
        )

        left = MemberExpression(
            receiver=self.get_register_value(analysis, obj_reg),
            # NOTE (fix): the original used `ConstantValue(property_name)`
            # here, which renders a *quoted string* as the dot-access
            # target (`obj."foo"` - not valid JS). A property name after
            # `.` must be a bare identifier, matching PutById's own
            # (correct) use of an identifier for the same kind of value.
            member=Identifier(name=property_name),
            computed=False,
        )
        right = self.get_register_value(analysis, value_reg)

        expression = AssignmentExpression(left=left, operator=AssignmentOperator.ASSIGN, right=right)

        variable = JSVariable(self.__class__.__name__, entry.address, "", expression)
        analysis.add_result(entry, variable)

        return OpcodeResult(entry, variable)


class PutNewOwnByIdShort(PutNewOwnByIdX):
    pass


class PutNewOwnById(PutNewOwnByIdX):
    pass


class PutNewOwnByIdLong(PutNewOwnByIdX):
    pass