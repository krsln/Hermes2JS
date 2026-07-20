from __future__ import annotations

from hermes_decompiler.cfg.BasicBlock import BasicBlock
from hermes_decompiler.cfg.ControlFlowGraph import ControlFlowGraph


class PostDominatorAnalysis:
    """
    Computes post-dominator sets for every basic block.

    A block post-dominates another block if every path from that block to
    function exit passes through it.
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

        exit_blocks = [
            block
            for block in blocks
            if not block.outgoing
        ]

        postdom: dict[int, set[int]] = {}

        #
        # Initialization
        #

        for block in blocks:

            if block in exit_blocks:
                postdom[block.id] = {block.id}
            else:
                postdom[block.id] = set(all_nodes)

        changed = True

        while changed:

            changed = False

            #
            # Traverse backwards
            #

            for block in reversed(reverse_post_order):

                if block in exit_blocks:
                    continue

                successors = [
                    cfg.get_block(edge.target)
                    for edge in block.outgoing
                ]

                successors = [
                    b
                    for b in successors
                    if b is not None
                ]

                if not successors:
                    continue

                new_set = set.intersection(
                    *(
                        postdom[s.id]
                        for s in successors
                    )
                )

                new_set.add(block.id)

                if new_set != postdom[block.id]:
                    postdom[block.id] = new_set

                    changed = True

        return postdom
