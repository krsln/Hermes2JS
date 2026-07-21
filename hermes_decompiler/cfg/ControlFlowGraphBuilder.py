from collections import deque

from hermes_decompiler.cfg import CFGValidator
from hermes_decompiler.cfg.BasicBlock import BasicBlock
from hermes_decompiler.cfg.CFGEdge import CFGEdge
from hermes_decompiler.cfg.ControlFlowGraph import ControlFlowGraph
from hermes_decompiler.cfg.EdgeKind import EdgeKind
from hermes_decompiler.cfg.analysis.ExceptionAnalysis import ExceptionAnalysis
from hermes_decompiler.Logger import get_logger

logger = get_logger(__name__)


class ControlFlowGraphBuilder:
    """
    Build edges between BasicBlocks.
    """

    # Handlers whose `goto` edge represents "the condition, as already
    # polarity-baked into the emitted `if (...)` text, evaluated true".
    # See handlers/Jump/Jmp.py: JmpFalse.BuildCondition already wraps
    # the value in `!...`, so from the CFG's point of view every one of
    # these behaves identically - goto=TRUE_BRANCH, fallthrough=FALSE_BRANCH.
    _CONDITIONAL_HANDLERS = {
        "JmpTrue", "JmpTrueLong",
        "JmpFalse", "JmpFalseLong",
        "JmpUndefined", "JmpUndefinedLong",
        "JmpBuiltinIs", "JmpBuiltinIsLong",
        "JmpBuiltinIsNot", "JmpBuiltinIsNotLong",
        "JmpTypeOfIs",
    }

    @classmethod
    def build(cls, blocks: list[BasicBlock], metadata: dict | None = None) -> ControlFlowGraph:

        cfg = ControlFlowGraph.from_blocks(blocks)

        cls._connect(cfg)
        cls._connect_exceptions(cfg, metadata)
        cls._heal_unreachable(cfg)

        CFGValidator.validate(cfg)

        return cfg

    @classmethod
    def _connect(cls, cfg: ControlFlowGraph):

        ordered = sorted(
            cfg,
            key=lambda block: block.start_addr,
        )

        for index, block in enumerate(ordered):

            if not block.instructions:
                continue

            last = block.instructions[-1]
            conditional = last.handler in cls._CONDITIONAL_HANDLERS

            #
            # explicit jump
            #

            if last.goto is not None:

                target = cfg.get_block(last.goto)

                if target is not None:
                    cls._connect_edge(
                        block,
                        target,
                        EdgeKind.TRUE_BRANCH if conditional else EdgeKind.UNCONDITIONAL,
                    )

            #
            # extra jump targets (SwitchImm: one per case label)
            #

            for extra_target_addr in last.extra_gotos:

                target = cfg.get_block(extra_target_addr)

                if target is not None:
                    cls._connect_edge(block, target, EdgeKind.UNCONDITIONAL)

            #
            # fallthrough
            #

            if cls._falls_through(last):

                if index + 1 < len(ordered):
                    cls._connect_edge(
                        block,
                        ordered[index + 1],
                        EdgeKind.FALSE_BRANCH if conditional else EdgeKind.FALLTHROUGH,
                    )

    @classmethod
    def _connect_exceptions(cls, cfg: ControlFlowGraph, metadata: dict | None):
        """
        Wire try-range -> catch-handler edges from Hermes exception
        metadata.

        Without this, a catch handler that's only ever reached via an
        implicit exception dispatch (never a real jump/fallthrough
        target of any instruction) has zero incoming edges and is
        flagged as unreachable by CFGValidator - this is what caused
        the `ValueError: Unreachable BasicBlocks: <handler address>`
        crash on real .hbc input.

        Deliberately a single edge from the block CONTAINING the try
        range's start address to the handler block, not one edge per
        instruction inside the try range: that's enough to make the
        handler reachable and available to TryStructurer, without
        adding an EXCEPTION edge out of every single block in the try
        body (which would be the more semantically complete model, but
        would also inflate every block inside a try/catch to look like
        a 2-successor block to naive `len(block.outgoing)` checks
        elsewhere). Region-building code that inspects `block.outgoing`
        for structuring purposes filters `EdgeKind.EXCEPTION` out
        explicitly - see StructuralAnalyzer._control_flow_edges.
        """

        if not metadata:
            return

        for region in ExceptionAnalysis.build(metadata):

            try_block = cls._block_containing(cfg, region.start)
            handler_block = cfg.get_block(region.handler)

            if try_block is None:
                logger.warning(
                    "Exception region start=%s has no containing BasicBlock; skipping",
                    region.start,
                )
                continue

            if handler_block is None:
                logger.warning(
                    "Exception region handler=%s does not match any BasicBlock; skipping",
                    region.handler,
                )
                continue

            already_connected = any(
                edge.target == handler_block.id and edge.kind == EdgeKind.EXCEPTION
                for edge in try_block.outgoing
            )

            if not already_connected:
                cls._connect_edge(try_block, handler_block, EdgeKind.EXCEPTION)

    @staticmethod
    def _block_containing(cfg: ControlFlowGraph, address: int) -> BasicBlock | None:
        """
        Exception region boundaries are byte offsets from Hermes
        metadata, not guaranteed to land exactly on a BasicBlock leader
        address - find the block whose instruction range spans it.
        """

        for block in cfg:
            if block.start_addr <= address <= block.end_addr:
                return block

        return None

    @classmethod
    def _heal_unreachable(cls, cfg: ControlFlowGraph):
        """
        Safety net: after normal + exception-edge wiring, anything
        still unreachable from entry gets a synthetic edge from entry
        instead of crashing the whole conversion in CFGValidator.

        This is intentionally loud (logger.warning per block) rather
        than silent - a healed block signals a jump/target pattern
        this builder doesn't understand yet (a candidate: generator
        resume points from SaveGenerator/ResumeGenerator, not yet
        audited the way Jmp.py and SwitchImm.py were). The resulting
        JS for a healed block will likely be structured wrong (it'll
        show up dangling at the top level rather than nested inside
        whatever construct actually reaches it) - treat the warning as
        a todo list, not as "handled".
        """

        visited: set[int] = set()
        queue = deque([cfg.entry])

        while queue:
            block = queue.popleft()
            if block.id in visited:
                continue
            visited.add(block.id)
            for edge in block.outgoing:
                target = cfg.get_block(edge.target)
                if target is not None:
                    queue.append(target)

        for block in cfg:

            if block.id in visited or block is cfg.entry:
                continue

            logger.warning(
                "BasicBlock %s is unreachable from entry after normal/exception/"
                "switch edge wiring. Patching in a synthetic edge from entry so "
                "conversion doesn't crash - the emitted JS for this block is "
                "likely structurally wrong and needs investigation (check for "
                "generator resume points or other jump patterns this builder "
                "doesn't wire into the CFG yet).",
                block.id,
            )
            cls._connect_edge(cfg.entry, block, EdgeKind.UNCONDITIONAL)

    @staticmethod
    def _connect_edge(
            source: BasicBlock,
            target: BasicBlock,
            kind: EdgeKind,
    ):

        edge = CFGEdge(
            source=source.id,
            target=target.id,
            kind=kind,
        )

        source.outgoing.append(edge)

        target.incoming.append(edge)

    @staticmethod
    def _falls_through(result) -> bool:
        """
        True if control can reach the next instruction in program order
        after this one.

        Ret/Throw/CompleteGenerator never fall through - they leave the
        function. Unconditional `Jmp`/`JmpLong` never fall through
        either - their `goto` edge (added above, kind=UNCONDITIONAL) is
        the *only* way out of the block; there is no "condition false"
        path to fall into.

        Conditional jumps (`JmpTrue`, `JmpFalse`, `JmpUndefined`,
        `JmpBuiltinIs`, `JmpBuiltinIsNot`, `JmpTypeOfIs`, and their
        `*Long` variants) DO fall through: the `goto` edge covers the
        "condition true" path (kind=TRUE_BRANCH), and the fallthrough
        edge added here covers the "condition false" / continuation
        path. Together they give exactly the two outgoing edges that
        IfRegion structuring depends on.

        TODO: `SwitchImm` case targets are now wired via `extra_gotos`
        (see `_connect`), but SwitchImm itself is still treated as
        falling through to the physically-next instruction too - i.e.
        every switch is currently modeled as if it also has an
        implicit "no case matched -> fall through" edge. That's a safe
        over-approximation (an extra reachable edge, never a missing
        one) but isn't necessarily correct Hermes SwitchImm semantics -
        worth confirming against a real disassembly of a `switch`
        statement before relying on the exact shape of SwitchRegion
        output.
        """

        non_falling = {
            "Ret",
            "Throw",
            "CompleteGenerator",
            "Jmp",
            "JmpLong",
        }

        return result.handler not in non_falling
