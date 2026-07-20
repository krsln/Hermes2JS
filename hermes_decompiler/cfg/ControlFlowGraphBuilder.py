from hermes_decompiler.cfg.BasicBlock import BasicBlock
from hermes_decompiler.cfg.CFGEdge import CFGEdge
from hermes_decompiler.cfg.ControlFlowGraph import ControlFlowGraph
from hermes_decompiler.cfg.EdgeKind import EdgeKind


class ControlFlowGraphBuilder:
    """
    Builds the Control Flow Graph (CFG) from basic blocks.
    """

    @classmethod
    def build(cls, blocks: list[BasicBlock]) -> ControlFlowGraph:
        """
        Construct a Control Flow Graph from linear basic blocks.
        """
        cfg = ControlFlowGraph.from_blocks(blocks)

        cls._connect_blocks(cfg)

        return cfg

    @classmethod
    def _connect_blocks(cls, cfg: ControlFlowGraph) -> None:
        """
        Connect basic blocks using control-flow edges.

        Supported:
            • fall-through
            • unconditional jumps
            • conditional jumps

        Future:
            • exception edges
            • switch edges
            • loop back-edges
        """

        ordered_blocks = sorted(
            cfg.blocks.values(),
            key=lambda block: block.start_addr,
        )

        for index, block in enumerate(ordered_blocks):

            if not block.instructions:
                continue

            last = block.instructions[-1]

            # --------------------------------------------------
            # explicit goto
            # --------------------------------------------------

            if last.goto is not None:
                cls._add_edge(
                    cfg,
                    block.start_addr,
                    last.goto,
                )

            # --------------------------------------------------
            # fall-through
            # --------------------------------------------------

            if cls._falls_through(last):

                if index + 1 < len(ordered_blocks):

                    cls._add_edge(
                        cfg,
                        block.start_addr,
                        ordered_blocks[index + 1].start_addr,
                    )

    @staticmethod
    def _falls_through(result) -> bool:
        """
        Returns whether execution continues with the next block.
        """

        terminal = {
            "Ret",
            "Throw",
            "CompleteGenerator",
        }

        return result.handler not in terminal

    @staticmethod
    def _add_edge(
            cfg: ControlFlowGraph,
            source_addr: int,
            target_addr: int,
            kind: EdgeKind,
    ) -> None:

        source = cfg.get_block(source_addr)
        target = cfg.get_block(target_addr)

        if source is None or target is None:
            return

        edge = CFGEdge(
            source=source_addr,
            target=target_addr,
            kind=kind,
        )

        source.outgoing.append(edge)
        target.incoming.append(edge)