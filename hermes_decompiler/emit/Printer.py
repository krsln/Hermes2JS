from __future__ import annotations

from hermes_decompiler.analysis.cfg import BasicBlock
from hermes_decompiler.analysis.regions.Regions import (
    SequenceRegion,
    LoopRegion,
    IfRegion,
    TryRegion,
    SwitchRegion,
)
from hermes_decompiler.ir import NodeVisitor
from hermes_decompiler.ir import (
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
    LabeledStatement,
    BreakStatement,
    ContinueStatement,
    ThrowStatement,
)

__all__ = [
    "Printer",
]


class Printer(NodeVisitor):
    """
    Converts the structured RegionGraph into JavaScript source.

    Assumptions
    -----------

    * CFG construction is complete.
    * Structural analysis is complete.
    * Every control-flow construct is represented by a Region.
    * BasicBlocks contain only ordinary IR statements.
    * Block terminators have already been consumed by the structurers.
    """

    INDENT = "    "

    def __init__(self, *, verbose: bool = False):
        self.verbose = verbose
        self._indent = 0

    # ---------------------------------------------------------
    # public
    # ---------------------------------------------------------

    def print_region(self, region) -> list[str]:

        self._indent = 1

        lines: list[str] = []

        self._emit_region(region, lines)

        return lines

    # ---------------------------------------------------------
    # dispatcher
    # ---------------------------------------------------------

    def _emit_region(self, region, lines):

        match region:

            case SequenceRegion():
                self._emit_sequence(region, lines)

            case LoopRegion():
                self._emit_loop(region, lines)

            case IfRegion():
                self._emit_if(region, lines)

            case TryRegion():
                self._emit_try(region, lines)

            case SwitchRegion():
                self._emit_switch(region, lines)

            case BasicBlock():
                self._emit_block(region, lines)

            case _:
                raise TypeError(type(region))

    # ---------------------------------------------------------
    # basic block
    # ---------------------------------------------------------

    def _emit_block(
            self,
            block: BasicBlock,
            lines: list[str],
    ):

        if self.verbose:
            self._write(lines, f"// ──────────────── Block {block.id} ──────────────── ")

        for instruction in block.instructions:

            if self.verbose:
                bytecode = instruction.opcode.bytecode
                bytecode = bytecode.split(":", 1)[1].strip() if ":" in bytecode else bytecode.strip()

                self._write(lines, f"// CODE → {bytecode}")

            if instruction.statement is not None:
                rendered = self.print_statement(instruction.statement)

                self._write(lines, rendered)

                continue

            if instruction.terminator is not None:
                rendered = self.print_terminator(instruction.terminator)

                self._write(lines, rendered)

                continue

            if instruction.value is None:
                continue

            rendered = self.print_expression(instruction.value)

            if instruction.dest_reg is not None:
                rendered = f"r{instruction.dest_reg} = {rendered}"

            if instruction.used:
                if self.verbose:
                    self._write(lines, f"// USED → {rendered};")

            else:
                self._write(lines, rendered)

    # ---------------------------------------------------------
    # sequence
    # ---------------------------------------------------------

    def _emit_sequence(self, region: SequenceRegion, lines):

        for child in region.children:
            self._emit_region(child, lines)

    # ---------------------------------------------------------
    # if
    # ---------------------------------------------------------

    def _emit_if(self, region: IfRegion, lines):

        cond = self.print_expression(region.condition)

        self._write(lines, f"if ({cond}) {{")

        self._indent += 1
        self._emit_region(region.then_body, lines)
        self._indent -= 1

        if region.else_body:
            self._write(lines, "} else {")

            self._indent += 1
            self._emit_region(region.else_body, lines)
            self._indent -= 1

        self._write(lines, "}")

    # ---------------------------------------------------------
    # loop
    # ---------------------------------------------------------

    def _emit_loop(self, region: LoopRegion, lines):

        kind = region.loop_kind
        if self.verbose:
            self._write(lines,f"// LOOP → START ({kind.value if kind else "unknown"})")

        cond = (
            self.print_expression(region.condition)
            if region.condition
            else "true"
        )

        self._write(lines, f"while ({cond}) {{")

        self._indent += 1
        self._emit_region(region.body, lines)
        self._indent -= 1

        self._write(lines, "}")
        self._write(lines, "// LOOP → END")


    # ---------------------------------------------------------
    # try
    # ---------------------------------------------------------

    def _emit_try(self, region: TryRegion, lines):

        self._write(lines, "try {")

        self._indent += 1
        self._emit_region(region.try_body, lines)
        self._indent -= 1

        if region.catch:
            name = region.catch.exception

            self._write(lines, f"}} catch ({name}) {{")

            self._indent += 1
            self._emit_region(region.catch.body, lines)
            self._indent -= 1

        if region.finally_:
            self._write(lines, "} finally {")

            self._indent += 1
            self._emit_region(region.finally_.body, lines)
            self._indent -= 1

        self._write(lines, "}")

    # ---------------------------------------------------------
    # switch
    # ---------------------------------------------------------

    def _emit_switch(self, region: SwitchRegion, lines):
        raise NotImplementedError

    # ---------------------------------------------------------
    # helpers
    # ---------------------------------------------------------

    def _write(self, lines: list[str], text: str):
        lines.append(f"{self.INDENT * self._indent}{text}")

    # ------------------------------------------------------------------
    # ------------------------------------------------------------------
    # ------------------------------------------------------------------

    # ------------------------------------------------------------------
    # Public entry points
    # ------------------------------------------------------------------

    def print_expression(self, node) -> str:
        return self.visit(node)

    def print_statement(self, node) -> str:
        return self.visit(node)

    def print_terminator(self, node) -> str:
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

    def visit_TerminatorJump(self, node) -> str:
        return f"goto label_{node.target};"

    def visit_TerminatorConditionalBranch(self, node) -> str:
        return f"if ({self.visit(node.condition)}) goto label_{node.target};"

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
