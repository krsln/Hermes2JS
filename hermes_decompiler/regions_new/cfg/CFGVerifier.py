class CFGVerifier:

    def __init__(self, cfg):

        self.cfg = cfg

    def verify(self):

        self._verify_entry()
        self._verify_edges()
        self._verify_blocks()

    def _verify_entry(self):

        assert self.cfg.entry is not None

    def _verify_edges(self):

        for block in self.cfg.blocks:

            for succ in block.successors:

                assert block in succ.predecessors

            for pred in block.predecessors:

                assert block in pred.successors

    def _verify_blocks(self):

        for block in self.cfg.blocks:

            assert len(block.instructions) > 0