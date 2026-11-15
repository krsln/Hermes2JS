"""A test block that writes its register twice, the last write a constant END reads (96/3450 `onload`).

`if (url.indexOf("file://") === 0 && (xhr.status < 200 || xhr.status > 599)) { status = 200 } else { status = xhr.status }`
compiles to `X: if (r2 !== 0) goto S; Y: r2 = env[3]; r6 = r2.status; r2 = 200; if (r6 < 200) goto T; ...; S: ...; T: put(r5, r2)`.
`_constants_for_the_end_edge` wanted the register written ONCE in the block, so the constant END reads (`r2 = 200`)
was not given its own copy on the edge into END, the crossed fold failed, and the printed
`if (r6 < 200 || ...) goto label_146; r5.status = 200;` set 200 on the not-out-of-range path too.
The block's LAST write is what END reads; the earlier ones only feed the test.
"""

from pathlib import Path

from hermes_decompiler.Decompiler import Decompiler

_DATA = Path(__file__).parent / "data"


def _render(name, index):
    hasm = (_DATA / name).read_text(encoding="utf-8")

    return Decompiler.render(Decompiler.build_context(hasm, index, strict=False), verbose=False, raw=False)


def test_the_status_test_is_one_condition_with_an_else():
    out = _render("rematerialized_constant_96_3450.hasm", 3450)

    assert "goto label" not in out
    assert "if (r2 === 0 && (r4[3].status < 200 || r4[3].status > 599)) {\n        r5.status = 200;\n    } else {" in out
