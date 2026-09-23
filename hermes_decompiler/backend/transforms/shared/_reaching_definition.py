from __future__ import annotations

from collections import deque

from hermes_decompiler.backend.analysis.cfg import BasicBlock
from hermes_decompiler.ir import Expression
from hermes_decompiler.ir.expressions import Identifier
from ._structural_key import structural_key

__all__ = ["resolve_identifier", "is_bare_register"]


def is_bare_register(expr) -> bool:
    """True for an `Identifier` that's still a literal `rN` register
    reference rather than a real, named JS-visible identifier."""

    return (
            isinstance(expr, Identifier)
            and expr.name.startswith("r")
            and expr.name[1:].isdigit()
    )


def resolve_identifier(expr: Expression, before_instr, before_block: BasicBlock):
    """Resolve a possibly-still-bare register reference to its defining expression.

    Extracted from `ForEachRegionPass._resolve_identifier` (see that
    method's own docstring for the full rationale) into a standalone,
    reusable helper - it never depended on any pass-instance state to
    begin with. `ForEachRegionPass` now delegates to this.

    Some handlers inline a register's defining expression directly
    (get_register_expression - e.g., IteratorNext's iterator,
    IteratorClose's .return() receiver), others deliberately keep
    a bare register reference (get_register_reference - e.g.,
    GetNextPName's list_val, to avoid re-embedding a large or
    side-effecting expression at every .next() call site).

    Resolves a bare r{N} reference to the register's REACHING
    definition at the point of use (before_block/before_instr) - not
    just any definition found anywhere in the function:

      1. Scan before_block's own instructions strictly before
         before_instr, in reverse, for a write to `reg`.
      2. If not found, do a backward BFS over EVERY predecessor
         path from before_block (not just a unique-predecessor
         chain - before_block is very often a loop header or a
         `finally` block, both of which always have more than one
         predecessor: an outside entry edge plus one or more
         in-loop back/exceptional edges - requiring a single
         predecessor would bail out immediately on exactly the
         shapes this is meant to target). Each path stops exploring
         further back as soon as it finds ANY write to `reg`,
         collecting that value.

    The register is only resolved if every path that found a
    definition agrees, via structural_key, on the same value. The
    single-assignment assumption above means genuine matches
    always agree here regardless of how many paths were walked
    (a loop's back edge never redefines the pre-loop setup
    register, so exploring through it just contributes nothing,
    not a conflicting value); a real structural disagreement means
    this isn't the simple shape this helper targets after all, so it
    bails rather than guessing which path is "the" reaching
    definition. Returns expr unchanged in that case, or if no path
    finds a definition at all.
    """
    if not is_bare_register(expr):
        return expr

    reg = int(expr.name[1:])

    # 1. Same block, strictly before before_instr.
    found = _find_definition_in_instructions(
        before_block.instructions, reg, stop_before=before_instr
    )
    if found is not None:
        return found

    # 2. Backward BFS over every predecessor path.
    visited = {before_block}
    queue = deque(before_block.predecessors)
    found_values = []

    while queue:
        block = queue.popleft()

        if block in visited:
            continue
        visited.add(block)

        value = _find_definition_in_instructions(block.instructions, reg)

        if value is not None:
            found_values.append(value)
            # Don't look further back past a definition on this path.
            continue

        queue.extend(block.predecessors)

    if not found_values:
        return expr

    first = found_values[0]

    for other in found_values[1:]:
        if structural_key(other) != structural_key(first):
            # Different paths reach different definitions - not
            # the clean single-assignment shape this helper targets.
            return expr

    return first


def _find_definition_in_instructions(instructions, reg: int, stop_before=None):
    """Scan `instructions` in reverse for the most recent write to `reg`.

    If `stop_before` is given, only instructions strictly before it
    (in list order) are considered - used to search "everything
    before the use site" within before_block itself.
    """
    if stop_before is not None:
        try:
            cutoff = instructions.index(stop_before)
        except ValueError:
            cutoff = len(instructions)
        instructions = instructions[:cutoff]

    for instr in reversed(instructions):
        if instr.dest_reg == reg and instr.value is not None:
            return instr.value

    return None
