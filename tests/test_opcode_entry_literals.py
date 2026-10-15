"""
`Object: {...}` / `Array: [...]` opcode comments carry a Python-repr-like
literal whose JS keywords (`null`/`true`/`false`/`undefined`) must be
rewritten for `ast.literal_eval` - without touching string CONTENTS.

String values can themselves be JavaScript source (a Reanimated worklet's
`code` field), so a plain regex over the whole comment either corrupts them
(`return null;` -> `return None;`) or, for `undefined`, splices a quoted
marker into the middle of an already-quoted string and makes the whole
literal unparseable: the `NewObjectWithBuffer ... No valid object parsed
from comment` errors seen when decompiling a full React Native bundle.
"""

from __future__ import annotations

import pytest

from hermes_decompiler.frontend.opcode.OpcodeEntry import JS_UNDEFINED, OpcodeEntry, _normalize_js_literals

parse_object = OpcodeEntry._parse_object_literal
parse_array = OpcodeEntry._parse_array_literal


def test_undefined_inside_a_string_does_not_break_parsing():
    parsed = parse_object("{'code': \"function f(m){if(m[6]!==undefined){return 1;}return 2;}\"}")

    assert parsed == {"code": "function f(m){if(m[6]!==undefined){return 1;}return 2;}"}


def test_keywords_inside_a_string_are_left_alone():
    parsed = parse_object("{'code': 'function f(){return null;}', 'a': \"x==true||y===false\", 'ok': true}")

    assert parsed["code"] == "function f(){return null;}"
    assert parsed["a"] == "x==true||y===false"
    assert parsed["ok"] is True


def test_bare_keywords_are_still_converted():
    parsed = parse_object("{'a': null, 'b': true, 'c': false, 'd': undefined, 'e': [undefined, null]}")

    assert parsed["a"] is None
    assert parsed["b"] is True
    assert parsed["c"] is False
    assert parsed["d"] is JS_UNDEFINED
    assert parsed["e"] == [JS_UNDEFINED, None]


def test_undefined_stays_distinct_from_null():
    parsed = parse_object("{'x': undefined, 'y': null}")

    assert parsed["x"] is JS_UNDEFINED
    assert parsed["y"] is None
    assert parsed["x"] is not parsed["y"]


def test_escaped_quote_does_not_end_the_string_early():
    parsed = parse_object("{'s': 'it\\'s null', 'n': null}")

    assert parsed == {"s": "it's null", "n": None}


def test_double_quoted_string_may_contain_single_quotes_and_braces():
    parsed = parse_object("{'code': \"if(typeof c==='number'){return null;}\"}")

    assert parsed == {"code": "if(typeof c==='number'){return null;}"}


def test_array_literal_strings_named_like_keywords_stay_strings():
    assert parse_array("['undefined', 'true', 'null', 3]") == ["undefined", "true", "null", 3]


def test_array_literal_bare_keywords_are_converted():
    assert parse_array("[null, true, false, undefined]") == [None, True, False, JS_UNDEFINED]


def test_normalizer_leaves_identifiers_that_merely_contain_a_keyword():
    # `\bnull\b` never matched these either; a token scanner must not split them.
    assert _normalize_js_literals("{'k': nullable, 'j': true_value}") == "{'k': nullable, 'j': true_value}"


def test_unterminated_string_does_not_hang_or_raise_in_the_normalizer():
    assert _normalize_js_literals("{'a': 'oops null") == "{'a': 'oops null"


@pytest.mark.parametrize("keyword", ["null", "true", "false", "undefined"])
def test_worklet_like_code_round_trips_unchanged(keyword):
    code = f"function w(a){{if(a=={keyword}){{return {keyword};}}return a;}}"

    assert parse_object("{'code': \"" + code + "\"}") == {"code": code}
