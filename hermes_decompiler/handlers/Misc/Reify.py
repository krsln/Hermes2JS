from hermes_decompiler.models.HermesAnalysis import HermesAnalysis
from hermes_decompiler.models.OpcodeResult import OpcodeResult
from hermes_decompiler.models.JSVariable import JSVariable
from hermes_decompiler.models.OpcodeEntry import OpcodeEntry
from hermes_decompiler.models.OpcodeHandler import OpcodeHandler

from hermes_decompiler.handlers._shared_patterns import REG, sequence


# DEFINE_OPCODE_1(ReifyArguments, Reg8)
# Example: <ReifyArguments>: <Reg8: 0>
class ReifyArguments(OpcodeHandler):
    _PATTERN = sequence(REG)

    def handle(self, analysis: HermesAnalysis, entry: OpcodeEntry) -> OpcodeResult:
        handler = self.__class__.__name__

        # Parse arguments: expecting "Reg8: X"
        match = self._PATTERN.match(entry.args.strip())
        if not match:
            return self.build_invalid_args_result(analysis, entry, "Expected Reg8 argument")

        dest_reg = int(match.group(1))
        variable = JSVariable(handler, entry.address, f'r{dest_reg}', 'arguments')
        analysis.add_result(entry, variable)

        # Optionally, mark the creation of the argument object in analysis.
        # analysis.MarkArgumentsObject(entry.address, dest_reg)
        print("MarkArgumentsObject", entry.address, dest_reg)

        return OpcodeResult(entry, variable)


# DEFINE_OPCODE_2(GetArgumentsLength, Reg8, Reg8)
# Example: <GetArgumentsLength>: <Reg8: 1, Reg8: 0>
class GetArgumentsLength(OpcodeHandler):
    _PATTERN = sequence(REG, REG)

    def handle(self, analysis: HermesAnalysis, entry: OpcodeEntry) -> OpcodeResult:
        handler = self.__class__.__name__

        match = self._PATTERN.match(entry.args.strip())
        if not match:
            return self.build_invalid_args_result(analysis, entry, "Expected two Reg8 arguments")

        dest_reg, _lazy_reg = map(int, match.groups())

        variable = JSVariable(handler, entry.address, f"r{dest_reg}", "arguments.length")
        analysis.add_result(entry, variable)

        return OpcodeResult(entry, variable)


# DEFINE_OPCODE_3(GetArgumentsPropByVal, Reg8, Reg8, Reg8)
# Example: <GetArgumentsPropByVal>: <Reg8: 2, Reg8: 1, Reg8: 0>
class GetArgumentsPropByVal(OpcodeHandler):
    _PATTERN = sequence(REG, REG, REG)

    def handle(self, analysis: HermesAnalysis, entry: OpcodeEntry) -> OpcodeResult:
        handler = self.__class__.__name__

        match = self._PATTERN.match(entry.args.strip())
        if not match:
            return self.build_invalid_args_result(analysis, entry, "Expected three Reg8 arguments")

        dest_reg, index_reg, _lazy_reg = map(int, match.groups())
        index_val = self.get_register_value(analysis, index_reg) or f"r{index_reg}"

        variable = JSVariable(handler, entry.address, f"r{dest_reg}", f"arguments[{index_val}]")
        analysis.add_result(entry, variable)

        return OpcodeResult(entry, variable)
