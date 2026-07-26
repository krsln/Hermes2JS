from __future__ import annotations

from hermes_decompiler.ir import (
    NodeVisitor,
    precedence,
)
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
)
from hermes_decompiler.ir.statements import (

    BlockStatement,
    EmptyStatement,
    ExpressionStatement,
    VariableDeclaration,
    IfStatement,
    ReturnStatement,
    DebuggerStatement,
    WhileStatement,
    DoWhileStatement,
    ForStatement,
    ForInStatement,
    ForOfStatement,
    LabeledStatement,
    BreakStatement,
    ContinueStatement,
    ThrowStatement,
    TryStatement,
)

__all__ = [
    "Printer",
]


class Printer(NodeVisitor):
    """
    Renders `ir` Expression/Statement nodes into JavaScript source text.

    This is a plain expression/single-statement printer - it returns a
    string for a given node and does not itself manage block indentation
    for multi-statement bodies. `JSRenderer` owns indentation and calls
    `print_expression`/`print_statement` per line; `BlockStatement`'s own
    children are therefore not expanded here (see `visit_BlockStatement`),
    that's `JSRenderer`'s job via the region tree.

    Only a single instance is needed; the class holds no mutable state.
    """

    # ------------------------------------------------------------------
    # Public entry points
    # ------------------------------------------------------------------

    def print_expression(self, node) -> str:
        return self.visit(node)

    def print_statement(self, node) -> str:
        return self.visit(node)

    # ------------------------------------------------------------------
    # Fallback
    # ------------------------------------------------------------------

    def generic_visit(self, node) -> str:
        return f"/* unsupported: {type(node).__name__} */"

    # ------------------------------------------------------------------
    # Expressions - primitives
    # ------------------------------------------------------------------

    def visit_Identifier(self, node: Identifier) -> str:
        return node.name

    def visit_ParenthesizedExpression(self, node: ParenthesizedExpression) -> str:
        return f"({self.visit(node.expression)})"

    def visit_RawExpression(self, node: RawExpression) -> str:
        return node.source

    # ------------------------------------------------------------------
    # Expressions - literals
    # ------------------------------------------------------------------

    def visit_NumericLiteral(self, node: NumericLiteral) -> str:
        return repr(node.value)

    def visit_BigIntLiteral(self, node: BigIntLiteral) -> str:
        return f"{node.value}n"

    def visit_StringLiteral(self, node: StringLiteral) -> str:
        import json
        return json.dumps(node.value)

    def visit_BooleanLiteral(self, node: BooleanLiteral) -> str:
        return "true" if node.value else "false"

    def visit_NullLiteral(self, node: NullLiteral) -> str:
        return "null"

    def visit_UndefinedLiteral(self, node: UndefinedLiteral) -> str:
        return "undefined"

    def visit_RegExpLiteral(self, node: RegExpLiteral) -> str:
        return f"/{node.pattern}/{node.flags}"

    def visit_TemplateLiteral(self, node: TemplateLiteral) -> str:
        parts = []

        for i, quasi in enumerate(node.quasis):
            parts.append(quasi.raw)

            if i < len(node.expressions):
                parts.append("${" + self.visit(node.expressions[i]) + "}")

        return "`" + "".join(parts) + "`"

    # ------------------------------------------------------------------
    # Expressions - operations
    # ------------------------------------------------------------------

    def visit_UnaryExpression(self, node: UnaryExpression) -> str:
        # Word operators (typeof/void/delete) already carry a trailing
        # space in UnaryOperator's values; symbolic ones (+/-/!/~) don't
        # need one. Simple concatenation covers both.
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
        return ", ".join(self.visit(e) for e in node.expressions)

    # ------------------------------------------------------------------
    # Expressions - access / calls
    # ------------------------------------------------------------------

    def visit_MemberExpression(self, node: MemberExpression) -> str:
        receiver = self._wrap_operand(node.receiver, node)
        access = "?." if node.optional else ""

        if node.computed:
            return f"{receiver}{access}[{self.visit(node.member)}]"

        if node.optional:
            return f"{receiver}?.{self.visit(node.member)}"

        return f"{receiver}.{self.visit(node.member)}"

    def visit_CallExpression(self, node: CallExpression) -> str:
        callee = self._wrap_operand(node.callee, node)
        args = ", ".join(self.visit(a) for a in node.arguments)
        call = "?.(" if node.optional else "("
        return f"{callee}{call}{args})"

    def visit_NewExpression(self, node: NewExpression) -> str:
        callee = self._wrap_operand(node.callee, node)
        args = ", ".join(self.visit(a) for a in node.arguments)
        return f"new {callee}({args})"

    def visit_SpreadElement(self, node: SpreadElement) -> str:
        return f"...{self.visit(node.argument)}"

    # ------------------------------------------------------------------
    # Expressions - collections
    # ------------------------------------------------------------------

    def visit_ArrayExpression(self, node: ArrayExpression) -> str:
        return "[" + ", ".join(self.visit(e) for e in node.elements) + "]"

    def visit_ObjectExpression(self, node: ObjectExpression) -> str:
        return "{ " + ", ".join(self.visit(p) for p in node.properties) + " }"

    def visit_ObjectProperty(self, node: ObjectProperty) -> str:
        if node.shorthand:
            return self.visit(node.value)

        key = f"[{self.visit(node.key)}]" if node.computed else self.visit(node.key)
        value = self.visit(node.value)

        if node.kind == PropertyKind.GET:
            return f"get {key}() {{ return {value}; }}"

        if node.kind == PropertyKind.SET:
            return f"set {key}(v) {{ {value} = v; }}"

        return f"{key}: {value}"

    # ------------------------------------------------------------------
    # Expressions - functions
    # ------------------------------------------------------------------

    def visit_FunctionExpression(self, node: FunctionExpression) -> str:
        name = self.visit(node.name) if node.name else ""
        params = ", ".join(self.visit(p) for p in node.parameters)
        prefix = "async function" if node.async_ else "function"
        star = "*" if node.generator else ""
        return f"{prefix}{star} {name}({params}) {{ ... }}"

    def visit_ArrowFunctionExpression(self, node: ArrowFunctionExpression) -> str:
        params = ", ".join(self.visit(p) for p in node.parameters)
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
    # Statements
    # ------------------------------------------------------------------

    def visit_BlockStatement(self, node: BlockStatement) -> str:
        # Multi-statement expansion is JSRenderer's responsibility (it
        # walks the region tree, not this flat block). Used only when a
        # BlockStatement shows up inline (e.g. as a function body stub).
        return "{ ... }"

    def visit_EmptyStatement(self, node: EmptyStatement) -> str:
        return ";"

    def visit_ExpressionStatement(self, node: ExpressionStatement) -> str:
        return f"{self.visit(node.expression)};"

    def visit_VariableDeclaration(self, node: VariableDeclaration) -> str:
        parts = []

        for decl in node.declarations:
            id_text = self.visit(decl.id)

            if decl.init is not None:
                parts.append(f"{id_text} = {self.visit(decl.init)}")
            else:
                parts.append(id_text)

        return f"{node.kind} " + ", ".join(parts) + ";"

    def visit_IfStatement(self, node: IfStatement) -> str:
        # JSRenderer renders if/else structurally via IfRegion; this
        # covers the case of printing just the condition/header text.
        return f"if ({self.visit(node.test)})"

    def visit_ReturnStatement(self, node: ReturnStatement) -> str:
        if node.argument is None:
            return "return;"

        return f"return {self.visit(node.argument)};"

    def visit_DebuggerStatement(self, node: DebuggerStatement) -> str:
        return "debugger;"

    def visit_ThrowStatement(self, node: ThrowStatement) -> str:
        return f"throw {self.visit(node.argument)};"

    def visit_BreakStatement(self, node: BreakStatement) -> str:
        if node.label is None:
            return "break;"

        return f"break {self.visit(node.label)};"

    def visit_ContinueStatement(self, node: ContinueStatement) -> str:
        if node.label is None:
            return "continue;"

        return f"continue {self.visit(node.label)};"

    def visit_LabeledStatement(self, node: LabeledStatement) -> str:
        return f"{self.visit(node.label)}:"

    # ------------------------------------------------------------------
    # Pre-structural control flow (see regions/models/Statements.py)
    # ------------------------------------------------------------------

    def visit_GotoStatement(self, node) -> str:
        return f"goto label_{node.target};"

    def visit_IfGotoStatement(self, node) -> str:
        return f"if ({self.visit(node.condition)}) goto label_{node.target};"

    def visit_SwitchGotoStatement(self, node) -> str:
        targets = ", ".join(f"label_{t}" for t in node.targets)
        return f"/* switch ({self.visit(node.selector)}) -> {targets} */"

    # ------------------------------------------------------------------
    # Operator precedence helpers
    # ------------------------------------------------------------------

    def _wrap_operand(self, operand, parent) -> str:
        """Parenthesize `operand` if it's a lower-precedence expression."""

        text = self.visit(operand)

        if isinstance(operand, (BinaryExpression, ConditionalExpression, AssignmentExpression, SequenceExpression)):
            return f"({text})"

        return text

    def _wrap_side(self, side, parent: BinaryExpression, is_right: bool) -> str:
        text = self.visit(side)

        if isinstance(side, BinaryExpression):
            parent_prec = precedence(parent.operator)
            side_prec = precedence(side.operator)

            if side_prec < parent_prec or (is_right and side_prec == parent_prec):
                return f"({text})"

        elif isinstance(side, (ConditionalExpression, AssignmentExpression, SequenceExpression)):
            return f"({text})"

        return text
