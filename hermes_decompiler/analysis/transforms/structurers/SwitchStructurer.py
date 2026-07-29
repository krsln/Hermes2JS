from __future__ import annotations

from hermes_decompiler.analysis.transforms.structurers._base import RegionStructurer


class SwitchStructurer(RegionStructurer):
    """
    Not yet implemented - switch/case blocks currently fall through as
    plain BasicBlocks with raw conditional jumps. Kept as an explicit
    no-op stub (rather than omitted) so StructuralAnalyzer's pipeline
    documents where switch structuring is meant to plug in.
    """

    def run(self):
        return
