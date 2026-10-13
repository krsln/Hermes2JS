"""
`GetByVal` reads its key by name, which keeps the key register's own
definition in the output. The object expression is inlined, so it has to see
that rewrite (96/13659):

    r1 = env[0];  r0 = env[1];  r0 = r1[r0]      is `r1[r0]`, not `r0[0][r0]`
"""

from hermes_decompiler.Decompiler import Decompiler

_HASM = r"""
=> [Function #13659 "get" of 17 bytes]: 1 params, frame size=2, strict=1, exc handler=0, debug info=0  @ offset 0x00220e98

Bytecode listing:

==> 00000000: <GetEnvironment>: <Reg8: 0, UInt8: 0>
==> 00000003: <LoadFromEnvironment>: <Reg8: 1, Reg8: 0, UInt8: 0>
==> 00000007: <LoadFromEnvironment>: <Reg8: 0, Reg8: 0, UInt8: 1>
==> 0000000b: <GetByVal>: <Reg8: 0, Reg8: 1, Reg8: 0>
==> 0000000f: <Ret>: <Reg8: 0>
"""


def test_inlined_object_is_not_read_through_the_redefined_key_register():
    js = Decompiler.render(Decompiler.build_context(_HASM, 13659, strict=False), verbose=False, raw=False)

    assert "r1 = r0[0];" in js
    assert "return r1[r0];" in js
    assert "r0[0][r0]" not in js
