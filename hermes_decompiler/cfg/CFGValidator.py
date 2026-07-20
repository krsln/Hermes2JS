from hermes_decompiler.cfg import ControlFlowGraph


class CFGValidator:

    @classmethod
    def validate(cls, cfg: ControlFlowGraph) -> None:

        cls._validate_entry(cfg)

        cls._validate_edges(cfg)

        cls._validate_blocks(cfg)

        cls._validate_reachability(cfg)