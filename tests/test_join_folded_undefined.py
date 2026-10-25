"""
A join read that names its register keeps the `undefined` an earlier test folded away (F-137, 98/9611 `dt`).

    r4 = undefined                  # 0x58
    if (undefined === r8) goto END  # JStrictEqual r4, r8: the test took `r4` as `undefined`
    ...
    r4 = <closure>                  # the other arm
    END: r3.size = r4               # PutOwnBySlotIdx r3, r4

The test inlined the constant and nothing printed `r4 = undefined`, so `r3.size = r4` read the
`highWaterMark` value `r4` still held on the path that jumps. `get_register_expression` now prints the
folded `undefined` definitions of the register when the join guard answers with `rN`.
"""

from pathlib import Path

from hermes_decompiler.Decompiler import Decompiler

_DATA = Path(__file__).parent / "data"


def _code() -> str:
    hasm = (_DATA / "join_folded_undefined_98_9611.hasm").read_text(encoding="utf-8")

    return Decompiler.render(Decompiler.build_context(hasm, 9611, strict=False), verbose=False, raw=False)


def test_the_undefined_a_test_folded_is_printed_before_the_join_reads_it():
    code = _code()

    assert code.index('r3 = { "highWaterMark": r4, "size": null };\n        r4 = undefined;') >= 0
    assert code.index("r4 = undefined;\n        if (undefined === r8) {") >= 0
    assert "r3.size = r4;" in code
