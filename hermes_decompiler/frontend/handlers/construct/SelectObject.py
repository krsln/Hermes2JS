from hermes_decompiler.frontend.handlers import OpcodeHandler, OpcodeContext, ArgsPattern, sequence, REG
from hermes_decompiler.frontend.opcode import OpcodeResult
from hermes_decompiler.ir.expressions import (
    CallExpression,
    Identifier,
    MemberExpression,
    NewExpression,
    ThisPlaceholder,
)


# Reg8, Reg8, Reg8 (total size 3)
# DEFINE_OPCODE_3(SelectObject, Reg8, Reg8, Reg8)
# Example: <SelectObject>: <Reg8: 6, Reg8: 7, Reg8: 4>
class SelectObject(OpcodeHandler):
    """
    Selects between the newly created `this` object and the return value
    of a constructor. During decompilation, this can often be simplified
    to the underlying NewExpression.
    """

    ARGUMENTS = ArgsPattern(sequence(REG, REG, REG), "Reg8, Reg8, Reg8")

    def handle(self, ctx: OpcodeContext) -> OpcodeResult:

        match = self.match_arguments(ctx)
        if isinstance(match, OpcodeResult):
            return match

        dest_reg, obj_reg, selector_reg = map(int, match.groups())

        state_obj = ctx.analysis.get_register_state(obj_reg)
        state_selector = ctx.analysis.get_register_state(selector_reg)

        obj_value = state_obj.value if state_obj else None
        selector_value = state_selector.value if state_selector else None

        # If either operand is a NewExpression, unwrap the SelectObject layer
        # and preserve the NewExpression directly, matching JavaScript's `new`
        # constructor semantics.
        if state_selector and isinstance(selector_value, NewExpression):
            expression = selector_value
            state_selector.mark_read()
            state_selector.mark_used()
        elif (
                state_selector
                and isinstance(obj_value, ThisPlaceholder)
                and self._is_reflect_construct(selector_value)
        ):
            # `super(...)` (hermes 98): the freshly allocated `this` placeholder
            # versus what `Reflect.construct` returned - the latter is the
            # derived constructor's `this` from here on. Without this the pair
            # fell through to the computed-member fallback and printed
            # `CreateThisForSuper(r2)[r1]`.
            #
            # The call is NOT inlined here: statements run between the super
            # call and this SelectObject (`ThrowIfThisInitialized`, reads of
            # the constructor's own arguments, ...), so folding it would move
            # the call past them. It keeps its own statement (referencing the
            # register pins it) and this opcode becomes a plain alias of it.
            expression = self.get_register_reference(ctx.analysis, selector_reg)
            state_obj.mark_read()
            state_obj.mark_used()
        elif state_obj and isinstance(obj_value, NewExpression):
            expression = obj_value
            state_obj.mark_read()
            state_obj.mark_used()
        else:
            # Standard computed member access (fallback) | Hermes 98 -> CallExpression
            obj = self.get_register_expression(ctx.analysis, obj_reg)
            selector = self.get_register_expression(ctx.analysis, selector_reg)
            expression = MemberExpression(obj=obj, prop=selector, computed=True)

        result = OpcodeResult(ctx.entry, value=expression, dest_reg=dest_reg)
        ctx.analysis.add_result(result)

        return result

    @staticmethod
    def _is_reflect_construct(value) -> bool:
        """`Reflect.construct(...)`, the shape CallWithNewTarget produces."""
        callee = getattr(value, "callee", None)

        return (
                isinstance(value, CallExpression)
                and isinstance(callee, MemberExpression)
                and not callee.computed
                and isinstance(callee.obj, Identifier) and callee.obj.name == "Reflect"
                and isinstance(callee.prop, Identifier) and callee.prop.name == "construct"
        )
