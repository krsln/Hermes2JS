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

# Matches the condition text embedded by handlers/Jump/Jmp.py's
# ConditionalJump/BuiltinConditionalJump/TypeOfConditionalJump, e.g.:
#   "if (r3) { /* jump to label_412 */ }"
#   "if (!r3) { /* jump to label_412 */ }"
#   'if (typeof r1 == "string") { /* jump to label_412 */ }'
#
# TODO(follow-up): this string-parses a value that was itself built by
# string-formatting a condition inside Jmp.py - fragile if that format
# ever changes, and it silently breaks on any condition expression that
# contains its own unbalanced parens. The clean fix is giving JSVariable
# a dedicated `condition_expr` field that jump handlers populate
# directly, and having this function read that field instead of
# regexing `value`. Left as regex for now to avoid touching every
# handlers/Jump/*.py class in the same change as the region builder.
_CONDITION_RE = re.compile(r"^if \((.*)\) \{ /\* jump")


class StructuralAnalyzer:
    """
    Converts a CFGAnalysis into a Region tree via structural analysis:
    a recursive-descent walk of the CFG in reverse-post-order that
    recognizes if/if-else headers (two-way conditional blocks), loop
    headers (from LoopAnalysis' natural loops), and exception ranges
    (from ExceptionAnalysis), and falls back to explicit break/
    continue/goto markers for anything it can't cleanly structure.

    This class is intentionally the *only* place that owns the
    traversal state (visited sets, RPO index, current bound). The
    Loop/Try structurers call back into it (`structure_range`,
    `extract_condition`, `is_if_header`, ...) rather than duplicating
    that logic, so there is exactly one implementation of "how do we
    walk from block A to block B" in the whole builder package.
    """

    def __init__(self, analysis: CFGAnalysis):
        self.analysis = analysis
        self.cfg = analysis.cfg
        self.rpo = analysis.reverse_post_order
        self.rpo_index = {block.id: i for i, block in enumerate(self.rpo)}

        self.loops_by_header = self._group_loops_by_header()
        self.exceptions_by_start = {e.start: e for e in analysis.exceptions}

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
        outgoing edges and they are the TRUE_BRANCH/FALSE_BRANCH pair
        that ControlFlowGraphBuilder assigns to every conditional jump
        handler (JmpTrue, JmpFalse, JmpUndefined, JmpBuiltinIs(Not),
        JmpTypeOfIs, and their *Long variants).

        Deliberately edge-kind-based rather than
        `handler.startswith("Jmp")` (the old check): a block ending in
        a plain unconditional `Jmp` also starts with "Jmp" but only
        ever gets ONE real outgoing edge (kind=UNCONDITIONAL) once the
        ControlFlowGraphBuilder fallthrough bug is fixed - so this
        check naturally excludes it without needing a handler
        allowlist here too.
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
    # Core traversal
    # ------------------------------------------------------------

    def structure_range(
        self,
        start_id: int,
        stop_id: int | None,
        bound: set[int] | None = None,
        suppress_loop_header: int | None = None,
        suppress_exception_start: int | None = None,
    ) -> tuple[SequenceRegion, int | None]:
        """
        Structure blocks starting at `start_id`, stopping when `stop_id`
        is reached (exclusive) or control runs out.

        `bound`, if given, restricts traversal to that set of block
        ids - used for loop bodies so a `break`/exit edge is detected
        by simply falling outside the set rather than needing separate
        bookkeeping.

        `suppress_loop_header`, if set, must equal `start_id`: it tells
        this call to treat that one block as an ordinary block instead
        of re-entering loop structuring for it. LoopStructurer needs
        this because do-while/infinite-loop bodies legitimately start
        AT the header - without the suppression, the first block visited
        would immediately re-trigger `LoopStructurer.build()` for the
        same header and recurse forever.

        `suppress_exception_start` is the same mechanism for
        TryStructurer: a try body legitimately starts AT the block
        that begins its own exception region, so without suppressing
        it on that first visit, `_try_structurer.build()` would
        immediately re-trigger itself for the same start address and
        recurse forever (this was a real bug caught by testing against
        production .hbc input, not a hypothetical).

        Returns `(region, next_id)` where `next_id` is where control
        resumes after this region - equal to `stop_id` on a clean
        merge, or `None` if every path inside this region terminated
        the function (all branches returned/threw) or left `bound`.
        """

        children: list[Region] = []
        current_id = start_id
        visited_here: set[int] = set()
        first_iteration = True

        while current_id is not None and current_id != stop_id:

            if bound is not None and current_id not in bound:
                # Left the bound without a recognized exit edge (e.g.
                # this range was entered speculatively). Nothing more
                # to add at this level; caller interprets `None`.
                current_id = None
                break

            if current_id in visited_here:
                # We've come back around within a region that isn't a
                # recognized loop - genuinely irreducible control flow.
                # Emit a goto and stop rather than spin forever.
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

            is_suppressed = first_iteration and current_id in (suppress_loop_header, suppress_exception_start)
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
                if_region, next_id = self._structure_if(block, bound)
                children.append(if_region)
                current_id = next_id
                continue

            children.append(self.block_region(block))
            current_id = self._successor_after(block, bound)

        return SequenceRegion(regions=children), current_id

    # ------------------------------------------------------------

    def _structure_if(self, block, bound: set[int] | None) -> tuple[Region, int | None]:

        then_edge = next(e for e in control_flow_edges(block) if e.kind == EdgeKind.TRUE_BRANCH)
        else_edge = next(e for e in control_flow_edges(block) if e.kind == EdgeKind.FALSE_BRANCH)

        condition = self.extract_condition(block)
        merge = self.merge_of(block.id)

        then_region = self._branch_region(then_edge.target, merge, bound)

        if else_edge.target == merge:
            return IfRegion(condition=condition, then_region=then_region), merge

        else_region = self._branch_region(else_edge.target, merge, bound)
        return IfElseRegion(condition=condition, then_region=then_region, else_region=else_region), merge

    def _branch_region(self, target: int, merge: int | None, bound: set[int] | None) -> Region:

        if bound is not None and target not in bound:
            # The only way to leave a loop's bound from inside a
            # branch is via one of its recognized exit edges, so this
            # is a `break`. (A branch back to the loop header instead
            # of out of it recurses into structure_range normally,
            # hits the "already visited" guard on the header, and
            # degrades to a raw `goto label_<header>;` rather than an
            # idiomatic `continue;` - see TODO in module docstring of
            # _LoopStructurer for promoting that to a real CONTINUE.)
            return SequenceRegion(regions=[GotoRegion(ControlTransferKind.BREAK)])

        region, _ = self.structure_range(target, stop_id=merge, bound=bound)
        return region

    def _successor_after(self, block, bound: set[int] | None) -> int | None:

        edges = control_flow_edges(block)

        if len(edges) == 0:
            return None

        if len(edges) == 1:
            target = edges[0].target

        else:
            # More than one *normal* outgoing edge on a block we didn't
            # classify as an if-header - most likely SwitchImm. Its
            # case targets are wired as real edges now (see
            # ControlFlowGraphBuilder._connect / extra_gotos), but
            # SwitchRegion structuring itself doesn't exist yet, so we
            # fall back to following the first edge, which keeps the
            # pipeline alive without reconstructing the switch shape.
            logger.debug(
                "Unstructured multi-successor block %s (%d normal outgoing edges); "
                "following the first one",
                block.id, len(edges),
            )
            target = edges[0].target

        if bound is not None and target not in bound:
            return None

        return target

    # ------------------------------------------------------------

    def _group_loops_by_header(self) -> dict[int, set[int]]:
        """
        LoopAnalysis emits one `Loop` per back-edge, so a header with
        multiple back-edges (multiple `continue`-equivalent paths)
        produces multiple Loop entries. Merge their bodies here so the
        rest of the builder only has to think about "the loop at this
        header", not "the loops (plural) at this header".
        """

        grouped: dict[int, set[int]] = {}

        for loop in self.analysis.loops:
            grouped.setdefault(loop.header, set()).update(loop.body)

        return grouped
