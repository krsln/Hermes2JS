from __future__ import annotations

from typing import Dict, List, Set

from hermes_decompiler.opcode import OpcodeResult, ControlFlowType
from .BasicBlock import BasicBlock
from .CFG import CFG

# Opcodes with no successor at all - the block simply exits the
# function (via return or exception), so no fallthrough edge should be
# added even though `goto` is None for them.
TERMINATING_CONTROL_FLOW = {
    ControlFlowType.RETURN,
    ControlFlowType.THROW,
}


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

        sorted_blocks = sorted(self.cfg.blocks, key=lambda b: b.first.opcode.address)

        for handler in raw_handlers:

            try_blocks = [
                block for block in sorted_blocks
                if handler["start"] <= block.first.opcode.address < handler["end"]
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

    def _find_leaders(self) -> Set[int]:

        leaders: Set[int] = set()

        if not self.results:
            return leaders

        leaders.add(self.results[0].opcode.address)

        for i, result in enumerate(self.results):

            if result.goto is not None:

                leaders.add(result.goto)

                if i + 1 < len(self.results):
                    leaders.add(self.results[i + 1].opcode.address)

        return leaders

    # -------------------------------------------------------------

    def _create_basic_blocks(self, leaders: Set[int]) -> None:

        current_block = None
        block_id = 0

        for result in self.results:

            address = result.opcode.address

            if address in leaders:

                current_block = BasicBlock(block_id)

                self.cfg.blocks.append(current_block)

                if self.cfg.entry is None:
                    self.cfg.entry = current_block

                self.address_to_block[address] = current_block

                block_id += 1

            current_block.add_instruction(result)

    # -------------------------------------------------------------

    def _connect_edges(self):

        for index, block in enumerate(self.cfg.blocks):

            last = block.instructions[-1]

            # --------------------------------------------------
            # unconditional jump
            # --------------------------------------------------

            if (
                    last.goto is not None
                    and self._is_unconditional_jump(last)
            ):

                target = self.address_to_block.get(last.goto)

                if target:
                    self._connect(block, target)

                continue

            # --------------------------------------------------
            # conditional jump
            # --------------------------------------------------

            if (
                    last.goto is not None
                    and self._is_conditional_jump(last)
            ):

                target = self.address_to_block.get(last.goto)

                if target:
                    self._connect(block, target)

                if index + 1 < len(self.cfg.blocks):
                    self._connect(block, self.cfg.blocks[index + 1])

                continue

            # --------------------------------------------------
            # return / throw (function exit - no successors)
            # --------------------------------------------------
            #
            # NOTE (fix): previously only checked `last.handler == "Ret"`
            # (a string), which left Throw-terminated blocks unhandled -
            # they fell through to the "fallthrough" branch below and
            # got an incorrect edge to whatever block happened to follow
            # in bytecode order, corrupting dominance/post-dominance
            # analysis for any function containing a `throw` that isn't
            # the very last instruction. Now driven by the real
            # `control_flow` enum every handler already sets.
            # --------------------------------------------------

            if last.control_flow in TERMINATING_CONTROL_FLOW:
                continue

            # --------------------------------------------------
            # fallthrough
            # --------------------------------------------------

            if index + 1 < len(self.cfg.blocks):
                self._connect(block, self.cfg.blocks[index + 1])

    # -------------------------------------------------------------

    def _connect(
            self,
            source: BasicBlock,
            target: BasicBlock,
    ) -> None:

        if target not in source.successors:
            source.successors.append(target)

        if source not in target.predecessors:
            target.predecessors.append(source)

    # -------------------------------------------------------------

    @staticmethod
    def _is_conditional_jump(result: OpcodeResult) -> bool:
        return result.control_flow == ControlFlowType.CONDITIONAL

    @staticmethod
    def _is_unconditional_jump(result: OpcodeResult) -> bool:
        return result.control_flow == ControlFlowType.UNCONDITIONAL
