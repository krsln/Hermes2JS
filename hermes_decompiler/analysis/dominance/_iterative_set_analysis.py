from __future__ import annotations

from abc import ABC, abstractmethod
from collections.abc import Iterable
from typing import Dict, Set

from hermes_decompiler.analysis.cfg.BasicBlock import BasicBlock


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

                neighbors = list(self.neighbors(block))

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
    def roots(self) -> Iterable[BasicBlock]:
        ...

    @abstractmethod
    def neighbors(self, block: BasicBlock) -> Iterable[BasicBlock]:
        ...

    def compute_immediate(self) -> Dict[BasicBlock, BasicBlock | None]:
        """
        Computes the immediate dominator or post-dominator for each block.

        The relation is derived from `self.result`, which contains the
        dominator or post-dominator set for each block.

        For each non-root block, the immediate relation is the strict
        dominator or post-dominator that is closest to the block.

        This implementation is shared by `DominatorTree` and
        `PostDominatorTree`; only `self.result` and `roots()` differ.
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
