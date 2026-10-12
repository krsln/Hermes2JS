"""
The call-argument window of `CallBuiltin` sits a fixed distance below the
frame size (7 on hbc96, 8 on hbc98 - read off the opcodes the function uses),
so a recent unrelated write one slot above the real window cannot move it:

  96/2877   copyDataProperties(r10, r9)    (was (r11, r10): the `this` slot)
  98/11966  throwTypeError("...")          (was r30, an older `this` slot)
"""

from hermes_decompiler.Decompiler import Decompiler

_HASM_96 = r"""
=> [Function #2877 "toJSON" of 75 bytes]: 1 params, frame size=18, strict=1, exc handler=0, debug info=0  @ offset 0x0014c22d

Bytecode listing:

==> 00000000: <LoadParam>: <Reg8: 1, UInt8: 0>
==> 00000003: <NewObject>: <Reg8: 0>
==> 00000005: <GetEnvironment>: <Reg8: 2, UInt8: 1>
==> 00000008: <LoadFromEnvironment>: <Reg8: 2, Reg8: 2, UInt8: 0>
==> 0000000c: <GetByIdShort>: <Reg8: 6, Reg8: 2, UInt8: 1, string_id: 107>  # String: 'default' (Identifier)
==> 00000011: <GetEnvironment>: <Reg8: 2, UInt8: 0>
==> 00000014: <LoadFromEnvironment>: <Reg8: 10, Reg8: 2, UInt8: 0>
==> 00000018: <LoadConstUndefined>: <Reg8: 4>
==> 0000001a: <LoadConstString>: <Reg8: 9, string_id: 9976>  # String: 'toJSON' (Identifier)
==> 0000001e: <LoadConstUInt8>: <Reg8: 7, UInt8: 3>
==> 00000021: <LoadConstUndefined>: <Reg8: 11>
==> 00000023: <Mov>: <Reg8: 8, Reg8: 1>
==> 00000026: <Call>: <Reg8: 3, Reg8: 6, UInt8: 5>
==> 0000002a: <NewArray>: <Reg8: 2, UInt16: 0>
==> 0000002e: <Call2>: <Reg8: 9, Reg8: 3, Reg8: 4, Reg8: 2>
==> 00000033: <Mov>: <Reg8: 10, Reg8: 0>
==> 00000036: <CallBuiltin>: <Reg8: 2, UInt8: 44, UInt8: 3>  # Built-in function: [#44 copyDataProperties]
==> 0000003a: <GetById>: <Reg8: 2, Reg8: 1, UInt8: 2, string_id: 8013>  # String: 'attribution' (Identifier)
==> 00000040: <LoadConstString>: <Reg8: 1, string_id: 8013>  # String: 'attribution' (Identifier)
==> 00000044: <PutOwnByVal>: <Reg8: 0, Reg8: 2, Reg8: 1, UInt8: 1>
==> 00000049: <Ret>: <Reg8: 0>
"""

_HASM_98 = r"""
=> [Function #1 "f" of 40 bytes]: 2 params, frame size=38, strict=1, exc handler=0, debug info=0  @ offset 0x00000000

Bytecode listing:

==> 00000000: <GetParentEnvironment>: <Reg8: 6, UInt8: 0>
==> 00000003: <LoadParam>: <Reg8: 13, UInt8: 1>
==> 00000006: <LoadConstUndefined>: <Reg8: 30>
==> 00000008: <LoadFromEnvironment>: <Reg8: 8, Reg8: 6, UInt8: 18>
==> 0000000c: <JmpTypeOfIs>: <Addr32: 16, Reg8: 8, UInt16: 128>  # Address: 0000001c
==> 00000014: <LoadConstString>: <Reg8: 29, string_id: 4299>  # String: 'Trying to call a non-function' (String)
==> 00000018: <CallBuiltin>: <Reg8: 5, UInt8: 44, UInt8: 2>  # Built-in function: [#44 throwTypeError]
==> 0000001c: <Ret>: <Reg8: 13>

"""


def _js(hasm: str, function_id: int) -> str:
    return Decompiler.render(Decompiler.build_context(hasm, function_id, strict=False), verbose=False, raw=False)


def test_hbc96_window_top_follows_frame_size():
    js = _js(_HASM_96, 2877)

    assert "copyDataProperties(r10, r9)" in js


def test_hbc98_window_top_ignores_unrelated_recent_write_above_it():
    js = _js(_HASM_98, 1)

    assert 'throwTypeError("Trying to call a non-function")' in js
