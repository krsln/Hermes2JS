from __future__ import annotations

from hermes_decompiler.cfg.BasicBlock import BasicBlock
from hermes_decompiler.cfg.ControlFlowGraph import ControlFlowGraph


class ReversePostOrder:
    """
    Computes Reverse Post Order traversal of a CFG.
    """

    @classmethod
    def build(cls, cfg: ControlFlowGraph) -> list[BasicBlock]:
        """
        Iterative post-order DFS (explicit stack), then reversed.

        BUG FIX (was): this used plain Python-call recursion
        (`def dfs(block): ... dfs(target) ...`), one stack frame per
        block depth in the DFS tree. For CFGs shaped like a long chain
        of sequential if/else guards - exactly what Hermes generator/
        async state-machine bytecode produces for large functions -
        DFS depth is roughly the number of guards, which routinely
        exceeds Python's default recursion limit (~1000) on real
        production .hbc input and raises RecursionError before
        StructuralAnalyzer even starts. Rewritten as an explicit-stack
        iterative DFS so traversal depth is bounded by available
        memory instead of the Python call stack - same fix rationale
        as `regions.building._StructuralAnalyzer`'s rewrite.
        """

        visited: set[int] = set()
        postorder: list[BasicBlock] = []

        # Each stack entry is (block, iterator-over-remaining-successor-blocks).
        # This is the standard "iterative DFS with explicit frame" pattern:
        # each stack entry mirrors what one recursive call's local state
        # (`block`, and its position while iterating `block.outgoing`) would
        # have been.
        stack: list[tuple[BasicBlock, iter]] = []

        def successors(block: BasicBlock):
            for edge in block.outgoing:
                target = cfg.get_block(edge.target)
                if target is not None:
                    yield target

        entry = cfg.entry
        visited.add(entry.id)
        stack.append((entry, successors(entry)))

        while stack:

            block, remaining = stack[-1]

            advanced = False
            for target in remaining:
                if target.id not in visited:
                    visited.add(target.id)
                    stack.append((target, successors(target)))
                    advanced = True
                    break

            if not advanced:
                # Exhausted this block's successors - this is the
                # moment the old recursive version would have returned
                # from `dfs(block)` and appended it post-order.
                postorder.append(block)
                stack.pop()

        postorder.reverse()

        return postorder