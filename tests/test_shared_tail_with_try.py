"""A shared tail is copied in a function with a `try` too, when nothing it touches is protected (F-193).

    if (!a) goto T; ...; if (b) goto E; T: x; jmp END; E: y; END:

`SharedTailDuplicationCfgPass` gave up on every function with an exception handler (a copy sits outside every try
range). 98/13397 `loadRoute` has a `try` as the first thing of the function and the `_result` tests far behind
it: the second test kept `if (r2 != null) goto label_111`. A tail, and the tests in front of it, that no handler
protects or starts at are copied as everywhere else; a function whose tail is protected is still left alone.

    98/13397 `loadRoute`   96/7898 `shouldPreventRemove` (the handler guards the loop at the end, the tail is before it)
"""

from pathlib import Path

from hermes_decompiler.Decompiler import Decompiler

_DATA = Path(__file__).parent / "data"


def _render(name: str, function_id: int) -> str:
    hasm = (_DATA / name).read_text(encoding="utf-8")
    out = Decompiler.render(Decompiler.build_context(hasm, function_id, strict=False), verbose=False, raw=False)

    return "\n".join(line for line in out.split("\n") if not line.strip().startswith("//"))


def test_the_tail_behind_a_try_is_copied_for_the_test_that_skips_it():
    out = _render("shared_tail_with_try_98_13397.hasm", 13397)

    assert "goto" not in out
    assert "} catch (caughtException) {" in out
    assert "if (r2 != null) {\n                r2 = r0;\n                r1 = r2._result;\n            } else {\n                r1 = r0;" in out


def test_the_instanceof_test_that_falls_into_the_new_set_is_one_if():
    out = _render("shared_tail_with_try_96_7898.hasm", 7898)

    assert "goto" not in out
    assert "r8 = r3;" in out and "r8 = param5[r1];" not in out
