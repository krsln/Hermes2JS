"""
Gives the test that skips a shared tail its own copy of it.

Hermes lays out `c ? x : y` / `a && b ? x : y` so that one small block is
reached both by jumps from several tests and by falling through the last
test, which jumps over it:

    if (!a) goto T;          // jumper
    if (!b) goto T;          // jumper
    ...
    if (c) goto END;         // P: skips T when c holds
    T: r0 = typeof a         // reached by the jumpers and by P's fall-through
    END: return r0

Neither arm owns `T`, so the structurers hand it to one test and the other
test loses its exit (a dropped `if`, or a raw `goto`). The block P falls
into gets a private copy placed right behind it; the jumpers keep the
original. Only a short run of plain instructions is copied, and never in a
function with exception handlers (a copy sits outside every try range).

The tail may also be a small forward region of a few blocks with an inner
test (`b != null ? b : null` after a `??`, 98/1871): every block in it
leaves only to a block of the region or to the single block `END` the
skipping test jumps to, and nothing outside enters it except by a forward
jump onto its first block.
"""

from __future__ import annotations

import copy
import dataclasses

from hermes_decompiler.backend.analysis.cfg import BasicBlock, CFG
from hermes_decompiler.backend.transforms.shared import repoint_node
from hermes_decompiler.ir.expressions import Identifier
from hermes_decompiler.ir.terminators import TerminatorConditionalBranch, TerminatorJump


class SharedTailDuplicationCfgPass:
    _MAX_INSTRUCTIONS = 12
    _MAX_REGION_BLOCKS = 4

    def __init__(self, cfg: CFG, regions: bool = False, per_predecessor: bool = False):
        self.cfg = cfg
        # `per_predecessor`: a small tail entered by a fall-through AND by jumps, while an EARLIER
        # test of the same chain skips it, gets one private copy per way in (98/2216 `getScriptURL`:
        # `r3 = r5` after the `file://` test). The last resort, run only when nothing else
        # structured the function.
        self.per_predecessor = per_predecessor
        # `regions`: also copy a tail of several blocks. Kept to the last
        # resort: on functions that structure fine without it, the copy
        # only breaks `||`/`&&` chains apart (96/7424) or loses a clamp
        # (98/14169).
        self.regions = regions

    def run(self) -> int:
        if self.cfg.exception_handlers:
            return 0

        copied = 0

        for tail in list(self.cfg.blocks):
            faller = self._faller_that_skips(tail)

            if faller is not None:
                self._give_private_copy(faller, tail)
                copied += 1
                continue

            found = self._region_that_skips(tail) if self.regions else None

            if found is not None:
                self._give_private_region_copy(*found)
                copied += 1
                continue

            if self.per_predecessor and self._split_per_predecessor(tail):
                copied += 1

        return copied

    def _faller_that_skips(self, tail: BasicBlock) -> BasicBlock | None:
        if len(tail.instructions) > self._MAX_INSTRUCTIONS or len(tail.predecessors) < 2:
            return None
        if tail.terminator is not None and not isinstance(tail.terminator, TerminatorJump):
            return None
        if len(tail.successors) != 1 or tail.successors[0].address <= tail.address:
            return None
        if any(i.terminator is not None and i.terminator is not tail.terminator for i in tail.instructions):
            return None

        blocks = self.cfg.blocks
        index = blocks.index(tail)

        if index == 0:
            return None

        faller = blocks[index - 1]
        branch = faller.terminator

        if not isinstance(branch, TerminatorConditionalBranch) or faller not in tail.predecessors:
            return None
        if branch.target != tail.successors[0].address or branch.target <= faller.address:
            return None
        if faller.address >= tail.address - 1:
            return None

        # Every other way in is a forward jump onto the tail.
        for pred in tail.predecessors:
            if pred is faller:
                continue
            terminator = pred.terminator
            if not isinstance(terminator, (TerminatorJump, TerminatorConditionalBranch)):
                return None
            if terminator.target != tail.address or terminator.target <= pred.address:
                return None

        return faller

    def _give_private_copy(self, faller: BasicBlock, tail: BasicBlock) -> None:
        blocks = self.cfg.blocks
        end = tail.successors[0]

        clone = BasicBlock(max(b.id for b in blocks) + 1, tail.address - 1)

        for instruction in tail.instructions:
            duplicate = copy.copy(instruction)
            # Passes tell writers apart by the identity of the value they hold.
            duplicate.value = copy.deepcopy(instruction.value)
            duplicate.statement = copy.deepcopy(instruction.statement)
            if instruction.terminator is not None:
                duplicate.terminator = copy.copy(instruction.terminator)
            clone.instructions.append(duplicate)

        if tail.instructions and tail.instructions[-1].terminator is tail.terminator:
            clone.terminator = clone.instructions[-1].terminator
        else:
            clone.terminator = TerminatorJump(target=end.address)

        faller.successors = [clone if s is tail else s for s in faller.successors]
        tail.predecessors.remove(faller)
        clone.predecessors.append(faller)
        clone.successors.append(end)
        end.predecessors.append(clone)

        blocks.insert(blocks.index(tail), clone)

    # -- tails of several blocks -------------------------------------------------

    def _region_that_skips(self, tail: BasicBlock):
        """`(faller, region, end)` when the blocks from `tail` up to (not
        including) the target of the test in front of it form a small forward
        region, reached by a fall-through from that test and by forward jumps
        onto `tail` only."""
        blocks = self.cfg.blocks
        index = blocks.index(tail)

        if index == 0 or len(tail.predecessors) < 2:
            return None

        faller = blocks[index - 1]
        branch = faller.terminator

        if not isinstance(branch, TerminatorConditionalBranch) or faller not in tail.predecessors:
            return None
        if branch.target <= tail.address:
            return None

        region = []
        for block in blocks[index:]:
            if block.address >= branch.target:
                break
            region.append(block)

        if not 2 <= len(region) <= self._MAX_REGION_BLOCKS:
            return None

        end = next((b for b in blocks if b.address == branch.target), None)
        if end is None or end.address != blocks[index + len(region)].address:
            return None

        if sum(len(b.instructions) for b in region) > self._MAX_INSTRUCTIONS:
            return None

        # Room for one address per copied block between the test and the tail.
        if faller.address >= tail.address - len(region):
            return None

        inside = set(region)
        reaches_end = False

        for position, block in enumerate(region):
            terminator = block.terminator

            if terminator is not None and not isinstance(terminator, (TerminatorJump, TerminatorConditionalBranch)):
                return None
            if any(i.terminator is not None and i.terminator is not terminator for i in block.instructions):
                return None

            last = position == len(region) - 1
            if last and isinstance(terminator, TerminatorConditionalBranch):
                return None  # its fall-through would reach the tail, not `END`

            for successor in block.successors:
                if successor is end:
                    reaches_end = True
                elif successor not in inside:
                    return None
                if successor.address <= block.address:
                    return None

            for pred in block.predecessors:
                if block is tail:
                    if pred is faller:
                        continue
                    pred_terminator = pred.terminator
                    if not isinstance(pred_terminator, (TerminatorJump, TerminatorConditionalBranch)):
                        return None
                    if pred_terminator.target != tail.address or pred_terminator.target <= pred.address:
                        return None
                elif pred not in inside:
                    return None

        if not reaches_end:
            return None

        return faller, region, end

    def _give_private_region_copy(self, faller: BasicBlock, region: list[BasicBlock], end: BasicBlock) -> None:
        blocks = self.cfg.blocks
        first_id = max(b.id for b in blocks) + 1
        base = region[0].address - len(region)

        clones = {
            block: BasicBlock(first_id + n, base + n)
            for n, block in enumerate(region)
        }
        new_address = {block.address: clones[block].address for block in region}

        for block in region:
            clone = clones[block]
            retargeted = None

            if isinstance(block.terminator, (TerminatorJump, TerminatorConditionalBranch)):
                retargeted = dataclasses.replace(
                    block.terminator,
                    target=new_address.get(block.terminator.target, block.terminator.target),
                )

            for instruction in block.instructions:
                duplicate = copy.copy(instruction)
                duplicate.value = copy.deepcopy(instruction.value)
                duplicate.statement = copy.deepcopy(instruction.statement)
                if instruction.terminator is not None:
                    duplicate.terminator = retargeted
                clone.instructions.append(duplicate)

            if retargeted is not None:
                clone.terminator = retargeted
            elif block is region[-1]:
                clone.terminator = TerminatorJump(target=end.address)
            else:
                clone.terminator = None

            clone.successors = [clones.get(s, s) for s in block.successors]

            for successor in clone.successors:
                successor.predecessors.append(clone)

        first = clones[region[0]]
        faller.successors = [first if s is region[0] else s for s in faller.successors]
        region[0].predecessors.remove(faller)
        first.predecessors.append(faller)

        position = blocks.index(region[0])
        blocks[position:position] = [clones[b] for b in region]

    # -- one copy per way in -------------------------------------------------------

    def _split_per_predecessor(self, tail: BasicBlock) -> bool:
        blocks = self.cfg.blocks

        if tail not in blocks or len(tail.predecessors) < 3 or len(tail.instructions) > 3:
            return False
        if tail.terminator is not None and not isinstance(tail.terminator, TerminatorJump):
            return False
        if any(i.terminator is not None and i.terminator is not tail.terminator for i in tail.instructions):
            return False
        if len(tail.successors) != 1 or tail.successors[0].address <= tail.address:
            return False

        index = blocks.index(tail)
        end = tail.successors[0]
        faller = blocks[index - 1] if index else None

        if faller is None or faller not in tail.predecessors or isinstance(faller.terminator,
                                                                           TerminatorConditionalBranch):
            return False

        jumpers = [p for p in tail.predecessors if p is not faller]
        for pred in jumpers:
            terminator = pred.terminator
            if not isinstance(terminator, (TerminatorJump, TerminatorConditionalBranch)):
                return False
            if terminator.target != tail.address or terminator.target <= pred.address:
                return False

        # An earlier test skips the tail altogether: otherwise it is an ordinary join.
        if not any(
                isinstance(b.terminator, (TerminatorJump, TerminatorConditionalBranch))
                and b.terminator.target == end.address and b.address < tail.address and b is not tail
                for b in blocks
        ):
            return False

        ways = [faller, *jumpers]
        if any(tail.address - len(ways) <= b.address < tail.address for b in blocks):
            return False  # no free addresses in front of the tail

        first_id = max(b.id for b in blocks) + 1
        clones = []

        for n, pred in enumerate(ways):
            clone = BasicBlock(first_id + n, tail.address - len(ways) + n)

            for instruction in tail.instructions:
                duplicate = copy.copy(instruction)
                duplicate.value = copy.deepcopy(instruction.value)
                duplicate.statement = copy.deepcopy(instruction.statement)
                duplicate.terminator = None
                clone.instructions.append(duplicate)

            clone.terminator = TerminatorJump(target=end.address)
            clone.successors = [end]
            end.predecessors.append(clone)
            clone.predecessors.append(pred)
            clones.append(clone)

            if pred is faller:
                pred.successors = [clone if s is tail else s for s in pred.successors]
            else:
                retargeted = dataclasses.replace(pred.terminator, target=clone.address)
                for instruction in pred.instructions:
                    if instruction.terminator is pred.terminator:
                        instruction.terminator = retargeted
                pred.terminator = retargeted
                pred.successors = [clone if s is tail else s for s in pred.successors]

        self._name_the_register_after_the_join(tail, clones, blocks)

        position = blocks.index(tail)
        blocks[position:position + 1] = clones
        end.predecessors.remove(tail)
        tail.predecessors.clear()
        tail.successors.clear()

        return True

    @staticmethod
    def _name_the_register_after_the_join(tail: BasicBlock, clones: list[BasicBlock], blocks) -> None:
        """Every copy writes the register now, so a read after the join names it.

        IR generation froze the tail's value straight into the readers after it (`r4[5] = <value>`):
        that is one path's value. With a copy on every way in, the readers say `rN` and each copy
        prints its own write (98/2216: `r3 = r5` on three paths, `r3 = null` on a fourth)."""
        for instruction in tail.instructions:
            if instruction.dest_reg is None or instruction.value is None:
                continue

            old = instruction.value
            replacement = Identifier(name=f"r{instruction.dest_reg}")
            readers = 0

            for block in blocks:
                if block is tail or block in clones:
                    continue

                for other in block.instructions:
                    if other.value is not None and _holds(other.value, old):
                        other.value = repoint_node(other.value, old, replacement, structural=False)[0]
                        readers += 1
                    if other.statement is not None and _holds(other.statement, old):
                        other.statement = repoint_node(other.statement, old, replacement, structural=False)[0]
                        readers += 1
                    terminator = other.terminator
                    if terminator is not None and terminator is block.terminator and _holds(terminator, old):
                        updated = repoint_node(terminator, old, replacement, structural=False)[0]
                        other.terminator = updated
                        block.terminator = updated
                        readers += 1

            if readers:
                for clone in clones:
                    for duplicate in clone.instructions:
                        if duplicate.dest_reg == instruction.dest_reg:
                            duplicate.definition_used = False


def _holds(node, target) -> bool:
    if node is target:
        return True
    if not dataclasses.is_dataclass(node):
        return False

    for field in dataclasses.fields(node):
        child = getattr(node, field.name)
        children = child if isinstance(child, tuple) else (child,)
        if any(c is not None and not isinstance(c, (str, int, float, bool)) and _holds(c, target) for c in children):
            return True

    return False
