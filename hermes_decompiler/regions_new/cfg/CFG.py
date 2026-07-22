from __future__ import annotations


class CFG:

    def __init__(self):
        self.blocks = []
        self.entry = None

        self.dominator_tree = None
        self.post_dominator_tree = None

    @classmethod
    def from_results(cls, results):
        from .CFGBuilder import CFGBuilder

        return CFGBuilder().build(results)

    def verify(self):
        from .CFGVerifier import CFGVerifier

        CFGVerifier(self).verify()

    def compute_dominators(self):
        from .DominatorTree import DominatorTree

        self.dominator_tree = DominatorTree(self)
        self.dominator_tree.compute()

    def compute_post_dominators(self):
        from .PostDominatorTree import PostDominatorTree

        self.post_dominator_tree = PostDominatorTree(self)
        self.post_dominator_tree.compute()
