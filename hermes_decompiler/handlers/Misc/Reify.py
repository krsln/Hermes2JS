from hermes_decompiler.models.HermesAnalysis import HermesAnalysis
from hermes_decompiler.models.OpcodeResult import OpcodeResult
from hermes_decompiler.models.JSVariable import JSVariable
from hermes_decompiler.models.OpcodeEntry import OpcodeEntry
from hermes_decompiler.models.OpcodeHandler import OpcodeHandler

from hermes_decompiler.handlers._shared_patterns import REG, sequence


# /// Create an actual 'arguments' array, if get-by-index and length isn't enough.
# /// Arg1 is the lazy loaded register, which afterwards will contain a proper
# ///      object that can be used by non-*Arguments* opcodes like Return.
# DEFINE_OPCODE_1(ReifyArguments, Reg8)
# Example: <ReifyArguments>: <Reg8: 0>
class ReifyArguments(OpcodeHandler):
    _PATTERN = sequence(REG)

    def Handle(self, analysis: HermesAnalysis, entry: OpcodeEntry) -> OpcodeResult:
        handler = self.__class__.__name__

        # Parse arguments: expecting "Reg8: X"
        match = self._PATTERN.match(entry.args.strip())
        if not match:
            return self.InvalidArgs(analysis, entry, "Expected Reg8 argument")

        # Extract destination register
        dest_reg = int(match.group(1))

        # Create JSVariable for the arguments object
        variable = JSVariable(handler, entry.address, f'r{dest_reg}', 'arguments')
        analysis.AddResult(entry, variable)

        # Optionally, mark the creation of the argument object in analysis.
        # analysis.MarkArgumentsObject(entry.address, dest_reg)
        print("MarkArgumentsObject", entry.address, dest_reg)

        return OpcodeResult(entry, variable)


# /// Arg1 = arguments.length, without materializing a full arguments object
# /// (that's what ReifyArguments is for — this is the cheap fast path).
# /// Arg2 is the VM's internal "lazy register" tracking the current frame's
# /// arguments; it doesn't correspond to a source-level value on its own.
# ///
# /// ⚠️ Operand layout reconstructed from general knowledge of Hermes's
# /// arguments-object opcodes, not a verified disassembly sample — confirm
# /// against a real `<GetArgumentsLength>` line before relying on this.
# DEFINE_OPCODE_2(GetArgumentsLength, Reg8, Reg8)
# Example: <GetArgumentsLength>: <Reg8: 1, Reg8: 0>
class GetArgumentsLength(OpcodeHandler):
    _PATTERN = sequence(REG, REG)

    def Handle(self, analysis: HermesAnalysis, entry: OpcodeEntry) -> OpcodeResult:
        handler = self.__class__.__name__

        match = self._PATTERN.match(entry.args.strip())
        if not match:
            return self.InvalidArgs(analysis, entry, "Expected two Reg8 arguments")

        dest_reg, _lazy_reg = map(int, match.groups())

        variable = JSVariable(handler, entry.address, f"r{dest_reg}", "arguments.length")
        analysis.AddResult(entry, variable)

        return OpcodeResult(entry, variable)


# /// Arg1 = arguments[Arg2] — same fast-path idea as GetArgumentsLength:
# /// index into the arguments frame without reifying a full object first.
# /// Arg3 is the VM's lazy register for the current frame's arguments.
# ///
# /// ⚠️ Same verification caveat as GetArgumentsLength above.
# DEFINE_OPCODE_3(GetArgumentsPropByVal, Reg8, Reg8, Reg8)
# Example: <GetArgumentsPropByVal>: <Reg8: 2, Reg8: 1, Reg8: 0>
class GetArgumentsPropByVal(OpcodeHandler):
    _PATTERN = sequence(REG, REG, REG)

    def Handle(self, analysis: HermesAnalysis, entry: OpcodeEntry) -> OpcodeResult:
        handler = self.__class__.__name__

        match = self._PATTERN.match(entry.args.strip())
        if not match:
            return self.InvalidArgs(analysis, entry, "Expected three Reg8 arguments")

        dest_reg, index_reg, _lazy_reg = map(int, match.groups())
        index_val = self.GetValueByReg(analysis, index_reg) or f"r{index_reg}"

        variable = JSVariable(handler, entry.address, f"r{dest_reg}", f"arguments[{index_val}]")
        analysis.AddResult(entry, variable)

        return OpcodeResult(entry, variable)
