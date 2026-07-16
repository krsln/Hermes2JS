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

    def Handle(self, analysis: HermesAnalysis, entry: OpcodeEntry) -> OpcodeResult:
        handler = self.__class__.__name__

        match = self._PATTERN.match(entry.args.strip())
        if not match:
            return self.InvalidArgs(analysis, entry)

        dest_reg = int(match.group(2))
        arg_count = int(match.group(3))
        func_index = int(match.group(4))

        func_name = analysis.functionTable.get(str(func_index), f"function_{func_index}")
        args = [f"arg{i}" for i in range(arg_count)]
        args_str = ", ".join(args)
        func_val = f"{func_name}({args_str})"

        variable = JSVariable(handler, entry.address, f"r{dest_reg}", func_val, func_name, func_val)
        analysis.AddResult(entry, variable)

        return OpcodeResult(entry, variable)
