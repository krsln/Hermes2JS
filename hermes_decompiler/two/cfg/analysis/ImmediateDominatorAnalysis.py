from __future__ import annotations

from hermes_decompiler.two.cfg.ControlFlowGraph import ControlFlowGraph


class ImmediateDominatorAnalysis:
    """
    Computes the immediate dominator (idom) for each basic block.

    The result is a mapping:

        block -> immediate dominator

    The entry block has no immediate dominator.
    """

    @classmethod
    def build(
        cls,
        cfg: ControlFlowGraph,
        dominators: dict[int, set[int]],
    ) -> dict[int, int | None]:

        idom: dict[int, int | None] = {
            cfg.entry.id: None,
        }

        for block in cfg:

            if block == cfg.entry:
                continue

            doms = dominators[block.id] - {block.id}

            immediate = None

            for candidate in doms:

                dominated_by_other = False

                for other in doms:

                    if other == candidate:
                        continue

                    #
                    # If another dominator dominates this candidate,
                    # candidate cannot be immediate.
                    #
                    if candidate in dominators[other]:
                        dominated_by_other = True
                        break

                if not dominated_by_other:
                    immediate = candidate
                    break

            idom[block.id] = immediate

        return idom