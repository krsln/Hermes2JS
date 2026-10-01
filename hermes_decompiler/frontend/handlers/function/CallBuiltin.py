import re

from hermes_decompiler.frontend.handlers import OpcodeHandler, OpcodeContext, ArgsPattern, sequence, REG, UINT8, UINT32
from hermes_decompiler.frontend.opcode import OpcodeResult
from hermes_decompiler.ir.expressions import CallExpression, Identifier


# /// Call a builtin function.
# /// Note this is NOT marked as a Ret target, because the callee is native and therefore never JS.
# /// Arg1 is the destination of the return value.
# /// Arg2 is the builtin number.
# /// Arg3 is the number of arguments, assumed to be found in reverse order from the end of the current frame.
# DEFINE_OPCODE_3(CallBuiltin, Reg8, UInt8, UInt8)

# Reg8, UInt8, UInt8 (total size 3)
# DEFINE_OPCODE_3(CallBuiltin, Reg8, UInt8, UInt8)
# Example: <CallBuiltin>: <Reg8: 1, UInt8: 46, UInt8: 3>  # Built-in function: [#46 arraySpread]
class CallBuiltin(OpcodeHandler):
    ARGUMENTS = ArgsPattern(sequence(REG, UINT8, UINT8), "Reg8, UInt8, UInt8")

    def handle(self, ctx: OpcodeContext) -> OpcodeResult:
        match = self.match_arguments(ctx)
        if isinstance(match, OpcodeResult):
            return match

        dest_reg, builtin_id, arg_count = map(int, match.groups())

        callee = Identifier(
            name=ctx.entry.builtin_function.name
            if ctx.entry.builtin_function
            else f"builtin_{builtin_id}/* unresolved arg */"
        )

        # CallBuiltin's arguments are NOT relative to dest_reg (it is only
        # where the return value lands), they occupy the outgoing-argument
        # window at the top of the frame: `[this, arg1, ..., argN]`, `this`
        # at the HIGHEST register of the window (same layout `Construct`
        # uses). `arg_count` includes that `this` slot, and native builtins
        # ignore `this`, so the compiler reserves the slot but never writes
        # it - printing it made every such call end in a dangling `rN`
        # (`copyDataProperties(r7, r6, r5)` with no `r5` anywhere).
        real_arg_count = max(arg_count - 1, 0)
        this_reg = self._window_top(ctx, real_arg_count)

        arguments = tuple(
            self.resolve_call_argument(ctx.analysis, reg)
            for reg in range(this_reg - 1, this_reg - 1 - real_arg_count, -1)
        )

        expression = CallExpression(callee=callee, arguments=arguments, )

        result = OpcodeResult(ctx.entry, value=expression, dest_reg=dest_reg)
        ctx.analysis.add_result(result)

        return result

    # How many instructions back a write still counts as "setting up THIS
    # call's arguments" when telling window candidates apart.
    _RECENT_WRITE_RANGE = 14
    _REG_OPERAND_RE = re.compile(r"Reg(?:8|32):\s*(\d+)")

    @classmethod
    def _window_top(cls, ctx: OpcodeContext, real_arg_count: int) -> int:
        """Register of the window's `this` slot (its top).

        The top is the same for every windowed call of a function (measured
        over all 65 functions of the hermes-96/98 fixtures that have one),
        so `max register seen SO FAR` is wrong whenever nothing has written
        that top slot yet: a builtin never does, so e.g. in
        spreadObjectTest the real arguments are r7/r6 but the old
        "highest so far" put the window one register too low.

        The unwritten `this` slot is at most one above the highest register
        any instruction of the function mentions, and is that register
        itself when something else in the function also uses the top slot.
        Both candidates are tried and the one whose argument slots were
        actually written just before this call (and whose `this` slot was
        not) wins; a tie goes to the more common `max + 1` layout.
        """
        operands = [
            int(reg)
            for entry in ctx.entries
            for reg in cls._REG_OPERAND_RE.findall(entry.args or "")
        ]

        if not operands:
            return real_arg_count

        highest = max(operands)

        if real_arg_count == 0:
            return highest + 1  # nothing to resolve

        index_of = {entry.address: i for i, entry in enumerate(ctx.entries)}
        recent: set[int] = set()

        for name, state in ctx.analysis.registers.items():
            defined_at = index_of.get(state.definition.address)

            if defined_at is not None and 0 < ctx.index - defined_at <= cls._RECENT_WRITE_RANGE:
                recent.add(int(name[1:]))

        def evidence(top: int) -> int:
            slots = range(top - 1, top - 1 - real_arg_count, -1)

            if min(slots) < 0:
                return -real_arg_count - 1

            return sum(1 for reg in slots if reg in recent) - (1 if top in recent else 0)

        return max((highest + 1, highest), key=lambda top: (evidence(top), top == highest + 1))


# Reg8, UInt8, UInt32 (total size 6)
# DEFINE_OPCODE_3(CallBuiltinLong, Reg8, UInt8, UInt32)
class CallBuiltinLong(CallBuiltin):
    ARGUMENTS = ArgsPattern(sequence(REG, UINT8, UINT32), "Reg8, UInt8, UInt32")
