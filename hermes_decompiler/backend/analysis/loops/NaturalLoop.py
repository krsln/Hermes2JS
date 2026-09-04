from __future__ import annotations

from dataclasses import dataclass, field
from typing import Optional

from hermes_decompiler.backend.analysis.cfg.BasicBlock import BasicBlock


@dataclass(slots=True, eq=False)
class NaturalLoop:
    """
    Represents a natural loop discovered in a control-flow graph.

    A natural loop is identified by its unique loop header. Multiple
    back edges may target the same header, so a single loop can have
    multiple latch blocks.

    Attributes:
        header: The unique entry block of the loop.
        members: All basic blocks belonging to the loop, including the
            header and all latch blocks.
        latches: Blocks containing back edges that target ``header``.
        exits: Successor blocks outside the loop that are reachable
            directly from a loop member.
        parent: The immediately enclosing natural loop, if any.
        children: Natural loops directly nested inside this loop.
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
    parent: Optional[NaturalLoop] = None
    children: list[NaturalLoop] = field(default_factory=list)

    @property
    def blocks(self) -> list[BasicBlock]:
        """Return loop members sorted by basic-block ID."""

        return sorted(self.members, key=lambda block: block.id)

    @property
    def latch_blocks(self) -> list[BasicBlock]:
        """Return loop latch blocks sorted by basic-block ID."""

        return sorted(self.latches, key=lambda block: block.id)

    @property
    def exit_blocks(self) -> list[BasicBlock]:
        """Return loop exit target blocks sorted by basic-block ID."""

        return sorted(self.exits, key=lambda block: block.id)

    @property
    def is_top_level(self) -> bool:
        """Return whether this loop is not nested inside another loop."""

        return self.parent is None

    @property
    def depth(self) -> int:
        """
        Return this loop's nesting depth.

        Top-level loops have depth ``0``. Each enclosing parent loop
        increases the depth by one.
        """

        depth = 0
        current = self.parent

        while current is not None:
            depth += 1
            current = current.parent

        return depth

    def __str__(self) -> str:
        return (
            "NaturalLoop("
            f"header={self.header.id}, "
            f"members={[block.id for block in self.blocks]}, "
            f"latches={[block.id for block in self.latch_blocks]}, "
            f"exits={[block.id for block in self.exit_blocks]}"
            ")"
        )
