from hermes_decompiler.regions_new.cfg.NaturalLoop import NaturalLoop


class LoopAnalysis:

    def __init__(self, cfg):

        self.cfg = cfg

        self.back_edges = []

        self.loops = []

    def compute(self):

        tree = self.cfg.dominator_tree

        self.back_edges.clear()
        self.loops.clear()

        for tail in self.cfg.blocks:

            for header in tail.successors:

                if header is tail:
                    continue

                if not tree.dominates(header, tail):
                    continue

                self.back_edges.append((tail, header))

                loop = self._build_loop(header, tail)

                self.loops.append(loop)

    def _build_loop(self, header, tail):

        loop = NaturalLoop(
            header=header,
            tail=tail,
        )

        loop.members.add(header)
        loop.members.add(tail)

        loop.latches.add(tail)

        stack = [tail]

        while stack:

            block = stack.pop()

            for pred in block.predecessors:

                if pred in loop.members:
                    continue

                loop.members.add(pred)

                if pred != header:
                    stack.append(pred)

        return loop