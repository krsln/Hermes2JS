from __future__ import annotations

from hermes_decompiler.analysis.models.regions import SequenceRegion


class SequenceStructurer:
    """
    Bootstraps the region tree's root SequenceRegion directly from the
    CFG's flat block list - the one structurer that does NOT extend
    `RegionStructurer`, because no `RegionGraph` exists yet for it to
    take as a constructor argument (it's what `RegionGraph` gets built
    from, in `StructuralAnalyzer.build()`).
    """

    def __init__(self, cfg):
        self.cfg = cfg

    def run(self) -> SequenceRegion:
        root = SequenceRegion()
        root.children.extend(self.cfg.blocks)

        return root
