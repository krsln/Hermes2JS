from __future__ import annotations

from hermes_decompiler.analysis.cfg import BasicBlock
from hermes_decompiler.analysis.regions.Regions import (
    IfRegion,
    LoopRegion,
    SequenceRegion,
    SwitchRegion,
    TryRegion,
)
from hermes_decompiler.analysis.terminators import TerminatorSwitch
from hermes_decompiler.analysis.transforms.structurers._base import RegionStructurer

from ._comparison_chain_builder import _ComparisonChainSwitchBuilder
from ._jump_table_builder import _JumpTableSwitchBuilder

# Below this many cases, folding into a `switch` adds no value over the
# `if`/`else if` chain IfStructurer already built - not wrong, just not
# worth the structural churn for a 1-2-way branch.
_MIN_CASES = 2


class SwitchStructurer(RegionStructurer):
    """
    Builds `SwitchRegion`s from whichever form Hermes compiled a
    `switch` statement into. For any given switch Hermes emits exactly
    one of the two shapes, never both:

    1. **Comparison chain** (small / sparse switches) - a chain of
       `IfRegion`s already produced by `IfStructurer`. Recovered by
       `_ComparisonChainSwitchBuilder`.

    2. **Jump table** (`SwitchImm` / `UIntSwitchImm`, dense switches) -
       a single raw `BasicBlock` whose terminator is `TerminatorSwitch`,
       untouched by `IfStructurer` (which only consumes
       `TerminatorConditionalBranch`). Recovered by
       `_JumpTableSwitchBuilder`.

    This class only dispatches between the two builders and owns the
    tree walk; all matching/recovery logic lives in the builders
    themselves (see each for its own mechanics).
    """

    def __init__(self, graph, cfg):
        super().__init__(graph, cfg)
        self._jump_table = _JumpTableSwitchBuilder(graph, cfg)
        self._comparison_chain = _ComparisonChainSwitchBuilder(graph)

    def run(self) -> None:
        self._visit(self.graph.root)
        self.dump_region_tree_if_debug(type(self).__name__)

    # -------------------------------------------------------------
    # Region walk
    # -------------------------------------------------------------

    def _visit(self, region) -> None:

        if isinstance(region, SequenceRegion):
            self._fold_sequence(region)

            for child in region.children:
                self._visit(child)

            return

        if isinstance(region, LoopRegion):
            self._visit(region.body)
            return

        if isinstance(region, IfRegion):
            self._visit(region.then_body)
            if region.else_body:
                self._visit(region.else_body)
            return

        if isinstance(region, TryRegion):
            self._visit(region.try_body)
            if region.catch:
                self._visit(region.catch.body)
            if region.finally_:
                self._visit(region.finally_.body)
            return

        if isinstance(region, SwitchRegion):
            for case in region.cases:
                self._visit(case.body)
            if region.default_body:
                self._visit(region.default_body)
            return

        if hasattr(region, "body"):
            self._visit(region.body)

    # -------------------------------------------------------------
    # Sequence folding entry point
    # -------------------------------------------------------------

    def _fold_sequence(self, region: SequenceRegion) -> None:
        """
        Repeatedly scans `region.children` for a switch-shaped item
        and converts it, restarting after each conversion since the
        list is mutated in place - the same "find one, convert,
        restart" shape `_DominanceIfBuilder._structure_sequence` uses
        for `IfRegion` construction.

        Bug fix vs. the pre-split version: that version returned
        after the FIRST successful conversion in this method, on the
        stated assumption that `_visit` would "re-scan on the next
        pass" - but `_visit` never actually re-invoked `_fold_sequence`
        on the same region. Two independent switch statements sitting
        as siblings in the same `SequenceRegion` (not nested inside
        one another) would silently leave the second one unconverted.
        The `while` loop below is the missing retry.
        """
        while self._try_fold_one(region):
            pass

    def _try_fold_one(self, region: SequenceRegion) -> bool:

        for item in region.children:

            if isinstance(item, BasicBlock) and isinstance(item.terminator, TerminatorSwitch):
                if self._jump_table.try_build(region, item):
                    return True
                continue

            if isinstance(item, IfRegion):
                if self._comparison_chain.try_build(region, item, _MIN_CASES):
                    return True
                continue

        return False
