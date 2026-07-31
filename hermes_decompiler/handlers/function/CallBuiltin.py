from hermes_decompiler.handlers import OpcodeHandler, REG, UINT8, UINT32, sequence
from hermes_decompiler.ir.expressions import CallExpression, Identifier
from hermes_decompiler.opcode import OpcodeEntry, OpcodeResult
from hermes_decompiler.runtime import HermesAnalysis


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
    _PATTERN = sequence(REG, UINT8, UINT8)

    def handle(self, analysis: HermesAnalysis, entry: OpcodeEntry) -> OpcodeResult:
        match = self._PATTERN.match(entry.args.strip())
        if not match:
            return self.build_invalid_args_result(analysis, entry)

        dest_reg, builtin_id, arg_count = map(int, match.groups())

        callee = Identifier(
            name=entry.builtin_function.name
            if entry.builtin_function
            else f"builtin_{builtin_id}"
        )

        arguments = tuple(
            Identifier(name=f"r{reg}")
            for reg in range(dest_reg - arg_count, dest_reg)
        )

        expression = CallExpression(callee=callee, arguments=arguments, )

        result = OpcodeResult(entry, value=expression, dest_reg=dest_reg)
        analysis.add_result(result)

        return result


# Reg8, UInt8, UInt32 (total size 6)
# DEFINE_OPCODE_3(CallBuiltinLong, Reg8, UInt8, UInt32)
class CallBuiltinLong(CallBuiltin):
    _PATTERN = sequence(REG, UINT8, UINT32)
