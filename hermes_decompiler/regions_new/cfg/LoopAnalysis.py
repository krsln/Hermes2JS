from hermes_decompiler.regions_new.cfg.NaturalLoop import NaturalLoop


class LoopAnalysis:

    def __init__(self, cfg):

        self.cfg = cfg

        self.back_edges = []

        self.loops: dict[int, NaturalLoop] = {}

    def compute(self):

        tree = self.cfg.dominator_tree

        self.loops.clear()

        for tail in self.cfg.blocks:

            for header in tail.successors:

                if header is tail:
                    continue

                if not tree.dominates(header, tail):
                    continue

                self._merge_back_edge(header, tail)

        self._compute_exits()

    def _merge_back_edge(
            self,
            header,
            tail,
    ):

        loop = self.loops.get(header.id)

        if loop is None:
            loop = NaturalLoop(header=header)

            self.loops[header.id] = loop

        loop.latches.add(tail)

        members = self._discover_members(header, tail)

        loop.members.update(members)

    def _discover_members(
            self,
            header,
            tail,
    ):

        members = {header, tail}

        stack = [tail]

        while stack:

            block = stack.pop()

            for pred in block.predecessors:

                if pred in members:
                    continue

                members.add(pred)

                if pred != header:
                    stack.append(pred)

        return members

    def _compute_exits(self):

        for loop in self.loops.values():

            for block in loop.members:

                for succ in block.successors:

                    if succ not in loop.members:
                        loop.exits.add(succ)
