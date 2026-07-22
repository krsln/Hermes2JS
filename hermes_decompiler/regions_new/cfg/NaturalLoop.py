from __future__ import annotations

from dataclasses import dataclass, field

from hermes_decompiler.regions_new.cfg.BasicBlock import BasicBlock


@dataclass(slots=True)
class NaturalLoop:
    """
    Represents one natural loop.

    Initially only header/tail/members are computed.

    Later we'll populate:

      - exits
      - latches
      - continue targets
      - break targets
      - loop kind (while / do-while / for)
    """

    header: BasicBlock
    tail: BasicBlock

    members: set[BasicBlock] = field(default_factory=set)

    exits: set[BasicBlock] = field(default_factory=set)

    latches: set[BasicBlock] = field(default_factory=set)

    @property
    def blocks(self):
        return sorted(self.members, key=lambda b: b.id)

    def __str__(self):

        ids = [b.id for b in self.blocks]

        return (
            f"NaturalLoop("
            f"header={self.header.id}, "
            f"tail={self.tail.id}, "
            f"members={ids}"
            f")"
        )