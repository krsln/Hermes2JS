from hermes_decompiler.ir.Expressions import MemberExpression
from hermes_decompiler.ir.Statements import AssignmentStatement
from hermes_decompiler.ir.Values import IdentifierValue

from hermes_decompiler.models.HermesAnalysis import HermesAnalysis
from hermes_decompiler.models.OpcodeEntry import OpcodeEntry
from hermes_decompiler.models.OpcodeHandler import OpcodeHandler
from hermes_decompiler.models.OpcodeResult import OpcodeResult
from hermes_decompiler.models.JSVariable import JSVariable

from hermes_decompiler.handlers._shared_patterns import (
    REG,
    UINT8,
    STRING_ID,
    sequence,
)


class PutById(OpcodeHandler):
    """
    Put object property by identifier.

    Hermes:
        PutById rObj, rValue, cache, string_id

    JavaScript:
        rObj.foo = rValue;
    """

    _PATTERN = sequence(REG, REG, UINT8, STRING_ID)

    def handle(
            self,
            analysis: HermesAnalysis,
            entry: OpcodeEntry,
    ) -> OpcodeResult:
        match = self._PATTERN.match(entry.args.strip())
        if not match:
            return self.build_invalid_args_result(analysis, entry)

        obj_reg, value_reg, _cache, string_id = map(int, match.groups())

        property_name = (
                entry.identifier_name
                or f"string_{string_id}"
        )

        left = MemberExpression(
            object=self.get_register_value(analysis, obj_reg),
            property=IdentifierValue(property_name),
            computed=False,
        )

        right = self.get_register_value(analysis, value_reg)

        variable = JSVariable(
            self.__class__.__name__,
            entry.address,
            "",
            AssignmentStatement(
                left=left,
                right=right,
            ),
        )

        analysis.add_result(entry, variable)

        return OpcodeResult(entry, variable)


class PutByIdLong(PutById):
    pass
