"""
`for (k in obj)` is printed without Hermes' null guard around it (96/5107 `addAnimatedValuesListenersToProps`).

    GetPNameList r6, r5, ...      # `undefined` for a null/undefined object
    JmpUndefined r6 -> exit       # the guard
    GetNextPName r2, r6, ...      # the loop

printed `r6 = HermesPropertyIterator(r5); if (r6 !== undefined) { for (const r2 in r5) { ... } }`. A for-in over
null/undefined runs zero times, so the guard and the list's own definition say nothing the loop does not. They stay
when later code still reads the list register.
"""

from hermes_decompiler.Decompiler import Decompiler

_HEADER = (
    '=> [Function #5107 "addAnimatedValuesListenersToProps" of 52 bytes]: 3 params, frame size=20, strict=1, '
    'exc handler=0, debug info=0  @ offset 0x0017d8a9'
)

_BODY = """
Bytecode listing:

==> 00000000: <LoadParam>: <Reg8: 8, UInt8: 1>
==> 00000003: <LoadParam>: <Reg8: 7, UInt8: 2>
==> 00000006: <Mov>: <Reg8: 5, Reg8: 8>
==> 00000009: <GetEnvironment>: <Reg8: 1, UInt8: 0>
==> 0000000c: <LoadConstUndefined>: <Reg8: 0>
==> 0000000e: <GetPNameList>: <Reg8: 6, Reg8: 5, Reg8: 4, Reg8: 3>
==> 00000013: <JmpUndefined>: <Addr8: 31, Reg8: 6>  # Address: 00000032
==> 00000016: <GetNextPName>: <Reg8: 2, Reg8: 6, Reg8: 5, Reg8: 4, Reg8: 3>
==> 0000001c: <JmpUndefined>: <Addr8: 22, Reg8: 2>  # Address: 00000032
==> 0000001f: <Mov>: <Reg8: 9, Reg8: 2>
==> 00000022: <GetByVal>: <Reg8: 10, Reg8: 8, Reg8: 9>
==> 00000026: <LoadFromEnvironment>: <Reg8: 9, Reg8: 1, UInt8: 11>
==> 0000002a: <Call3>: <Reg8: 9, Reg8: 9, Reg8: 0, Reg8: 10, Reg8: 7>
==> 00000030: <Jmp>: <Addr8: -26>  # Address: 00000016
==> 00000032: <Ret>: <Reg8: {returned}>
"""


def _render(returned: int) -> str:
    hasm = f"\n{_HEADER}\n{_BODY.format(returned=returned)}"

    return Decompiler.render(Decompiler.build_context(hasm, 5107, strict=False), verbose=False, raw=False)


def test_the_null_guard_and_the_property_list_are_not_printed():
    code = _render(returned=0)

    assert "for (const r2 in r5) {" in code
    assert "HermesPropertyIterator" not in code
    assert "!== undefined" not in code
    assert "goto" not in code


def test_the_guard_stays_when_the_property_list_is_read_after_the_loop():
    code = _render(returned=6)

    assert "HermesPropertyIterator(r5)" in code
    assert "if (r6 !== undefined) {" in code
