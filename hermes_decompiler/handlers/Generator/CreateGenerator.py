from hermes_decompiler.ir import CallExpression, Identifier
from hermes_decompiler.models.HermesAnalysis import HermesAnalysis
from hermes_decompiler.models.OpcodeResult import OpcodeResult
from hermes_decompiler.models.JSVariable import JSVariable
from hermes_decompiler.models.OpcodeEntry import OpcodeEntry
from hermes_decompiler.models.OpcodeHandler import OpcodeHandler

from hermes_decompiler.handlers._shared_patterns import REG, FUNCTION_ID, sequence


# DEFINE_OPCODE_3(CreateGenerator, Reg8, Reg8, UInt16)
# DEFINE_OPCODE_3(CreateGeneratorLongIndex, Reg8, Reg8, UInt32)
# Example: <CreateGenerator>: <Reg8: 0, Reg8: 0, function_id: 11946> # Function: [#11946 ?anon_0_ of 251 bytes]: 2 params @ offset 0x002191ac
class CreateGenerator(OpcodeHandler):
    """Create a generator object."""

    _PATTERN = sequence(REG, REG, FUNCTION_ID)

    def handle(self, analysis: HermesAnalysis, entry: OpcodeEntry) -> OpcodeResult:
        handler = self.__class__.__name__

        match = self._PATTERN.match(entry.args.strip())
        if not match:
            return self.build_invalid_args_result(analysis, entry)

        dest_reg, env_reg, function_id = map(int, match.groups())
        env = self.get_register_value(analysis, env_reg)
        func_name = (entry.function.name if entry.function and entry.function.name else f"function_{function_id}")

        # Same named pseudo-call convention as createThis()/getEnvironment():
        # actually instantiating a generator object isn't plain JS syntax.
        value = CallExpression(
            callee=Identifier(name="createGenerator"),
            arguments=(env, Identifier(name=func_name)),
        )

        variable = JSVariable(handler, entry.address, f"r{dest_reg}", value)
        analysis.add_result(entry, variable)

        return OpcodeResult(entry, variable)


class CreateGeneratorLongIndex(CreateGenerator):
    """Long index variant."""

    pass


# DEFINE_OPCODE_3(CreateGeneratorClosure, Reg8, Reg8, UInt16)
# DEFINE_OPCODE_3(CreateGeneratorClosureLongIndex, Reg8, Reg8, UInt32)
# Example: <CreateGeneratorClosure>: <Reg8: 1, Reg8: 0, function_id: 11945>  # Function: [#11945  of 9 bytes]: 2 params @ offset 0x002191a3
class CreateGeneratorClosure(OpcodeHandler):
    """Create a closure for a GeneratorFunction."""

    _PATTERN = sequence(REG, REG, FUNCTION_ID)

    def handle(self, analysis: HermesAnalysis, entry: OpcodeEntry) -> OpcodeResult:
        handler = self.__class__.__name__

        match = self._PATTERN.match(entry.args.strip())
        if not match:
            return self.build_invalid_args_result(analysis, entry)

        dest_reg, env_reg, function_id = map(int, match.groups())

        func_name = (
            entry.function.name
            if entry.function and entry.function.name
            else f"function_{function_id}"
        )

        # Same treatment as CreateClosure: a closure over a generator
        # function is still just a name reference in real JS; the
        # captured environment register is dropped (see CreateClosure.py).
        value = Identifier(name=func_name)

        variable = JSVariable(handler, entry.address, f"r{dest_reg}", value)
        analysis.add_result(entry, variable)

        return OpcodeResult(entry, variable)


class CreateGeneratorClosureLongIndex(CreateGeneratorClosure):
    """Long index variant."""

    pass
