from hermes_decompiler.frontend.opcode import OpcodeResult
from frontend.handlers import OpcodeHandler, OpcodeContext, ArgsPattern, sequence, REG, UINT16, UINT32
from hermes_decompiler.ir.expressions import (
    ArrayExpression,
    Expression,
    ObjectExpression,
    ObjectProperty,
    StringLiteral,
    python_literal,
)


def _json_to_expression(value: object) -> Expression:
    """
    Recursively convert a parsed JSON value (from an opcode comment) into
    the matching `ir` expression, including nested objects/arrays.
    """

    if isinstance(value, dict):
        properties = tuple(
            ObjectProperty(key=StringLiteral(k), value=_json_to_expression(v))
            for k, v in value.items()
        )
        return ObjectExpression(properties=properties)

    if isinstance(value, list):
        return ArrayExpression(elements=tuple(_json_to_expression(v) for v in value))

    return python_literal(value)


# Reg8, UInt16, UInt16 (total size 5)
# DEFINE_OPCODE_5(NewObjectWithBuffer, Reg8, UInt16, UInt16, UInt16, UInt16)
# DEFINE_OPCODE_3(NewObjectWithBuffer, Reg8, UInt16, UInt16)
# Example: <NewObjectWithBuffer>: <Reg8: 7, UInt16: 27, UInt16: 17989>  # Object: {'enumerable': true, 'get': null}
# Example: <NewObjectWithBuffer>: <Reg8: 37, UInt16: 9, UInt16: 9, UInt16: 194, UInt16: 115>  # Object: {'type': null, 'target': null, 'currentTarget': null, 'eventPhase': null, 'bubbles': null, 'cancelable': null, 'timeStamp': null, 'defaultPrevented': null, 'isTrusted': null}
class NewObjectWithBuffer(OpcodeHandler):
    """Create an object from a static map of values using buffer."""

    ARGUMENTS = (
        ArgsPattern(sequence(REG, UINT16, UINT16, UINT16, UINT16), "Reg8, UInt16, UInt16, UInt16, UInt16"),
        ArgsPattern(sequence(REG, UINT16, UINT16), "Reg8, UInt16, UInt16"),  # DEFINE_OPCODE_3
    )

    def handle(self, ctx: OpcodeContext) -> OpcodeResult:
        match = self.match_arguments(ctx)
        if isinstance(match, OpcodeResult):
            return match

        dest_reg = int(match.group(1))

        expression = self._object_expression_from_entry(ctx.entry)

        if expression is None:
            error = f"// Warning: No valid object parsed from comment: {ctx.entry.comment}"
            return self.build_exception_result(ctx.analysis, ctx.entry, error)

        result = OpcodeResult(ctx.entry, value=expression, dest_reg=dest_reg)
        ctx.analysis.add_result(result)

        return result

    @staticmethod
    def _object_expression_from_entry(entry) -> ObjectExpression | None:
        """
        Build an `ObjectExpression` from the entry's pre-parsed
        `object_literal` (populated by `OpcodeEntry` from the `Object:
        {...}` comment marker). An empty/missing comment still yields an
        empty object literal, matching a `NewObjectWithBuffer` with no
        properties; a present-but-unparseable `Object:` comment is a
        genuine failure (`object_literal` stays `None`).
        """
        if not entry.comment:
            return ObjectExpression(properties=())

        if entry.object_literal is None:
            return None

        properties = tuple(
            ObjectProperty(key=StringLiteral(k), value=_json_to_expression(v))
            for k, v in entry.object_literal.items()
        )
        return ObjectExpression(properties=properties)


# Reg8, UInt32, UInt32 (total size 9)
# DEFINE_OPCODE_5(NewObjectWithBufferLong, Reg8, UInt16, UInt16, UInt32, UInt32)
# DEFINE_OPCODE_3(NewObjectWithBufferLong, Reg8, UInt32, UInt32)
class NewObjectWithBufferLong(NewObjectWithBuffer):
    """Long variant."""

    ARGUMENTS = (
        ArgsPattern(sequence(REG, UINT16, UINT16, UINT32, UINT32), "Reg8, UInt16, UInt16, UInt32, UInt32"),
        ArgsPattern(sequence(REG, UINT32, UINT32), "Reg8, UInt32, UInt32"),  # DEFINE_OPCODE_3
    )


# Reg8, Reg8, UInt32, UInt32 (total size 10)
# DEFINE_OPCODE_4(NewObjectWithBufferAndParent, Reg8, Reg8, UInt32, UInt32)
# Example: <NewObjectWithBufferAndParent>: <Reg8: 8, Reg8: 0, UInt32: 1594, UInt32: 17242>
class NewObjectWithBufferAndParent(NewObjectWithBuffer):
    """Create an object from a static buffer with an explicit parent/prototype."""

    ARGUMENTS = ArgsPattern(sequence(REG, REG, UINT32, UINT32), "Reg8, Reg8, UInt32, UInt32"),

    def handle(self, ctx: OpcodeContext) -> OpcodeResult:
        match = self.match_arguments(ctx)
        if isinstance(match, OpcodeResult):
            return match

        dest_reg, _parent_reg, *_buffer_operands = map(int, match.groups())

        object_expr = self._object_expression_from_entry(ctx.entry)

        if object_expr is None:
            error = f"// Warning: No valid object parsed from comment: {ctx.entry.comment}"
            return self.build_exception_result(ctx.analysis, ctx.entry, error)

        # Parent register is resolved but not woven into `object_expr`
        # itself -- see module-level caveat above. Left available here
        # so a future fix can incorporate it (e.g. Object.create/
        # Object.setPrototypeOf) once the real IR shape for this is
        # decided.
        _parent = self.get_register_expression(ctx.analysis, _parent_reg)

        result = OpcodeResult(ctx.entry, value=object_expr, dest_reg=dest_reg)
        ctx.analysis.add_result(result)

        return result
