from __future__ import annotations

from hermes_decompiler.cfg.CFGAnalysis import CFGAnalysis
from hermes_decompiler.regions.model.Region import Region
from hermes_decompiler.regions.building._StructuralAnalyzer import StructuralAnalyzer


class RegionBuilder:
    """
    Converts a CFG (+ its analyses) into a hierarchical Region tree.

    Kept as a thin facade deliberately: callers (HermesAnalysis,
    tests) depend on this one stable `build()` entry point, while the
    structuring algorithm underneath - currently StructuralAnalyzer,
    with LoopStructurer/TryStructurer/MergePointResolver as its
    collaborators - is free to evolve without touching call sites.
    """

    @classmethod
    def build(cls, analysis: CFGAnalysis) -> Region:
        return StructuralAnalyzer(analysis).run()
