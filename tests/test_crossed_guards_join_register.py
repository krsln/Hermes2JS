"""
Crossed guards whose first test is skipped by a register join (98/2044):

    if (typeof a === "undefined") goto NULL;
    r14 = a;  if (typeof r14 === "object") goto END;
    NULL: r14 = null;
    END: use(r14)

`r14 = a` is one arm of the join with `r14 = null`. Folding the two tests into
one condition must not delete it with the second test's block, or the reader
is left with `null` on the path that should see `a`.
"""

from hermes_decompiler.Decompiler import Decompiler

_HASM = r"""
=> [Function #2044 "join" of 40 bytes]: 2 params, frame size=3, strict=1, exc handler=0, debug info=0  @ offset 0x0015c6da

Bytecode listing:

==> 00000000: <LoadParam>: <Reg8: 1, UInt8: 1>
==> 00000003: <JmpTypeOfIs>: <Addr32: 19, Reg8: 1, UInt16: 1>  # Address: 00000016
==> 0000000b: <Mov>: <Reg8: 0, Reg8: 1>
==> 0000000e: <JmpTypeOfIs>: <Addr32: 10, Reg8: 0, UInt16: 495>  # Address: 00000018
==> 00000016: <LoadConstNull>: <Reg8: 0>
==> 00000018: <Ret>: <Reg8: 0>
"""


def test_join_write_removed_with_the_second_test_is_kept():
    js = Decompiler.render(Decompiler.build_context(_HASM, 2044, strict=False), verbose=False, raw=False)
    code = "\n".join(line for line in js.splitlines() if not line.strip().startswith("//"))

    assert "param1" in code.split("return", 1)[0] or "r0 = param1" in code
    assert "return null;" not in code
