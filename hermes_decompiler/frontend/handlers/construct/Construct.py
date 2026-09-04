from hermes_decompiler.frontend.opcode import OpcodeResult
from frontend.handlers import OpcodeHandler, OpcodeContext, ArgsPattern, sequence, REG, UINT8, UINT32
from hermes_decompiler.ir.expressions import Expression, NewExpression, ThisPlaceholder


# Reg8, Reg8, UInt8 (total size 3)
# DEFINE_OPCODE_3(Construct, Reg8, Reg8, UInt8)
# Example: <Construct>: <Reg8: 2, Reg8: 4, UInt8: 2>
class Construct(OpcodeHandler):
    """
    Construct using UInt8 argument count.
    """

    ARGUMENTS = ArgsPattern(sequence(REG, REG, UINT8), "Reg8, Reg8, UInt8")

    def handle(self, ctx: OpcodeContext) -> OpcodeResult:
        match = self.match_arguments(ctx)
        if isinstance(match, OpcodeResult):
            return match

        dest_reg, ctor_reg, arg_count = map(int, match.groups())

        constructor = self.get_register_expression(ctx.analysis, ctor_reg)
        arguments: list[OpcodeResult] = []

        for result in reversed(ctx.analysis.results):
            if result.definition_used:
                continue
            if result.dest_reg is None:
                continue
            if result.entry.address >= ctx.entry.address:
                continue

            arguments.append(result)
            if len(arguments) == arg_count:
                break

        # Register frame order
        arguments.sort(key=lambda r: r.dest_reg)

        this_slots = [i for i, arg in enumerate(arguments) if self._is_this_value(arg.value)]
        if len(this_slots) > 1:
            raise AssertionError(
                f"Construct@{ctx.entry.address}: expected at most one this-placeholder, "
                f"found {len(this_slots)}"
            )

        for arg in arguments:
            arg.definition_used = True

        for i in reversed(this_slots):
            arguments.pop(i)

        values = tuple(arg.value for arg in arguments)
        expression = NewExpression(callee=constructor, arguments=values)

        result = OpcodeResult(ctx.entry, value=expression, dest_reg=dest_reg)
        ctx.analysis.add_result(result)

        return result

    @staticmethod
    def _is_this_value(expr: Expression) -> bool:
        return isinstance(expr, ThisPlaceholder)


# Reg8, Reg8, UInt32 (total size 6)
# DEFINE_OPCODE_3(ConstructLong, Reg8, Reg8, UInt32)
class ConstructLong(Construct):
    """
    Construct using UInt32 argument count.
    """

    ARGUMENTS = ArgsPattern(sequence(REG, REG, UINT32), "Reg8, Reg8, UInt32")
