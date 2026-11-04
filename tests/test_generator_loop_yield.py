"""
A `yield` in the body of a `do { } while` (96/718 `createValueIterator`, 96/720
`createKeyIterator`): the resume guard has no `else`, the loop's `i++` is a sibling
behind it, and the register the suspend point yields is not the one written right
before the `SaveGenerator`:

    r1 = param1[r3]
    Mov r2, r3                  (the counter, read again behind the guard)
    SaveGenerator -> R ; Ret r1  (the `Ret` is never reached; it yields r1)
    R: ResumeGenerator r1, r5 ; JmpTrue r5, <return>
    Inc r3, r2                  (reads the copy)

The fold used to bail out on a guard with siblings behind it and left
`r1 = await yield; if (__resumeIsReturn) { return r1; }` and a `return r2;` after the
loop (the unreachable `Ret`). Folding it must yield what the `Ret` returns (not the
instruction before the save) and must not hide a write the code behind the guard reads.
"""

from hermes_decompiler.Decompiler import Decompiler

_HASM_718 = r"""
=> [Function #718 "?anon_0_createValueIterator" of 64 bytes]: 2 params, frame size=6, strict=1, exc handler=0, debug info=0  @ offset 0x00106368

Bytecode listing:

==> 00000000: <StartGenerator>: <>
==> 00000001: <LoadParam>: <Reg8: 4, UInt8: 1>
==> 00000004: <ResumeGenerator>: <Reg8: 0, Reg8: 1>
==> 00000007: <JmpTrue>: <Addr8: 54, Reg8: 1>  # Address: 0000003d
==> 0000000a: <GetByIdShort>: <Reg8: 1, Reg8: 4, UInt8: 1, string_id: 169>  # String: 'length' (Identifier)
==> 0000000f: <LoadConstZero>: <Reg8: 3>
==> 00000011: <Less>: <Reg8: 1, Reg8: 3, Reg8: 1>
==> 00000015: <JmpFalse>: <Addr8: 32, Reg8: 1>  # Address: 00000035
==> 00000018: <GetByVal>: <Reg8: 1, Reg8: 4, Reg8: 3>
==> 0000001c: <Mov>: <Reg8: 2, Reg8: 3>
==> 0000001f: <SaveGenerator>: <Addr8: 4>  # Address: 00000023
==> 00000021: <Ret>: <Reg8: 1>
==> 00000023: <ResumeGenerator>: <Reg8: 1, Reg8: 5>
==> 00000026: <JmpTrue>: <Addr8: 20, Reg8: 5>  # Address: 0000003a
==> 00000029: <Inc>: <Reg8: 3, Reg8: 2>
==> 0000002c: <GetByIdShort>: <Reg8: 2, Reg8: 4, UInt8: 1, string_id: 169>  # String: 'length' (Identifier)
==> 00000031: <JLess>: <Addr8: -25, Reg8: 3, Reg8: 2>  # Address: 00000018
==> 00000035: <LoadConstUndefined>: <Reg8: 2>
==> 00000037: <CompleteGenerator>: <>
==> 00000038: <Ret>: <Reg8: 2>
==> 0000003a: <CompleteGenerator>: <>
==> 0000003b: <Ret>: <Reg8: 1>
==> 0000003d: <CompleteGenerator>: <>
==> 0000003e: <Ret>: <Reg8: 0>
"""

_HASM_720 = r"""
=> [Function #720 "?anon_0_createKeyIterator" of 60 bytes]: 2 params, frame size=6, strict=1, exc handler=0, debug info=0  @ offset 0x001063b1

Bytecode listing:

==> 00000000: <StartGenerator>: <>
==> 00000001: <LoadParam>: <Reg8: 4, UInt8: 1>
==> 00000004: <ResumeGenerator>: <Reg8: 0, Reg8: 1>
==> 00000007: <JmpTrue>: <Addr8: 50, Reg8: 1>  # Address: 00000039
==> 0000000a: <GetByIdShort>: <Reg8: 1, Reg8: 4, UInt8: 1, string_id: 169>  # String: 'length' (Identifier)
==> 0000000f: <LoadConstZero>: <Reg8: 3>
==> 00000011: <Less>: <Reg8: 1, Reg8: 3, Reg8: 1>
==> 00000015: <JmpFalse>: <Addr8: 28, Reg8: 1>  # Address: 00000031
==> 00000018: <Mov>: <Reg8: 2, Reg8: 3>
==> 0000001b: <SaveGenerator>: <Addr8: 4>  # Address: 0000001f
==> 0000001d: <Ret>: <Reg8: 2>
==> 0000001f: <ResumeGenerator>: <Reg8: 1, Reg8: 5>
==> 00000022: <JmpTrue>: <Addr8: 20, Reg8: 5>  # Address: 00000036
==> 00000025: <Inc>: <Reg8: 3, Reg8: 2>
==> 00000028: <GetByIdShort>: <Reg8: 2, Reg8: 4, UInt8: 1, string_id: 169>  # String: 'length' (Identifier)
==> 0000002d: <JLess>: <Addr8: -21, Reg8: 3, Reg8: 2>  # Address: 00000018
==> 00000031: <LoadConstUndefined>: <Reg8: 2>
==> 00000033: <CompleteGenerator>: <>
==> 00000034: <Ret>: <Reg8: 2>
==> 00000036: <CompleteGenerator>: <>
==> 00000037: <Ret>: <Reg8: 1>
==> 00000039: <CompleteGenerator>: <>
==> 0000003a: <Ret>: <Reg8: 0>
"""


def _code(hasm: str, index: int) -> str:
    js = Decompiler.render(Decompiler.build_context(hasm, index, strict=False), verbose=False, raw=False)

    return "\n".join(line for line in js.splitlines() if not line.strip().startswith("//"))


def test_yield_in_do_while_yields_what_the_ret_returns():
    code = _code(_HASM_718, 718)

    assert "__resumeIsReturn" not in code
    assert "await yield" not in code
    assert "yield param1[r3];" in code
    assert "return" not in code


def test_copy_made_before_the_save_stays_defined_for_the_code_behind_the_guard():
    code = _code(_HASM_718, 718)

    assert "r2 = r3;" in code
    assert code.index("r2 = r3;") < code.index("r3 = r2 + 1;")


def test_yielded_register_read_behind_the_guard_is_not_hidden():
    code = _code(_HASM_720, 720)

    assert "__resumeIsReturn" not in code
    assert "return" not in code
    # `Mov r2, r3; Save; Ret r2` and `Inc r3, r2` behind the guard reads r2.
    assert code.index("r2 = r3;") < code.index("yield r2;") < code.index("r3 = r2 + 1;")
