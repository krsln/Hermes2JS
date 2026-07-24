from hermes_decompiler.ir.Expressions import CallExpression
from hermes_decompiler.ir.Values import RegisterValue, IdentifierValue
from hermes_decompiler.models.HermesAnalysis import HermesAnalysis
from hermes_decompiler.models.OpcodeResult import OpcodeResult
from hermes_decompiler.models.JSVariable import JSVariable
from hermes_decompiler.models.OpcodeEntry import OpcodeEntry
from hermes_decompiler.models.OpcodeHandler import OpcodeHandler

from hermes_decompiler.handlers._shared_patterns import REG, UINT8, UINT16, sequence


# DEFINE_OPCODE_3(CallDirect, Reg8, UInt8, UInt16)
# DEFINE_RET_TARGET(CallDirect)
class CallDirect(OpcodeHandler):
    _PATTERN = sequence(REG, UINT8, UINT16)

    def handle(self, analysis: HermesAnalysis, entry: OpcodeEntry) -> OpcodeResult:
        handler = self.__class__.__name__

        match = self._PATTERN.match(entry.args.strip())
        if not match:
            return self.build_invalid_args_result(analysis, entry)

        dest_reg, arg_count, func_index = map(int, match.groups())

        func_name = (
            entry.function.name
            if entry.function and entry.function.name
            else f"function_{func_index}"
        )

        arguments = [
            RegisterValue(dest_reg - arg_count + i)
            for i in range(arg_count)
        ]
        value = CallExpression(callee=IdentifierValue(func_name), arguments=arguments)

        variable = JSVariable(handler, entry.address, f"r{dest_reg}", value)
        analysis.add_result(entry, variable)

        return OpcodeResult(entry, variable)
