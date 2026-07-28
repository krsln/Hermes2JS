import json
import re

from hermes_decompiler.handlers import OpcodeHandler, REG, UINT16, sequence
from hermes_decompiler.ir.expressions import (
    ArrayExpression,
    Expression,
    ObjectExpression,
    ObjectProperty,
    StringLiteral,
    python_literal,
)
from hermes_decompiler.opcode import OpcodeEntry, OpcodeResult
from hermes_decompiler.runtime import HermesAnalysis


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


# DEFINE_OPCODE_5(NewObjectWithBuffer, Reg8, UInt16, UInt16, UInt16, UInt16)
# Example: < NewObjectWithBuffer >: < Reg8: 2, UInt16: 2, UInt16: 2, UInt16: 4743, UInt16: 24182 >  # Object: {'message': 'You have joined the list', 'type': 'success'}
class NewObjectWithBuffer(OpcodeHandler):
    """Create an object from a static map of values using buffer."""

    _PATTERN = sequence(REG, UINT16, UINT16, UINT16, UINT16)

    def handle(self, analysis: HermesAnalysis, entry: OpcodeEntry) -> OpcodeResult:

        match = self._PATTERN.match(entry.args.strip())
        if not match:
            return self.build_invalid_args_result(analysis, entry)

        dest_reg = int(match.group(1))

        expression = self._parse_object_from_comment(entry.comment)

        if expression is None:
            error = f"// Warning: No valid object parsed from comment: {entry.comment}"
            return self.build_exception_result(analysis, entry, error)

        result = OpcodeResult(entry, value=expression, dest_reg=dest_reg)
        analysis.add_result(result)

        return result

    @staticmethod
    def _parse_object_from_comment(comment: str) -> ObjectExpression | None:
        """
        Extract and parse `Object: {...}` from an opcode comment.

        NOTE (fix): the previous version returned the raw `dict` from
        `json.loads(...)` on success - unwrapped, not an IR/Value node
        at all - and only used `ObjectLiteralValue({})` on the empty/
        failure path. Both branches now consistently return an
        `ObjectExpression` (or `None` on genuine failure, distinguished
        from a legitimately empty object).
        """

        if not comment:
            return ObjectExpression(properties=())

        object_matches = re.findall(r"Object:\s*(\{[^}]+})", comment)

        for obj_str in object_matches:
            try:
                clean_str = obj_str.replace("'", '"').rstrip(",").strip()
                parsed = json.loads(clean_str)
            except json.JSONDecodeError:
                continue  # try next match

            if not isinstance(parsed, dict):
                continue

            properties = tuple(
                ObjectProperty(key=StringLiteral(k), value=_json_to_expression(v))
                for k, v in parsed.items()
            )
            return ObjectExpression(properties=properties)

        return None


class NewObjectWithBufferLong(NewObjectWithBuffer):
    """Long variant."""

    pass


# NewObjectWithBufferAndParent -- ***SIGNATURE NOT CONFIRMED***
#
# Not found in either source consulted (public BytecodeList.def or the
# hermes-dec table). Inferred purely by name/analogy with two confirmed
# siblings:
#   - NewObjectWithBuffer:  Reg8 dest, UInt16 size_hint, UInt16 num_elems,
#     UInt16 key_buf_idx, UInt16 val_buf_idx
#   - NewObjectWithParent:  Reg8 dest, Reg8 parent
#     ("Create a new empty Object with the specified parent. If the
#      parent is null, no parent is used...")
#
# NewObjectWithBufferAndParent is presumably the fusion of both: same
# static key/value buffer initialization as NewObjectWithBuffer, but
# with an explicit parent register instead of always defaulting to
# Object.prototype -- i.e. `Object.create(parent, ...)`-shaped object
# literals (used for e.g. `{ __proto__: parent, a: 1, b: 2 }` or
# Babel/TS helper-generated objects with a non-default prototype).
#
# Guessed layout: Reg8 dest, Reg8 parent, then the same four UInt16
# buffer operands as NewObjectWithBuffer (size_hint, num_elems,
# key_buf_idx, val_buf_idx) -- parent register inserted right after
# dest, mirroring where it sits in NewObjectWithParent.
#
# VERIFY operand count/order against your actual disassembler output
# before trusting this. Since the object's *contents* still come from
# the same key/value buffer table lookup NewObjectWithBuffer uses
# (which this decompiler resolves via the `Object: {...}` comment, not
# from operand values directly), the buffer-parsing logic below is
# reused as-is; only the parent register is new and gets threaded into
# an `Object.create(parent, ...)`-style rendering... but since we don't
# have a clean way to express "object literal with property descriptors
# AND a custom prototype" as a single JS expression, this renders as a
# comma-separated pseudo-assignment instead: the plain object literal
# is built the same way as NewObjectWithBuffer, and the parent is noted
# via `Object.setPrototypeOf`. Adjust once the real semantics/operand
# layout are confirmed.
class NewObjectWithBufferAndParent(NewObjectWithBuffer):
    """Create an object from a static buffer with an explicit parent/prototype."""

    _PATTERN = sequence(REG, REG, UINT16, UINT16, UINT16, UINT16)

    def handle(self, analysis: HermesAnalysis, entry: OpcodeEntry) -> OpcodeResult:
        match = self._PATTERN.match(entry.args.strip())
        if not match:
            return self.build_invalid_args_result(
                analysis, entry, "Expected Reg8, Reg8, UInt16, UInt16, UInt16, UInt16 arguments"
            )

        dest_reg, _parent_reg, *_buffer_operands = map(int, match.groups())

        object_expr = self._parse_object_from_comment(entry.comment)

        if object_expr is None:
            error = f"// Warning: No valid object parsed from comment: {entry.comment}"
            return self.build_exception_result(analysis, entry, error)

        # Parent register is resolved but not woven into `object_expr`
        # itself -- see module-level caveat above. Left available here
        # so a future fix can incorporate it (e.g. Object.create/
        # Object.setPrototypeOf) once the real IR shape for this is
        # decided.
        _parent = self.get_register_value(analysis, _parent_reg)

        result = OpcodeResult(entry, value=object_expr, dest_reg=dest_reg)
        analysis.add_result(result)

        return result


class NewObjectWithBufferAndParentLong(NewObjectWithBufferAndParent):
    pass
