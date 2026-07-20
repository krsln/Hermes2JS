from __future__ import annotations

from abc import ABC
from dataclasses import dataclass, field


@dataclass(slots=True)
class Region(ABC):
    """
    Base class for all high-level control-flow regions.

    A Region represents a structured control flow reconstructed from the
    Control Flow Graph (CFG). Examples include basic blocks, if/else,
    loops, try/catch, switch statements, and functions.
    """

    children: list["Region"] = field(default_factory=list)