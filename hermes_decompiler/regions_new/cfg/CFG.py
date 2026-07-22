from __future__ import annotations

from typing import List

from hermes_decompiler.models.OpcodeResult import OpcodeResult

from .BasicBlock import BasicBlock


class CFG:
    """
    Control Flow Graph.

    Phase-1:

        results
            ↓
        one BasicBlock

    Later this will split blocks using jump targets.
    """

    def __init__(self):
        self.blocks: List[BasicBlock] = []

        self.entry: BasicBlock | None = None

    @classmethod
    def from_results(cls, results: List[OpcodeResult]) -> "CFG":
        cfg = cls()

        block = BasicBlock(0)

        for result in results:
            block.add_instruction(result)

        cfg.blocks.append(block)
        cfg.entry = block

        return cfg