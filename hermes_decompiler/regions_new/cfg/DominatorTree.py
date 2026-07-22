from __future__ import annotations

from typing import Dict, List, Optional, Set

from .CFG import CFG
from .BasicBlock import BasicBlock
from ._IterativeSetAnalysis import _IterativeSetAnalysis


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

        self._compute_immediate_dominators()

        self._build_tree()

    # ---------------------------------------------------------

    def _compute_immediate_dominators(self):

        self.idom.clear()

        entry = self.cfg.entry

        if entry is None:
            return

        self.idom[entry] = None

        for block in self.cfg.blocks:

            if block is entry:
                continue

            strict_doms = self.dominators[block] - {block}

            immediate = None

            #
            # Immediate dominator =
            # strict dominator that is not dominated
            # by any other strict dominator.
            #

            for candidate in strict_doms:

                if all(
                    candidate not in self.dominators[other]
                    for other in strict_doms
                    if other is not candidate
                ):
                    immediate = candidate
                    break

            self.idom[block] = immediate

    # ---------------------------------------------------------

    def _build_tree(self):

        self.children = {
            block: []
            for block in self.cfg.blocks
        }

        for block, parent in self.idom.items():

            if parent is None:
                continue

            self.children[parent].append(block)

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