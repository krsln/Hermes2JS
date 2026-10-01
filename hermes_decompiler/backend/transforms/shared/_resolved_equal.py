from __future__ import annotations

import dataclasses

from ._reaching_definition import is_bare_register, resolve_identifier
from ._structural_key import structural_key

__all__ = ["resolved_structural_equal"]

# A bare-register aliasing chain longer than this is treated as outside
# the "clean single-assignment" shape resolve_identifier targets, the
# same conservative bailout resolve_identifier itself applies to a
# single hop - see that function's own docstring.
_MAX_RESOLUTION_DEPTH = 4


def resolved_structural_equal(
        a, a_instr, a_block,
        b, b_instr, b_block,
        *, _depth: int = 0,
) -> bool:
    """Structural equality between two expression trees, treating a
    bare `rN` register reference on EITHER side as equal to the other
    side whenever it resolves (via `resolve_identifier`, walking
    backward from `a_instr`/`a_block` or `b_instr`/`b_block`
    respectively) to something the other side matches.

    Exists for the same reason `resolve_identifier` does: Hermes'
    `finally`-duplication routinely re-derives the "same" logical
    value through a different physical register at each copy - e.g.
    one copy reads a `Mov`-aliased register while the other reads the
    original parameter register directly (see
    tryCatchFinallyBranchInFinallyTest's raw disassembly). Plain
    `structural_key` equality, which compares registers by their
    literal name, then never recognizes the two copies as the same
    content, and a wider handler that's really a `finally` wrapper
    stays mis-recognized as an ordinary, independent handler.

    Falls straight back to `structural_key` equality whenever neither
    side is a still-bare register - the common case - so this is only
    ever more permissive than plain equality, never less. Recurses
    through dataclass fields and list/tuple structure the same way
    `structural_key` does, but needs a real tree walk (rather than
    reducing each side to an independent hashable key first) because
    resolution can only be tried once we know exactly which leaf, in
    which side's context, disagreed.

    Depth-bounded (`_MAX_RESOLUTION_DEPTH`) to guard against an
    unexpected resolution cycle; only resolution hops count against
    the bound; plain tree descent does not, so this is never
    reached for a deep-but-otherwise-ordinary expression tree.
    """

    if structural_key(a) == structural_key(b):
        return True

    a_is_reg = is_bare_register(a)
    b_is_reg = is_bare_register(b)

    if a_is_reg or b_is_reg:
        if _depth >= _MAX_RESOLUTION_DEPTH:
            return False

        resolved_a = resolve_identifier(a, a_instr, a_block) if a_is_reg else a
        resolved_b = resolve_identifier(b, b_instr, b_block) if b_is_reg else b

        if resolved_a is a and resolved_b is b:
            # Neither side actually resolved to anything new - a bare
            # register with no reaching definition found, on the side(s)
            # that needed one. Nothing further to try.
            return False

        return resolved_structural_equal(
            resolved_a, a_instr, a_block,
            resolved_b, b_instr, b_block,
            _depth=_depth + 1,
        )

    if type(a) is not type(b):
        return False

    if dataclasses.is_dataclass(a) and not isinstance(a, type):
        return all(
            resolved_structural_equal(
                getattr(a, f.name), a_instr, a_block,
                getattr(b, f.name), b_instr, b_block,
                _depth=_depth,
            )
            for f in dataclasses.fields(a)
        )

    if isinstance(a, (list, tuple)):
        if len(a) != len(b):
            return False
        return all(
            resolved_structural_equal(x, a_instr, a_block, y, b_instr, b_block, _depth=_depth)
            for x, y in zip(a, b)
        )

    return a == b
