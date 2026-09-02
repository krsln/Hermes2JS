from hermes_decompiler.frontend.opcode import OpcodeResult
from hermes_decompiler.handlers import OpcodeHandler, OpcodeContext, ArgsPattern, sequence, REG, UINT8
from hermes_decompiler.ir.expressions import CallExpression, Identifier, NumericLiteral


# Reg8, Reg8, UInt8 (total size 3)
# DEFINE_OPCODE_3(GetEnvironment, Reg8, Reg8, UInt8)
# DEFINE_OPCODE_2(GetEnvironment, Reg8, UInt8)
# Example: <GetEnvironment>: <Reg8: 4, Reg8: 3, UInt8: 1>
class GetEnvironment(OpcodeHandler):
    """
    Resolve an environment from the lexical scope chain.

    level = 0  -> current environment
    level = 1  -> parent environment
    level = 2  -> grandparent
    ...
    """

    ARGUMENTS = (
        ArgsPattern(sequence(REG, REG, UINT8), "Reg8, Reg8, UInt8"),
        ArgsPattern(sequence(REG, UINT8), "Reg8, UInt8"),  # DEFINE_OPCODE_2
    )

    def handle(self, ctx: OpcodeContext) -> OpcodeResult:
        match = self.match_arguments(ctx)
        if isinstance(match, OpcodeResult):
            return match

        groups = tuple(map(int, match.groups()))

        if len(groups) == 2:
            dest_reg, level = groups
            environment_reg = None

        elif len(groups) == 3:
            dest_reg, environment_reg, level = groups

        else:
            return self.build_exception_result(ctx.analysis, ctx.entry, f"Unexpected GetEnvironment operands: {groups}")

        if environment_reg is None:
            expression = CallExpression(
                callee=Identifier(name="getEnvironment"),
                arguments=(NumericLiteral(level),)
            )
        else:
            expression = CallExpression(
                callee=Identifier(name="getEnvironment"),
                arguments=(Identifier(name=f"r{environment_reg}"), NumericLiteral(level))
            )

        result = OpcodeResult(ctx.entry, value=expression, dest_reg=dest_reg)
        ctx.analysis.add_result(result)

        return result
