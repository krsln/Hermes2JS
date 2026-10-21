from __future__ import annotations

from hermes_decompiler.backend.analysis.cfg import BasicBlock
from hermes_decompiler.backend.regions import IfRegion, RegionVisitor, SequenceRegion
from hermes_decompiler.core.logging import get_logger
from hermes_decompiler.ir.terminators import TerminatorConditionalBranch, TerminatorReturn, TerminatorThrow
from ._base import RegionPass

logger = get_logger(__name__)


class GuardExitRegionPass(RegionPass, RegionVisitor):
    """`if (c) return x;` whose exit block was laid out after the code it guards.

        if (a) {
            ...
            if (c) goto EXIT;          # taken: leave the function
        }                              # not taken: falls on to TAIL
        TAIL
        EXIT: return x;

    `IfStructurer` can only pull a branch target into the `if` when it sits
    inside the same sequence, so the guard stayed a raw `if (c) goto label`
    with `return x;` dangling after the tail. A target that only ends the
    function and is reached by this one branch can simply move into the `if`,
    provided the branch's fall-through really is the next thing that runs
    (checked against the tree, not the addresses).
    """

    def run(self) -> None:
        self.visit(self.graph.root)

    def visit_SequenceRegion(self, node: SequenceRegion) -> None:
        for child in list(node.children):
            if isinstance(child, BasicBlock):
                self._try_guard(node, child)

        for child in list(node.children):
            if not isinstance(child, BasicBlock):
                self.visit(child)

    def _try_guard(self, owner: SequenceRegion, block: BasicBlock) -> None:
        branch = block.terminator

        if not isinstance(branch, TerminatorConditionalBranch):
            return

        exit_block = next((b for b in block.successors if b.address == branch.target), None)
        others = [b for b in block.successors if b is not exit_block]

        if (
                exit_block is None
                or len(others) != 1
                or exit_block.successors
                or not (
                exit_block.terminator is None or isinstance(exit_block.terminator, (TerminatorReturn, TerminatorThrow)))
                or list(exit_block.predecessors) != [block]
                or exit_block.address <= block.address
        ):
            return

        # The graph's owner map can lag behind earlier splices; trust the tree.
        exit_owner = self._holder(self.graph.root, exit_block)

        if exit_owner is None or exit_owner is owner:
            return

        # Inside a loop the branch may be one of the loop's own exits. Walk the
        # CFG itself: the loop analysis predates the copies the duplication
        # passes make, and the loop regions may not be built yet.
        if self._on_a_cycle(block):
            return

        if not self._falls_on_to(owner, block, others[0]):
            return

        if not block.instructions or block.instructions[-1].terminator is not branch:
            return

        block.instructions.pop()
        block.terminator = None

        exit_owner.children.remove(exit_block)
        exit_owner.invalidate_coverage()

        then_body = SequenceRegion()
        self.graph.transfer([exit_block], then_body)

        if_region = IfRegion()
        if_region.condition = branch.condition
        if_region.then_body = then_body
        if_region.else_body = None

        self.graph.insert_at(owner, owner.children.index(block) + 1, if_region)
        logger.debug("guard exit: block %d takes %d", block.id, exit_block.id)

    @staticmethod
    def _on_a_cycle(block: BasicBlock) -> bool:
        seen: set = set()
        stack = list(block.successors)

        while stack:
            current = stack.pop()

            if current is block:
                return True

            if current in seen:
                continue

            seen.add(current)
            stack.extend(current.successors)

        return False

    def _holder(self, region, block: BasicBlock):
        """The sequence that directly holds `block`, found by walking the tree."""
        if isinstance(region, SequenceRegion):
            if any(child is block for child in region.children):
                return region

            for child in region.children:
                if not isinstance(child, BasicBlock):
                    found = self._holder(child, block)

                    if found is not None:
                        return found

            return None

        for child in self._sub_regions(region):
            found = self._holder(child, block)

            if found is not None:
                return found

        return None

    @staticmethod
    def _sub_regions(region):
        parts = []

        for name in ("then_body", "else_body", "body", "try_body", "default_body"):
            part = getattr(region, name, None)

            if part is not None:
                parts.append(part)

        for name in ("catch", "finally_"):
            part = getattr(region, name, None)

            if part is not None and getattr(part, "body", None) is not None:
                parts.append(part.body)

        parts.extend(case.body for case in getattr(region, "cases", ()) if case.body is not None)

        return [p for p in parts if not isinstance(p, BasicBlock)]

    @staticmethod
    def _falls_on_to(owner: SequenceRegion, block: BasicBlock, follower: BasicBlock) -> bool:
        """True if the next thing to run after `block` finishes is `follower`."""
        sequence: SequenceRegion = owner
        item = block

        while True:
            index = sequence.children.index(item)

            if index + 1 < len(sequence.children):
                nxt = sequence.children[index + 1]

                if isinstance(nxt, BasicBlock):
                    return nxt is follower

                covered = [b for b in nxt.covered_blocks if b.address >= 0]

                return follower in covered and follower is min(covered, key=lambda b: b.address)

            parent = sequence.parent

            if not isinstance(parent, IfRegion):
                return False

            holder = parent.parent

            if not isinstance(holder, SequenceRegion) or parent not in holder.children:
                return False

            item, sequence = parent, holder
