from hermes_decompiler.cfg import ControlFlowGraph, BasicBlock


class PostDominatorAnalyzer:

    @classmethod
    def find_merge(
            cls,
            cfg: ControlFlowGraph,
            block: BasicBlock,
    ) -> BasicBlock | None:
        ...
