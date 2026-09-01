from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass

from hermes_decompiler.ir.expressions import Expression

__all__ = [
    "Terminator",
    "TerminatorConditionalBranch",
    "TerminatorJump",
    "TerminatorReturn",
    "TerminatorSwitch",
    "TerminatorThrow",
]


class Terminator(ABC):
    """Ends a basic block."""

    @property
    @abstractmethod
    def targets(self) -> tuple[int, ...]:
        """CFG successor targets."""


@dataclass(slots=True)
class TerminatorConditionalBranch(Terminator):
    condition: Expression
    target: int

    @property
    def targets(self):
        return (self.target,)


@dataclass(slots=True)
class TerminatorJump(Terminator):
    target: int

    @property
    def targets(self):
        return (self.target,)


@dataclass(slots=True)
class TerminatorReturn(Terminator):
    value: Expression | None

    @property
    def targets(self):
        return ()


@dataclass(slots=True)
class TerminatorThrow(Terminator):
    value: Expression | None

    @property
    def targets(self):
        return ()


@dataclass(slots=True)
class TerminatorSwitch(Terminator):
    selector: Expression
    case_map: dict[int, int]
    default_target: int | None

    @property
    def targets(self):
        targets = set(self.case_map.values())

        if self.default_target is not None:
            targets.add(self.default_target)

        return tuple(sorted(targets))
