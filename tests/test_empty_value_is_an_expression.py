"""Hermes' `empty` value (the uninitialized `this` of a derived constructor) prints as an expression (98/4214 `FlatList`).

`LoadConstEmpty` printed a bare comment, so `__environment__[0] = /* empty */;` and `__throwIfThisInitialized__(/* empty */)`
did not parse. The marker stays visible: `undefined /* empty */`.
"""

import re
from pathlib import Path

from hermes_decompiler.Decompiler import Decompiler

_DATA = Path(__file__).parent / "data"


def _render() -> str:
    hasm = (_DATA / "empty_value_in_a_derived_constructor_98_4214.hasm").read_text(encoding="utf-8")

    return Decompiler.render(Decompiler.build_context(hasm, 0, strict=False), verbose=False, raw=False)


def test_the_empty_marker_is_never_a_bare_comment():
    out = _render()

    assert "/* empty */" in out
    assert not re.search(r"(?<!undefined )/\* empty \*/", out)


def test_the_uninitialized_this_is_stored_and_checked_as_an_expression():
    out = _render()

    assert "__environment__[0] = undefined /* empty */;" in out
    assert "__throwIfThisInitialized__(undefined /* empty */);" in out
