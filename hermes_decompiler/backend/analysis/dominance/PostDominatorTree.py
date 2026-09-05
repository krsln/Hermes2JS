from __future__ import annotations

from typing import Dict, List, Optional

from hermes_decompiler.backend.analysis.cfg.BasicBlock import BasicBlock
from hermes_decompiler.backend.analysis.dominance._iterative_set_analysis import _IterativeSetAnalysis


class PostDominatorTree(_IterativeSetAnalysis):

    def __init__(self, cfg):
        super().__init__(cfg)

        self.immediate_post_dominators: Dict[BasicBlock, Optional[BasicBlock]] = {}
        self.children: Dict[BasicBlock, List[BasicBlock]] = {}

    def roots(self):
        #
        # all exits
        #

        return [

            b

            for b in self.cfg.blocks

            if not b.successors

        ]

    def neighbors(self, block):
        return block.successors

    # ---------------------------------------------------------

    def compute(self):
        super().compute()

        self.immediate_post_dominators = self.compute_immediate()
        self.children = self.build_tree(self.immediate_post_dominators)

    # ---------------------------------------------------------

    def post_dominates(
            self,
            post_dominator: BasicBlock,
            block: BasicBlock,
    ) -> bool:
        return post_dominator in self.result.get(block, set())

    def immediate_post_dominator(
            self,
            block: BasicBlock,
    ) -> Optional[BasicBlock]:
        return self.immediate_post_dominators.get(block)

    def dominated_children(
            self,
            block: BasicBlock,
    ) -> List[BasicBlock]:
        """
        Children of `block` in the post-dominator tree - the post-dominator
        analogue of `DominatorTree.dominated_children`. Named the same
        (rather than e.g. `post_dominated_children`) so both trees expose
        an identical, interchangeable API for any pass that walks either
        one generically.
        """

        return self.children.get(block, [])
