"""
hermes-98 `super(...)` / `new` plumbing: `CallWithNewTarget`, the `SelectObject`
that follows it, and the dead `CreateThisForNew` that precedes a `Construct`.

Small hand-written sections, same shape as `test_slot_and_define_folding.py`.
The layouts mirror real functions of the hermes-98 test bundle
(`CustomEvent`, `createInstance`), where the old output was, respectively,
`Reflect.construct(r2, [r-1, r0, r1], new.target)` followed by
`CreateThisForSuper(r2)[r1]`, and a dead `r2 = CreateThisForNew(r1)` before
`return new r1[3]()`.
"""

from __future__ import annotations

from hermes_decompiler.Decompiler import Decompiler


def _section(*instructions: str) -> str:
    body = "\n".join(f"==> {i * 4:08x}: {text}" for i, text in enumerate(instructions))

    return (
            '\n=> [Function #1 "f" of 99 bytes]: 3 params, frame size=20, strict=1, exc handler=0, '
            "debug info=0  @ offset 0x00000000\n\nBytecode listing:\n\n" + body + "\n\n"
    )


def _out(*instructions: str) -> str:
    out = Decompiler.render(Decompiler.build_context(_section(*instructions), 1), verbose=False)

    return "\n".join(line for line in out.split("\n") if not line.strip().startswith("//"))


# `super(param1, param2)`: the window is [this, arg1, arg2] = r8, r7, r6, with
# `this` copied from CreateThisForSuper's register (r3) by a Mov.
_SUPER_PRELUDE = (
    "<GetParentEnvironment>: <Reg8: 2, UInt8: 0>",
    "<GetNewTarget>: <Reg8: 5>",
    "<CreateThisForSuper>: <Reg8: 3, Reg8: 2, Reg8: 5, UInt8: 0>",
    "<LoadParam>: <Reg8: 7, UInt8: 1>",
    "<Mov>: <Reg8: 8, Reg8: 3>",
    "<LoadParam>: <Reg8: 6, UInt8: 2>",
    "<CallWithNewTarget>: <Reg8: 1, Reg8: 2, Reg8: 5, UInt8: 3>",
)


def test_super_call_window_is_read_from_the_top_of_the_frame():
    out = _out(*_SUPER_PRELUDE, "<SelectObject>: <Reg8: 1, Reg8: 3, Reg8: 1>", "<Ret>: <Reg8: 1>")

    # Not relative to the callee register (r2): that gave `[r-1, r0, r1]`.
    assert "Reflect.construct(r2, [param1, param2], new.target)" in out.replace("getParentEnvironment(0)", "r2")
    assert "r-1" not in out


def test_the_this_placeholder_never_reaches_the_output():
    out = _out(*_SUPER_PRELUDE, "<SelectObject>: <Reg8: 1, Reg8: 3, Reg8: 1>", "<Ret>: <Reg8: 1>")

    assert "CreateThisForSuper" not in out


def test_select_object_after_super_is_an_alias_not_a_computed_member():
    out = _out(*_SUPER_PRELUDE, "<SelectObject>: <Reg8: 1, Reg8: 3, Reg8: 1>", "<Ret>: <Reg8: 1>")

    assert "return r1;" in out
    # `SelectObject r1, r3, r1` is a no-op on the register: no `r1 = r1`.
    assert "r1 = r1" not in out


def test_select_object_into_another_register_is_a_plain_alias():
    out = _out(*_SUPER_PRELUDE, "<SelectObject>: <Reg8: 4, Reg8: 3, Reg8: 1>", "<Ret>: <Reg8: 4>")

    # r4 is just the super call's result, so the return reads it directly -
    # not `CreateThisForSuper(r2)[r1]`.
    assert "return r1;" in out
    assert "CreateThisForSuper" not in out


def test_super_call_is_not_moved_past_statements_between_it_and_select_object():
    out = _out(
        *_SUPER_PRELUDE,
        "<LoadConstString>: <Reg8: 9, string_id: 6>  # String: 'after-super' (String)",
        "<PutByIdStrict>: <Reg8: 9, Reg8: 9, UInt8: 0, string_id: 7>  # String: 'p' (Identifier)",
        "<SelectObject>: <Reg8: 1, Reg8: 3, Reg8: 1>",
        "<Ret>: <Reg8: 1>",
    )

    # Folding the call into the SelectObject would print it after these.
    assert out.index("Reflect.construct") < out.index("after-super")


def test_super_call_without_arguments_has_an_empty_argument_list():
    out = _out(
        "<GetParentEnvironment>: <Reg8: 2, UInt8: 0>",
        "<GetNewTarget>: <Reg8: 5>",
        "<CreateThisForSuper>: <Reg8: 3, Reg8: 2, Reg8: 5, UInt8: 0>",
        "<Mov>: <Reg8: 8, Reg8: 3>",
        "<CallWithNewTarget>: <Reg8: 1, Reg8: 2, Reg8: 5, UInt8: 1>",
        "<SelectObject>: <Reg8: 1, Reg8: 3, Reg8: 1>",
        "<Ret>: <Reg8: 1>",
    )

    assert "[]" in out
    assert "CreateThisForSuper" not in out


def test_new_expression_drops_the_dead_create_this_for_new():
    # hermes-98 allocates `this` in r2 but hands Construct an unrelated,
    # never-written `this` slot (r3), so r2 used to print as a dead line.
    out = _out(
        "<GetParentEnvironment>: <Reg8: 1, UInt8: 0>",
        "<LoadFromEnvironment>: <Reg8: 1, Reg8: 1, UInt8: 3>",
        "<CreateThisForNew>: <Reg8: 2, Reg8: 1, UInt8: 0>",
        "<LoadConstUndefined>: <Reg8: 3>",
        "<Construct>: <Reg8: 1, Reg8: 1, UInt8: 1>",
        "<Ret>: <Reg8: 1>",
    )

    assert "return new r1[3]();" in out
    assert "CreateThisForNew" not in out


def test_a_create_this_for_new_from_another_constructor_is_left_alone():
    # Only the placeholder made from THIS `new`'s constructor register (r1)
    # is consumed; an unrelated one (r5, made from r4) must not be swallowed.
    # The never-written `this` slot is r6, the highest register of the window.
    out = _out(
        "<GetParentEnvironment>: <Reg8: 1, UInt8: 0>",
        "<LoadFromEnvironment>: <Reg8: 4, Reg8: 1, UInt8: 4>",
        "<LoadFromEnvironment>: <Reg8: 1, Reg8: 1, UInt8: 3>",
        "<CreateThisForNew>: <Reg8: 5, Reg8: 4, UInt8: 0>",
        "<CreateThisForNew>: <Reg8: 2, Reg8: 1, UInt8: 0>",
        "<LoadConstUndefined>: <Reg8: 6>",
        "<Construct>: <Reg8: 1, Reg8: 1, UInt8: 1>",
        "<PutByIdStrict>: <Reg8: 1, Reg8: 5, UInt8: 0, string_id: 7>  # String: 'p' (Identifier)",
        "<Ret>: <Reg8: 1>",
    )

    # r5 is read afterwards, so it is not a dead placeholder: it keeps its
    # definition (naming the constructor it came from, r4 = r1[4]) and the
    # reader names the register.
    assert "r5 = CreateThisForNew(r1[4])" in out
    assert "r1.p = r5" in out
    assert out.count("CreateThisForNew") == 1


def test_a_placeholder_nothing_reads_is_dropped():
    # `r3 = CreateThisForNew(r1)` in front of a `typeof` guard, never read.
    out = _out(
        "<GetParentEnvironment>: <Reg8: 1, UInt8: 0>",
        "<LoadFromEnvironment>: <Reg8: 1, Reg8: 1, UInt8: 3>",
        "<CreateThisForNew>: <Reg8: 3, Reg8: 1, UInt8: 0>",
        "<Ret>: <Reg8: 1>",
    )

    assert "CreateThisForNew" not in out


def test_a_placeholder_with_several_readers_is_one_object_not_one_per_use():
    # An inlined `_classCallCheck`-style constructor body: the fresh object is
    # written to twice. Inlining the placeholder at each use printed
    # `CreateThisForNew(r1[3])._a = 0; CreateThisForNew(r1[3])._b = 0`.
    out = _out(
        "<GetParentEnvironment>: <Reg8: 1, UInt8: 0>",
        "<LoadFromEnvironment>: <Reg8: 1, Reg8: 1, UInt8: 3>",
        "<CreateThisForNew>: <Reg8: 7, Reg8: 1, UInt8: 0>",
        "<LoadConstZero>: <Reg8: 0>",
        "<PutByIdStrict>: <Reg8: 7, Reg8: 0, UInt8: 0, string_id: 6>  # String: '_a' (Identifier)",
        "<PutByIdStrict>: <Reg8: 7, Reg8: 0, UInt8: 1, string_id: 7>  # String: '_b' (Identifier)",
        "<Ret>: <Reg8: 7>",
    )

    assert out.count("CreateThisForNew") == 1
    assert "r7._a = 0" in out and "r7._b = 0" in out


def test_default_derived_constructor_forwards_arguments():
    # hermes-98 implicit `constructor(...args) { super(...args) }`.
    out = _out(
        "<GetParentEnvironment>: <Reg8: 0, UInt8: 0>",
        "<LoadFromEnvironment>: <Reg8: 0, Reg8: 0, UInt8: 2>",
        "<LoadParentNoTraps>: <Reg8: 2, Reg8: 0>",
        "<GetNewTarget>: <Reg8: 1>",
        "<CreateThisForSuper>: <Reg8: 4, Reg8: 2, Reg8: 1, UInt8: 0>",
        "<Mov>: <Reg8: 5, Reg8: 2>",
        "<Mov>: <Reg8: 3, Reg8: 1>",
        "<CallBuiltin>: <Reg8: 0, UInt8: 50, UInt8: 4>  # Built-in function: [#50 applyArguments]",
        "<Ret>: <Reg8: 0>",
    )

    assert "Reflect.construct(r2, arguments, new.target)" in out
    assert "CreateThisForSuper" not in out
    assert "applyArguments" not in out
