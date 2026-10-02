"""
Shared safety logic for building array / object literals one element at a
time (`NewArray` + `PutOwnByIndex`, `NewObject` + `PutNewOwnById`, ...).

The element stores arrive as separate instructions, so each one has to be
folded into the literal that is "in progress" in its register:

    NewObject r5; PutNewOwnById r5, a, 'x'; PutNewOwnById r5, b, 'y'
        -> r5 = { "x": a, "y": b }

Folding is only exactly equivalent when nothing could have observed or
interleaved with the intermediate literal, which is what `fold_into_literal`
checks. When it cannot fold, the caller prints a plain `rN.k = v` statement
(which defines nothing) - always correct, just less compact.
"""

from __future__ import annotations

from typing import Callable

from hermes_decompiler.frontend.handlers import OpcodeContext
from hermes_decompiler.frontend.opcode import OpcodeResult
from hermes_decompiler.ir.expressions import Expression


def fold_into_literal(
        ctx: OpcodeContext,
        reg: int,
        literal_type: type,
        extend: Callable[[Expression], Expression | None],
) -> OpcodeResult | None:
    """Replaces `reg`'s in-progress literal with `extend(literal)`.

    Returns the new definition (already added to the analysis), or None when
    folding is not safe or `extend` declines (it returns None for an element
    that cannot be appended, e.g. a gap in an array, a duplicate object key).

    Folding requires that

    - `reg` still holds a `literal_type` literal that no one has read,
      pinned, or folded into a consumer (nothing observed the intermediate
      value, so replacing it is invisible);
    - since that literal was created nothing else happened: no control flow
      and no PRINTED statement. Then evaluating the element here instead of
      at its original position reorders nothing. (An element that is itself
      a printed definition, e.g. a call result `r4 = f()`, therefore blocks
      the fold, and so does anything else with an effect.)

    Callers must resolve the element's expression BEFORE calling this: that
    marks the element's own definition as folded (`definition_used`), which
    is what the "nothing printed since" scan expects.

    The previous definition's statement is suppressed; the new one (printed
    where the current store is) carries the longer literal.
    """
    state = ctx.analysis.get_register_state(reg)

    if state is None or not isinstance(state.value, literal_type):
        return None

    previous = state.definition

    if state.reads != 0 or previous.definition_pinned or previous.definition_used:
        return None

    results = ctx.analysis.results
    start = next((i for i in range(len(results) - 1, -1, -1) if results[i] is previous), None)

    if start is None:
        return None

    for later in results[start + 1:]:
        if later.terminator is not None or not later.definition_used:
            return None

    extended = extend(state.value)

    if extended is None:
        return None

    previous.definition_used = True

    result = OpcodeResult(ctx.entry, value=extended, dest_reg=reg)
    ctx.analysis.add_result(result)

    return result
