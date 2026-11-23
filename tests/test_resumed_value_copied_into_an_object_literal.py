"""A resumed value that an object literal copied keeps its binding (96/12207, a lazy image `{ src: <resumed> }`).

The literal is built from the resume placeholder (`await yield`, not valid JavaScript); the fold only rewrote the
placeholder object itself, not the copy inside the literal. Every placeholder now carries the address of its own
`ResumeGenerator`, so a copy is found without reaching the placeholder of the next resume point.
"""

from pathlib import Path

from hermes_decompiler.Decompiler import Decompiler

_DATA = Path(__file__).parent / "data"


def _render() -> str:
    hasm = (_DATA / "resumed_value_copied_into_an_object_literal_96_12207.hasm").read_text(encoding="utf-8")

    return Decompiler.render(Decompiler.build_context(hasm, 0, strict=False), verbose=False, raw=False)


def test_no_placeholder_is_printed():
    assert "await yield" not in _render()


def test_the_literal_reads_the_bound_register():
    out = _render()

    assert "r1 = yield r2[1];" in out
    assert '{ "src": r1 }' in out
