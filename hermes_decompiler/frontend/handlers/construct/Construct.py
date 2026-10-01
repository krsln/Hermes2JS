from hermes_decompiler.frontend.handlers import OpcodeHandler, OpcodeContext, ArgsPattern, sequence, REG, UINT8, UINT32
from hermes_decompiler.frontend.opcode import OpcodeResult
from hermes_decompiler.ir.expressions import NewExpression


# Reg8, Reg8, UInt8 (total size 3)
# DEFINE_OPCODE_3(Construct, Reg8, Reg8, UInt8)
# Example: <Construct>: <Reg8: 2, Reg8: 4, UInt8: 2>
class Construct(OpcodeHandler):
    """
    Construct using UInt8 argument count.

    Same register-frame convention as the plain `Call` opcode (see
    Call.py's own docstring) - `arg_count` CONSECUTIVE registers ending
    at `highest` (the top of the currently live register range),
    highest-to-lowest: `[this, arg1, arg2, ..., argN]`. Unlike Call1-4,
    neither `Construct` nor `ConstructLong` encodes individual argument
    register numbers in the instruction itself (only `argCount`), so
    there's no explicit operand to read them from - `highest` is the
    only anchor available, exactly like plain `Call`.

    A previous version of this handler instead walked `analysis.results`
    backwards collecting the last `arg_count` not-yet-consumed
    definitions, then sorted THOSE by `dest_reg` ascending to recover
    frame order. That's a different, weaker signal than the register
    range itself: it breaks the moment something between the argument
    loads and the Construct isn't itself a fresh, still-unconsumed
    definition with a `dest_reg` - e.g. the `Mov` that copies
    CreateThis's placeholder into its OWN frame slot right before the
    call (see CreateThis.py/CreateThisForNew.py) sits at whatever
    register `Mov` targets, which doesn't have to be (and here, isn't)
    the highest of the group, so sorting by `dest_reg` silently put
    `this` in the wrong frame position and reversed the two real
    arguments with it - confirmed against ClassTests.ts's
    `new Animal("Generic", "...")` and `new Dog("Rex", "Labrador")`,
    both of which came out with their arguments swapped end-to-end
    before this fix.
    """

    ARGUMENTS = ArgsPattern(sequence(REG, REG, UINT8), "Reg8, Reg8, UInt8")

    def handle(self, ctx: OpcodeContext) -> OpcodeResult:
        match = self.match_arguments(ctx)
        if isinstance(match, OpcodeResult):
            return match

        dest_reg, ctor_reg, arg_count = map(int, match.groups())

        constructor = self.get_register_expression(ctx.analysis, ctor_reg)

        highest = max(
            int(r[1:])
            for r in ctx.analysis.registers
        )

        if highest + 1 < arg_count:
            return self.build_invalid_args_result(ctx.analysis, ctx.entry)

        # [this, arg1, arg2, ..., argN], highest register first.
        this_reg, *arg_regs = range(highest, highest - arg_count, -1)

        # Consumed for its side effect (marks the CreateThis/
        # CreateThisForNew placeholder's defining Mov as folded away
        # rather than left to print as its own `rN = ...;` statement -
        # see ThisPlaceholder's own docstring: it must never survive
        # into rendered output). The value itself is discarded; a
        # `new` expression has no separate `this` slot to print,
        # that's exactly what `constructor` and `arguments` together
        # already express.
        self.get_register_expression(ctx.analysis, this_reg)

        arguments = tuple(
            self.resolve_call_argument(ctx.analysis, reg)
            for reg in arg_regs
        )

        expression = NewExpression(callee=constructor, arguments=arguments)

        result = OpcodeResult(ctx.entry, value=expression, dest_reg=dest_reg)
        ctx.analysis.add_result(result)

        return result


# Reg8, Reg8, UInt32 (total size 6)
# DEFINE_OPCODE_3(ConstructLong, Reg8, Reg8, UInt32)
class ConstructLong(Construct):
    """
    Construct using UInt32 argument count.
    """

    ARGUMENTS = ArgsPattern(sequence(REG, REG, UINT32), "Reg8, Reg8, UInt32")
