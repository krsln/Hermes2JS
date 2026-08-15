from hermes_decompiler.frontend.opcode import OpcodeResult
from hermes_decompiler.handlers import OpcodeHandler, OpcodeContext, ArgsPattern, sequence, REG, UINT8, UINT16
from hermes_decompiler.ir.Operators import AssignmentOperator
from hermes_decompiler.ir.expressions import AssignmentExpression, MemberExpression, NumericLiteral


# Reg8, UInt8, Reg8 (total size 3)
# DEFINE_OPCODE_3(StoreToEnvironment, Reg8, UInt8, Reg8)
# Example: <StoreToEnvironment>: <Reg8: 1, UInt8: 0, Reg8: 4>
class StoreToEnvironment(OpcodeHandler):
    """
    Store a value into a lexical environment.

        env[slot] = value
    """

    ARGUMENTS = ArgsPattern(sequence(REG, UINT8, REG), "Reg8, UInt8, Reg8"),

    def handle(self, ctx: OpcodeContext) -> OpcodeResult:
        match = self.match_arguments(ctx)
        if isinstance(match, OpcodeResult):
            return match

        env_reg, slot, value_reg = map(int, match.groups())
        env = self.get_register_expression(ctx.analysis, env_reg)
        value = self.get_register_expression(ctx.analysis, value_reg)

        left = MemberExpression(receiver=env, member=NumericLiteral(slot), computed=True)
        expression = AssignmentExpression(left=left, operator=AssignmentOperator.ASSIGN, right=value)

        # No destination register (name=""): OpcodeResult/JSRenderer
        # already render a name-less Expression as a bare statement
        # (`env[17] = r5;`), so no extra ExpressionStatement wrapper
        # is needed here.
        result = OpcodeResult(ctx.entry, value=expression, dest_reg=None)
        ctx.analysis.add_result(result)

        return result


# Reg8, UInt16, Reg8 (total size 4)
# DEFINE_OPCODE_3(StoreToEnvironmentL, Reg8, UInt16, Reg8)
# Example: <StoreToEnvironmentL>: <Reg8: 5, UInt16: 385, Reg8: 4>
class StoreToEnvironmentL(StoreToEnvironment):
    ARGUMENTS = ArgsPattern(sequence(REG, UINT16, REG), "Reg8, UInt16, Reg8"),


# Reg8, UInt8, Reg8 (total size 3)
# DEFINE_OPCODE_3(StoreNPToEnvironment, Reg8, UInt8, Reg8)
# Example: <StoreNPToEnvironment>: <Reg8: 3, UInt8: 13, Reg8: 0>
class StoreNPToEnvironment(StoreToEnvironment):
    """
    Non-pointer variant.

    Semantically identical during decompilation.
    """

    pass


# Reg8, UInt16, Reg8 (total size 4)
# DEFINE_OPCODE_3(StoreNPToEnvironmentL, Reg8, UInt16, Reg8)
# Example: <StoreNPToEnvironmentL>: <Reg8: 0, UInt16: 264, Reg8: 11>
class StoreNPToEnvironmentL(StoreToEnvironmentL):
    """
    Long non-pointer variant.
    """
    ARGUMENTS = ArgsPattern(sequence(REG, UINT16, REG), "Reg8, UInt16, Reg8"),
