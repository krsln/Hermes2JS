"""
A definition that PRINTS is a statement later code reads by name; nothing may
look past it as clutter.

- the printer's else-if flattening skipped a block of constant loads
  (`r5 = undefined`) that a later `if (!r5)` reads by name;
- `UnfoldedMergeRepairPass` refused to repair an arm write whose value object a
  READER (`Mov r11, r5`) also held, as if it were a second definer;
- the default `r1 = param1` an `if` condition consumed inline has to print when
  the arm that overwrites it is skipped.
"""

from hermes_decompiler.Decompiler import Decompiler

_SCROLL_TO_HASM = """
=> [Function #5704 "" of 159 bytes]: 4 params, frame size=20, strict=1, exc handler=0, debug info=0  @ offset 0x0018cc8e

Bytecode listing:

==> 00000000: <LoadParam>: <Reg8: 1, UInt8: 1>
==> 00000003: <LoadParam>: <Reg8: 2, UInt8: 2>
==> 00000006: <LoadParam>: <Reg8: 0, UInt8: 3>
==> 00000009: <TypeOf>: <Reg8: 4, Reg8: 1>
==> 0000000c: <LoadConstString>: <Reg8: 3, string_id: 7552>  # String: 'number' (Identifier)
==> 00000010: <JStrictEqual>: <Addr8: 31, Reg8: 4, Reg8: 3>  # Address: 0000002f
==> 00000014: <LoadConstUndefined>: <Reg8: 5>
==> 00000016: <LoadConstUndefined>: <Reg8: 4>
==> 00000018: <LoadConstUndefined>: <Reg8: 6>
==> 0000001a: <JmpFalse>: <Addr8: 52, Reg8: 1>  # Address: 0000004e
==> 0000001d: <GetByIdShort>: <Reg8: 4, Reg8: 1, UInt8: 1, string_id: 7>  # String: 'y' (Identifier)
==> 00000022: <GetByIdShort>: <Reg8: 5, Reg8: 1, UInt8: 2, string_id: 41>  # String: 'x' (Identifier)
==> 00000027: <GetById>: <Reg8: 6, Reg8: 1, UInt8: 3, string_id: 7210>  # String: 'animated' (Identifier)
==> 0000002d: <Jmp>: <Addr8: 33>  # Address: 0000004e
==> 0000002f: <GetGlobalObject>: <Reg8: 3>
==> 00000031: <TryGetById>: <Reg8: 8, Reg8: 3, UInt8: 4, string_id: 99>  # String: 'console' (Identifier)
==> 00000037: <GetByIdShort>: <Reg8: 7, Reg8: 8, UInt8: 5, string_id: 131>  # String: 'warn' (Identifier)
==> 0000003c: <LoadConstString>: <Reg8: 3, string_id: 5061>  # String: '`scrollTo(y, x, animated)` is deprecated. Use `scrollTo({x: 5, y: 5, animated: true})` instead.' (String)
==> 00000040: <Call2>: <Reg8: 3, Reg8: 7, Reg8: 8, Reg8: 3>
==> 00000045: <Mov>: <Reg8: 5, Reg8: 2>
==> 00000048: <Mov>: <Reg8: 4, Reg8: 1>
==> 0000004b: <Mov>: <Reg8: 6, Reg8: 0>
==> 0000004e: <GetEnvironment>: <Reg8: 0, UInt8: 0>
==> 00000051: <LoadFromEnvironment>: <Reg8: 1, Reg8: 0, UInt8: 0>
==> 00000055: <GetById>: <Reg8: 0, Reg8: 1, UInt8: 6, string_id: 9729>  # String: 'getNativeScrollRef' (Identifier)
==> 0000005b: <Call1>: <Reg8: 3, Reg8: 0, Reg8: 1>
==> 0000005f: <LoadConstNull>: <Reg8: 0>
==> 00000061: <JEqual>: <Addr8: 58, Reg8: 3, Reg8: 0>  # Address: 0000009b
==> 00000065: <GetEnvironment>: <Reg8: 0, UInt8: 2>
==> 00000068: <LoadFromEnvironment>: <Reg8: 0, Reg8: 0, UInt8: 24>
==> 0000006c: <GetByIdShort>: <Reg8: 2, Reg8: 0, UInt8: 7, string_id: 107>  # String: 'default' (Identifier)
==> 00000071: <GetById>: <Reg8: 1, Reg8: 2, UInt8: 8, string_id: 10037>  # String: 'scrollTo' (Identifier)
==> 00000077: <JmpTrue>: <Addr8: 5, Reg8: 5>  # Address: 0000007c
==> 0000007a: <LoadConstZero>: <Reg8: 5>
==> 0000007c: <JmpTrue>: <Addr8: 5, Reg8: 4>  # Address: 00000081
==> 0000007f: <LoadConstZero>: <Reg8: 4>
==> 00000081: <LoadConstFalse>: <Reg8: 0>
==> 00000083: <StrictNeq>: <Reg8: 9, Reg8: 6, Reg8: 0>
==> 00000087: <Mov>: <Reg8: 13, Reg8: 2>
==> 0000008a: <Mov>: <Reg8: 12, Reg8: 3>
==> 0000008d: <Mov>: <Reg8: 11, Reg8: 5>
==> 00000090: <Mov>: <Reg8: 10, Reg8: 4>
==> 00000093: <Call>: <Reg8: 0, Reg8: 1, UInt8: 5>
==> 00000097: <LoadConstUndefined>: <Reg8: 0>
==> 00000099: <Ret>: <Reg8: 0>
==> 0000009b: <LoadConstUndefined>: <Reg8: 0>
==> 0000009d: <Ret>: <Reg8: 0>
"""

_SINGLE_TOUCH_HASM = """
=> [Function #6221 "extractSingleTouch" of 77 bytes]: 2 params, frame size=7, strict=1, exc handler=0, debug info=0  @ offset 0x00198775

Bytecode listing:

==> 00000000: <LoadParam>: <Reg8: 1, UInt8: 1>
==> 00000003: <GetById>: <Reg8: 3, Reg8: 1, UInt8: 1, string_id: 12462>  # String: 'touches' (Identifier)
==> 00000009: <GetById>: <Reg8: 4, Reg8: 1, UInt8: 2, string_id: 16944>  # String: 'changedTouches' (Identifier)
==> 0000000f: <Mov>: <Reg8: 2, Reg8: 3>
==> 00000012: <JmpFalse>: <Addr8: 14, Reg8: 2>  # Address: 00000020
==> 00000015: <GetByIdShort>: <Reg8: 5, Reg8: 3, UInt8: 3, string_id: 169>  # String: 'length' (Identifier)
==> 0000001a: <LoadConstZero>: <Reg8: 0>
==> 0000001c: <Greater>: <Reg8: 2, Reg8: 5, Reg8: 0>
==> 00000020: <Mov>: <Reg8: 0, Reg8: 4>
==> 00000023: <JmpFalse>: <Addr8: 14, Reg8: 0>  # Address: 00000031
==> 00000026: <GetByIdShort>: <Reg8: 6, Reg8: 4, UInt8: 3, string_id: 169>  # String: 'length' (Identifier)
==> 0000002b: <LoadConstZero>: <Reg8: 5>
==> 0000002d: <Greater>: <Reg8: 0, Reg8: 6, Reg8: 5>
==> 00000031: <JmpTrue>: <Addr8: 14, Reg8: 2>  # Address: 0000003f
==> 00000034: <JmpFalse>: <Addr8: 11, Reg8: 0>  # Address: 0000003f
==> 00000037: <LoadConstZero>: <Reg8: 0>
==> 00000039: <GetByVal>: <Reg8: 0, Reg8: 4, Reg8: 0>
==> 0000003d: <Jmp>: <Addr8: 14>  # Address: 0000004b
==> 0000003f: <JmpFalse>: <Addr8: 9, Reg8: 2>  # Address: 00000048
==> 00000042: <LoadConstZero>: <Reg8: 2>
==> 00000044: <GetByVal>: <Reg8: 1, Reg8: 3, Reg8: 2>
==> 00000048: <Mov>: <Reg8: 0, Reg8: 1>
==> 0000004b: <Ret>: <Reg8: 0>
"""


def _code(hasm, function_id):
    out = Decompiler.render(Decompiler.build_context(hasm, function_id), verbose=False)
    return "\n".join(line for line in out.splitlines() if not line.strip().startswith("//"))


def test_else_if_flattening_keeps_the_defaults_in_front_of_the_nested_if():
    # hermes-96 `scrollTo`: `else { r5 = undefined; r4 = undefined; r6 = undefined; if (param1) {...} }`
    code = _code(_SCROLL_TO_HASM, 5704)

    assert "} else {\n        r5 = undefined;\n        r4 = undefined;\n        r6 = undefined;\n        if (param1) {" in code


def test_arm_write_read_by_a_mov_is_printed_and_the_reader_names_the_register():
    # `if (!r5) { r5 = 0 }` then `Mov r11, r5`: the 0 used to be inlined into the
    # Mov and the arm left empty (`if (!r5) { }`).
    code = _code(_SCROLL_TO_HASM, 5704)

    assert "if (!r5) {\n            r5 = 0;\n        }" in code
    assert "r11 = r5;" in code
    assert "if (!r5) {\n        }" not in code


def test_parameter_default_printed_when_the_overwriting_arm_is_skipped():
    # hermes-96 `extractSingleTouch`: `r0 = r1` after `if (..) { r1 = r3[r2] }`
    # reads the parameter when the `if` is skipped.
    code = _code(_SINGLE_TOUCH_HASM, 6221)

    assert "r1 = param1;" in code
    assert code.index("r1 = param1;") < code.index("r0 = r1;")
