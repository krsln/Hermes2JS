"""
A copy that a test consumed and a later join reads by name (96/5371):

    r0 = this.context;  if (!r0) goto END;  …  r0 = a === b;  END: return !!r0

`r0 = this.context` is folded into the `if (this.context)` test, so nothing
defined `r0` on the path that skipped the arm and `return !!r0` read an
undefined register.
"""

from hermes_decompiler.Decompiler import Decompiler

_HASM = r"""
=> [Function #5371 "_isNestedWithSameOrientation" of 69 bytes]: 1 params, frame size=13, strict=1, exc handler=0, debug info=0  @ offset 0x00183c7c

Bytecode listing:

==> 00000000: <LoadParam>: <Reg8: 2, UInt8: 0>
==> 00000003: <GetByIdShort>: <Reg8: 1, Reg8: 2, UInt8: 1, string_id: 101>  # String: 'context' (Identifier)
==> 00000008: <Mov>: <Reg8: 0, Reg8: 1>
==> 0000000b: <JmpFalse>: <Addr8: 50, Reg8: 0>  # Address: 0000003d
==> 0000000e: <GetById>: <Reg8: 1, Reg8: 1, UInt8: 2, string_id: 12155>  # String: 'horizontal' (Identifier)
==> 00000014: <Not>: <Reg8: 1, Reg8: 1>
==> 00000017: <GetEnvironment>: <Reg8: 3, UInt8: 1>
==> 0000001a: <LoadFromEnvironment>: <Reg8: 3, Reg8: 3, UInt8: 15>
==> 0000001e: <GetById>: <Reg8: 4, Reg8: 3, UInt8: 3, string_id: 16767>  # String: 'horizontalOrDefault' (Identifier)
==> 00000024: <GetByIdShort>: <Reg8: 2, Reg8: 2, UInt8: 4, string_id: 204>  # String: 'props' (Identifier)
==> 00000029: <GetById>: <Reg8: 3, Reg8: 2, UInt8: 2, string_id: 12155>  # String: 'horizontal' (Identifier)
==> 0000002f: <LoadConstUndefined>: <Reg8: 2>
==> 00000031: <Call2>: <Reg8: 2, Reg8: 4, Reg8: 2, Reg8: 3>
==> 00000036: <Not>: <Reg8: 1, Reg8: 1>
==> 00000039: <StrictEq>: <Reg8: 0, Reg8: 1, Reg8: 2>
==> 0000003d: <Not>: <Reg8: 0, Reg8: 0>
==> 00000040: <Not>: <Reg8: 0, Reg8: 0>
==> 00000043: <Ret>: <Reg8: 0>
"""


def test_copy_folded_into_a_test_is_still_defined_for_the_join_read():
    js = Decompiler.render(Decompiler.build_context(_HASM, 5371, strict=False), verbose=False, raw=False)
    code = "\n".join(line for line in js.splitlines() if not line.strip().startswith("//"))

    assert "r0 = this.context;" in code
    assert code.index("r0 = this.context;") < code.index("return !!r0;")
