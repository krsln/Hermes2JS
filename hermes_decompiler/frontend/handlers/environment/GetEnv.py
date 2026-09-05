from hermes_decompiler.frontend.handlers import OpcodeHandler, OpcodeContext, ArgsPattern, sequence, REG, UINT8
from hermes_decompiler.frontend.opcode import OpcodeResult
from hermes_decompiler.ir.expressions import CallExpression, Identifier, NumericLiteral


# /// Get an environment (scope) from N levels up the stack.
# /// 0 is the current environment, 1 is the caller's environment, etc.
# DEFINE_OPCODE_2(GetEnvironment, Reg8, UInt8)

# /// Get an environment by traversing the scope chain.
# /// Arg1 is the destination.
# /// Arg2 is the environment from which to start traversing.
# /// Arg3 is the number of levels up the scope chain to go.
# DEFINE_OPCODE_3(GetEnvironment, Reg8, Reg8, UInt8)

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

        groups = match.groups()

        if len(groups) == 2:
            dest_reg, level = map(int, groups)

        elif len(groups) == 3:
            # Reg8, Reg8, UInt8: op1=dest, op2=unused, op3=level.
            # Matches hermes-dec's own semantics for hbc>=97
            # (pass2_transform_code.py: `GET(op1, op3)` — op2 is never
            # read).
            dest_reg, _, level = map(int, groups)

        else:
            return self.build_exception_result(ctx.analysis, ctx.entry, f"Unexpected GetEnvironment operands: {groups}")

        expression = CallExpression(
            callee=Identifier(name="getEnvironment"),
            arguments=(NumericLiteral(level),),
        )

        result = OpcodeResult(ctx.entry, value=expression, dest_reg=dest_reg)
        ctx.analysis.add_result(result)

        return result
