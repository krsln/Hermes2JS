from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Dict, Set

from .BasicBlock import BasicBlock


class _IterativeSetAnalysis(ABC):

    def __init__(self, cfg):

        self.cfg = cfg

        self.result: Dict[BasicBlock, Set[BasicBlock]] = {}

    # -------------------------------------------------

    def compute(self):

        blocks = self.cfg.blocks

        roots = self.roots()

        #
        # initialize
        #

        for block in blocks:

            if block in roots:

                self.result[block] = {block}

            else:

                self.result[block] = set(blocks)

        #
        # iterate
        #

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

    # -------------------------------------------------

    @abstractmethod
    def roots(self):

        ...

    @abstractmethod
    def neighbors(self, block):

        ...