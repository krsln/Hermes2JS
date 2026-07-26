from __future__ import annotations

from dataclasses import dataclass

__all__ = [
    "Position",
    "SourceLocation",
]


@dataclass(frozen=True, slots=True)
class Position:
    """
    A single point within a source file.

    Attributes:
        line: 1-based line number.
        column: 0-based column number.
        offset: Character offset from the start of the file.
    """

    line: int
    column: int
    offset: int

    def __post_init__(self) -> None:
        if self.line < 1:
            raise ValueError(f"line must be >= 1, got {self.line}")

        if self.column < 0:
            raise ValueError(f"column must be >= 0, got {self.column}")

        if self.offset < 0:
            raise ValueError(f"offset must be >= 0, got {self.offset}")

    def __str__(self) -> str:
        return f"{self.line}:{self.column}"


@dataclass(frozen=True, slots=True)
class SourceLocation:
    """
    Start/end span of an IR node within its source.

    `source` identifies which source a node belongs to when multiple
    sources are involved in a single pipeline (e.g. multiple Hermes
    bytecode sections).
    """

    start: Position
    end: Position
    source: str | None = None

    def __str__(self) -> str:
        prefix = f"{self.source}:" if self.source else ""
        return f"{prefix}{self.start}-{self.end}"