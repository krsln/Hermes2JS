from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Dict, Set
from .BasicBlock import BasicBlock


class _IterativeSetAnalysis(ABC):

    def __init__(self, cfg):

        self.cfg = cfg

        self.result: Dict[BasicBlock, Set[BasicBlock]] = {}

    def compute(self):

        blocks = self.cfg.blocks
        roots = self.roots()

        for block in blocks:
            if block in roots:
                self.result[block] = {block}
            else:
                self.result[block] = set(blocks)

        changed = True

        while changed:
            changed = False
            for block in blocks:
                if block in roots:
                    continue

                neighbors = self.neighbors(block)

                if not neighbors:
                    continue

                it = iter(neighbors)
                new_set = self.result[next(it)].copy()

                for n in it:
                    new_set &= self.result[n]

                new_set.add(block)

                if new_set != self.result[block]:
                    self.result[block] = new_set
                    changed = True

    @abstractmethod
    def roots(self):
        ...

    @abstractmethod
    def neighbors(self, block):
        ...

    def compute_immediate(self) -> Dict[BasicBlock, "BasicBlock | None"]:
        """
        Generic 'immediate' relation derived from `self.result` (the set
        of dominators/post-dominators per block, already computed by
        `compute()`): for each non-root block, the strict
        dominator/post-dominator that isn't itself dominated/post-
        dominated by any other strict one - i.e. the closest one.

        Shared by `DominatorTree` (immediate dominator) and
        `PostDominatorTree` (immediate post-dominator); the math is
        identical, only `self.result`/`roots()` differ.
        """

        roots = set(self.roots())
        immediate: Dict[BasicBlock, "BasicBlock | None"] = {}

        for block in self.cfg.blocks:

            if block in roots:
                immediate[block] = None
                continue

            strict = self.result[block] - {block}
            candidate = None

            for c in strict:
                if all(c not in self.result[other] for other in strict if other is not c):
                    candidate = c
                    break

            immediate[block] = candidate

        return immediate
