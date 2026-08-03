import re
from typing import Dict

from hermes_decompiler.frontend.opcode import OpcodeEntry, OpcodeResult
from hermes_decompiler.handlers import OpcodeHandler, REG, UINT8, sequence
from hermes_decompiler.ir.expressions import CallExpression, Identifier, MemberExpression
from hermes_decompiler.runtime import HermesAnalysis


# Reg8, Reg8, UInt8 (total size 3)
# DEFINE_OPCODE_3(Call, Reg8, Reg8, UInt8)
# Example: <Call>: <Reg8: 4, Reg8: 9, UInt8: 6>
class Call(OpcodeHandler):
    """
    Runtime argument count variant.

    Hermes layout:

        [arg1][arg2]...[argN][callee]

    Example:

        Call r4, r9, 6

    means

        r4 = r9(r3, r4, r5, r6, r7, r8)
    """

    _PATTERN = sequence(REG, REG, UINT8)

    def handle(self, analysis: HermesAnalysis, entry: OpcodeEntry) -> OpcodeResult:
        match = self._PATTERN.match(entry.args.strip())
        if not match:
            return self.build_invalid_args_result(analysis, entry)

        dest_reg, func_reg, num_args = map(int, match.groups())

        callee = self.get_register_expression(analysis, func_reg)
        arg_regs = list(range(func_reg - num_args, func_reg))  # Arguments in reverse order

        # NOTE: kept as bare register references (not resolved via
        # get_register_value), same as the original - the argument slots
        # here are a contiguous stack range that doesn't necessarily
        # correspond to individually tracked register assignments.
        arguments = tuple(
            self.get_register_reference(analysis, r)
            for r in arg_regs
        )

        expression = CallExpression(callee=callee, arguments=arguments)

        result = OpcodeResult(entry, value=expression, dest_reg=dest_reg)
        analysis.add_result(result)

        return result


class Call1(OpcodeHandler):
    """
    Call a function with one arg (`Call1`), and shared base
    implementation for the rest of the fixed-arg-count Call family
    (`Call2`, `Call3`, `Call4`). A real opcode is used as the shared base
    (rather than a separate non-opcode `CallX` class) - see `Add` in
    `handlers/arithmetic/Binary.py` for the rationale.

    Hermes CallN opcodes mirror `Function.prototype.call` semantics:
    the FIRST argument register is always the `this` context, not a
    regular positional argument - `CallN dst, callee, thisArg, arg1,
    arg2, ...`. For the extremely common `obj.method(...)` shape, the
    compiler puts `obj` itself into the `thisArg` slot (the same value
    already sitting in a preceding `GetById`'s receiver), so rendering
    it a second time as an explicit argument duplicates the receiver
    expression and produces `obj.method(obj)` instead of `obj.method()`.

    We special-case the common pattern: if `callee` is a
    `MemberExpression` whose `.receiver` is structurally identical to
    the resolved `thisArg` value, the call is a plain method call and
    `thisArg` is dropped entirely (it's already implicit in
    `obj.method(...)`). Otherwise `this` isn't the callee's own
    receiver (e.g. `fn.call(otherThis, ...)`, or a bare function call
    where `thisArg` is `undefined`/unrelated) and must be preserved
    explicitly via `.call(thisArg, ...)` to keep semantics correct.
    """

    _PATTERN: Dict[int, "re.Pattern[str]"] = {
        n: sequence(*([REG] * (n + 2))) for n in (1, 2, 3, 4)
    }

    num_args = 1  # to be overridden

    def handle(self, analysis: HermesAnalysis, entry: OpcodeEntry) -> OpcodeResult:
        reg_pattern = self._PATTERN.get(self.num_args)
        if not reg_pattern:
            return self.build_invalid_args_result(analysis, entry)

        match = re.match(reg_pattern, entry.args.strip())
        if not match:
            return self.build_invalid_args_result(analysis, entry)

        dest_reg, func_reg, *arg_regs = (int(x) for x in match.groups())

        if not arg_regs:
            # No registers at all means not even a `this` slot was
            # encoded - shouldn't happen for a real CallN, but don't
            # crash on malformed input.
            return self.build_invalid_args_result(analysis, entry, "missing thisArg register")

        this_reg, *rest_arg_regs = arg_regs

        callee = self.get_register_expression(analysis, func_reg)
        this_value = self.get_register_expression(analysis, this_reg)
        real_arguments = tuple(
            self.get_register_expression(analysis, reg)
            for reg in rest_arg_regs
        )

        if isinstance(callee, MemberExpression) and callee.receiver.structurally_equal(this_value):
            # Plain `obj.method(...)` - `this` is already implicit.
            expression = CallExpression(callee=callee, arguments=real_arguments)

        # elif isinstance(this_value, UndefinedLiteral):
        #     # `this` explicitly undefined and unrelated to callee's receiver -
        #     # a bare call already has this=undefined in strict mode, so
        #     # `.call(undefined, ...)` is semantically redundant here.
        #     expression = CallExpression(callee=callee, arguments=real_arguments)

        else:
            # `this` doesn't match the callee's own receiver (or callee
            # isn't a member access at all) - preserve it explicitly.
            call_callee = MemberExpression(receiver=callee, member=Identifier(name="call"), computed=False)
            expression = CallExpression(callee=call_callee, arguments=(this_value, *real_arguments))

        result = OpcodeResult(entry, value=expression, dest_reg=dest_reg)
        analysis.add_result(result)

        return result


# Reg8, Reg8, Reg8, Reg8 (total size 4)
# DEFINE_OPCODE_4(Call2, Reg8, Reg8, Reg8, Reg8)
# Example: <Call2>: <Reg8: 3, Reg8: 4, Reg8: 5, Reg8: 3>
class Call2(Call1): num_args = 2


# Reg8, Reg8, Reg8, Reg8, Reg8 (total size 5)
# DEFINE_OPCODE_5(Call3, Reg8, Reg8, Reg8, Reg8, Reg8)
# Example: <Call3>: <Reg8: 7, Reg8: 7, Reg8: 9, Reg8: 8, Reg8: 10>
class Call3(Call1): num_args = 3


# Reg8, Reg8, Reg8, Reg8, Reg8, Reg8 (total size 6)
# DEFINE_OPCODE_6(Call4, Reg8, Reg8, Reg8, Reg8, Reg8, Reg8)
# Example: <Call4>: <Reg8: 0, Reg8: 4, Reg8: 7, Reg8: 2, Reg8: 0, Reg8: 1>
class Call4(Call1): num_args = 4
