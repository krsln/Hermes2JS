from __future__ import annotations

from hermes_decompiler.backend.analysis.cfg import BasicBlock
from hermes_decompiler.backend.regions import (
    IfRegion,
    LoopRegion,
    SequenceRegion,
    TryRegion,
)
from hermes_decompiler.backend.transforms.shared import negate_condition, is_loop_guard_shaped
from hermes_decompiler.backend.transforms.structurers import RegionStructurer
from hermes_decompiler.core.Exceptions import StructurerInvariantError
from hermes_decompiler.core.logging import get_logger
from hermes_decompiler.ir.expressions import BinaryExpression, Literal, UndefinedLiteral
from hermes_decompiler.ir.Operators import BinaryOperator
from hermes_decompiler.ir.terminators import TerminatorConditionalBranch, TerminatorJump, TerminatorReturn
from ._predicates import is_backward_branch, is_constant_comparison, representative_block

logger = get_logger(__name__)


class _DominanceIfBuilder(RegionStructurer):
    """Converts BasicBlocks ending in a ConditionalBranch into IfRegions.

    Two CFG shapes are recognized:

    1. No else::

           if (C) goto MERGE;
           THEN
           MERGE:

       becomes::

           if (!C) { THEN }

    2. If/else::

           if (C) goto ELSE;
           THEN
           goto MERGE;
           ELSE:
               ELSE_BODY
           MERGE:

       becomes::

           if (C) { ELSE_BODY } else { THEN }

    Loop header blocks are excluded - their ConditionalBranch is
    consumed later by LoopConditionExtractor when building
    while/do-while regions.

    then/else membership is decided by dominance (see `_convert`), not
    by position in `region.children`, so else-if chains and any block
    layout the compiler chose are handled without special-casing.

    Purely structural: only decides which blocks become then/else of a
    new IfRegion and splices the tree accordingly. Condition-shape
    rewrites (`&&`/`||` folding, cascade recovery) are
    `_CompoundConditionFolder`'s job and always run after this builder
    (see `IfStructurer.run`).
    """

    def __init__(self, graph, cfg):
        super().__init__(graph, cfg)

        self._address_to_block: dict[int, BasicBlock] = {
            block.address: block
            for block in cfg.blocks
        }

    # -------------------------------------------------------------

    def run(self) -> None:
        """Structure the tree, then re-sweep for residual branches.

        A second sweep (not a fixed-point loop) is required: the first
        pass can leave a freshly created else-arm's own residual
        branch unconverted, since that branch didn't exist yet when
        the sweep reached it. One extra sweep always catches it, since
        at most one new residual is introduced per level of `&&`/`||`
        nesting; deeper nesting is folded afterward by
        `_CompoundConditionFolder`, not built fresh here.
        """
        self._visit(self.graph.root, exclude=frozenset())
        self._visit(self.graph.root, exclude=frozenset())
        self.dump_region_tree_if_debug(type(self).__name__)

    # -------------------------------------------------------------
    # Tree traversal
    # -------------------------------------------------------------

    def _visit(self, region, exclude: frozenset):
        """Recursively structure conditional blocks throughout region."""

        if isinstance(region, SequenceRegion):
            self._structure_sequence(region, exclude)

            for child in region.children:
                self._visit(child, frozenset())

            return

        if isinstance(region, LoopRegion):
            exclude = (
                frozenset({region.header_block})
                if is_loop_guard_shaped(region.header_block, region)
                else frozenset()
            )
            self._visit(region.body, exclude)
            return

        if isinstance(region, IfRegion):
            self._visit(region.then_body, frozenset())

            if region.else_body:
                self._visit(region.else_body, frozenset())

            return

        if isinstance(region, TryRegion):
            self._visit(region.try_body, frozenset())

            region_catch = region.catch
            if region_catch is not None:
                self._visit(region_catch.body, frozenset())

            region_finally = region.finally_
            if region_finally is not None:
                self._visit(region_finally.body, frozenset())

            return

        if hasattr(region, "body"):
            self._visit(region.body, frozenset())

    # -------------------------------------------------------------
    # Sequence conversion
    # -------------------------------------------------------------

    def _structure_sequence(self, region: SequenceRegion, exclude: frozenset):
        """Convert eligible conditional blocks in region.children.

        Repeatedly converts the leftmost eligible block, restarting
        after each conversion since the list is mutated in place.
        Blocks where `_convert` bails out are tracked in `failed` and
        never retried, since `_convert` leaves them unchanged and the
        next search would otherwise find the same candidate forever.
        """

        failed: set = set()

        while True:

            block = self._find_candidate(region, exclude | failed)

            if block is None:
                return

            if not self._convert(region, block):
                failed.add(block)

    # -------------------------------------------------------------

    @staticmethod
    def _find_candidate(region: SequenceRegion, exclude: frozenset) -> BasicBlock | None:
        """Return the first convertible conditional block, or None."""

        for item in region.children:

            if not isinstance(item, BasicBlock):
                continue

            if item in exclude:
                continue

            if not isinstance(item.terminator, TerminatorConditionalBranch):
                continue

            if is_backward_branch(item):
                # Loop machinery (guard/continue test), never a
                # genuine forward if/goto-merge residual. Must stay
                # untouched here so LoopConditionExtractor (runs later,
                # in region_passes) can recognize it as the loop guard.
                continue

            return item

        return None

    # -------------------------------------------------------------

    def _convert(self, region: SequenceRegion, block: BasicBlock) -> bool:
        """Try to convert `block` into an IfRegion; return success.

        Classifies every item after `block` by dominance rather than
        list position: an item is "then" iff dominated by the
        fallthrough block, and "else" iff dominated by the branch
        target - regardless of how the compiler interleaved the two
        arms in the flat sequence, or where `merge_block` sits. This
        also subsumes the single-entry check: an item with a
        predecessor outside its claimed side simply fails the
        `dominates()` test below and the candidate correctly bails.
        """

        branch = block.terminator
        if not isinstance(branch, TerminatorConditionalBranch):
            raise StructurerInvariantError(
                f"expected block {block.id} to end in TerminatorConditionalBranch, "
                f"got {type(branch).__name__}"
            )

        if self.cfg.dominator_tree is None:
            # Dominator tree must be precomputed by the caller before
            # structuring runs; nothing can be safely classified without it.
            return False

        block_index = region.children.index(block)
        then_start = block_index + 1

        if then_start >= len(region.children):
            # No fallthrough successor - can't structure safely.
            return False

        then_root = region.children[then_start]
        then_entry = representative_block(then_root)

        if then_entry is None:
            return False

        merge_block: BasicBlock | None = None

        if self.cfg.post_dominator_tree is not None:
            merge_block = self.cfg.post_dominator_tree.immediate_post_dominator(block)

        goto_block = self._address_to_block.get(branch.target)

        if goto_block is not None and merge_block is goto_block and self._leaves_its_loop(block, goto_block):
            # `if (x < 0) goto RET; ...rest` in a loop body, RET behind the loop: as
            # `if (!(x < 0)) { rest }` the body would simply end and the loop go on.
            # `LoopBreakStructurer` takes such an exit when it owns the target; a shared
            # `return` it does not own (96/4123: `if (n < 0 || n > 255) return null`)
            # stays a branch, and the attempt with private return copies has it.
            return False

        if merge_block is None and goto_block is not None and not isinstance(then_root, BasicBlock):
            # Post-dominance can legitimately come back empty when the
            # fallthrough side contains its own internal dead-end with
            # no CFG successor - most commonly a raw, not-yet-structured
            # `throw` inside a loop (IfStructurer runs before
            # TryStructurer, so a try/catch nested in the loop hasn't
            # been recognized yet - see
            # tryCatchInsideLoopTest/section_15085's own zero-trip loop
            # guard: "if (!(0 < items.length)) { skip } else { for
            # (...) { try { ...; if (x<0) throw ...; } catch {...} } }").
            # That dead-end being unreachable from the exit doesn't
            # mean goto_block ISN'T still the genuine shared
            # continuation for every path that DOESN'T hit it - check
            # plain forward reachability instead, which only needs ONE
            # path to confirm the connection, unlike post-dominance
            # (which correctly, for its own stricter purpose, requires
            # EVERY path to agree).
            #
            # Deliberately restricted to `then_root` already being a
            # structured Region (a LoopRegion here, but any Region
            # qualifies), NOT a bare BasicBlock: a raw block's own
            # pending conditional branch can ALSO directly reach
            # `goto_block` via its OWN alternate arm - reachable, but
            # not because it's a shared merge point, only because it's
            # one option among several a still-unstructured comparison
            # chain could take (see switchTest/section_15056's `case 3:
            # case 4:` fallthrough chain, whose own cascading
            # `if (3!==x) { if (4!==x) {...} }` shape relies on
            # `has_else=True` at EVERY link for SwitchStructurer to
            # recognize it afterward - this fallback firing there
            # collapses that chain into a differently-shaped, still
            # correct but no-longer-recognizable nested if/else).
            # `representative_block`'s own single-block value is what
            # would get reached via `then_root.terminator`, not some
            # separate, already-resolved "the region eventually exits
            # here" edge the way a Region's own back-edge/break
            # machinery provides - so the same reachability check
            # means something entirely different (and unreliable) for
            # it.
            if self._is_reachable(then_entry, goto_block):
                merge_block = goto_block

        if (
                goto_block is not None
                and goto_block is not merge_block
                and (
                self._arm_leaves_the_region(region, then_start, goto_block)
                or (
                        # Only once shared returns were given private copies:
                        # until then the arm's own exit can still be the block
                        # the else side owns, and a join would drop it silently.
                        getattr(self.cfg, "duplicated_returns", False)
                        and merge_block is None
                        and self._arm_tests_into(then_entry, goto_block)
                )
                or (
                        # `if (a) { if (b) return x; else goto tail } tail`: the arm's
                        # own test jumps to the code the outer branch skips to, and
                        # that code goes on (no exit block): it is the join.
                        merge_block is None
                        and goto_block.successors
                        and not self._reaches_itself(then_entry)
                        and (
                                self._arm_tests_into(then_entry, goto_block)
                                or self._arm_runs_into(then_entry, goto_block, block)
                        )
                )
                or (
                        # `if (a) { ...; x(); } return null` where the branch skips to a
                        # shared `return` and the arm's last block runs on into it: the
                        # `return` follows the `if`; as an `else` arm it would leave the
                        # arm's end without it.
                        merge_block is None
                        and not goto_block.successors
                        and isinstance(goto_block.terminator, TerminatorReturn)
                        and self._arm_runs_into(then_entry, goto_block, block, outside_loops=True)
                )
                or (
                        # `if (n > 0) { for (...) { ... } } tail`: the loop the guard
                        # skips ends into the very code the guard jumps to (its exit
                        # edge is the one of `tail`), so `tail` follows the `if`.
                        # Other exits of the loop (a `return`, a `break` elsewhere)
                        # make the post-dominator a later block, which hides it.
                        isinstance(then_root, LoopRegion)
                        and goto_block.successors
                        and self._arm_runs_into_after_loop(then_entry, goto_block, block)
                )
                or (
                        # Only once the shared returns were copied (a retry): the arm's other exits
                        # are real `return`s then, so an arm that runs on into the branch target
                        # leaves the target after the `if`, not in an `else` arm that would print it
                        # on the branch's own path only (98/10128, 96/11046: the loop tail entered by
                        # the `is()` test and fallen into by the last check).
                        getattr(self.cfg, "duplicated_returns", False)
                        and not is_constant_comparison(branch.condition)
                        and goto_block.successors
                        and self._arm_falls_into(then_entry, goto_block, block)
                )
                or (
                        # `if (a) { if (b) return x; } tail`: the arm's guard
                        # falls through into the very code the outer branch
                        # jumps to, which only ends the function, so no
                        # post-dominator exists to say it is a join.
                        merge_block is None
                        and self._arm_guard_falls_into(region, then_entry, goto_block, block)
                )
        )
                and any(
            pred is not block and self.cfg.dominator_tree.dominates(then_entry, pred)
            for pred in goto_block.predecessors
        )
        ):
            # The fallthrough arm itself flows into the branch target, so
            # the target is the join, not an `else` arm. The post-dominator
            # can miss it when another path of the arm leaves the region
            # (`if (a) { if (b) break; } x();` with `x` the loop latch).
            # Gated on such a carved-out exit: a plain case-fallthrough
            # chain (`switchTest`) needs `has_else` at every link.
            merge_block = goto_block

        has_else = goto_block is not merge_block and goto_block is not None

        # else_root = None
        else_entry = None

        if has_else and goto_block is not None:

            else_root = self.graph.find_covering_item(region, goto_block)

            if else_root is None or else_root is then_root:
                # goto target isn't a distinct sibling in this region -
                # bail rather than guess.
                return False
            else_entry = representative_block(else_root)

        # -------------------------------------------------------------
        # Classify region.children[then_start:] by dominance until the
        # merge point (or end of region) is reached.
        # -------------------------------------------------------------

        dominators = self.cfg.dominator_tree

        then_items: list = []
        else_items: list = []

        index = then_start
        boundary = len(region.children)
        last_side: list | None = None

        while index < len(region.children):

            item = region.children[index]

            if item is merge_block:
                boundary = index
                break

            rep = representative_block(item)

            if rep is not None and rep.address < 0 and last_side is not None:
                # A region made only of synthetic blocks (`if (c) break;`
                # after the loop structurers ran) has no node in the
                # dominator tree. It stays with the item it follows:
                # that item's conditional branch is what it replaced.
                last_side.append(item)

            elif dominators.dominates(then_entry, rep):
                then_items.append(item)
                last_side = then_items

            elif has_else and dominators.dominates(else_entry, rep):
                else_items.append(item)
                last_side = else_items

            else:
                # Neither side dominates - this is the true merge
                # point. `merge_block` is only a heuristic shortcut for
                # finding it in advance and can legitimately differ,
                # e.g., when a break (or other loop-exit edge) already
                # carved out into its own region bypasses the merge on
                # the raw CFG. Safe to stop here regardless, since
                # `then_root` always self-dominates and is guaranteed
                # to already be in `then_items` by this point.
                boundary = index
                break

            index += 1

        if has_else and not else_items:
            # else_root dominates itself and must have been classified
            # above; empty here means something upstream is
            # inconsistent. Bail rather than build a broken else.
            return False

        # A trailing unconditional jump to merge_block is the
        # compiled-away "goto past the if/else" and would otherwise
        # print as a confusing literal `goto label_N;`. Only a jump to
        # *this* merge_block, on the branch's last block, is stripped;
        # jumps elsewhere (genuine tail-merged code) are left alone -
        # that's labeled break/continue support, not handled here.
        if merge_block is not None:
            self._strip_trailing_jump_to(then_items, merge_block)
            if has_else:
                self._strip_trailing_jump_to(else_items, merge_block)

        # Prefer RegionGraph mutation APIs so covered_blocks stays in sync.
        self.graph.splice_out(region, then_start, boundary)

        then_body = SequenceRegion()
        else_body = SequenceRegion() if has_else else None

        if has_else and else_body is not None:

            self.graph.transfer(then_items, else_body)
            self.graph.transfer(else_items, then_body)

            condition = branch.condition

        else:

            self.graph.transfer(then_items, then_body)

            condition = negate_condition(branch.condition)

        if_region = IfRegion()
        if_region.condition = condition
        if_region.then_body = then_body
        if_region.else_body = else_body

        # The ConditionalBranch is now represented by the IfRegion.
        if block.instructions[-1].terminator is None:
            raise StructurerInvariantError(
                f"block {block.id}'s last instruction lost its terminator "
                "before the IfRegion could replace it"
            )
        block.instructions.pop()
        block.terminator = None

        insert_at = region.children.index(block) + 1
        self.graph.insert_at(region, insert_at, if_region)

        return True

    # -------------------------------------------------------------
    # Reachability fallback (see `_convert`'s own comment)
    # -------------------------------------------------------------

    def _arm_tests_into(self, then_entry: BasicBlock, goto_block: BasicBlock) -> bool:
        """True if a conditional branch inside the fallthrough arm jumps to
        `goto_block` (`a || b` shape: both tests share the target)."""
        dominators = self.cfg.dominator_tree
        return any(
            isinstance(pred.terminator, TerminatorConditionalBranch)
            and pred.terminator.target == goto_block.address
            and dominators.dominates(then_entry, pred)
            and not is_constant_comparison(pred.terminator.condition)
            for pred in goto_block.predecessors
        )

    def _arm_falls_into(self, then_entry: BasicBlock, goto_block: BasicBlock, block: BasicBlock) -> bool:
        """True if a block of the fallthrough arm falls through into `goto_block` (a plain block, or a
        test whose taken edge goes elsewhere)."""
        dominators = self.cfg.dominator_tree
        return any(
            pred is not block
            and (
                    pred.terminator is None
                    or (
                            isinstance(pred.terminator, TerminatorConditionalBranch)
                            and pred.terminator.target != goto_block.address
                    )
            )
            and goto_block.address > pred.address
            and dominators.dominates(then_entry, pred)
            for pred in goto_block.predecessors
        )

    def _arm_runs_into(self, then_entry: BasicBlock, goto_block: BasicBlock, block: BasicBlock,
                       outside_loops: bool = False) -> bool:
        """True if a plain block of the fallthrough arm runs on into `goto_block`
        (`if (a) { ...; if (b) return; ...<runs into T> } T` with `a` jumping to `T`).

        `outside_loops`: only blocks that are in no loop count (a loop's exits to a shared
        `return` stay exits)."""
        dominators = self.cfg.dominator_tree
        loop_analysis = self.cfg.loop_analysis if outside_loops else None
        loops = list(loop_analysis.loops.values()) if loop_analysis is not None else []
        return any(
            pred is not block
            and pred.terminator is None
            and dominators.dominates(then_entry, pred)
            and not any(pred in loop.members for loop in loops)
            for pred in goto_block.predecessors
        )

    def _leaves_its_loop(self, block: BasicBlock, target: BasicBlock) -> bool:
        """Is `block` inside a loop (not its header test) and `target` outside it?"""
        loop_analysis = self.cfg.loop_analysis

        if loop_analysis is None:
            return False

        return any(
            block in loop.members
            and block is not loop.header
            and target is not loop.header
            and target not in loop.members
            for loop in loop_analysis.loops.values()
        )

    def _arm_runs_into_after_loop(self, then_entry: BasicBlock, goto_block: BasicBlock, block: BasicBlock) -> bool:
        """True if a block of the loop arm (its exit test) falls through into `goto_block`,
        the code the guard `block` jumps over the loop to."""
        dominators = self.cfg.dominator_tree
        return any(
            pred is not block
            and isinstance(pred.terminator, TerminatorConditionalBranch)
            and pred.terminator.target != goto_block.address
            and dominators.dominates(then_entry, pred)
            for pred in goto_block.predecessors
        )

    def _arm_guard_falls_into(self, region, then_entry: BasicBlock, goto_block: BasicBlock, region_block=None) -> bool:
        """True if `goto_block` ends the function and a conditional branch
        inside the fallthrough arm reaches it by falling through (its taken
        edge goes elsewhere)."""
        if goto_block.successors:
            return False

        # A loop's own exits and back edges are not guards (the exit would be
        # taken for the loop's join): leave those to the loop structurers.
        if self._reaches_itself(then_entry):
            return False

        dominators = self.cfg.dominator_tree

        # No code of the arm may be laid out after the join: it would be left
        # outside the `if` (the arm's own code resumes behind the exit block).
        children = region.children

        if goto_block in children:
            for item in children[children.index(goto_block) + 1:]:
                rep = representative_block(item)

                if (
                        rep is not None
                        and rep.address >= 0
                        and dominators.dominates(then_entry, rep)
                        # a lone exit block is a guard's target, which
                        # `GuardExitRegionPass` moves into its `if` afterwards
                        and not (isinstance(item, BasicBlock) and not item.successors)
                ):
                    return False

        return any(
            (
                # a guard whose taken edge goes elsewhere, or a plain block that
                # runs on into the exit (`if (r5) return a; set(); <exit>`)
                    (
                            isinstance(pred.terminator, TerminatorConditionalBranch)
                            and pred.terminator.target != goto_block.address
                    )
                    or (
                            pred.terminator is None
                            and pred is not region_block
                            and isinstance(goto_block.terminator, TerminatorReturn)
                    )
            )
            and dominators.dominates(then_entry, pred)
            for pred in goto_block.predecessors
        )

    @staticmethod
    def _reaches_itself(block: BasicBlock) -> bool:
        """True if `block` lies on a CFG cycle (it is part of a loop)."""
        seen: set = set()
        stack = list(block.successors)

        while stack:
            current = stack.pop()

            if current is block:
                return True

            if current in seen:
                continue

            seen.add(current)
            stack.extend(current.successors)

        return False

    @staticmethod
    def _arm_leaves_the_region(region, then_start: int, goto_block) -> bool:
        """True if a loop-exit marker (a synthetic `break`/`continue`
        block) sits between the branch and `goto_block` in the sequence."""
        for item in region.children[then_start:]:
            if item is goto_block:
                return False
            rep = representative_block(item)
            if rep is not None and rep.address < 0:
                return True
        return False

    @staticmethod
    def _is_reachable(start: BasicBlock, target: BasicBlock) -> bool:
        """Plain forward reachability via `.successors`, ignoring
        anything structural (Regions) - a raw graph-edges BFS.

        Used only as a fallback signal when post-dominance itself came
        back `None` (see `_convert`) - deliberately weaker than
        post-dominance (only needs ONE path to connect, not every
        path), which is exactly the property needed there: a dead-end
        on some OTHER path (e.g. an unstructured `throw`) doesn't
        invalidate the genuine connection this path provides.
        """
        seen = {start}
        stack = [start]

        while stack:
            current = stack.pop()

            if current is target:
                return True

            for successor in current.successors:
                if successor not in seen:
                    seen.add(successor)
                    stack.append(successor)

        return False

    # -------------------------------------------------------------
    # Trailing-jump cleanup
    # -------------------------------------------------------------

    @staticmethod
    def _strip_trailing_jump_to(items: list, merge_block: BasicBlock) -> None:
        """Remove a trailing jump/branch to merge_block from items.

        Handles both an unconditional jump straight to `merge_block`,
        and a ConditionalBranch whose true edge targets merge_block
        (empty then-body) - dropping the terminator lets the later
        compound-condition pass fold the surrounding IfRegion cleanly.
        """
        if not items:
            return

        last = items[-1]
        if not isinstance(last, BasicBlock):
            return

        terminator = last.terminator

        # Unconditional jump to merge.
        if isinstance(terminator, TerminatorJump):
            if terminator.target != merge_block.address:
                return
            if last.instructions and last.instructions[-1].terminator is terminator:
                last.instructions.pop()
            last.terminator = None
            return

        # Conditional whose true edge is the merge (empty then).
        if isinstance(terminator, TerminatorConditionalBranch):
            if terminator.target != merge_block.address:
                return
            if any(succ is not merge_block for succ in last.successors):
                # The false edge does not reach the merge either: it enters
                # a block outside this arm (a tail shared with the sibling
                # arm). Dropping the test would drop that path silently.
                return
            # The false edge falls through; after stripping, the block
            # becomes a pure condition holder that higher-level folding
            # can turn into part of a compound expression.
            if last.instructions and last.instructions[-1].terminator is terminator:
                last.instructions.pop()
            last.terminator = None
