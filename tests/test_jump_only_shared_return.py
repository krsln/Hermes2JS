"""
A constant `return` reached only by jumps (`a === 1 || a === 2 ... return true`,
98/8021) is copied per jumper, the last one keeping the original, so no
`goto label_N` is left. Nested tail merges of the resulting `return r0` must
still resolve `r0` along every arm (98/2190: all-`true` arms once collapsed the
whole function to `return true`).
"""

from hermes_decompiler.Decompiler import Decompiler

_IS_TRANSITION_PROP = """
=> [Function #8021 "isTransitionProp" of 59 bytes]: 2 params, frame size=3, strict=1, exc handler=0, debug info=0  @ offset 0x001e7794

Bytecode listing:

==> 00000000: <LoadParam>: <Reg8: 2, UInt8: 1>
==> 00000003: <LoadConstString>: <Reg8: 1, string_id: 14389>  # String: 'transitionProperty' (Identifier)
==> 00000007: <JStrictEqual>: <Addr8: 48, Reg8: 1, Reg8: 2>  # Address: 00000037
==> 0000000b: <LoadConstString>: <Reg8: 1, string_id: 14259>  # String: 'transitionDuration' (Identifier)
==> 0000000f: <JStrictEqual>: <Addr8: 40, Reg8: 1, Reg8: 2>  # Address: 00000037
==> 00000013: <LoadConstString>: <Reg8: 1, string_id: 13592>  # String: 'transitionTimingFunction' (Identifier)
==> 00000017: <JStrictEqual>: <Addr8: 32, Reg8: 1, Reg8: 2>  # Address: 00000037
==> 0000001b: <LoadConstString>: <Reg8: 1, string_id: 14254>  # String: 'transitionDelay' (Identifier)
==> 0000001f: <JStrictEqual>: <Addr8: 24, Reg8: 1, Reg8: 2>  # Address: 00000037
==> 00000023: <LoadConstString>: <Reg8: 1, string_id: 14249>  # String: 'transitionBehavior' (Identifier)
==> 00000027: <JStrictEqual>: <Addr8: 16, Reg8: 1, Reg8: 2>  # Address: 00000037
==> 0000002b: <LoadConstString>: <Reg8: 1, string_id: 6760>  # String: 'transition' (Identifier)
==> 0000002f: <JStrictEqual>: <Addr8: 8, Reg8: 1, Reg8: 2>  # Address: 00000037
==> 00000033: <LoadConstFalse>: <Reg8: 0>
==> 00000035: <Ret>: <Reg8: 0>
==> 00000037: <LoadConstTrue>: <Reg8: 0>
==> 00000039: <Ret>: <Reg8: 0>


"""

_IS_VALID_POSITION = """
=> [Function #2190 "isValidPosition" of 53 bytes]: 2 params, frame size=13, strict=1, exc handler=0, debug info=0  @ offset 0x00161b72

Bytecode listing:

==> 00000000: <LoadParam>: <Reg8: 2, UInt8: 1>
==> 00000003: <GetByIdShort>: <Reg8: 3, Reg8: 2, UInt8: 0, string_id: 135>  # String: 'endsWith' (Identifier)
==> 00000008: <LoadConstString>: <Reg8: 1, string_id: 307>  # String: 'px' (String)
==> 0000000c: <Call2>: <Reg8: 1, Reg8: 3, Reg8: 2, Reg8: 1>
==> 00000011: <JmpTrue>: <Addr8: 32, Reg8: 1>  # Address: 00000031
==> 00000014: <GetByIdShort>: <Reg8: 3, Reg8: 2, UInt8: 0, string_id: 135>  # String: 'endsWith' (Identifier)
==> 00000019: <LoadConstString>: <Reg8: 1, string_id: 856>  # String: '%' (String)
==> 0000001d: <Call2>: <Reg8: 1, Reg8: 3, Reg8: 2, Reg8: 1>
==> 00000022: <JmpTrue>: <Addr8: 15, Reg8: 1>  # Address: 00000031
==> 00000025: <LoadConstString>: <Reg8: 1, string_id: 810>  # String: '0' (String)
==> 00000029: <JStrictEqual>: <Addr8: 8, Reg8: 2, Reg8: 1>  # Address: 00000031
==> 0000002d: <LoadConstFalse>: <Reg8: 0>
==> 0000002f: <Ret>: <Reg8: 0>
==> 00000031: <LoadConstTrue>: <Reg8: 0>
==> 00000033: <Ret>: <Reg8: 0>


"""


def _js(hasm, index):
    return Decompiler.render(Decompiler.build_context(hasm, index, strict=False), verbose=False, raw=False)


def test_jump_only_constant_return_has_no_goto():
    js = _js(_IS_TRANSITION_PROP, 8021)

    assert "goto" not in js
    assert js.count("return true;") == 6
    assert "return false;" in js


def test_nested_merged_returns_keep_the_false_path():
    js = _js(_IS_VALID_POSITION, 2190)

    assert "r0 = false;" in js
    assert js.strip().endswith("return r0;\n}")
