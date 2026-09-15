from hermes_decompiler.frontend.handlers import OpcodeHandler, OpcodeContext, ArgsPattern, sequence, REG, UINT8, UINT32
from hermes_decompiler.frontend.opcode import OpcodeResult
from hermes_decompiler.ir.expressions import CallExpression, Identifier


# Reg8, Reg8, UInt32, UInt8 (total size 7)
# DEFINE_OPCODE_4(CacheNewObject, Reg8, Reg8, UInt32, UInt8)
# Example: <CacheNewObject>: <Reg8: 4, Reg8: 5, UInt32: 2297, UInt8: 0>
class CacheNewObject(OpcodeHandler):
    """Runtime hint: look up/cache the hidden-class shape for a `this`/new.target pair. No JS-visible effect."""

    ARGUMENTS = ArgsPattern(sequence(REG, REG, UINT32, UINT8), "Reg8, Reg8, UInt32, UInt8")

    def handle(self, ctx: OpcodeContext) -> OpcodeResult:
        match = self.match_arguments(ctx)
        if isinstance(match, OpcodeResult):
            return match

        this_reg, new_target_reg, _shape_idx, _cache_idx = map(int, match.groups())

        this_value = self.get_register_expression(ctx.analysis, this_reg)
        new_target = self.get_register_expression(ctx.analysis, new_target_reg)

        expression = CallExpression(
            callee=Identifier(name="__cacheNewObject__"),
            arguments=(this_value, new_target),
        )

        # No destination register -- this opcode doesn't produce a value.
        result = OpcodeResult(ctx.entry, value=expression, dest_reg=None)
        ctx.analysis.add_result(result)

        return result
