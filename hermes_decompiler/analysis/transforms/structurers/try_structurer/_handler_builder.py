from __future__ import annotations

from hermes_decompiler.analysis.cfg import BasicBlock
from hermes_decompiler.analysis.models import TerminatorReturn, TerminatorThrow
from hermes_decompiler.analysis.models.regions import CatchRegion, SequenceRegion, TryRegion
from hermes_decompiler.ir.expressions import Expression, Identifier

TERMINATING_TERMINATORS = (TerminatorReturn, TerminatorThrow)


class _HandlerBuilder:
    """Builds the base TryRegion/CatchRegion shape from a raw handler.

    Splits the covering sequence into a try body and a catch body via
    the try/handler blocks' lowest common sequence ancestor.

    Purely structural: only decides where the try/catch boundaries
    fall and splices the tree accordingly. Has no concept of finally -
    a handler this builder structures may later be recognized as a
    finally-wrapper (`_finally_matcher`) or reinterpreted as one after
    the fact (`_finally_attacher`), both of which run afterward, in
    `TryStructurer.run`.
    """

    def __init__(self, graph, cfg):
        self.graph = graph
        self.cfg = cfg

    def build(self, handler: dict) -> TryRegion | None:

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

        stop_at = {merge_block} if merge_block is not None else set()

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

    @staticmethod
    def _extract_catch_param(handler_block: BasicBlock) -> str:

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

    @staticmethod
    def _find_catch_boundary(region: SequenceRegion, start: int, stop_at: set) -> int:

        index = start

        while index < len(region.children):

            item = region.children[index]

            if item in stop_at:
                return index

            if (
                    isinstance(item, BasicBlock)
                    and isinstance(item.terminator, TERMINATING_TERMINATORS)
            ):
                return index + 1

            index += 1

        return index
