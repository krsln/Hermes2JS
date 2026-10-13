"""
A shared `r0 = false; return r0` block (the `typeof a === ... || x === null`
guard shape, 98/2336 and 98/5366) is copied per jumper like a bare `return`,
so no `goto label_N` is left behind. When the arms then end in the same
`return rN` with different values (98/5366, 98/4378), the merged return stays
`return rN` and every arm prints its own `rN = ...`.
"""

import re

from hermes_decompiler.Decompiler import Decompiler

_IS_IGNORED = """
=> [Function #2336 "isIgnored" of 40 bytes]: 2 params, frame size=13, strict=1, exc handler=0, debug info=0  @ offset 0x001655dd

Bytecode listing:

==> 00000000: <LoadParam>: <Reg8: 3, UInt8: 1>
==> 00000003: <JmpTypeOfIs>: <Addr32: 14, Reg8: 3, UInt16: 253>  # Address: 00000011
==> 0000000b: <LoadConstNull>: <Reg8: 0>
==> 0000000d: <JNotEqual>: <Addr8: 8, Reg8: 3, Reg8: 0>  # Address: 00000015
==> 00000011: <LoadConstFalse>: <Reg8: 0>
==> 00000013: <Ret>: <Reg8: 0>
==> 00000015: <GetParentEnvironment>: <Reg8: 1, UInt8: 0>
==> 00000018: <LoadFromEnvironment>: <Reg8: 2, Reg8: 1, UInt8: 0>
==> 0000001c: <GetByIdShort>: <Reg8: 1, Reg8: 2, UInt8: 0, string_id: 11>  # String: 'has' (Identifier)
==> 00000021: <Call2>: <Reg8: 1, Reg8: 1, Reg8: 2, Reg8: 3>
==> 00000026: <Ret>: <Reg8: 1>


"""

_IS_PLAIN_OBJECT = """
=> [Function #5366 "isPlainObject" of 57 bytes]: 2 params, frame size=14, strict=1, exc handler=0, debug info=0  @ offset 0x001b1899

Bytecode listing:

==> 00000000: <LoadParam>: <Reg8: 4, UInt8: 1>
==> 00000003: <JmpTypeOfIs>: <Addr32: 14, Reg8: 4, UInt16: 253>  # Address: 00000011
==> 0000000b: <LoadConstNull>: <Reg8: 0>
==> 0000000d: <JStrictNotEqual>: <Addr8: 8, Reg8: 4, Reg8: 0>  # Address: 00000015
==> 00000011: <LoadConstFalse>: <Reg8: 0>
==> 00000013: <Ret>: <Reg8: 0>
==> 00000015: <GetGlobalObject>: <Reg8: 1>
==> 00000017: <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 0, string_id: 23>  # String: 'Object' (Identifier)
==> 0000001d: <GetById>: <Reg8: 2, Reg8: 3, UInt8: 1, string_id: 6472>  # String: 'getPrototypeOf' (Identifier)
==> 00000023: <Call2>: <Reg8: 2, Reg8: 2, Reg8: 3, Reg8: 4>
==> 00000028: <TryGetById>: <Reg8: 1, Reg8: 1, UInt8: 0, string_id: 23>  # String: 'Object' (Identifier)
==> 0000002e: <GetByIdShort>: <Reg8: 1, Reg8: 1, UInt8: 2, string_id: 212>  # String: 'prototype' (Identifier)
==> 00000033: <StrictEq>: <Reg8: 0, Reg8: 2, Reg8: 1>
==> 00000037: <Ret>: <Reg8: 0>


"""

_ARE_INPUTS_EQUAL = """
=> [Function #4378 "areInputsEqual" of 113 bytes]: 3 params, frame size=22, strict=1, exc handler=0, debug info=0  @ offset 0x001a1d77

Bytecode listing:

==> 00000000: <GetParentEnvironment>: <Reg8: 10, UInt8: 0>
==> 00000003: <LoadParam>: <Reg8: 9, UInt8: 1>
==> 00000006: <LoadParam>: <Reg8: 8, UInt8: 2>
==> 00000009: <GetByIdShort>: <Reg8: 11, Reg8: 9, UInt8: 0, string_id: 177>  # String: 'length' (Identifier)
==> 0000000e: <GetByIdShort>: <Reg8: 7, Reg8: 8, UInt8: 0, string_id: 177>  # String: 'length' (Identifier)
==> 00000013: <JStrictNotEqual>: <Addr8: 90, Reg8: 11, Reg8: 7>  # Address: 0000006d
==> 00000017: <GetByIdShort>: <Reg8: 7, Reg8: 9, UInt8: 0, string_id: 177>  # String: 'length' (Identifier)
==> 0000001c: <LoadConstZero>: <Reg8: 0>
==> 0000001e: <Less>: <Reg8: 3, Reg8: 0, Reg8: 7>
==> 00000022: <LoadConstUInt8>: <Reg8: 2, UInt8: 1>
==> 00000025: <LoadConstTrue>: <Reg8: 4>
==> 00000027: <LoadConstUndefined>: <Reg8: 5>
==> 00000029: <LoadConstFalse>: <Reg8: 6>
==> 0000002b: <JmpFalse>: <Addr8: 64, Reg8: 3>  # Address: 0000006b
==> 0000002e: <GetByVal>: <Reg8: 12, Reg8: 9, Reg8: 0>
==> 00000032: <GetByVal>: <Reg8: 11, Reg8: 8, Reg8: 0>
==> 00000036: <Mov>: <Reg8: 1, Reg8: 0>
==> 00000039: <LoadConstTrue>: <Reg8: 3>
==> 0000003b: <JStrictEqual>: <Addr8: 30, Reg8: 12, Reg8: 11>  # Address: 00000059
==> 0000003f: <LoadFromEnvironment>: <Reg8: 7, Reg8: 10, UInt8: 0>
==> 00000043: <Call2>: <Reg8: 12, Reg8: 7, Reg8: 5, Reg8: 12>
==> 00000048: <LoadConstFalse>: <Reg8: 3>
==> 0000004a: <JmpFalse>: <Addr8: 15, Reg8: 12>  # Address: 00000059
==> 0000004d: <Call2>: <Reg8: 7, Reg8: 7, Reg8: 5, Reg8: 11>
==> 00000052: <LoadConstFalse>: <Reg8: 3>
==> 00000054: <JmpFalse>: <Addr8: 5, Reg8: 7>  # Address: 00000059
==> 00000057: <LoadConstTrue>: <Reg8: 3>
==> 00000059: <JmpTrue>: <Addr8: 5, Reg8: 3>  # Address: 0000005e
==> 0000005c: <Ret>: <Reg8: 6>
==> 0000005e: <AddN>: <Reg8: 0, Reg8: 1, Reg8: 2>
==> 00000062: <GetByIdShort>: <Reg8: 7, Reg8: 9, UInt8: 0, string_id: 177>  # String: 'length' (Identifier)
==> 00000067: <JLess>: <Addr8: -57, Reg8: 0, Reg8: 7>  # Address: 0000002e
==> 0000006b: <Ret>: <Reg8: 4>
==> 0000006d: <LoadConstFalse>: <Reg8: 4>
==> 0000006f: <Ret>: <Reg8: 4>


"""


def _js(hasm, index):
    return Decompiler.render(Decompiler.build_context(hasm, index, strict=False), verbose=False, raw=False)


def test_constant_return_shared_by_a_guard_chain_has_no_goto():
    js = _js(_IS_IGNORED, 2336)

    assert "goto" not in js
    # One `return false` for the whole guard (`!(a && b)` folded to one test),
    # not one per jumper: both exits are the same constant.
    assert js.count("return false;") == 1
    assert "return r1;" in js


def test_arms_returning_different_values_keep_the_register_return():
    js = _js(_IS_PLAIN_OBJECT, 5366)

    assert "goto" not in js
    assert js.count("r0 = false;") == 1
    assert "r0 = r2 === Object.prototype;" in js
    assert re.search(r"return r0;\n}$", js.strip())


def test_constant_defined_before_the_if_is_printed_when_return_is_merged():
    js = _js(_ARE_INPUTS_EQUAL, 4378)

    assert "r4 = false;" in js
    assert "r4 = true;" in js
    assert js.strip().endswith("return r4;\n}")
