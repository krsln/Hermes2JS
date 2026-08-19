from __future__ import annotations

from hermes_decompiler.analysis.models.regions import SequenceRegion


class SequenceStructurer:
    """
    Creates the root SequenceRegion from the CFG blocks.

    This bootstrapping step runs before RegionGraph exists, so it operates
    directly on the CFG rather than through a RegionStructurer.
    """

    def __init__(self, cfg):
        self.cfg = cfg

    def run(self) -> SequenceRegion:
        root = SequenceRegion()
        root.children.extend(self.cfg.blocks)

        return root
