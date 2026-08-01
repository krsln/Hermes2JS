from __future__ import annotations

from abc import ABC, abstractmethod

from hermes_decompiler.analysis.regions.RegionGraph import RegionGraph


class RegionStructurer(ABC):
    """
    Base class for every pass that BUILDS a new region-tree node type
    (`IfRegion`, `LoopRegion`, `TryRegion`, `SwitchRegion`, ...) out of
    raw `BasicBlock`s or existing regions, via `RegionGraph` mutation.

    Standard interface: `__init__(graph, cfg)`, then `run()` mutates
    `self.graph`'s tree in place and returns nothing. Every structurer
    is stateless between `run()` calls and safe to construct fresh
    per `StructuralAnalyzer.build()` invocation (see that class - it's
    the only place these are ever wired together).

    Passes that only rewrite/fold nodes an existing structurer already
    produced, without introducing a new region *kind*, do NOT belong
    here - see `transforms/region_passes/` (e.g. `BooleanChainFolder`,
    `LoopConditionExtractor`).

    `SequenceStructurer` is the one exception in this package: it
    bootstraps the region tree's root before any `RegionGraph` exists,
    so it can't take one as a constructor argument and doesn't extend
    this class - see its own docstring.
    """

    def __init__(self, graph: RegionGraph, cfg):
        self.graph = graph
        self.cfg = cfg

    @abstractmethod
    def run(self) -> None:
        """Mutate `self.graph`'s tree in place."""
        ...
