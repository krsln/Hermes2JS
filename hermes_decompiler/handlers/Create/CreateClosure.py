from hermes_decompiler.ir import Identifier
from hermes_decompiler.models.HermesAnalysis import HermesAnalysis
from hermes_decompiler.models.JSVariable import JSVariable
from hermes_decompiler.models.OpcodeEntry import OpcodeEntry
from hermes_decompiler.models.OpcodeHandler import OpcodeHandler
from hermes_decompiler.models.OpcodeResult import OpcodeResult

from hermes_decompiler.handlers._shared_patterns import REG, FUNCTION_ID, sequence


# DEFINE_OPCODE_3(CreateClosure, Reg8, Reg8, UInt16)
# DEFINE_OPCODE_3(CreateClosureLongIndex, Reg8, Reg8, UInt32)
# Example: <CreateClosure>: <Reg8: 3, Reg8: 1, function_id: 11944>  # Function: [#11944  of 37 bytes]: 1 params @ offset 0x0021917e
# Example: <CreateClosure>: <Reg8: 0, Reg8: 0, function_id: 11947>  # Function: [#11947 fetchMovies of 29 bytes]: 2 params @ offset 0x00150430
class CreateClosure(OpcodeHandler):
    """Creates a closure bound to the given environment register, resolving
    its display name from the function table (or a `function_N` fallback
    if the id isn't in the table)."""

    _PATTERN = sequence(REG, REG, FUNCTION_ID)

    def handle(self, analysis: HermesAnalysis, entry: OpcodeEntry) -> OpcodeResult:
        handler = self.__class__.__name__

        match = self._PATTERN.match(entry.args.strip())
        if not match:
            return self.build_invalid_args_result(analysis, entry, "Expected Reg8, Reg8 and function_id arguments")

        dest_reg, value_reg, func_id = (int(x) for x in match.groups())

        func_name = (
            entry.function.name
            if entry.function and entry.function.name
            else f"function_{func_id}"
        )

        # NOTE: `environment_register`/`environment` (the old
        # `ClosureValue`'s comment about which env the closure captures)
        # is dropped here. In real JS, a closure's environment capture
        # is implicit lexical scoping, not syntax - a plain reference to
        # the function name is the correct AST shape. The captured env
        # register is still visible in verbose mode via the `// CODE ->`
        # bytecode comment if needed for debugging.
        value = Identifier(name=func_name)

        variable = JSVariable(handler, entry.address, f"r{dest_reg}", value)
        analysis.add_result(entry, variable)

        return OpcodeResult(entry, variable)


class CreateClosureLongIndex(CreateClosure):
    def handle(self, analysis: HermesAnalysis, entry: OpcodeEntry) -> OpcodeResult:
        return super().handle(analysis, entry)