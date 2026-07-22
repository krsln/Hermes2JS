from hermes_decompiler.regions_new.cfg.NaturalLoop import NaturalLoop


class LoopAnalysis:

    def __init__(self, cfg):

        self.cfg = cfg

        self.back_edges = []

        self.loops: list[NaturalLoop] = []

    def compute(self):

        tree = self.cfg.dominator_tree

        self.back_edges.clear()
        self.loops.clear()

        for tail in self.cfg.blocks:

            for header in tail.successors:

                if header is tail:
                    continue

                if tree.dominates(header, tail):

                    self.back_edges.append((tail, header))

                    loop = NaturalLoop(
                        header=header,
                        tail=tail,
                    )

                    self.loops.append(loop)