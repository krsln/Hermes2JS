from __future__ import annotations

from hermes_decompiler.two.cfg.BasicBlock import BasicBlock
from hermes_decompiler.two.cfg.ControlFlowGraph import ControlFlowGraph


class DominatorAnalysis:
    """
    Computes dominator sets for every BasicBlock.

    Algorithm:
        Iterative data-flow analysis.
    """

    @classmethod
    def build(
            cls,
            cfg: ControlFlowGraph,
            reverse_post_order: list[BasicBlock],
    ) -> dict[int, set[int]]:

        blocks = list(cfg)

        all_nodes = {
            block.id
            for block in blocks
        }

        dominators: dict[int, set[int]] = {}

        #
        # Initialization
        #

        for block in blocks:

            if block == cfg.entry:
                dominators[block.id] = {
                    block.id
                }
            else:
                dominators[block.id] = set(all_nodes)

        changed = True

        while changed:

            changed = False

            #
            # Skip entry
            #

            for block in reverse_post_order[1:]:

                predecessors = [
                    cfg.get_block(edge.source)
                    for edge in block.incoming
                ]

                predecessors = [
                    p
                    for p in predecessors
                    if p is not None
                ]

                if not predecessors:
                    continue

                new_dom = set.intersection(
                    *(
                        dominators[p.id]
                        for p in predecessors
                    )
                )

                new_dom.add(block.id)

                if new_dom != dominators[block.id]:
                    dominators[block.id] = new_dom

                    changed = True

        return dominators
