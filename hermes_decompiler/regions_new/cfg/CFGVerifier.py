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

            if not block.instructions:
                raise ValueError(
                    f"Empty basic block: {block.id}"
                )

    # ---------------------------------------------------------

    def _verify_edges(self):

        for block in self.cfg.blocks:

            for succ in block.successors:

                if block not in succ.predecessors:

                    raise ValueError(
                        f"Broken edge: {block.id} -> {succ.id}"
                    )

            for pred in block.predecessors:

                if block not in pred.successors:

                    raise ValueError(
                        f"Broken edge: {pred.id} -> {block.id}"
                    )