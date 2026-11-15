"""
A suspend point whose resume pair is followed by `Mov`s, and a `SaveGenerator` that
falls into its own resume address (96/6777, an `async` body):

    r1 = await getMethod(...)
    SaveGenerator -> R ; Ret r1            (the `Ret` is never reached)
    R: ResumeGenerator r1, r2
       Mov r4, r2                          (the return flag the guard tests)
       Mov r2, r1                          (the resumed value, read behind the guard)
       JmpFalse r4, ...

Three things went wrong, each leaving a raw `goto label_64` and `r2 = await yield;`:

1. `RedundantJumpRegionPass` took the `SaveGenerator` of the first arm for a bare jump
   to the next block and dropped the instruction with its jump;
2. `GeneratorStateMachineRegionPass` only knew a resume block that ENDS with the pair,
   so the `Mov`s hid it;
3. the unreachable `Ret` behind the first arm's save landed in the `then` arm of the
   SECOND arm's resume guard, so that guard held two `Ret`s and was not recognized.
"""

from hermes_decompiler.Decompiler import Decompiler

_HASM = r"""
=> [Function #6777 "?anon_0_" of 143 bytes]: 1 params, frame size=14, strict=1, exc handler=0, debug info=0  @ offset 0x001a3763

Bytecode listing:

==> 00000000: <StartGenerator>: <>
==> 00000001: <ResumeGenerator>: <Reg8: 0, Reg8: 1>
==> 00000004: <JmpTrueLong>: <Addr32: 136, Reg8: 1>  # Address: 0000008c
==> 0000000a: <GetGlobalObject>: <Reg8: 1>
==> 0000000c: <TryGetById>: <Reg8: 4, Reg8: 1, UInt8: 1, string_id: 24>  # String: 'Object' (Identifier)
==> 00000012: <GetByIdShort>: <Reg8: 2, Reg8: 4, UInt8: 2, string_id: 118>  # String: 'keys' (Identifier)
==> 00000017: <GetEnvironment>: <Reg8: 3, UInt8: 1>
==> 0000001a: <LoadFromEnvironment>: <Reg8: 1, Reg8: 3, UInt8: 5>
==> 0000001e: <Call2>: <Reg8: 1, Reg8: 2, Reg8: 4, Reg8: 1>
==> 00000023: <GetByIdShort>: <Reg8: 2, Reg8: 1, UInt8: 3, string_id: 169>  # String: 'length' (Identifier)
==> 00000028: <LoadConstZero>: <Reg8: 1>
==> 0000002a: <JGreater>: <Addr8: 37, Reg8: 2, Reg8: 1>  # Address: 0000004f
==> 0000002e: <LoadFromEnvironment>: <Reg8: 2, Reg8: 3, UInt8: 0>
==> 00000032: <GetById>: <Reg8: 1, Reg8: 2, UInt8: 4, string_id: 17625>  # String: 'getMethod' (Identifier)
==> 00000038: <Call1>: <Reg8: 1, Reg8: 1, Reg8: 2>
==> 0000003c: <SaveGenerator>: <Addr8: 4>  # Address: 00000040
==> 0000003e: <Ret>: <Reg8: 1>
==> 00000040: <ResumeGenerator>: <Reg8: 1, Reg8: 2>
==> 00000043: <Mov>: <Reg8: 4, Reg8: 2>
==> 00000046: <Mov>: <Reg8: 2, Reg8: 1>
==> 00000049: <JmpFalse>: <Addr8: 38, Reg8: 4>  # Address: 0000006f
==> 0000004c: <CompleteGenerator>: <>
==> 0000004d: <Ret>: <Reg8: 1>
==> 0000004f: <LoadFromEnvironment>: <Reg8: 5, Reg8: 3, UInt8: 0>
==> 00000053: <GetById>: <Reg8: 4, Reg8: 5, UInt8: 4, string_id: 17625>  # String: 'getMethod' (Identifier)
==> 00000059: <LoadFromEnvironment>: <Reg8: 1, Reg8: 3, UInt8: 5>
==> 0000005d: <Call2>: <Reg8: 1, Reg8: 4, Reg8: 5, Reg8: 1>
==> 00000062: <SaveGenerator>: <Addr8: 4>  # Address: 00000066
==> 00000064: <Ret>: <Reg8: 1>
==> 00000066: <ResumeGenerator>: <Reg8: 1, Reg8: 4>
==> 00000069: <Mov>: <Reg8: 2, Reg8: 1>
==> 0000006c: <JmpTrue>: <Addr8: 29, Reg8: 4>  # Address: 00000089
==> 0000006f: <LoadFromEnvironment>: <Reg8: 4, Reg8: 3, UInt8: 1>
==> 00000073: <GetByIdShort>: <Reg8: 4, Reg8: 4, UInt8: 5, string_id: 93>  # String: 'current' (Identifier)
==> 00000078: <JmpFalse>: <Addr8: 14, Reg8: 4>  # Address: 00000086
==> 0000007b: <LoadFromEnvironment>: <Reg8: 4, Reg8: 3, UInt8: 2>
==> 0000007f: <LoadConstUndefined>: <Reg8: 3>
==> 00000081: <Call2>: <Reg8: 3, Reg8: 4, Reg8: 3, Reg8: 2>
==> 00000086: <CompleteGenerator>: <>
==> 00000087: <Ret>: <Reg8: 2>
==> 00000089: <CompleteGenerator>: <>
==> 0000008a: <Ret>: <Reg8: 1>
==> 0000008c: <CompleteGenerator>: <>
==> 0000008d: <Ret>: <Reg8: 0>
"""


def _code() -> str:
    js = Decompiler.render(Decompiler.build_context(_HASM, 6777, strict=False), verbose=False, raw=False)

    return "\n".join(line for line in js.splitlines() if not line.strip().startswith("//"))


def test_resume_pair_followed_by_copies_is_folded_away():
    code = _code()

    assert "goto" not in code
    assert "__resumeIsReturn" not in code
    assert "await yield" not in code


def test_each_arm_binds_the_resumed_value_to_the_register_the_rest_reads():
    code = _code()

    # The `Mov r2, r1` copy is folded into the await that produced the value.
    assert "r2 = await r5.getMethod(r1);" in code
    assert "r2 = await r2.getMethod();" in code
    assert code.rstrip().endswith("return r2;\n}")
