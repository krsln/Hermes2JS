from hermes_decompiler.frontend.opcode import OpcodeResult
from hermes_decompiler.handlers import OpcodeHandler, OpcodeContext, ArgsPattern, sequence, REG, STRING_ID, UINT8
from hermes_decompiler.ir.expressions import Identifier, MemberExpression, CallExpression, StringLiteral


# Reg8, Reg8, UInt8, UInt16 (string_id) (total size 5)
# DEFINE_OPCODE_4(GetById, Reg8, Reg8, UInt8, UInt16)
# Example: <GetById>: <Reg8: 2, Reg8: 3, UInt8: 3, string_id: 21914>  # String: 'trackJoinCompetitionList' (Identifier)
class GetById(OpcodeHandler):
    """Get property by string ID: obj[propName]"""

    ARGUMENTS = ArgsPattern(
        sequence(REG, REG, UINT8, STRING_ID),
        "Reg8, Reg8, UInt8, UInt16 (string_id)",
    )

    def handle(self, ctx: OpcodeContext) -> OpcodeResult:
        match = self.match_arguments(ctx)
        if isinstance(match, OpcodeResult):
            return match

        dest_reg, obj_reg, _cache, string_id = map(int, match.groups())

        prop_name = ctx.entry.identifier_name or f"string_{string_id}"
        obj = self.get_register_expression(ctx.analysis, obj_reg)

        expression = MemberExpression(obj=obj, prop=Identifier(name=prop_name))

        result = OpcodeResult(ctx.entry, value=expression, dest_reg=dest_reg)
        ctx.analysis.add_result(result)

        return result


# Reg8, Reg8, UInt8, UInt8 (string_id) (total size 4)
# DEFINE_OPCODE_4(GetByIdShort, Reg8, Reg8, UInt8, UInt8)
# Example: <GetByIdShort>: <Reg8: 6, Reg8: 1, UInt8: 4, string_id: 103>  # String: 'concat' (Identifier)
class GetByIdShort(GetById):
    pass


# Reg8, Reg8, UInt8, UInt32 (string_id) (total size 7)
# DEFINE_OPCODE_4(GetByIdLong, Reg8, Reg8, UInt8, UInt32)
# Example:
class GetByIdLong(GetById):
    pass


# Reg8, Reg8, UInt8, UInt16 (string_id) (total size 5)
# DEFINE_OPCODE_4(TryGetById, Reg8, Reg8, UInt8, UInt16)
# Example: <TryGetById>: <Reg8: 14, Reg8: 13, UInt8: 8, string_id: 23> # String: 'Math' (Identifier)
class TryGetById(GetById):
    """TryGetById - similar to GetById, often used with global-object."""

    pass


# Reg8, Reg8, UInt8, UInt32 (string_id) (total size 7)
# DEFINE_OPCODE_4(TryGetByIdLong, Reg8, Reg8, UInt8, UInt32)
# Example:
class TryGetByIdLong(TryGetById):
    pass


# Reg8, Reg8, UInt8, Reg8, UInt32 (string_id) (total size 8)
# DEFINE_OPCODE_5(GetByIdWithReceiverLong, Reg8, Reg8, UInt8, Reg8, UInt32)
# Example: <GetByIdWithReceiverLong>: <Reg8: 8, Reg8: 6, UInt8: 0, Reg8: 2, string_id: 231>  # String: 'start' (Identifier)
class GetByIdWithReceiverLong(OpcodeHandler):
    """obj[prop] lookup with an explicit receiver, e.g. super.prop / Reflect.get semantics."""

    ARGUMENTS = ArgsPattern(sequence(REG, REG, UINT8, REG, STRING_ID), "Reg8, Reg8, UInt8, Reg8, UInt32 (string_id)")

    def handle(self, ctx: OpcodeContext) -> OpcodeResult:
        match = self.match_arguments(ctx)
        if isinstance(match, OpcodeResult):
            return match

        dest_reg, obj_reg, _cache, receiver_reg, string_id = map(int, match.groups())

        prop_name = ctx.entry.identifier_name or f"string_{string_id}"
        obj = self.get_register_expression(ctx.analysis, obj_reg)
        receiver = self.get_register_expression(ctx.analysis, receiver_reg)

        callee = MemberExpression(
            obj=Identifier(name="Reflect"),
            prop=Identifier(name="get"),
            computed=False,
        )

        expression = CallExpression(
            callee=callee,
            arguments=(obj, StringLiteral(value=prop_name), receiver),
        )

        result = OpcodeResult(ctx.entry, value=expression, dest_reg=dest_reg)
        ctx.analysis.add_result(result)

        return result
