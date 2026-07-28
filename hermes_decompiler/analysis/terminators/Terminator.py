from __future__ import annotations

from abc import ABC
from dataclasses import dataclass

from hermes_decompiler.ir.expressions import Expression


class Terminator(ABC):
    """Ends a basic block."""


@dataclass(slots=True)
class TerminatorConditionalBranch(Terminator):
    condition: Expression
    target: int


@dataclass(slots=True)
class TerminatorJump(Terminator):
    target: int


@dataclass(slots=True)
class TerminatorReturn(Terminator):
    value: Expression | None


@dataclass(slots=True)
class TerminatorThrow(Terminator):
    value: Expression | None


@dataclass(slots=True)
class TerminatorSwitch(Terminator):
    selector: Expression
    targets: tuple[int, ...]
