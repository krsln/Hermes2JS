from __future__ import annotations

from ._IterativeSetAnalysis import _IterativeSetAnalysis


class PostDominatorTree(_IterativeSetAnalysis):

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