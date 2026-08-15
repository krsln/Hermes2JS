import ast
import re

from hermes_decompiler.frontend.opcode import OpcodeResult
from hermes_decompiler.handlers import OpcodeHandler, OpcodeContext, ArgsPattern, sequence, REG, UINT16, UINT32
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

        expression = self._parse_object_from_comment(ctx.entry.comment)

        if expression is None:
            error = f"// Warning: No valid object parsed from comment: {ctx.entry.comment}"
            return self.build_exception_result(ctx.analysis, ctx.entry, error)

        result = OpcodeResult(ctx.entry, value=expression, dest_reg=dest_reg)
        ctx.analysis.add_result(result)

        return result

    @staticmethod
    def _parse_object_from_comment(comment: str) -> ObjectExpression | None:
        """
        Extract and parse `Object: {...}` from an opcode comment.

        Handles nested braces and braces that appear inside string values
        (common with Reanimated / worklet 'code' fields).
        """
        if not comment:
            return ObjectExpression(properties=())

        marker = "Object:"
        idx = comment.find(marker)
        if idx == -1:
            return None

        # İlk '{' karakterini bul
        start = comment.find("{", idx + len(marker))
        if start == -1:
            return None

        # Balanced brace extraction (string-aware)
        obj_str = NewObjectWithBuffer._extract_balanced_braces(comment, start)
        if obj_str is None:
            return None

        try:
            clean = obj_str
            clean = re.sub(r"\btrue\b", "True", clean)
            clean = re.sub(r"\bfalse\b", "False", clean)
            clean = re.sub(r"\bnull\b", "None", clean)

            parsed = ast.literal_eval(clean)
        except (SyntaxError, ValueError, TypeError):
            return None

        if not isinstance(parsed, dict):
            return None

        properties = tuple(
            ObjectProperty(key=StringLiteral(k), value=_json_to_expression(v))
            for k, v in parsed.items()
        )
        return ObjectExpression(properties=properties)

    @staticmethod
    def _extract_balanced_braces(text: str, start: int) -> str | None:
        """
        text[start] == '{' varsayılır.
        String literal içindeki { } karakterlerini yok sayarak
        eşleşen kapanış '}' pozisyonuna kadar olan substring'i döner.
        """
        if start >= len(text) or text[start] != "{":
            return None

        depth = 0
        i = start
        in_string = False
        string_char = None  # "'" veya '"'
        escape = False

        while i < len(text):
            ch = text[i]

            if in_string:
                if escape:
                    escape = False
                elif ch == "\\":
                    escape = True
                elif ch == string_char:
                    in_string = False
                    string_char = None
            else:
                if ch in ("'", '"'):
                    in_string = True
                    string_char = ch
                elif ch == "{":
                    depth += 1
                elif ch == "}":
                    depth -= 1
                    if depth == 0:
                        return text[start: i + 1]

            i += 1

        return None


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

        object_expr = self._parse_object_from_comment(ctx.entry.comment)

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
