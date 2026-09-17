"""
Rewrites a recognized hbc97+ generator state machine (see
`_generator_dispatch.detect`) into single-entry, sequential suspend
points - the CFG-level counterpart of what
`GeneratorStateMachineRegionPass` does on the region tree for hbc96's
StartGenerator-based machine.

Why this has to happen on the CFG, not the region tree
--------------------------------------------------------
hbc96's suspend/resume machinery is a single extra `if` per suspend point,
entirely local to where it appears - IfStructurer already turns it into a
clean IfRegion, and the region pass just folds that shape away.

hbc97+'s entry dispatch is not local. It gives every resume point's
target block an *extra predecessor* - the dispatch arm - on top of
whatever predecessor it already has in the function's normal control
flow. A resume point in the middle of a loop body is a real example: the
loop already has one predecessor (its own back edge), and the dispatch
arm adds a second, unrelated one. No structurer accepts that as a
single-entry region, so by the time a region tree exists the damage is
already done - the loop is permanently unstructurable, and the raw goto
that results has nothing to do with the loop itself.

So this pass removes the extra predecessor before any structurer looks
at the CFG: each suspend site's `Ret` is rewired directly to its resume
block, and every block whose only purpose was the dispatch (the
reentrancy/exhausted guards, the comparison chain, each arm's
`.throw()`/`.return()` preamble) is deleted outright. What's left is
ordinary single-entry control flow that every existing structurer already
knows how to handle.
"""

from __future__ import annotations

import re

from hermes_decompiler.backend.analysis.cfg import BasicBlock, CFG
from hermes_decompiler.backend.transforms.cfg_passes._generator_dispatch import GeneratorDispatch, SuspendSite
from hermes_decompiler.core.logging import get_logger
from hermes_decompiler.frontend.opcode import OpcodeResult
from hermes_decompiler.ir.expressions import AwaitExpression, YieldExpression
from hermes_decompiler.ir.expressions.Literals import BooleanLiteral, NullLiteral, NumericLiteral, StringLiteral
from hermes_decompiler.ir.terminators import TerminatorJump, TerminatorReturn

logger = get_logger(__name__)

_PARAM_RE = re.compile(r"UInt8:\s*(-?\d+)")


def _literal_expression(value):
    """
    The IR literal node for a value Hermes baked directly into a
    NewObjectWithBuffer template - i.e. a yielded/awaited expression that
    was a compile-time constant in the source (`yield 1`, not `yield i`).

    `None` itself never reaches here: `_extract_yield_value` treats a
    `None` "value" property in the template as "not baked in, expect a
    following PutOwnBySlotIdx instead" (Hermes's own encoding for
    `{value: undefined, ...}` uses this same `None` placeholder as a
    literal `undefined` in *other* contexts, which is exactly the
    ambiguity that rules out treating a bare `None` as one here).
    """
    if isinstance(value, bool):
        return BooleanLiteral(value=value)
    if isinstance(value, (int, float)):
        return NumericLiteral(value=value)
    if isinstance(value, str):
        return StringLiteral(value=value)

    return NullLiteral()


#: Instructions a suspend site's tail may consist of, beyond the value
#: expression itself, and still be recognized: register shuffling and
#: environment stores (the resume-point/state writes, and any other
#: protocol bookkeeping alongside them - see the module docstring on
#: `_generator_dispatch` for why more than just the resume slot gets
#: written here), then the `{value, done: false}` object construction.
#: Anything else in the tail is unrecognized and the site is left alone.
_TAIL_HANDLERS = frozenset({
    "Mov",
    "StoreToEnvironment", "StoreToEnvironmentL",
    "StoreNPToEnvironment", "StoreNPToEnvironmentL",
    "NewObjectWithBuffer", "NewObjectWithBufferLong",
    "PutOwnBySlotIdx",
    # The Ret opcode's own OpcodeResult is present in block.instructions
    # *in addition to* being block.terminator - this pass replaces the
    # terminator outright (see _apply_fold), so its instructions-list
    # twin is inert leftover, not a real statement to preserve or reject.
    "Ret",
})


class GeneratorStateDispatchCfgPass:
    """
    Applies one recognized `GeneratorDispatch` to `cfg`, in place.

    Deliberately all-or-nothing: `run()` either transforms every suspend
    site and returns True, or changes nothing at all and returns False.
    A half-applied rewrite - some sites folded, others still reading a
    resume slot that no longer gets written because its dispatch chain
    was removed - would silently produce wrong code, which is worse than
    leaving the whole function in its raw, merely-ugly form.
    """

    def __init__(self, cfg: CFG, dispatch: GeneratorDispatch, is_async: bool):
        self.cfg = cfg
        self.dispatch = dispatch
        self.is_async = is_async

    def run(self) -> bool:
        by_address = {block.address: block for block in self.cfg.blocks}

        entry_address = self.dispatch.dispatch_targets.get(0)
        entry_block = by_address.get(entry_address)

        if entry_block is None:
            logger.debug(
                "Generator dispatch: resume point 0 target 0x%x is not a known block; "
                "leaving the raw form in place.",
                entry_address if entry_address is not None else -1,
            )
            return False

        foldable = []  # [(SuspendSite, continuation_block, cut_index, OpcodeResult), ...]

        for site in self.dispatch.suspend_sites:
            continuation = by_address.get(self.dispatch.dispatch_targets[site.resume_point])

            if continuation is None:
                logger.debug(
                    "Generator dispatch: resume point %d has no resolvable target block; "
                    "leaving the raw form in place.",
                    site.resume_point,
                )
                return False

            folded = self._fold_site(site, continuation)

            if folded is None:
                return False

            cut_index, result = folded
            foldable.append((site, continuation, cut_index, result))

        # Every site parsed - simulate the rewiring's effect on
        # reachability *before* touching `cfg` at all, and bail if the
        # dispatch chain would still be reachable afterward. This is not
        # hypothetical: a catch handler cleaning up after an exception
        # mid-suspend can jump straight back into the entry dispatch to
        # re-derive where to resume/re-throw - real generator semantics
        # the JS engine would provide natively once real `yield`s exist,
        # but Hermes still has to hand-implement here, exactly like the
        # reentrancy guard. When that happens, the dispatch chain is not
        # actually dead, and folding the sites anyway would remove the
        # only route back to it while leaving it looking abandoned -
        # confusing at best. See `_dispatch_survives`.
        site_continuations = {site.block.id: continuation for site, continuation, _, _ in foldable}
        dispatch_ids = {block.id for block in self.dispatch.dispatch_blocks}

        if self._dispatch_survives(entry_block, site_continuations, dispatch_ids):
            logger.debug(
                "Generator dispatch on env[%d]: the entry dispatch chain is still reachable "
                "after simulating the rewrite (likely a catch handler re-entering it to "
                "resume/re-throw) - leaving the raw form in place rather than folding the "
                "sites while stranding it.",
                self.dispatch.resume_slot,
            )
            return False

        # Nothing above this point touched `cfg`.
        for site, continuation, cut_index, result in foldable:
            self._apply_fold(site, continuation, cut_index, result)

        self._prune_unreachable(entry_block)

        return True

    def _dispatch_survives(
            self,
            entry_block: BasicBlock,
            site_continuations: dict[int, BasicBlock],
            dispatch_ids: set[int],
    ) -> bool:
        """
        True if any of `dispatch_ids` would still be reachable from
        `entry_block` after rewiring - computed by walking the *current*
        graph's real `.successors`, except at a site block, where the walk
        follows its future continuation instead (the rewire this class is
        about to apply, simulated rather than performed). Reads only;
        nothing here is mutated.

        Mirrors `_prune_unreachable`'s own traversal, including the
        exception-handler fixed point - a handler whose `try_blocks`
        happens to include a site block needs that same substitution
        applied before deciding whether the handler itself, and the rest
        of its protected range, are reachable.
        """
        reachable: set[int] = set()
        frontier = [entry_block]

        while frontier:
            new_frontier: list[BasicBlock] = []

            for block in frontier:
                if block.id in reachable:
                    continue
                reachable.add(block.id)

                if block.id in site_continuations:
                    new_frontier.append(site_continuations[block.id])
                else:
                    new_frontier.extend(block.successors)

            for handler in self.cfg.exception_handlers:
                handler_block = handler["handler_block"]

                if handler_block.id in reachable:
                    continue

                if any(b.id in reachable for b in handler["try_blocks"]):
                    new_frontier.append(handler_block)

            frontier = new_frontier

        return bool(reachable & dispatch_ids)

    # ------------------------------------------------------------------
    # Per-site folding
    # ------------------------------------------------------------------

    def _fold_site(self, site: SuspendSite, continuation: BasicBlock) -> OpcodeResult | None:
        """
        Parse (without mutating) what `site.block` would become.

        Returns the single OpcodeResult the block's tail collapses into,
        or None if the tail doesn't match a recognized shape - in which
        case the caller bails on the *entire* dispatch, per this class's
        all-or-nothing contract.
        """
        block = site.block
        extracted = self._extract_yield_value(block, site.result_index)

        if extracted is None:
            logger.debug(
                "Generator dispatch: could not find the yielded value at block %d (0x%x); "
                "leaving the raw form in place.",
                block.id, block.address,
            )
            return None

        value_expression, cut_index, source_entry, tail_start = extracted
        tail = block.instructions[tail_start:]

        if any(instruction.handler not in _TAIL_HANDLERS for instruction in tail):
            logger.debug(
                "Generator dispatch: unrecognized instruction between the yielded value and "
                "the suspend at block %d (0x%x); leaving the raw form in place.",
                block.id, block.address,
            )
            return None

        if self._reads_resumed_value(continuation):
            # `x = yield ...;` - the resumed value is read back. Real in
            # our fixtures only via LoadParam of the "sent value" formal
            # at the very top of a resume target, and never exercised by
            # any of them - see the module docstring's async/generator
            # note for why binding it correctly needs more than a single
            # register rename. Bailing here is deliberately the same
            # "don't guess a used value away" stance
            # GeneratorStateMachineRegionPass takes on hbc96's equivalent
            # case.
            logger.debug(
                "Generator dispatch: resume point %d's continuation appears to read the "
                "resumed value, which this pass does not yet bind; leaving the raw form in place.",
                site.resume_point,
            )
            return None

        expression = (
            AwaitExpression(argument=value_expression)
            if self.is_async
            else YieldExpression(argument=value_expression)
        )

        return cut_index, OpcodeResult(source_entry, value=expression, dest_reg=None)

    @staticmethod
    def _extract_yield_value(
            block: BasicBlock,
            result_index: int,
    ):
        """
        What the source actually yielded/awaited, and where to cut.

        Returns `(value_expression, cut_index, source_entry, tail_start)`,
        or None if neither recognized shape matches. `cut_index` is where
        the fold replaces `block.instructions[cut_index:]` with the
        single new suspend instruction - `_apply_fold` keeps everything
        before it untouched, which is what preserves any real code that
        happens to run earlier in the same block. `tail_start` is where
        the *validation* in `_fold_site` begins - not always the same
        index as `cut_index`, see below.

        Two shapes, both produced by the same `NewObjectWithBuffer` +
        (optional `PutOwnBySlotIdx`) + `Ret` pattern, differing only in
        whether the yielded value was a compile-time constant:

          - Dynamic (`yield i * i`): the object template has a `None`
            placeholder for `value`, and a following `PutOwnBySlotIdx`
            fills it from a register. The instruction defining that
            register - found by walking backward from the object
            construction - is both the value and the cut point. It is
            real, already-verified computation, not leftover machinery -
            `tail_start` is one past it, so `_fold_site` doesn't turn
            around and reject its own extracted value for not being a
            recognized *tail* shape.

          - Constant (`yield 1`): Hermes folds the literal directly into
            the object template at compile time, and there is no
            `PutOwnBySlotIdx` at all - nothing to walk back to, so the
            whole protocol tail starting at the resume-point store cuts
            away as one piece. `site.store_index` (passed in as
            `result_index`'s sibling on `SuspendSite`) is exactly that
            boundary, but this method only sees the block, so it locates
            the same boundary independently: the object construction
            itself. Here `tail_start` equals `cut_index` - the object
            construction is genuine tail machinery, not an extracted
            value, so it stays subject to validation.
        """
        obj_instruction = block.instructions[result_index]
        literal = getattr(obj_instruction.entry, "object_literal", None)
        baked_value = literal.get("value") if isinstance(literal, dict) else None

        if baked_value is not None:
            return _literal_expression(baked_value), result_index, obj_instruction.entry, result_index

        if result_index + 1 >= len(block.instructions):
            return None

        put = block.instructions[result_index + 1]

        if put.handler != "PutOwnBySlotIdx":
            return None

        slot_args = re.findall(r"Reg8:\s*(-?\d+)", getattr(put.entry, "args", "") or "")

        if len(slot_args) < 2:
            return None

        value_reg = int(slot_args[1])

        for index in range(result_index - 1, -1, -1):
            if block.instructions[index].dest_reg == value_reg:
                instruction = block.instructions[index]
                return instruction.value, index, instruction.entry, index + 1

        return None

    @staticmethod
    def _reads_resumed_value(continuation: BasicBlock) -> bool:
        """
        Conservative check for `x = yield ...;` at a resume target.

        The resumed value arrives as the generator body's second
        parameter (see `_generator_dispatch._action_register`'s sibling
        note on the first), so its presence right at the top of the
        continuation is the signal this pass currently refuses to
        handle. Deliberately narrow (only this one block, only near the
        top) - see `_fold_site`'s docstring for why bailing here is the
        safe default rather than a real limitation.
        """
        return any(
            instruction.handler == "LoadParam"
            and re.search(r"UInt8:\s*2\b", getattr(instruction.entry, "args", "") or "")
            for instruction in continuation.instructions[:3]
        )

    def _apply_fold(
            self,
            site: SuspendSite,
            continuation: BasicBlock,
            cut_index: int,
            result: OpcodeResult,
    ) -> None:
        block = site.block

        block.instructions = block.instructions[:cut_index] + [result]
        block.terminator = TerminatorJump(target=continuation.address)

        for successor in list(block.successors):
            if successor in block.successors:
                block.successors.remove(successor)
            if block in successor.predecessors:
                successor.predecessors.remove(block)

        block.successors.append(continuation)
        if block not in continuation.predecessors:
            continuation.predecessors.append(block)

    # ------------------------------------------------------------------
    # Machinery removal
    # ------------------------------------------------------------------

    def _prune_unreachable(self, entry_block: BasicBlock) -> None:
        """
        Keep only what's reachable from `entry_block`, plus anything
        reachable from there via a surviving exception handler.

        Forward-enumerating every kind of block the dispatch machine
        contains - the resume-point comparison chain, each arm's
        `.throw()`/`.return()` preamble, *and* their landing pads, *and*
        the reentrancy/exhausted guards ahead of all of it, which turned
        out to have their own nested action-dispatch - doesn't generalize:
        each new shape found by reading actual output was one this
        decompiler hadn't been told about yet. Reachability sidesteps the
        enumeration problem entirely: once every suspend site's `Ret` is
        rewired to jump straight to its resume block (see `_apply_fold`),
        anything the dispatch machine used to route through and that nothing
        else refers to is - by construction - no longer reachable, whatever
        shape it happens to have.

        The fixed point over exception handlers matters for the same
        reason `_prune_exception_handlers` exists: a `try_blocks` entry
        that survives (still has at least one reachable block after this
        prune) keeps its handler reachable too, and that handler's own
        body can reach blocks nothing else does.
        """
        self.cfg.entry = entry_block

        handlers = self.cfg.exception_handlers
        reachable: set[int] = set()
        frontier = [entry_block]

        while frontier:
            new_frontier: list[BasicBlock] = []

            for block in frontier:
                if block.id in reachable:
                    continue
                reachable.add(block.id)
                new_frontier.extend(block.successors)

            for handler in handlers:
                handler_block = handler["handler_block"]

                if handler_block.id in reachable:
                    continue

                if any(b.id in reachable for b in handler["try_blocks"]):
                    new_frontier.append(handler_block)

            frontier = new_frontier

        self.cfg.blocks = [block for block in self.cfg.blocks if block.id in reachable]

        for block in self.cfg.blocks:
            block.predecessors = [p for p in block.predecessors if p.id in reachable]
            block.successors = [s for s in block.successors if s.id in reachable]

        self._prune_exception_handlers(reachable)

    def _prune_exception_handlers(self, reachable: set[int]) -> None:
        """
        Drop pruned blocks from every `try_blocks` list.

        `cfg.exception_handlers` is captured once at CFG-construction time
        (see `CFGBuilder._resolve_exception_handlers`) as literal
        `BasicBlock` references, independent of `cfg.blocks` - pruning a
        block from the latter does nothing to the former on its own.
        """
        surviving: list[dict] = []

        for handler in self.cfg.exception_handlers:
            try_blocks = [block for block in handler["try_blocks"] if block.id in reachable]

            if not try_blocks or handler["handler_block"].id not in reachable:
                continue

            surviving.append({**handler, "try_blocks": try_blocks})

        self.cfg.exception_handlers = surviving
