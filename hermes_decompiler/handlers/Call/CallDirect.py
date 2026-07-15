from hermes_decompiler.models.HermesAnalysis import HermesAnalysis
from hermes_decompiler.models.OpcodeResult import OpcodeResult
from hermes_decompiler.models.JSVariable import JSVariable
from hermes_decompiler.models.OpcodeEntry import OpcodeEntry
from hermes_decompiler.models.OpcodeHandler import OpcodeHandler

from hermes_decompiler.handlers._shared_patterns import REG, UINT8, UINT16, sequence


# /// Call a function directly without a closure.
# /// Arg1 is the destination of the return value.
# /// Arg2 is the number of arguments, assumed to be found in reverse order
# ///      from the end of the current frame. The first argument 'this'
# ///      is assumed to be created with CreateThis.
# /// Arg3 is index in the function table.
# DEFINE_OPCODE_3(CallDirect, Reg8, UInt8, UInt16)
# OPERAND_FUNCTION_ID(CallDirect, 3)
# DEFINE_RET_TARGET(CallDirect)
class CallDirect(OpcodeHandler):
    _PATTERN = sequence(REG, UINT8, UINT16)

    def Handle(self, analysis: HermesAnalysis, entry: OpcodeEntry) -> OpcodeResult:
        handler = self.__class__.__name__

        # Parse args: Reg8, UInt8, UInt16
        match = self._PATTERN.match(entry.args.strip())
        if not match:
            return self.InvalidArgs(analysis, entry)

        dest_reg = int(match.group(2))
        arg_count = int(match.group(3))
        func_index = int(match.group(4))

        # Lookup the function name from function index table, assume it's stored in analysis context
        func_name = analysis.functionTable.get(str(func_index), f"function_{func_index}")

        # Get arguments from the frame, assume `GetArgsFromFrame` helper exists or can be implemented
        args = [f"arg{i}" for i in range(arg_count)]
        args_str = ", ".join(args)

        func_val = f"{func_name}({args_str})"
        variable = JSVariable(handler, entry.address, f"r{dest_reg}", func_val, func_name, func_val)
        analysis.AddResult(entry, variable)

        return OpcodeResult(entry, variable)
