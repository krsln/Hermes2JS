"""
A value loaded from memory is stale once a store to that location ran.

    r0 = param1.x;      // load
    param1.x = null;    // store to the same location
    return r0;          // must still be the OLD value

`ReturnValueResolutionPass` folded `return r0` back into `param1.x`, and
`get_register_expression` inlined it into a later reader, so both read the
value AFTER the store (the `throw r3[25]` of `processEventQueue`).
A store to a different property, or to a deeper chain, leaves it valid.
"""

from hermes_decompiler.Decompiler import Decompiler

_HEADER = """
=> [Function #1 "f" of 40 bytes]: 2 params, frame size=4, strict=1, exc handler=0, debug info=0  @ offset 0x00000000

Bytecode listing:

"""

_X = "string_id: 10143>  # String: 'x' (Identifier)"
_Y = "string_id: 10144>  # String: 'y' (Identifier)"


def _render(body: str) -> str:
    return Decompiler.render(Decompiler.build_context(_HEADER + body, 1), verbose=False)


def test_return_does_not_read_through_a_store_to_the_same_property():
    out = _render(f"""
==> 00000000: <LoadParam>: <Reg8: 1, UInt8: 1>
==> 00000003: <GetById>: <Reg8: 0, Reg8: 1, UInt8: 0, {_X}
==> 00000009: <LoadConstNull>: <Reg8: 2>
==> 0000000b: <PutById>: <Reg8: 1, Reg8: 2, UInt8: 0, {_X}
==> 00000011: <Ret>: <Reg8: 0>
""")

    assert "r0 = param1.x;" in out, out
    assert "return r0;" in out, out


def test_return_still_folds_across_a_store_to_another_property():
    out = _render(f"""
==> 00000000: <LoadParam>: <Reg8: 1, UInt8: 1>
==> 00000003: <GetById>: <Reg8: 0, Reg8: 1, UInt8: 0, {_X}
==> 00000009: <LoadConstNull>: <Reg8: 2>
==> 0000000b: <PutById>: <Reg8: 1, Reg8: 2, UInt8: 0, {_Y}
==> 00000011: <Ret>: <Reg8: 0>
""")

    assert "return param1.x;" in out, out


def test_a_later_reader_does_not_inline_a_load_across_the_store():
    out = _render(f"""
==> 00000000: <LoadParam>: <Reg8: 1, UInt8: 1>
==> 00000003: <GetById>: <Reg8: 0, Reg8: 1, UInt8: 0, {_X}
==> 00000009: <LoadConstNull>: <Reg8: 2>
==> 0000000b: <PutById>: <Reg8: 1, Reg8: 2, UInt8: 0, {_X}
==> 00000011: <LoadConstUInt8>: <Reg8: 3, UInt8: 1>
==> 00000014: <Add>: <Reg8: 3, Reg8: 0, Reg8: 3>
==> 00000018: <Ret>: <Reg8: 3>
""")

    assert "r0 = param1.x;" in out, out
    assert "r0 + 1" in out, out
