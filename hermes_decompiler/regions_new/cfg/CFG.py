from __future__ import annotations

from typing import List

from hermes_decompiler.models.OpcodeResult import OpcodeResult

from .BasicBlock import BasicBlock


class CFG:

    def __init__(self):
        self.blocks: List[BasicBlock] = []

        self.entry: BasicBlock | None = None

        self.dominator_tree = None

    @classmethod
    def from_results(cls, results: List[OpcodeResult]) -> "CFG":
        from .CFGBuilder import CFGBuilder
        from .DominatorTree import DominatorTree

        cfg = CFGBuilder().build(results)

        cfg.dominator_tree = DominatorTree(cfg)

        cfg.dominator_tree.compute()

        return cfg

    def dump(self):
        for block in self.blocks:
            print(f"\nBlock {block.id}")

            print(
                "  preds:",
                [b.id for b in block.predecessors]
            )

            print(
                "  succs:",
                [b.id for b in block.successors]
            )

            print(
                "  instructions:",
                [i.address for i in block.instructions]
            )