from __future__ import annotations

from hermes_decompiler.backend.analysis.cfg import BasicBlock
from hermes_decompiler.backend.regions import IfRegion, RegionVisitor, SequenceRegion
from hermes_decompiler.core.logging import get_logger
from hermes_decompiler.ir.terminators import (
    TerminatorConditionalBranch,
    TerminatorJump,
    TerminatorReturn,
    TerminatorThrow,
)
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

        if isinstance(branch, TerminatorJump):
            self._try_jump_exit(owner, block, branch)
            return

        if not isinstance(branch, TerminatorConditionalBranch):
            return

        exit_block = next((b for b in block.successors if b.address == branch.target), None)
        others = [b for b in block.successors if b is not exit_block]

        if exit_block is not None and len(others) == 1 and exit_block.successors:
            self._try_region_exit(owner, block, branch, exit_block, others[0])
            return

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

    def _try_region_exit(self, owner, block: BasicBlock, branch, exit_block: BasicBlock, other: BasicBlock) -> None:
        """`if (c) goto X` where X starts code that only this branch enters and that ends the function.

        Several blocks (`found: { ...; return }`) laid out after the loop or `if`
        that holds the test: the whole tail moves into the `if`.
        """
        if exit_block.address <= block.address or exit_block not in [b for b in block.successors]:
            return

        exit_owner = self._holder(self.graph.root, exit_block)

        if exit_owner is None or exit_owner is owner or exit_block not in exit_owner.children:
            return

        tail = exit_owner.children[exit_owner.children.index(exit_block):]
        covered = set()

        for item in tail:
            covered.update(
                b for b in ([item] if isinstance(item, BasicBlock) else item.covered_blocks) if b.address >= 0)

        # One way in (this branch), nothing leaves the tail except by ending the function.
        for member in covered:
            if any(pred is not block and pred not in covered for pred in member.predecessors):
                return
            if any(succ not in covered for succ in member.successors):
                return

        if not any(not member.successors for member in covered):
            return

        # The branch's other edge must be the next thing that runs (inside this loop
        # body or `if` arm), as in the one-block case.
        if not self._falls_on_in(owner, block, other):
            return

        if not block.instructions or block.instructions[-1].terminator is not branch:
            return

        block.instructions.pop()
        block.terminator = None

        for item in tail:
            exit_owner.children.remove(item)
        exit_owner.invalidate_coverage()

        then_body = SequenceRegion()
        self.graph.transfer(list(tail), then_body)

        if_region = IfRegion()
        if_region.condition = branch.condition
        if_region.then_body = then_body
        if_region.else_body = None

        self.graph.insert_at(owner, owner.children.index(block) + 1, if_region)
        logger.debug("guard exit region: block %d takes %d items", block.id, len(tail))

    def _falls_on_in(self, owner, block: BasicBlock, follower: BasicBlock) -> bool:
        """Like `_falls_on_to`, and a loop body's end continues into the loop itself."""
        if self._falls_on_to(owner, block, follower):
            return True

        index = owner.children.index(block)

        if index + 1 < len(owner.children):
            return False

        parent = owner.parent
        return type(parent).__name__ == "LoopRegion" and follower in getattr(parent, "covered_blocks", ())

    def _try_jump_exit(self, owner: SequenceRegion, block: BasicBlock, jump) -> None:
        """`goto EXIT` as the last thing of an arm, EXIT only ending the function.

        An exit block that nothing else enters can stand where its one jump is.
        """
        exit_block = next((b for b in block.successors if b.address == jump.target), None)

        if (
                exit_block is None
                or len(block.successors) != 1
                or exit_block.successors
                or not (
                exit_block.terminator is None or isinstance(exit_block.terminator, (TerminatorReturn, TerminatorThrow)))
                or list(exit_block.predecessors) != [block]
                or exit_block.address <= block.address
                or owner.children[-1] is not block
                or not block.instructions
                or block.instructions[-1].terminator is not jump
        ):
            return

        exit_owner = self._holder(self.graph.root, exit_block)

        if exit_owner is owner:
            return

        block.instructions.pop()
        block.terminator = None

        # Not in the tree at all: an earlier pass took a lone `return` out of it
        # (a trailing one), leaving this jump pointing at nothing.
        if exit_owner is not None:
            exit_owner.children.remove(exit_block)
            exit_owner.invalidate_coverage()

        self.graph.insert_at(owner, owner.children.index(block) + 1, exit_block)
        logger.debug("jump exit: block %d takes %d", block.id, exit_block.id)

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
