import re

from hermes_decompiler.models.HermesAnalysis import HermesAnalysis
from hermes_decompiler.models.OpcodeResult import OpcodeResult
from hermes_decompiler.models.JSVariable import JSVariable
from hermes_decompiler.models.OpcodeEntry import OpcodeEntry
from hermes_decompiler.models.OpcodeHandler import OpcodeHandler

from ._shared_patterns import REG, FUNCTION_ID, ADDR, sequence

# Pre-compiled patterns
START_GENERATOR_PATTERN = re.compile(r'^(?:<>)?$')


# /// Start the generator by jumping to the next instruction to begin.
# /// Restore the stack frame if this generator has previously been suspended.
# DEFINE_OPCODE_0(StartGenerator)
# Example: <StartGenerator>: <>
class StartGenerator(OpcodeHandler):
    """Initialize generator execution."""

    def Handle(self, analysis: HermesAnalysis, entry: OpcodeEntry) -> OpcodeResult:
        handler = self.__class__.__name__

        if not START_GENERATOR_PATTERN.match(entry.args.strip()):
            return self.InvalidArgs(analysis, entry)

        variable = JSVariable(handler, entry.address, "",
                              f"// StartGenerator: prepare generator context and jump to next instruction")
        analysis.AddResult(entry, variable)

        return OpcodeResult(entry, variable)


# /// Resume generator by performing one of the following user-requested actions:
# /// - next(val): Set Arg1 to val, Arg2 to false, run next instruction
# /// - return(val): Set Arg1 to val, Arg2 to true, run next instruction
# /// - throw(val): Throw val as an error
# /// Arg1 is the result provided by the user.
# /// Arg2 is a boolean which is true if the user requested a return().
# DEFINE_OPCODE_2(ResumeGenerator, Reg8, Reg8)
# Example: <ResumeGenerator>: <Reg8: 0, Reg8: 2>
class ResumeGenerator(OpcodeHandler):
    """Resume a suspended generator."""
    _PATTERN = sequence(REG, REG)

    def Handle(self, analysis: HermesAnalysis, entry: OpcodeEntry) -> OpcodeResult:
        handler = self.__class__.__name__

        match = self._PATTERN.match(entry.args.strip())
        if not match:
            return self.InvalidArgs(analysis, entry)

        dest_reg, _flag_reg = map(int, match.groups())

        # Generate JavaScript: e.g., 'r0 = await yield;'
        variable = JSVariable(handler, entry.address, f'r{dest_reg}', f"await yield")
        analysis.AddResult(entry, variable)

        return OpcodeResult(entry, variable)


# /// Set the generator status to complete, but do not return.
# DEFINE_OPCODE_0(CompleteGenerator)
# Example: <CompleteGenerator>: <>
class CompleteGenerator(OpcodeHandler):
    """Mark generator as completed."""

    def Handle(self, analysis: HermesAnalysis, entry: OpcodeEntry) -> OpcodeResult:
        handler = self.__class__.__name__

        if not START_GENERATOR_PATTERN.match(entry.args.strip()):
            return self.InvalidArgs(analysis, entry)

        variable = JSVariable(handler, entry.address, "", f"// CompleteGenerator: No output needed")
        analysis.AddResult(entry, variable)

        return OpcodeResult(entry, variable)


# /// Unconditional branch to Arg1.
# DEFINE_JUMP_1(Jmp)
# /// Conditional branches to Arg1 based on Arg2.
# DEFINE_JUMP_2(JmpTrue)
# DEFINE_JUMP_2(JmpFalse)
# /// Jump if the value is undefined.
# DEFINE_JUMP_2(JmpUndefined)
# /// Save the provided value, yield, and signal the VM to restart execution at the provided target.
# DEFINE_JUMP_1(SaveGenerator)
# Example: <SaveGenerator>: <Addr8: 4>  # Address: 00000095
class SaveGenerator(OpcodeHandler):
    """Save generator state and yield."""
    _PATTERN = sequence(ADDR)

    def Handle(self, analysis: HermesAnalysis, entry: OpcodeEntry) -> OpcodeResult:
        handler = self.__class__.__name__

        match = self._PATTERN.match(entry.args.strip())
        if not match:
            return self.InvalidArgs(analysis, entry)

        addr = int(match.group(1))
        label = f"label_{addr}"
        analysis.gotoList.append(addr)  # TODO: ??

        variable = JSVariable(handler, entry.address, "",
                              f'yield {label};  // SaveGenerator: suspend and jump to {addr}')
        analysis.AddResult(entry, variable, goto=addr)

        return OpcodeResult(entry, variable, goto=addr)


# /// Create a generator.
# /// Arg1 is the register in which to store the generator.
# /// Arg2 is the current environment as loaded by GetEnvironment 0.
# /// Arg3 is index in the function table.
# DEFINE_OPCODE_3(CreateGenerator, Reg8, Reg8, UInt16)
# DEFINE_OPCODE_3(CreateGeneratorLongIndex, Reg8, Reg8, UInt32)
# OPERAND_FUNCTION_ID(CreateGenerator, 3)
# OPERAND_FUNCTION_ID(CreateGeneratorLongIndex, 3)
# Example: <CreateGenerator>: <Reg8: 0, Reg8: 0, function_id: 11946>  # Function: [#11946 ?anon_0_ of 251 bytes]: 2 params @ offset 0x002191ac
class CreateGenerator(OpcodeHandler):
    """Create a generator object."""
    _PATTERN = sequence(REG, REG, FUNCTION_ID)

    def Handle(self, analysis: HermesAnalysis, entry: OpcodeEntry) -> OpcodeResult:
        handler = self.__class__.__name__

        match = self._PATTERN.match(entry.args.strip())
        if not match:
            return self.InvalidArgs(analysis, entry)

        dest_reg, env_reg, function_id = map(int, match.groups())

        func_name = analysis.functionTable.get(str(function_id), f"gen_{function_id}")

        value = f"createGenerator(r{env_reg}, {func_name})"

        variable = JSVariable(handler, entry.address, f"r{dest_reg}", value)
        analysis.AddResult(entry, variable)

        return OpcodeResult(entry, variable)


class CreateGeneratorLongIndex(CreateGenerator):
    """Long index variant."""
    pass


# /// Create a closure for a GeneratorFunction.
# /// Arg1 is the register in which to store the closure.
# /// Arg2 is the current environment as loaded by GetEnvironment 0.
# /// Arg3 is index in the function table.
# DEFINE_OPCODE_3(CreateGeneratorClosure, Reg8, Reg8, UInt16)
# DEFINE_OPCODE_3(CreateGeneratorClosureLongIndex, Reg8, Reg8, UInt32)
# OPERAND_FUNCTION_ID(CreateGeneratorClosure, 3)
# OPERAND_FUNCTION_ID(CreateGeneratorClosureLongIndex, 3)
# Example: <CreateGeneratorClosure>: <Reg8: 1, Reg8: 0, function_id: 11945>  # Function: [#11945  of 9 bytes]: 2 params @ offset 0x002191a3
class CreateGeneratorClosure(OpcodeHandler):
    """Create a closure for a GeneratorFunction."""
    _PATTERN = sequence(REG, REG, FUNCTION_ID)

    def Handle(self, analysis: HermesAnalysis, entry: OpcodeEntry) -> OpcodeResult:
        handler = self.__class__.__name__

        match = self._PATTERN.match(entry.args.strip())
        if not match:
            return self.InvalidArgs(analysis, entry)

        dest_reg, env_reg, function_id = map(int, match.groups())

        func_name = analysis.functionTable.get(str(function_id), f"gen_{function_id}")

        value = f"createGeneratorClosure(r{env_reg}, {func_name})"

        variable = JSVariable(handler, entry.address, f"r{dest_reg}", value)
        analysis.AddResult(entry, variable)

        return OpcodeResult(entry, variable)


class CreateGeneratorClosureLongIndex(CreateGeneratorClosure):
    """Long index variant."""
    pass
