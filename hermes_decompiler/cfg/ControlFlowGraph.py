from __future__ import annotations

from dataclasses import dataclass

from hermes_decompiler.cfg.BasicBlock import BasicBlock


@dataclass(slots=True)
class ControlFlowGraph:
    """
    Control Flow Graph consisting of BasicBlocks.
    """

    blocks: dict[int, BasicBlock]
    entry: BasicBlock

    def get_block(self, address: int) -> BasicBlock | None:
        return self.blocks.get(address)

    def contains(self, address: int) -> bool:
        return address in self.blocks

    def successors(self, block: BasicBlock) -> list[BasicBlock]:
        return [
            self.blocks[address]
            for address in block.successors
            if address in self.blocks
        ]

    def predecessors(self, block: BasicBlock) -> list[BasicBlock]:
        return [
            self.blocks[address]
            for address in block.predecessors
            if address in self.blocks
        ]