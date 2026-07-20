from __future__ import annotations

from hermes_decompiler.cfg.ControlFlowGraph import ControlFlowGraph


class ImmediatePostDominatorAnalysis:
    """
    Computes the immediate post-dominator (ipdom) for each basic block.

    Mirrors ImmediateDominatorAnalysis, but walks the *post*-dominator
    sets produced by PostDominatorAnalysis instead of the dominator sets.

    The immediate post-dominator of a block is the closest block that
    every path from `block` to a function exit is guaranteed to pass
    through - it is the canonical "merge point" the region builder uses
    to know where an if/if-else region reconverges after branching.

    Exit blocks (no outgoing edges) have no immediate post-dominator.
    """

    @classmethod
    def build(
        cls,
        cfg: ControlFlowGraph,
        post_dominators: dict[int, set[int]],
    ) -> dict[int, int | None]:

        ipdom: dict[int, int | None] = {}

        for block in cfg:

            if not block.outgoing:
                ipdom[block.id] = None
                continue

            pdoms = post_dominators[block.id] - {block.id}

            immediate = None

            for candidate in pdoms:

                dominated_by_other = False

                for other in pdoms:

                    if other == candidate:
                        continue

                    #
                    # If another post-dominator post-dominates this
                    # candidate, candidate cannot be immediate.
                    #
                    if candidate in post_dominators[other]:
                        dominated_by_other = True
                        break

                if not dominated_by_other:
                    immediate = candidate
                    break

            ipdom[block.id] = immediate

        return ipdom
