"""An early-return tail laid out after the closing return becomes `if (c) { tail }` in a function with a `try` (F-277).

`if (signal && signal.aborted) { return reject(new DOMException(...)) }` ahead of a `try` compiles to a branch to a
block placed behind the function's closing `return undefined`. `relocate_terminal_tails` moves such a tail behind its
branch, but gave up on any function that has handlers; only a branch or tail a handler guards must stay (96/3448
`fetch` of the XHR polyfill).
"""

from pathlib import Path

from hermes_decompiler.Decompiler import Decompiler

_DATA = Path(__file__).parent / "data"


def test_the_abort_tail_is_an_if_body_before_the_try():
    hasm = (_DATA / "terminal_tail_relocated_in_function_with_try_96_3448.hasm").read_text(encoding="utf-8")
    out = Decompiler.render(Decompiler.build_context(hasm, 3448, strict=False), verbose=False, raw=False)

    assert "goto" not in out
    assert 'new r4("Aborted", "AbortError")' in out
    assert out.index('"AbortError"') < out.index("try {")
