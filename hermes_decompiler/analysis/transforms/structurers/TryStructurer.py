from __future__ import annotations

from hermes_decompiler.analysis.cfg import BasicBlock
from hermes_decompiler.analysis.regions.Regions import SequenceRegion, TryRegion, CatchRegion
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

        for handler in handlers:
            self._structure_handler(handler)

    # -------------------------------------------------------------

    def _structure_handler(self, handler: dict):

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
