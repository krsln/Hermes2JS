from abc import ABC

from hermes_decompiler.analysis.cfg import BasicBlock


class Region(ABC):
    """
    Base class for every node in the region tree.

    `covered_blocks` is the set of every raw BasicBlock reachable
    anywhere under this region. It's lazily computed and cached;
    `invalidate_coverage()` must be called whenever the subtree
    changes shape and propagates up through `.parent` so an ancestor
    never serves a stale answer.
    """

    def __init__(self):
        self.parent: Region | None = None
        self._covered_blocks: set[BasicBlock] | None = None

    @property
    def covered_blocks(self) -> set[BasicBlock]:
        covered_blocks = self._covered_blocks

        if covered_blocks is None:
            covered_blocks = self._compute_covered_blocks()
            self._covered_blocks = covered_blocks

        return covered_blocks

    def invalidate_coverage(self) -> None:
        if self._covered_blocks is None and self.parent is None:
            return
        self._covered_blocks = None
        if self.parent is not None:
            self.parent.invalidate_coverage()

    def _compute_covered_blocks(self) -> set[BasicBlock]:
        raise NotImplementedError


class SequenceRegion(Region):

    def __init__(self):
        super().__init__()

        self.children: list[BasicBlock | Region] = []
        self.items = []

    def append(self, node):
        if isinstance(node, Region):
            node.parent = self

        self.children.append(node)
        self.invalidate_coverage()

    def _compute_covered_blocks(self) -> set[BasicBlock]:
        covered: set[BasicBlock] = set()

        for child in self.children:
            if isinstance(child, BasicBlock):
                covered.add(child)
            else:
                covered |= child.covered_blocks

        return covered
