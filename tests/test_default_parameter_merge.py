"""
A9: a value merged at an `if` is read after it.

- `defaultParameterTest`: the inner ternary fold handed the `Add` after the outer
  `if` a COPY of its value (`(r3 === undefined) ? 10 : arguments[1]`), so on the
  path that skips the outer `if` the parameter default was never read - and
  `r3` is not even assigned there. The reader has to name `r5`.
- `shouldFilter`: `UnfoldedMergeRepairPass` repointed every structural copy of an
  arm's `r4[0]`, including the definition `r4 = r4[0]` of another arm, which
  became `r4 = r6`.
"""

from hermes_decompiler.Decompiler import Decompiler

_DEFAULT_PARAMETER_HASM = """
=> [Function #15154 "defaultParameterTest" of 121 bytes]: 2 params, frame size=16, strict=1, exc handler=0, debug info=0  @ offset 0x0026aa9c

Bytecode listing:

==> 00000000: <LoadConstUndefined>: <Reg8: 0>
==> 00000002: <LoadConstUndefined>: <Reg8: 2>
==> 00000004: <GetArgumentsLength>: <Reg8: 3, Reg8: 2>
==> 00000007: <LoadConstUInt8>: <Reg8: 1, UInt8: 1>
==> 0000000a: <Greater>: <Reg8: 3, Reg8: 3, Reg8: 1>
==> 0000000e: <LoadConstUInt8>: <Reg8: 4, UInt8: 10>
==> 00000011: <Mov>: <Reg8: 5, Reg8: 4>
==> 00000014: <JmpFalse>: <Addr8: 18, Reg8: 3>  # Address: 00000026
==> 00000017: <GetArgumentsPropByVal>: <Reg8: 3, Reg8: 1, Reg8: 2>
==> 0000001b: <Mov>: <Reg8: 5, Reg8: 4>
==> 0000001e: <JStrictEqual>: <Addr8: 8, Reg8: 3, Reg8: 0>  # Address: 00000026
==> 00000022: <GetArgumentsPropByVal>: <Reg8: 5, Reg8: 1, Reg8: 2>
==> 00000026: <GetArgumentsLength>: <Reg8: 3, Reg8: 2>
==> 00000029: <LoadConstUInt8>: <Reg8: 1, UInt8: 2>
==> 0000002c: <Greater>: <Reg8: 3, Reg8: 3, Reg8: 1>
==> 00000030: <LoadConstString>: <Reg8: 6, string_id: 7363>  # String: 'result' (Identifier)
==> 00000034: <Mov>: <Reg8: 4, Reg8: 6>
==> 00000037: <JmpFalse>: <Addr8: 18, Reg8: 3>  # Address: 00000049
==> 0000003a: <GetArgumentsPropByVal>: <Reg8: 3, Reg8: 1, Reg8: 2>
==> 0000003e: <Mov>: <Reg8: 4, Reg8: 6>
==> 00000041: <JStrictEqual>: <Addr8: 8, Reg8: 3, Reg8: 0>  # Address: 00000049
==> 00000045: <GetArgumentsPropByVal>: <Reg8: 4, Reg8: 1, Reg8: 2>
==> 00000049: <GetGlobalObject>: <Reg8: 1>
==> 0000004b: <TryGetById>: <Reg8: 6, Reg8: 1, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
==> 00000051: <GetByIdShort>: <Reg8: 3, Reg8: 6, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
==> 00000056: <LoadConstString>: <Reg8: 2, string_id: 4772>  # String: '__BC:Functions/DefaultParameterTests/defaultParameterTest/start' (String)
==> 0000005a: <Call2>: <Reg8: 2, Reg8: 3, Reg8: 6, Reg8: 2>
==> 0000005f: <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
==> 00000065: <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
==> 0000006a: <LoadParam>: <Reg8: 1, UInt8: 1>
==> 0000006d: <Add>: <Reg8: 1, Reg8: 1, Reg8: 5>
==> 00000071: <Call3>: <Reg8: 1, Reg8: 2, Reg8: 3, Reg8: 4, Reg8: 1>
==> 00000077: <Ret>: <Reg8: 0>
"""

_SHOULD_FILTER_HASM = """
=> [Function #10752 "shouldFilter" of 101 bytes]: 2 params, frame size=17, strict=1, exc handler=0, debug info=0  @ offset 0x0021dd62

Bytecode listing:

==> 00000000: <GetParentEnvironment>: <Reg8: 4, UInt8: 0>
==> 00000003: <LoadParam>: <Reg8: 5, UInt8: 1>
==> 00000006: <LoadFromEnvironment>: <Reg8: 3, Reg8: 4, UInt8: 1>
==> 0000000a: <GetById>: <Reg8: 2, Reg8: 3, UInt8: 0, string_id: 13492>  # String: 'skipNull' (Identifier)
==> 00000010: <JmpFalse>: <Addr8: 52, Reg8: 2>  # Address: 00000044
==> 00000013: <GetParentEnvironment>: <Reg8: 6, UInt8: 1>
==> 00000016: <LoadFromEnvironment>: <Reg8: 7, Reg8: 6, UInt8: 5>
==> 0000001a: <LoadFromEnvironment>: <Reg8: 6, Reg8: 4, UInt8: 0>
==> 0000001e: <GetByVal>: <Reg8: 6, Reg8: 6, Reg8: 5>
==> 00000022: <JmpTypeOfIs>: <Addr32: 16, Reg8: 7, UInt16: 128>  # Address: 00000032
==> 0000002a: <LoadConstString>: <Reg8: 8, string_id: 4299>  # String: 'Trying to call a non-function' (String)
==> 0000002e: <CallBuiltin>: <Reg8: 7, UInt8: 44, UInt8: 2>  # Built-in function: [#44 throwTypeError]
==> 00000032: <LoadConstNull>: <Reg8: 0>
==> 00000034: <StrictEq>: <Reg8: 0, Reg8: 6, Reg8: 0>
==> 00000038: <JmpTrue>: <Addr8: 9, Reg8: 0>  # Address: 00000041
==> 0000003b: <LoadConstUndefined>: <Reg8: 1>
==> 0000003d: <StrictEq>: <Reg8: 0, Reg8: 6, Reg8: 1>
==> 00000041: <Mov>: <Reg8: 2, Reg8: 0>
==> 00000044: <JmpTrue>: <Addr8: 31, Reg8: 2>  # Address: 00000063
==> 00000047: <GetById>: <Reg8: 3, Reg8: 3, UInt8: 1, string_id: 15748>  # String: 'skipEmptyString' (Identifier)
==> 0000004d: <JmpFalse>: <Addr8: 19, Reg8: 3>  # Address: 00000060
==> 00000050: <LoadFromEnvironment>: <Reg8: 4, Reg8: 4, UInt8: 0>
==> 00000054: <GetByVal>: <Reg8: 5, Reg8: 4, Reg8: 5>
==> 00000058: <LoadConstString>: <Reg8: 4, string_id: 6457>  # String: '' (Identifier)
==> 0000005c: <StrictEq>: <Reg8: 3, Reg8: 5, Reg8: 4>
==> 00000060: <Mov>: <Reg8: 2, Reg8: 3>
==> 00000063: <Ret>: <Reg8: 2>
"""


def _code(hasm, function_id):
    out = Decompiler.render(Decompiler.build_context(hasm, function_id), verbose=False)
    return "\n".join(line for line in out.splitlines() if not line.strip().startswith("//"))


def test_reader_after_the_if_names_the_register_not_a_copy_of_the_folded_arm():
    code = _code(_DEFAULT_PARAMETER_HASM, 15154)

    assert "r1 = param1 + r5;" in code
    assert "r5 = (r3 === undefined) ? 10 : arguments[1];" in code
    assert "param1 + ((r3" not in code


def test_definition_with_the_same_value_is_not_repointed_to_another_arms_register():
    code = _code(_SHOULD_FILTER_HASM, 10752)

    assert "r4 = r4[0];" in code
    assert "r4 = r6;" not in code
