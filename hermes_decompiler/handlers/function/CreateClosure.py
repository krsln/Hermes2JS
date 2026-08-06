from hermes_decompiler.frontend.opcode import OpcodeResult
from hermes_decompiler.handlers import OpcodeHandler, OpcodeContext, ArgsPattern, sequence, REG, FUNCTION_ID
from hermes_decompiler.ir.expressions import Identifier


# Reg8, Reg8, UInt16 (function_id) (total size 4)
# DEFINE_OPCODE_3(CreateClosure, Reg8, Reg8, UInt16)
# Example: <CreateClosure>: <Reg8: 0, Reg8: 0, function_id: 11947>  # Function: [#11947 fetchMovies of 29 bytes]: 2 params @ offset 0x00150430
class CreateClosure(OpcodeHandler):
    """Creates a closure bound to the given environment register, resolving
    its display name from the function table (or a `function_N` fallback
    if the id isn't in the table)."""

    ARGUMENTS = ArgsPattern(sequence(REG, REG, FUNCTION_ID), "Reg8, Reg8, UInt16 (function_id)")

    def handle(self, ctx: OpcodeContext) -> OpcodeResult:
        match = self.match_arguments(ctx)
        if isinstance(match, OpcodeResult):
            return match

        dest_reg, value_reg, func_id = (int(x) for x in match.groups())

        func_name = (
            ctx.entry.function.name
            if ctx.entry.function and ctx.entry.function.name
            else f"function_{func_id}"
        )

        # NOTE: `environment_register`/`environment` (the old
        # `ClosureValue`'s comment about which env the closure captures)
        # is dropped here. In real JS, a closure's environment capture
        # is implicit lexical scoping, not syntax - a plain reference to
        # the function name is the correct AST shape. The captured env
        # register is still visible in verbose mode via the `// CODE ->`
        # bytecode comment if needed for debugging.
        expression = Identifier(name=func_name)

        result = OpcodeResult(ctx.entry, value=expression, dest_reg=dest_reg)
        ctx.analysis.add_result(result)

        return result


# Reg8, Reg8, UInt32 (function_id) (total size 6)
# DEFINE_OPCODE_3(CreateClosureLongIndex, Reg8, Reg8, UInt32)
class CreateClosureLongIndex(CreateClosure):
    def handle(self, ctx: OpcodeContext) -> OpcodeResult:
        return super().handle(ctx)
