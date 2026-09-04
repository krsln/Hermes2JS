from __future__ import annotations

from hermes_decompiler.backend.regions import SequenceRegion


class SequenceStructurer:
    """
    Bootstraps the root SequenceRegion from the CFG's flat blocklist.

    Runs before RegionGraph exists, so it operates directly on the CFG
    rather than extending RegionStructurer.
    """

    def __init__(self, cfg):
        self.cfg = cfg

    def run(self) -> SequenceRegion:
        root = SequenceRegion()
        root.children.extend(self.cfg.blocks)

        return root
