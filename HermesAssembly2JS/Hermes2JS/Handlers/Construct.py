import re

from Hermes2JS.Models.HermesAnalysis import HermesAnalysis
from Hermes2JS.Models.OpcodeResult import OpcodeResult
from Hermes2JS.Models.JSVariable import JSVariable
from Hermes2JS.Models.OpcodeEntry import OpcodeEntry
from Hermes2JS.Models.OpcodeHandler import OpcodeHandler


class Construct(OpcodeHandler):
    def Handle(self, analysis: HermesAnalysis, entry: OpcodeEntry) -> OpcodeResult:
        handler = self.__class__.__name__

        # Match: Reg8 (dest), Reg8 (closure to invoke), UInt8 (arg count)
        match = re.match(r'Reg8:\s*(\d+),\s*Reg8:\s*(\d+),\s*UInt8:\s*(\d+)', entry.args.strip())

        if not match:
            return self.InvalidArgs(entry)

        dest_reg, func_reg, arg_count = map(int, match.groups())

        # Reverse-order args: usually preloaded into registers before this
        args = [f"arg{i}" for i in range(arg_count)]
        args_str = ", ".join(args)

        func_name = f'new r{func_reg}'
        func_val = f"({args_str})"

        variable = JSVariable(handler, entry.address, f'r{dest_reg}', f"{func_name}{func_val};", func_name, func_val)
        analysis.AddResult(entry, variable)

        return OpcodeResult(entry, variable)
