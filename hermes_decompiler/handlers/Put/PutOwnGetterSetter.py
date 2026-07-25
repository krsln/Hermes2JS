from hermes_decompiler.handlers._shared_patterns import REG, UINT8, sequence
from hermes_decompiler.ir import (
    CallExpression,
    Identifier,
    MemberExpression,
    ObjectExpression,
    ObjectProperty,
    python_literal,
)
from hermes_decompiler.models.HermesAnalysis import HermesAnalysis
from hermes_decompiler.models.OpcodeEntry import OpcodeEntry
from hermes_decompiler.models.OpcodeHandler import OpcodeHandler
from hermes_decompiler.models.OpcodeResult import OpcodeResult

# Patterns
PUT_GETTER_SETTER_PATTERN = sequence(REG, REG, REG, REG, UINT8)


class PutOwnGetterSetterByVal(OpcodeHandler):
    """Define getter/setter property."""

    def handle(self, analysis: HermesAnalysis, entry: OpcodeEntry) -> OpcodeResult:

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

        # NOTE: get_register_value() always returns a fallback
        # Identifier, never None (pre-existing behavior, unchanged by
        # this migration), so getter/setter are unconditionally
        # included - same as before.
        properties = (
            ObjectProperty(key=Identifier(name="get"), value=self.get_register_value(analysis, getter_reg)),
            ObjectProperty(key=Identifier(name="set"), value=self.get_register_value(analysis, setter_reg)),
            ObjectProperty(key=Identifier(name="enumerable"), value=python_literal(bool(enumerable_flag))),
            ObjectProperty(key=Identifier(name="configurable"), value=python_literal(True)),
        )

        descriptor = ObjectExpression(properties=properties)

        expression = CallExpression(
            callee=MemberExpression(
                receiver=Identifier(name="Object"),
                member=Identifier(name="defineProperty"),
            ),
            arguments=(
                self.get_register_value(analysis, obj_reg),
                self.get_register_value(analysis, key_reg),
                descriptor,
            ),
        )

        result = OpcodeResult(entry, value=expression, dest_reg=None)
        analysis.add_result(result)

        return result
