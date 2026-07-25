from hermes_decompiler.handlers._shared_patterns import REG, UINT8, UINT16, sequence
from hermes_decompiler.ir import CallExpression, Identifier
from hermes_decompiler.models.HermesAnalysis import HermesAnalysis
from hermes_decompiler.models.OpcodeEntry import OpcodeEntry
from hermes_decompiler.models.OpcodeHandler import OpcodeHandler
from hermes_decompiler.models.OpcodeResult import OpcodeResult


# DEFINE_OPCODE_3(CallDirect, Reg8, UInt8, UInt16)
# DEFINE_RET_TARGET(CallDirect)
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
