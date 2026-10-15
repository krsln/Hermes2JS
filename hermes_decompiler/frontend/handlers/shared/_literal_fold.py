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

import dataclasses
import re
from typing import Callable

from hermes_decompiler.frontend.handlers import OpcodeContext
from hermes_decompiler.frontend.opcode import OpcodeResult
from hermes_decompiler.ir.expressions import (
    ArrayExpression,
    Expression,
    Identifier,
    MemberExpression,
    NullLiteral,
    NumericLiteral,
    ObjectExpression,
    ObjectProperty,
    StringLiteral,
    UndefinedLiteral,
)


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


# --- arrays ----------------------------------------------------------------

def fold_array_element(ctx: OpcodeContext, reg: int, index: int, value: Expression) -> OpcodeResult | None:
    """`arr[index] = value` as the next element of the array literal in `reg`.

    Only the next free index extends it: a gap would be a hole, not
    `undefined`.
    """
    return fold_into_literal(
        ctx, reg, ArrayExpression,
        lambda array: (
            ArrayExpression(elements=array.elements + (value,))
            if index == len(array.elements) else None
        ),
    )


# --- objects ---------------------------------------------------------------

_IDENTIFIER_NAME = re.compile(r"[A-Za-z_$][A-Za-z0-9_$]*")


def property_access(obj: Expression, name: str) -> MemberExpression:
    """`obj.name`, or `obj["name"]` when `name` is not an identifier name
    (`aria-label`, `a b`, ...), which `obj.name` could not express."""
    if _IDENTIFIER_NAME.fullmatch(name):
        return MemberExpression(obj=obj, prop=Identifier(name=name), computed=False)

    return MemberExpression(obj=obj, prop=StringLiteral(name), computed=True)


def object_property(key: Expression, value: Expression) -> ObjectProperty:
    """The literal property for a DEFINE of `key`.

    A plain key stays a plain key (`"k": v` / `1: v`); everything that is
    not one becomes a computed key `[expr]: v`:

    - `"__proto__"`: `{ "__proto__": v }` SETS THE PROTOTYPE, whereas the
      opcodes define an own data property - only the computed form
      `{ ["__proto__"]: v }` does that;
    - a non-literal key, or a number that is not a non-negative integer
      (`{ -1: v }` is not even valid JS).
    """
    if isinstance(key, StringLiteral):
        return ObjectProperty(key=key, value=value, computed=key.value == "__proto__")

    if isinstance(key, NumericLiteral) and float(key.value).is_integer() and key.value >= 0:
        return ObjectProperty(key=key, value=value)

    return ObjectProperty(key=key, value=value, computed=True)


def static_key(prop: ObjectProperty) -> str | None:
    """A property's key as a string, when it is known statically."""
    if prop.computed:
        return None

    if isinstance(prop.key, StringLiteral):
        return prop.key.value

    if isinstance(prop.key, NumericLiteral):
        return str(int(prop.key.value))

    return None


def fold_object_property(
        ctx: OpcodeContext, reg: int, key: Expression, value: Expression,
) -> OpcodeResult | None:
    """`obj[key] = value` (a DEFINE) as the next property of the object
    literal in `reg`. A key already present statically is not folded: keep
    the second store a statement instead of reasoning about literal
    duplicate-key rules."""
    prop = object_property(key, value)
    name = static_key(prop)

    return fold_into_literal(
        ctx, reg, ObjectExpression,
        lambda obj: (
            None if name is not None and any(static_key(p) == name for p in obj.properties)
            else ObjectExpression(properties=obj.properties + (prop,))
        ),
    )


# --- slot-indexed stores (hermes 98) -----------------------------------------

def slot_key(ctx: OpcodeContext, reg: int, slot: int) -> str | None:
    """The property name behind hidden-class slot `slot` of the object
    literal in `reg`.

    `PutOwnBySlotIdx` carries no name, only the slot. The slots of an object
    built by `NewObjectWithBuffer` are its buffer keys in order: over all
    15,173 slot stores in the hermes-98 bundle, 15,144 resolve this way, none
    is out of range, and where the stored value is a named function its name
    equals the key 93.7% of the time (the rest are plainly different names,
    `onPress: handlePress`).

    Declines (None) when the register does not hold a known literal, or when
    an index-like key makes the slot order differ from the source order.
    """
    state = ctx.analysis.get_register_state(reg)

    if state is None or not isinstance(state.value, ObjectExpression):
        return None

    props = state.value.properties
    names = [static_key(p) for p in props]

    if slot >= len(props) or names[slot] is None:
        return None

    if any(name is not None and name.isdigit() for name in names):
        return None

    return names[slot]


def fold_slot_value(ctx: OpcodeContext, reg: int, slot: int, value: Expression) -> OpcodeResult | None:
    """Fills the placeholder at `slot` of the object literal in `reg`
    (`{ "start": null, ... }` -> `{ "start": start, ... }`).

    The compiler puts `null` in the buffer for every property whose value is
    not a constant, then stores the real value by slot; only such a
    placeholder is replaced."""

    def extend(obj: ObjectExpression) -> ObjectExpression | None:
        props = obj.properties

        if slot >= len(props) or not isinstance(props[slot].value, (NullLiteral, UndefinedLiteral)):
            return None

        if slot_key(ctx, reg, slot) is None:
            return None

        return ObjectExpression(
            properties=props[:slot] + (dataclasses.replace(props[slot], value=value),) + props[slot + 1:],
        )

    return fold_into_literal(ctx, reg, ObjectExpression, extend)
