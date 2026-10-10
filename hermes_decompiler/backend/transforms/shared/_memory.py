"""Which memory stores can invalidate a value that was loaded earlier."""

from __future__ import annotations

from hermes_decompiler.ir.expressions import (
    ArrayExpression, AssignmentExpression, Identifier, MemberExpression, NumericLiteral, ObjectExpression,
    StringLiteral,
)
from ._structural_key import structural_key

#: The function's own environment: never the same object as a parent one.
_OWN_ENVIRONMENT = "__environment__"


def property_key(member: MemberExpression) -> str | None:
    """`a.b` / `a["b"]` / `a[3]` -> "b" / "b" / "3"; `a[k]` -> None."""
    prop = member.prop
    if not member.computed and isinstance(prop, Identifier):
        return prop.name
    if isinstance(prop, (StringLiteral, NumericLiteral)):
        return str(prop.value)
    return None


def stored_member(value) -> MemberExpression | None | bool:
    """The member a memory-store instruction assigns, `None` when it stores
    somewhere unknown, `False` when it only builds a literal (no earlier
    load can be affected)."""
    if isinstance(value, AssignmentExpression) and isinstance(value.left, MemberExpression):
        return value.left
    if isinstance(value, (ArrayExpression, ObjectExpression)):
        return False
    return None


def read_members(value) -> tuple[MemberExpression, ...]:
    return tuple(node for node in value.walk() if isinstance(node, MemberExpression))


def may_alias(read: MemberExpression, store: MemberExpression | None) -> bool:
    """The store may write the location `read` loaded: the same key (or an
    unknown one) on the same base, or on another plain variable (which may
    hold the same object). A deeper chain (`r1[0][0]` against the read
    `r1[0]`) is a different location."""
    if store is None:
        return True

    read_key, store_key = property_key(read), property_key(store)
    if read_key is not None and store_key is not None and read_key != store_key:
        return False

    if structural_key(read.obj) == structural_key(store.obj):
        return True

    if not (isinstance(read.obj, Identifier) and isinstance(store.obj, Identifier)):
        return False

    return _OWN_ENVIRONMENT not in (read.obj.name, store.obj.name)
