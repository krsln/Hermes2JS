from __future__ import annotations

import re
from dataclasses import dataclass, field

from hermes_decompiler.Logger import get_logger
from hermes_decompiler.two.cfg.CFGAnalysis import CFGAnalysis
from hermes_decompiler.two.cfg.EdgeKind import EdgeKind

from hermes_decompiler.two.regions.model.Region import Region
from hermes_decompiler.two.regions.model.BlockRegion import BlockRegion
from hermes_decompiler.two.regions.model.SequenceRegion import SequenceRegion
from hermes_decompiler.two.regions.model.IfRegion import IfRegion
from hermes_decompiler.two.regions.model.IfElseRegion import IfElseRegion
from hermes_decompiler.two.regions.model.GotoRegion import GotoRegion, ControlTransferKind

from hermes_decompiler.two.regions.building._MergePointResolver import MergePointResolver
from hermes_decompiler.two.regions.building._LoopStructurer import LoopStructurer
from hermes_decompiler.two.regions.building._TryStructurer import TryStructurer
from hermes_decompiler.two.regions.building._ControlFlowEdges import control_flow_edges

logger = get_logger(__name__)

_CONDITION_RE = re.compile(r"^if \((.*)\) \{ /\* jump")


# ------------------------------------------------------------------
# Explicit-stack machine state (replaces Python call recursion)
# ------------------------------------------------------------------

@dataclass
class _IfWait:
    """
    Bookkeeping for an if-header whose then/else branch(es) are being
    built. Lives on the _Frame that owns the if-header while we wait
    for a pushed child _Frame (or an immediately-resolved CONTINUE/
    BREAK region) to produce the branch's Region.
    """
    condition: str
    merge: int | None
    else_target: int | None   # None => single-branch IfRegion (else falls straight to merge)
    stage: str                # "then" or "else"
    then_region: Region | None = None


@dataclass
class _Frame:
    """
    One logical invocation of `structure_range`. Where the original
    recursive implementation had one of these live as Python-call-stack
    locals per nested if/else level, this version keeps them as
    heap-allocated objects on an explicit `list` stack in
    `structure_range` - so nesting depth is bounded by available
    memory, not by Python's (default ~1000 frame) recursion limit.

    Every field here corresponds 1:1 to a local variable or parameter
    the old recursive `structure_range`/`_structure_if`/`_branch_region`
    trio used to carry on the Python call stack.
    """
    stop_id: int | None
    bound: set[int] | None
    active_loop_header: int | None
    current_id: int | None
    children: list = field(default_factory=list)
    visited_here: set = field(default_factory=set)
    first_iteration: bool = True
    suppress_loop_header: int | None = None
    suppress_exception_start: int | None = None
    waiting: _IfWait | None = None
    pending_child_result: Region | None = None


class StructuralAnalyzer:
    """
    Converts a CFGAnalysis into a Region tree via structural analysis:
    a reverse-post-order walk of the CFG that recognizes if/if-else
    headers, loop headers (from LoopAnalysis' natural loops), and
    exception ranges (from ExceptionAnalysis), falling back to
    explicit break/continue/goto markers for anything it can't
    cleanly structure.

    RECURSION NOTE: `structure_range` is iterative, not recursive - it
    drives an explicit stack of `_Frame` objects instead of using
    Python call recursion for nested if/else branches. This matters in
    practice: Hermes generator/async state-machine bytecode routinely
    compiles to long chains of sequential guard-ifs
    (`if (cond) { ... } else { if (cond2) { ... } else { ... } }`,
    hundreds of levels deep for large functions), and the original
    recursive-descent version (structure_range -> _structure_if ->
    _branch_region -> structure_range -> ...) blew Python's recursion
    limit on real production .hbc input - raising
    `sys.setrecursionlimit` only delays the crash to a larger input,
    it doesn't fix the underlying unbounded-stack-depth problem.

    LoopStructurer.build() / TryStructurer.build() still call back into
    `structure_range` via an ordinary Python call (not pushed onto the
    explicit stack) - that's fine because loop/try NESTING depth (how
    many loops/trys are lexically inside each other) is small in
    practice, unlike if/else CHAIN length (how many sequential guard
    conditions a function has), which is what this rewrite targets.
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
        # call. Stops mutual recursion between two DIFFERENT headers
        # whose bodies overlap (irreducible/improper-region control
        # flow) - see LoopStructurer.build()/TryStructurer.build().
        self._loop_headers_in_progress: set[int] = set()
        self._exception_starts_in_progress: set[int] = set()

        # Blocks whose OWN instructions have already been emitted (as
        # a BlockRegion) anywhere in the output, tracked GLOBALLY
        # across the entire structuring pass. Fix for a real bug
        # (confirmed against a production 83-instruction function):
        # when `merge_of(header)` legitimately returns None - a CFG
        # shape with a chain of early-exit guard clauses where each
        # guard's "true" branch jumps to a shared tail block, but its
        # "false" fallthrough ALSO has its own independent path to a
        # DIFFERENT exit, so no single block post-dominates every path
        # - `_advance_frame`'s if-header handling had no natural stop
        # point and would fully re-structure the SAME shared tail block
        # from scratch inside every guard branch that reaches it. Each
        # occurrence pushes frames for the entire remaining graph again,
        # which blew Python's recursion limit even on a tiny function
        # (the "deep if/else chain" hypothesis that motivated this
        # class's iterative rewrite was a real, separate scalability
        # concern for LARGE functions - but this None-merge duplication
        # was the actual cause of that specific crash).
        #
        # Once a block has been fully structured once, any later
        # traversal that reaches it again gets a `goto label_X;` stub
        # instead of re-structuring it - bounding total structuring
        # work to O(number of blocks) regardless of how many branches
        # converge on it. Not idiomatic (a human would factor out the
        # shared guard-clause tail), but always valid, always
        # terminating JS.
        self._emitted_once: set[int] = set()

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
        """
        A block is a two-way conditional header if it has exactly two
        outgoing (non-exception) edges and they are the TRUE_BRANCH/
        FALSE_BRANCH pair that ControlFlowGraphBuilder assigns to
        every conditional jump handler.
        """
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
    # Core traversal (iterative)
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
        """
        Structure blocks starting at `start_id`, stopping when `stop_id`
        is reached (exclusive) or control runs out.

        Same contract as the original recursive version (see git
        history / earlier revision for the docstring detailing
        `bound`, `suppress_loop_header`, `suppress_exception_start`,
        and the `(region, next_id)` return shape) - only the
        implementation strategy changed, from Python-call recursion to
        an explicit `_Frame` stack.
        """

        root = _Frame(
            stop_id=stop_id,
            bound=bound,
            active_loop_header=active_loop_header,
            current_id=start_id,
            suppress_loop_header=suppress_loop_header,
            suppress_exception_start=suppress_exception_start,
        )
        stack: list[_Frame] = [root]

        while True:

            frame = stack[-1]
            status = self._advance_frame(frame, stack)

            if status == "pushed":
                # A child _Frame was appended to `stack` (for an if
                # branch); go work on it next iteration. `frame` stays
                # exactly where it is, waiting via `frame.waiting`.
                continue

            # status == "done": this frame has nothing left to do.
            region = SequenceRegion(regions=frame.children)
            next_id = frame.current_id
            stack.pop()

            if not stack:
                return region, next_id

            # Hand the completed region up to whichever frame pushed
            # this one - it'll pick it up via `frame.waiting` /
            # `pending_child_result` on its next `_advance_frame` call.
            parent = stack[-1]
            parent.pending_child_result = region

    def _advance_frame(self, frame: _Frame, stack: list[_Frame]) -> str:
        """
        Advance `frame` by zero or more straight-line steps (blocks,
        loops, trys) until it either:

          - needs a child frame for an if-branch: pushes it onto
            `stack` and returns "pushed" (leaving `frame.waiting` set
            so the next call to `_advance_frame` on this same frame
            picks up where it left off), or

          - runs out of blocks (hit `stop_id`, left `bound`, or the
            CFG ended): returns "done", with `frame.children` and
            `frame.current_id` holding the final result.
        """

        while True:

            # --- resume after a pushed if-branch child completed ---
            if frame.waiting is not None:
                w = frame.waiting

                if w.stage == "then":
                    w.then_region = frame.pending_child_result
                    frame.pending_child_result = None

                    if w.else_target is None:
                        frame.children.append(
                            IfRegion(condition=w.condition, then_region=w.then_region)
                        )
                        frame.current_id = w.merge
                        frame.waiting = None
                        continue

                    w.stage = "else"
                    immediate = self._push_branch(
                        stack, w.else_target, w.merge, frame.bound, frame.active_loop_header,
                    )
                    if immediate is not None:
                        frame.children.append(
                            IfElseRegion(
                                condition=w.condition,
                                then_region=w.then_region,
                                else_region=immediate,
                            )
                        )
                        frame.current_id = w.merge
                        frame.waiting = None
                        continue

                    return "pushed"

                else:  # w.stage == "else"
                    else_region = frame.pending_child_result
                    frame.pending_child_result = None
                    frame.children.append(
                        IfElseRegion(
                            condition=w.condition,
                            then_region=w.then_region,
                            else_region=else_region,
                        )
                    )
                    frame.current_id = w.merge
                    frame.waiting = None
                    continue

            # --- normal termination checks ---
            if frame.current_id is None or frame.current_id == frame.stop_id:
                return "done"

            if frame.bound is not None and frame.current_id not in frame.bound:
                frame.current_id = None
                return "done"

            if frame.current_id in frame.visited_here:
                logger.warning(
                    "Irreducible control flow detected re-entering block %s; "
                    "emitting fallback goto", frame.current_id,
                )
                frame.children.append(
                    GotoRegion(ControlTransferKind.GOTO, label=f"label_{frame.current_id}")
                )
                frame.current_id = None
                return "done"

            frame.visited_here.add(frame.current_id)
            block = self.cfg.get_block(frame.current_id)

            if block is None:
                frame.current_id = None
                return "done"

            is_suppressed_start = frame.first_iteration and frame.current_id in (
                frame.suppress_loop_header, frame.suppress_exception_start,
            )
            is_in_progress = (
                frame.current_id in self._loop_headers_in_progress
                or frame.current_id in self._exception_starts_in_progress
            )
            is_suppressed = is_suppressed_start or is_in_progress
            frame.first_iteration = False

            if not is_suppressed and frame.current_id in self.loops_by_header:
                loop_region, next_id = self._loop_structurer.build(frame.current_id)
                frame.children.append(loop_region)
                frame.current_id = next_id
                continue

            if not is_suppressed and frame.current_id in self.exceptions_by_start:
                try_region, next_id = self._try_structurer.build(frame.current_id)
                frame.children.append(try_region)
                frame.current_id = next_id
                continue

            # `block`'s own instructions are about to be emitted (as an
            # if-header or ordinary block) - guard against re-emitting
            # content already fully structured elsewhere. See the
            # `_emitted_once` comment in __init__.
            if frame.current_id in self._emitted_once:
                frame.children.append(GotoRegion(ControlTransferKind.GOTO, label=f"label_{frame.current_id}"))
                frame.current_id = None
                return "done"
            self._emitted_once.add(frame.current_id)

            if self.is_if_header(block):
                frame.children.append(self.block_region(block))

                then_edge = next(e for e in control_flow_edges(block) if e.kind == EdgeKind.TRUE_BRANCH)
                else_edge = next(e for e in control_flow_edges(block) if e.kind == EdgeKind.FALSE_BRANCH)
                condition = self.extract_condition(block)
                merge = self.merge_of(block.id)
                else_target = None if else_edge.target == merge else else_edge.target

                frame.waiting = _IfWait(
                    condition=condition, merge=merge, else_target=else_target, stage="then",
                )

                immediate = self._push_branch(
                    stack, then_edge.target, merge, frame.bound, frame.active_loop_header,
                )
                if immediate is not None:
                    frame.pending_child_result = immediate
                    continue  # let the "resume after..." branch above consume it

                return "pushed"

            # --- ordinary straight-line block ---
            frame.children.append(self.block_region(block))

            edges = control_flow_edges(block)

            if len(edges) == 0:
                frame.current_id = None
                continue

            if len(edges) == 1:
                target = edges[0].target
            else:
                # More than one *normal* outgoing edge on a block we
                # didn't classify as an if-header - most likely
                # SwitchImm. Its case targets are wired as real edges
                # (see ControlFlowGraphBuilder._connect / extra_gotos),
                # but SwitchRegion structuring itself doesn't exist
                # yet, so we fall back to following the first edge.
                logger.debug(
                    "Unstructured multi-successor block %s (%d normal outgoing edges); "
                    "following the first one",
                    block.id, len(edges),
                )
                target = edges[0].target

            if frame.active_loop_header is not None and target == frame.active_loop_header:
                frame.children.append(GotoRegion(ControlTransferKind.CONTINUE))
                frame.current_id = None
                continue

            if frame.bound is not None and target not in frame.bound:
                frame.current_id = None
                continue

            frame.current_id = target
            # loop continues within this same frame - no recursion

    @staticmethod
    def _push_branch(
            stack: list[_Frame],
            target: int,
            merge: int | None,
            bound: set[int] | None,
            active_loop_header: int | None,
    ) -> Region | None:
        """
        Resolve one if/else branch target.

        Returns a Region immediately for the two short-circuit cases
        that need no further structuring (CONTINUE: branch jumps
        straight back to the loop header; BREAK: branch leaves the
        loop's bound). Otherwise pushes a new `_Frame` onto `stack` for
        the branch's body and returns None - the caller must then
        return "pushed" and wait for it to complete.

        Equivalent to the old recursive `_branch_region`, minus the
        recursive `structure_range` call at the end (pushing a frame
        instead).
        """

        if active_loop_header is not None and target == active_loop_header:
            return SequenceRegion(regions=[GotoRegion(ControlTransferKind.CONTINUE)])

        if bound is not None and target not in bound:
            return SequenceRegion(regions=[GotoRegion(ControlTransferKind.BREAK)])

        stack.append(_Frame(
            stop_id=merge,
            bound=bound,
            active_loop_header=active_loop_header,
            current_id=target,
        ))
        return None

    # ------------------------------------------------------------

    def _group_loops_by_header(self) -> dict[int, set[int]]:
        """
        LoopAnalysis emits one `Loop` per back-edge, so a header with
        multiple back-edges produces multiple Loop entries. Merge
        their bodies here so the rest of the builder only has to think
        about "the loop at this header".
        """

        grouped: dict[int, set[int]] = {}

        for loop in self.analysis.loops:
            grouped.setdefault(loop.header, set()).update(loop.body)

        return grouped