"""
A value test with a pure setup load in front of its second condition
(`loop`, 96/5242, the default of a destructured parameter):

    A: JNotGreater  len, 1  -> NEW          # taken: no argument at all
    B: r0 = arguments[1]; JStrictNotEqual r0, undefined -> USE
    NEW: r0 = {}                            # reached from A (taken) AND B (fall-through)
    USE: r0 = arguments[1]

`NEW` has two predecessors, the crossed `!a || b` shape, but `ShortCircuitCondition
CfgPass` only accepted a setup block made of constants the condition had already
inlined. `B`'s `GetArgumentsPropByVal` is a pure value that both exits overwrite,
so it is substituted into the test and the two blocks become one condition.
Before, the function printed `if (r0 !== undefined) goto label_26;`.
"""

from hermes_decompiler.Decompiler import Decompiler

_LOOP = r"""

=> [Function #5242 "loop" of 45 bytes]: 2 params, frame size=4, strict=1, exc handler=0, debug info=0  @ offset 0x0017fffc

Bytecode listing:

==> 00000000: <LoadConstUndefined>: <Reg8: 3>
==> 00000002: <LoadConstUndefined>: <Reg8: 2>
==> 00000004: <GetArgumentsLength>: <Reg8: 0, Reg8: 2>
==> 00000007: <LoadConstUInt8>: <Reg8: 1, UInt8: 1>
==> 0000000a: <JNotGreater>: <Addr8: 12, Reg8: 0, Reg8: 1>  # Address: 00000016
==> 0000000e: <GetArgumentsPropByVal>: <Reg8: 0, Reg8: 1, Reg8: 2>
==> 00000012: <JStrictNotEqual>: <Addr8: 8, Reg8: 0, Reg8: 3>  # Address: 0000001a
==> 00000016: <NewObject>: <Reg8: 0>
==> 00000018: <Jmp>: <Addr8: 6>  # Address: 0000001e
==> 0000001a: <GetArgumentsPropByVal>: <Reg8: 0, Reg8: 1, Reg8: 2>
==> 0000001e: <GetById>: <Reg8: 0, Reg8: 0, UInt8: 1, string_id: 7391>  # String: 'iterations' (Identifier)
==> 00000024: <GetEnvironment>: <Reg8: 0, UInt8: 0>
==> 00000027: <LoadFromEnvironment>: <Reg8: 0, Reg8: 0, UInt8: 1>
==> 0000002b: <Ret>: <Reg8: 0>
"""


def test_pure_setup_in_front_of_the_second_test_is_folded():
    context = Decompiler.build_context(_LOOP, 5242, strict=False)
    js = Decompiler.render(context, verbose=False, raw=False)

    assert "goto" not in js
    assert "if (r0 > 1 && arguments[1] !== undefined) {" in js
