from hermes_decompiler.frontend.opcode import OpcodeResult
from frontend.handlers import OpcodeHandler, OpcodeContext, ArgsPattern, sequence, REG, UINT8
from hermes_decompiler.ir.expressions import (
    CallExpression,
    Identifier,
    MemberExpression,
    ObjectExpression,
    ObjectProperty,
    python_literal,
)


# Reg8, Reg8, Reg8, Reg8, UInt8 (total size 5)
# Example: <Reg8: 1, Reg8: 3, Reg8: 4, Reg8: 0, UInt8: 1>
class PutOwnGetterSetterByVal(OpcodeHandler):
    """Add a getter and a setter for a property by value."""

    ARGUMENTS = ArgsPattern(
        sequence(REG, REG, REG, REG, UINT8),
        "Reg8, Reg8, Reg8, Reg8, UInt8 (total size 5)"
    )

    def handle(self, ctx: OpcodeContext) -> OpcodeResult:
        match = self.match_arguments(ctx)
        if isinstance(match, OpcodeResult):
            return match

        obj_reg, key_reg, getter_reg, setter_reg, enumerable_flag = map(
            int,
            match.groups(),
        )

        # NOTE: get_register_value() always returns a fallback
        # Identifier, never None (pre-existing behavior, unchanged by
        # this migration), so getter/setter are unconditionally
        # included - same as before.
        properties = (
            ObjectProperty(key=Identifier(name="get"), value=self.get_register_expression(ctx.analysis, getter_reg)),
            ObjectProperty(key=Identifier(name="set"), value=self.get_register_expression(ctx.analysis, setter_reg)),
            ObjectProperty(key=Identifier(name="enumerable"), value=python_literal(bool(enumerable_flag))),
            ObjectProperty(key=Identifier(name="configurable"), value=python_literal(True)),
        )

        descriptor = ObjectExpression(properties=properties)

        expression = CallExpression(
            callee=MemberExpression(obj=Identifier(name="Object"), prop=Identifier(name="defineProperty")),
            arguments=(
                self.get_register_expression(ctx.analysis, obj_reg),
                self.get_register_expression(ctx.analysis, key_reg),
                descriptor,
            ),
        )

        result = OpcodeResult(ctx.entry, value=expression, dest_reg=None)
        ctx.analysis.add_result(result)

        return result
