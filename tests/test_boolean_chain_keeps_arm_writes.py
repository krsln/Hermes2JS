"""
A value-producing `||` chain is folded away together with its arm. A write to
ANOTHER register inside that arm (`r8 = r18`) goes with it, and code after
the `if` that holds the arm's value inline (`StoreToEnvironment r8`) would
then claim it on the path that skips the arm (98/4563, the iterator
destructuring's `done` flag):

    r8 = undefined;  if (!done) { r8 = r18; ... }  env[1] = r8
"""

from hermes_decompiler.Decompiler import Decompiler

_HASM = r"""
=> [Function #4563 "useWindowDimensions" of 125 bytes]: 1 params, frame size=20, strict=1, exc handler=0, debug info=0  @ offset 0x001a5143

Bytecode listing:

==> 00000000: <GetParentEnvironment>: <Reg8: 3, UInt8: 0>
==> 00000003: <LoadFromEnvironment>: <Reg8: 5, Reg8: 3, UInt8: 1>
==> 00000007: <GetByIdShort>: <Reg8: 4, Reg8: 5, UInt8: 0, string_id: 251>  # String: 'useState' (Identifier)
==> 0000000c: <LoadConstUndefined>: <Reg8: 1>
==> 0000000e: <CreateClosure>: <Reg8: 3, Reg8: 3, function_id: 10363>  # Function: [#10363  of 28 bytes]: 1 params @ offset 0x00216947
==> 00000013: <Call2>: <Reg8: 3, Reg8: 4, Reg8: 1, Reg8: 3>
==> 00000018: <Mov>: <Reg8: 8, Reg8: 3>
==> 0000001b: <IteratorBegin>: <Reg8: 6, Reg8: 8>
==> 0000001e: <Mov>: <Reg8: 3, Reg8: 8>
==> 00000021: <IteratorNext>: <Reg8: 4, Reg8: 6, Reg8: 3>
==> 00000025: <Mov>: <Reg8: 3, Reg8: 6>
==> 00000028: <StrictEq>: <Reg8: 0, Reg8: 3, Reg8: 1>
==> 0000002c: <LoadConstUndefined>: <Reg8: 3>
==> 0000002e: <JmpTrue>: <Addr8: 6, Reg8: 0>  # Address: 00000034
==> 00000031: <Mov>: <Reg8: 3, Reg8: 4>
==> 00000034: <CreateFunctionEnvironment>: <Reg8: 4, UInt8: 2>
==> 00000037: <StoreToEnvironment>: <Reg8: 4, UInt8: 0, Reg8: 3>
==> 0000003b: <LoadConstUndefined>: <Reg8: 7>
==> 0000003d: <JmpTrue>: <Addr8: 28, Reg8: 0>  # Address: 00000059
==> 00000040: <IteratorNext>: <Reg8: 8, Reg8: 6, Reg8: 8>
==> 00000044: <Mov>: <Reg8: 9, Reg8: 6>
==> 00000047: <StrictEq>: <Reg8: 2, Reg8: 9, Reg8: 1>
==> 0000004b: <LoadConstUndefined>: <Reg8: 7>
==> 0000004d: <Mov>: <Reg8: 0, Reg8: 2>
==> 00000050: <JmpTrue>: <Addr8: 9, Reg8: 2>  # Address: 00000059
==> 00000053: <Mov>: <Reg8: 7, Reg8: 8>
==> 00000056: <Mov>: <Reg8: 0, Reg8: 2>
==> 00000059: <StoreToEnvironment>: <Reg8: 4, UInt8: 1, Reg8: 7>
==> 0000005d: <JmpTrue>: <Addr8: 6, Reg8: 0>  # Address: 00000063
==> 00000060: <IteratorClose>: <Reg8: 6, UInt8: 0>
==> 00000063: <GetByIdShort>: <Reg8: 6, Reg8: 5, UInt8: 1, string_id: 249>  # String: 'useEffect' (Identifier)
==> 00000068: <NewArray>: <Reg8: 5, UInt16: 1>
==> 0000006c: <DefineOwnInDenseArray>: <Reg8: 5, Reg8: 3, UInt8: 0>
==> 00000070: <CreateClosure>: <Reg8: 4, Reg8: 4, function_id: 10364>  # Function: [#10364  of 142 bytes]: 1 params @ offset 0x00216963
==> 00000075: <Call3>: <Reg8: 4, Reg8: 6, Reg8: 1, Reg8: 4, Reg8: 5>
==> 0000007b: <Ret>: <Reg8: 3>
"""


def test_arm_write_read_after_the_if_is_not_folded_away():
    js = Decompiler.render(Decompiler.build_context(_HASM, 4563, strict=False), verbose=False, raw=False)
    code = "\n".join(line for line in js.splitlines() if not line.strip().startswith("//"))

    assert "||" not in code
    assert "r7 = r8;" in code
    assert "__environment__[1] = r7;" in code
