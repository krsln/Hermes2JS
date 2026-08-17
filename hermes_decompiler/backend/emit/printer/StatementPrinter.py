from __future__ import annotations

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

from ._PrinterVisitor import PrinterVisitor
from .ExpressionPrinter import ExpressionPrinter

__all__ = [
    "StatementPrinter",
]


class StatementPrinter(PrinterVisitor):
    """
    Converts IR statements and raw terminators into JavaScript text.

    Structural control-flow rendering remains the responsibility of
    RegionPrinter. In particular, IfStatement only renders its header;
    IfRegion renders the actual control-flow structure.
    """

    printer_name = "StatementPrinter"

    def __init__(
            self,
            expressions: ExpressionPrinter,
    ) -> None:
        self.expressions = expressions

    def print(self, node) -> str:
        """Render one statement or terminator."""
        return self.visit(node)

    # ------------------------------------------------------------------
    # statements
    # ------------------------------------------------------------------

    def visit_BlockStatement(self, _node: BlockStatement) -> str:
        # Multi-statement expansion is JSRenderer's responsibility (it
        # walks the region tree, not this flat block). Used only when a
        # BlockStatement shows up inline (e.g., as a function body stub).
        return "{ ... }"

    def visit_EmptyStatement(self, _node: EmptyStatement) -> str:
        return ";"

    def visit_ExpressionStatement(self, node: ExpressionStatement) -> str:
        return f"{self.expressions.print(node.expression)};"

    def visit_VariableDeclaration(self, node: VariableDeclaration) -> str:
        parts: list[str] = []

        for declaration in node.declarations:
            identifier = self.expressions.print(declaration.id)

            if declaration.init is not None:
                initializer = self.expressions.print(
                    declaration.init
                )
                parts.append(
                    f"{identifier} = {initializer}"
                )
            else:
                parts.append(identifier)

        return f"{node.kind} " + ", ".join(parts) + ";"

    def visit_IfStatement(self, node: IfStatement) -> str:
        # JSRenderer renders if/else structurally via IfRegion; this
        # covers the case of printing just the condition/header text.
        return f"if ({self.expressions.print(node.test)})"

    def visit_ReturnStatement(self, node: ReturnStatement) -> str:
        if node.argument is None:
            return "return;"

        return f"return {self.expressions.print(node.argument)};"

    def visit_DebuggerStatement(self, _node: DebuggerStatement) -> str:
        return "debugger;"

    def visit_ThrowStatement(self, node: ThrowStatement) -> str:
        return f"throw {self.expressions.print(node.argument)};"

    def visit_BreakStatement(self, node: BreakStatement) -> str:
        if node.label is None:
            return "break;"

        return f"break {self.expressions.print(node.label)};"

    def visit_ContinueStatement(self, node: ContinueStatement) -> str:
        if node.label is None:
            return "continue;"

        return f"continue {self.expressions.print(node.label)};"

    def visit_LabeledStatement(self, node: LabeledStatement) -> str:
        return f"{self.expressions.print(node.label)}:"

    # ------------------------------------------------------------------
    # pre-structural control flow
    # ------------------------------------------------------------------

    def visit_TerminatorJump(self, node) -> str:
        return f"goto label_{node.target};"

    def visit_TerminatorConditionalBranch(self, node) -> str:
        condition = self.expressions.print(node.condition)

        return (
            f"if ({condition}) "
            f"goto label_{node.target};"
        )

    def visit_TerminatorSwitch(self, _) -> str:
        return (
            "// Raw TerminatorSwitch reached Printer. "
            "SwitchStructurer should have converted it "
            "into a SwitchRegion."
        )
