"""
A constructor call in one arm of an `if`, read after it (`AnimatedAddition`,
96/5146):

    this._a = typeof a === "number" ? new AnimatedValue(a) : a

The arm's `SelectObject` result held the `Construct`, which the reader after the
`if` inlined: `r0._a = new r3(r11)` ran the constructor on BOTH paths (and
with `r3`/`r11`, set inside the arm, unassigned on the path that skips it).
`UnfoldedMergeRepairPass` refused every side-effecting arm value for fear of
running it twice; repointing the reader MOVES the effect instead.
"""

from hermes_decompiler.Decompiler import Decompiler

_ANIMATED_ADDITION = r"""

=> [Function #5146 "AnimatedAddition" of 165 bytes]: 4 params, frame size=19, strict=1, exc handler=0, debug info=0  @ offset 0x0017e712

Bytecode listing:

==> 00000000: <LoadParam>: <Reg8: 7, UInt8: 1>
==> 00000003: <LoadParam>: <Reg8: 4, UInt8: 2>
==> 00000006: <LoadParam>: <Reg8: 6, UInt8: 0>
==> 00000009: <GetEnvironment>: <Reg8: 2, UInt8: 1>
==> 0000000c: <LoadFromEnvironment>: <Reg8: 0, Reg8: 2, UInt8: 0>
==> 00000010: <GetByIdShort>: <Reg8: 0, Reg8: 0, UInt8: 1, string_id: 107>  # String: 'default' (Identifier)
==> 00000015: <GetEnvironment>: <Reg8: 1, UInt8: 0>
==> 00000018: <LoadFromEnvironment>: <Reg8: 5, Reg8: 1, UInt8: 0>
==> 0000001c: <LoadConstUndefined>: <Reg8: 3>
==> 0000001e: <Call3>: <Reg8: 0, Reg8: 0, Reg8: 3, Reg8: 6, Reg8: 5>
==> 00000024: <LoadFromEnvironment>: <Reg8: 0, Reg8: 2, UInt8: 2>
==> 00000028: <GetByIdShort>: <Reg8: 1, Reg8: 0, UInt8: 1, string_id: 107>  # String: 'default' (Identifier)
==> 0000002d: <NewArray>: <Reg8: 0, UInt16: 1>
==> 00000031: <LoadParam>: <Reg8: 8, UInt8: 3>
==> 00000034: <PutOwnByIndex>: <Reg8: 0, Reg8: 8, UInt8: 0>
==> 00000038: <Call4>: <Reg8: 0, Reg8: 1, Reg8: 3, Reg8: 6, Reg8: 5, Reg8: 0>
==> 0000003f: <TypeOf>: <Reg8: 3, Reg8: 7>
==> 00000042: <LoadConstString>: <Reg8: 5, string_id: 7552>  # String: 'number' (Identifier)
==> 00000046: <Mov>: <Reg8: 1, Reg8: 7>
==> 00000049: <JStrictNotEqual>: <Addr8: 36, Reg8: 3, Reg8: 5>  # Address: 0000006d
==> 0000004d: <LoadFromEnvironment>: <Reg8: 3, Reg8: 2, UInt8: 6>
==> 00000051: <GetByIdShort>: <Reg8: 3, Reg8: 3, UInt8: 1, string_id: 107>  # String: 'default' (Identifier)
==> 00000056: <GetByIdShort>: <Reg8: 6, Reg8: 3, UInt8: 2, string_id: 206>  # String: 'prototype' (Identifier)
==> 0000005b: <CreateThis>: <Reg8: 6, Reg8: 6, Reg8: 3>
==> 0000005f: <Mov>: <Reg8: 12, Reg8: 6>
==> 00000062: <Mov>: <Reg8: 11, Reg8: 7>
==> 00000065: <Construct>: <Reg8: 3, Reg8: 3, UInt8: 2>
==> 00000069: <SelectObject>: <Reg8: 1, Reg8: 6, Reg8: 3>
==> 0000006d: <PutById>: <Reg8: 0, Reg8: 1, UInt8: 1, string_id: 7361>  # String: '_a' (Identifier)
==> 00000073: <TypeOf>: <Reg8: 3, Reg8: 4>
==> 00000076: <Mov>: <Reg8: 1, Reg8: 4>
==> 00000079: <JStrictNotEqual>: <Addr8: 36, Reg8: 3, Reg8: 5>  # Address: 0000009d
==> 0000007d: <LoadFromEnvironment>: <Reg8: 2, Reg8: 2, UInt8: 6>
==> 00000081: <GetByIdShort>: <Reg8: 2, Reg8: 2, UInt8: 1, string_id: 107>  # String: 'default' (Identifier)
==> 00000086: <GetByIdShort>: <Reg8: 3, Reg8: 2, UInt8: 2, string_id: 206>  # String: 'prototype' (Identifier)
==> 0000008b: <CreateThis>: <Reg8: 3, Reg8: 3, Reg8: 2>
==> 0000008f: <Mov>: <Reg8: 12, Reg8: 3>
==> 00000092: <Mov>: <Reg8: 11, Reg8: 4>
==> 00000095: <Construct>: <Reg8: 2, Reg8: 2, UInt8: 2>
==> 00000099: <SelectObject>: <Reg8: 1, Reg8: 3, Reg8: 2>
==> 0000009d: <PutById>: <Reg8: 0, Reg8: 1, UInt8: 2, string_id: 11393>  # String: '_b' (Identifier)
==> 000000a3: <Ret>: <Reg8: 0>
"""


def _render() -> str:
    context = Decompiler.build_context(_ANIMATED_ADDITION, 5146, strict=False)

    return Decompiler.render(context, verbose=False, raw=False)


def test_constructor_runs_only_in_the_arm_that_takes_it():
    js = _render()

    assert "r0._a = new" not in js
    assert "r0._b = new" not in js
    assert js.count("new r") == 2  # one per arm, nowhere else


def test_the_join_value_is_named_after_the_if():
    js = _render()

    assert "r1 = new r3(r11);" in js
    assert "r0._a = r1;" in js
    assert "r0._b = r1;" in js
