"""
A value written in only ONE arm of an `if` that stays an `if` (no fold pass could
express it as `?:` / `||` / `??=`) leaves the register holding the DEFAULT on the
path that skips the arm. Code after the `if` reads the register by name, so the
default's own statement has to print - but a default that a condition consumed
inline (`LoadConstUInt8 r3, 100` -> `param1 > 100`) is flagged `definition_used`
and printed nowhere, so that path read a register nothing ever assigned.
"""

from hermes_decompiler.Decompiler import Decompiler

_CLAMP_HASM = """
=> [Function #15070 "ternaryTest" of 137 bytes]: 2 params, frame size=14, strict=1, exc handler=0, debug info=0  @ offset 0x002685a6

Bytecode listing:

==> 00000000: <LoadParam>: <Reg8: 2, UInt8: 1>
==> 00000003: <GetGlobalObject>: <Reg8: 0>
==> 00000005: <TryGetById>: <Reg8: 4, Reg8: 0, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
==> 0000000b: <GetByIdShort>: <Reg8: 3, Reg8: 4, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
==> 00000010: <LoadConstString>: <Reg8: 1, string_id: 4641>  # String: '__BC:ControlFlow/TernaryTests/ternaryTest/start' (String)
==> 00000014: <Call2>: <Reg8: 1, Reg8: 3, Reg8: 4, Reg8: 1>
==> 00000019: <LoadConstZero>: <Reg8: 1>
==> 0000001b: <Greater>: <Reg8: 3, Reg8: 2, Reg8: 1>
==> 0000001f: <LoadConstString>: <Reg8: 5, string_id: 866>  # String: 'positive' (String)
==> 00000023: <JmpTrue>: <Addr8: 21, Reg8: 3>  # Address: 00000038
==> 00000026: <Less>: <Reg8: 4, Reg8: 2, Reg8: 1>
==> 0000002a: <LoadConstString>: <Reg8: 3, string_id: 615>  # String: 'zero' (String)
==> 0000002e: <JmpFalse>: <Addr8: 7, Reg8: 4>  # Address: 00000035
==> 00000031: <LoadConstString>: <Reg8: 3, string_id: 1323>  # String: 'negative' (String)
==> 00000035: <Mov>: <Reg8: 5, Reg8: 3>
==> 00000038: <TryGetById>: <Reg8: 4, Reg8: 0, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
==> 0000003e: <GetByIdShort>: <Reg8: 3, Reg8: 4, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
==> 00000043: <Call2>: <Reg8: 3, Reg8: 3, Reg8: 4, Reg8: 5>
==> 00000048: <LoadConstUInt8>: <Reg8: 3, UInt8: 100>
==> 0000004b: <Greater>: <Reg8: 4, Reg8: 2, Reg8: 3>
==> 0000004f: <JmpTrue>: <Addr8: 18, Reg8: 4>  # Address: 00000061
==> 00000052: <Less>: <Reg8: 4, Reg8: 2, Reg8: 1>
==> 00000056: <LoadConstZero>: <Reg8: 1>
==> 00000058: <JmpTrue>: <Addr8: 6, Reg8: 4>  # Address: 0000005e
==> 0000005b: <Mov>: <Reg8: 1, Reg8: 2>
==> 0000005e: <Mov>: <Reg8: 3, Reg8: 1>
==> 00000061: <TryGetById>: <Reg8: 2, Reg8: 0, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
==> 00000067: <GetByIdShort>: <Reg8: 1, Reg8: 2, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
==> 0000006c: <Call2>: <Reg8: 1, Reg8: 1, Reg8: 2, Reg8: 3>
==> 00000071: <TryGetById>: <Reg8: 2, Reg8: 0, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
==> 00000077: <GetByIdShort>: <Reg8: 1, Reg8: 2, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
==> 0000007c: <LoadConstString>: <Reg8: 0, string_id: 3481>  # String: '__BC:ControlFlow/TernaryTests/ternaryTest/end' (String)
==> 00000080: <Call2>: <Reg8: 0, Reg8: 1, Reg8: 2, Reg8: 0>
==> 00000085: <LoadConstUndefined>: <Reg8: 0>
==> 00000087: <Ret>: <Reg8: 0>
"""


def _code(hasm, function_id):
    out = Decompiler.render(Decompiler.build_context(hasm, function_id), verbose=False)
    return "\n".join(line for line in out.splitlines() if not line.strip().startswith("//"))


def test_default_consumed_by_the_condition_is_still_assigned_on_the_skipping_path():
    # `r3 = 100; if (param1 > 100) skip; ...; r3 = clamped; console.log(r3)`:
    # when param1 > 100 nothing else sets r3, so `r3 = 100` must print.
    code = _code(_CLAMP_HASM, 15070)

    assert "r3 = 100;" in code
    assert code.index("r3 = 100;") < code.index("if (param1 <= 100) {")
    assert code.index("if (param1 <= 100) {") < code.index("console.log(r3);")


def test_default_that_already_prints_is_not_printed_twice():
    # `r5 = "positive"` is not consumed inline, so it already prints once.
    code = _code(_CLAMP_HASM, 15070)

    assert code.count('r5 = "positive";') == 1


_ARM_NAMED_AFTER_IF_HASM = """
=> [Function #9643 "y" of 92 bytes]: 2 params, frame size=16, strict=1, exc handler=0, debug info=0  @ offset 0x00206171

Bytecode listing:

==> 00000000: <GetParentEnvironment>: <Reg8: 3, UInt8: 0>
==> 00000003: <GetGlobalObject>: <Reg8: 1>
==> 00000005: <GetById>: <Reg8: 2, Reg8: 1, UInt8: 0, string_id: 10621>  # String: 'queueMicrotask' (Identifier)
==> 0000000b: <JmpTypeOfIs>: <Addr32: 56, Reg8: 2, UInt16: 128>  # Address: 00000043
==> 00000013: <CreateFunctionEnvironment>: <Reg8: 2, UInt8: 1>
==> 00000016: <LoadFromEnvironment>: <Reg8: 6, Reg8: 3, UInt8: 3>
==> 0000001a: <CreateThisForNew>: <Reg8: 5, Reg8: 6, UInt8: 1>
==> 0000001e: <CreateTopLevelEnvironment>: <Reg8: 4, UInt32: 1>
==> 00000024: <CreateClosure>: <Reg8: 7, Reg8: 4, function_id: 12507>  # Function: [#12507  of 19 bytes]: 2 params @ offset 0x00210ffa
==> 00000029: <Mov>: <Reg8: 8, Reg8: 5>
==> 0000002c: <Construct>: <Reg8: 4, Reg8: 6, UInt8: 2>
==> 00000030: <SelectObject>: <Reg8: 4, Reg8: 5, Reg8: 4>
==> 00000034: <StoreToEnvironment>: <Reg8: 2, UInt8: 0, Reg8: 4>
==> 00000038: <CreateClosure>: <Reg8: 2, Reg8: 2, function_id: 12552>  # Function: [#12552 y of 47 bytes]: 2 params @ offset 0x00245474
==> 0000003d: <StoreToEnvironment>: <Reg8: 3, UInt8: 12, Reg8: 2>
==> 00000041: <Jmp>: <Addr8: 15>  # Address: 00000050
==> 00000043: <TryGetById>: <Reg8: 1, Reg8: 1, UInt8: 0, string_id: 10621>  # String: 'queueMicrotask' (Identifier)
==> 00000049: <StoreToEnvironment>: <Reg8: 3, UInt8: 12, Reg8: 1>
==> 0000004d: <Mov>: <Reg8: 2, Reg8: 1>
==> 00000050: <LoadParam>: <Reg8: 1, UInt8: 1>
==> 00000053: <LoadConstUndefined>: <Reg8: 0>
==> 00000055: <Call2>: <Reg8: 1, Reg8: 2, Reg8: 0, Reg8: 1>
==> 0000005a: <Ret>: <Reg8: 1>
"""


def test_an_arm_write_the_code_after_the_if_names_still_prints():
    # `r2` is written on BOTH paths (`queueMicrotask` / the `y` closure) and is
    # read by name after the `if` (`r2.call(...)`). The else arm's `r2 = y` is
    # also inlined into `r3[12] = y` inside the arm; that used to be taken as
    # "used" and left that path calling an `r2` nothing had assigned.
    code = _code(_ARM_NAMED_AFTER_IF_HASM, 9643)

    assert "r2 = queueMicrotask;" in code
    assert "r2 = y;" in code
    assert code.index("r2 = y;") < code.index("r2.call(")


_NESTED_IF_CONST_HASM = """

=> [Function #13356 "" of 74 bytes]: 2 params, frame size=15, strict=1, exc handler=0, debug info=0  @ offset 0x00257d42

Bytecode listing:

==> 00000000: <GetParentEnvironment>: <Reg8: 3, UInt8: 0>
==> 00000003: <LoadParam>: <Reg8: 5, UInt8: 1>
==> 00000006: <LoadFromEnvironment>: <Reg8: 4, Reg8: 3, UInt8: 0>
==> 0000000a: <JmpTypeOfIs>: <Addr32: 34, Reg8: 5, UInt16: 128>  # Address: 0000002c
==> 00000012: <LoadConstUndefined>: <Reg8: 0>
==> 00000014: <LoadConstNull>: <Reg8: 1>
==> 00000016: <LoadConstUndefined>: <Reg8: 2>
==> 00000018: <JStrictEqual>: <Addr8: 27, Reg8: 5, Reg8: 1>  # Address: 00000033
==> 0000001c: <LoadConstUndefined>: <Reg8: 2>
==> 0000001e: <JStrictEqual>: <Addr8: 21, Reg8: 5, Reg8: 0>  # Address: 00000033
==> 00000022: <PutByIdStrict>: <Reg8: 5, Reg8: 4, UInt8: 0, string_id: 57>  # String: 'current' (Identifier)
==> 00000028: <LoadConstUndefined>: <Reg8: 2>
==> 0000002a: <Jmp>: <Addr8: 9>  # Address: 00000033
==> 0000002c: <LoadConstUndefined>: <Reg8: 0>
==> 0000002e: <Call2>: <Reg8: 2, Reg8: 5, Reg8: 0, Reg8: 4>
==> 00000033: <LoadFromEnvironment>: <Reg8: 0, Reg8: 3, UInt8: 1>
==> 00000037: <JmpTrue>: <Addr8: 17, Reg8: 0>  # Address: 00000048
==> 0000003a: <JmpTypeOfIs>: <Addr32: 14, Reg8: 2, UInt16: 383>  # Address: 00000048
==> 00000042: <LoadConstTrue>: <Reg8: 0>
==> 00000044: <StoreNPToEnvironment>: <Reg8: 3, UInt8: 1, Reg8: 0>
==> 00000048: <Ret>: <Reg8: 2>
"""


def test_a_printed_constant_between_nested_ifs_is_not_looked_past():
    # `if (p !== null) { r2 = undefined; if (p !== undefined) {...} }`: the
    # `r2 = undefined` between the two tests is a printed definition later code
    # reads by name, so the ifs must not be folded into one `&&` that drops it.
    code = _code(_NESTED_IF_CONST_HASM, 13356)

    assert "param1 !== null && param1 !== undefined" not in code
    assert "if (param1 !== undefined) {" in code
    assert code.index("if (param1 !== null) {") < code.index("if (param1 !== undefined) {")
