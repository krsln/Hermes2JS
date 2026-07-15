from hermes_decompiler.models.HermesAnalysis import HermesAnalysis
from hermes_decompiler.models.JSVariable import JSVariable
from hermes_decompiler.models.OpcodeEntry import OpcodeEntry
from hermes_decompiler.models.OpcodeHandler import OpcodeHandler
from hermes_decompiler.models.OpcodeResult import OpcodeResult

from hermes_decompiler.handlers._shared_patterns import REG, FUNCTION_ID, sequence


# /// Create a closure.
# /// Arg1 is the register in which to store the closure.
# /// Arg2 is the current environment as loaded by GetEnvironment 0.
# /// Arg3 is index in the function table.
# DEFINE_OPCODE_3(CreateClosure, Reg8, Reg8, UInt16)
# DEFINE_OPCODE_3(CreateClosureLongIndex, Reg8, Reg8, UInt32)
# OPERAND_FUNCTION_ID(CreateClosure, 3)
# OPERAND_FUNCTION_ID(CreateClosureLongIndex, 3)
# Example: <CreateClosure>: <Reg8: 3, Reg8: 1, function_id: 11944>  # Function: [#11944  of 37 bytes]: 1 params @ offset 0x0021917e
# Example: <CreateClosure>: <Reg8: 0, Reg8: 0, function_id: 11947>  # Function: [#11947 fetchMovies of 29 bytes]: 2 params @ offset 0x00150430
class CreateClosure(OpcodeHandler):
    """Creates a closure bound to the given environment register, resolving
    its display name from the function table (or a `function_N` fallback
    if the id isn't in the table)."""

    _PATTERN = sequence(REG, REG, FUNCTION_ID)

    def Handle(self, analysis: HermesAnalysis, entry: OpcodeEntry) -> OpcodeResult:
        handler = self.__class__.__name__

        match = self._PATTERN.match(entry.args.strip())
        if not match:
            return self.InvalidArgs(analysis, entry, "Expected Reg8, Reg8 and function_id arguments")

        dest, env, func_id = (int(x) for x in match.groups())

        func_name = analysis.functionTable.get(str(func_id), f"function_{func_id}")

        env_var = self.GetVariableByReg(analysis.results, env)
        env_value = env_var.value if env_var and env_var.value else 'undefined'
        # print(env, env_value)

        # Simplified closure representation
        variable = JSVariable(
            handler,
            entry.address,
            f'r{dest}',
            f"{func_name} /* Closure with env r{env} = {env_value} */",
        )
        analysis.AddResult(entry, variable)

        return OpcodeResult(entry, variable)


# The long-index variant only differs in the function_id operand's on-disk
# width (UInt32 instead of UInt16); the disassembler still labels it
# `function_id:` either way, so the shared FUNCTION_ID pattern already
# covers both and no logic needs to change.
#
# NOTE: this class was documented in the header comment above but never
# actually defined/registered in the original file — CreateClosureLongIndex
# opcodes would have silently fallen through to "no handler found" during
# dispatch. Added here to close that gap.
class CreateClosureLongIndex(CreateClosure):
    def Handle(self, analysis: HermesAnalysis, entry: OpcodeEntry) -> OpcodeResult:
        return super().Handle(analysis, entry)
