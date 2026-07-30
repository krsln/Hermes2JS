from __future__ import annotations

from hermes_decompiler.analysis.cfg import BasicBlock
from hermes_decompiler.analysis.regions.Regions import SequenceRegion, TryRegion, CatchRegion, FinallyRegion
from hermes_decompiler.analysis.terminators import TerminatorReturn, TerminatorThrow
from hermes_decompiler.ir.expressions import Expression, Identifier
from hermes_decompiler.analysis.transforms.structurers._base import RegionStructurer

TERMINATING_TERMINATORS = (TerminatorReturn, TerminatorThrow)


class TryStructurer(RegionStructurer):

    def run(self):

        handlers = sorted(
            self.cfg.exception_handlers,
            key=lambda h: h["end"] - h["start"],
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

    # -------------------------------------------------------------

    @classmethod
    def _find_finally_wrapper_target(cls, handler: dict, processed: list):
        """
        Returns the (handler, try_region) pair that `handler` is a
        finally-wrapper for, or None if `handler` looks like an
        ordinary (non-finally) handler.

        `handler` wraps `inner` when they protect the same starting
        instruction and `handler`'s range also swallows `inner`'s own
        catch-entry target - i.e. `handler` is reached whenever either
        the try *or* the catch of `inner` throws.
        """

        for inner_handler, inner_region in processed:

            if inner_handler["target"] == handler["target"]:
                continue

            if inner_handler["start"] != handler["start"]:
                continue

            if handler["start"] <= inner_handler["target"] < handler["end"]:
                return inner_handler, inner_region

        return None

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

        if try_region.catch is not None:
            self._strip_duplicate_run(try_region.catch.body, finally_values)

        finally_body = SequenceRegion()
        self.graph.transfer([finally_block], finally_body)

        finally_region = FinallyRegion()
        finally_region.body = finally_body
        finally_body.parent = finally_region

        try_region.finally_ = finally_region

    # -------------------------------------------------------------

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

        n = len(finally_values)

        for block in list(region.covered_blocks):

            candidates = [i for i in block.instructions if i.value is not None]

            for start in range(len(candidates) - n + 1):

                window = candidates[start:start + n]

                if [c.value for c in window] != finally_values:
                    continue

                for instr in window:
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
            return

        lca_seq, start_repr, handler_repr = lca

        if (
                start_repr not in lca_seq.children
                or handler_repr not in lca_seq.children
        ):
            return

        start_idx = lca_seq.children.index(start_repr)
        handler_idx = lca_seq.children.index(handler_repr)

        if handler_idx <= start_idx:
            return

        end_repr = self.graph.find_covering_item(
            lca_seq,
            try_blocks[-1],
        )

        if end_repr is None:
            return

        if end_repr not in lca_seq.children:
            return

        end_idx = lca_seq.children.index(end_repr)

        if not (start_idx <= end_idx < handler_idx):
            return

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
