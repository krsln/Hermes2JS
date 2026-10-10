"""
A conditional jump right after a join reads the register's MERGED value
(`r0 = a; if (!r0) r0 = b; if (!r0) r0 = c`), not the last arm's write.

- the jump used to inline the arm's value, and a negated test (`JmpFalse`) is a new
  expression no fold could repoint, so a three-operand `||` chain was left as a
  broken pair of ternaries over a register nothing assigned;
- `BooleanChainRegionPass` now recognises an `if (!rN)` that tests the register
  it just built, and the folds' "is the register read by name later" check sees
  the tests the structurers already moved into `IfRegion`s.
"""

from hermes_decompiler.Decompiler import Decompiler

_PRESS_HANDLER_HASM = """
=> [Function #6283 "_hasPressHandler" of 75 bytes]: 1 params, frame size=4, strict=1, exc handler=0, debug info=0  @ offset 0x0019a07d

Bytecode listing:

==> 00000000: <LoadParam>: <Reg8: 1, UInt8: 0>
==> 00000003: <GetByIdShort>: <Reg8: 0, Reg8: 1, UInt8: 1, string_id: 204>  # String: 'props' (Identifier)
==> 00000008: <GetByIdShort>: <Reg8: 0, Reg8: 0, UInt8: 2, string_id: 129>  # String: 'onPress' (Identifier)
==> 0000000d: <LoadConstNull>: <Reg8: 2>
==> 0000000f: <Neq>: <Reg8: 0, Reg8: 0, Reg8: 2>
==> 00000013: <JmpTrue>: <Addr8: 18, Reg8: 0>  # Address: 00000025
==> 00000016: <GetByIdShort>: <Reg8: 3, Reg8: 1, UInt8: 1, string_id: 204>  # String: 'props' (Identifier)
==> 0000001b: <GetById>: <Reg8: 3, Reg8: 3, UInt8: 3, string_id: 9702>  # String: 'onPressIn' (Identifier)
==> 00000021: <Neq>: <Reg8: 0, Reg8: 3, Reg8: 2>
==> 00000025: <JmpTrue>: <Addr8: 18, Reg8: 0>  # Address: 00000037
==> 00000028: <GetByIdShort>: <Reg8: 3, Reg8: 1, UInt8: 1, string_id: 204>  # String: 'props' (Identifier)
==> 0000002d: <GetById>: <Reg8: 3, Reg8: 3, UInt8: 4, string_id: 14963>  # String: 'onPressOut' (Identifier)
==> 00000033: <Neq>: <Reg8: 0, Reg8: 3, Reg8: 2>
==> 00000037: <JmpTrue>: <Addr8: 18, Reg8: 0>  # Address: 00000049
==> 0000003a: <GetByIdShort>: <Reg8: 1, Reg8: 1, UInt8: 1, string_id: 204>  # String: 'props' (Identifier)
==> 0000003f: <GetById>: <Reg8: 1, Reg8: 1, UInt8: 5, string_id: 14414>  # String: 'onLongPress' (Identifier)
==> 00000045: <Neq>: <Reg8: 0, Reg8: 1, Reg8: 2>
==> 00000049: <Ret>: <Reg8: 0>
"""

_STRIP_BASE_URL_HASM = """
=> [Function #5896 "stripBaseUrl" of 131 bytes]: 2 params, frame size=17, strict=1, exc handler=0, debug info=0  @ offset 0x001be280

Bytecode listing:

==> 00000000: <LoadParam>: <Reg8: 5, UInt8: 2>
==> 00000003: <LoadConstUndefined>: <Reg8: 0>
==> 00000005: <JStrictNotEqual>: <Addr8: 8, Reg8: 5, Reg8: 0>  # Address: 0000000d
==> 00000009: <LoadConstString>: <Reg8: 5, string_id: 6457>  # String: '' (Identifier)
==> 0000000d: <LoadParam>: <Reg8: 6, UInt8: 1>
==> 00000010: <JmpTrue>: <Addr8: 5, Reg8: 5>  # Address: 00000015
==> 00000013: <Ret>: <Reg8: 6>
==> 00000015: <GetParentEnvironment>: <Reg8: 2, UInt8: 0>
==> 00000018: <GetByIdShort>: <Reg8: 4, Reg8: 6, UInt8: 0, string_id: 217>  # String: 'replace' (Identifier)
==> 0000001d: <LoadConstString>: <Reg8: 3, string_id: 503>  # String: '/' (String)
==> 00000021: <CreateRegExp>: <Reg8: 1, string_id: 1677, string_id: 6578, UInt32: 110>  # String: '^\\/+' (String)  # String: 'g' (Identifier)
==> 0000002f: <Call3>: <Reg8: 4, Reg8: 4, Reg8: 6, Reg8: 1, Reg8: 3>
==> 00000035: <GetByIdShort>: <Reg8: 3, Reg8: 4, UInt8: 0, string_id: 217>  # String: 'replace' (Identifier)
==> 0000003a: <GetGlobalObject>: <Reg8: 1>
==> 0000003c: <TryGetById>: <Reg8: 6, Reg8: 1, UInt8: 1, string_id: 29>  # String: 'RegExp' (Identifier)
==> 00000042: <LoadFromEnvironment>: <Reg8: 2, Reg8: 2, UInt8: 0>
==> 00000046: <GetByIdShort>: <Reg8: 2, Reg8: 2, UInt8: 2, string_id: 115>  # String: 'default' (Identifier)
==> 0000004b: <Call2>: <Reg8: 5, Reg8: 2, Reg8: 0, Reg8: 5>
==> 00000050: <TryGetById>: <Reg8: 1, Reg8: 1, UInt8: 3, string_id: 10>  # String: 'HermesInternal' (Identifier)
==> 00000056: <GetByIdShort>: <Reg8: 2, Reg8: 1, UInt8: 4, string_id: 105>  # String: 'concat' (Identifier)
==> 0000005b: <LoadConstString>: <Reg8: 1, string_id: 1206>  # String: '^\\/?' (String)
==> 0000005f: <Call2>: <Reg8: 8, Reg8: 2, Reg8: 1, Reg8: 5>
==> 00000064: <CreateThisForNew>: <Reg8: 5, Reg8: 6, UInt8: 5>
==> 00000068: <LoadConstString>: <Reg8: 7, string_id: 6578>  # String: 'g' (Identifier)
==> 0000006c: <Mov>: <Reg8: 9, Reg8: 5>
==> 0000006f: <Construct>: <Reg8: 1, Reg8: 6, UInt8: 3>
==> 00000073: <LoadConstString>: <Reg8: 2, string_id: 6457>  # String: '' (Identifier)
==> 00000077: <SelectObject>: <Reg8: 1, Reg8: 5, Reg8: 1>
==> 0000007b: <Call3>: <Reg8: 1, Reg8: 3, Reg8: 4, Reg8: 1, Reg8: 2>
==> 00000081: <Ret>: <Reg8: 1>
"""

_BOX_SHADOW_HASM = """
=> [Function #9040 "parseBoxShadowString" of 60 bytes]: 2 params, frame size=11, strict=1, exc handler=0, debug info=0  @ offset 0x001d3f8f

Bytecode listing:

==> 00000000: <LoadParam>: <Reg8: 2, UInt8: 1>
==> 00000003: <LoadConstString>: <Reg8: 0, string_id: 7424>  # String: 'none' (Identifier)
==> 00000007: <JStrictEqual>: <Addr8: 47, Reg8: 2, Reg8: 0>  # Address: 00000036
==> 0000000b: <GetByIdShort>: <Reg8: 1, Reg8: 2, UInt8: 1, string_id: 171>  # String: 'match' (Identifier)
==> 00000010: <GetEnvironment>: <Reg8: 0, UInt8: 0>
==> 00000013: <LoadFromEnvironment>: <Reg8: 0, Reg8: 0, UInt8: 0>
==> 00000017: <Call2>: <Reg8: 2, Reg8: 1, Reg8: 2, Reg8: 0>
==> 0000001c: <JmpTrue>: <Addr8: 7, Reg8: 2>  # Address: 00000023
==> 0000001f: <NewArray>: <Reg8: 2, UInt16: 0>
==> 00000023: <GetByIdShort>: <Reg8: 1, Reg8: 2, UInt8: 2, string_id: 170>  # String: 'map' (Identifier)
==> 00000028: <CreateEnvironment>: <Reg8: 0>
==> 0000002a: <CreateClosure>: <Reg8: 0, Reg8: 0, function_id: 9041>  # Function: [#9041  of 66 bytes]: 2 params @ offset 0x001d3fcb
==> 0000002f: <Call2>: <Reg8: 0, Reg8: 1, Reg8: 2, Reg8: 0>
==> 00000034: <Ret>: <Reg8: 0>
==> 00000036: <NewArray>: <Reg8: 0, UInt16: 0>
==> 0000003a: <Ret>: <Reg8: 0>
"""


def _code(hasm, function_id):
    out = Decompiler.render(Decompiler.build_context(hasm, function_id), verbose=False)
    return "\n".join(line for line in out.splitlines() if not line.strip().startswith("//"))


def test_three_operand_or_chain_folds_into_one_expression():
    # hermes-96 `_hasPressHandler`: onPress || onPressIn || onPressOut || onLongPress.
    code = _code(_PRESS_HANDLER_HASM, 6283)

    for prop in ("onPress", "onPressIn", "onPressOut", "onLongPress"):
        assert f".{prop} != null" in code

    assert code.count("||") == 3
    assert "?" not in code
    # every register the chain reads is one the output assigns
    assert "r3" not in code


def test_default_folded_into_a_ternary_keeps_its_register_for_the_branch():
    # hermes-98 `stripBaseUrl`: `r5 = param2 ?? ""` is tested by name right after.
    code = _code(_STRIP_BASE_URL_HASM, 5896)

    assert 'r5 = (param2 !== undefined) ? param2 : "";' in code
    assert code.index('r5 = (param2 !== undefined) ? param2 : "";') < code.index("if (r5) {")


def test_register_tested_fold_does_not_repoint_an_unrelated_identical_literal():
    # hermes-96 `parseBoxShadowString`: folding `r2 = match(..) || []` must not
    # rewrite the OTHER `[]` (`r0 = []` of the `"none"` arm) into the fold.
    code = _code(_BOX_SHADOW_HASM, 9040)

    assert "r2 = param1.match(r0) || [];" in code
    assert "r0 = [];" in code
    assert code.rstrip().endswith("return r0;\n}")
