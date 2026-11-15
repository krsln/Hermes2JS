"""
`IfTailMergeRegionPass` keeps a `return` that a test (still unresolved, ending its sequence) jumps to (F-210,
96/13834 `getInitialURL`).

`if (r3 === "web") { ...; if (r1) goto HREF }` runs on into the native-platform code when `r1` is false; the
`HREF` block (`r0 = window.location; return r0.href`) was merged into the one `return r0` after the `if`, so the
test printed `if (r1) { r0 = ...href }` and the true case ran on into the native code instead of returning.
"""

from pathlib import Path

from hermes_decompiler.Decompiler import Decompiler

_DATA = Path(__file__).parent / "data"


def _code() -> str:
    hasm = (_DATA / "if_tail_merge_tested_return_96_13834.hasm").read_text(encoding="utf-8")
    out = Decompiler.render(Decompiler.build_context(hasm, 13834, strict=False), verbose=False, raw=False)

    return "\n".join(line for line in out.split("\n") if not line.strip().startswith("//"))


def test_the_href_case_returns_where_the_test_is():
    code = _code()

    assert "goto" not in code
    assert "if (r1) {\n                r0 = window.location;\n                return r0.href;\n            }" in code
