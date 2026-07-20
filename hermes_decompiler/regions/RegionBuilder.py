from hermes_decompiler.cfg.ControlFlowGraph import ControlFlowGraph
from hermes_decompiler.regions.SequenceRegion import SequenceRegion


class RegionBuilder:

    @classmethod
    def build(cls, cfg: ControlFlowGraph):

        blocks = sorted(
            cfg.blocks.values(),
            key=lambda block: block.start_addr,
        )

        return SequenceRegion(blocks)