from __future__ import annotations

import logging
from abc import ABC, abstractmethod

from hermes_decompiler.analysis.models import RegionGraph, RegionVisitor
from hermes_decompiler.core.logging import get_logger

logger = get_logger(__name__)


class RegionStructurer(ABC):
    """
    Base class for passes that build a new region-tree node type
    (IfRegion, LoopRegion, TryRegion, SwitchRegion) from raw
    BasicBlocks or existing regions via RegionGraph mutation.

    Contract: __init__(graph, cfg), then run() mutates self.graph in
    place and returns None. Each structurer is stateless between
    run() calls.

    Passes that fold or rewrite existing region-tree nodes without
    introducing a new region kind belong in transforms/region_passes/
    instead.

    SequenceStructurer is the one exception in this package: it
    bootstraps the region tree before any RegionGraph exists, so it
    does not extend this class.
    """

    def __init__(self, graph: RegionGraph, cfg):
        self.graph = graph
        self.cfg = cfg

    @abstractmethod
    def run(self) -> None:
        """Mutate self.graph's tree in place."""
        ...

    def dump_region_tree_if_debug(self, label: str) -> None:
        """
        Logs the current region tree at DEBUG level, prefixed with
        `label`. No-op unless DEBUG logging is enabled.
        """
        if not logger.isEnabledFor(logging.DEBUG):
            return

        logger.debug("===== REGION TREE: after %s =====", label)
        _RegionTreeDumper().visit(self.graph.root)


class _RegionTreeDumper(RegionVisitor):
    """
    Logs each region-tree node at DEBUG level. One instance per dump
    call, since indentation is tracked as an instance state.
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
        header_id = node.header_block.id if node.header_block is not None else "?"
        logger.debug("%sLoopRegion(header=%s)", self._prefix(), header_id)
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
