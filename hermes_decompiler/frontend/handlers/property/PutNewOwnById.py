from hermes_decompiler.frontend.handlers import OpcodeContext, ArgsPattern, sequence, REG, STRING_ID
from hermes_decompiler.frontend.handlers.shared import fold_object_property, property_access
from hermes_decompiler.frontend.opcode import OpcodeResult
from hermes_decompiler.ir.Operators import AssignmentOperator
from hermes_decompiler.ir.expressions import AssignmentExpression, StringLiteral
from .PutById import PutById


# Reg8, Reg8, UInt16 (string_id) (total size 4)
# DEFINE_OPCODE_3(PutNewOwnById, Reg8, Reg8, UInt16)
# Example: <PutNewOwnById>: <Reg8: 15, Reg8: 2, string_id: 19648>  # String: 'silentJSONParsing' (Identifier)
class PutNewOwnById(PutById):
    """
    Set an existing own property identified at a slot index, and shared
    base implementation for `PutNewOwnByIdShort`/`PutNewOwnByIdLong` (which
    only differ in the string-id operand width, already handled
    uniformly by `STRING_ID`/`sequence(...)`). A real opcode is used as
    the shared base - see `Add` in `handlers/arithmetic/Binary.py` for the
    rationale.
    """

    ARGUMENTS = ArgsPattern(sequence(REG, REG, STRING_ID), "Reg8, Reg8, UInt16 (string_id)")

    def handle(self, ctx: OpcodeContext) -> OpcodeResult:
        match = self.match_arguments(ctx)
        if isinstance(match, OpcodeResult):
            return match

        obj_reg, value_reg, string_id = map(int, match.groups())

        property_name = ctx.entry.identifier_name or f"string_{string_id}"

        # Resolve the value first: inlining it marks its own definition as
        # folded, which the fold's "nothing printed since" check relies on.
        right = self.get_register_expression(ctx.analysis, value_reg)

        # `NewObject` + property stores -> one literal: `{ "x": a, "y": b }`
        # (string keys, like the literals `NewObjectWithBuffer` builds).
        folded = fold_object_property(ctx, obj_reg, StringLiteral(property_name), right)

        if folded is not None:
            return folded

        # Plain statement: `obj.name = value`. It defines nothing, so it
        # never changes what the object register holds.
        obj_value = self.get_register_expression(ctx.analysis, obj_reg)

        left = property_access(obj_value, property_name)
        expression = AssignmentExpression(left=left, operator=AssignmentOperator.ASSIGN, right=right)

        result = OpcodeResult(ctx.entry, value=expression, dest_reg=None)
        ctx.analysis.add_result(result)

        return result


# Reg8, Reg8, UInt8 (string_id) (total size 3)
# DEFINE_OPCODE_3(PutNewOwnByIdShort, Reg8, Reg8, UInt8)
# Example: <PutNewOwnByIdShort>: <Reg8: 1, Reg8: 0, string_id: 249>  # String: 'value' (Identifier)
class PutNewOwnByIdShort(PutNewOwnById):
    """Set an existing own property identified at a slot index."""
    pass


# Reg8, Reg8, UInt32 (string_id) (total size 6)
# DEFINE_OPCODE_3(PutNewOwnByIdLong, Reg8, Reg8, UInt32)
# Example:
class PutNewOwnByIdLong(PutNewOwnByIdShort):
    """Set an existing own property identified at a slot index."""
    pass
