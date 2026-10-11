"""
A call may write any property, so a member read loaded before it is not what
the same expression reads after it (98/11177):

    r8 = r5.params;  r5 = ...;  r9 = r8[k]      (not `r5.params[k]` later)

A load consumed as the callee / `this` of the call being handled is exempt
(`console.log` fetched before the argument's own call).
"""

from hermes_decompiler.Decompiler import Decompiler

_HASM = """
=> [Function #11177 "" of 186 bytes]: 2 params, frame size=20, strict=1, exc handler=0, debug info=0  @ offset 0x002252ac

Bytecode listing:

==> 00000000: <GetParentEnvironment>: <Reg8: 5, UInt8: 0>
==> 00000003: <LoadParam>: <Reg8: 6, UInt8: 1>
==> 00000006: <GetByIdShort>: <Reg8: 8, Reg8: 6, UInt8: 0, string_id: 232>  # String: 'startsWith' (Identifier)
==> 0000000b: <LoadConstString>: <Reg8: 7, string_id: 4447>  # String: '[...' (String)
==> 0000000f: <Call2>: <Reg8: 7, Reg8: 8, Reg8: 6, Reg8: 7>
==> 00000014: <JmpTrue>: <Addr8: 91, Reg8: 7>  # Address: 0000006f
==> 00000017: <GetByIdShort>: <Reg8: 8, Reg8: 6, UInt8: 0, string_id: 232>  # String: 'startsWith' (Identifier)
==> 0000001c: <LoadConstString>: <Reg8: 7, string_id: 1103>  # String: '[' (String)
==> 00000020: <Call2>: <Reg8: 7, Reg8: 8, Reg8: 6, Reg8: 7>
==> 00000025: <JmpFalse>: <Addr8: 20, Reg8: 7>  # Address: 00000039
==> 00000028: <GetByIdShort>: <Reg8: 8, Reg8: 6, UInt8: 1, string_id: 135>  # String: 'endsWith' (Identifier)
==> 0000002d: <LoadConstString>: <Reg8: 7, string_id: 1218>  # String: ']' (String)
==> 00000031: <Call2>: <Reg8: 7, Reg8: 8, Reg8: 6, Reg8: 7>
==> 00000036: <JmpTrue>: <Addr8: 5, Reg8: 7>  # Address: 0000003b
==> 00000039: <Ret>: <Reg8: 6>
==> 0000003b: <LoadFromEnvironment>: <Reg8: 7, Reg8: 5, UInt8: 0>
==> 0000003f: <GetByIdShort>: <Reg8: 9, Reg8: 7, UInt8: 2, string_id: 196>  # String: 'params' (Identifier)
==> 00000044: <LoadConstNull>: <Reg8: 2>
==> 00000046: <Eq>: <Reg8: 2, Reg8: 9, Reg8: 2>
==> 0000004a: <LoadConstUndefined>: <Reg8: 7>
==> 0000004c: <JmpTrue>: <Addr8: 27, Reg8: 2>  # Address: 00000067
==> 0000004f: <GetByIdShort>: <Reg8: 8, Reg8: 6, UInt8: 3, string_id: 120>  # String: 'slice' (Identifier)
==> 00000054: <LoadConstInt>: <Reg8: 0, Imm32: -1>
==> 0000005a: <LoadConstUInt8>: <Reg8: 1, UInt8: 1>
==> 0000005d: <Call3>: <Reg8: 8, Reg8: 8, Reg8: 6, Reg8: 1, Reg8: 0>
==> 00000063: <GetByVal>: <Reg8: 7, Reg8: 9, Reg8: 8>
==> 00000067: <JmpTrue>: <Addr8: 6, Reg8: 7>  # Address: 0000006d
==> 0000006a: <Mov>: <Reg8: 7, Reg8: 6>
==> 0000006d: <Ret>: <Reg8: 7>
==> 0000006f: <LoadFromEnvironment>: <Reg8: 5, Reg8: 5, UInt8: 0>
==> 00000073: <GetByIdShort>: <Reg8: 8, Reg8: 5, UInt8: 2, string_id: 196>  # String: 'params' (Identifier)
==> 00000078: <LoadConstNull>: <Reg8: 2>
==> 0000007a: <Eq>: <Reg8: 4, Reg8: 8, Reg8: 2>
==> 0000007e: <LoadConstUndefined>: <Reg8: 5>
==> 00000080: <JmpTrue>: <Addr8: 50, Reg8: 4>  # Address: 000000b2
==> 00000083: <GetByIdShort>: <Reg8: 7, Reg8: 6, UInt8: 3, string_id: 120>  # String: 'slice' (Identifier)
==> 00000088: <LoadConstInt>: <Reg8: 0, Imm32: -1>
==> 0000008e: <LoadConstUInt8>: <Reg8: 1, UInt8: 4>
==> 00000091: <Call3>: <Reg8: 7, Reg8: 7, Reg8: 6, Reg8: 1, Reg8: 0>
==> 00000097: <GetByVal>: <Reg8: 9, Reg8: 8, Reg8: 7>
==> 0000009b: <Eq>: <Reg8: 2, Reg8: 9, Reg8: 2>
==> 0000009f: <LoadConstUndefined>: <Reg8: 5>
==> 000000a1: <JmpTrue>: <Addr8: 17, Reg8: 2>  # Address: 000000b2
==> 000000a4: <GetByIdShort>: <Reg8: 8, Reg8: 9, UInt8: 4, string_id: 167>  # String: 'join' (Identifier)
==> 000000a9: <LoadConstString>: <Reg8: 7, string_id: 503>  # String: '/' (String)
==> 000000ad: <Call2>: <Reg8: 5, Reg8: 8, Reg8: 9, Reg8: 7>
==> 000000b2: <JmpTrue>: <Addr8: 6, Reg8: 5>  # Address: 000000b8
==> 000000b5: <Mov>: <Reg8: 5, Reg8: 6>
==> 000000b8: <Ret>: <Reg8: 5>


"""


def test_member_read_before_a_call_is_named_not_reread_after_it():
    js = Decompiler.render(Decompiler.build_context(_HASM, 11177, strict=False), verbose=False, raw=False)

    assert "r8 = r5.params;" in js
    assert "r9 = r8[r7];" in js
    assert "r9 = r5.params[r7];" not in js
