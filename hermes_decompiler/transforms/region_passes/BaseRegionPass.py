from __future__ import annotations

from abc import ABC, abstractmethod

from hermes_decompiler.analysis.models import RegionGraph


class RegionPass(ABC):
    """Base class for passes that rewrite/fold region-tree nodes in place.

    Operates on nodes an existing RegionStructurer already produced,
    without introducing a new region kind (see
    `structurers._base.RegionStructurer`'s own docstring for that
    distinction - passes that do build a new region kind belong there
    instead, not here).

    Standard interface: `__init__(graph, cfg)`, then `run()` mutates
    self.graph's tree in place and returns nothing - deliberately
    identical to RegionStructurer's contract, so StructuralAnalyzer can
    wire up every structurer and every region pass the same way
    (`SomePass(self.graph, self.cfg).run()`) without special-casing any
    individual one. A pass with no use for cfg (or, less commonly,
    graph beyond graph.root) simply doesn't reference it; the uniform
    signature still holds, so every pass stays interchangeable at the
    call site.
    """

    def __init__(self, graph: RegionGraph, cfg):
        self.graph = graph
        self.cfg = cfg

    @abstractmethod
    def run(self) -> None:
        """Mutate `self.graph`'s tree in place."""
        ...
