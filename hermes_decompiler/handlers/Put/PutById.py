from hermes_decompiler.ir import AssignmentExpression, Identifier, MemberExpression
from hermes_decompiler.ir.Operators import AssignmentOperator

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
            receiver=self.get_register_value(analysis, obj_reg),
            member=Identifier(name=property_name),
            computed=False,
        )

        right = self.get_register_value(analysis, value_reg)

        # No destination register (name=""): OpcodeResult/JSRenderer
        # already render a name-less Expression as a bare statement
        # (`obj.foo = value;`), same pattern as StoreToEnvironment.
        expression = AssignmentExpression(left=left, operator=AssignmentOperator.ASSIGN, right=right)

        variable = JSVariable(self.__class__.__name__, entry.address, "", expression)
        analysis.add_result(entry, variable)

        return OpcodeResult(entry, variable)


class PutByIdLong(PutById):
    pass