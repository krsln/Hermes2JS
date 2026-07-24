from __future__ import annotations

from typing import List

from hermes_decompiler.models.OpcodeResult import OpcodeResult


class BasicBlock:

    def __init__(self, block_id: int):
        self.id = block_id

        self.instructions: List[OpcodeResult] = []

        self.predecessors: List["BasicBlock"] = []

        self.successors: List["BasicBlock"] = []

    def add_instruction(self, result: OpcodeResult):
        self.instructions.append(result)

    @property
    def first(self):
        return self.instructions[0]

    @property
    def last(self):
        return self.instructions[-1]

    def __len__(self):
        return len(self.instructions)

    def __repr__(self):
        return f"Block({self.id})"

    def __hash__(self):
        return hash(self.id)

    def __eq__(self, other):
        return isinstance(other, BasicBlock) and self.id == other.id
