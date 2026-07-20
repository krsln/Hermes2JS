from __future__ import annotations

from hermes_decompiler.cfg.BasicBlock import BasicBlock
from hermes_decompiler.cfg.ControlFlowGraph import ControlFlowGraph


class ReversePostOrder:
    """
    Computes Reverse Post Order traversal of a CFG.
    """

    @classmethod
    def build(cls, cfg: ControlFlowGraph) -> list[BasicBlock]:

        visited: set[int] = set()

        postorder: list[BasicBlock] = []

        def dfs(block: BasicBlock):

            if block.id in visited:
                return

            visited.add(block.id)

            for edge in block.outgoing:

                target = cfg.get_block(edge.target)

                if target is not None:
                    dfs(target)

            postorder.append(block)

        dfs(cfg.entry)

        postorder.reverse()

        return postorder