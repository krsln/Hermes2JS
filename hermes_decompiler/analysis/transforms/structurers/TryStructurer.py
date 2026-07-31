from __future__ import annotations

import dataclasses

from hermes_decompiler.analysis.cfg import BasicBlock
from hermes_decompiler.analysis.regions.Regions import SequenceRegion, TryRegion, CatchRegion, FinallyRegion
from hermes_decompiler.analysis.terminators import TerminatorReturn, TerminatorThrow
from hermes_decompiler.ir.expressions import Expression, Identifier
from hermes_decompiler.analysis.transforms.structurers._base import RegionStructurer

TERMINATING_TERMINATORS = (TerminatorReturn, TerminatorThrow)


class TryStructurer(RegionStructurer):

    def run(self):

        # Some functions list two handlers with the *identical*
        # [start, end) range but different targets (seen e.g. in
        # tryCatchFinallyImplicitThrowTest's `[start=0x19,end=0x3f,
        # target=0x55]` / `[start=0x19,end=0x3f,target=0x87]` pair).
        # Exception tables are matched in listed order, so for any
        # exception raised inside that identical range the *first*
        # entry always wins - the second is permanently shadowed and
        # never actually fires at runtime. Structuring it anyway
        # produces a phantom empty wrapper once its target block gets
        # legitimately claimed elsewhere (see the finally-wrapper for
        # the real, first handler). Drop shadowed duplicates before
        # doing anything else.
        seen_ranges = set()
        handlers = []

        for handler in self.cfg.exception_handlers:
            key = (handler["start"], handler["end"])

            if key in seen_ranges:
                continue

            seen_ranges.add(key)
            handlers.append(handler)

        # Process narrower-scoped handlers before the wider ones that
        # wrap them, so `_structure_handler`'s splicing always finds
        # its inner region already built. Sorting by raw range size
        # (end - start) breaks down when a wrapper's `start` sits later
        # than the handler it wraps (its `end` alone can then make it
        # look "smaller"). Sorting by `end` ascending is safe
        # regardless: a finally-wrapper protects through the end of
        # the catch it wraps, so its `end` is always >= the wrapped
        # handler's `end` - that ordering constraint holds no matter
        # where either handler's `start` falls.
        handlers = sorted(
            handlers,
            key=lambda h: h["end"],
        )

        # Hermes has no bytecode-level `finally` construct: a
        # try/catch/finally is lowered as TWO overlapping exception
        # handlers sharing the same `start` - a narrow one covering just
        # the try (real `catch`), and a wider one covering try+catch
        # together, whose target is a block that re-runs the cleanup
        # code and rethrows. We must recognize the wider handler as a
        # `finally` wrapper for the region the narrower handler already
        # built, rather than structuring it as a second, nested
        # try/catch - see `_find_finally_wrapper_target`.
        processed: list[tuple[dict, TryRegion]] = []

        for handler in handlers:

            wrapped = self._find_finally_wrapper_target(handler, processed)

            if wrapped is not None:
                _, try_region = wrapped
                self._attach_finally(handler, try_region)
                continue

            try_region = self._structure_handler(handler)

            if try_region is not None:
                processed.append((handler, try_region))

        # A plain `try { } finally { }` (no `catch` at all) compiles to
        # a SINGLE handler, since there's no separate narrower handler
        # to pair it with - it never goes through `_attach_finally`
        # above. Structurally that lone handler is indistinguishable
        # from an ordinary catch until we look at its *content*: it
        # both runs cleanup code AND unconditionally rethrows the very
        # exception it just caught. Reinterpret those as `finally`
        # after the fact, once every handler has been resolved.
        for _, try_region in processed:
            if try_region.finally_ is None:
                self._maybe_reinterpret_as_finally(try_region)

    # -------------------------------------------------------------

    def _find_finally_wrapper_target(self, handler: dict, processed: list):
        """
        Returns the (handler, try_region) pair that `handler` is a
        finally-wrapper for, or None if `handler` looks like an
        ordinary (non-finally) handler.

        `handler` wraps `inner` when its range swallows `inner`'s own
        catch-entry target (i.e. `handler` is reached whenever either
        the try *or* the catch of `inner` throws) AND `handler`'s own
        body content is a duplicate of code that already appears
        inside `inner`'s try/catch bodies - the tell-tale sign Hermes
        left behind from inlining the finally code at every normal
        exit point. The content check matters because the two
        handlers' `start` addresses aren't always byte-identical (the
        wider one can start a few instructions earlier or later
        depending on what setup code precedes the try), so range
        containment alone is too strict AND, on its own, too easy to
        satisfy by coincidence for genuinely unrelated nested handlers.
        """

        for inner_handler, inner_region in processed:

            if inner_handler["target"] == handler["target"]:
                continue

            if not (handler["start"] <= inner_handler["target"] < handler["end"]):
                continue

            if self._finally_content_matches(handler, inner_region):
                return inner_handler, inner_region

        return None

    # -------------------------------------------------------------

    def _finally_content_matches(self, handler: dict, inner_region: TryRegion) -> bool:

        values = self._candidate_finally_values(handler["handler_block"])

        if not values:
            return False

        keys = [self._structural_key(v) for v in values]
        n = len(keys)

        regions = [inner_region.try_body]

        catch_region = inner_region.catch

        if catch_region is not None:
            regions.append(catch_region.body)

        for region in regions:

            for block in region.covered_blocks:

                candidates = [i for i in block.instructions if i.value is not None]
                candidate_keys = [self._structural_key(c.value) for c in candidates]

                for start in range(len(candidate_keys) - n + 1):
                    if candidate_keys[start:start + n] == keys:
                        return True

        return False

    # -------------------------------------------------------------

    @staticmethod
    def _candidate_finally_values(handler_block: BasicBlock) -> list:
        """
        The value-bearing instructions of `handler_block` that would
        actually constitute a `finally` body: the leading `Catch`
        exception-binding and a trailing bare rethrow (if present)
        excluded, since neither has any JS-visible surface inside a
        real `finally` clause. Read-only - callers that intend to
        commit to treating the block as a finally must still perform
        the actual mutation themselves (see `_attach_finally`).
        """

        instructions = list(handler_block.instructions)

        if (
                instructions
                and instructions[0].dest_reg is not None
                and isinstance(instructions[0].value, Identifier)
        ):
            instructions = instructions[1:]

        if (
                instructions
                and isinstance(handler_block.terminator, TerminatorThrow)
                and isinstance(handler_block.terminator.value, Identifier)
        ):
            instructions = instructions[:-1]

        return [i.value for i in instructions if i.value is not None]

    # -------------------------------------------------------------

    def _maybe_reinterpret_as_finally(self, try_region: TryRegion) -> None:
        """
        Handles the single-handler `try { } finally { }` case (no
        `catch` at all in the source): with nothing to pair against,
        `_structure_handler` has no choice but to build an ordinary
        `catch` region out of it. If that "catch" body's last
        statement is a bare rethrow of its own bound exception - and
        there's at least one other statement before it (an empty
        `catch (e) { throw e; }` is legitimate, if pointless, source
        and shouldn't be rewritten) - it's really a `finally` that had
        nowhere to attach to. Only handles a single straight-line
        block for now; a finally body containing its own branching
        needs the fuller multi-block treatment `_attach_finally`
        performs for the two-handler case.
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

        if block.terminator.value.name != catch_region.exception:
            return

        if len(block.instructions) < 2:
            return

        block.instructions.pop()
        block.terminator = None

        # Same reasoning as _attach_finally: Hermes also duplicates the
        # finally code inline at the try body's own normal-completion
        # exit, not just at the handler. Missing this step leaves the
        # cleanup code printed - and actually running - twice.
        finally_values = [
            instr.value
            for instr in block.instructions
            if instr.value is not None
        ]

        self._strip_duplicate_run(try_region.try_body, finally_values)

        try_region.catch = None

        finally_region = FinallyRegion()
        finally_region.body = body
        body.parent = finally_region

        try_region.finally_ = finally_region

    # -------------------------------------------------------------

    def _attach_finally(self, handler: dict, try_region: TryRegion):

        finally_block = handler["handler_block"]

        # Pull the block out of wherever it currently sits in the
        # region tree (it hasn't been touched yet - still a bare
        # top-level BasicBlock sibling of `try_region`).
        self.graph.extract_block(finally_block)

        # Drop the leading `Catch` binding - `finally` has no bound
        # exception parameter.
        if finally_block.instructions:
            first = finally_block.instructions[0]

            if (
                    first.dest_reg is not None
                    and isinstance(first.value, Identifier)
            ):
                finally_block.instructions.pop(0)

        # Drop the trailing rethrow - real JS `finally` semantics
        # already guarantee the original exception propagates once the
        # finally body finishes, so an explicit `throw` here would be
        # redundant. Only strip it when it's provably a plain rethrow
        # (the thrown value is a bare identifier), to avoid silently
        # discarding a throw with real side effects.
        last = finally_block.instructions[-1] if finally_block.instructions else None

        if (
                last is not None
                and isinstance(finally_block.terminator, TerminatorThrow)
                and isinstance(finally_block.terminator.value, Identifier)
        ):
            finally_block.instructions.pop()
            finally_block.terminator = None

        # Hermes duplicates the finally code inline at every normal
        # exit point too (e.g. right before the catch's own `return`),
        # since it has no true finally construct. Now that we're
        # emitting a real `finally` clause, those inline copies must be
        # removed or the cleanup code would run twice at runtime.
        # Expression trees are register-free (registers only exist
        # while resolving values, not in the final AST), so `==`
        # reliably identifies the duplicated statements regardless of
        # which scratch registers each copy happened to use.
        finally_values = [
            instr.value
            for instr in finally_block.instructions
            if instr.value is not None
        ]

        self._strip_duplicate_run(try_region.try_body, finally_values)

        catch_region = try_region.catch

        if catch_region is not None:
            self._strip_duplicate_run(catch_region.body, finally_values)

        finally_body = SequenceRegion()
        self.graph.transfer([finally_block], finally_body)

        finally_region = FinallyRegion()
        finally_region.body = finally_body
        finally_body.parent = finally_region

        try_region.finally_ = finally_region

    # -------------------------------------------------------------

    @staticmethod
    def _structural_key(value):
        """
        Value-based key for an expression node, independent of whether
        its class defines `__eq__` (many of the IR expression classes
        don't, so plain `==` silently falls back to object identity and
        never matches two separately-built-but-equivalent trees). Deeply
        unpacks dataclasses into tuples so structurally identical trees
        - regardless of which registers produced them - compare equal.
        Falls back to `repr()` for anything that isn't a dataclass.
        """

        if dataclasses.is_dataclass(value) and not isinstance(value, type):
            return tuple(
                TryStructurer._structural_key(getattr(value, f.name))
                for f in dataclasses.fields(value)
            )

        if isinstance(value, (list, tuple)):
            return tuple(TryStructurer._structural_key(v) for v in value)

        try:
            hash(value)
            return value
        except TypeError:
            return repr(value)

    @staticmethod
    def _strip_duplicate_run(region: SequenceRegion, finally_values: list) -> None:
        """
        Removes the first contiguous run of instructions in `region`
        whose `.value`s exactly match `finally_values`, if any. The
        duplicate isn't necessarily at the very end of a block - e.g.
        a catch body normally continues with more statements (and a
        `return`) after its inlined finally-copy - so this scans for
        the run anywhere, not just as a trailing slice.
        """

        if not finally_values:
            return

        finally_keys = [TryStructurer._structural_key(v) for v in finally_values]
        n = len(finally_keys)

        for block in list(region.covered_blocks):

            candidates = [i for i in block.instructions if i.value is not None]

            candidate_keys = [TryStructurer._structural_key(c.value) for c in candidates]

            for start in range(len(candidates) - n + 1):

                if candidate_keys[start:start + n] != finally_keys:
                    continue

                for instr in candidates[start:start + n]:
                    block.instructions.remove(instr)

                break

    # -------------------------------------------------------------

    def _structure_handler(self, handler: dict) -> TryRegion | None:

        try_blocks = handler["try_blocks"]
        handler_block = handler["handler_block"]

        start_block = try_blocks[0]

        lca = self.graph.lowest_common_sequence(
            start_block,
            handler_block,
        )

        if lca is None:
            return None

        lca_seq, start_repr, handler_repr = lca

        if (
                start_repr not in lca_seq.children
                or handler_repr not in lca_seq.children
        ):
            return None

        start_idx = lca_seq.children.index(start_repr)
        handler_idx = lca_seq.children.index(handler_repr)

        if handler_idx <= start_idx:
            return None

        end_repr = self.graph.find_covering_item(
            lca_seq,
            try_blocks[-1],
        )

        if end_repr is None:
            return None

        if end_repr not in lca_seq.children:
            return None

        end_idx = lca_seq.children.index(end_repr)

        if not (start_idx <= end_idx < handler_idx):
            return None

        merge_block = None

        if self.cfg.post_dominator_tree is not None:
            merge_block = (
                self.cfg.post_dominator_tree
                .immediate_post_dominator(handler_block)
            )

        stop_at = {merge_block} if merge_block else set()

        catch_end = self._find_catch_boundary(
            lca_seq,
            handler_idx,
            stop_at,
        )

        items = self.graph.splice_out(
            lca_seq,
            start_idx,
            catch_end,
        )

        split = handler_idx - start_idx

        try_items = items[:split]
        catch_items = items[split:]

        try_body = SequenceRegion()
        self.graph.transfer(
            try_items,
            try_body,
        )

        catch_body = SequenceRegion()
        self.graph.transfer(
            catch_items,
            catch_body,
        )

        catch_region = CatchRegion()
        catch_region.exception = self._extract_catch_param(handler_block)
        catch_region.body = catch_body
        catch_body.parent = catch_region

        try_region = TryRegion()
        try_region.try_body = try_body
        try_body.parent = try_region

        try_region.catch = catch_region
        catch_region.parent = try_region

        self.graph.insert_at(
            lca_seq,
            start_idx,
            try_region,
        )

        return try_region

    # -------------------------------------------------------------

    @classmethod
    def _extract_catch_param(cls, handler_block: BasicBlock) -> str:

        if not handler_block.instructions:
            return "e"

        first = handler_block.instructions[0]

        name = (
            first.value.name
            if isinstance(first.value, Identifier)
            else "e"
        )

        if (
                first.dest_reg is not None
                and isinstance(first.value, Expression)
        ):
            handler_block.instructions.pop(0)

        return name

    # -------------------------------------------------------------

    @classmethod
    def _find_catch_boundary(cls, region: SequenceRegion, start: int, stop_at: set) -> int:

        index = start

        while index < len(region.children):

            item = region.children[index]

            if item in stop_at:
                return index

            if isinstance(item, BasicBlock) and isinstance(item.terminator, TERMINATING_TERMINATORS):
                return index + 1

            index += 1

        return index
