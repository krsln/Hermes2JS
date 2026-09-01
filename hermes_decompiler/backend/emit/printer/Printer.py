from __future__ import annotations

from ._PrinterContext import PrinterContext
from ._ConditionComment import ConditionCommentPrinter
from .ExpressionPrinter import ExpressionPrinter
from .StatementPrinter import StatementPrinter
from .RegionPrinter import RegionPrinter

__all__ = [
    "Printer",
]


class Printer:
    """
    Public facade for JavaScript emission.

    Printer owns the individual rendering components but does not itself
    implement IR visitor methods or region-specific rendering logic.

    Public API intentionally remains compatible with the previous Printer:
        Printer(verbose=False)
        printer.print_region(region)
        printer.print_expression(node)
        printer.print_statement(node)
        printer.print_terminator(node)
    """

    def __init__(
            self,
            *,
            verbose: bool = False,
    ) -> None:
        ctx = PrinterContext(verbose=verbose)

        expressions = ExpressionPrinter()
        statements = StatementPrinter(expressions)
        condition_comments = ConditionCommentPrinter(ctx, expressions)

        regions = RegionPrinter(ctx, expressions, statements, condition_comments)

        self._context = ctx
        self._expressions = expressions
        self._statements = statements
        self._condition_comments = condition_comments
        self._regions = regions

    @property
    def verbose(self) -> bool:
        """Whether verbose emission is enabled."""
        return self._context.verbose

    def print_region(self, region) -> list[str]:
        """Render a structured region tree."""
        return self._regions.print(region)

    def print_expression(self, node) -> str:
        """Render one expression."""
        return self._expressions.print(node)

    def print_statement(self, node) -> str:
        """Render one statement."""
        return self._statements.print(node)

    def print_terminator(self, node) -> str:
        """Render one raw/pre-structural terminator."""
        return self._statements.print(node)
