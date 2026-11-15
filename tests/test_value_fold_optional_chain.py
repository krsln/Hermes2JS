"""
`a?.b || a?.c` used as a test folds into one condition (F-221, 98/7639 `resolveSource`).

    r6 = undefined; if (a == null) goto M; r6 = a.b; M: if (r6) goto BODY

The jump to `M` itself keeps the value the head block just wrote. `ValueConditionFoldCfgPass` only followed jumps
through arm blocks, so the diamond stayed, and the second test printed `if (r6) goto L` into the body.
"""

from pathlib import Path

from hermes_decompiler.Decompiler import Decompiler

_DATA = Path(__file__).parent / "data"


def test_the_optional_chain_tests_fold_into_one_condition():
    hasm = (_DATA / "value_fold_optional_chain_98_7639.hasm").read_text(encoding="utf-8")
    out = Decompiler.render(Decompiler.build_context(hasm, 7639, strict=False), verbose=False, raw=False)
    code = "\n".join(line for line in out.split("\n") if not line.strip().startswith("//"))

    assert "goto" not in code
    assert 'typeof param1 === "object" && ((param1 == null ? undefined : param1.blurhash) || ' in code
