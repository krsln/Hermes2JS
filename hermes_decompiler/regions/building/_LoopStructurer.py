from __future__ import annotations

from hermes_decompiler.regions.model.LoopRegion import LoopKind, LoopRegion


class LoopStructurer:
    """
    Builds a LoopRegion for a recognized loop header.

    Takes the StructuralAnalyzer instance as a collaborator (rather
    than duplicating its traversal helpers) so loop bodies are
    structured with exactly the same if/try/nested-loop logic as
    everything else - a loop body is just a bounded region like any
    other, not a special case.

    Three patterns are attempted, in order of how "clean" the
    resulting JS reads:

      1. WHILE      - the loop header itself is the exit test (one
                       successor stays in the body, one leaves it).
                       This is what Hermes emits for `while (cond) {}`
                       and for-loops after their init/update are
                       inlined into the body.

      2. DO_WHILE    - the loop's latch (the block with the back-edge
                       to the header) carries the exit test instead.
                       Matches `do { } while (cond)`.

      3. INFINITE    - neither pattern matches cleanly (multiple exits,
                       header/latch aren't simple conditional blocks,
                       etc). Falls back to `while (true) { ... }`.
                       Exits found this way become BREAK markers when
                       the branch inside the body is structured (see
                       StructuralAnalyzer._branch_region) - this is the
                       "graceful degradation" path: the output is valid
                       JS, just not necessarily idiomatic, and is worth
                       diffing against a real disassembly to see if a
                       new pattern should be promoted to its own case.
    """

    def __init__(self, analyzer):
        self._a = analyzer

    def build(self, header_id: int) -> tuple[LoopRegion, int | None]:

        body = self._a.loops_by_header[header_id]
        header_block = self._a.cfg.get_block(header_id)

        while_result = self._try_while(header_id, header_block, body)
        if while_result is not None:
            return while_result

        do_while_result = self._try_do_while(header_id, body)
        if do_while_result is not None:
            return do_while_result

        return self._build_infinite(header_id, body)

    # ------------------------------------------------------------

    def _try_while(self, header_id, header_block, body):

        if not self._a.is_if_header(header_block):
            return None

        in_body = [e for e in header_block.outgoing if e.target in body]
        out_body = [e for e in header_block.outgoing if e.target not in body]

        if len(in_body) != 1 or len(out_body) != 1:
            return None

        condition = self._a.extract_condition(header_block)

        body_region, _ = self._a.structure_range(
            in_body[0].target,
            stop_id=header_id,
            bound=body,
        )

        region = LoopRegion(kind=LoopKind.WHILE, condition=condition, body=body_region)
        return region, out_body[0].target

    def _try_do_while(self, header_id, body):

        latch_id = self._find_conditional_latch(header_id, body)
        if latch_id is None:
            return None

        latch_block = self._a.cfg.get_block(latch_id)
        condition = self._a.extract_condition(latch_block)

        exit_edges = [e for e in latch_block.outgoing if e.target not in body]
        if len(exit_edges) != 1:
            return None

        # Structure the body starting at the header, but tell
        # structure_range to treat this specific visit to `header_id`
        # as a plain block instead of re-entering loop structuring -
        # otherwise we'd recurse into LoopStructurer.build(header_id)
        # again immediately and never terminate.
        body_region, _ = self._a.structure_range(
            header_id,
            stop_id=latch_id,
            bound=body,
            suppress_loop_header=header_id,
        )
        body_region.regions.append(self._a.block_region(latch_block))

        region = LoopRegion(kind=LoopKind.DO_WHILE, condition=condition, body=body_region)
        return region, exit_edges[0].target

    def _find_conditional_latch(self, header_id, body):
        """
        The latch is whichever block inside the loop body has an
        outgoing edge back to the header. Natural loops (as produced
        by LoopAnalysis) are back-edge-per-latch, so there can be more
        than one candidate for loops with multiple `continue`-style
        paths; we only treat this as a do-while if exactly one latch
        exists AND it looks like a two-way conditional block (i.e. one
        edge is the loop-back, the other genuinely exits the body).
        """

        candidates = []

        for block_id in body:

            if block_id == header_id:
                continue

            block = self._a.cfg.get_block(block_id)

            if block is None:
                continue

            targets = {e.target for e in block.outgoing}

            if header_id in targets and self._a.is_if_header(block):
                candidates.append(block_id)

        if len(candidates) == 1:
            return candidates[0]

        return None

    def _build_infinite(self, header_id, body):

        body_region, _ = self._a.structure_range(
            header_id,
            stop_id=None,
            bound=body,
            suppress_loop_header=header_id,
        )

        exit_targets = self._exit_targets(body)
        next_id = exit_targets[0] if exit_targets else None

        region = LoopRegion(kind=LoopKind.INFINITE, condition=None, body=body_region)
        return region, next_id

    def _exit_targets(self, body) -> list[int]:

        targets: list[int] = []

        for block_id in body:

            block = self._a.cfg.get_block(block_id)

            if block is None:
                continue

            for edge in block.outgoing:

                if edge.target not in body and edge.target not in targets:
                    targets.append(edge.target)

        return targets
