from __future__ import annotations

from typing import List, Optional, Dict, Tuple, TYPE_CHECKING

from hermes_decompiler.analysis.cfg import BasicBlock
from hermes_decompiler.frontend.opcode import OpcodeResult

if TYPE_CHECKING:
    from hermes_decompiler.analysis.dominance.DominatorTree import DominatorTree
    from hermes_decompiler.analysis.dominance.PostDominatorTree import PostDominatorTree
    from hermes_decompiler.analysis.loops.LoopAnalysis import LoopAnalysis


class CFG:

    def __init__(self):
        self.loop_analysis: Optional["LoopAnalysis"] = None
        self.blocks: List[BasicBlock] = []

        self.entry: Optional[BasicBlock] = None

        self.dominator_tree: Optional["DominatorTree"] = None
        self.post_dominator_tree: Optional["PostDominatorTree"] = None

        self.exception_handlers: list[dict] = []

        # dest_reg -> [(address, BasicBlock, OpcodeResult), ...]
        # Entries are stored in program order. Unlike
        # HermesAnalysis.registers, this preserves every register
        # definition along with the BasicBlock where it occurs, rather
        # than only the latest definition.
        #
        # CFGBuilder populates this mapping in a single pass for
        # reaching-definition-style queries, such as detecting loop
        # induction registers and distinguishing initializers from
        # updates.
        self.reg_definitions: Dict[
            int, List[Tuple[int, BasicBlock, OpcodeResult]]
        ] = {}

    @classmethod
    def from_results(cls, results: List[OpcodeResult], exception_handlers: list[dict] | None = None) -> "CFG":
        from hermes_decompiler.analysis.cfg.CFGBuilder import CFGBuilder

        return CFGBuilder().build(results, exception_handlers or [])

    def verify(self):
        from hermes_decompiler.analysis.cfg.CFGVerifier import CFGVerifier

        CFGVerifier(self).verify()

    def compute_dominators(self) -> None:
        from hermes_decompiler.analysis.dominance.DominatorTree import DominatorTree

        dominator_tree = DominatorTree(self)
        dominator_tree.compute()
        self.dominator_tree = dominator_tree

    def compute_post_dominators(self) -> None:
        from hermes_decompiler.analysis.dominance.PostDominatorTree import PostDominatorTree

        post_dominator_tree = PostDominatorTree(self)
        post_dominator_tree.compute()
        self.post_dominator_tree = post_dominator_tree

    def compute_loops(self) -> None:
        from hermes_decompiler.analysis.loops.LoopAnalysis import LoopAnalysis

        loop_analysis = LoopAnalysis(self)
        loop_analysis.compute()
        self.loop_analysis = loop_analysis
