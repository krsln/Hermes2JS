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

from hermes_decompiler.backend.analysis.cfg import CFG
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
