from hermes_decompiler.frontend.opcode import OpcodeResult
from frontend.handlers import OpcodeHandler, OpcodeContext, ArgsPattern, sequence, REG, FUNCTION_ID
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

        function_info = ctx.entry.function

        if function_info is not None:
            params = (
                ", ".join(f"param{i}" for i in range(1, function_info.param_count))
                if function_info.param_count is not None
                else ""
            )

            name = function_info.name or f"function_{func_id}"
            function = f"{name}({params})"
        else:
            function = f"function_{func_id}"

        # NOTE: The environment register is intentionally not represented in
        # the JavaScript expression. It identifies the lexical environment
        # captured by the closure at the bytecode level, while lexical
        # environment capture is implicit in JavaScript syntax.
        #
        # Therefore, the closure is represented by its function reference;
        # the captured environment does not require a separate AST node.
        expression = Identifier(name=function)

        result = OpcodeResult(ctx.entry, value=expression, dest_reg=dest_reg)
        ctx.analysis.add_result(result)

        return result


# Reg8, Reg8, UInt32 (function_id) (total size 6)
# DEFINE_OPCODE_3(CreateClosureLongIndex, Reg8, Reg8, UInt32)
class CreateClosureLongIndex(CreateClosure):
    def handle(self, ctx: OpcodeContext) -> OpcodeResult:
        return super().handle(ctx)
