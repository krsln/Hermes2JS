"""
Two guards that cross over a shared exit (98/11871):

    if (!unit)  goto L;  if (unit !== "px") goto EXIT;  L: if (n < 0) goto EXIT;  return n;  EXIT: return null;

The first test jumps into the middle of the second one's arm, so the pair is
not a plain `||` chain. It is merged into one condition (`!a || b`) instead of
being left as a `goto`, and neither exit may be dropped on the way.
"""

from hermes_decompiler.Decompiler import Decompiler

_HASM = r"""
=> [Function #11871 "reactNativeReanimated_filterTs2" of 38 bytes]: 2 params, frame size=5, strict=1, exc handler=0, debug info=0  @ offset 0x00231082

Bytecode listing:

==> 00000000: <LoadParam>: <Reg8: 3, UInt8: 1>
==> 00000003: <GetById>: <Reg8: 2, Reg8: 3, UInt8: 0, string_id: 12994>  # String: 'numberValue' (Identifier)
==> 00000009: <GetById>: <Reg8: 4, Reg8: 3, UInt8: 1, string_id: 7977>  # String: 'unit' (Identifier)
==> 0000000f: <JmpFalse>: <Addr8: 11, Reg8: 4>  # Address: 0000001a
==> 00000012: <LoadConstString>: <Reg8: 3, string_id: 307>  # String: 'px' (String)
==> 00000016: <JStrictNotEqual>: <Addr8: 12, Reg8: 4, Reg8: 3>  # Address: 00000022
==> 0000001a: <LoadConstZero>: <Reg8: 0>
==> 0000001c: <JLess>: <Addr8: 6, Reg8: 2, Reg8: 0>  # Address: 00000022
==> 00000020: <Ret>: <Reg8: 2>
==> 00000022: <LoadConstNull>: <Reg8: 1>
==> 00000024: <Ret>: <Reg8: 1>
"""


def test_crossed_guards_sharing_an_exit_have_no_goto_and_keep_both_exits():
    js = Decompiler.render(Decompiler.build_context(_HASM, 11871, strict=False), verbose=False, raw=False)
    code = "\n".join(line for line in js.splitlines() if not line.strip().startswith("//"))

    assert "goto" not in code
    assert "return r2;" in code
    assert "return null;" in code
    # both guards still reach the `null` exit
    assert 'r4 !== "px"' in code
    assert "r2 < 0" in code or "r2 >= 0" in code
