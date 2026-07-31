from hermes_decompiler.handlers import OpcodeHandler, REG, UINT8, sequence
from hermes_decompiler.ir.expressions import (
    CallExpression,
    Identifier,
    MemberExpression,
    ObjectExpression,
    ObjectProperty,
    python_literal,
)
from hermes_decompiler.opcode import OpcodeEntry, OpcodeResult
from hermes_decompiler.runtime import HermesAnalysis


# Reg8, Reg8, Reg8, Reg8, UInt8 (total size 5)
# Example: <Reg8: 1, Reg8: 3, Reg8: 4, Reg8: 0, UInt8: 1>
class PutOwnGetterSetterByVal(OpcodeHandler):
    """Add a getter and a setter for a property by value."""

    _PATTERN = sequence(REG, REG, REG, REG, UINT8)

    def handle(self, analysis: HermesAnalysis, entry: OpcodeEntry) -> OpcodeResult:
        match = self._PATTERN.match(entry.args.strip())
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
            ObjectProperty(key=Identifier(name="get"), value=self.get_register_expression(analysis, getter_reg)),
            ObjectProperty(key=Identifier(name="set"), value=self.get_register_expression(analysis, setter_reg)),
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
                self.get_register_expression(analysis, obj_reg),
                self.get_register_expression(analysis, key_reg),
                descriptor,
            ),
        )

        result = OpcodeResult(entry, value=expression, dest_reg=None)
        analysis.add_result(result)

        return result
