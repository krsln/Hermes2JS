from __future__ import annotations

from hermes_decompiler.backend.analysis.cfg import BasicBlock
from hermes_decompiler.backend.regions import (
    Region, TryRegion, CatchRegion, FinallyRegion,
    SequenceRegion, LoopRegion, IfRegion,

)
from hermes_decompiler.backend.transforms.shared import (
    negate_condition, is_loop_guard_shaped, has_bottom_tested_guard
)
from hermes_decompiler.core.Exceptions import StructurerInvariantError
from hermes_decompiler.core.logging import get_logger
from hermes_decompiler.ir.statements import BreakStatement
from hermes_decompiler.ir.terminators import (
    TerminatorConditionalBranch,
    TerminatorJump,
    TerminatorReturn,
    TerminatorThrow,
)
from ._base import RegionStructurer

logger = get_logger(__name__)


class LoopBreakStructurer(RegionStructurer):
    """
    Converts a mid-loop conditional exit into a structured control flow.

    Two exit-body shapes are recognized, both requiring a single-block
    exit body reached only from the candidate block (see `_convert`'s
    shared predecessor/ownership checks):

    Shape A - the exit body rejoins the loop's own post-loop code:

        <loop body block>:
            if (cond) goto EXIT; # EXIT is outside loop.members
            ...

        EXIT:
            <exit body>
            goto MERGE; # loop's own back-edge exit target

    Rewritten to:

        <loop body block>:
            if (cond) {
                <exit body>
                break;
            }
            ...

    Shape B - the exit body terminates the function outright (a direct
    `return`/`throw`) rather than rejoining the loop's merge point at
    all:

        <loop body block>:
            if (cond) goto EXIT;
            ...

        EXIT:
            <exit body>
            return X; # or: throw X;

    Rewritten to:

        <loop body block>:
            if (cond) {
                <exit body>
                return X; # exit_block's own terminator, untouched
            }
            ...

    No synthetic `break` is needed for Shape B: a `return`/`throw`
    already exits every enclosing scope (including the loop) on its
    own, so there's nothing for a `break` to add - and, unlike Shape
    A, there is no "loop's own natural merge address" to compare
    against, since the exit body never rejoins the loop's normal
    completion path at all.

    Shape D - the exit target IS the loop's own natural merge block,
    not just code that eventually jumps there:

        <loop body block>:
            if (cond) goto MERGE; # MERGE is the loop's OWN merge address
            ...

        MERGE: # loop's own back-edge exit ALSO lands here
            <shared post-loop code>

    Rewritten to:

        <loop body block>:
            if (cond) {
                break;
            }
            ...

        MERGE: # untouched, still reached identically by normal completion
            <shared post-loop code>

    A `break` in JS already jumps to exactly this same point that
    falling out of the loop normally does - so unlike Shapes A-C,
    nothing needs relocating at all: MERGE stays exactly where it is,
    in the tree, still reached by the loop's own latch edge exactly as
    before conversion. This is what actually makes Shape D safe
    despite MERGE having more than one predecessor (`block`, plus at
    least one of `loop.latches`) - the single-predecessor requirement
    the other shapes need exists specifically because THEY relocate
    exit_block into the break's own `then` branch, which would strand
    any other predecessor; Shape D never relocates anything, so that
    requirement doesn't apply to it. Most commonly seen when the loop
    sits inside a `try`/`finally` whose `finally` covers the loop's
    exit as a whole (see `tryFinallyLoopBreakTest`): the natural
    completion path and the break path are BOTH, entirely legitimately,
    routed through that same shared merge point.

    Must run after LoopStructurer (needs loop.body.covered_blocks) and
    before IfStructurer, which would otherwise consume the branch as
    an ordinary conditional and strand it - see StructuralAnalyzer's
    unstructured-block audit.

    Deliberately narrow: only a single-block exit body is matched, and
    only when its own terminator is one of the recognized shapes
    above (trailing unconditional jump to the loop's natural merge, a
    direct Return/Throw, or - Shape D - the exit target coinciding
    with the loop's own merge block outright). Anything else (a
    Switch, another ConditionalBranch, a jump elsewhere) is left as an
    unstructured conditional branch rather than guessed at.
    """

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
            self._try_recognize_breaks(region)
            self._visit(region.body)
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

    def _try_recognize_breaks(self, loop: LoopRegion) -> None:
        """
        Converts one break candidate at a time in loop.body.children,
        restarting the scan after each conversion since mutation
        invalidates iteration.
        """

        failed: set = set()

        while True:
            block = self._find_candidate(loop, failed)

            if block is None:
                return

            if not self._convert(loop, block):
                failed.add(block)

    @staticmethod
    def _find_candidate(loop: LoopRegion, exclude: set) -> BasicBlock | None:

        header_is_guard = is_loop_guard_shaped(loop.header_block, loop)

        for item in loop.body.children:

            if not isinstance(item, BasicBlock):
                continue

            if item in exclude:
                continue

            if item is loop.header_block and header_is_guard:
                # Only exclude the header when it's genuinely the loop's
                # top-tested guard (LoopConditionRegionPass will consume
                # it). When the loop is actually bottom-tested (guard
                # lives at the latch - see is_loop_guard_shaped), the
                # header's own branch is just an ordinary in-body
                # conditional and IS a legitimate break candidate.
                continue

            if item in loop.latches and header_is_guard:
                # Mirror: only exclude the latch when the header holds the
                # real guard (top-tested) - a latch's own back-edge test
                # is then unconditional and never itself a break shape.
                # When the loop is bottom-tested instead, the latch DOES
                # carry the loop's real conditional guard and must stay
                # untouched here (LoopConditionRegionPass's job) -
                # `has_bottom_tested_guard` covers that case directly.
                continue

            if item in loop.latches and has_bottom_tested_guard(loop):
                continue

            if isinstance(item, BasicBlock) and isinstance(item.terminator, TerminatorConditionalBranch):
                return item

        return None

    def _convert(self, loop: LoopRegion, block: BasicBlock) -> bool:

        branch = block.terminator
        if not isinstance(branch, TerminatorConditionalBranch):
            raise StructurerInvariantError(
                f"expected block {block.id} to end in TerminatorConditionalBranch, "
                f"got {type(branch).__name__}"
            )

        covered = loop.body.covered_blocks

        target_block = next(
            (s for s in block.successors if s.address == branch.target), None
        )
        fallthrough_candidates = [s for s in block.successors if s is not target_block]
        fallthrough_block = fallthrough_candidates[0] if len(fallthrough_candidates) == 1 else None

        if target_block is None or fallthrough_block is None:
            return False

        target_inside = target_block in covered
        fallthrough_inside = fallthrough_block in covered

        if target_inside == fallthrough_inside:
            # Both inside (ordinary in-loop if) or both outside
            # (shouldn't happen for a block that's itself in the
            # loop) - not the shape this pass handles.
            return False

        if target_inside:
            # `_stay_block` (the branch target that remains inside the loop)
            # is only kept for symmetry with the `else` arm below - it's not
            # otherwise consumed by this method.
            exit_block, _stay_block, condition = fallthrough_block, target_block, negate_condition(branch.condition)
        else:
            exit_block, _stay_block, condition = target_block, fallthrough_block, branch.condition

        if list(exit_block.predecessors) != [block]:
            # Reached some other way too - ordinarily not a clean
            # single-purpose exit body, so not safe to relocate. But
            # when that "some other way" is specifically the loop's
            # OWN natural completion edge landing on this exact same
            # block - i.e. exit_block doesn't just eventually rejoin
            # the loop's post-loop code, it IS that code, already
            # sitting exactly where it needs to stay - nothing needs
            # relocating at all. See Shape D below.
            if self._is_loops_own_merge_block(loop, block, exit_block):
                return self._convert_bare_break(loop, block, branch, condition)

            logger.debug(
                "LoopBreakStructurer: block %d's exit target %d has other "
                "predecessors; skipping.", block.id, exit_block.id,
            )
            return False

        exit_owner = self.graph.owner(exit_block)

        if exit_owner is None:
            return False

        exit_terminator = exit_block.terminator

        # ---- Shape A: exit body rejoins the loop's own natural merge via an explicit jump ----
        if isinstance(exit_terminator, TerminatorJump):
            natural_merge = self._natural_loop_merge(loop)
            if natural_merge is None or exit_terminator.target != natural_merge:
                return False
            return self._convert_break_shape(
                loop, block, branch, exit_block, exit_terminator, condition,
            )

        # ---- Shape C: exit body rejoins the loop's natural merge via implicit fallthrough ----
        #
        # Hermes sometimes lays the exit body out as the LAST block before
        # the loop's own post-loop code, with no explicit trailing Jmp -
        # the "fallthrough" itself already lands on the merge address (see
        # CFGBuilder._connect_edges' `case None:`, which wires such a
        # block straight to the next block in program order). Structurally
        # identical to Shape A - same natural-merge check - just without
        # an instruction to strip, since there was never a jump to begin
        # with.
        if exit_terminator is None:
            natural_merge = self._natural_loop_merge(loop)
            successors = list(exit_block.successors)
            if (
                    natural_merge is None
                    or len(successors) != 1
                    or successors[0].address != natural_merge
            ):
                return False
            return self._convert_break_shape_fallthrough(loop, block, branch, exit_block, condition)

        # ---- Shape B: exit body terminates the function directly ----
        if isinstance(exit_terminator, (TerminatorReturn, TerminatorThrow)):
            return self._convert_terminal_shape(loop, block, branch, exit_block, condition)

        return False

    def _convert_break_shape_fallthrough(
            self,
            loop: LoopRegion,
            block: BasicBlock,
            branch: TerminatorConditionalBranch,
            exit_block: BasicBlock,
            condition,
    ) -> bool:
        """Shape C: like `_convert_break_shape`, but exit_block never had
        an explicit trailing Jmp to strip - it merged into the loop's
        natural post-loop code purely by falling off the end of the block
        list. Only the synthetic `break` needs appending; there's no
        terminator instruction to clear first.
        """
        if not self._strip_block_branch(block, branch):
            return False

        # Append a synthetic break as a NEW instruction, since - unlike
        # Shape A - there is no existing trailing jump instruction here to
        # commandeer. Mirrors LoopLabeledExitStructurer's
        # `_append_labeled_statement` approach for the same reason: the
        # escape edge is a bare fallthrough with nothing to repurpose.
        # `hex_address=""` is safe here too: OpcodeEntry maps an invalid
        # address to 0, and nothing downstream keys off this entry's address.
        from hermes_decompiler.frontend.opcode import OpcodeEntry, OpcodeResult

        entry = OpcodeEntry(bytecode="<synthetic>: BreakStatement", hex_address="")
        exit_block.instructions.append(OpcodeResult(entry, statement=BreakStatement(label=None)))

        self._splice_exit_block_as_then(loop, block, exit_block, condition)
        return True

    # -------------------------------------------------------------
    # Shape A: synthetic `break`
    # -------------------------------------------------------------

    def _convert_break_shape(
            self,
            loop: LoopRegion,
            block: BasicBlock,
            branch: TerminatorConditionalBranch,
            exit_block: BasicBlock,
            exit_terminator: TerminatorJump,
            condition,
    ) -> bool:

        if not self._strip_block_branch(block, branch):
            return False

        # ---- strip exit_block's trailing jump, append synthetic break ----

        if exit_block.instructions and exit_block.instructions[-1].terminator is exit_terminator:
            break_instr = exit_block.instructions[-1]
            break_instr.terminator = None
            break_instr.value = None
            break_instr.statement = BreakStatement(label=None)
        else:
            return False

        exit_block.terminator = None

        self._splice_exit_block_as_then(loop, block, exit_block, condition)
        return True

    # -------------------------------------------------------------
    # Shape B: exit body's own Return/Throw is left untouched
    # -------------------------------------------------------------

    def _convert_terminal_shape(
            self,
            loop: LoopRegion,
            block: BasicBlock,
            branch: TerminatorConditionalBranch,
            exit_block: BasicBlock,
            condition,
    ) -> bool:
        """
        Splice a Return/Throw-terminated exit block in as a structured
        `if`, with no synthetic `break`.

        Unlike Shape A, exit_block's own terminator (Return/Throw)
        already exits every enclosing scope on its own - there's no
        loop-merge address to strip a jump down to, and nothing needs
        appending. `exit_block.terminator` is deliberately left as-is;
        only `block`'s own conditional branch is consumed here.
        """

        if not self._strip_block_branch(block, branch):
            return False

        self._splice_exit_block_as_then(loop, block, exit_block, condition)
        return True

    # -------------------------------------------------------------
    # Shape D: exit target IS the loop's own merge block - bare `break`
    # -------------------------------------------------------------

    def _is_loops_own_merge_block(self, loop: LoopRegion, block: BasicBlock, exit_block: BasicBlock) -> bool:
        """True when every predecessor of `exit_block` OTHER than
        `block` itself is either one of `loop.latches` DIRECTLY, or a
        block that DOMINATES `loop.header_block` - i.e. `exit_block`
        isn't just some code that happens to sit at the same address
        the loop's own completion would also land on (address
        collisions do happen - see below), it is, itself, actually
        reached by the loop's own machinery: its back-edge exit (a
        latch), or a pre-header guard mandatorily passed through
        before the loop is ever entered at all (`tryFinallyLoopBreakTest`'s
        own shape: an empty-array check that skips the loop, and the
        loop's own natural completion, BOTH land on the same
        try/finally cleanup exit_block also sits at).

        A predecessor that merely DOESN'T belong to `loop.body` is not
        enough on its own to qualify as that pre-header guard: an
        OUTER loop's own latch is equally outside THIS (inner) loop's
        `covered_blocks`, yet reaches this exact address purely by
        coincidence when a labeled `continue` on that outer loop
        happens to target it (confirmed regression in
        `tripleNestedLabeledTest`: turned a real `continue loop_2;`
        into a bare `break;`, silently dropping the label along with
        the entire outer iteration it was supposed to complete).
        Dominance is what tells these two apart where a plain
        "outside `covered`" check can't: a genuine pre-header guard is
        passed through on EVERY path into the loop, so it dominates
        `loop.header_block` by definition; an outer loop's latch does
        NOT (the outer loop's very first iteration reaches the inner
        loop's header without ever passing through the outer latch at
        all).

        A SECOND, independent hazard applies specifically when the
        match comes through `loop.latches` (not the dominance branch):
        this loop's own latch reaching `exit_block` is only trustworthy
        when `exit_block` is genuinely post-loop code, not another
        loop's own back-edge machinery that this loop's latch happens
        to fall straight into on natural completion (confirmed, a
        second time, in `tripleNestedLabeledTest`: the INNERMOST loop's
        own natural completion falls directly into the MIDDLE loop's
        own latch/recheck block - exactly where a labeled `continue
        loop_2;`, from deeper inside the innermost loop, ALSO lands, so
        the two coincide purely from nested-loop code layout, not
        because it's this loop's own exit). A back-edge - any
        terminator target address at or before `exit_block`'s own
        address - is what marks a block as being itself some OTHER
        loop's latch, so that's refused outright rather than trying to
        identify whose loop it actually belongs to.
        """
        others = set(exit_block.predecessors) - {block}

        if not others:
            return False

        latches = set(loop.latches)

        if latches & others and exit_block.terminator is not None:
            if any(
                    target <= exit_block.address
                    for target in exit_block.terminator.targets
            ):
                return False

        dominator_tree = self.cfg.dominator_tree

        for predecessor in others:
            if predecessor in latches:
                continue

            if (
                    dominator_tree is not None
                    and dominator_tree.dominates(predecessor, loop.header_block)
            ):
                continue

            return False

        return True

    def _convert_bare_break(
            self,
            loop: LoopRegion,
            block: BasicBlock,
            branch: TerminatorConditionalBranch,
            condition,
    ) -> bool:
        """Shape D: splice in a bare `if (cond) { break; }`, touching
        nothing but `block` itself - unlike every other shape, there is
        no exit body to move: `exit_block` (the loop's own merge block)
        stays exactly where it already is, in the tree, still reached
        by the loop's own latch edge precisely as before. The `then`
        body is a brand new single-instruction block holding nothing
        but the synthetic `break`, matching how `_convert_break_shape_
        fallthrough` fabricates one where Hermes left no real
        instruction to repurpose.
        """

        if not self._strip_block_branch(block, branch):
            return False

        from hermes_decompiler.frontend.opcode import OpcodeEntry, OpcodeResult

        new_id = max((b.id for b in self.cfg.blocks), default=0) + 1

        break_block = BasicBlock(new_id, address=block.address)

        entry = OpcodeEntry(bytecode="<synthetic>: BreakStatement", hex_address="")
        break_block.instructions.append(OpcodeResult(entry, statement=BreakStatement(label=None)))

        self.cfg.blocks.append(break_block)

        then_body = SequenceRegion()
        self.graph.transfer([break_block], then_body)

        if_region = IfRegion()
        if_region.condition = condition
        if_region.then_body = then_body
        if_region.else_body = None

        insert_at = loop.body.children.index(block) + 1
        self.graph.insert_at(loop.body, insert_at, if_region)

        return True

    # -------------------------------------------------------------
    # Shared helpers
    # -------------------------------------------------------------

    @staticmethod
    def _strip_block_branch(block: BasicBlock, branch: TerminatorConditionalBranch) -> bool:
        """Remove `branch` from `block`, clearing both the terminator
        and its owning instruction. Shared by both shapes since the
        candidate block's own branch is consumed identically either
        way - only what happens to `exit_block` differs.
        """

        if block.instructions and block.instructions[-1].terminator is branch:
            block.instructions.pop()
            block.terminator = None
            return True

        # Invariant violated: the branch we're converting isn't
        # owned by block's last instruction. Bail rather than
        # clear block.terminator while leaving a stale
        # branch-owning instruction behind.
        logger.warning(
            "LoopBreakStructurer: block %d's terminator instruction "
            "was not found where expected; aborting conversion.",
            block.id,
        )
        return False

    def _splice_exit_block_as_then(
            self,
            loop: LoopRegion,
            block: BasicBlock,
            exit_block: BasicBlock,
            condition,
    ) -> None:
        """Move exit_block out of its old home, into a fresh then_body
        spliced in right after `block` in the loop body.
        """

        self.graph.extract_block(exit_block)

        then_body = SequenceRegion()
        self.graph.transfer([exit_block], then_body)

        if_region = IfRegion()
        if_region.condition = condition
        if_region.then_body = then_body
        if_region.else_body = None

        insert_at = loop.body.children.index(block) + 1
        self.graph.insert_at(loop.body, insert_at, if_region)

    # -------------------------------------------------------------

    @staticmethod
    def _natural_loop_merge(loop: LoopRegion) -> int | None:
        """
        Address a `break` (or the loop's own normal completion) lands
        on, after chasing through any bare-Jmp trampoline blocks Hermes
        routes this edge through (see `_chase_trampoline_address` -
        mirrors LoopLabeledExitStructurer's identical need for the same
        reason: a latch's immediate exit successor is sometimes just a
        single-instruction unconditional-Jmp block, not the true
        post-loop merge point itself).

        Returns None unless every latch agrees on the same FINAL
        (post-trampoline) address - disagreement signals an irregular
        loop shape this pass should not guess about.
        """
        covered = loop.body.covered_blocks

        address_to_block = LoopBreakStructurer._address_to_block_map(loop)

        merge_addresses = {
            LoopBreakStructurer._chase_trampoline_address(
                successor.address, covered, address_to_block
            )
            for latch in loop.latches
            for successor in latch.successors
            if successor not in covered
        }

        if len(merge_addresses) != 1:
            return None

        return merge_addresses.pop()

    @staticmethod
    def _address_to_block_map(loop: LoopRegion) -> dict[int, BasicBlock]:
        """Build an address->block map covering every block reachable from
        the loop's own latches - enough to resolve a short trampoline
        chain without needing the full cfg.blocks list threaded through
        this (currently cfg-less) static helper.

        Walking from covered/latch successors rather than requiring a
        `cfg` reference keeps `_natural_loop_merge` a plain staticmethod,
        matching its existing signature; the chain here is always at most
        a couple of hops.
        """
        seen: dict[int, BasicBlock] = {}
        stack = [
            successor
            for latch in loop.latches
            for successor in latch.successors
            if successor not in loop.body.covered_blocks
        ]
        while stack:
            block = stack.pop()
            if block.address in seen:
                continue
            seen[block.address] = block
            stack.extend(block.successors)
        return seen

    @staticmethod
    def _chase_trampoline_address(
            address: int,
            covered: set,
            address_to_block: dict,
    ) -> int:
        """Follow a chain of bare-Jmp trampoline blocks starting at
        `address`, returning the address the chain ultimately lands on.

        Same logic and same rationale as
        LoopLabeledExitStructurer._chase_trampoline_address - duplicated
        rather than shared/imported across structurer packages per this
        codebase's existing convention (see e.g. `_negate_condition`
        imports vs. inlined near-duplicates elsewhere), since the two
        passes' block/cfg access shapes differ slightly (this one walks
        from `loop.latches` instead of a `self.cfg.blocks` address map).
        """
        seen: set[int] = set()

        while address not in seen:
            seen.add(address)
            candidate = address_to_block.get(address)

            if candidate is None or candidate in covered:
                return address

            if not isinstance(candidate.terminator, TerminatorJump):
                return address

            if len(candidate.instructions) > 1:
                return address

            if (
                    candidate.instructions
                    and candidate.instructions[0].terminator is not candidate.terminator
            ):
                return address

            address = candidate.terminator.target

        return address
