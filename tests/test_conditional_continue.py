"""
`if (c) continue;` compiled as a conditional branch back to the loop (96/5924,
an `assign`-like `for (k in src) { if (src[k] == null) continue; dst[k] = src[k]; }`):

    JEqual r8, r1 -> header      # taken: next iteration
    <rest of the body>
    Jmp -> header

No structurer took a conditional BACKWARD branch (`IfStructurer` leaves them to
the loop guard, `LoopContinueRegionPass` only knows unconditional jumps), so the
function printed `if (r8 == null) goto label_19;` and was not valid JavaScript.
"""

from hermes_decompiler.Decompiler import Decompiler

_ASSIGN = r"""

=> [Function #5924 "" of 51 bytes]: 3 params, frame size=10, strict=1, exc handler=0, debug info=0  @ offset 0x00191c56

Bytecode listing:

==> 00000000: <LoadParam>: <Reg8: 0, UInt8: 1>
==> 00000003: <LoadParam>: <Reg8: 7, UInt8: 2>
==> 00000006: <Mov>: <Reg8: 5, Reg8: 7>
==> 00000009: <LoadConstNull>: <Reg8: 1>
==> 0000000b: <GetPNameList>: <Reg8: 6, Reg8: 5, Reg8: 4, Reg8: 3>
==> 00000010: <JmpUndefined>: <Addr8: 33, Reg8: 6>  # Address: 00000031
==> 00000013: <GetNextPName>: <Reg8: 2, Reg8: 6, Reg8: 5, Reg8: 4, Reg8: 3>
==> 00000019: <JmpUndefined>: <Addr8: 24, Reg8: 2>  # Address: 00000031
==> 0000001c: <Mov>: <Reg8: 9, Reg8: 2>
==> 0000001f: <GetByVal>: <Reg8: 8, Reg8: 7, Reg8: 9>
==> 00000023: <JEqual>: <Addr8: -16, Reg8: 8, Reg8: 1>  # Address: 00000013
==> 00000027: <GetByVal>: <Reg8: 8, Reg8: 7, Reg8: 9>
==> 0000002b: <PutByVal>: <Reg8: 0, Reg8: 9, Reg8: 8>
==> 0000002f: <Jmp>: <Addr8: -28>  # Address: 00000013
==> 00000031: <Ret>: <Reg8: 0>
"""


def _render() -> str:
    context = Decompiler.build_context(_ASSIGN, 5924, strict=False)

    return Decompiler.render(context, verbose=False, raw=False)


def test_conditional_branch_back_to_the_loop_is_a_continue():
    js = _render()

    assert "goto" not in js
    assert "if (r8 == null) {\n            continue;\n        }" in js
    assert js.index("continue;") < js.index("param1[r9] = param2[r9];")
