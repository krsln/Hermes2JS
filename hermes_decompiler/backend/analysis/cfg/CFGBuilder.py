from __future__ import annotations

from bisect import bisect_right

from hermes_decompiler.backend.analysis.cfg.BasicBlock import BasicBlock
from hermes_decompiler.backend.analysis.cfg.CFG import CFG
from hermes_decompiler.core.logging import get_logger
from hermes_decompiler.frontend.opcode import OpcodeResult
from hermes_decompiler.ir.terminators import (
    TerminatorConditionalBranch,
    TerminatorJump,
    TerminatorSwitch,
    TerminatorReturn,
    TerminatorThrow,
)

logger = get_logger(__name__)


class CFGBuilder:
    """
    Builds a Control Flow Graph from OpcodeResults.

    Phase 2:

        - Detect leaders
        - Split instructions into basic blocks
        - Connect successor and predecessor edges

    Not yet supported:

        - Exception edges
        - Switch extra gotos
        - Try/catch
    """

    def __init__(self):
        self.results: list[OpcodeResult] = []

        self.cfg = CFG()

        self.address_to_index: dict[int, int] = {}

        self.address_to_block: dict[int, BasicBlock] = {}

    def build(
            self,
            results: list[OpcodeResult],
            exception_handlers: list[dict] | None = None,
    ) -> CFG:

        self.results = results
        exception_handlers = exception_handlers or []

        self.address_to_index = {
            r.entry.address: i
            for i, r in enumerate(results)
        }

        leaders = self._find_leaders()

        # Exception handler targets must also be block boundaries.
        # They are reached through the VM's implicit exception dispatch,
        # which is not represented by `result.goto`.
        #
        # Hermes may place a handler target in the middle of an existing
        # block. Without adding the target as a leader, no BasicBlock
        # would start at that address and the handler could not be resolved.
        for handler in exception_handlers:
            leaders.add(handler["target"])

        self._create_basic_blocks(leaders)

        self._connect_edges()

        self.cfg.exception_handlers = self._resolve_exception_handlers(
            exception_handlers
        )

        return self.cfg

    def _resolve_exception_handlers(self, raw_handlers: list[dict]) -> list[dict]:

        raw_handlers = self._merge_fragmented_handlers(raw_handlers)

        resolved = []

        sorted_blocks = sorted(self.cfg.blocks, key=lambda b: b.address)

        # A block ends at the start of the next block in program order.
        # The last block extends to infinity. This allows protected ranges
        # to overlap blocks whose start address lies outside the range.
        block_end: dict[int, float] = {}

        for i, block in enumerate(sorted_blocks):
            block_end[block.address] = (
                sorted_blocks[i + 1].address
                if i + 1 < len(sorted_blocks)
                else float("inf")
            )

        for handler in raw_handlers:

            # Hermes records protected ranges at instruction granularity,
            # so a handler range may start or end inside a basic block.
            # Use range overlap rather than the block start address alone.
            try_blocks = [
                block
                for block in sorted_blocks
                if block.address < handler["end"]
                   and block_end[block.address] > handler["start"]
            ]

            handler_block = self.address_to_block.get(handler["target"])

            if not try_blocks or handler_block is None:
                continue

            resolved.append({
                "start": handler["start"],
                "end": handler["end"],
                "target": handler["target"],
                "try_blocks": try_blocks,
                "handler_block": handler_block,
            })

        return resolved

    @staticmethod
    def _merge_fragmented_handlers(raw_handlers: list[dict]) -> list[dict]:
        """Merge exception-handler ranges that are really one try body
        split into fragments, rather than one [start, end) entry covering
        the whole protected region.

        This happens whenever the try body's own linear instruction
        stream is interrupted by something the handler must not cover -
        most commonly the success path's unconditional `Jmp` skipping over
        a conditional `throw` (see e.g. tryCatchInsideLoopTest), a
        `continue` inside a for-of loop, or a generator/async suspend
        point (`SaveGenerator` + `Ret`, see asyncTryCatchTest). Hermes
        records this as several table entries, [start1, end1),
        [start2, end2), ... all targeting the same catch/finally block,
        with small gaps between them.

        Left unmerged, `TryStructurer` processes each fragment as an
        independent handler. By the time the second one is built, its
        `handler_block` has already been spliced into the TryRegion the
        first one built, and structuring it again against an
        already-relocated target block produces scrambled output (catch
        content ordered before the try body, orphaned/dead tail code,
        stray gotos).

        Two rules make the merge robust:

        1. Fragments are grouped by TARGET, never by their position in the
           sorted table. A wider handler with a different target (e.g. the
           finally-wrapper of a try/catch/finally, which has to cover the
           suspend/`Jmp` gap the catch fragments leave open) routinely
           sorts BETWEEN two fragments of the same catch; an
           adjacency-based merge would never see them as neighbours.

        2. A fragment is absorbed into the latest same-target range when it
           overlaps it, or when the gap between them is "clear": no entry
           in the table - of any target - starts or ends strictly inside
           the gap, and no other-target entry lies wholly inside it.
           Coverage by every other handler is then constant across the
           gap, i.e. nothing else considers it a boundary of its own.
           That is what keeps this from merging two genuinely distinct
           protected regions that merely share a handler (see
           nestedArrayDestructureTest, where nested handlers sit inside
           the gap and nothing is merged).

        Because rule 2 looks at the OTHER handlers' boundaries, and those
        handlers may themselves be fragmented (a fragmented catch inside a
        fragmented finally-wrapper, see parseBoxShadowString), one pass is
        not enough: the wrapper's own fragment edges would keep blocking
        the catch's merge. Passes therefore repeat, recomputing boundaries
        from the already-merged entries, until nothing more merges. Every
        pass strictly reduces the entry count or ends the loop.

        Deterministic: the result depends only on the SET of entries; ties
        in `(start, end)` keep table order (Hermes matches entries in
        listed order, so the first-listed of two identical ranges is the
        one that ever fires). The input list and its dicts are never
        mutated.
        """
        if not raw_handlers:
            return raw_handlers

        # (table_index, entry). The index only breaks (start, end) ties.
        entries = [(i, dict(h)) for i, h in enumerate(raw_handlers)]

        while True:
            merged = CFGBuilder._merge_pass(entries)
            if len(merged) == len(entries):
                return [entry for _, entry in merged]
            entries = merged

    @staticmethod
    def _merge_pass(entries: list[tuple[int, dict]]) -> list[tuple[int, dict]]:
        """One left-to-right merge pass. See `_merge_fragmented_handlers`."""
        ordered = sorted(entries, key=lambda t: (t[1]["start"], t[1]["end"], t[0]))
        all_handlers = [entry for _, entry in ordered]

        boundaries = sorted(
            {h["start"] for h in all_handlers} | {h["end"] for h in all_handlers}
        )

        merged: list[tuple[int, dict]] = []
        latest_by_target: dict[int, tuple[int, dict]] = {}

        for index, handler in ordered:
            slot = latest_by_target.get(handler["target"])

            if slot is not None and CFGBuilder._can_absorb(
                    slot[1], handler, all_handlers, boundaries
            ):
                slot[1]["end"] = max(slot[1]["end"], handler["end"])
                continue

            # A fresh copy: `handler["end"]` may still grow if a later
            # fragment is absorbed, and pass inputs must stay untouched.
            slot = (index, dict(handler))
            merged.append(slot)
            latest_by_target[handler["target"]] = slot

        return merged

    @staticmethod
    def _can_absorb(
            candidate: dict,
            handler: dict,
            all_handlers: list[dict],
            boundaries: list[int],
    ) -> bool:
        """True if `handler` (same target as `candidate`, and starting at or
        after `candidate["start"]`) is another fragment of `candidate`'s
        protected range. See `_merge_fragmented_handlers`.
        """
        gap_start, gap_end = candidate["end"], handler["start"]

        if gap_end <= gap_start:
            # Adjacent or overlapping: nothing between them to inspect.
            return True

        # Any table boundary strictly inside the gap?
        i = bisect_right(boundaries, gap_start)
        if i < len(boundaries) and boundaries[i] < gap_end:
            return False

        # A different handler occupying exactly the gap has both of its
        # boundaries ON the gap's edges, so the check above can't see it.
        return not any(
            other["target"] != handler["target"]
            and other["start"] >= gap_start
            and other["end"] <= gap_end
            for other in all_handlers
        )

    def _find_leaders(self) -> set[int]:

        leaders: set[int] = set()

        if not self.results:
            return leaders

        leaders.add(self.results[0].address)

        for i, result in enumerate(self.results):
            terminator = result.terminator

            if terminator is not None:
                leaders.update(terminator.targets)

                if terminator.targets and i + 1 < len(self.results):
                    leaders.add(self.results[i + 1].address)

            if result.handler == "Catch":
                # Always a fresh entry point, regardless of whether this
                # address happens to be a declared exception handler
                # target (see `build()`'s separate seeding of those) - a
                # `<Catch>` reached only through such an untracked address
                # would otherwise merge into whatever preceded it, and
                # since Throw/Return (unlike Jump/Branch/Switch) have no
                # `.targets` to force the split above, nothing else here
                # would catch that. Observed in real hbc98 output: two
                # consecutive Throw-then-Catch pairs at 0x201/0x203 where
                # only 0x20a (not 0x203) is a registered handler target.
                leaders.add(result.address)

        return leaders

    def _create_basic_blocks(self, leaders: set[int]) -> None:

        current_block = None
        block_id = 0

        for result in self.results:

            address = result.address

            # A single instruction may produce multiple OpcodeResults with
            # the same `entry.address` (for example, ResumeGenerator produces
            # a destination register result and a flag register result).
            #
            # Only the first result at a given address may start a block.
            # Otherwise, the second result would create another block at the
            # same address and overwrite `address_to_block[address]`.
            is_new_address = (
                    current_block is None
                    or current_block.address != address
            )

            if address in leaders and is_new_address:

                current_block = BasicBlock(block_id, address)

                self.cfg.blocks.append(current_block)

                if self.cfg.entry is None:
                    self.cfg.entry = current_block

                self.address_to_block[address] = current_block

                block_id += 1

            if current_block:

                if result.terminator:

                    if current_block.terminator is None:
                        current_block.terminator = result.terminator
                    else:
                        logger.warning(
                            "BasicBlock %d already has a terminator.\n"
                            "    Current terminator : %s\n"
                            "    New terminator     : %s\n"
                            "    Produced by opcode : %s",
                            current_block.id,
                            current_block.terminator,
                            result.terminator,
                            result.handler,
                        )

                        # Hermes 98 is not stable, so keep this as a warning
                        # instead of raising an error for now.
                        # raise RuntimeError(f"Block {current_block.id} already has a terminator.")

                current_block.add_instruction(result)

                # Populate register definitions during the same pass and in
                # program order. Only results with both a destination register
                # and a concrete value are considered register definitions.
                if result.dest_reg is not None and result.value is not None:
                    self.cfg.reg_definitions.setdefault(
                        result.dest_reg,
                        [],
                    ).append(
                        (result.address, current_block, result)
                    )

    def _connect_edges(self):

        for index, block in enumerate(self.cfg.blocks):

            terminator = block.terminator

            match terminator:

                #
                # Conditional branch
                #
                case TerminatorConditionalBranch(_, target):

                    self._connect(block, self.address_to_block[target])

                    if index + 1 < len(self.cfg.blocks):
                        self._connect(block, self.cfg.blocks[index + 1])

                #
                # Unconditional jump
                #
                case TerminatorJump(target):

                    self._connect(block, self.address_to_block[target])

                #
                # Switch
                #
                case TerminatorSwitch(_, case_map, default_target):

                    targets = set(case_map.values())
                    if default_target is not None:
                        targets.add(default_target)

                    for target in targets:
                        self._connect(block, self.address_to_block[target])

                #
                # Return
                #
                case TerminatorReturn():

                    pass

                #
                # Throw
                #
                case TerminatorThrow():

                    pass

                #
                # Ordinary block
                #
                case None:

                    if index + 1 < len(self.cfg.blocks):
                        self._connect(block, self.cfg.blocks[index + 1])

    @classmethod
    def _connect(cls, source: BasicBlock, target: BasicBlock) -> None:

        if target not in source.successors:
            source.successors.append(target)

        if source not in target.predecessors:
            target.predecessors.append(source)
