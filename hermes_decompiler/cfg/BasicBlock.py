from __future__ import annotations

from dataclasses import dataclass, field

from hermes_decompiler.cfg.BlockType import BlockType
from hermes_decompiler.models.OpcodeResult import OpcodeResult


@dataclass(slots=True)
class BasicBlock:
    """
    Linear sequence of instructions with a single entry point.
    """

    start_addr: int
    end_addr: int = 0

    instructions: list[OpcodeResult] = field(default_factory=list)

    predecessors: set[int] = field(default_factory=set)
    successors: set[int] = field(default_factory=set)

    block_type: BlockType = BlockType.NORMAL

    @property
    def id(self) -> int:
        return self.start_addr

    @property
    def first(self) -> OpcodeResult:
        return self.instructions[0]

    @property
    def last(self) -> OpcodeResult:
        return self.instructions[-1]

    @property
    def successor_count(self) -> int:
        return len(self.successors)

    @property
    def predecessor_count(self) -> int:
        return len(self.predecessors)

    @property
    def is_conditional(self) -> bool:
        return self.successor_count == 2

    @property
    def is_unconditional(self) -> bool:
        return self.successor_count == 1

    @property
    def is_terminal(self) -> bool:
        return self.successor_count == 0
