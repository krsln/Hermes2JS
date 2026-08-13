from __future__ import annotations

from typing import List, Optional, Dict

from hermes_decompiler.analysis.cfg import BasicBlock
from hermes_decompiler.frontend.opcode import OpcodeResult


class CFG:

    def __init__(self):
        self.loop_analysis = None
        self.blocks: List[BasicBlock] = []

        self.entry: Optional[BasicBlock] = None

        self.dominator_tree = None
        self.post_dominator_tree = None

        self.exception_handlers: list[dict] = []

        # dest_reg -> [(address, BasicBlock, OpcodeResult), ...]
        # program-order sırasında. HermesAnalysis.registers'ın aksine
        # yalnızca SON tanımı değil, register'ın tüm tanımlarını,
        # hangi BasicBlock'ta olduklarıyla birlikte tutar. reaching-
        # definition tarzı sorgular (loop induction register tespiti,
        # initializer/update ayrıştırma) için CFGBuilder tarafından
        # tek geçişte doldurulur.
        self.reg_definitions: Dict[int, List[Tuple[int, BasicBlock, OpcodeResult]]] = {}

    @classmethod
    def from_results(cls, results: List[OpcodeResult], exception_handlers: list[dict] | None = None) -> "CFG":
        from hermes_decompiler.analysis.cfg.CFGBuilder import CFGBuilder

        return CFGBuilder().build(results, exception_handlers or [])

    # ---------------------------------------------------------

    def verify(self):
        from hermes_decompiler.analysis.cfg.CFGVerifier import CFGVerifier

        CFGVerifier(self).verify()

    # ---------------------------------------------------------

    def compute_dominators(self):
        from hermes_decompiler.analysis.dominance.DominatorTree import DominatorTree

        self.dominator_tree = DominatorTree(self)

        self.dominator_tree.compute()

    # ---------------------------------------------------------

    def compute_post_dominators(self):
        from hermes_decompiler.analysis.dominance.PostDominatorTree import PostDominatorTree

        self.post_dominator_tree = PostDominatorTree(self)

        self.post_dominator_tree.compute()

    def compute_loops(self):
        from hermes_decompiler.analysis.loops.LoopAnalysis import LoopAnalysis

        self.loop_analysis = LoopAnalysis(self)

        self.loop_analysis.compute()
