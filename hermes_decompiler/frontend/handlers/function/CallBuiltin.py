from hermes_decompiler.frontend.opcode import OpcodeResult
from frontend.handlers import OpcodeHandler, OpcodeContext, ArgsPattern, sequence, REG, UINT8, UINT32
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

        # CallBuiltin's arguments are NOT relative to dest_reg. Per the
        # Hermes bytecode spec, they are "found in reverse order from the
        # end of the current frame" - i.e. they occupy the arg_count
        # registers ending at the highest register index written so far
        # in this function, with the first logical argument at the
        # highest register and later arguments at lower ones (confirmed
        # against the native builtin signatures, e.g.
        # copyDataProperties(target, source, excludedItems) - target ends
        # up at the topmost register). dest_reg can be small/unrelated
        # (it's just where the return value lands), so anchoring on it -
        # as CallDirect correctly does for its own, different, calling
        # convention - produces wrong or even negative register indices
        # here. `Call` (handlers/function/Call.py) already resolves the
        # analogous case correctly; this mirrors that approach.
        highest = max(
            (int(r[1:]) for r in ctx.analysis.registers),
            default=dest_reg,
        )

        arguments = tuple(
            Identifier(name=f"r{reg}")
            for reg in range(highest, highest - arg_count, -1)
        )

        expression = CallExpression(callee=callee, arguments=arguments, )

        result = OpcodeResult(ctx.entry, value=expression, dest_reg=dest_reg)
        ctx.analysis.add_result(result)

        return result


# Reg8, UInt8, UInt32 (total size 6)
# DEFINE_OPCODE_3(CallBuiltinLong, Reg8, UInt8, UInt32)
class CallBuiltinLong(CallBuiltin):
    ARGUMENTS = ArgsPattern(sequence(REG, UINT8, UINT32), "Reg8, UInt8, UInt32")
