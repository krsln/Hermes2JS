from __future__ import annotations

from hermes_decompiler.backend.analysis.cfg import BasicBlock, CFG
from hermes_decompiler.backend.regions import FinallyRegion, SequenceRegion, TryRegion
from hermes_decompiler.core.logging import get_logger
from hermes_decompiler.ir.expressions import Identifier
from hermes_decompiler.ir.terminators import TerminatorReturn, TerminatorThrow
from ._predicates import strip_duplicate_run, strip_duplicate_span, structural_key

logger = get_logger(__name__)


class _FinallyAttacher:
    """
    Commits a recognized `finally` shaped handler into the region tree.

    Handles the two shapes Hermes compiles a try/finally into:

    - `attach`: the two-handler case (a real catch exists alongside
      it) - `_finally_matcher.find_finally_wrapper_target` already
      identified the wider handler as this try/catch's
      finally-wrapper; this installs it.
    - `maybe_reinterpret_as_finally`: the single-handler case (no
      catch in the source at all) - `_HandlerBuilder` had no choice
      but to build an ordinary catch out of the lone handler; this
      recognizes after the fact that it's really a `finally` and
      rewrites it in place.

    Two shapes this class must additionally handle, beyond a single
    straight-line handler block, both stemming from the fact that
    IfStructurer already runs BEFORE TryStructurer in the pipeline:

    1. The finally-wrapper handler's OWN body may already have been
       folded by IfStructurer into an `IfRegion` sibling immediately
       after `handler_block`, with a trailing rethrow block after
       that - i.e. the handler's true content spans THREE siblings
       (condition block, IfRegion, rethrow block), not one. See
       `_finally_extent`.

    2. Once the finally body is known (see #1), the code it duplicates
       inline (at the try's own normal completion, and/or the catch's)
       may ALSO have been folded into an IfRegion by IfStructurer -
       `strip_duplicate_run` alone (a flat run of instruction values
       within one block) can never recognize that as a duplicate. See
       `strip_duplicate_span` in `_predicates.py`.

    A third, orthogonal issue this class handles: once a duplicate is
    found and stripped from inside `try_body`/`catch_region.body`,
    whatever code originally followed that duplicate IN THE SAME BLOCK
    is - by construction of how Hermes inlines `finally` - code that
    belongs AFTER the whole `try/catch/finally`, not part of the
    try/catch clause the block was captured as part of.
    `_HandlerBuilder` has no way to know this boundary in advance
    (nothing in the raw CFG marks it; Hermes only splits blocks at
    real jump targets, and this boundary isn't one - see
    `tryCatchTest`/section_15075, where catch's entire normal
    completion - "catch-block" print, duplicate finally content,
    "end" print, implicit return - is ONE physical block with no
    internal split at all). See `_extract_tail`/`_insert_tail_after`.
    """

    def __init__(self, graph):
        self.graph = graph

    def attach(self, handler: dict, try_region: TryRegion, inner_handler: dict, cfg: CFG) -> None:

        finally_block: BasicBlock = handler["handler_block"]

        finally_items = self._extract_finally_items(finally_block, cfg)

        self._strip_leading_catch_binding(finally_items)
        self._strip_trailing_rethrow(finally_items)
        finally_items = self._drop_empty_edge_blocks(finally_items)

        catch_region = try_region.catch

        if any(not isinstance(item, BasicBlock) for item in finally_items):
            # The finally body itself branches (see class docstring
            # point #1/#2) - dedupe at the region-tree level. No tail
            # relocation attempted here: every branching-finally
            # fixture found so far already has its shared
            # continuation correctly positioned as an ordinary
            # sibling by `_HandlerBuilder` (nothing to relocate), and
            # generalizing tail-splitting to a span containing a
            # nested IfRegion isn't a shape any current fixture
            # exercises - safer to leave it unhandled than guess.
            strip_duplicate_span(try_region.try_body, finally_items)
            if catch_region is not None:
                strip_duplicate_span(catch_region.body, finally_items)
        else:
            finally_values = [
                instr.value
                for item in finally_items
                for instr in item.instructions
                if instr.value is not None
            ]

            # Each call independently finds-and-strips its own match
            # (or is a safe no-op if that region has none) - calling
            # both unconditionally, rather than short-circuiting after
            # the first hit, matters when BOTH the try's own normal
            # completion AND the catch's own normal completion inline
            # a duplicate copy (each needs its duplicate stripped
            # either way; only one resulting tail actually gets
            # relocated below, since both would represent the same
            # shared continuation).
            tail_from_catch = (
                self._extract_tail(catch_region.body, finally_values, cfg)
                if catch_region is not None
                else None
            )
            tail_from_try = self._extract_tail(try_region.try_body, finally_values, cfg)

            tail = tail_from_catch or tail_from_try

            if tail:
                self._insert_tail_after(try_region, tail)

        # Hermes may also place the duplicated finally sequence in the shared
        # continuation point following the normal completion of the inner
        # try/catch (its immediate post-dominator). This is the same copy that
        # allows `find_finally_wrapper_target` to identify the enclosing
        # finally wrapper.
        #
        # The continuation block is not part of `try_body` or `catch.body`;
        # it remains a sibling of the TryRegion in the region tree. It must
        # therefore be cleaned up separately to prevent the ``finally`` body from
        # being emitted twice.
        if cfg is not None and cfg.post_dominator_tree is not None:
            merge_block = cfg.post_dominator_tree.immediate_post_dominator(
                inner_handler["handler_block"]
            )
            if merge_block is not None:
                owner = self.graph.owner(merge_block)
                if owner is not None:
                    if any(not isinstance(item, BasicBlock) for item in finally_items):
                        strip_duplicate_span(owner, finally_items)
                    else:
                        finally_values = [
                            instr.value
                            for item in finally_items
                            for instr in item.instructions
                            if instr.value is not None
                        ]
                        strip_duplicate_run(owner, finally_values)

        finally_body = SequenceRegion()
        self.graph.transfer(finally_items, finally_body)

        finally_region = FinallyRegion()
        finally_region.body = finally_body
        finally_body.parent = finally_region

        try_region.finally_ = finally_region

    # -----------------------------------------------------------------
    # Multi-sibling extraction of the finally-wrapper handler's own body
    # -----------------------------------------------------------------

    def _extract_finally_items(self, finally_block: BasicBlock, cfg: CFG) -> list:
        """Pull the finally-wrapper handler's full body out of wherever
        it currently sits in the region tree - `finally_block` itself
        plus, if IfStructurer already folded the handler's own
        branching into a sibling IfRegion (see class docstring #1),
        that IfRegion and the trailing rethrow block after it.
        """
        owner = self.graph.owner(finally_block)

        if owner is None or finally_block not in owner.children:
            # Shouldn't normally happen at this pipeline stage - fall
            # back to the historical single-block behavior rather
            # than crashing.
            self.graph.extract_block(finally_block)
            return [finally_block]

        start_idx = owner.children.index(finally_block)

        merge_block = None
        if cfg is not None and cfg.post_dominator_tree is not None:
            merge_block = cfg.post_dominator_tree.immediate_post_dominator(finally_block)

        end_idx = self._finally_extent(owner, start_idx, merge_block)

        return self.graph.splice_out(owner, start_idx, end_idx)

    @staticmethod
    def _finally_extent(owner: SequenceRegion, start_idx: int, merge_block) -> int:
        """Returns the exclusive end index of the finally-wrapper
        handler's own content within `owner`, starting at `start_idx`.

        `merge_block` (the immediate post-dominator of `handler_block`)
        is where every branch inside the handler's own content
        reconverges - that's also exactly where the handler's trailing
        rethrow lives (Hermes always closes a finally-wrapper handler
        with a bare rethrow of the exception it caught). Walking
        forward through `owner`'s children and stopping at (inclusive
        of) the sibling that covers `merge_block` therefore captures
        the whole handler body - condition block, any folded IfRegion,
        and the trailing rethrow - in one span, regardless of how many
        pieces IfStructurer split it into.

        Falls back to `start_idx + 1` (the historical single-block
        span) if `merge_block` can't be found as a sibling within
        `owner` at or after `start_idx` - a shape this method doesn't
        recognize, better handled by the old assumption than by
        over-extending the span into unrelated code.
        """
        if merge_block is None:
            return start_idx + 1

        for index in range(start_idx, len(owner.children)):
            item = owner.children[index]

            if item is merge_block:
                return index + 1

            if not isinstance(item, BasicBlock) and merge_block in item.covered_blocks:
                return index + 1

        return start_idx + 1

    # -----------------------------------------------------------------
    # Leading Catch-binding / trailing rethrow stripping
    # -----------------------------------------------------------------

    @staticmethod
    def _strip_leading_catch_binding(items: list) -> None:
        """Drop the leading Catch binding - finally has no bound
        exception parameter. Only ever the very first instruction of
        the very first item (the handler's own entry block), regardless
        of how many siblings the rest of the body now spans.
        """
        leading = items[0] if items and isinstance(items[0], BasicBlock) else None

        if leading is None or not leading.instructions:
            return

        first = leading.instructions[0]

        if first.dest_reg is not None and isinstance(first.value, Identifier):
            leading.instructions.pop(0)

    @staticmethod
    def _strip_trailing_rethrow(items: list) -> None:
        """Drop the trailing rethrow - real JS finally semantics already
        guarantee the original exception propagates once the finally
        body finishes, so an explicit throw here would be redundant.
        Only strip it when it's provably a plain rethrow (the thrown
        value is a bare identifier), to avoid discarding a throw with
        real side effects. Now potentially on the LAST item's own
        block rather than necessarily the same block the leading
        Catch-binding was stripped from, since the handler's own
        content may span multiple siblings (see `_finally_extent`).
        """
        trailing = items[-1] if items and isinstance(items[-1], BasicBlock) else None

        if trailing is None:
            return

        terminator = trailing.terminator

        if isinstance(terminator, TerminatorThrow) and isinstance(terminator.value, Identifier):
            last = trailing.instructions[-1] if trailing.instructions else None
            if last is not None and last.terminator is terminator:
                trailing.instructions.pop()
            trailing.terminator = None

    @staticmethod
    def _drop_empty_edge_blocks(items: list) -> list:
        """After stripping the leading Catch-binding / trailing
        rethrow, the first and/or last item may now be a completely
        empty BasicBlock (no instructions, no terminator) that was
        only ever scaffolding. Printing it would be a no-op at best;
        dropping it also keeps `finally_values`/`strip_duplicate_span`
        matching against only genuinely meaningful content.
        """

        def is_empty(item) -> bool:
            return (
                    isinstance(item, BasicBlock)
                    and not item.instructions
                    and item.terminator is None
            )

        result = list(items)

        if result and is_empty(result[0]):
            result.pop(0)

        if result and is_empty(result[-1]):
            result.pop()

        return result

    # -----------------------------------------------------------------
    # Tail relocation (see class docstring, point 3)
    # -----------------------------------------------------------------

    def _extract_tail(self, region: SequenceRegion, finally_values: list, cfg: CFG):
        """Find-and-strip EVERY run in `region.covered_blocks` matching
        `finally_values` (same matching, and same "one match per
        block, scan every block" contract, as `strip_duplicate_run` -
        Hermes may duplicate the same finally sequence independently
        across multiple exit paths, e.g. a loop's own break/continue/
        normal-completion branches, each needing its own copy
        stripped, regardless of nesting depth).

        Additionally, for the (at most one) match found DIRECTLY in
        `region` itself (i.e. `graph.owner(block) is region`, not some
        block nested inside further loop/conditional structure within
        `region`) - the "shared normal completion" copy - also splits
        off and returns whatever content followed that run, in the
        same block and in any later DIRECT siblings of `region`, as a
        list of region-tree items ready to be spliced in elsewhere.

        A match nested deeper is stripped exactly as `strip_duplicate_run`
        alone would leave it, with nothing relocated: relocating code
        out from under a branch/loop it's still conditionally scoped
        to would change what actually executes.

        Returns None if no top-level match was found, or if nothing
        followed it (the common, already-correctly-handled case) -
        regardless of how many nested matches were stripped.
        """
        if not finally_values:
            return None

        from hermes_decompiler.backend.transforms.shared import structural_key

        finally_keys = [structural_key(v) for v in finally_values]
        n = len(finally_keys)

        tail = None

        for block in list(region.covered_blocks):

            candidates = [i for i in block.instructions if i.value is not None]
            candidate_keys = [structural_key(c.value) for c in candidates]

            for start in range(len(candidates) - n + 1):

                if candidate_keys[start:start + n] != finally_keys:
                    continue

                matched = candidates[start:start + n]

                # Capture whatever ORIGINALLY followed the matched run
                # BEFORE removing anything - `block.instructions.remove`
                # below only removes the matched instructions
                # themselves, by identity, leaving everything else
                # (both before AND after the match) untouched in place.
                # Without this, `_split_off_tail` would treat the
                # genuine catch/try content that came BEFORE the match
                # (e.g. "catch-block", the caught error) as part of the
                # tail too, incorrectly relocating it out of the
                # try/catch entirely.
                last_matched_pos = block.instructions.index(matched[-1])
                after_match = block.instructions[last_matched_pos + 1:]

                for instr in matched:
                    block.instructions.remove(instr)

                is_top_level = tail is None and self.graph.owner(block) is region

                if is_top_level:
                    for instr in after_match:
                        block.instructions.remove(instr)
                    tail = self._split_off_tail(block, region, cfg, after_match)

                # Whether or not this was the top-level match, keep
                # scanning the REMAINING blocks - see docstring.
                break

        return tail

    def _split_off_tail(self, block: BasicBlock, region: SequenceRegion, cfg: CFG, after_match: list):

        tail_items = []

        has_own_tail = bool(after_match) or block.terminator is not None

        if has_own_tail:
            new_id = max((b.id for b in cfg.blocks), default=0) + 1 if cfg is not None else id(block)

            tail_block = BasicBlock(new_id, address=block.address)
            tail_block.instructions = after_match
            tail_block.terminator = block.terminator
            tail_block.successors = list(block.successors)

            block.terminator = None
            block.successors = []

            if cfg is not None:
                # See `_HandlerBuilder._split_leading_unprotected_content`'s
                # matching comment: any code allocating a new block id
                # this way must register it on `cfg.blocks` too, or a
                # later allocation (in either file) can collide with it.
                cfg.blocks.append(tail_block)

            tail_items.append(tail_block)

        idx = region.children.index(block)
        following = self.graph.splice_out(region, idx + 1, len(region.children))
        tail_items.extend(following)

        return tail_items or None

    def _insert_tail_after(self, try_region: TryRegion, tail_items: list) -> None:

        parent = try_region.parent

        if not isinstance(parent, SequenceRegion):
            # Shouldn't happen post-`_HandlerBuilder` - don't silently
            # corrupt the tree if it ever does.
            logger.warning(
                "_FinallyAttacher: TryRegion has no SequenceRegion "
                "parent; leaving relocated tail undropped."
            )
            return

        insert_idx = parent.children.index(try_region) + 1

        for offset, item in enumerate(tail_items):
            self.graph.insert_at(parent, insert_idx + offset, item)

    # -----------------------------------------------------------------

    # -----------------------------------------------------------------
    # Evidence for `maybe_reinterpret_as_finally`
    # -----------------------------------------------------------------

    @staticmethod
    def _count_duplicate_blocks(region: SequenceRegion, values: list) -> int:
        """Number of blocks in `region` that contain `values` as a
        contiguous run - the exact matching (`structural_key`, one match
        per block, every covered block scanned) `_extract_tail` and
        `strip_duplicate_run` use to strip a copy, so a non-zero count
        here means the strip that follows will really remove something.

        Read-only. Zero for an empty `values`: there is nothing to match.
        A copy that lives in the block AFTER the try body is not counted
        here - see `_find_trailing_copy`.
        """
        if not values:
            return 0

        keys = [structural_key(v) for v in values]
        n = len(keys)
        count = 0

        for block in region.covered_blocks:
            block_keys = [
                structural_key(i.value) for i in block.instructions if i.value is not None
            ]

            if any(block_keys[s:s + n] == keys for s in range(len(block_keys) - n + 1)):
                count += 1

        return count

    @staticmethod
    def _has_normal_exit(region: SequenceRegion) -> bool:
        """True if some path through `region` leaves it without throwing:
        a `return`, or any CFG edge to a block outside the region
        (fall-through past the end, `break`, `continue`, a jump to code
        after the try). Hermes inlines a `finally` copy on each of those.
        """
        covered = region.covered_blocks

        return any(
            isinstance(block.terminator, TerminatorReturn)
            or any(successor not in covered for successor in block.successors)
            for block in covered
        )

    def _find_trailing_copy(self, try_region: TryRegion, values: list) -> BasicBlock | None:
        """The block right after the try that carries the inlined `finally`
        copy for EVERY normal exit, or None.

        When a try body's exits converge - a loop's `break` and the loop's
        own end both jump to the code after the loop - Hermes emits the
        `finally` body once, at the start of that shared block, instead of
        once per exit inside the try. Returning that block means:

        - all exits leave the try through this ONE block (so stripping the
          copy from it strips it from every exit), and
        - nothing outside the try body can reach it (a block that some
          other path also enters must keep its first statements: they are
          not the `finally`'s), and
        - it is the try's next sibling, so after `finally` runs, control
          falls into it exactly as the jumps did, and
        - it begins with the handler's body (`_starts_with_run`).

        Deliberately narrow: a try body containing a `return` is declined,
        because each `return` carries its own inlined copy inside the try
        and this does not model those; so is any exit set other than one
        block. Declining leaves the faithful `catch` + rethrow in place,
        never a `finally` with a copy still running next to it.
        """
        if not values:
            return None

        covered = try_region.try_body.covered_blocks

        if any(isinstance(block.terminator, TerminatorReturn) for block in covered):
            return None

        exits = {
            successor
            for block in covered
            for successor in block.successors
            if successor not in covered
        }

        if len(exits) != 1:
            return None

        (block,) = exits

        if any(predecessor not in covered for predecessor in block.predecessors):
            return None

        parent = try_region.parent

        if not isinstance(parent, SequenceRegion):
            return None

        try_index = parent.children.index(try_region)

        if try_index + 1 >= len(parent.children) or parent.children[try_index + 1] is not block:
            return None

        return block if self._starts_with_run(block, values) else None

    @staticmethod
    def _starts_with_run(block: BasicBlock, values: list) -> bool:
        keys = [structural_key(v) for v in values]
        n = len(keys)

        block_keys = [
            structural_key(i.value) for i in block.instructions if i.value is not None
        ]

        return n > 0 and block_keys[:n] == keys

    @staticmethod
    def _strip_leading_run(block: BasicBlock, values: list) -> None:
        """Remove the first `len(values)` value-bearing instructions of
        `block` (which `_starts_with_run` established are the copy).
        Removes by identity: instruction equality must not be allowed to
        pick a look-alike elsewhere in the block.
        """
        doomed = {
            id(instr)
            for instr in [i for i in block.instructions if i.value is not None][:len(values)]
        }

        block.instructions[:] = [i for i in block.instructions if id(i) not in doomed]

    def maybe_reinterpret_as_finally(self, try_region: TryRegion, cfg: CFG | None = None) -> None:
        """Reinterpret a lone catch as finally when it's really one.

        Handles the single-handler `try { } finally { }` case (no
        catch at all in the source): with nothing to pair against,
        `_HandlerBuilder` has no choice but to build an ordinary catch
        region out of it. If that "catch" body's last statement is a
        bare rethrow of its own bound exception - and there's at least
        one other statement before it (an empty `catch (e) { throw e; }`
        is a legitimate, if pointless, source and shouldn't be rewritten)
        - It's a candidate for a `finally` that had nowhere to attach to.

        That SHAPE alone cannot tell the two sources apart:

            try { A } catch (e) { B; throw e; }      // B runs only on throw
            try { A } finally  { B }                 // B runs on every exit

        compile to the same handler table and the same handler block. What
        differs is the try body: Hermes inlines a copy of a `finally` body
        at every NORMAL exit of the try (fall-through, `return`, `break`,
        `continue`), whereas a catch that rethrows leaves no copy anywhere.
        Rewriting the former as `finally` and the latter as `finally` too
        would run B on the success path of code that never asked for it
        (see Metro's loadModuleImplementation: a `catch` that marks the
        module as failed, rewritten into a `finally` that marks EVERY
        module as failed).

        So the rewrite is committed only with evidence, decided BEFORE
        anything is mutated:

        - a copy of the handler's body exists in the try body and can be
          stripped (the rewrite is then exactly what the source said), or
        - the try body has no normal exit at all (every path throws), where
          `catch { B; throw e }` and `finally { B }` are equivalent anyway,
          or
        - every normal exit leads to ONE block right after the try that
          starts with a copy of the handler's body, and nothing else can
          reach that block (see `_find_trailing_copy` - a loop's `break`
          and its normal end both jump to the same code after the try, so
          Hermes puts the single inlined copy there, not inside the try).

        Otherwise the region is left as the faithful `try/catch` + rethrow
        `_HandlerBuilder` already built. That is what the bytecode does, at
        the cost of not recovering a `finally` whose inlined copy this pass
        cannot see (e.g. a copy under different register names - see
        `_count_duplicate_blocks`).

        Only handles a single straight-line block for now; a `finally`
        body with its own branching needs the fuller multi-block
        treatment `attach` performs for the two-handler case.
        """

        catch_region = try_region.catch

        if catch_region is None:
            return

        body = catch_region.body

        if len(body.children) != 1:
            return

        block = body.children[0]

        if not isinstance(block, BasicBlock):
            return

        if not isinstance(block.terminator, TerminatorThrow):
            return

        if not isinstance(block.terminator.value, Identifier):
            return

        # `Throw`'s own value is deliberately kept as a bare `r{N}`
        # reference now (never inlined - see Throw.py's own
        # docstring), so it can no longer be expected to already read
        # as the catch parameter's friendly display name
        # (`catch_region.exception`). Compare by raw register number
        # instead, when available; only fall back to the friendly-name
        # comparison for a `handler_block` whose leading instruction
        # didn't yield one (see `_extract_catch_param`'s own `None`
        # case), keeping this working for that narrower shape too.
        thrown_name = block.terminator.value.name

        if catch_region.exception_reg is not None:
            if thrown_name != f"r{catch_region.exception_reg}":
                return
        elif thrown_name != catch_region.exception:
            return

        if len(block.instructions) < 2:
            return

        # Evidence gate - see the docstring. Must run before the first
        # mutation below (popping the rethrow, clearing the terminator).
        handler_values = [
            instr.value
            for instr in block.instructions
            if instr.value is not None and instr.terminator is not block.terminator
        ]

        trailing_copy = None

        if (
                self._count_duplicate_blocks(try_region.try_body, handler_values) == 0
                and self._has_normal_exit(try_region.try_body)
        ):
            trailing_copy = self._find_trailing_copy(try_region, handler_values)

            if trailing_copy is None:
                return

        # Only pop the trailing instruction once confirmed to be the
        # actual carrier of the throw terminator (see `attach` for why);
        # the terminator itself is always cleared, since the rethrow is
        # redundant under real finally semantics either way.
        if block.instructions[-1].terminator is block.terminator:
            block.instructions.pop()
        block.terminator = None

        # Same reasoning as `attach`: Hermes also duplicates the
        # `finally` code inline at the try body's own normal-completion
        # exit, not just at the handler. Missing this step leaves the
        # cleanup code printed - and actually running - twice.
        finally_values = [
            instr.value
            for instr in block.instructions
            if instr.value is not None
        ]

        # See class docstring point 3: whatever followed the duplicate
        # inside try_body's own normal-completion block belongs AFTER
        # the whole try/finally, not inside it. `_extract_tail` does
        # its own find-and-strip internally (same matching as
        # `strip_duplicate_run`) - calling `strip_duplicate_run`
        # separately first would consume the match before
        # `_extract_tail` ever got to look for it.
        tail = self._extract_tail(try_region.try_body, finally_values, cfg)

        if trailing_copy is not None:
            self._strip_leading_run(trailing_copy, finally_values)

        try_region.catch = None

        finally_region = FinallyRegion()
        finally_region.body = body
        body.parent = finally_region

        try_region.finally_ = finally_region

        if tail:
            self._insert_tail_after(try_region, tail)
