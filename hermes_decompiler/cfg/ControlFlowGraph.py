from __future__ import annotations

from dataclasses import dataclass

from hermes_decompiler.cfg.BasicBlock import BasicBlock


@dataclass(slots=True)
class ControlFlowGraph:
    """
    Directed control-flow graph.
    """

    blocks: dict[int, BasicBlock]

    entry: BasicBlock

    @classmethod
    def from_blocks(
        cls,
        blocks: list[BasicBlock],
    ) -> "ControlFlowGraph":

        mapping = {
            block.start_addr: block
            for block in blocks
        }

        return cls(
            blocks=mapping,
            entry=blocks[0],
        )

    def get_block(self, address: int) -> BasicBlock | None:
        return self.blocks.get(address)

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