from __future__ import annotations

from contextlib import contextmanager
from dataclasses import dataclass
from typing import Iterator

__all__ = [
    "PrinterContext",
]


@dataclass(slots=True)
class PrinterContext:
    """
    Mutable state shared by the JavaScript printers.

    The context deliberately contains only rendering state. It does not
    contain IR, CFG, RegionGraph, or analysis state.
    """

    verbose: bool = False
    indent: int = 1

    INDENT: str = "    "

    @contextmanager
    def indented(self) -> Iterator[None]:
        """Temporarily increase the current output indentation."""

        self.indent += 1
        try:
            yield
        finally:
            self.indent -= 1

    def write(self, lines: list[str], text: str) -> None:
        """Append one correctly indented line to the output."""

        lines.append(f"{self.INDENT * self.indent}{text}")

    def reset(self) -> None:
        """Reset per-document rendering state."""

        self.indent = 1
