from __future__ import annotations

from abc import ABC, abstractmethod

from hermes_decompiler.analysis.models import RegionGraph


class RegionPass(ABC):
    """
    Base class for every pass that rewrites/folds region-tree nodes an
    existing `RegionStructurer` already produced, WITHOUT introducing
    a new region *kind* (see `structurers._base.RegionStructurer`'s own
    docstring for that distinction - passes that DO build a new region
    kind belong there instead, not here).

    Standard interface: `__init__(graph, cfg)`, then `run()` mutates
    `self.graph`'s tree in place and returns nothing - deliberately
    identical to `RegionStructurer`'s contract, so `StructuralAnalyzer`
    can wire up every structurer AND every region pass the same way
    (`SomePass(self.graph, self.cfg).run()`) without special-casing
    any individual one.

    This uniformity didn't exist before: the five region passes this
    package used to have each took a different constructor shape
    (`cfg` only, `graph` only, or the bare region-tree `root`) and two
    different `run()` shapes (`run(root)` vs. `run()`), forcing
    `StructuralAnalyzer` to hand-wire each call site differently - and
    making it unclear what a sixth pass should copy. A pass that
    genuinely has no use for `cfg` (or, less commonly, `graph` beyond
    `graph.root`) simply doesn't reference it; the uniform signature
    still holds so every pass is interchangeable at the call site.
    """

    def __init__(self, graph: RegionGraph, cfg):
        self.graph = graph
        self.cfg = cfg

    @abstractmethod
    def run(self) -> None:
        """Mutate `self.graph`'s tree in place."""
        ...