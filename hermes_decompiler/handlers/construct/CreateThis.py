from hermes_decompiler.frontend.opcode import OpcodeResult
from hermes_decompiler.handlers import OpcodeHandler, OpcodeContext, ArgsPattern, sequence, REG, UINT8
from hermes_decompiler.ir.expressions import ThisPlaceholder


# Reg8, Reg8, Reg8 (total size 3)
# DEFINE_OPCODE_3(CreateThis, Reg8, Reg8, Reg8)
# Example: <CreateThis>: <Reg8: 3, Reg8: 3, Reg8: 2>
class CreateThis(OpcodeHandler):
    """Represents `this` object allocation prior to a constructor call."""

    ARGUMENTS = ArgsPattern(sequence(REG, REG, REG), "Reg8, Reg8, Reg8")

    def handle(self, ctx: OpcodeContext) -> OpcodeResult:
        match = self.match_arguments(ctx)
        if isinstance(match, OpcodeResult):
            return match

        dest_reg, func, new_target = (int(x) for x in match.groups())

        # self.get_register_expression(ctx.analysis, func) # consume it ?
        this_expr = ThisPlaceholder(origin="CreateThis", source_reg=func)

        result = OpcodeResult(ctx.entry, value=this_expr, dest_reg=dest_reg)
        ctx.analysis.add_result(result)

        return result


# Reg8, Reg8, UInt8 (total size 3)
# DEFINE_OPCODE_3(CreateThisForNew, Reg8, Reg8, UInt8)
# Example: <CreateThisForNew>: <Reg8: 2, Reg8: 3, UInt8: 3>
class CreateThisForNew(OpcodeHandler):
    """Allocate the uninitialized `this` object ahead of a `new` call."""

    ARGUMENTS = ArgsPattern(sequence(REG, REG, UINT8), "Reg8, Reg8, UInt8")

    def handle(self, ctx: OpcodeContext) -> OpcodeResult:
        match = self.match_arguments(ctx)
        if isinstance(match, OpcodeResult):
            return match

        dest_reg, constructor_reg, _cache = map(int, match.groups())

        this_expr = ThisPlaceholder(origin="CreateThisForNew", source_reg=constructor_reg)

        result = OpcodeResult(ctx.entry, value=this_expr, dest_reg=dest_reg)
        ctx.analysis.add_result(result)

        return result


# Reg8, Reg8, Reg8, UInt8 (total size 4)
# DEFINE_OPCODE_4(CreateThisForSuper, Reg8, Reg8, Reg8, UInt8)
# Example: <CreateThis>: <CreateThisForSuper>: <Reg8: 4, Reg8: 2, Reg8: 1, UInt8: 0>
class CreateThisForSuper(OpcodeHandler):
    """Allocate the uninitialized `this` object ahead of a `super(...)` call."""

    ARGUMENTS = ArgsPattern(sequence(REG, REG, REG, UINT8), "Reg8, Reg8, Reg8, UInt8")

    def handle(self, ctx: OpcodeContext) -> OpcodeResult:
        match = self.match_arguments(ctx)
        if isinstance(match, OpcodeResult):
            return match

        dest_reg, constructor_reg, new_target_reg, _cache = map(int, match.groups())

        this_expr = ThisPlaceholder(origin="CreateThisForSuper", source_reg=constructor_reg)

        result = OpcodeResult(ctx.entry, value=this_expr, dest_reg=dest_reg)
        ctx.analysis.add_result(result)

        return result
