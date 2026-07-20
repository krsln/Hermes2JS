from hermes_decompiler.cfg import BasicBlock, ControlFlowGraph


class ControlFlowGraphBuilder:

    @classmethod
    def build(cls, blocks: list[BasicBlock]) -> ControlFlowGraph:
        cfg = ControlFlowGraph.from_blocks(blocks)

        cls._connect_blocks(cfg)

        return cfg

    @staticmethod
    def _connect_blocks(cfg: ControlFlowGraph) -> None:
        """
        Populate predecessor/successor relationships between basic blocks.
        """
        ...
