from __future__ import annotations

import dataclasses

from hermes_decompiler.backend.analysis.cfg import BasicBlock
from hermes_decompiler.backend.regions import LoopKind, LoopRegion, RegionVisitor
from hermes_decompiler.ir import Node
from hermes_decompiler.ir.expressions import Identifier
from ._base import RegionPass


class _LoopConditionRegisterCollector(RegionVisitor):
    """One-time walk collecting, for every `LoopRegion` with a
    `condition_block`/`update_block`, the set of registers its
    `condition`/`update` expressions reference - keyed by whichever of
    those two blocks the expression came from.

    Exists purely to feed `DeadMovEliminationPass`'s liveness check -
    see that class's own docstring ("condition/update-block blind
    spot") for what this protects against.
    """

    def __init__(self) -> None:
        self.by_block: dict[BasicBlock, set[int]] = {}

    def visit_LoopRegion(self, node: LoopRegion) -> None:
        # `for...of` / `for...in` never PRINT `condition`/`update`
        # (`ForEachRegionPass` replaces them with the iterable/binding),
        # so whatever stale expression it left behind is not a real
        # read and must not keep otherwise-dead copies alive.
        if node.loop_kind in (LoopKind.FOR_OF, LoopKind.FOR_IN):
            self.visit(node.body)
            return

        for block, expr in (
                (node.condition_block, node.condition),
                (node.update_block, node.update),
        ):
            if block is None or expr is None:
                continue

            registers = self._registers_read(expr)

            if registers:
                self.by_block.setdefault(block, set()).update(registers)

        self.visit(node.body)

    @staticmethod
    def _registers_read(node) -> set[int]:
        """Same generic dataclass-tree walk `LoopConditionRegionPass.
        _registers_read` already uses to collect every register an
        `Expression` subtree reads - duplicated here rather than
        imported, matching this codebase's own precedent (see e.g.
        `LoopInductionAliasPass._repoint_node`'s docstring) of not
        reaching across pass modules for a few-line generic tree walk.
        """
        registers: set[int] = set()

        def visit(n) -> None:
            if isinstance(n, Identifier):
                if n.name.startswith("r") and n.name[1:].isdigit():
                    registers.add(int(n.name[1:]))
                return

            if not dataclasses.is_dataclass(n) or not isinstance(n, Node):
                return

            for field in dataclasses.fields(n):
                value = getattr(n, field.name)

                if isinstance(value, Node):
                    visit(value)
                elif isinstance(value, tuple):
                    for item in value:
                        if isinstance(item, Node):
                            visit(item)

        visit(node)
        return registers


class DeadMovEliminationPass(RegionPass):
    """Removes a `rN = rM;` register-copy instruction whose destination
    is never read before being overwritten (or the function ends).

    Hermes' own register allocator produces these routinely - a value
    gets copied into a register "just in case" (e.g. to keep an
    iterator reachable across a `try`/`finally` boundary a particular
    source shape never actually needed), and nothing in the source the
    bytecode came from ever reads it back out. Left in place, it
    prints as a pointless `rN = rM;` statement with no effect on
    anything that follows (see forOfTest/section_15092, whose loop
    body used to start with a dead `r4 = r3` immediately preceding the
    real `console.log(item)` call - `r4` gets overwritten two
    instructions later without ever being read).

    condition/update-block blind spot
    ----------------------------------
    `_is_dead_after`'s forward scan only ever looks at `block.
    instructions` - but `LoopConditionRegionPass` (much earlier in
    `StructuralAnalyzer`'s own pass order) already POPPED the
    conditional-branch instruction that USED to read the induction/
    boundary register out of `loop.condition_block.instructions`
    entirely, moving that read into `loop.condition` (a `LoopRegion`
    attribute, not any block's own instruction list) - likewise for
    `loop.update_block`/`loop.update`. A register whose ONLY read left
    behind was that one becomes invisible to a scan that never looks
    past `block.instructions`, and if the SAME register number happens
    to be reused for something else entirely later in the same
    function (an everyday occurrence - Hermes' allocator reuses
    registers aggressively once a value's original meaning is done
    with), that LATER, unrelated write reads as "redefined before
    ever read" - textbook dead-store shape, but wrong, since the
    read the scan can't see already happened, once every iteration.

    Confirmed bug (`tryLoopMultiReturnTest`): the loop's own header
    copies the induction register into a second one purely so the
    `while (...)` condition has a stable per-iteration alias to read
    (`r6 = r4;`, then `while (!(r6 >= r5))`) - by the time this pass
    ran, that read was already gone from the header block's own
    instructions (extracted into `loop.condition`), `r6` got reused a
    few blocks later for plain array indexing, and the alias copy
    silently vanished as "dead" - leaving `r6` referenced by the
    printed `while` condition with NO assignment anywhere in the
    function to give it a value. Not just noisier output: `r6` reads
    as `undefined` every time, so the loop's own top-of-loop check
    runs at most once correctly before misbehaving.

    `_LoopConditionRegisterCollector` (above) closes this blind spot:
    a one-time walk, before the main elimination loop starts, records
    which registers each loop's `condition_block`/`update_block`
    needs to treat as unconditionally live - checked FIRST in
    `_is_dead_after`, before the forward scan even begins, so a
    protected register is never removed regardless of what the scan
    would otherwise conclude.

    Deliberately narrow, for safety:

      - Only ever touches an instruction whose value is a bare
        `Identifier` referencing another register (`rN = rM` - a pure
        register copy) - never a literal, computed expression, or
        anything else, even though those could in principle also be
        dead. A copy is the one shape genuinely safe to reason about
        here: it can never have a side effect of its own, so removing
        it is always safe once its destination is confirmed dead.
      - "Dead" is checked via a simple SINGLE-successor forward walk,
        not full liveness analysis: starting right after the
        candidate instruction, scan forward (same block, then follow
        successors) for a read of the destination register, stopping
        as soon as either a read is found (not dead - keep it) or the
        register is redefined (dead - safe to remove, since nothing
        between the copy and the redefinition ever observed the
        stale value). The walk stops and treats the register as
        LIVE (i.e. does NOT remove the instruction) the moment it
        hits a block with more than one successor, or none at all
        without ever finding a read/redefinition - a branch or an
        unresolved tail means "might still be read on some path this
        pass didn't verify", and the conservative answer is to leave
        the instruction exactly as `strip_duplicate_run` and friends
        already do elsewhere in this codebase: a missed dead-store
        removal is a readability regression, a wrong one would be a
        correctness regression.
    """

    def run(self) -> None:
        collector = _LoopConditionRegisterCollector()
        collector.visit(self.graph.root)
        self._protected_registers = collector.by_block

        for block in list(self.graph.blocks()):
            for instr in list(block.instructions):

                if instr.terminator is not None:
                    continue

                if instr.dest_reg is None:
                    continue

                value = instr.value

                if not (
                        isinstance(value, Identifier)
                        and value.name.startswith("r")
                        and value.name[1:].isdigit()
                ):
                    continue

                if self._is_dead_after(block, instr, instr.dest_reg):
                    block.instructions.remove(instr)

    # -----------------------------------------------------------------

    def _is_dead_after(self, block: BasicBlock, after_instr, reg: int) -> bool:
        """True if `reg` is never read before being redefined, walking
        forward from immediately after `after_instr` - same block
        first, then following the STRUCTURED (region-tree) "what runs
        next" chain. See class docstring for the full safety
        rationale, including the `_protected_registers` check below -
        without it, this method has no way to see a read that a
        loop's own extracted `condition`/`update` still makes of `reg`
        once `LoopConditionRegionPass` has already removed the
        instruction that used to carry it out of `block`'s own
        instruction list.

        Deliberately follows region-tree sibling position
        (`self.graph.owner(block)` + its position in
        `SequenceRegion.children`), not `BasicBlock.successors`:
        successors reflect the RAW, pre-structuring CFG - a loop
        header block still carries two successors (body entry, loop
        exit) at the raw level even once structuring has long since
        resolved which one is "next" for any given position, so a
        successor-count check alone would treat nearly every loop
        header as an unresolvable branch and never confirm anything
        dead inside one.
        """
        if reg in self._protected_registers.get(block, ()):
            return False

        visited = set()

        start_index = block.instructions.index(after_instr) + 1

        return self._scan_block(block, start_index, reg, visited)

    def _scan_block(self, block: BasicBlock, start_index: int, reg: int, visited: set) -> bool:
        if block in visited:
            # Back-edge revisit with no resolution found yet on this
            # path - treat as live rather than loop forever or
            # over-claim deadness across an iteration boundary.
            return False

        visited.add(block)

        for instr in block.instructions[start_index:]:

            if self._reads_register(instr, reg):
                return False

            if instr.dest_reg == reg:
                # Redefined before ever being read on this path - the
                # candidate copy's value never escapes this point.
                return True

        next_block = self._next_sibling_block(block)

        if next_block is None:
            # No single, structurally-confirmed "what runs next" -
            # either genuinely the end of this sequence, or the next
            # item is a compound Region (If/Loop/Switch) this method
            # doesn't walk into. Either way, not enough to confirm
            # dead - stay conservative.
            return False

        return self._scan_block(next_block, 0, reg, visited)

    def _next_sibling_block(self, block: BasicBlock) -> BasicBlock | None:
        """Return the next DIRECT sibling in `block`'s own owning
        SequenceRegion, if - and only if - that sibling is itself a
        bare BasicBlock. A compound sibling (IfRegion/LoopRegion/...)
        or "no next sibling at all" both return None, deferring to
        the conservative "stay alive" default in `_scan_block`.
        """
        owner = self.graph.owner(block)

        if owner is None:
            return None

        try:
            index = owner.children.index(block)
        except ValueError:
            return None

        if index + 1 >= len(owner.children):
            return None

        candidate = owner.children[index + 1]

        return candidate if isinstance(candidate, BasicBlock) else None

    @staticmethod
    def _reads_register(instr, reg: int) -> bool:
        target = f"r{reg}"

        def walk(node) -> bool:
            if isinstance(node, Identifier):
                return node.name == target

            if hasattr(node, "__dataclass_fields__"):
                for field_name in node.__dataclass_fields__:
                    value = getattr(node, field_name)
                    if walk_value(value):
                        return True
                return False

            return False

        def walk_value(value) -> bool:
            if isinstance(value, (list, tuple)):
                return any(walk_value(item) for item in value)
            if hasattr(value, "__dataclass_fields__") or isinstance(value, Identifier):
                return walk(value)
            return False

        if instr.value is not None and walk_value(instr.value):
            return True

        if instr.statement is not None and walk_value(instr.statement):
            return True

        return False
