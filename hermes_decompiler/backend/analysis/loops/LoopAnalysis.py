from __future__ import annotations

from typing import TYPE_CHECKING

from hermes_decompiler.backend.analysis.cfg.BasicBlock import BasicBlock
from hermes_decompiler.backend.analysis.loops.NaturalLoop import NaturalLoop

if TYPE_CHECKING:
    from hermes_decompiler.backend.analysis.cfg import CFG


class LoopAnalysis:
    """
    Discover and organize natural loops in a control-flow graph.

    The analysis identifies back edges using dominator information.
    Back edges targeting the same header are merged into a single
    ``NaturalLoop`` instance. After all loops are discovered, the
    analysis computes their exit blocks and nesting relationships.
    """

    def __init__(self, cfg: CFG) -> None:
        """
        Initialize the loop analysis.

        Args:
            cfg: The control-flow graph to analyze.
        """

        self.cfg = cfg
        self.loops: dict[int, NaturalLoop] = {}

    def compute(self) -> None:
        """
        Compute all natural loops in the control-flow graph.

        The analysis proceeds in three phases:

        1. Identify back edges using dominator relationships.
        2. Merge back edges with the same header into natural loops.
        3. Compute loop exits and loop nesting relationships.
        """

        dominator_tree = self.cfg.dominator_tree
        self.loops.clear()

        for tail in self.cfg.blocks:
            for header in tail.successors:
                if dominator_tree.dominates(header, tail):
                    self._merge_back_edge(header, tail)

        self._compute_exits()
        self._compute_nesting()

    def _merge_back_edge(self, header: BasicBlock, tail: BasicBlock) -> None:
        """
        Merge a back edge into the natural loop for its header.

        Multiple back edges may target the same loop header. Their
        discovered members are merged into one ``NaturalLoop``.
        """

        loop = self.loops.get(header.id)

        if loop is None:
            loop = NaturalLoop(header=header)
            self.loops[header.id] = loop

        loop.latches.add(tail)
        loop.members.update(self._discover_members(header, tail))

    @staticmethod
    def _discover_members(header: BasicBlock, tail: BasicBlock) -> set[BasicBlock]:
        """
        Discover the natural-loop members induced by a back edge.

        Starting from the back-edge tail, the algorithm walks
        predecessor edges backwards until reaching the loop header.
        The header itself is included in the result but is not expanded
        through, preventing predecessors outside the loop from being
        included.

        A self-loop is handled as a special case because its header and
        tail are the same block. Expanding predecessors from that block
        could incorrectly pull external predecessor blocks into the
        loop.

        Args:
            header: The target of the back edge and loop entry block.
            tail: The source of the back edge.

        Returns:
            The set of basic blocks belonging to the natural loop
            induced by this back edge.
        """

        if header is tail:
            return {header}

        members: set[BasicBlock] = {header, tail}
        stack: list[BasicBlock] = [tail]

        while stack:
            block = stack.pop()

            for predecessor in block.predecessors:
                if predecessor in members:
                    continue

                members.add(predecessor)

                if predecessor is not header:
                    stack.append(predecessor)

        return members

    def _compute_exits(self) -> None:
        """
        Compute all direct exit targets for each discovered loop.

        A block is an exit target when it is the successor of a loop
        member but does not itself belong to the same loop.
        """

        for loop in self.loops.values():
            loop.exits.clear()

            for block in loop.members:
                for successor in block.successors:
                    if successor not in loop.members:
                        loop.exits.add(successor)

    def _compute_nesting(self) -> None:
        """
        Compute immediate parent-child relationships between loops.

        A loop is nested inside another loop when all of its members are
        contained in the other loop, and the two loops do not have the
        same member set. The smallest enclosing loop becomes the direct
        parent.
        """

        loops = list(self.loops.values())

        for loop in loops:
            loop.parent = None
            loop.children.clear()

        for child in loops:
            best_parent: NaturalLoop | None = None

            for candidate in loops:
                if candidate is child:
                    continue

                if not child.members < candidate.members:
                    continue

                if (
                        best_parent is None
                        or len(candidate.members) < len(best_parent.members)
                ):
                    best_parent = candidate

            if best_parent is not None:
                child.parent = best_parent
                best_parent.children.append(child)
