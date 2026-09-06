from __future__ import annotations

from hermes_decompiler.backend.analysis.cfg.CFG import CFG
from hermes_decompiler.backend.analysis.cfg.BasicBlock import BasicBlock
from hermes_decompiler.backend.analysis.dominance._iterative_set_analysis import _IterativeSetAnalysis


class DominatorTree(_IterativeSetAnalysis):
    """
    Classical iterative dominator analysis.

    Computes:

        dominators
        immediate dominator (idom)
        dominator tree
    """

    def __init__(self, cfg: CFG):
        super().__init__(cfg)

        self.dominators: dict[BasicBlock, set[BasicBlock]] = {}

        self.idom: dict[BasicBlock, BasicBlock | None] = {}

        self.children: dict[BasicBlock, list[BasicBlock]] = {}

    # ---------------------------------------------------------

    def roots(self):
        return [self.cfg.entry]

    # ---------------------------------------------------------

    def neighbors(self, block):
        return block.predecessors

    # ---------------------------------------------------------

    def compute(self):
        super().compute()

        #
        # alias
        #

        self.dominators = self.result

        self.idom = self.compute_immediate()

        self.children = self.build_tree(self.idom)

    # ---------------------------------------------------------

    def dominates(
            self,
            dominator: BasicBlock,
            block: BasicBlock,
    ) -> bool:
        return dominator in self.dominators.get(block, set())

    # ---------------------------------------------------------

    def immediate_dominator(
            self,
            block: BasicBlock,
    ) -> BasicBlock | None:
        return self.idom.get(block)

    # ---------------------------------------------------------

    def dominated_children(
            self,
            block: BasicBlock,
    ) -> list[BasicBlock]:
        return self.children.get(block, [])
