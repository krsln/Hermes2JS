from hermes_decompiler.models.HermesAnalysis import HermesAnalysis
from hermes_decompiler.models.OpcodeResult import OpcodeResult
from hermes_decompiler.models.JSVariable import JSVariable
from hermes_decompiler.models.OpcodeEntry import OpcodeEntry
from hermes_decompiler.models.OpcodeHandler import OpcodeHandler

from hermes_decompiler.handlers._shared_patterns import REG, UINT8, sequence


# DEFINE_OPCODE_3(CallBuiltin, Reg8, UInt8, UInt8)
# Example: <CallBuiltin>: <Reg8: 3, UInt8: 12, UInt8: 2>
class CallBuiltin(OpcodeHandler):
    _PATTERN = sequence(REG, UINT8, UINT8)

    def handle(self, analysis: HermesAnalysis, entry: OpcodeEntry) -> OpcodeResult:
        handler = self.__class__.__name__

        match = self._PATTERN.match(entry.args.strip())
        if not match:
            return self.build_invalid_args_result(analysis, entry, "Expected Reg8, UInt8, UInt8 arguments")

        dest_reg, builtin_id, arg_count = map(int, match.groups())

        builtin_table = getattr(analysis, "builtinTable", None) or {}
        func_name = builtin_table.get(str(builtin_id), f"builtin_{builtin_id}")

        arg_start = dest_reg - arg_count
        args = []
        for offset, reg in enumerate(range(arg_start, dest_reg)):
            value = self.get_register_value(analysis, reg)
            args.append(value if value is not None else f"arg{offset}")

        args_str = ", ".join(args)
        func_val = f"({args_str})"

        variable = JSVariable(handler, entry.address, f"r{dest_reg}", f"{func_name}{func_val}", func_name, func_val)
        analysis.add_result(entry, variable)

        return OpcodeResult(entry, variable)
