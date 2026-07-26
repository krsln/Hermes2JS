from __future__ import annotations

from typing import Dict, Optional

from ._IterativeSetAnalysis import _IterativeSetAnalysis
from .BasicBlock import BasicBlock


class PostDominatorTree(_IterativeSetAnalysis):

    def __init__(self, cfg):
        super().__init__(cfg)

        self.ipdom: Dict[BasicBlock, Optional[BasicBlock]] = {}

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

        self.ipdom = self.compute_immediate()

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
        return self.ipdom.get(block)
