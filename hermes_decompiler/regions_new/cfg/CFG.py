from __future__ import annotations

from typing import List

from hermes_decompiler.models.OpcodeResult import OpcodeResult

from .BasicBlock import BasicBlock


class CFG:

    def __init__(self):
        self.blocks: List[BasicBlock] = []

        self.entry: BasicBlock | None = None

    @classmethod
    def from_results(cls, results: List[OpcodeResult]) -> "CFG":
        from .CFGBuilder import CFGBuilder

        return CFGBuilder().build(results)
