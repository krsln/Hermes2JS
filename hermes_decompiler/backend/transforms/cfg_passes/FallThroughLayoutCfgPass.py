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

import dataclasses

from hermes_decompiler.backend.transforms.shared import negate_condition
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

    def relocate_terminal_tails(self, loop_stubs: bool = False) -> int:
        """`if (c) goto TAIL` where the code behind TAIL is entered by this branch alone and never comes back
        (every path ends in a `return`/`throw`), and the compiler laid it out after the function's closing return
        (98/12534 `pipeTo`: the `signal.aborted` branch, `abortAlgorithm(); return;` inlined at the very end).

        It is an `if (c) { tail }`: the tail moves right behind the branch, which is inverted to jump over it to the
        code it used to fall into. The tail's own blocks keep their order, so their fall-throughs stay intact.

        With `loop_stubs` a tail may also end in the jump back to the loop header (a `continue`), and a branch inside
        one `try` (the `for ... of` iterator close) may move it: 98/8045 lays the `transitionDuration` and
        `transitionDelay` stores behind the shared `timing function` code the tests fall through to."""
        # A branch or tail a handler guards or starts at stays where it is; the rest of a function that has
        # handlers moves like any other (96/3448: the abort test sits before the `try`).
        if self.cfg.exception_handlers and getattr(self.cfg, "unresolved_dispatch", False):
            return 0

        handler_blocks = {handler["handler_block"] for handler in self.cfg.exception_handlers}
        protected = {
            block
            for handler in self.cfg.exception_handlers
            for block in (*handler["try_blocks"], handler["handler_block"])
        }

        moved = 0
        relocated: list[BasicBlock] = []

        # A branch whose fall-through only leads on to a relocated one moves with it (the nest stays readable), which
        # takes a later round: the inner branch has to be placed first.
        for _ in range(4 if loop_stubs else 1):
            before = moved
            moved += self._relocate_round(loop_stubs, handler_blocks, protected, relocated)

            if moved == before:
                break

        return moved

    def _relocate_round(self, loop_stubs, handler_blocks, protected, relocated) -> int:
        moved = 0

        for block in list(self.cfg.blocks):
            if not isinstance(block.terminator, TerminatorConditionalBranch) or len(block.successors) != 2:
                continue

            if block in (handler_blocks if loop_stubs else protected):
                continue

            taken, fall = block.successors
            blocks = self.cfg.blocks
            at = blocks.index(block)

            if taken is block or fall is block or blocks.index(taken) <= at + 1 or taken.predecessors != [block]:
                continue

            tail = self._closed_tail(taken, block, loop_stubs)

            if tail is None or fall in tail or blocks.index(fall) != at + 1:
                continue

            # Only a stub that sits behind code ANOTHER branch also enters: the structurer reads that code as the
            # fall-through arm's join and has no place for the stub (a lone fall-through nests the stub fine).
            # A test that falls into this branch and jumps to the same code is the first half of `a && b`: the
            # short-circuit fold reads that layout as it is.
            if loop_stubs and (
                    (len(fall.predecessors) < 2 and fall not in relocated)
                    or any(pred is not block and block in pred.successors for pred in fall.predecessors)
            ):
                continue

            # Inside one `try` the move changes nothing for the handler: the branch, the tail and the code it
            # falls into are guarded by the same handlers (the `for ... of` iterator close of 98/8045).
            if tail & protected and not (loop_stubs and self._same_guards(block, tail)):
                continue

            tail_blocks = [b for b in blocks if b in tail]

            for tail_block in tail_blocks:
                blocks.remove(tail_block)

            at = blocks.index(block)
            blocks[at + 1:at + 1] = tail_blocks

            if loop_stubs:
                # A loop body is ordered by block id; `follows` keeps the moved stub behind its branch there too.
                for tail_block in tail_blocks:
                    tail_block.follows = block

            terminator = dataclasses.replace(
                block.terminator, condition=negate_condition(block.terminator.condition), target=fall.address
            )
            block.terminator = terminator
            if block.instructions:
                block.instructions[-1].terminator = terminator
            block.successors = [fall, taken]
            relocated.append(block)
            moved += 1

        return moved

    def _same_guards(self, branch: BasicBlock, tail: set[BasicBlock]) -> bool:
        """Every block of `tail`, and the block the branch falls into, sits in the `try` blocks of exactly the
        handlers the branch does."""
        fall = branch.successors[1]

        return all(
            all((b in handler["try_blocks"]) == (branch in handler["try_blocks"]) for b in (*tail, fall))
            for handler in self.cfg.exception_handlers
        )

    @staticmethod
    def _closed_tail(entry: BasicBlock, branch: BasicBlock, loop_stubs: bool = False) -> set[BasicBlock] | None:
        """The blocks reached from `entry`, when nothing else enters them and they all end the function."""
        tail: set[BasicBlock] = set()
        stack = [entry]

        while stack:
            block = stack.pop()

            if block in tail:
                continue

            if block is branch:
                return None

            tail.add(block)

            if not block.successors and not isinstance(block.terminator, (TerminatorReturn, TerminatorThrow)):
                return None

            # A stub that ends in the jump back to the loop header (`continue`) closes the tail as well: it never
            # runs into the code the branch falls into (98/8045: the `transitionDelay` store).
            if loop_stubs and isinstance(block.terminator, TerminatorJump) and block.successors \
                    and block.successors[0].address <= branch.address and block.successors[0] not in tail:
                continue

            stack.extend(block.successors)

        for block in tail:
            for pred in block.predecessors:
                if pred not in tail and not (block is entry and pred is branch):
                    return None

        return tail
