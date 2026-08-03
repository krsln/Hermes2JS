from hermes_decompiler.frontend.opcode import OpcodeEntry, OpcodeResult
from hermes_decompiler.handlers import sequence, REG, FUNCTION_ID
from hermes_decompiler.handlers.OpcodeHandler import OpcodeHandler
from hermes_decompiler.ir.expressions import CallExpression, Identifier
from hermes_decompiler.runtime import HermesAnalysis


# Reg8, Reg8, UInt16 (function_id) (total size 4)
# DEFINE_OPCODE_3(CreateGenerator, Reg8, Reg8, UInt16)
# Example: <CreateGenerator>: <Reg8: 0, Reg8: 0, function_id: 11946> # Function: [#11946 ?anon_0_ of 251 bytes]: 2 params @ offset 0x002191ac
class CreateGenerator(OpcodeHandler):
    """Create a generator object."""

    _PATTERN = sequence(REG, REG, FUNCTION_ID)

    def handle(self, analysis: HermesAnalysis, entry: OpcodeEntry) -> OpcodeResult:
        match = self._PATTERN.match(entry.args.strip())
        if not match:
            return self.build_invalid_args_result(analysis, entry)

        dest_reg, env_reg, function_id = map(int, match.groups())
        env = self.get_register_expression(analysis, env_reg)
        func_name = (entry.function.name if entry.function and entry.function.name else f"function_{function_id}")

        # Same named pseudo-call convention as createThis()/getEnvironment():
        # actually instantiating a generator object isn't plain JS syntax.
        expression = CallExpression(
            callee=Identifier(name="createGenerator"),
            arguments=(env, Identifier(name=func_name)),
        )

        result = OpcodeResult(entry, value=expression, dest_reg=dest_reg)
        analysis.add_result(result)

        return result


# Reg8, Reg8, UInt32 (function_id) (total size 6)
# DEFINE_OPCODE_3(CreateGeneratorLongIndex, Reg8, Reg8, UInt32)
class CreateGeneratorLongIndex(CreateGenerator):
    """Long index variant."""

    pass


# Reg8, Reg8, UInt16 (function_id) (total size 4)
# DEFINE_OPCODE_3(CreateGeneratorClosure, Reg8, Reg8, UInt16)
# Example: <CreateGeneratorClosure>: <Reg8: 1, Reg8: 0, function_id: 11945>  # Function: [#11945  of 9 bytes]: 2 params @ offset 0x002191a3
class CreateGeneratorClosure(OpcodeHandler):
    """Create a closure for a GeneratorFunction."""

    _PATTERN = sequence(REG, REG, FUNCTION_ID)

    def handle(self, analysis: HermesAnalysis, entry: OpcodeEntry) -> OpcodeResult:
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
        expression = Identifier(name=func_name)

        result = OpcodeResult(entry, value=expression, dest_reg=dest_reg)
        analysis.add_result(result)

        return result


# Reg8, Reg8, UInt32 (function_id) (total size 6)
# DEFINE_OPCODE_3(CreateGeneratorClosureLongIndex, Reg8, Reg8, UInt32)
class CreateGeneratorClosureLongIndex(CreateGeneratorClosure):
    """Long index variant."""

    pass
