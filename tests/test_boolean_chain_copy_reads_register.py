"""
A copy of a boolean chain that the code after the `if` holds reads the register
the chain printed into, it does not repeat the chain (`isArrayish`, 96/12935):

    r3 = f(x, r3); if (r3) { r3 = a !== b }; r2 = r3; r1 = r2; r0 = r1

`BooleanChainRegionPass` repointed the `Mov` copies of the arm's value to the
whole folded chain. The chain is printed as `r3 = f(x, r3) && ...`, so the copy
called `f` a second time and read `r3` (and the callee's own register) after
that statement had replaced them: `r0 = r5(param1, r3) && ...`.
"""

import re

from hermes_decompiler.Decompiler import Decompiler

_IS_ARRAYISH = r"""

=> [Function #12935 "isArrayish" of 156 bytes]: 2 params, frame size=17, strict=0, exc handler=0, debug info=0  @ offset 0x0023301c

Bytecode listing:

==> 00000000: <LoadParam>: <Reg8: 4, UInt8: 1>
==> 00000003: <JmpFalseLong>: <Addr32: 149, Reg8: 4>  # Address: 00000098
==> 00000009: <TypeOf>: <Reg8: 1, Reg8: 4>
==> 0000000c: <LoadConstString>: <Reg8: 0, string_id: 7961>  # String: 'string' (Identifier)
==> 00000010: <JStrictEqualLong>: <Addr32: 136, Reg8: 1, Reg8: 0>  # Address: 00000098
==> 00000017: <GetGlobalObject>: <Reg8: 3>
==> 00000019: <TryGetById>: <Reg8: 0, Reg8: 3, UInt8: 1, string_id: 6>  # String: 'Array' (Identifier)
==> 0000001f: <InstanceOf>: <Reg8: 0, Reg8: 4, Reg8: 0>
==> 00000023: <JmpTrue>: <Addr8: 19, Reg8: 0>  # Address: 00000036
==> 00000026: <TryGetById>: <Reg8: 2, Reg8: 3, UInt8: 1, string_id: 6>  # String: 'Array' (Identifier)
==> 0000002c: <GetByIdShort>: <Reg8: 1, Reg8: 2, UInt8: 2, string_id: 5>  # String: 'isArray' (Identifier)
==> 00000031: <Call2>: <Reg8: 0, Reg8: 1, Reg8: 2, Reg8: 4>
==> 00000036: <JmpTrue>: <Addr8: 96, Reg8: 0>  # Address: 00000096
==> 00000039: <GetByIdShort>: <Reg8: 2, Reg8: 4, UInt8: 3, string_id: 169>  # String: 'length' (Identifier)
==> 0000003e: <LoadConstZero>: <Reg8: 1>
==> 00000040: <GreaterEq>: <Reg8: 1, Reg8: 2, Reg8: 1>
==> 00000044: <JmpFalse>: <Addr8: 79, Reg8: 1>  # Address: 00000093
==> 00000047: <GetById>: <Reg8: 5, Reg8: 4, UInt8: 4, string_id: 13199>  # String: 'splice' (Identifier)
==> 0000004d: <TryGetById>: <Reg8: 2, Reg8: 3, UInt8: 5, string_id: 7500>  # String: 'Function' (Identifier)
==> 00000053: <InstanceOf>: <Reg8: 2, Reg8: 5, Reg8: 2>
==> 00000057: <JmpTrue>: <Addr8: 57, Reg8: 2>  # Address: 00000090
==> 0000005a: <TryGetById>: <Reg8: 6, Reg8: 3, UInt8: 6, string_id: 24>  # String: 'Object' (Identifier)
==> 00000060: <GetByIdShort>: <Reg8: 5, Reg8: 6, UInt8: 7, string_id: 150>  # String: 'getOwnPropertyDescriptor' (Identifier)
==> 00000065: <GetByIdShort>: <Reg8: 7, Reg8: 4, UInt8: 3, string_id: 169>  # String: 'length' (Identifier)
==> 0000006a: <LoadConstUInt8>: <Reg8: 3, UInt8: 1>
==> 0000006d: <Sub>: <Reg8: 3, Reg8: 7, Reg8: 3>
==> 00000071: <Call3>: <Reg8: 3, Reg8: 5, Reg8: 6, Reg8: 4, Reg8: 3>
==> 00000077: <JmpFalse>: <Addr8: 22, Reg8: 3>  # Address: 0000008d
==> 0000007a: <GetById>: <Reg8: 4, Reg8: 4, UInt8: 8, string_id: 9124>  # String: 'constructor' (Identifier)
==> 00000080: <GetByIdShort>: <Reg8: 5, Reg8: 4, UInt8: 9, string_id: 176>  # String: 'name' (Identifier)
==> 00000085: <LoadConstString>: <Reg8: 4, string_id: 34>  # String: 'String' (Identifier)
==> 00000089: <StrictNeq>: <Reg8: 3, Reg8: 5, Reg8: 4>
==> 0000008d: <Mov>: <Reg8: 2, Reg8: 3>
==> 00000090: <Mov>: <Reg8: 1, Reg8: 2>
==> 00000093: <Mov>: <Reg8: 0, Reg8: 1>
==> 00000096: <Ret>: <Reg8: 0>
==> 00000098: <LoadConstFalse>: <Reg8: 0>
==> 0000009a: <Ret>: <Reg8: 0>
"""


def _render(hasm: str, function_id: int) -> str:
    context = Decompiler.build_context(hasm, function_id, strict=False)

    return Decompiler.render(context, verbose=False, raw=False)


def test_chain_with_a_call_is_not_repeated_in_the_copy_after_the_if():
    js = _render(_IS_ARRAYISH, 12935)

    assert js.count("Object.getOwnPropertyDescriptor(") == 1
    assert not re.search(r"\br5\(", js)
    # The copy chain is `r0 = r1` (`Mov r0, r1`), r1 being the `length >= 0`
    # result on the path that skips the chain (`r0 = r3` read the global
    # object there: r3 was never written on that path).
    assert re.search(r"\br0 = r1;", js)
    assert not re.search(r"\br0 = r3;", js)


def test_every_path_into_the_merge_reads_the_register_it_wrote():
    """96/12935, the path where `splice instanceof Function` holds: `Mov r1, r2`
    after `r2 = splice instanceof Function` (that path) / `r2 = r3` (the chain
    path). The copy read `r3` (the global object there), and `r1 = len >= 0`,
    which the `if`'s own test inlined, was not assigned for `length < 0`."""
    js = _render(_IS_ARRAYISH, 12935)

    assert re.search(r"\br2 = param1\.splice instanceof Function;", js)
    assert re.search(r"\br2 = r3;", js)
    assert re.search(r"\br1 = r2;", js)
    assert re.search(r"\br1 = param1\.length >= 0;", js)
    assert not re.search(r"\br1 = r3;", js)


def test_a_ternary_copy_after_its_test_register_was_overwritten_reads_the_register():
    """96/9349 `cmp`: two ternaries in a row test the same register
    (`r3 = typeof a; r1 = r3 !== "object" ? a : a.version; r3 = typeof b; ...`),
    and `return r1 === r0` read a COPY of the first one that now tested the
    SECOND `typeof` (F-118). The reader reads the register the first ternary
    assigns; a reader that stands where its test still holds keeps the copy."""
    from pathlib import Path

    hasm = (Path(__file__).parent / "data" / "sequential_ternaries_96_9349.hasm").read_text(encoding="utf-8")
    js = _render(hasm, 9349)

    assert 'r1 = r3 !== "object" ? param1 : param1.version;' in js
    assert 'return r1 === (r3 !== "object" ? param3 : param3.version);' in js
    assert 'param1.version) ===' not in js


def test_a_write_folded_into_its_readers_does_not_make_the_ternary_copy_stale():
    """96/8499 `callGuardDEV`: `r3 = stack ?? ""` is merged by a `Mov r3, r1` that
    is folded into its readers (never printed). It is not a redefinition of the
    `r3` the second ternary's test names, so the readers keep the copy
    (`r17 = (r3 != null) ? caughtException.stack : ""`) instead of the register
    `r1`, which the NEXT merge overwrites."""
    from pathlib import Path

    hasm = (Path(__file__).parent / "data" / "merge_copy_after_absorbed_write_96_8499.hasm").read_text(
        encoding="utf-8")
    js = _render(hasm, 8499)

    assert 'r17 = r3 != null ? caughtException.stack : "";' in js
    assert 'r16 = r2 != null ? caughtException.name : "WorkletsError";' in js
    assert "r17 = r1;" not in js
