"""
F-124: `if (a === undefined) goto R; if (a === null) goto R; ...` where R is `return a`.

    98/11208 `wrappedFn`, 96/4157 `parseFileSlash`, 96/1139 `processColor`: two constant tests
    of the same value that share one body are not a `switch` (it needs two bodies), but the
    second test was folded away as if it were a case link, so `a === null` fell off the end
    of the function and returned `undefined` instead of `a`.
"""

from pathlib import Path

from hermes_decompiler.Decompiler import Decompiler

_DATA = Path(__file__).parent / "data"


def test_both_labels_of_a_shared_return_keep_their_return():
    hasm = (_DATA / "two_labels_one_return_98_11208.hasm").read_text(encoding="utf-8")
    out = Decompiler.render(Decompiler.build_context(hasm, 11208, strict=False), verbose=False, raw=False)

    assert "goto" not in out
    assert "case undefined:\n            return r3;" in out
    assert "case null:\n            return r3;" in out
    # the old shape: the `null` case silently returned nothing
    assert "else if (r3 !== null)" not in out
