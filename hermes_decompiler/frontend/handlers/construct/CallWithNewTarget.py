from hermes_decompiler.frontend.handlers import OpcodeHandler, OpcodeContext, ArgsPattern, sequence, REG, UINT8
from hermes_decompiler.frontend.opcode import OpcodeResult
from hermes_decompiler.ir.expressions import (
    ArrayExpression,
    CallExpression,
    Identifier,
    MemberExpression,
    ThisPlaceholder,
)


# Reg8, Reg8, Reg8, UInt8 (total size 4)
# DEFINE_OPCODE_4(CallWithNewTarget, Reg8, Reg8, Reg8, UInt8)
# Example: <CallWithNewTarget>: <Reg8: 1, Reg8: 2, Reg8: 5, UInt8: 3>
class CallWithNewTarget(OpcodeHandler):
    """
    Call a function with an explicit `new.target`, e.g. super(...) plumbing.

    Same outgoing-argument window as `Construct` (see its docstring):
    `[this, arg1, ..., argN]`, `this` at the HIGHEST register of the window,
    and the count includes `this`. The window is NOT relative to the callee
    register - the old `range(func_reg - num_args, func_reg)` produced
    `Reflect.construct(r2, [r-1, r0, r1], ...)`: wrong registers, some of
    them not even valid (negative), none of them defined anywhere.

    For a `super(...)` call the `this` slot holds the placeholder
    `CreateThisForSuper` created (usually through a `Mov`), so the window's
    top is found as the not-yet-read placeholder derived from this very
    callee; "highest register seen so far" (what `Construct` uses) is only
    the fallback. The `this` slot is consumed here and not printed - what
    `super(...)` actually returns is picked up by the `SelectObject` that
    follows (see SelectObject.py).
    """

    ARGUMENTS = ArgsPattern(sequence(REG, REG, REG, UINT8), "Reg8, Reg8, Reg8, UInt8")

    def handle(self, ctx: OpcodeContext) -> OpcodeResult:
        match = self.match_arguments(ctx)
        if isinstance(match, OpcodeResult):
            return match

        dest_reg, func_reg, new_target_reg, num_args = map(int, match.groups())

        this_reg = self._window_top(ctx, func_reg)

        if num_args < 1 or this_reg + 1 < num_args:
            return self.build_invalid_args_result(ctx.analysis, ctx.entry)

        callee = self.get_register_expression(ctx.analysis, func_reg)
        new_target = self.get_register_expression(ctx.analysis, new_target_reg)

        # Consumed for its side effect only (marks the placeholder's defining
        # `Mov` as folded away); `this` has no surface syntax of its own.
        self.get_register_expression(ctx.analysis, this_reg, keep_placeholder=True)

        arguments = ArrayExpression(elements=tuple(
            self.resolve_call_argument(ctx.analysis, reg)
            for reg in range(this_reg - 1, this_reg - num_args, -1)
        ))

        call_callee = MemberExpression(
            obj=Identifier(name="Reflect"),
            prop=Identifier(name="construct"),
            computed=False,
        )

        expression = CallExpression(
            callee=call_callee,
            arguments=(callee, arguments, new_target),
        )

        result = OpcodeResult(ctx.entry, value=expression, dest_reg=dest_reg)
        ctx.analysis.add_result(result)

        return result

    @staticmethod
    def _window_top(ctx: OpcodeContext, func_reg: int) -> int:
        """Register of the window's `this` slot (its top)."""
        candidates = [
            int(name[1:])
            for name, state in ctx.analysis.registers.items()
            if isinstance(state.value, ThisPlaceholder)
               and state.value.origin == "CreateThisForSuper"
               and state.value.source_reg == func_reg
               and state.reads == 0
        ]

        if candidates:
            return max(candidates)

        return max((int(name[1:]) for name in ctx.analysis.registers), default=-1)


# Reg8, Reg8, Reg8, Reg8 (total size 4)
# DEFINE_OPCODE_4(CallWithNewTargetLong, Reg8, Reg8, Reg8, Reg8)
class CallWithNewTargetLong(CallWithNewTarget):
    _PATTERN = sequence(REG, REG, REG, REG)
    ARGUMENTS = ArgsPattern(sequence(REG, REG, REG, REG), "Reg8, Reg8, Reg8, Reg8")
