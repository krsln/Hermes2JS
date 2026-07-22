from __future__ import annotations

from typing import List, Tuple

from .CFG import CFG
from .BasicBlock import BasicBlock


class LoopAnalysis:

    """
    Loop analysis.

    Stage-1

        Detect back edges.

    Natural loop discovery will be added
    in the next stage.
    """

    def __init__(self, cfg: CFG):

        self.cfg = cfg

        self.back_edges: List[Tuple[BasicBlock, BasicBlock]] = []

    # ---------------------------------------------------------

    def compute(self):

        self.back_edges.clear()

        tree = self.cfg.dominator_tree

        if tree is None:
            return

        for tail in self.cfg.blocks:

            for header in tail.successors:

                if header is tail:
                    continue
                #
                # Back edge:
                #
                # header dominates tail
                #

                if tree.dominates(header, tail):

                    self.back_edges.append(
                        (
                            tail,
                            header,
                        )
                    )