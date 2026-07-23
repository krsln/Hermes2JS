from __future__ import annotations

from hermes_decompiler.two.cfg.ControlFlowGraph import ControlFlowGraph
from hermes_decompiler.two.cfg.Loop import Loop


class LoopAnalysis:
    """
    Detect natural loops from CFG back-edges.
    """

    @classmethod
    def build(
            cls,
            cfg: ControlFlowGraph,
            dominators: dict[int, set[int]],
    ) -> list[Loop]:

        loops: list[Loop] = []

        for block in cfg:

            for edge in block.outgoing:

                #
                # Back-edge:
                #
                # target dominates source
                #

                if edge.target not in dominators[block.id]:
                    continue

                body = cls._collect_loop(
                    cfg,
                    edge.source,
                    edge.target,
                )

                loops.append(
                    Loop(
                        header=edge.target,
                        latch=edge.source,
                        body=body,
                    )
                )

        return loops

    @classmethod
    def _collect_loop(
        cls,
        cfg: ControlFlowGraph,
        latch: int,
        header: int,
    ) -> set[int]:

        body = {header}

        stack = [latch]

        while stack:

            current = stack.pop()

            if current in body:
                continue

            body.add(current)

            block = cfg.get_block(current)

            if block is None:
                continue

            for edge in block.incoming:
                stack.append(edge.source)

        return body