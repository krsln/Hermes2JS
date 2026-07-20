from dataclasses import dataclass, field

from hermes_decompiler.cfg.BasicBlock import BasicBlock


@dataclass(slots=True)
class ControlFlowGraph:
    """
    Represents the Control Flow Graph (CFG) of a single Hermes function.
    """

    blocks: list[BasicBlock] = field(default_factory=list)

    @property
    def entry_block(self) -> BasicBlock | None:
        return self.blocks[0] if self.blocks else None

    @property
    def exit_blocks(self) -> list[BasicBlock]:
        return [b for b in self.blocks if not b.successors]

    def get_block(self, address: int) -> BasicBlock | None:
        return next(
            (b for b in self.blocks if b.start_addr == address),
            None,
        )

    def get_next_block(self, block: BasicBlock) -> BasicBlock | None:
        try:
            index = self.blocks.index(block)
        except ValueError:
            return None

        if index + 1 >= len(self.blocks):
            return None

        return self.blocks[index + 1]

    def __iter__(self):
        return iter(self.blocks)

    def __len__(self):
        return len(self.blocks)

    def __getitem__(self, index: int) -> BasicBlock:
        return self.blocks[index]
