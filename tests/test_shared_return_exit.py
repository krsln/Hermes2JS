"""
One `return` block shared by two early exits in different `if` arms, with an
`||`-style join behind them (`maybeSwapComponents`, 96/9150):

    if (!(p[0] in A)) return p;            // jumps to the shared `return p`
    if (p[1] !== undefined && !(p[1] in B)) return p;   // falls into it
    ...swap...

The block belonged to the first branch only; the second test lost its exit
and the swap code ended up under `r5 === undefined` alone.
`SharedReturnDuplicationCfgPass` gives each jumper its own copy and
`_DominanceIfBuilder` treats the shared `||` target as the join.
"""

import re

from hermes_decompiler.Decompiler import Decompiler

_HASM = """
=> [Function #9150 "maybeSwapComponents" of 107 bytes]: 2 params, frame size=16, strict=1, exc handler=0, debug info=0  @ offset 0x001d6a13

Bytecode listing:

==> 00000000: <LoadParam>: <Reg8: 1, UInt8: 1>
==> 00000003: <LoadConstZero>: <Reg8: 4>
==> 00000005: <GetByVal>: <Reg8: 3, Reg8: 1, Reg8: 4>
==> 00000009: <GetEnvironment>: <Reg8: 0, UInt8: 0>
==> 0000000c: <LoadFromEnvironment>: <Reg8: 2, Reg8: 0, UInt8: 0>
==> 00000010: <IsIn>: <Reg8: 2, Reg8: 3, Reg8: 2>
==> 00000014: <JmpFalse>: <Addr8: 31, Reg8: 2>  # Address: 00000033
==> 00000017: <LoadConstUInt8>: <Reg8: 2, UInt8: 1>
==> 0000001a: <GetByVal>: <Reg8: 5, Reg8: 1, Reg8: 2>
==> 0000001e: <LoadConstUndefined>: <Reg8: 3>
==> 00000020: <JStrictEqual>: <Addr8: 21, Reg8: 5, Reg8: 3>  # Address: 00000035
==> 00000024: <GetByVal>: <Reg8: 3, Reg8: 1, Reg8: 2>
==> 00000028: <LoadFromEnvironment>: <Reg8: 0, Reg8: 0, UInt8: 1>
==> 0000002c: <IsIn>: <Reg8: 0, Reg8: 3, Reg8: 0>
==> 00000030: <JmpTrue>: <Addr8: 5, Reg8: 0>  # Address: 00000035
==> 00000033: <Ret>: <Reg8: 1>
==> 00000035: <NewArray>: <Reg8: 0, UInt16: 0>
==> 00000039: <Mov>: <Reg8: 8, Reg8: 0>
==> 0000003c: <Mov>: <Reg8: 7, Reg8: 1>
==> 0000003f: <LoadConstZero>: <Reg8: 6>
==> 00000041: <CallBuiltin>: <Reg8: 1, UInt8: 46, UInt8: 4>  # Built-in function: [#46 arraySpread]
==> 00000045: <GetByVal>: <Reg8: 3, Reg8: 0, Reg8: 2>
==> 00000049: <NewArray>: <Reg8: 1, UInt16: 2>
==> 0000004d: <PutOwnByIndex>: <Reg8: 1, Reg8: 3, UInt8: 0>
==> 00000051: <GetByVal>: <Reg8: 3, Reg8: 0, Reg8: 4>
==> 00000055: <PutOwnByIndex>: <Reg8: 1, Reg8: 3, UInt8: 1>
==> 00000059: <GetByVal>: <Reg8: 3, Reg8: 1, Reg8: 4>
==> 0000005d: <PutByVal>: <Reg8: 0, Reg8: 4, Reg8: 3>
==> 00000061: <GetByVal>: <Reg8: 1, Reg8: 1, Reg8: 2>
==> 00000065: <PutByVal>: <Reg8: 0, Reg8: 2, Reg8: 1>
==> 00000069: <Ret>: <Reg8: 0>
"""


def test_the_swap_runs_after_both_checks_and_both_exits_stay():
    out = Decompiler.render(Decompiler.build_context(_HASM, 9150), verbose=False)

    assert "goto" not in out, out
    assert out.count("return param1;") == 2, out
    assert re.search(r"if \(r5 !== undefined\) \{.*?if \(!r0\) \{\s*return param1;\s*\}\s*\}\s*r0 = \[\];", out, re.S), out
