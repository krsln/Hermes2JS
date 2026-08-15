from __future__ import annotations

import logging
from abc import ABC, abstractmethod

from hermes_decompiler.analysis.models import RegionGraph, RegionVisitor
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
        given block. No-op (skips even building the tree walk) unless
        DEBUG logging is enabled.
        """
        if not logger.isEnabledFor(logging.DEBUG):
            return

        logger.debug("===== REGION TREE: after %s =====", label)
        _RegionTreeDumper().visit(self.graph.root)


class _RegionTreeDumper(RegionVisitor):
    """
    Logs each region-tree node at DEBUG level as `RegionVisitor` walks
    it. One instance per dump call - `_indent` is instance state
    (rather than a `visit()` parameter) because `RegionVisitor` keeps
    a uniform single-argument dispatch signature across every
    subclass; a fresh instance per call keeps that state from leaking
    between unrelated dumps.

    Indentation deltas and the "then:"/"else:"/"try:"/"catch:"/
    "finally:" label lines match the dump's previous hand-rolled
    version exactly, for anyone used to reading its output.
    `SwitchRegion` is new here - the previous version had no branch
    for it at all and silently fell through to printing just the bare
    type name via its own `else` clause, with no visibility into case
    values or bodies.
    """

    def __init__(self):
        self._indent = 0

    def _prefix(self) -> str:
        return " " * self._indent

    def visit_SequenceRegion(self, node) -> None:
        logger.debug("%sSequenceRegion", self._prefix())
        self._indent += 4
        for child in node.children:
            self.visit(child)
        self._indent -= 4

    def visit_LoopRegion(self, node) -> None:
        logger.debug("%sLoopRegion(header=%d)", self._prefix(), node.header_block.id)
        self._indent += 4
        self.visit(node.body)
        self._indent -= 4

    def visit_IfRegion(self, node) -> None:
        prefix = self._prefix()
        logger.debug("%sIfRegion", prefix)

        logger.debug("%s  then:", prefix)
        self._indent += 8
        self.visit(node.then_body)
        self._indent -= 8

        if node.else_body is not None:
            logger.debug("%s  else:", prefix)
            self._indent += 8
            self.visit(node.else_body)
            self._indent -= 8

    def visit_TryRegion(self, node) -> None:
        prefix = self._prefix()
        logger.debug("%sTryRegion", prefix)

        logger.debug("%s  try:", prefix)
        self._indent += 8
        self.visit(node.try_body)
        self._indent -= 8

        if node.catch is not None:
            logger.debug("%s  catch:", prefix)
            self._indent += 8
            self.visit(node.catch.body)
            self._indent -= 8

        if node.finally_ is not None:
            logger.debug("%s  finally:", prefix)
            self._indent += 8
            self.visit(node.finally_.body)
            self._indent -= 8

    def visit_SwitchRegion(self, node) -> None:
        prefix = self._prefix()
        logger.debug("%sSwitchRegion", prefix)

        for case in node.cases:
            tests = ", ".join(repr(test) for test in case.tests)
            logger.debug("%s  case %s:", prefix, tests)
            self._indent += 8
            self.visit(case.body)
            self._indent -= 8

        if node.default_body is not None:
            logger.debug("%s  default:", prefix)
            self._indent += 8
            self.visit(node.default_body)
            self._indent -= 8

    def visit_BasicBlock(self, node) -> None:
        logger.debug("%sBlock %d", self._prefix(), node.id)

    def generic_visit(self, node) -> None:
        logger.debug("%s%s", self._prefix(), type(node).__name__)
