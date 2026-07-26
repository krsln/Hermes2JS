from hermes_decompiler.regions.cfg.NaturalLoop import NaturalLoop


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
        self._compute_nesting()

        # print("\n=== Natural Loops ===")
        # for loop in sorted(
        #         self.loops.values(),
        #         key=lambda l: l.header.id
        # ):
        #     print(
        #         f"header={loop.header.id} "
        #         f"parent={loop.parent.header.id if loop.parent else None} "
        #         f"children={[c.header.id for c in loop.children]} "
        #         f"members={[b.id for b in loop.blocks]}"
        #     )

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

    def _compute_nesting(self):

        loops = list(self.loops.values())

        #
        # önce temizle
        #
        for loop in loops:
            loop.parent = None
            loop.children.clear()

        #
        # her loop için en küçük kapsayan parent'ı bul
        #
        for child in loops:

            best_parent = None
            best_size = None

            for parent in loops:

                if parent is child:
                    continue

                #
                # child tamamen parent'ın içinde mi?
                #
                if not child.members.issubset(parent.members):
                    continue

                #
                # kendisiyle aynı loop değil
                #
                if len(child.members) == len(parent.members):
                    continue

                #
                # en küçük kapsayan parent
                #
                if best_parent is None or len(parent.members) < best_size:
                    best_parent = parent
                    best_size = len(parent.members)

            if best_parent is not None:
                child.parent = best_parent
                best_parent.children.append(child)
