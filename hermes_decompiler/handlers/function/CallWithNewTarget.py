from hermes_decompiler.handlers import OpcodeHandler, REG, UINT8, sequence
from hermes_decompiler.ir.expressions import (
    ArrayExpression,
    CallExpression,
    Identifier,
    MemberExpression,
)
from hermes_decompiler.opcode import OpcodeEntry, OpcodeResult
from hermes_decompiler.runtime import HermesAnalysis


# DEFINE_OPCODE_4(CallWithNewTarget, Reg8, Reg8, Reg8, UInt8)   [confirmed, hermes-dec table]
#
#   "Call a function with an explicitly specified `new.target`.
#    Arg1 is the destination of the return value. Arg2 is the closure
#    to invoke. Arg3 is the value of new.target. Arg4 is the number of
#    arguments, assumed to be found in reverse order from the end of
#    the current frame."
#
# Same runtime-argument-count/stack-range shape as `Call` (Arg4 here
# plays the same role as Call's Arg3), plus an explicit new.target
# register that plain Call doesn't have. This backs the low-level
# mechanics of derived-class `super(...)` calls and Reflect.construct,
# where new.target must be forwarded rather than defaulting to the
# callee itself.
#
# There's no single native JS call syntax for "invoke closure C with an
# explicit new.target" other than Reflect.construct(target, argsList,
# newTarget) -- and Reflect.construct's argsList parameter is an actual
# array, not a spread arg list, so the arguments are wrapped in an
# ArrayExpression rather than spread positionally (unlike plain `Call`,
# which spreads them). The CallX `this`-elision special-casing doesn't
# apply here either, since this opcode has no separate thisArg operand
# at all -- the callee's own `this` binding is governed by new.target.
#
# NOTE: `CallWithNewTargetLong` (32-bit arg count variant, matching the
# Call/CallLong pattern) was not independently found for this opcode --
# add analogously if it shows up in your bytecode stream.
class CallWithNewTarget(OpcodeHandler):
    """Call a function with an explicit `new.target`, e.g. super(...) plumbing."""

    _PATTERN = sequence(REG, REG, REG, UINT8)

    def handle(self, analysis: HermesAnalysis, entry: OpcodeEntry) -> OpcodeResult:
        match = self._PATTERN.match(entry.args.strip())
        if not match:
            return self.build_invalid_args_result(
                analysis, entry, "Expected Reg8, Reg8, Reg8, UInt8 arguments"
            )

        dest_reg, func_reg, new_target_reg, num_args = map(int, match.groups())

        callee = self.get_register_value(analysis, func_reg)
        new_target = self.get_register_value(analysis, new_target_reg)

        arg_regs = list(range(func_reg - num_args, func_reg))
        arguments = ArrayExpression(elements=tuple(Identifier(name=f"r{r}") for r in arg_regs))

        call_callee = MemberExpression(
            receiver=Identifier(name="Reflect"),
            member=Identifier(name="construct"),
            computed=False,
        )

        expression = CallExpression(
            callee=call_callee,
            arguments=(callee, arguments, new_target),
        )

        result = OpcodeResult(entry, value=expression, dest_reg=dest_reg)
        analysis.add_result(result)

        return result

# CallWithNewTargetLong
