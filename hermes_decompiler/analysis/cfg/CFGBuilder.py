from __future__ import annotations

from typing import Dict, List, Set

from hermes_decompiler.analysis.cfg.BasicBlock import BasicBlock
from hermes_decompiler.analysis.cfg.CFG import CFG
from hermes_decompiler.analysis.models.Terminator import (
    TerminatorConditionalBranch,
    TerminatorJump,
    TerminatorSwitch,
    TerminatorReturn,
    TerminatorThrow,
)
from hermes_decompiler.core.logging import get_logger
from hermes_decompiler.frontend.opcode import OpcodeResult

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
        self.results: List[OpcodeResult] = []

        self.cfg = CFG()

        self.address_to_index: Dict[int, int] = {}

        self.address_to_block: Dict[int, BasicBlock] = {}

    def build(
            self,
            results: List[OpcodeResult],
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
        block_end: Dict[int, float] = {}

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
        split into contiguous fragments, rather than one [start, end)
        entry covering the whole protected region.

        This happens whenever the try body's own linear instruction
        stream is interrupted by a jump - most commonly the success
        path's unconditional `Jmp` skipping over a conditional `throw`
        (see e.g. tryCatchInsideLoopTest: `if (items[i] < 0) throw ...`
        followed by `console.log(...)`, where the success path jumps
        past the throw-construction code straight to the loop
        increment). Hermes records this as two separate table entries -
        [start1, end1) for the code before the Jmp, [start2, end2) for
        the code after it - both targeting the same catch/finally
        block, with a small gap between end1 and start2 covering only
        the (unprotected, can't-itself-throw) Jmp instruction.

        Left unmerged, `TryStructurer` processes each fragment as an
        independent handler. By the time the second one is built, its
        `handler_block` has already been spliced into the TryRegion the
        first one built, and structuring it as a second, separate
        try/catch against an already-relocated target block produces
        scrambled output (catch content ordered before the try body,
        orphaned/dead tail code, stray gotos).

        Two entries are merged when they target the same handler block,
        are adjacent or overlapping in address order, and nothing else
        in the exception table has a start or end address strictly
        inside the gap between them - i.e. nothing else considers that
        gap a boundary of its own. That last condition is what keeps
        this from merging two genuinely distinct protected regions that
        simply happen to share a handler.
        """
        if not raw_handlers:
            return raw_handlers

        ordered = sorted(raw_handlers, key=lambda h: (h["start"], h["end"]))

        boundaries = {h["start"] for h in ordered} | {h["end"] for h in ordered}

        merged: list[dict] = [dict(ordered[0])]

        for handler in ordered[1:]:
            last = merged[-1]

            gap_is_clear = not any(
                last["end"] < addr < handler["start"]
                for addr in boundaries
            )

            if (
                    handler["target"] == last["target"]
                    and handler["start"] >= last["end"]
                    and gap_is_clear
            ):
                last["end"] = max(last["end"], handler["end"])
                continue

            merged.append(dict(handler))

        return merged

    def _find_leaders(self) -> set[int]:

        leaders: set[int] = set()

        if not self.results:
            return leaders

        leaders.add(self.results[0].address)

        for i, result in enumerate(self.results):
            terminator = result.terminator

            if terminator is None:
                continue

            leaders.update(terminator.targets)

            if terminator.targets and i + 1 < len(self.results):
                leaders.add(self.results[i + 1].address)

        return leaders

    def _create_basic_blocks(self, leaders: Set[int]) -> None:

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
