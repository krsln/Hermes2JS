from __future__ import annotations
from dataclasses import dataclass, field
from enum import Enum, auto
from typing import List, Dict, Set, Optional, Any


class BlockType(Enum):
    STANDARD = auto()
    HEADER = auto()  # Loop header
    EXIT = auto()


@dataclass
class BasicBlock:
    id: int
    start_addr: int
    end_addr: int
    results: List[Any] = field(default_factory=list)
    predecessors: Set[BasicBlock] = field(default_factory=set)
    successors: Set[BasicBlock] = field(default_factory=set)
    block_type: BlockType = BlockType.STANDARD
    is_loop_header: bool = False
    loop_latch: Optional[BasicBlock] = None

    def add_successor(self, target: BasicBlock):
        self.successors.add(target)
        target.predecessors.add(self)

    def __hash__(self):
        return hash(self.id)

    def __repr__(self):
        return f"Block(id={self.id}, addr={self.start_addr}-{self.end_addr})"
