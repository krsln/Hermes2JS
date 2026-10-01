from hermes_decompiler.frontend.handlers import OpcodeHandler, OpcodeContext, ArgsPattern, sequence, REG, UINT8
from hermes_decompiler.frontend.opcode import OpcodeResult
from hermes_decompiler.ir.Operators import AssignmentOperator
from hermes_decompiler.ir.expressions import AssignmentExpression, MemberExpression, Identifier


def _resolve_private_field_name(ctx: OpcodeContext, private_name_reg: int) -> str:
    """
    The real `#fieldName` for `private_name_reg`, if PrivateNameTable can
    resolve it - the `__private_N__` numeric placeholder otherwise.

    `ctx.entry.identifier_name` (checked first, matching every other
    handler that falls back to it) never actually fires for any of the
    three opcodes that call this: none of AddOwnPrivateBySym/
    GetOwnPrivateBySym/PutOwnPrivateBySym encodes a string_id operand at
    all (see each one's own ARGUMENTS - all plain registers), so there is
    never a disassembler identifier-comment to read here in the first
    place. Kept as the first check anyway for the same reason every other
    `field_name`-style fallback in this codebase does: cheap, and correct
    if a future Hermes version ever changes that encoding.

    The real recovery path is PrivateNameTable, keyed by the (depth,
    slot) `private_name_reg` was loaded from - see
    OpcodeResult.env_source and LoadFromEnvironment.py/Mov.py for how
    that's carried forward from whichever LoadFromEnvironment actually
    produced this register's value, possibly several instructions (and
    Movs) earlier.
    """
    if ctx.entry.identifier_name:
        return ctx.entry.identifier_name

    state = ctx.analysis.get_register_state(private_name_reg)
    env_source = state.definition.env_source if state else None

    if env_source is not None and ctx.function_id is not None and ctx.batch_tables is not None:
        depth, slot = env_source
        name = ctx.batch_tables.private_name_table.name_for(ctx.function_id, depth, slot)

        if name is not None:
            # PrivateNameTable's own names already carry the leading
            # "#" (see CreatePrivateName.py's identifier_name comment) -
            # every call site below adds its own "#" prefix, so strip it
            # back off here rather than have two different `field_name`
            # conventions (one with the "#", one without) depending on
            # which fallback fired.
            return name[1:] if name.startswith("#") else name

    return f"__private_{private_name_reg}__"


# Reg8, Reg8, Reg8 (total size 3)
# DEFINE_OPCODE_3(AddOwnPrivateBySym, Reg8, Reg8, Reg8)
# Example: <AddOwnPrivateBySym>: <Reg8: 4, Reg8: 3, Reg8: 7>
class AddOwnPrivateBySym(OpcodeHandler):
    """Initialize a private class field on a fresh instance: obj.#field = value."""

    ARGUMENTS = ArgsPattern(sequence(REG, REG, REG), "Reg8, Reg8, Reg8 (total size 3)")

    def handle(self, ctx: OpcodeContext) -> OpcodeResult:
        match = self.match_arguments(ctx)
        if isinstance(match, OpcodeResult):
            return match

        obj_reg, private_name_reg, value_reg = map(int, match.groups())

        field_name = _resolve_private_field_name(ctx, private_name_reg)

        left = MemberExpression(
            obj=self.get_register_expression(ctx.analysis, obj_reg),
            prop=Identifier(name=f"#{field_name}"),
            computed=False,
        )
        right = self.get_register_expression(ctx.analysis, value_reg)

        expression = AssignmentExpression(left=left, operator=AssignmentOperator.ASSIGN, right=right)

        result = OpcodeResult(ctx.entry, value=expression, dest_reg=None)
        ctx.analysis.add_result(result)

        return result


# Reg8, Reg8, UInt8, Reg8 (total size 4)
# DEFINE_OPCODE_4(GetOwnPrivateBySym, Reg8, Reg8, UInt8, Reg8)
# <GetOwnPrivateBySym>: <Reg8: 7, Reg8: 5, UInt8: 0, Reg8: 4>
class GetOwnPrivateBySym(OpcodeHandler):
    """Read a private class field: obj.#field"""

    ARGUMENTS = ArgsPattern(sequence(REG, REG, UINT8, REG), "Reg8, Reg8, UInt8, Reg8 (total size 4)")

    def handle(self, ctx: OpcodeContext) -> OpcodeResult:
        match = self.match_arguments(ctx)
        if isinstance(match, OpcodeResult):
            return match

        dest_reg, obj_reg, _cache, private_name_reg = map(int, match.groups())

        field_name = _resolve_private_field_name(ctx, private_name_reg)

        expression = MemberExpression(
            obj=self.get_register_expression(ctx.analysis, obj_reg),
            prop=Identifier(name=f"#{field_name}"),
            computed=False,
        )

        result = OpcodeResult(ctx.entry, value=expression, dest_reg=dest_reg)
        ctx.analysis.add_result(result)

        return result


# Reg8, Reg8, UInt8, Reg8 (total size 4)
# DEFINE_OPCODE_4(PutOwnPrivateBySym, Reg8, Reg8, UInt8, Reg8)
# <PutOwnPrivateBySym>: <Reg8: 4, Reg8: 5, UInt8: 1, Reg8: 6>
class PutOwnPrivateBySym(OpcodeHandler):
    """Write a private class field on an already-initialized instance: obj.#field = value"""

    ARGUMENTS = ArgsPattern(sequence(REG, REG, UINT8, REG), "Reg8, Reg8, UInt8, Reg8 (total size 4)")

    def handle(self, ctx: OpcodeContext) -> OpcodeResult:
        match = self.match_arguments(ctx)
        if isinstance(match, OpcodeResult):
            return match

        obj_reg, value_reg, _cache, private_name_reg = map(int, match.groups())

        field_name = _resolve_private_field_name(ctx, private_name_reg)

        left = MemberExpression(
            obj=self.get_register_expression(ctx.analysis, obj_reg),
            prop=Identifier(name=f"#{field_name}"),
            computed=False,
        )
        right = self.get_register_expression(ctx.analysis, value_reg)

        expression = AssignmentExpression(left=left, operator=AssignmentOperator.ASSIGN, right=right)

        result = OpcodeResult(ctx.entry, value=expression, dest_reg=None)
        ctx.analysis.add_result(result)

        return result
