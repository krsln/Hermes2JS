from __future__ import annotations

from dataclasses import dataclass, field

from hermes_decompiler.cfg.BasicBlock import BasicBlock


@dataclass(slots=True)
class ControlFlowGraph:
    blocks: dict[int, BasicBlock]
    entry: BasicBlock

    @classmethod
    def from_blocks(cls, blocks: list[BasicBlock]) -> "ControlFlowGraph":
        block_map = {b.start_addr: b for b in blocks}

        return cls(
            blocks=block_map,
            entry=blocks[0],
        )
