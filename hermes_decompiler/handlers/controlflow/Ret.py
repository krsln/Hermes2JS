from hermes_decompiler.analysis.models import TerminatorReturn
from hermes_decompiler.frontend.opcode import OpcodeResult
from hermes_decompiler.handlers import OpcodeHandler, OpcodeContext, ArgsPattern, sequence, REG
from hermes_decompiler.ir.statements import ReturnStatement


# Reg8 (total size 1)
# DEFINE_OPCODE_1(Ret, Reg8)
# Example: <Ret>: <Reg8: 0>
class Ret(OpcodeHandler):
    """
    Return from the current function.

    NOTE (fix): this file previously contained a stray copy of
    `Throw.py` - a `class Throw` (not `Ret`), which meant no handler was
    ever registered for the `Ret` opcode at all (`OpcodeHandler.
    __init_subclass__` keys the registry by class name). Every function
    body was ending with an unhandled `Ret`, and the file's duplicate
    `Throw` class was silently overwriting the real one from Misc/Throw.py
    in the registry, depending on import order.
    """

    ARGUMENTS = ArgsPattern(sequence(REG), "Reg8")

    def handle(self, ctx: OpcodeContext) -> OpcodeResult:
        match = self.match_arguments(ctx)
        if isinstance(match, OpcodeResult):
            return match

        value_reg = int(match.group(1))

        # NOTE (fix): previously `get_register_expression`, which
        # inlines whatever value was MOST RECENTLY seen for this
        # register during this single, linear, ADDRESS-ORDER scan of
        # the bytecode - with no notion of control flow at all. For a
        # register written conditionally (e.g. inside a `catch` block,
        # or on only some loop iterations) and never rewritten
        # afterward in ADDRESS order, that conditional write gets
        # inlined as if it always executes - producing a WRONG return
        # value whenever the actual runtime path never took that
        # write (see tryCatchInsideLoopTest/section_15085's own
        # `failures` counter: `Ret r0` was rendering as `return r2 +
        # 1;`, a copy of the counter's `catch`-only increment,
        # regardless of whether any exception was ever actually
        # caught). Kept symbolic here (`r{N}`, never inlined) - a NEW,
        # later region pass
        # (`region_passes.ReturnValueResolutionPass`) runs AFTER
        # structuring, when real CFG/dominance information is
        # available, and only then folds this back into an inlined
        # expression when it can positively confirm every reaching
        # definition agrees.
        expression = self.get_register_reference(ctx.analysis, value_reg)
        terminator = TerminatorReturn(value=expression)

        # NOTE (fix): a `Return` terminator is never "consumed" by any
        # structurer (only `ConditionalBranch` is, when folded into an
        # if/while condition) - so unless this opcode also carries its
        # own renderable `statement`, the `return` disappears from the
        # output entirely once it reaches the printer. Building the
        # `ReturnStatement` right here, at the source of truth for what
        # value is being returned, is the most robust place: it can't
        # get skipped by a structural-analysis pass forgetting about it.
        statement = ReturnStatement(argument=expression)

        result = OpcodeResult(
            ctx.entry, value=expression, statement=statement, terminator=terminator, dest_reg=None
        )
        ctx.analysis.add_result(result)

        return result
