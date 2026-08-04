from __future__ import annotations

from typing import Dict, List, Set

from hermes_decompiler.core.logging import get_logger
from hermes_decompiler.frontend.opcode import OpcodeResult
from .BasicBlock import BasicBlock
from .CFG import CFG
from ..terminators import (
    TerminatorConditionalBranch, TerminatorJump, TerminatorSwitch, TerminatorReturn, TerminatorThrow
)

logger = get_logger(__name__)


class CFGBuilder:
    """
    Builds a Control Flow Graph from OpcodeResults.

    Phase-2

        - Detect leaders
        - Split into basic blocks
        - Connect successor / predecessor edges

    Not yet supported

        - Exception edges
        - Switch extra_gotos
        - Try/Catch
    """

    def __init__(self):
        self.results: List[OpcodeResult] = []

        self.cfg = CFG()

        self.address_to_index: Dict[int, int] = {}

        self.address_to_block: Dict[int, BasicBlock] = {}

    # -------------------------------------------------------------

    def build(self, results: List[OpcodeResult], exception_handlers: list[dict] | None = None) -> CFG:

        self.results = results
        exception_handlers = exception_handlers or []

        self.address_to_index = {
            r.opcode.address: i
            for i, r in enumerate(results)
        }

        leaders = self._find_leaders()

        # Exception handler targets (catch-block entry points) must be
        # block boundaries too, even though they're never the destination
        # of a normal Jmp/JCompare - they're reached only via the VM's
        # implicit exception-dispatch mechanism, which `result.goto`
        # doesn't model at all. Without this, a target address landing
        # mid-block (as Hermes routinely produces) leaves no BasicBlock
        # starting exactly there, so `_resolve_exception_handlers` can
        # never find a `handler_block` for it and silently drops the
        # handler - see CFGBuilder's DROPPED debug trail.
        for handler in exception_handlers:
            leaders.add(handler["target"])

        self._create_basic_blocks(leaders)

        self._connect_edges()

        self.cfg.exception_handlers = self._resolve_exception_handlers(exception_handlers)

        return self.cfg

    # -------------------------------------------------------------

    def _resolve_exception_handlers(self, raw_handlers: list[dict]) -> list[dict]:

        resolved = []

        sorted_blocks = sorted(self.cfg.blocks, key=lambda b: b.address)

        # End address of each block = start address of the next block in
        # program order (or +inf for the last block). Needed because a
        # handler's "start" address routinely falls *inside* a block
        # rather than exactly on a leader/block boundary (Hermes marks
        # the protected range at instruction granularity, not block
        # granularity) - so membership must be decided by range overlap,
        # not by testing whether the block's own start address falls
        # inside [handler.start, handler.end).
        block_end: Dict[int, float] = {}
        for i, block in enumerate(sorted_blocks):
            block_end[block.address] = (
                sorted_blocks[i + 1].address
                if i + 1 < len(sorted_blocks)
                else float("inf")
            )

        for handler in raw_handlers:

            try_blocks = [
                block for block in sorted_blocks
                if block.address < handler["end"] and block_end[block.address] > handler["start"]
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

    # -------------------------------------------------------------

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

    # -------------------------------------------------------------

    def _create_basic_blocks(self, leaders: Set[int]) -> None:

        current_block = None
        block_id = 0

        for result in self.results:

            address = result.address

            if address in leaders:

                current_block = BasicBlock(block_id, address)

                self.cfg.blocks.append(current_block)

                if self.cfg.entry is None:
                    self.cfg.entry = current_block

                self.address_to_block[address] = current_block

                block_id += 1

            # NOTE (fix): terminator-bearing results (Ret, Throw, Jmp,
            # JCompare, SwitchImm) used to be routed *only* into
            # `block.terminator` and excluded from `block.instructions`,
            # which meant Printer/StatementBuilder - which only ever
            # walk `block.instructions` - could never render them. Any
            # terminator the structurers didn't explicitly consume
            # (only ConditionalBranch is folded into if/while
            # conditions) was silently dropped: `Return`/`Throw` are
            # *never* consumed by a structurer, so every `return`/
            # `throw` in the program was being lost. Terminator-bearing
            # results are now always added to `instructions` too, so
            # they always get a chance to render (via `result.statement`
            # - see Ret.py/Throw.py) or at minimum keep their verbose
            # `// CODE ->` trace line; `block.terminator` below is still
            # populated for the structurers' own CFG-level analysis.
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
                        # Hermes 98 is not stable, so just warning not raise error for now
                        # raise RuntimeError(f"Block {current_block.id} already has a terminator.")
                # else:
                current_block.add_instruction(result)

    # -------------------------------------------------------------

    def _connect_edges(self):

        for index, block in enumerate(self.cfg.blocks):

            terminator = block.terminator

            match terminator:

                #
                # conditional branch
                #
                case TerminatorConditionalBranch(_, target):

                    self._connect(block, self.address_to_block[target])

                    if index + 1 < len(self.cfg.blocks):
                        self._connect(block, self.cfg.blocks[index + 1])

                #
                # unconditional jump
                #
                case TerminatorJump(target):

                    self._connect(block, self.address_to_block[target])

                #
                # switch
                #
                case TerminatorSwitch(_, case_map, default_target):
                    targets = set(case_map.values())
                    targets.add(default_target)

                    for target in targets:
                        self._connect(block, self.address_to_block[target])

                #
                # return
                #
                case TerminatorReturn():

                    pass

                #
                # throw
                #
                case TerminatorThrow():

                    pass

                #
                # ordinary block
                #
                case None:

                    if index + 1 < len(self.cfg.blocks):
                        self._connect(block, self.cfg.blocks[index + 1])

    # -------------------------------------------------------------

    @classmethod
    def _connect(cls, source: BasicBlock, target: BasicBlock) -> None:

        if target not in source.successors:
            source.successors.append(target)

        if source not in target.predecessors:
            target.predecessors.append(source)
