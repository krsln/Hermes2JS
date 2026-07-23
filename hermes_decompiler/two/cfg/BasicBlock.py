from dataclasses import dataclass, field

from hermes_decompiler.two.cfg.BlockType import BlockType
from hermes_decompiler.two.cfg.CFGEdge import CFGEdge
from hermes_decompiler.models.OpcodeResult import OpcodeResult


@dataclass(slots=True)
class BasicBlock:
    """
    Linear sequence of instructions with a single entry point.
    """

    start_addr: int
    end_addr: int = 0

    instructions: list[OpcodeResult] = field(default_factory=list)

    incoming: list[CFGEdge] = field(default_factory=list)
    outgoing: list[CFGEdge] = field(default_factory=list)

    block_type: BlockType = BlockType.NORMAL

    @property
    def id(self) -> int:
        return self.start_addr
