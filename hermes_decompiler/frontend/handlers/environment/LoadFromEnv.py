from hermes_decompiler.frontend.opcode import OpcodeResult
from frontend.handlers import OpcodeHandler, OpcodeContext, ArgsPattern, sequence, REG, UINT8, UINT16
from hermes_decompiler.ir.expressions import MemberExpression, NumericLiteral


# Reg8, Reg8, UInt8 (total size 3)
# DEFINE_OPCODE_3(LoadFromEnvironment, Reg8, Reg8, UInt8)
# Example: <LoadFromEnvironment>: <Reg8: 5, Reg8: 1, UInt8: 19>
class LoadFromEnvironment(OpcodeHandler):
    """
    Load a value from a lexical environment.

        dst = env[slot]
    """

    ARGUMENTS = ArgsPattern(sequence(REG, REG, UINT8), "Reg8, Reg8, UInt8")

    def handle(self, ctx: OpcodeContext) -> OpcodeResult:
        match = self.match_arguments(ctx)
        if isinstance(match, OpcodeResult):
            return match

        dest_reg, env_reg, slot = map(int, match.groups())

        env = self.get_register_expression(ctx.analysis, env_reg)

        expression = MemberExpression(obj=env, prop=NumericLiteral(slot), computed=True)

        result = OpcodeResult(ctx.entry, value=expression, dest_reg=dest_reg)
        ctx.analysis.add_result(result)

        return result


# Reg8, Reg8, UInt16 (total size 4)
# DEFINE_OPCODE_3(LoadFromEnvironmentL, Reg8, Reg8, UInt16)
# Example: <LoadFromEnvironmentL>: <Reg8: 7, Reg8: 5, UInt16: 269>
class LoadFromEnvironmentL(LoadFromEnvironment):
    ARGUMENTS = ArgsPattern(sequence(REG, REG, UINT16), "Reg8, Reg8, UInt16")
