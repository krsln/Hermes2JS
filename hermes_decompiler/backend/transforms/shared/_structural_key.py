from __future__ import annotations

import dataclasses


def structural_key(value):
    """
    Value-based key for an expression node, independent of whether its
    class defines `__eq__` (many of the IR expression classes don't,
    so plain `==` silently falls back to object identity and never
    matches two separately-built-but-equivalent trees). Deeply unpacks
    dataclasses into tuples so structurally identical trees -
    regardless of which registers produced them - compare equal.
    Falls back to `repr()` for anything that isn't a dataclass.

    Shared home for what used to be two independent, near-identical
    copies (`TryStructurer._structural_key`,
    `ForEachRecognizer._structural_key`) - both passes need to compare
    IR values by content rather than by register/object identity, for
    the same underlying reason: recognizing that two register-free
    expression trees, built at different points in the pipeline,
    represent the same logical value.
    """

    if dataclasses.is_dataclass(value) and not isinstance(value, type):
        return tuple(
            structural_key(getattr(value, f.name))
            for f in dataclasses.fields(value)
        )

    if isinstance(value, (list, tuple)):
        return tuple(structural_key(v) for v in value)

    try:
        hash(value)
        return value
    except TypeError:
        return repr(value)
