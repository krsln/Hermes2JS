"""
Tests for `tests/tools/dangling.py`'s text analysis (`analyze`).

The tool is a correctness proxy for decompiler output, so a bug in it shows up
as a phantom regression (or hides a real one) in every measurement. These tests
pin its comment/string stripping.
"""

from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest

_TOOL = Path(__file__).resolve().parent / "tools" / "dangling.py"


@pytest.fixture(scope="module")
def dangling():
    # dangling.py reads sys.argv at import time (output path / repo root) and
    # inserts the repo root into sys.path; give it a clean argv so pytest's own
    # arguments are not mistaken for a repo path.
    saved = sys.argv
    sys.argv = ["dangling.py"]
    try:
        spec = importlib.util.spec_from_file_location("dangling_under_test", _TOOL)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
    finally:
        sys.argv = saved

    return module


def test_double_slash_inside_a_string_is_not_a_comment(dangling):
    # The `//` in the URL used to be stripped as a line comment first. That
    # deleted the closing quote, and the orphaned `"` then swallowed the code
    # up to the next quote - including the real definition of r2.
    js = (
        "function f() {\n"
        '    r1 = "see https://example.com/x";\n'
        "    r2 = { a: 1 };\n"
        '    r3 = "b";\n'
        "    return r2 + r3 + r1;\n"
        "}\n"
    )

    never_defined, read_before_def = dangling.analyze(js)

    assert never_defined == set()
    assert read_before_def == set()


def test_quote_inside_a_comment_does_not_open_a_string(dangling):
    js = (
        "function f() {\n"
        "    // it's a note\n"
        "    r1 = 1;\n"
        '    r2 = "x";\n'
        "    return r1 + r2;\n"
        "}\n"
    )

    never_defined, read_before_def = dangling.analyze(js)

    assert never_defined == set()
    assert read_before_def == set()


def test_registers_mentioned_only_in_comments_are_ignored(dangling):
    js = (
        "function f() {\n"
        "    // r9 = 1;\n"
        "    /* r8 */\n"
        "    r1 = 1;\n"
        "    return r1;\n"
        "}\n"
    )

    never_defined, read_before_def = dangling.analyze(js)

    assert never_defined == set()
    assert read_before_def == set()


def test_registers_inside_strings_are_ignored(dangling):
    js = 'function f() {\n    r1 = "r7 = r8";\n    return r1;\n}\n'

    never_defined, _ = dangling.analyze(js)

    assert never_defined == set()


def test_a_genuinely_undefined_register_is_still_reported(dangling):
    # The fix must not make the tool blind: a read with no definition anywhere
    # (even next to a URL string) is still a finding.
    js = (
        "function f() {\n"
        '    r1 = "https://example.com";\n'
        "    return r1 + r5;\n"
        "}\n"
    )

    never_defined, _ = dangling.analyze(js)

    assert never_defined == {"r5"}


def test_a_read_before_its_definition_is_still_reported(dangling):
    js = "function f() {\n    r1 = r2;\n    r2 = 1;\n    return r1;\n}\n"

    never_defined, read_before_def = dangling.analyze(js)

    assert never_defined == set()
    assert read_before_def == {"r2"}


@pytest.mark.parametrize("pattern", [
    "[r8, r7, r0] = r6;",
    "[[r8, r7], , [, r0]] = r6;",
    "[r8 = 0, r7 = 0, ...r0] = r6;",
    "{ a: r8, b: r7, c: r0 } = r6;",
])
def test_destructuring_assignment_targets_count_as_definitions(dangling, pattern):
    # Nested / holey / defaulted / rest forms used to stop at the first inner
    # `]`, so their targets (r8, r7, r0) looked read-but-never-defined.
    js = f"function f() {{\n    r6 = [1];\n    {pattern}\n    console.log(r8, r7, r0);\n}}\n"

    never_defined, read_before_def = dangling.analyze(js)

    assert never_defined == set()
    assert read_before_def == set()


def test_a_register_missing_from_a_destructuring_pattern_is_still_reported(dangling):
    js = "function f() {\n    r6 = [1];\n    [[r8, r7]] = r6;\n    console.log(r8, r7, r0);\n}\n"

    never_defined, _ = dangling.analyze(js)

    assert never_defined == {"r0"}
