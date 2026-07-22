from __future__ import annotations

from ._IterativeSetAnalysis import _IterativeSetAnalysis


class DominatorTree(_IterativeSetAnalysis):

    def roots(self):

        return [self.cfg.entry]

    def neighbors(self, block):

        return block.predecessors