from __future__ import annotations

from abc import ABC, abstractmethod
from collections.abc import Iterable
from typing import Dict, List, Optional, Set

from hermes_decompiler.backend.analysis.cfg.BasicBlock import BasicBlock


class _IterativeSetAnalysis(ABC):

    def __init__(self, cfg):

        self.cfg = cfg

        self.result: Dict[BasicBlock, Set[BasicBlock]] = {}

    def compute(self):

        blocks = self.cfg.blocks
        roots = self.roots()

        handler_by_target: dict[BasicBlock, dict] = {
            h["handler_block"]: h
            for h in getattr(self.cfg, "exception_handlers", [])
        }

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
                    handler = handler_by_target.get(block)
                    neighbors = handler["try_blocks"] if handler else []

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

    def compute_immediate(self) -> Dict[BasicBlock, BasicBlock | None]:
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
        immediate: Dict[BasicBlock, "BasicBlock | None"] = {}

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
            immediate: Dict[BasicBlock, Optional[BasicBlock]],
    ) -> Dict[BasicBlock, List[BasicBlock]]:
        """
        Turns an immediate-dominator/post-dominator map (as produced by
        `compute_immediate()`) into a children adjacency map, i.e. the
        actual dominator/post-dominator *tree*.

        Shared by `DominatorTree` and `PostDominatorTree` for the same
        reason `compute_immediate()` is: the two analyses only differ in
        `roots()`/`neighbors()`, never in how the resulting immediate-map
        is turned into a tree.
        """

        children: Dict[BasicBlock, List[BasicBlock]] = {
            block: []
            for block in self.cfg.blocks
        }

        for block, parent in immediate.items():

            if parent is None:
                continue

            children[parent].append(block)

        return children
