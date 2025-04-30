import re

from HermesAssembly2JS.Hermes2JS.Models.HermesAnalysis import HermesAnalysis
from HermesAssembly2JS.Hermes2JS.Models.OpcodeResult import OpcodeResult
from HermesAssembly2JS.Hermes2JS.Models.JSVariable import JSVariable
from HermesAssembly2JS.Hermes2JS.Models.OpcodeEntry import OpcodeEntry
from HermesAssembly2JS.Hermes2JS.Models.OpcodeHandler import OpcodeHandler


# Load a function parameter by index. Starts at 0 with 'this'.
# Arg1 = Arg2 == 0 ? this : arguments[Arg2 - 1];
# DEFINE_OPCODE_2(LoadParam, Reg8, UInt8)
# Example: <LoadParam>: <Reg8: 1, UInt8: 1>
class LoadParam(OpcodeHandler):
    def Handle(self, analysis: HermesAnalysis, entry: OpcodeEntry) -> OpcodeResult:
        handler = self.__class__.__name__

        match = re.match(r'Reg8:\s*(\d+),\s*UInt8:\s*(\d+)', entry.args.strip())

        if not match:
            return self.InvalidArgs(entry)

        dest_reg, param_index = map(int, match.groups())

        variable = JSVariable(handler, entry.address, f'r{dest_reg}', f"param{param_index}")
        analysis.AddResult(entry, variable)

        return OpcodeResult(entry, variable)


class LoadConstString(OpcodeHandler):
    def Handle(self, analysis: HermesAnalysis, entry: OpcodeEntry) -> OpcodeResult:
        handler = self.__class__.__name__

        match = re.match(r'Reg8:\s*(\d+),\s*string_id:\s*(\d+)', entry.args.strip())

        if not match:
            return self.InvalidArgs(entry)

        dest_reg = int(match.group(1))
        string_id = match.group(2)

        # Try to resolve the actual string from analysis.stringMap
        const_value = analysis.stringTable.get(string_id, f'str_{string_id}')

        variable = JSVariable(handler, entry.address, f'r{dest_reg}', f'"{const_value}"')
        analysis.AddResult(entry, variable)

        return OpcodeResult(entry, variable)


class LoadConstUndefined(OpcodeHandler):
    def Handle(self, analysis: HermesAnalysis, entry: OpcodeEntry) -> OpcodeResult:
        handler = self.__class__.__name__

        match = re.match(r'Reg8:\s*(\d+)', entry.args.strip())

        if not match:
            return self.InvalidArgs(entry)

        dest_reg = int(match.group(1))

        variable = JSVariable(handler, entry.address, f'r{dest_reg}', f"undefined")
        analysis.AddResult(entry, variable)

        return OpcodeResult(entry, variable)
