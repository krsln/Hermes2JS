"""A static property whose name is not an identifier prints in brackets (`param1["@@iterator"]`, 96/775).

Hermes (and the Babel helpers compiled with it) read `@@iterator` and `@@nativeEmitterSubscription@@`; printed as
`param1.@@iterator` the output did not parse (11 files in 96 and 98). A private name (`#x`) keeps its dot form.
"""

import pytest

from hermes_decompiler.backend.emit.printer.ExpressionPrinter import ExpressionPrinter
from hermes_decompiler.ir.expressions import Identifier, MemberExpression


def _print(name, optional=False):
    return ExpressionPrinter().visit(MemberExpression(Identifier("param1"), Identifier(name), optional=optional))


@pytest.mark.parametrize("name", ["@@iterator", "@@nativeEmitterSubscription@@", "a-b"])
def test_a_name_that_is_not_an_identifier_is_bracketed(name):
    assert _print(name) == f'param1["{name}"]'


def test_an_optional_access_keeps_its_question_mark():
    assert _print("@@iterator", optional=True) == 'param1?.["@@iterator"]'


@pytest.mark.parametrize("name", ["props", "_x", "$el", "#__private_2__", "größe"])
def test_an_identifier_keeps_the_dot(name):
    assert _print(name) == f"param1.{name}"
