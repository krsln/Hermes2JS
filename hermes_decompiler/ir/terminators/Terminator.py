from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass

from hermes_decompiler.ir.expressions import Expression


class Terminator(ABC):
    """
    Ends a basic block.

    Immutable, like every other IR node (see `ir.Node`'s contract) -
    subclasses use `@dataclass(frozen=True, slots=True, eq=False)`.
    Nothing in the codebase mutates a Terminator's fields in place;
    every pass that changes a block's terminator does so by replacing
    the reference (`block.terminator = dataclasses.replace(old, ...)`
    or `block.terminator = new_terminator`), exactly like the
    replace-and-reassign pattern used elsewhere on frozen Nodes.
    `eq=False` avoids relying on Python's auto-generated `__hash__`/
    `__eq__` over dataclass fields, which would break the moment
    something (e.g. `hash()`) touched `TerminatorSwitch.case_map` - a
    plain `dict`, and therefore unhashable.
    """

    @property
    @abstractmethod
    def targets(self) -> tuple[int, ...]:
        """CFG successor targets."""


@dataclass(frozen=True, slots=True, eq=False)
class TerminatorConditionalBranch(Terminator):
    condition: Expression
    target: int

    @property
    def targets(self):
        return (self.target,)


@dataclass(frozen=True, slots=True, eq=False)
class TerminatorJump(Terminator):
    target: int

    @property
    def targets(self):
        return (self.target,)


@dataclass(frozen=True, slots=True, eq=False)
class TerminatorReturn(Terminator):
    value: Expression | None

    @property
    def targets(self):
        return ()


@dataclass(frozen=True, slots=True, eq=False)
class TerminatorThrow(Terminator):
    value: Expression | None

    @property
    def targets(self):
        return ()


@dataclass(frozen=True, slots=True, eq=False)
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
