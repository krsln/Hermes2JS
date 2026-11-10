"""Puts the fall-through of a conditional branch right behind it, when only that branch enters it.

A conditional branch falls into the NEXT BLOCK IN THE LAYOUT (`successors == [taken, fall]`). The generator
dispatch orders the blocks topologically, lowest address first, and a block that other tests jump to (the
`requestPermission` tail of 98/12903, entered by two resume tests as well) comes after all of them, far from
the branch that falls into it. Printed as a raw `if (c) goto L;` the code behind the `goto` was then whatever
block happened to be next: the output ran the wrong code for `!c` (not just a `goto` too many).

Once a duplication pass has given the jumpers their own copies, the fall-through block has one predecessor and
can simply move behind its branch. A block that ends in a `return`/`throw`/jump does not depend on what follows
it, so moving it leaves nothing else broken.
"""

from __future__ import annotations

from hermes_decompiler.backend.analysis.cfg import CFG, BasicBlock
from hermes_decompiler.ir.terminators import TerminatorConditionalBranch, TerminatorJump, TerminatorReturn, \
    TerminatorThrow


class FallThroughLayoutCfgPass:
    def __init__(self, cfg: CFG):
        self.cfg = cfg

    def run(self) -> int:
        moved = 0

        for block in list(self.cfg.blocks):
            if not isinstance(block.terminator, TerminatorConditionalBranch) or len(block.successors) != 2:
                continue

            fall = block.successors[1]
            blocks = self.cfg.blocks
            at = blocks.index(block)

            if at + 1 < len(blocks) and blocks[at + 1] is fall:
                continue

            if fall.predecessors != [block] or fall is block:
                continue

            if not isinstance(fall.terminator, (TerminatorReturn, TerminatorThrow, TerminatorJump)):
                continue

            if any(handler.get("handler_block") is fall for handler in self.cfg.exception_handlers):
                continue

            blocks.remove(fall)
            blocks.insert(blocks.index(block) + 1, fall)
            moved += 1

        return moved

    def bridge_remaining(self, everywhere: bool = False) -> int:
        """A branch whose fall-through still is not the next block (a loop body entered by two tests has to precede
        the `return` the first test falls into: 98/9673) would be read by the structurer as falling into the wrong
        block. Give it an empty block right behind it that jumps to the real fall-through.

        Without `everywhere` only a branch followed by a loop is bridged (the first attempts keep the layouts the
        duplication passes repair); the last rung bridges every such branch."""
        blocks = self.cfg.blocks
        base = max(b.address for b in blocks) + 1
        first_id = max(b.id for b in blocks) + 1
        added = 0

        for block in list(blocks):
            if not isinstance(block.terminator, TerminatorConditionalBranch) or len(block.successors) != 2:
                continue

            at = blocks.index(block)
            fall = block.successors[1]

            if fall is block or (at + 1 < len(blocks) and blocks[at + 1] is fall):
                continue

            if at + 1 >= len(blocks):
                continue

            if not everywhere and not self._reaches(blocks[at + 1], [blocks[at + 1]], skip_start=True):
                continue

            bridge = BasicBlock(first_id + added, base + added)
            added += 1
            bridge.terminator = TerminatorJump(target=fall.address)
            bridge.successors = [fall]
            bridge.predecessors = [block]
            block.successors[1] = bridge
            fall.predecessors = [bridge if p is block else p for p in fall.predecessors]
            blocks.insert(at + 1, bridge)

        return added

    @staticmethod
    def _reaches(start: BasicBlock, targets, skip_start: bool = False) -> bool:
        """Whether `start` runs into one of `targets`; with `skip_start`, only by a path of at least one edge (so
        `start` itself counts when it lies on a cycle: the block laid out behind the branch is a loop)."""
        wanted = {id(t) for t in targets}
        seen: set[int] = set()
        stack = list(start.successors) if skip_start else [start]

        while stack:
            block = stack.pop()

            if id(block) in seen:
                continue
            seen.add(id(block))

            if id(block) in wanted:
                return True
            stack.extend(block.successors)

        return False
