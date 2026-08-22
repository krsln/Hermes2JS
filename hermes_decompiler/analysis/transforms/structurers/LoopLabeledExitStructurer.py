from __future__ import annotations

from typing import Literal

from hermes_decompiler.analysis.cfg import BasicBlock
from hermes_decompiler.analysis.models import TerminatorConditionalBranch
from hermes_decompiler.analysis.models.regions import (
    Region, TryRegion, CatchRegion, FinallyRegion,
    SequenceRegion, LoopRegion, IfRegion
)
# noinspection PyProtectedMember
from hermes_decompiler.analysis.transforms._shared import _negate_condition  # noqa: SLF001
from hermes_decompiler.analysis.transforms.structurers._base import RegionStructurer
from hermes_decompiler.core.logging import get_logger
from hermes_decompiler.frontend.opcode import OpcodeEntry, OpcodeResult
from hermes_decompiler.ir.expressions import Identifier
from hermes_decompiler.ir.statements import BreakStatement, ContinueStatement

logger = get_logger(__name__)

TargetLoopKind = Literal["continue", "break"]


class LoopLabeledExitStructurer(RegionStructurer):
    """
    Converts a conditional exit that escapes one or more ENCLOSING
    loops into a labeled `break`/`continue` (a single-level escape is
    LoopBreakStructurer's job instead).

    Must run immediately after LoopBreakStructurer, still before
    IfStructurer. This ordering is load-bearing, not conventional:
    IfStructurer only sees region-local siblings when classifying a
    branch target, so an edge escaping to an ancestor loop's sibling
    scope is silently collapsed into a same-level `if` with the
    escape edge discarded. If LoopConditionRegionPass then runs
    against that shape, the escaping path falls through into the
    loop's own back-edge test using a never-incremented loop
    variable - this has produced an effectively infinite loop in
    practice. Running before IfStructurer avoids the broken shape
    entirely instead of needing to detect and repair it afterward.

    For each innermost loop first, a candidate block matching
    LoopBreakStructurer's target/fallthrough shape is tested against
    every ENCLOSING loop, outward, for whether its exit edge's
    address matches that ancestor's latch (-> `continue <label>`) or
    natural merge (-> `break <label>`). The first matching ancestor
    is labeled (`loop_<header_block_id>`, reused if already labeled),
    and the exit block is spliced in as the branch's missing arm.

    Unlike LoopBreakStructurer, the synthesized statement is never
    attached to an existing instruction - Hermes commonly leaves this
    edge as a bare fallthrough with no explicit jump. A minimal
    synthetic instruction is appended instead (see
    `_append_labeled_statement`).

    Deliberately narrow: only a single-block exit with a single CFG
    successor is recognized. Anything else is left unconverted.
    """

    def __init__(self, graph, cfg):
        super().__init__(graph, cfg)
        self._synth_block_id: int | None = None

    def run(self) -> None:
        self._visit(self.graph.root)
        self.dump_region_tree_if_debug(type(self).__name__)

    # -------------------------------------------------------------

    def _visit(self, region: BasicBlock | Region) -> None:
        if isinstance(region, BasicBlock):
            return

        if isinstance(region, SequenceRegion):
            for child in list(region.children):
                self._visit(child)
            return

        if isinstance(region, LoopRegion):
            # Innermost-first: resolve nested loops' own escapes
            # before this loop's, so a genuinely single-level escape
            # isn't reconsidered here after inner structure changes.
            self._visit(region.body)
            self._try_recognize_labeled_exits(region)
            return

        # condition, _then_body, _else_body
        if isinstance(region, IfRegion):
            self._visit(region.then_body)

            region_else_body = region.else_body
            if region_else_body:
                self._visit(region_else_body)
            return

        # _try_body, _catch, _finally
        if isinstance(region, TryRegion):
            self._visit(region.try_body)

            region_catch = region.catch
            if region_catch is not None:
                self._visit(region_catch.body)

            region_finally = region.finally_
            if region_finally is not None:
                self._visit(region_finally.body)
            return

        # CatchRegion / FinallyRegion
        if isinstance(region, (CatchRegion, FinallyRegion)):
            self._visit(region.body)
            return

    # -------------------------------------------------------------

    @staticmethod
    def _find_candidate(loop: LoopRegion, exclude: set) -> BasicBlock | None:
        """
        Unlike LoopBreakStructurer, the loop's own header is not
        excluded: for a labeled exit, the header can itself be the
        source of the escaping edge (e.g., an inner loop's header
        testing a condition that continues an outer loop directly).
        Safety against misclassifying an ordinary guard as an escape
        comes from `_find_target_loop_for_address` only ever matching
        an ancestor's own latch/header/merge address, not from
        excluding candidate blocks here.
        """

        for item in loop.body.children:

            if not isinstance(item, BasicBlock):
                continue

            if item in exclude:
                continue

            if isinstance(item.terminator, TerminatorConditionalBranch):
                return item

        return None

    def _try_recognize_labeled_exits(self, loop: LoopRegion) -> None:
        """
        Converts one labeled-exit candidate at a time, restarting the
        scan after each conversion since mutation invalidates
        iteration.
        """

        failed: set = set()

        while True:
            block = self._find_candidate(loop, failed)

            if block is None:
                return

            if not self._convert(loop, block):
                failed.add(block)

    def _convert(self, loop: LoopRegion, block: BasicBlock) -> bool:

        branch = block.terminator
        assert isinstance(branch, TerminatorConditionalBranch)

        if block in loop.latches:
            # The loop's own back-edge test - not an escape edge.
            return False

        covered = loop.body.covered_blocks

        target_block = next(
            (s for s in block.successors if s.address == branch.target), None
        )
        fallthrough = [s for s in block.successors if s is not target_block]

        if target_block is None or len(fallthrough) != 1:
            return False

        fallthrough_block = fallthrough[0]

        target_inside = target_block in covered
        fallthrough_inside = fallthrough_block in covered

        if target_inside == fallthrough_inside:
            return False

        if target_inside:
            exit_block, condition = fallthrough_block, _negate_condition(branch.condition)
        else:
            exit_block, condition = target_block, branch.condition

        target_loop, kind = self._find_target_loop_for_address(loop, exit_block.address)

        if target_loop is None:
            successors = list(exit_block.successors)

            if len(successors) == 1:
                target_loop, kind = self._find_target_loop_for_address(
                    loop,
                    successors[0].address,
                )

        if target_loop is None:
            logger.debug(
                "LoopLabeledExitStructurer: no ancestor match for block %d "
                "(exit block %d, address 0x%x).",
                block.id,
                exit_block.id,
                exit_block.address,
            )
            return False

        if target_loop is loop:
            return False

        assert kind is not None
        assert target_loop is not None

        # ---- convert `block`'s branch into a structured IfRegion ----
        #
        # Deferred until here: nothing below is mutated until we've
        # confirmed the branch-owning instruction can actually be
        # removed, so a failed conversion never leaves a stray label
        # or partial edit behind.

        if block.instructions and block.instructions[-1].terminator is branch:
            block.instructions.pop()
            block.terminator = None
        else:
            logger.warning(
                "LoopLabeledExitStructurer: block %d's terminator "
                "instruction was not found where expected; aborting "
                "conversion.", block.id,
            )
            return False

        target_loop_label = target_loop.label
        if target_loop_label is None:
            target_loop_label = f"loop_{target_loop.header_block.id}"
            target_loop.label = target_loop_label

        label_node = Identifier(name=target_loop_label)
        statement = (
            ContinueStatement(label=label_node)
            if kind == "continue"
            else BreakStatement(label=label_node)
        )

        synth_block = BasicBlock(self._allocate_block_id(), address=-1)
        self._append_labeled_statement(synth_block, statement)

        # `exit_block` may carry real side-effecting content (e.g., a
        # console.log immediately preceding the escape) that must
        # still execute before the break/continue on the way out.
        # Only splice exit_block's own content into then_body -
        # extracting it from wherever it currently lives - when doing
        # so is safe: `block` must be its sole predecessor (mirrors
        # LoopBreakStructurer's identical guard - a block reached some
        # other way too isn't a clean single-purpose exit body), and it
        # must not be structural machinery of the loop being escaped to
        # (its header or one of its own latches). A shared merge point
        # (e.g., the code right after a loop, reached by both a normal
        # completion and this escape) or a loop's own back-edge test
        # must stay exactly where it is - every other path that reaches
        # it depends on it still being there; moving it either strands
        # that other path or - for a latch - dismantles the very
        # machinery a later pass needs to rebuild the loop's condition.
        #
        # `extract_block` (not a manual owner.children.remove) is used
        # here for the same reason LoopBreakStructurer uses it: plain
        # list surgery skips whatever bookkeeping the graph does on
        # relocation, which later region passes (e.g., induction-variable
        # aliasing) rely on being current.
        exit_is_structural_to_target = (
                exit_block in target_loop.latches
                or exit_block is target_loop.header_block
        )

        blocks_for_then_body: list = []

        if (
                exit_block.instructions
                and not exit_is_structural_to_target
                and list(exit_block.predecessors) == [block]
        ):
            self.graph.extract_block(exit_block)
            exit_block.terminator = None
            blocks_for_then_body.append(exit_block)

        blocks_for_then_body.append(synth_block)

        then_body = SequenceRegion()
        self.graph.transfer(blocks_for_then_body, then_body)

        if_region = IfRegion()
        if_region.condition = condition
        if_region.then_body = then_body
        if_region.else_body = None

        insert_at = loop.body.children.index(block) + 1
        self.graph.insert_at(loop.body, insert_at, if_region)

        block.successors = [s for s in block.successors if s is not exit_block]
        exit_block.predecessors = [p for p in exit_block.predecessors if p is not block]

        logger.debug(
            "LoopLabeledExitStructurer: block %d -> %s %s (header=%d)",
            block.id, kind, target_loop.label, target_loop.header_block.id,
        )
        return True

    def _allocate_block_id(self) -> int:
        """Allocates a unique BasicBlock id for a synthetic block."""

        if self._synth_block_id is None:
            self._synth_block_id = max((b.id for b in self.cfg.blocks), default=0) + 1

        assert self._synth_block_id is not None

        block_id = self._synth_block_id
        self._synth_block_id += 1
        return block_id

    def _find_target_loop_for_address(
            self,
            inner_loop: LoopRegion,
            target_address: int,
    ) -> tuple[LoopRegion | None, TargetLoopKind | None]:
        """
        Walks `inner_loop`'s ancestors outward, returning the first
        one whose latch, header, or natural merge address matches
        `target_address`, paired with "continue" or "break"
        respectively. (None, None) if no ancestor matches.
        """

        node = inner_loop.parent

        while node is not None:

            if isinstance(node, LoopRegion):

                latch_address = {latch.address for latch in node.latches}

                if target_address in latch_address:
                    return node, "continue"

                if node.header_block is not None and target_address == node.header_block.address:
                    # Some Hermes builds target the loop header rather
                    # than a latch for `continue`.
                    return node, "continue"

                merge = self._natural_loop_merge(node)

                if merge is not None and target_address == merge:
                    return node, "break"

            node = node.parent

        return None, None

    def _natural_loop_merge(self, loop: LoopRegion) -> int | None:
        """
        Address the loop's own back-edge test leaves to on normal
        completion, i.e., where a `break` also lands. None unless
        every latch agrees on the same address.

        Hermes sometimes routes this edge through one or more bare
        single-instruction trampoline blocks (an unconditional Jmp
        with no other content) before reaching the block whose
        address a labeled `break`'s target actually needs to match.
        Chasing through them here keeps `_find_target_loop_for_address`
        a plain address comparison, rather than needing trampoline
        awareness of its own.
        """
        covered = loop.body.covered_blocks

        merge_addresses = {
            self._chase_trampoline_address(successor.address, covered)
            for latch in loop.latches
            for successor in latch.successors
            if successor not in covered
        }

        if len(merge_addresses) != 1:
            return None

        return merge_addresses.pop()

    def _chase_trampoline_address(self, address: int, covered: set) -> int:
        """
        Follows a chain of bare single-successor, instruction-less
        blocks starting at `address`, returning the address the
        chain ultimately lands on. Stops as soon as a block has real
        content, more than one successor, or isn't found at all.
        Bounded by `seen` against a malformed/cyclic CFG.
        """
        address_to_block: dict[int, BasicBlock] = {b.address: b for b in self.cfg.blocks}
        seen: set[int] = set()

        while address not in seen:
            seen.add(address)
            candidate = address_to_block.get(address)

            if candidate is None or candidate in covered or candidate.instructions:
                return address

            successors = list(candidate.successors)
            if len(successors) != 1:
                return address

            address = successors[0].address

        return address

    # -------------------------------------------------------------

    @staticmethod
    def _append_labeled_statement(block: BasicBlock, statement) -> None:
        """
        Appends a minimal synthetic instruction carrying only
        `statement`. Unlike LoopBreakStructurer/LoopContinueRegionPass,
        which commandeers an existing terminator-bearing instruction,
        this pass cannot assume one exists - the escape edge is
        frequently a bare fallthrough. `hex_address=""` is safe:
        `OpcodeEntry` maps an invalid address to 0, and nothing
        downstream keys off this entry's address.
        """

        entry = OpcodeEntry(
            bytecode=f"<synthetic>: {type(statement).__name__}",
            hex_address="",
        )

        block.instructions.append(OpcodeResult(entry, statement=statement))
