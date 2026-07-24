from hermes_decompiler.ir.Expressions import MemberExpression
from hermes_decompiler.ir.Statements import AssignmentStatement
from hermes_decompiler.ir.Values import ConstantValue

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

        variable = JSVariable(
            self.__class__.__name__,
            entry.address,
            "",
            AssignmentStatement(
                left=MemberExpression(
                    object=self.get_register_value(analysis, obj_reg),
                    property=ConstantValue(property_name),
                ),
                right=self.get_register_value(analysis, value_reg),
            ),
        )

        analysis.add_result(entry, variable)

        return OpcodeResult(entry, variable)


class PutNewOwnByIdShort(PutNewOwnByIdX):
    pass


class PutNewOwnById(PutNewOwnByIdX):
    pass


class PutNewOwnByIdLong(PutNewOwnByIdX):
    pass