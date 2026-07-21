from __future__ import annotations

import re

from hermes_decompiler.Logger import get_logger
from hermes_decompiler.cfg.CFGAnalysis import CFGAnalysis
from hermes_decompiler.cfg.EdgeKind import EdgeKind

from hermes_decompiler.regions.model.Region import Region
from hermes_decompiler.regions.model.BlockRegion import BlockRegion
from hermes_decompiler.regions.model.SequenceRegion import SequenceRegion
from hermes_decompiler.regions.model.IfRegion import IfRegion
from hermes_decompiler.regions.model.IfElseRegion import IfElseRegion
from hermes_decompiler.regions.model.GotoRegion import GotoRegion, ControlTransferKind

from hermes_decompiler.regions.building._MergePointResolver import MergePointResolver
from hermes_decompiler.regions.building._LoopStructurer import LoopStructurer
from hermes_decompiler.regions.building._TryStructurer import TryStructurer
from hermes_decompiler.regions.building._ControlFlowEdges import control_flow_edges

logger = get_logger(__name__)

_CONDITION_RE = re.compile(r"^if \((.*)\) \{ /\* jump")


class StructuralAnalyzer:
    """
    Converts a CFGAnalysis into a Region tree via structural analysis.
    """

    def __init__(self, analysis: CFGAnalysis):
        self.analysis = analysis
        self.cfg = analysis.cfg
        self.rpo = analysis.reverse_post_order
        self.rpo_index = {block.id: i for i, block in enumerate(self.rpo)}

        self.loops_by_header = self._group_loops_by_header()
        self.exceptions_by_start = {e.start: e for e in analysis.exceptions}

        # Persist for the *entire* nested construction of a loop/try
        # region, not just the first block of one structure_range()
        # call (that's what suppress_loop_header/suppress_exception_start
        # below are for - they only cover re-entrance on the literal
        # start block). This set is what stops mutual recursion between
        # two DIFFERENT headers whose bodies overlap - e.g. header A's
        # body contains header B, and header B's body (from a separate,
        # overlapping natural loop) contains header A back. That's
        # irreducible/improper-region control flow in the classic
        # compiler sense, not a hypothetical: it showed up on real
        # generator-heavy .hbc input as a RecursionError between
        # LoopStructurer.build(29) and LoopStructurer.build(158).
        #
        # When a header/exception-start is "in progress" and we walk
        # back into it from deeper in the recursion, it's treated as an
        # ordinary block for that one visit (same as `is_suppressed`
        # below) instead of re-triggering construction. This can mean
        # that block's contents get emitted more than once in the final
        # output (once inside its own loop/try, again wherever the
        # overlapping structure re-reaches it) - not idiomatic, but
        # valid JS and no crash, the same "graceful degradation"
        # tradeoff used for irreducible control flow elsewhere in this
        # class. Worth diffing the affected function's output against
        # its disassembly if you see duplicated blocks.
        self._loop_headers_in_progress: set[int] = set()
        self._exception_starts_in_progress: set[int] = set()

        self._merge_resolver = MergePointResolver(analysis)
        self._loop_structurer = LoopStructurer(self)
        self._try_structurer = TryStructurer(self)

    def run(self) -> Region:
        region, _ = self.structure_range(self.cfg.entry.id, stop_id=None, bound=None)
        return region

    # ------------------------------------------------------------
    # Shared helpers (used by LoopStructurer / TryStructurer too)
    # ------------------------------------------------------------

    def merge_of(self, header_id: int) -> int | None:
        return self._merge_resolver.merge_of(header_id)

    def block_region(self, block) -> BlockRegion:
        return BlockRegion(block=block)

    def is_if_header(self, block) -> bool:
        if len(control_flow_edges(block)) != 2:
            return False

        kinds = {edge.kind for edge in control_flow_edges(block)}
        return kinds == {EdgeKind.TRUE_BRANCH, EdgeKind.FALSE_BRANCH}

    def extract_condition(self, block) -> str:

        last = block.instructions[-1]
        match = _CONDITION_RE.match(last.variable.value.strip())

        if match:
            return match.group(1)

        logger.warning(
            "Could not extract condition text from block %s (value=%r)",
            block.id, last.variable.value,
        )
        return f"/* unrecoverable condition @ block {block.id} */ true"

    # ------------------------------------------------------------
    # Core traversal
    # ------------------------------------------------------------

    def structure_range(
            self,
            start_id: int,
            stop_id: int | None,
            bound: set[int] | None = None,
            suppress_loop_header: int | None = None,
            suppress_exception_start: int | None = None,
            active_loop_header: int | None = None,
    ) -> tuple[SequenceRegion, int | None]:

        children: list[Region] = []
        current_id = start_id
        visited_here: set[int] = set()
        first_iteration = True

        while current_id is not None and current_id != stop_id:

            if bound is not None and current_id not in bound:
                current_id = None
                break

            if current_id in visited_here:
                logger.warning(
                    "Irreducible control flow detected re-entering block %s; "
                    "emitting fallback goto", current_id,
                )
                children.append(GotoRegion(ControlTransferKind.GOTO, label=f"label_{current_id}"))
                current_id = None
                break

            visited_here.add(current_id)
            block = self.cfg.get_block(current_id)

            if block is None:
                current_id = None
                break

            # A block is treated as "ordinary" for this one visit -
            # skipping loop/try (re-)construction - if either:
            #   (a) it's the literal start block AND the caller asked
            #       to suppress it (do-while/infinite loop bodies and
            #       try bodies legitimately start AT their own header),
            #   (b) it's a header/exception-start whose construction is
            #       already in progress somewhere up the call stack -
            #       see the in-progress-set comment in __init__.
            is_suppressed_start = first_iteration and current_id in (suppress_loop_header, suppress_exception_start)
            is_in_progress = (
                current_id in self._loop_headers_in_progress
                or current_id in self._exception_starts_in_progress
            )
            is_suppressed = is_suppressed_start or is_in_progress
            first_iteration = False

            if not is_suppressed and current_id in self.loops_by_header:
                loop_region, next_id = self._loop_structurer.build(current_id)
                children.append(loop_region)
                current_id = next_id
                continue

            if not is_suppressed and current_id in self.exceptions_by_start:
                try_region, next_id = self._try_structurer.build(current_id)
                children.append(try_region)
                current_id = next_id
                continue

            if self.is_if_header(block):
                children.append(self.block_region(block))
                if_region, next_id = self._structure_if(block, bound, active_loop_header)
                children.append(if_region)
                current_id = next_id
                continue

            children.append(self.block_region(block))
            extra_region, next_id = self._successor_after(block, bound, active_loop_header)

            if extra_region is not None:
                children.append(extra_region)

            current_id = next_id

        return SequenceRegion(regions=children), current_id

    # ------------------------------------------------------------

    def _structure_if(self, block, bound: set[int] | None, active_loop_header: int | None) -> tuple[
        Region, int | None,]:

        then_edge = next(e for e in control_flow_edges(block) if e.kind == EdgeKind.TRUE_BRANCH)
        else_edge = next(e for e in control_flow_edges(block) if e.kind == EdgeKind.FALSE_BRANCH)

        condition = self.extract_condition(block)
        merge = self.merge_of(block.id)

        then_region = self._branch_region(then_edge.target, merge, bound, active_loop_header)

        if else_edge.target == merge:
            return IfRegion(condition=condition, then_region=then_region), merge

        else_region = self._branch_region(else_edge.target, merge, bound, active_loop_header)

        return IfElseRegion(condition=condition, then_region=then_region, else_region=else_region), merge

    def _branch_region(self, target: int, merge: int | None, bound: set[int] | None,
                       active_loop_header: int | None, ) -> Region:

        if active_loop_header is not None and target == active_loop_header:
            return SequenceRegion(regions=[GotoRegion(ControlTransferKind.CONTINUE)])

        if bound is not None and target not in bound:
            return SequenceRegion(regions=[GotoRegion(ControlTransferKind.BREAK)])

        region, _ = self.structure_range(target, stop_id=merge, bound=bound, active_loop_header=active_loop_header)
        return region

    def _successor_after(
            self, block, bound: set[int] | None, active_loop_header: int | None,
    ) -> tuple[Region | None, int | None]:
        edges = control_flow_edges(block)

        if len(edges) == 0:
            return None, None

        if len(edges) == 1:
            target = edges[0].target

        else:
            logger.debug(
                "Unstructured multi-successor block %s (%d normal outgoing edges); "
                "following the first one",
                block.id, len(edges),
            )
            target = edges[0].target

        if active_loop_header is not None and target == active_loop_header:
            return GotoRegion(ControlTransferKind.CONTINUE), None

        if bound is not None and target not in bound:
            return None, None

        return None, target

    # ------------------------------------------------------------

    def _group_loops_by_header(self) -> dict[int, set[int]]:

        grouped: dict[int, set[int]] = {}

        for loop in self.analysis.loops:
            grouped.setdefault(loop.header, set()).update(loop.body)

        return grouped