from __future__ import annotations

from typing import List

from hermes_decompiler.models.OpcodeResult import OpcodeResult


class BasicBlock:
    """
    Basic Control Flow Graph block.

    Phase-1:
        - Contains a linear list of instructions.
        - CFG edges will be added later.
    """

    def __init__(self, block_id: int):
        self.id = block_id

        self.instructions: List[OpcodeResult] = []

        self.predecessors: List["BasicBlock"] = []

        self.successors: List["BasicBlock"] = []

    def add_instruction(self, result: OpcodeResult) -> None:
        self.instructions.append(result)

    def __repr__(self) -> str:
        return f"BasicBlock(id={self.id}, instructions={len(self.instructions)})"