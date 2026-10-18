"""
Decoding of the `TypeOfIsTypes` bitmask carried by `TypeOfIs` / `JmpTypeOfIs`.

The bit assignment is MEASURED, not guessed: `hermesc` (bytecode 98,
`hermes-compiler@250829098.0.14`) compiles

    typeof x === "undefined"  -> TypeOfIs ..., 1
    typeof x === "string"     -> TypeOfIs ..., 4
    typeof x === "symbol"     -> TypeOfIs ..., 8
    typeof x === "boolean"    -> TypeOfIs ..., 16
    typeof x === "number"     -> TypeOfIs ..., 32
    typeof x === "bigint"     -> TypeOfIs ..., 64
    typeof x === "function"   -> TypeOfIs ..., 128
    typeof x === "object"     -> TypeOfIs ..., 258      (2 | 256)
    typeof x !== "object"     -> TypeOfIs ..., 253      (511 & ~258)

so bit 1 and bit 8 are the two halves of `typeof x === "object"`: `null`
and a non-null object. A mask carrying both is exactly `typeof x ===
"object"`; a mask carrying only one of them is not a plain `typeof` test
and is decoded as `x === null` / `typeof x === "object" && x !== null`
(never produced by hermesc for ordinary source - only the combined form was
observed).

Hbc96 has no `TypeOfIs`/`JmpTypeOfIs` opcodes at all, so this only ever runs
on 98+ bundles.
"""
from __future__ import annotations

from hermes_decompiler.ir.Operators import BinaryOperator, LogicalOperator, UnaryOperator
from hermes_decompiler.ir.expressions import (
    BinaryExpression,
    Expression,
    NullLiteral,
    StringLiteral,
    UnaryExpression,
)

__all__ = ["build_typeof_condition", "TYPEOF_NAME_BITS", "NULL_BIT", "OBJECT_BIT"]

NULL_BIT = 1 << 1
OBJECT_BIT = 1 << 8

# bit -> the `typeof` result string it stands for (null/object handled apart).
TYPEOF_NAME_BITS: dict[int, str] = {
    1 << 0: "undefined",
    1 << 2: "string",
    1 << 3: "symbol",
    1 << 4: "boolean",
    1 << 5: "number",
    1 << 6: "bigint",
    1 << 7: "function",
}

_ALL_BITS = NULL_BIT | OBJECT_BIT | sum(TYPEOF_NAME_BITS)


def _typeof_is(value: Expression, name: str, operator: BinaryOperator) -> Expression:
    return BinaryExpression(
        left=UnaryExpression(operator=UnaryOperator.TYPEOF, operand=value),
        operator=operator,
        right=StringLiteral(value=name),
    )


def _names(mask: int) -> list[str] | None:
    """The `typeof` result strings `mask` covers, in bit order; `None` when it
    holds just one of the null/object halves (no plain `typeof` form)."""
    has_null = bool(mask & NULL_BIT)
    has_object = bool(mask & OBJECT_BIT)

    if has_null != has_object:
        return None

    names = [name for bit, name in TYPEOF_NAME_BITS.items() if mask & bit]

    if has_null:
        names.append("object")

    return names


def _chain(terms: list[Expression], operator: LogicalOperator) -> Expression:
    result = terms[0]

    for term in terms[1:]:
        result = BinaryExpression(result, operator, term)

    return result


def build_typeof_condition(value: Expression, mask: int) -> Expression:
    """`typeof value` is in `mask`, as a boolean expression.

    One covered type reads `typeof x === "t"`; a mask covering most types is
    written as the negation of its complement (`typeof x !== "object"` for 253
    instead of a seven-way `||`)."""
    if mask <= 0 or mask & ~_ALL_BITS:
        return _typeof_is(value, f"<unresolved_typeof_mask_0x{mask:04x}>", BinaryOperator.STRICT_EQUAL)

    names = _names(mask)
    complement = _names(_ALL_BITS & ~mask)

    if names is not None and complement is not None and complement and len(complement) < len(names):
        return _chain(
            [_typeof_is(value, name, BinaryOperator.STRICT_NOT_EQUAL) for name in complement],
            LogicalOperator.AND,
        )

    if names is not None:
        return _chain([_typeof_is(value, name, BinaryOperator.STRICT_EQUAL) for name in names], LogicalOperator.OR)

    # Only one of the null/object halves is set: spell the two out.
    terms: list[Expression] = [
        _typeof_is(value, name, BinaryOperator.STRICT_EQUAL)
        for bit, name in TYPEOF_NAME_BITS.items()
        if mask & bit
    ]

    if mask & NULL_BIT:
        terms.append(BinaryExpression(value, BinaryOperator.STRICT_EQUAL, NullLiteral()))
    else:
        terms.append(BinaryExpression(
            _typeof_is(value, "object", BinaryOperator.STRICT_EQUAL),
            LogicalOperator.AND,
            BinaryExpression(value, BinaryOperator.STRICT_NOT_EQUAL, NullLiteral()),
        ))

    return _chain(terms, LogicalOperator.OR)
