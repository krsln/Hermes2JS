from __future__ import annotations

from dataclasses import dataclass, field
from typing import Optional

from hermes_decompiler.regions.cfg.BasicBlock import BasicBlock


@dataclass(slots=True)
class NaturalLoop:
    """
    One natural loop in the CFG.

    A loop is uniquely identified by its header.

    Multiple back edges may enter the same header, therefore a loop
    may have multiple latches.
    """

    # unique loop entry
    header: BasicBlock

    # all blocks that belong to this loop
    members: set[BasicBlock] = field(default_factory=set)

    # blocks jumping back to the header (continue targets)
    latches: set[BasicBlock] = field(default_factory=set)

    # successors leaving the loop
    exits: set[BasicBlock] = field(default_factory=set)

    # nesting
    parent: Optional["NaturalLoop"] = None
    children: list["NaturalLoop"] = field(default_factory=list)

    @property
    def blocks(self) -> list[BasicBlock]:
        return sorted(self.members, key=lambda b: b.id)

    @property
    def latch_blocks(self) -> list[BasicBlock]:
        return sorted(self.latches, key=lambda b: b.id)

    @property
    def exit_blocks(self) -> list[BasicBlock]:
        return sorted(self.exits, key=lambda b: b.id)

    @property
    def is_top_level(self) -> bool:
        return self.parent is None

    @property
    def depth(self) -> int:
        depth = 0
        current = self.parent

        while current is not None:
            depth += 1
            current = current.parent

        return depth

    def __str__(self):
        return (
            f"NaturalLoop("
            f"header={self.header.id}, "
            f"members={[b.id for b in self.blocks]}, "
            f"latches={[b.id for b in self.latch_blocks]}, "
            f"exits={[b.id for b in self.exit_blocks]}"
            f")"
        )
