from hermes_decompiler.core.Naming import to_js_identifier
from hermes_decompiler.frontend.handlers import OpcodeHandler, OpcodeContext, ArgsPattern, sequence, REG, FUNCTION_ID
from hermes_decompiler.frontend.opcode import OpcodeResult
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
            name = function_info.name or f"function_{func_id}"
            # name comes straight from the function table and isn't
            # guaranteed to be a valid JS identifier - e.g. an
            # anonymous generator/async body is named "?anon_0_..."
            # (see hermes_decompiler.core.Naming for why).
            #
            # The value is the BARE function name - a reference, not a
            # call. It used to carry an arity annotation baked into the
            # name (`sideEffect(param1, param2)`), which made every closure
            # read as a call: `param6.ifTest = ifTest(param1)` (a
            # reference assignment), and `sideEffect(param1, param2)(
            # "and-left", param1)` once the closure was actually called.
            function = to_js_identifier(name)
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
