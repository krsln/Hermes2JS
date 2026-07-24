from __future__ import annotations

from typing import List, Optional

from hermes_decompiler.models.OpcodeResult import OpcodeResult

from .BasicBlock import BasicBlock


class CFG:

    def __init__(self):

        self.loop_analysis = None
        self.blocks: List[BasicBlock] = []

        self.entry: Optional[BasicBlock] = None

        self.dominator_tree = None
        self.post_dominator_tree = None

    @classmethod
    def from_results(cls, results: List[OpcodeResult]) -> "CFG":

        from .CFGBuilder import CFGBuilder

        return CFGBuilder().build(results)

    # ---------------------------------------------------------

    def verify(self):

        from .CFGVerifier import CFGVerifier

        CFGVerifier(self).verify()

    # ---------------------------------------------------------

    def compute_dominators(self):

        from .DominatorTree import DominatorTree

        self.dominator_tree = DominatorTree(self)

        self.dominator_tree.compute()

    # ---------------------------------------------------------

    def compute_post_dominators(self):

        from .PostDominatorTree import PostDominatorTree

        self.post_dominator_tree = PostDominatorTree(self)

        self.post_dominator_tree.compute()

    def compute_loops(self):
        from hermes_decompiler.regions.cfg.LoopAnalysis import LoopAnalysis

        self.loop_analysis = LoopAnalysis(self)

        self.loop_analysis.compute()