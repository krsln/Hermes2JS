"""Shared `throw` exits reached only by jumps (98/3508 `toQueryPair`: `typeof r !== "object"` / `r == null`, twice).

The first test of a pair kept a copy of the exit, the later one kept the original: the copy of the second pair sat
behind the whole `else` arm and the test printed `if (typeof r7 !== "object") goto label_N;` with the throw after the
arm. The EARLIER jumper now keeps the original, every later one gets a private copy.
"""

from pathlib import Path

from hermes_decompiler.Decompiler import Decompiler

_DATA = Path(__file__).parent / "data"


def test_both_typeof_object_tests_throw_in_place():
    hasm = (_DATA / "shared_throw_copies_in_iterator_pair_98_3508.hasm").read_text(encoding="utf-8")
    out = Decompiler.render(Decompiler.build_context(hasm, 3508, strict=False), verbose=False, raw=False)

    assert "goto label_" not in out
    assert out.count('throw new TypeError("The provided value is not an object");') == 4
