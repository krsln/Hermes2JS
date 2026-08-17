from __future__ import annotations

from typing import Any

from hermes_decompiler.core.logging import get_logger
from hermes_decompiler.ir import NodeVisitor

__all__ = [
    "PrinterVisitor",
]

logger = get_logger(__name__)


class PrinterVisitor(NodeVisitor):
    """
    Base visitor for IR-to-JavaScript printers.

    Unlike NodeVisitor's traversal-oriented generic_visit(), this visitor
    produces a textual fallback for unsupported nodes.
    """

    printer_name = "Printer"

    def generic_visit(self, node: Any) -> str:
        node_type = type(node).__name__

        logger.warning(
            "%s: unsupported node type %s",
            self.printer_name,
            node_type,
        )

        return f"/* unsupported: {node_type} */"
