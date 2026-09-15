from __future__ import annotations

from hermes_decompiler.backend.analysis.cfg import BasicBlock
from hermes_decompiler.ir.expressions import Identifier
from ._base import RegionPass


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
        rationale.

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
