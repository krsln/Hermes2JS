from hermes_decompiler.frontend.handlers import OpcodeHandler, OpcodeContext, ArgsPattern, sequence, REG, STRING_ID, UINT8
from hermes_decompiler.frontend.opcode import OpcodeResult
from hermes_decompiler.ir.Operators import UnaryOperator
from hermes_decompiler.ir.expressions import UnaryExpression, MemberExpression, Identifier


# Reg8, Reg8, UInt16 (string_id) (total size 4)
# DEFINE_OPCODE_3(DelById, Reg8, Reg8, UInt16)
# Example: <DelById>: <Reg8: 11, Reg8: 11, string_id: 15620>  # String: 'channels' (Identifier)
class DelById(OpcodeHandler):
    ARGUMENTS = ArgsPattern(sequence(REG, REG, STRING_ID), "Reg8, Reg8, UInt16 (string_id)")

    def handle(self, ctx: OpcodeContext) -> OpcodeResult:
        match = self.match_arguments(ctx)
        if isinstance(match, OpcodeResult):
            return match

        dest_reg, obj_reg, string_id = map(int, match.groups())

        prop_name = ctx.entry.identifier_name or f"string_{string_id}"
        obj = self.get_register_expression(ctx.analysis, obj_reg)

        expression = UnaryExpression(
            operator=UnaryOperator.DELETE,
            operand=MemberExpression(obj=obj, prop=Identifier(name=prop_name)),
        )

        result = OpcodeResult(ctx.entry, value=expression, dest_reg=dest_reg)
        ctx.analysis.add_result(result)

        return result


# Reg8, Reg8, UInt32 (string_id) (total size 6)
# DEFINE_OPCODE_3(DelByIdLong, Reg8, Reg8, UInt32)

# Reg8, Reg8, UInt16 (string_id) (total size 4)
# DEFINE_OPCODE_3(DelByIdLoose, Reg8, Reg8, UInt16)

# Reg8, Reg8, UInt32 (string_id) (total size 6)
# DEFINE_OPCODE_3(DelByIdLooseLong, Reg8, Reg8, UInt32)

# Reg8, Reg8, UInt16 (string_id) (total size 4)
# DEFINE_OPCODE_3(DelByIdStrict, Reg8, Reg8, UInt16)

# Reg8, Reg8, UInt32 (string_id) (total size 6)
# DEFINE_OPCODE_3(DelByIdStrictLong, Reg8, Reg8, UInt32)


# Reg8, Reg8, Reg8, UInt8 (total size 4)
# DEFINE_OPCODE_3(DelByVal, Reg8, Reg8, Reg8)
# DEFINE_OPCODE_4(DelByVal, Reg8, Reg8, Reg8, UInt8)
# Example:<DelByVal>: <Reg8: 0, Reg8: 17, Reg8: 5, UInt8: 1>
class DelByVal(OpcodeHandler):
    """delete obj[prop]"""

    ARGUMENTS = (
        ArgsPattern(sequence(REG, REG, REG, UINT8), "Reg8, Reg8, Reg8, UInt8"),
        ArgsPattern(sequence(REG, REG, REG), "Reg8, Reg8, Reg8"),  # DEFINE_OPCODE_3
    )

    def handle(self, ctx: OpcodeContext) -> OpcodeResult:
        match = self.match_arguments(ctx)
        if isinstance(match, OpcodeResult):
            return match

        dest_reg, obj_reg, prop_reg, *_ = map(int, match.groups())

        obj = self.get_register_expression(ctx.analysis, obj_reg)
        prop = self.get_register_expression(ctx.analysis, prop_reg)

        expression = UnaryExpression(
            operator=UnaryOperator.DELETE,
            operand=MemberExpression(obj=obj, prop=prop, computed=True)
        )

        result = OpcodeResult(ctx.entry, value=expression, dest_reg=dest_reg)
        ctx.analysis.add_result(result)

        return result


# Reg8, Reg8, Reg8 (total size 3)
# DEFINE_OPCODE_3(DelByValLoose, Reg8, Reg8, Reg8)
class DelByValLoose(DelByVal):
    pass


# Reg8, Reg8, Reg8 (total size 3)
# DEFINE_OPCODE_3(DelByValStrict, Reg8, Reg8, Reg8)
class DelByValStrict(DelByVal):
    pass
