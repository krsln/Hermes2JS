from __future__ import annotations

import logging
from abc import ABC, abstractmethod

from hermes_decompiler.analysis.cfg import BasicBlock
from hermes_decompiler.analysis.regions.RegionGraph import RegionGraph
from hermes_decompiler.core.logging import get_logger

logger = get_logger(__name__)


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

    def dump_region_tree_if_debug(self, label: str) -> None:
        """
        Logs the current region tree shape at DEBUG level, prefixed
        with `label` (e.g. the calling structurer's class name) so
        multiple dumps in the same run - one per structurer, taken
        immediately after each one finishes - can be told apart and
        diffed against each other to see exactly which pass moved a
        given block. No-op (skips even building the string) unless
        DEBUG logging is enabled.
        """
        if not logger.isEnabledFor(logging.DEBUG):
            return

        logger.debug("===== REGION TREE: after %s =====", label)
        self._dump_region_tree(self.graph.root)

    def _dump_region_tree(self, node, indent: int = 0) -> None:
        from hermes_decompiler.analysis.regions.Regions import SequenceRegion, LoopRegion

        prefix = " " * indent

        if isinstance(node, SequenceRegion):
            logger.debug("%sSequenceRegion", prefix)
            for child in node.children:
                self._dump_region_tree(child, indent + 4)

        elif isinstance(node, LoopRegion):
            logger.debug("%sLoopRegion(header=%d)", prefix, node.header_block.id)
            self._dump_region_tree(node.body, indent + 4)

        elif isinstance(node, BasicBlock):
            logger.debug("%sBlock %d", prefix, node.id)

        else:
            logger.debug("%s%s", prefix, type(node).__name__)
