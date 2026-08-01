from hermes_decompiler.handlers import OpcodeHandler, REG, UINT8, UINT16, sequence, UINT32
from hermes_decompiler.ir.expressions import CallExpression, Identifier
from hermes_decompiler.opcode import OpcodeEntry, OpcodeResult
from hermes_decompiler.runtime import HermesAnalysis


# Reg8, UInt8, UInt16 (function_id) (total size 4)
# DEFINE_OPCODE_3(CallDirect, Reg8, UInt8, UInt16)
class CallDirect(OpcodeHandler):
    _PATTERN = sequence(REG, UINT8, UINT16)

    def handle(self, analysis: HermesAnalysis, entry: OpcodeEntry) -> OpcodeResult:
        match = self._PATTERN.match(entry.args.strip())
        if not match:
            return self.build_invalid_args_result(analysis, entry)

        dest_reg, arg_count, func_index = map(int, match.groups())

        func_name = (
            entry.function.name
            if entry.function and entry.function.name
            else f"function_{func_index}"
        )

        arguments = tuple(
            Identifier(name=f"r{dest_reg - arg_count + i}")
            for i in range(arg_count)
        )

        expression = CallExpression(callee=Identifier(name=func_name), arguments=arguments)

        result = OpcodeResult(entry, value=expression, dest_reg=dest_reg)
        analysis.add_result(result)

        return result


# Reg8, UInt8, UInt32 (total size 6)
class CallDirectLongIndex(CallDirect):
    _PATTERN = sequence(REG, UINT8, UINT32)
