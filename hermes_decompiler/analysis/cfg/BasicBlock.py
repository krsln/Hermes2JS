from __future__ import annotations

from typing import List

from hermes_decompiler.analysis.terminators import Terminator
from hermes_decompiler.opcode import OpcodeResult


class BasicBlock:

    def __init__(self, block_id: int, address: int):
        self.id = block_id
        self.address = address

        self.instructions: List[OpcodeResult] = []
        self.terminator: Terminator | None = None

        self.predecessors: List["BasicBlock"] = []
        self.successors: List["BasicBlock"] = []

    @property
    def first_instruction(self) -> OpcodeResult | None:
        return self.instructions[0] if self.instructions else None

    @property
    def last_instruction(self) -> OpcodeResult | None:
        return self.instructions[-1] if self.instructions else None

    def add_instruction(self, result: OpcodeResult):
        self.instructions.append(result)
