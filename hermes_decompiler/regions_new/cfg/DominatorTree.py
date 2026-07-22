from __future__ import annotations

from typing import Dict, Set

from .CFG import CFG
from .BasicBlock import BasicBlock


class DominatorTree:
    """
    Classical iterative dominator analysis.

    Phase-1

        Computes only dominator sets.

    Immediate dominators
    will be added next.
    """

    def __init__(self, cfg: CFG):

        self.cfg = cfg

        self.dominators: Dict[BasicBlock, Set[BasicBlock]] = {}

    # --------------------------------------------------------

    def compute(self):

        blocks = self.cfg.blocks

        entry = self.cfg.entry

        if entry is None:
            return

        #
        # initialization
        #

        for block in blocks:

            if block is entry:
                self.dominators[block] = {block}

            else:
                self.dominators[block] = set(blocks)

        #
        # fixed point
        #

        changed = True

        while changed:

            changed = False

            for block in blocks:

                if block is entry:
                    continue

                if not block.predecessors:
                    continue

                new_dom = set(blocks)

                for pred in block.predecessors:

                    new_dom &= self.dominators[pred]

                new_dom.add(block)

                if new_dom != self.dominators[block]:

                    self.dominators[block] = new_dom

                    changed = True