from __future__ import annotations

from dataclasses import dataclass

from hermes_decompiler.two.cfg.BasicBlock import BasicBlock


@dataclass(slots=True)
class ControlFlowGraph:
    """
    Control Flow Graph.

    Owns all BasicBlocks of a function.
    """

    blocks: dict[int, BasicBlock]

    @classmethod
    def from_blocks(cls, blocks: list[BasicBlock]) -> "ControlFlowGraph":
        return cls(
            {
                block.start_addr: block
                for block in blocks
            }
        )

    @property
    def entry(self) -> BasicBlock:
        return next(iter(self.blocks.values()))

    def get_block(self, address: int) -> BasicBlock | None:
        return self.blocks.get(address)

    @property
    def exit_blocks(self) -> list[BasicBlock]:
        return [
            block
            for block in self
            if not block.outgoing
        ]

    def ordered_blocks(self) -> list[BasicBlock]:
        return sorted(
            self.blocks.values(),
            key=lambda block: block.start_addr,
        )

    def __iter__(self):
        return iter(self.blocks.values())

    def __len__(self):
        return len(self.blocks)