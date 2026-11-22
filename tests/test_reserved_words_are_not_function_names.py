"""A function named like a reserved word gets a trailing underscore (`return_`, `in_`; 30 files in 96 and 98).

Class methods called `return`, `delete`, `catch`, `in`, `with` compile to functions of that name; printed as is,
`function delete(...)` and `{ "return": return }` do not parse. 96/142 builds an iterator object from two such
closures.
"""

from pathlib import Path

import pytest

from hermes_decompiler.Decompiler import Decompiler
from hermes_decompiler.core.Naming import to_js_identifier

_DATA = Path(__file__).parent / "data"


@pytest.mark.parametrize("name", ["return", "delete", "catch", "in", "with", "typeof", "static", "yield"])
def test_a_reserved_word_gets_an_underscore(name):
    assert to_js_identifier(name) == f"{name}_"


@pytest.mark.parametrize("name", ["next", "Return", "returns", "of", "get", "async", "$delete"])
def test_other_names_are_untouched(name):
    assert to_js_identifier(name) == name


def test_a_closure_named_return_is_read_through_its_safe_name():
    hasm = (_DATA / "closure_named_after_a_reserved_word_96_142.hasm").read_text(encoding="utf-8")
    out = Decompiler.render(Decompiler.build_context(hasm, 0, strict=False), verbose=False, raw=False)

    assert '"return": return_ }' in out
    assert ": return }" not in out
