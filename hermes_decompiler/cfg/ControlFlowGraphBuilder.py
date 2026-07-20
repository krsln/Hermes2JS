from hermes_decompiler.cfg import CFGValidator
from hermes_decompiler.cfg.BasicBlock import BasicBlock
from hermes_decompiler.cfg.CFGEdge import CFGEdge
from hermes_decompiler.cfg.ControlFlowGraph import ControlFlowGraph
from hermes_decompiler.cfg.EdgeKind import EdgeKind


class ControlFlowGraphBuilder:
    """
    Build edges between BasicBlocks.
    """

    @classmethod
    def build(cls, blocks: list[BasicBlock]) -> ControlFlowGraph:

        cfg = ControlFlowGraph.from_blocks(blocks)

        cls._connect(cfg)

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

            #
            # explicit jump
            #

            if last.goto is not None:

                target = cfg.get_block(last.goto)

                if target is not None:
                    cls._connect_edge(
                        block,
                        target,
                        cls._edge_kind(last),
                    )

            #
            # fallthrough
            #

            if cls._falls_through(last):

                if index + 1 < len(ordered):
                    cls._connect_edge(
                        block,
                        ordered[index + 1],
                        EdgeKind.FALLTHROUGH,
                    )

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

        terminal = {
            "Ret",
            "Throw",
            "CompleteGenerator",
        }

        return result.handler not in terminal

    @staticmethod
    def _edge_kind(result) -> EdgeKind:

        handler = result.handler

        if handler.startswith("JmpTrue"):
            return EdgeKind.TRUE_BRANCH

        if handler.startswith("JmpFalse"):
            return EdgeKind.FALSE_BRANCH

        return EdgeKind.UNCONDITIONAL
