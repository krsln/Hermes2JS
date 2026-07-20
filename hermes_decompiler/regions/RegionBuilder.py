from __future__ import annotations

from hermes_decompiler.cfg.ControlFlowGraph import ControlFlowGraph
from hermes_decompiler.regions.SequenceRegion import SequenceRegion


class RegionBuilder:
    """
    Builds the initial Region tree from a ControlFlowGraph.

    The first implementation performs no structural analysis and simply
    converts every reachable basic block into a SequenceRegion.

    Later passes will progressively replace parts of this tree with
    IfRegion, LoopRegion, TryRegion, SwitchRegion, etc.
    """

    @classmethod
    def build(cls, graph: ControlFlowGraph) -> SequenceRegion:
        region = SequenceRegion()

        for block in graph.blocks:
            region.blocks.append(block)

        return region