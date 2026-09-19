from hermes_decompiler.frontend.handlers import OpcodeHandler, OpcodeContext, ArgsPattern, sequence, REG, UINT8
from hermes_decompiler.frontend.opcode import OpcodeResult
from hermes_decompiler.ir.expressions import CallExpression, Identifier, NumericLiteral

_OWN_FRAME_OPCODES = ("CreateEnvironment", "CreateFunctionEnvironment")


# Reg8, UInt8 (total size 2)
# DEFINE_OPCODE_2(GetParentEnvironment, Reg8, UInt8)
# Example: <GetParentEnvironment>: <Reg8: 2, UInt8: 0>
class GetParentEnvironment(OpcodeHandler):
    """Fetch an environment N levels up the *enclosing* scope chain."""

    ARGUMENTS = ArgsPattern(sequence(REG, UINT8), "Reg8, UInt8")

    def handle(self, ctx: OpcodeContext) -> OpcodeResult:
        match = self.match_arguments(ctx)
        if isinstance(match, OpcodeResult):
            return match

        dest_reg, levels = map(int, match.groups())

        expression = CallExpression(
            callee=Identifier(name="getParentEnvironment"),
            arguments=(NumericLiteral(value=levels),),
        )

        # "N levels up the ENCLOSING chain" (see this class's own
        # docstring) - levels=0 already means one hop up (the immediate
        # lexical parent) *only* when this function has its own depth-0
        # frame to skip past in the first place; for a function that
        # never runs its own CreateEnvironment/CreateFunctionEnvironment,
        # there's no such layer, so levels=0 here means exactly the same
        # thing GetEnvironment's own levels=0 would (confirmed against
        # PrivateStaticTests.ts's inlined `new Counter()` - see
        # EnvironmentOriginTable's own docstring on `frame_offset` for
        # the full reasoning, this is that same adjustment applied here
        # instead of at table-build time since this handler has the
        # current function's own entries on hand to check directly).
        has_own_frame = any(entry.opcode in _OWN_FRAME_OPCODES for entry in ctx.entries)
        effective_depth = levels + (1 if has_own_frame else 0)

        result = OpcodeResult(ctx.entry, value=expression, dest_reg=dest_reg, env_source=(effective_depth, None))
        ctx.analysis.add_result(result)

        return result
