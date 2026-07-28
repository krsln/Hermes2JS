from __future__ import annotations

from hermes_decompiler.analysis.cfg import BasicBlock
from hermes_decompiler.analysis.regions.RegionGraph import RegionGraph
from hermes_decompiler.analysis.regions.Regions import (
    SequenceRegion,
    TryRegion,
    CatchRegion,
)
from hermes_decompiler.ir.expressions import Expression, Identifier
from hermes_decompiler.opcode import ControlFlowType

TERMINATING_CONTROL_FLOW = {ControlFlowType.RETURN, ControlFlowType.THROW}


class TryStructurer:

    def __init__(self, graph: RegionGraph, cfg):
        self.graph = graph
        self.cfg = cfg

    def run(self):

        handlers = sorted(
            self.cfg.exception_handlers,
            key=lambda h: h["end"] - h["start"],
        )

        for handler in handlers:
            self._structure_handler(handler)

    def _structure_handler(self, handler: dict):

        try_blocks = handler["try_blocks"]
        handler_block = handler["handler_block"]

        start_block = try_blocks[0]
        end_block = try_blocks[-1]

        lca = self.graph.lowest_common_sequence(start_block, handler_block)

        if lca is None:
            return

        lca_seq, start_repr, handler_repr = lca

        if start_repr not in lca_seq.children or handler_repr not in lca_seq.children:
            return

        start_idx = lca_seq.children.index(start_repr)
        handler_idx = lca_seq.children.index(handler_repr)

        if handler_idx <= start_idx:
            return

        # end_block must resolve to a representative within
        # [start_idx, handler_idx) at this same level - otherwise the
        # try range isn't one contiguous slice here and we bail.
        end_repr = self.graph.find_covering_item(lca_seq, end_block)

        if end_repr is None or end_repr not in lca_seq.children:
            return

        end_idx = lca_seq.children.index(end_repr)

        if not (start_idx <= end_idx < handler_idx):
            return

        try_items = lca_seq.children[start_idx:handler_idx]

        merge_block = None
        if self.cfg.post_dominator_tree is not None:
            merge_block = self.cfg.post_dominator_tree.immediate_post_dominator(handler_block)

        stop_at = {merge_block} if merge_block is not None else set()
        catch_end = self._find_catch_boundary(lca_seq, handler_idx, stop_at)

        catch_items = self.graph.splice_out(lca_seq, start_idx, catch_end)
        # splice_out already removed [start_idx:catch_end]; slice the
        # returned list back into try/catch halves by relative offset.
        try_items = catch_items[: handler_idx - start_idx]
        catch_items = catch_items[handler_idx - start_idx:]

        try_body = SequenceRegion()
        self.graph.transfer(try_items, try_body)

        catch_param = self._extract_catch_param(handler_block)

        catch_body = SequenceRegion()
        self.graph.transfer(catch_items, catch_body)

        catch_region = CatchRegion()
        catch_region.exception = catch_param
        catch_region.body = catch_body
        catch_body.parent = catch_region

        try_region = TryRegion()
        try_region.try_body = try_body
        try_body.parent = try_region
        try_region.catch = catch_region
        catch_region.parent = try_region

        self.graph.insert_at(lca_seq, start_idx, try_region)

    def _extract_catch_param(self, handler_block: BasicBlock) -> str:

        if not handler_block.instructions:
            return "e"

        first = handler_block.instructions[0]
        name = first.value.name if isinstance(first.value, Identifier) else "e"

        if first.dest_reg is not None and isinstance(first.value, Expression):
            handler_block.instructions.pop(0)

        return name

    def _find_catch_boundary(self, region: SequenceRegion, start: int, stop_at: set) -> int:

        index = start

        while index < len(region.children):

            item = region.children[index]

            if item in stop_at:
                return index

            if isinstance(item, BasicBlock) and item.instructions:
                last = item.instructions[-1]
                if last.control_flow in TERMINATING_CONTROL_FLOW:
                    return index + 1

            index += 1

        return index
