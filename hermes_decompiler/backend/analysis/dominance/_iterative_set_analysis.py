from __future__ import annotations

from abc import ABC, abstractmethod
from collections.abc import Iterable

from hermes_decompiler.backend.analysis.cfg.BasicBlock import BasicBlock


class _IterativeSetAnalysis(ABC):

    def __init__(self, cfg):

        self.cfg = cfg

        self.result: dict[BasicBlock, set[BasicBlock]] = {}

    def compute(self):

        blocks = self.cfg.blocks
        roots = self.roots()

        # Approximated virtual predecessors for a handler_block, keyed by
        # the block itself. Hermes may point MULTIPLE distinct handler
        # entries (different [start, end) protected ranges) at the exact
        # same physical handler_block - `_merge_fragmented_handlers`
        # deliberately leaves them separate whenever another handler's
        # range sits in the gap between them (see its own docstring,
        # nestedArrayDestructureTest). A plain `{handler_block: handler}`
        # dict here would keep only the LAST such handler and silently
        # drop every other one's try_blocks, starving this block of most
        # of its real virtual predecessors - which, if every OTHER
        # contributor also happens to be unreachable/dead code, can leave
        # it (and blocks that in turn depend on it) stuck at the initial
        # universal set below and never converge. Collect every
        # contributing handler's try_blocks instead of just one.
        virtual_predecessors_by_target: dict[BasicBlock, list[BasicBlock]] = {}

        for h in getattr(self.cfg, "exception_handlers", []):
            existing = virtual_predecessors_by_target.setdefault(h["handler_block"], [])
            for block in h["try_blocks"]:
                if block not in existing:
                    existing.append(block)

        for block in blocks:
            self.result[block] = {block} if block in roots else set(blocks)

        changed = True

        while changed:
            changed = False

            for block in blocks:
                if block in roots:
                    continue

                neighbors = list(self.neighbors(block))

                if not neighbors:
                    # No real edge reaches this block - typically a handler
                    # entered only via exception dispatch (CFGBuilder doesn't
                    # model that as a real edge, see that file's own
                    # docstring: "Not yet supported: Exception edges").
                    # Approximate the missing edge from the exception table:
                    # a handler is treated as if it had a "virtual"
                    # predecessor edge from every block it guards - because
                    # an exception can genuinely be thrown from there.
                    neighbors = virtual_predecessors_by_target.get(block, [])

                if not neighbors:
                    continue

                it = iter(neighbors)
                new_set = self.result[next(it)].copy()

                for n in it:
                    new_set &= self.result[n]

                new_set.add(block)

                if new_set != self.result[block]:
                    self.result[block] = new_set
                    changed = True

    @abstractmethod
    def roots(self) -> Iterable[BasicBlock]:
        ...

    @abstractmethod
    def neighbors(self, block: BasicBlock) -> Iterable[BasicBlock]:
        ...

    def compute_immediate(self) -> dict[BasicBlock, BasicBlock | None]:
        """
        Computes the immediate dominator or post-dominator for each block.

        The relation is derived from `self.result`, which contains the
        dominator or post-dominator set for each block.

        For each non-root block, the immediate relation is the strict
        dominator or post-dominator that is closest to the block.

        This implementation is shared by `DominatorTree` and
        `PostDominatorTree`; only `self.result` and `roots()` differ.
        """

        roots = set(self.roots())
        immediate: dict[BasicBlock, "BasicBlock | None"] = {}

        for block in self.cfg.blocks:

            if block in roots:
                immediate[block] = None
                continue

            strict = self.result[block] - {block}
            candidate = None

            for c in strict:
                if all(c not in self.result[other] for other in strict if other is not c):
                    candidate = c
                    break

            immediate[block] = candidate

        return immediate

    def build_tree(
            self,
            immediate: dict[BasicBlock, BasicBlock | None],
    ) -> dict[BasicBlock, list[BasicBlock]]:
        """
        Turns an immediate-dominator/post-dominator map (as produced by
        `compute_immediate()`) into a children adjacency map, i.e., the
        actual dominator/post-dominator *tree*.

        Shared by `DominatorTree` and `PostDominatorTree` for the same
        reason `compute_immediate()` is: the two analyses only differ in
        `roots()`/`neighbors()`, never in how the resulting immediate-map
        is turned into a tree.
        """

        children: dict[BasicBlock, list[BasicBlock]] = {
            block: []
            for block in self.cfg.blocks
        }

        for block, parent in immediate.items():

            if parent is None:
                continue

            children[parent].append(block)

        return children
