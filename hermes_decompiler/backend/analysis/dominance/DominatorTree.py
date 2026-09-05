from __future__ import annotations

from typing import Dict, List, Optional, Set

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

        self.dominators: Dict[BasicBlock, Set[BasicBlock]] = {}

        self.idom: Dict[BasicBlock, Optional[BasicBlock]] = {}

        self.children: Dict[BasicBlock, List[BasicBlock]] = {}

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
    ) -> Optional[BasicBlock]:
        return self.idom.get(block)

    # ---------------------------------------------------------

    def dominated_children(
            self,
            block: BasicBlock,
    ) -> List[BasicBlock]:
        return self.children.get(block, [])
