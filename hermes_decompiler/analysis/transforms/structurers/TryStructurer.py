from __future__ import annotations

from hermes_decompiler.analysis.cfg import BasicBlock
from hermes_decompiler.analysis.regions.RegionGraph import RegionGraph
from hermes_decompiler.analysis.regions.Regions import (
    SequenceRegion,
    LoopRegion,
    IfRegion,
    TryRegion,
    CatchRegion,
)
from hermes_decompiler.ir.expressions import Expression, Identifier
from hermes_decompiler.opcode import ControlFlowType

TERMINATING_CONTROL_FLOW = {ControlFlowType.RETURN, ControlFlowType.THROW}


class TryStructurer:
    """
    Converts a resolved `cfg.exception_handlers` entry (try-range +
    catch target, already mapped to real BasicBlocks by
    `CFGBuilder._resolve_exception_handlers`) into a real `TryRegion`.

    Must run AFTER `LoopStructurer`/`IfStructurer`: Hermes exception
    ranges routinely cover only a *sub-slice* of a loop's body (e.g.
    everything except the loop header/back-edge instructions), while
    the handler sits structurally *after the whole loop*. Once
    Loop/If have run, the try-range's raw blocks end up nested one or
    more levels deep inside a `LoopRegion`/`IfRegion`, while the
    handler block remains a sibling of that *outer* region - they are
    no longer flat siblings in the same `SequenceRegion`.

    To handle this, we don't look for `start_block`/`handler_block` as
    direct list members of one shared sequence. Instead we compute the
    full root-to-leaf *path* (list of `(owning SequenceRegion, item)`
    pairs) for every block, find the deepest `SequenceRegion` common
    to both the try-range's blocks and the handler block (their
    "lowest common ancestor" sequence), and use each side's
    ancestor-or-self *item at that level* (which may be the raw block
    itself, or a `LoopRegion`/`IfRegion` that now contains it) as the
    thing to actually splice into `TryRegion.try_body` /
    `CatchRegion.body`.

    This subsumes the simple case too: when try-range and handler
    really are flat siblings (no intervening loop/if), the LCA
    sequence is just their shared owner and the "representative" is
    the block itself - identical to the original simpler
    implementation.

    Does NOT attempt to handle:
        - `finally` blocks (Hermes typically compiles `finally` as a
          duplicated/inlined cleanup path per exit, not a single
          block Hermes tags for us)
        - nested try/catch with overlapping ranges
        - a try-range whose blocks resolve to two *different*
          representative items that themselves aren't contiguous
          siblings at the LCA level (bails out rather than guessing)

    Must run before `StatementBuilder` (needs BasicBlocks intact).
    """

    def __init__(self, graph: RegionGraph, cfg):
        self.graph = graph
        self.cfg = cfg
        self._paths: dict[BasicBlock, list[tuple[SequenceRegion, object]]] = {}

    def run(self):
        for handler in self.cfg.exception_handlers:
            # Rebuilt per-handler: structuring one handler mutates the
            # tree (splices try/catch out), which would invalidate a
            # path cache built before that mutation for any handler
            # processed afterward.
            self._paths = self._build_paths(self.graph.root)
            self._structure_handler(handler)

    # ------------------------------------------------------------------
    # Path indexing / LCA
    # ------------------------------------------------------------------

    def _build_paths(self, root) -> dict:
        paths: dict[BasicBlock, list[tuple[SequenceRegion, object]]] = {}

        def walk(region, path):

            if isinstance(region, SequenceRegion):
                for item in region.children:
                    new_path = path + [(region, item)]
                    if isinstance(item, BasicBlock):
                        paths[item] = new_path
                    else:
                        walk(item, new_path)
                return

            if isinstance(region, LoopRegion):
                walk(region.body, path)
                return

            if isinstance(region, IfRegion):
                walk(region.then_body, path)
                if region.else_body:
                    walk(region.else_body, path)
                return

            if isinstance(region, TryRegion):
                walk(region.try_body, path)
                if region.catch:
                    walk(region.catch.body, path)
                if region.finally_:
                    walk(region.finally_.body, path)
                return

            if hasattr(region, "body"):
                walk(region.body, path)

        walk(root, [])
        return paths

    def _representative_in(self, block: BasicBlock, sequence: SequenceRegion):
        """The ancestor-or-self item of `block` that sits directly in
        `sequence.children`, or None if `block`'s path never passes
        through `sequence`."""

        path = self._paths.get(block)

        if path is None:
            return None

        for seq, item in path:
            if seq is sequence:
                return item

        return None

    def _find_lca(self, block_a: BasicBlock, block_b: BasicBlock):
        """Deepest SequenceRegion common to both blocks' paths, plus
        each block's representative item at that level."""

        path_a = self._paths.get(block_a)
        path_b = self._paths.get(block_b)

        if not path_a or not path_b:
            return None

        seqs_b = {seq: item for seq, item in path_b}

        for seq, item in reversed(path_a):
            if seq in seqs_b:
                return seq, item, seqs_b[seq]

        return None

    # ------------------------------------------------------------------

    def _structure_handler(self, handler: dict):

        try_blocks = handler["try_blocks"]
        handler_block = handler["handler_block"]

        start_block = try_blocks[0]
        end_block = try_blocks[-1]

        lca = self._find_lca(start_block, handler_block)

        if lca is None:
            return

        lca_seq, start_repr, handler_repr = lca

        if not isinstance(lca_seq, SequenceRegion):
            return

        if start_repr not in lca_seq.children or handler_repr not in lca_seq.children:
            return

        start_idx = lca_seq.children.index(start_repr)
        handler_idx = lca_seq.children.index(handler_repr)

        if handler_idx <= start_idx:
            return

        # Sanity check: the try range's LAST block must resolve to a
        # representative that also sits within [start_idx, handler_idx)
        # at this same LCA level - otherwise the try range spans
        # something more exotic than "one contiguous representative
        # slice", and guessing would risk mis-scoping the try body.
        end_repr = self._representative_in(end_block, lca_seq)

        if end_repr is None or end_repr not in lca_seq.children:
            return

        end_idx = lca_seq.children.index(end_repr)

        if not (start_idx <= end_idx < handler_idx):
            return

        # -------------------------------------------------------------
        # try body = everything from the try-range's representative up
        # to (not including) the handler's representative, at the LCA
        # level.
        # -------------------------------------------------------------

        try_items = lca_seq.children[start_idx:handler_idx]

        # -------------------------------------------------------------
        # catch body = handler onward, up to the merge point, or the
        # first terminating (return/throw) block if there's no merge
        # point (e.g. a handler that unconditionally rethrows).
        # -------------------------------------------------------------

        merge_block = None
        if self.cfg.post_dominator_tree is not None:
            merge_block = self.cfg.post_dominator_tree.immediate_post_dominator(handler_block)

        stop_at = {merge_block} if merge_block is not None else set()
        catch_end = self._find_catch_boundary(lca_seq, handler_idx, stop_at)

        catch_items = lca_seq.children[handler_idx:catch_end]

        # -------------------------------------------------------------
        # Splice both ranges out of the LCA sequence in one shot.
        # -------------------------------------------------------------

        del lca_seq.children[start_idx:catch_end]

        try_body = SequenceRegion()
        self.graph.transfer(try_items, try_body)

        catch_param = self._extract_catch_param(handler_block)

        catch_body = SequenceRegion()
        self.graph.transfer(catch_items, catch_body)

        catch_region = CatchRegion()
        catch_region.exception = catch_param
        catch_region.body = catch_body

        try_region = TryRegion()
        try_region.try_body = try_body
        try_region.catch = catch_region

        lca_seq.children.insert(start_idx, try_region)
        try_region.parent = lca_seq
        catch_region.parent = try_region

    # ------------------------------------------------------------------

    def _extract_catch_param(self, handler_block: BasicBlock) -> str:

        if not handler_block.instructions:
            return "e"

        first = handler_block.instructions[0]

        if isinstance(first.value, Identifier):
            name = first.value.name
        else:
            name = "e"

        if first.dest_reg is not None and isinstance(first.value, Expression):
            handler_block.instructions.pop(0)

        return name

    def _find_catch_boundary(self, region: SequenceRegion, start: int, stop_at: set) -> int:
        """
        Stops at the first item in `stop_at`, or right after a block
        that terminates control flow (return/throw) - a rethrowing
        handler has no legitimate "continue past me" sibling; anything
        after it in the same sequence belongs to an unrelated path
        (e.g. the function's normal-exit return) and must not be
        swallowed into the catch body.
        """

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