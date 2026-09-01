from __future__ import annotations

import json
from typing import Any

from hermes_decompiler.ir import precedence
from hermes_decompiler.ir.expressions import (
    Identifier,
    ParenthesizedExpression,
    NumericLiteral,
    BigIntLiteral,
    StringLiteral,
    BooleanLiteral,
    NullLiteral,
    UndefinedLiteral,
    RegExpLiteral,
    TemplateLiteral,
    UnaryExpression,
    UpdateExpression,
    BinaryExpression,
    AssignmentExpression,
    ConditionalExpression,
    SequenceExpression,
    MemberExpression,
    CallExpression,
    NewExpression,
    SpreadElement,
    ArrayExpression,
    ObjectExpression,
    ObjectProperty,
    PropertyKind,
    FunctionExpression,
    ArrowFunctionExpression,
    AwaitExpression,
    YieldExpression,
    RawExpression,
    ThisPlaceholder,
)
from ._PrinterVisitor import PrinterVisitor

__all__ = [
    "ExpressionPrinter",
]


# noinspection PyMethodMayBeStatic
class ExpressionPrinter(PrinterVisitor):
    """
    Converts IR expressions into JavaScript source text.

    This class is intentionally stateless. Indentation and output-buffer
    management belong to PrinterContext / RegionPrinter.
    """

    printer_name = "ExpressionPrinter"

    def print(self, node) -> str:
        """Render one expression."""
        return self.visit(node)

    # ------------------------------------------------------------------
    # primitives
    # ------------------------------------------------------------------

    def visit_Identifier(self, node: Identifier) -> str:
        return node.name

    def visit_ParenthesizedExpression(self, node: ParenthesizedExpression) -> str:
        return f"({self.visit(node.expression)})"

    def visit_RawExpression(self, node: RawExpression) -> str:
        return node.source

    def visit_ThisPlaceholder(self, node: ThisPlaceholder) -> str:
        return f"{node.origin}(r{node.source_reg})"

    # ------------------------------------------------------------------
    # literals
    # ------------------------------------------------------------------

    def visit_NumericLiteral(self, node: NumericLiteral) -> str:
        value = node.value

        if value != value:  # NaN
            return "NaN"

        if value == float("inf"):
            return "Infinity"

        if value == float("-inf"):
            return "-Infinity"

        if isinstance(value, float) and value.is_integer():
            return str(int(value))

        return repr(value)

    def visit_BigIntLiteral(self, node: BigIntLiteral) -> str:
        return f"{node.value}n"

    def visit_StringLiteral(self, node: StringLiteral) -> str:
        return json.dumps(node.value)

    def visit_BooleanLiteral(self, node: BooleanLiteral) -> str:
        return "true" if node.value else "false"

    def visit_NullLiteral(self, _node: NullLiteral) -> str:
        return "null"

    def visit_UndefinedLiteral(self, _node: UndefinedLiteral) -> str:
        return "undefined"

    def visit_RegExpLiteral(self, node: RegExpLiteral) -> str:
        return f"/{node.pattern}/{node.flags}"

    def visit_TemplateLiteral(self, node: TemplateLiteral) -> str:
        parts: list[str] = []

        for index, quasi in enumerate(node.quasis):
            parts.append(quasi.raw)

            if index < len(node.expressions):
                parts.append("${" + self.visit(node.expressions[index]) + "}")

        return "`" + "".join(parts) + "`"

    # ------------------------------------------------------------------
    # operations
    # ------------------------------------------------------------------

    def visit_UnaryExpression(self, node: UnaryExpression) -> str:
        operand = self._wrap_operand(node.operand, node)
        return f"{node.operator}{operand}"

    def visit_UpdateExpression(self, node: UpdateExpression) -> str:
        argument = self.visit(node.argument)

        if node.prefix:
            return f"{node.operator}{argument}"

        return f"{argument}{node.operator}"

    def visit_BinaryExpression(self, node: BinaryExpression) -> str:
        left = self._wrap_side(node.left, node, is_right=False)
        right = self._wrap_side(node.right, node, is_right=True)

        return f"{left} {node.operator} {right}"

    def visit_AssignmentExpression(self, node: AssignmentExpression) -> str:
        left = self.visit(node.left)
        right = self.visit(node.right)

        return f"{left} {node.operator} {right}"

    def visit_ConditionalExpression(self, node: ConditionalExpression) -> str:
        test = self._wrap_operand(node.test, node)
        consequent = self.visit(node.consequent)
        alternate = self.visit(node.alternate)

        return f"{test} ? {consequent} : {alternate}"

    def visit_SequenceExpression(self, node: SequenceExpression) -> str:
        return ", ".join(
            self.visit(expression)
            for expression in node.expressions
        )

    # ------------------------------------------------------------------
    # access / calls
    # ------------------------------------------------------------------

    def visit_MemberExpression(self, node: MemberExpression) -> str:
        if (
                not node.computed
                and isinstance(node.obj, Identifier)
                and node.obj.name == "globalThis"
        ):
            # Hermes represents global property access explicitly through
            # `globalThis`, but source-level JavaScript typically uses the
            # global binding directly (e.g. `Promise` instead of
            # `globalThis.Promise`).
            return self.visit(node.prop)

        obj = self._wrap_operand(node.obj, node)
        prop = self.visit(node.prop)

        if node.receiver is not None:
            receiver = self.visit(node.receiver)

            if node.optional:
                return (
                    f"Reflect.get("
                    f"{obj}, {prop}, {receiver}"
                    f") /* optional receiver access */"
                )

            return f"Reflect.get({obj}, {prop}, {receiver})"

        access = "?." if node.optional else ""

        if node.computed:
            return f"{obj}{access}[{prop}]"

        if node.optional:
            return f"{obj}?.{prop}"

        return f"{obj}.{prop}"

    def visit_CallExpression(self, node: CallExpression) -> str:
        callee = self._wrap_operand(node.callee, node)
        # if callee.startswith("globalThis."):
        #     callee = callee.removeprefix("globalThis.")
        args = ", ".join(
            self.visit(argument)
            for argument in node.arguments
        )

        call = "?.(" if node.optional else "("

        return f"{callee}{call}{args})"

    def visit_NewExpression(self, node: NewExpression) -> str:
        callee = self._wrap_operand(node.callee, node)
        args = ", ".join(
            self.visit(argument)
            for argument in node.arguments
        )

        return f"new {callee}({args})"

    def visit_SpreadElement(self, node: SpreadElement) -> str:
        return f"...{self.visit(node.argument)}"

    # ------------------------------------------------------------------
    # collections
    # ------------------------------------------------------------------

    def visit_ArrayExpression(self, node: ArrayExpression) -> str:
        return "[" + ", ".join(self.visit(e) for e in node.elements) + "]"

    def visit_ObjectExpression(self, node: ObjectExpression) -> str:
        return "{ " + ", ".join(self.visit(p) for p in node.properties) + " }"

    def visit_ObjectProperty(self, node: ObjectProperty) -> str:
        if node.shorthand:
            return self.visit(node.value)

        key = (
            f"[{self.visit(node.key)}]"
            if node.computed
            else self.visit(node.key)
        )
        value = self.visit(node.value)

        if node.kind == PropertyKind.GET:
            return f"get {key}() {{ return {value}; }}"

        if node.kind == PropertyKind.SET:
            return f"set {key}(v) {{ {value} = v; }}"

        return f"{key}: {value}"

    # ------------------------------------------------------------------
    # functions
    # ------------------------------------------------------------------

    def visit_FunctionExpression(self, node: FunctionExpression) -> str:
        name = self.visit(node.name) if node.name else ""
        params = ", ".join(self.visit(param) for param in node.parameters)

        prefix = "async function" if node.async_ else "function"
        star = "*" if node.generator else ""

        return f"{prefix}{star} {name}({params}) {{ ... }}"

    def visit_ArrowFunctionExpression(self, node: ArrowFunctionExpression) -> str:
        params = ", ".join(self.visit(param) for param in node.parameters)
        prefix = "async " if node.async_ else ""

        return f"{prefix}({params}) => {{ ... }}"

    def visit_AwaitExpression(self, node: AwaitExpression) -> str:
        return f"await {self._wrap_operand(node.argument, node)}"

    def visit_YieldExpression(self, node: YieldExpression) -> str:
        star = "*" if node.delegate else ""

        if node.argument is None:
            return f"yield{star}"

        return f"yield{star} {self.visit(node.argument)}"

    # ------------------------------------------------------------------
    # precedence
    # ------------------------------------------------------------------

    def _wrap_operand(self, operand: Any, _parent: Any) -> str:
        """
        Parenthesize operands whose syntax cannot safely be emitted
        without grouping.
        """
        text = self.visit(operand)

        tuple_expressions = (
            BinaryExpression,
            ConditionalExpression,
            AssignmentExpression,
            SequenceExpression,
        )
        if isinstance(operand, tuple_expressions):
            return f"({text})"

        return text

    def _wrap_side(self, side, parent: BinaryExpression, is_right: bool) -> str:
        text = self.visit(side)

        if isinstance(side, BinaryExpression):
            parent_precedence = precedence(parent.operator)
            side_precedence = precedence(side.operator)

            if (
                    side_precedence < parent_precedence
                    or (is_right and side_precedence == parent_precedence)
            ):
                return f"({text})"

        elif isinstance(side, (ConditionalExpression, AssignmentExpression, SequenceExpression)):
            return f"({text})"

        return text
