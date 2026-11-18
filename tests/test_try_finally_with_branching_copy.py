"""A `finally` whose body branches is one `finally`, with no second copy after the try (F-274).

`try { cb() } catch (e) { report(e) } finally { restore; if (a && b) { a.types = b.types } restore }` compiles
to a handler copy that ends in a rethrow and a normal-path copy after the try. The handler's last `if` tests the
merge block, so the span used to stop before it (a `goto` into the copy), and the copy after the try keeps its own
temporaries (`r4 = r3; r4.types`), so it was not recognised as the same code (96/1030 `startTransition`).
"""

from pathlib import Path

from hermes_decompiler.Decompiler import Decompiler

_DATA = Path(__file__).parent / "data"


def test_the_branching_finally_is_whole_and_not_repeated_after_the_try():
    hasm = (_DATA / "try_finally_branching_copy_96_1030.hasm").read_text(encoding="utf-8")
    out = Decompiler.render(Decompiler.build_context(hasm, 1030, strict=False), verbose=False, raw=False)

    assert "goto" not in out
    assert "} finally {" in out
    assert out.count("r1.types") == 1
    assert out.count(".T = r1") == 1
    assert out.rstrip().endswith("}\n}")
