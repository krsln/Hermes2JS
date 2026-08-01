from __future__ import annotations


class CFGVerifier:

    def __init__(self, cfg):

        self.cfg = cfg

    # ---------------------------------------------------------

    def verify(self):

        self._verify_entry()

        self._verify_blocks()

        self._verify_edges()

    # ---------------------------------------------------------

    def _verify_entry(self):

        if self.cfg.entry is None:
            raise ValueError("CFG has no entry block.")

    # ---------------------------------------------------------

    def _verify_blocks(self):

        for block in self.cfg.blocks:

            if (
                    not block.instructions
                    and block.terminator is None
            ):
                raise ValueError(f"Empty basic block: {block.id}")

    # ---------------------------------------------------------

    def _verify_edges(self):

        for block in self.cfg.blocks:

            for successor in block.successors:

                if block not in successor.predecessors:
                    raise ValueError(f"Broken edge: {block.id} -> {successor.id}")

            for predecessor in block.predecessors:

                if block not in predecessor.successors:
                    raise ValueError(f"Broken edge: {predecessor.id} -> {block.id}")
