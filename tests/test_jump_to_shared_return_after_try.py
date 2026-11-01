"""A plain `jmp` to a shared `return` takes the return along (F-158).

The exit of a `try` body is a `jmp` over the catch to the closing `return`. The private copy was a separate
block that nothing placed after the `try`, so a `goto` stayed.

    96/6731  `ensureNativeModulesAreInstalled`
"""

from pathlib import Path

from hermes_decompiler.Decompiler import Decompiler

_DATA = Path(__file__).parent / "data"


def test_the_exit_of_a_try_body_returns_in_place():
    hasm = (_DATA / "jump_to_shared_return_after_try_96_6731.hasm").read_text(encoding="utf-8")
    out = Decompiler.render(Decompiler.build_context(hasm, 6731, strict=False), verbose=False, raw=False)
    out = "\n".join(line for line in out.split("\n") if not line.strip().startswith("//"))

    assert "goto" not in out
    assert out.index("} catch") < out.index("return undefined;")
