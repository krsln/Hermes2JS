from hermes_decompiler.ir.Expressions import CallExpression, MemberExpression
from hermes_decompiler.ir.Values import ObjectLiteralValue, ConstantValue, IdentifierValue
from hermes_decompiler.models.HermesAnalysis import HermesAnalysis
from hermes_decompiler.models.OpcodeResult import OpcodeResult
from hermes_decompiler.models.JSVariable import JSVariable
from hermes_decompiler.models.OpcodeEntry import OpcodeEntry
from hermes_decompiler.models.OpcodeHandler import OpcodeHandler

from hermes_decompiler.handlers._shared_patterns import REG, UINT8, STRING_ID, sequence

# Patterns
PUT_GETTER_SETTER_PATTERN = sequence(REG, REG, REG, REG, UINT8)


class PutOwnGetterSetterByVal(OpcodeHandler):
    """Define getter/setter property."""

    def handle(self, analysis: HermesAnalysis, entry: OpcodeEntry) -> OpcodeResult:
        handler = self.__class__.__name__

        match = PUT_GETTER_SETTER_PATTERN.match(entry.args.strip())
        if not match:
            return self.build_invalid_args_result(
                analysis,
                entry,
                "Expected 4 Reg + UInt8",
            )

        obj_reg, key_reg, getter_reg, setter_reg, enumerable_flag = map(
            int,
            match.groups(),
        )

        properties = {}

        getter = self.get_register_value_new(analysis, getter_reg)
        if getter is not None:
            properties["get"] = getter

        setter = self.get_register_value_new(analysis, setter_reg)
        if setter is not None:
            properties["set"] = setter

        properties["enumerable"] = ConstantValue(bool(enumerable_flag))
        properties["configurable"] = ConstantValue(True)

        descriptor = ObjectLiteralValue(properties)

        call = CallExpression(
            callee=MemberExpression(
                object=IdentifierValue("Object"),
                property=ConstantValue("defineProperty"),
            ),
            arguments=[
                self.get_register_value_new(analysis, obj_reg),
                self.get_register_value_new(analysis, key_reg),
                descriptor,
            ],
        )

        variable = JSVariable(
            self.__class__.__name__,
            entry.address,
            "",
            call,
        )

        analysis.add_result(entry, variable)

        return OpcodeResult(entry, variable)
