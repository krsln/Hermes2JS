from collections import deque

from hermes_decompiler.cfg.ControlFlowGraph import ControlFlowGraph


class CFGValidator:
    """
    Validates structural correctness of a Control Flow Graph.

    The validator ensures that later analysis stages operate on a
    consistent graph.
    """

    @classmethod
    def validate(cls, cfg: ControlFlowGraph) -> None:

        cls._validate_entry(cfg)
        cls._validate_blocks(cfg)
        cls._validate_edges(cfg)
        cls._validate_reachability(cfg)

    # ---------------------------------------------------------

    @staticmethod
    def _validate_entry(cfg: ControlFlowGraph) -> None:

        if len(cfg) == 0:
            raise ValueError("CFG contains no basic blocks.")

    # ---------------------------------------------------------

    @staticmethod
    def _validate_blocks(cfg: ControlFlowGraph) -> None:

        for block in cfg:

            if not block.instructions:
                raise ValueError(
                    f"BasicBlock {block.start_addr} is empty."
                )

            if block.start_addr > block.end_addr:
                raise ValueError(
                    f"Invalid BasicBlock range "
                    f"{block.start_addr} -> {block.end_addr}"
                )

    # ---------------------------------------------------------

    @staticmethod
    def _validate_edges(cfg: ControlFlowGraph) -> None:

        for block in cfg:

            for edge in block.outgoing:

                if cfg.get_block(edge.target) is None:
                    raise ValueError(
                        f"Edge points to unknown block "
                        f"{edge.target}"
                    )

    # ---------------------------------------------------------

    @staticmethod
    def _validate_reachability(cfg: ControlFlowGraph) -> None:

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

        unreachable = [
            block.start_addr
            for block in cfg
            if block.id not in visited
        ]

        if unreachable:

            raise ValueError(
                "Unreachable BasicBlocks: "
                + ", ".join(map(str, unreachable))
            )