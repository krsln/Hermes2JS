"""
The remaining literal-building stores: hermes-98's `PutOwnBySlotIdx`,
`DefineOwnById`, `DefineOwnByVal`, `DefineOwnInDenseArray`, and hermes-96's
`PutOwnByVal`. Small hand-written sections exercise each rule; one real
section covers the printer's else-if flattening.

`PutOwnBySlotIdx` carries only a hidden-class slot; the property name is that
slot's key in the `NewObjectWithBuffer` literal being built.
"""

from __future__ import annotations

from pathlib import Path

from hermes_decompiler.Decompiler import Decompiler

_DATA = Path(__file__).parent / "data"


def _section(*instructions: str) -> str:
    body = "\n".join(f"==> {i * 4:08x}: {text}" for i, text in enumerate(instructions))

    return (
            '\n=> [Function #1 "f" of 99 bytes]: 3 params, frame size=20, strict=1, exc handler=0, '
            "debug info=0  @ offset 0x00000000\n\nBytecode listing:\n\n" + body + "\n\n"
    )


def _out(*instructions: str) -> str:
    out = Decompiler.render(Decompiler.build_context(_section(*instructions), 1), verbose=False)

    return "\n".join(line for line in out.split("\n") if not line.strip().startswith("//"))


_PARAM = "<LoadParam>: <Reg8: 1, UInt8: 1>"
_RET = "<Ret>: <Reg8: 0>"
_BUFFER = "<NewObjectWithBuffer>: <Reg8: 0, UInt16: 1, UInt16: 2>  # Object: {%s}"
_SLOT0 = "<PutOwnBySlotIdx>: <Reg8: 0, Reg8: 1, UInt8: 0>"


def test_slot_store_fills_the_buffer_placeholder():
    out = _out(_PARAM, _BUFFER % "'value': null, 'done': true", _SLOT0, _RET)

    assert 'r0 = { "value": param1, "done": true }' in out
    assert "slot_" not in out


def test_slot_name_resolves_even_when_the_store_cannot_fold():
    # `Mov r3, r0` reads the literal first, so the store stays a statement -
    # but it is `r0.value`, not `r0.slot_0`.
    out = _out(_PARAM, _BUFFER % "'value': null, 'done': true", "<Mov>: <Reg8: 3, Reg8: 0>", _SLOT0, _RET)

    assert "r0.value = param1" in out
    assert "slot_" not in out


def test_only_a_null_placeholder_is_replaced():
    out = _out(_PARAM, _BUFFER % "'value': 5, 'done': true", _SLOT0, _RET)

    assert '"value": 5' in out
    assert "r0.value = param1" in out


def test_index_like_keys_make_the_slot_order_unreliable():
    out = _out(_PARAM, _BUFFER % "'0': null, 'a': true", _SLOT0, _RET)

    assert "r0.slot_0 = param1" in out


def test_define_own_by_id_folds():
    out = _out(
        _PARAM, "<NewObject>: <Reg8: 0>",
        "<DefineOwnById>: <Reg8: 0, Reg8: 1, UInt8: 0, UInt16: 5>  # String: 'name' (Identifier)", _RET,
    )

    assert 'r0 = { "name": param1 }' in out


def test_non_identifier_property_name_is_written_as_a_string_key():
    # `obj.aria-hidden = v` is not valid JavaScript.
    out = _out(
        "<LoadParam>: <Reg8: 0, UInt8: 1>", _PARAM,
        "<DefineOwnById>: <Reg8: 0, Reg8: 1, UInt8: 0, UInt16: 5>  # String: 'aria-hidden' (Identifier)", _RET,
    )

    assert '["aria-hidden"] = ' in out
    assert ".aria-hidden" not in out


def test_enumerable_define_by_value_folds_into_a_computed_property():
    out = _out(
        _PARAM, "<NewObject>: <Reg8: 0>", "<LoadConstString>: <Reg8: 2, string_id: 6>  # String: 'k' (String)",
        "<DefineOwnByVal>: <Reg8: 0, Reg8: 1, Reg8: 2, UInt8: 1>", _RET,
    )

    assert 'r0 = { "k": param1 }' in out


def test_non_enumerable_define_is_never_folded_into_a_literal():
    # enumerable == 0 (class methods: 1,136 of 1,278 in the hermes-98
    # bundle) would become an enumerable literal property if folded.
    out = _out(
        _PARAM, "<NewObject>: <Reg8: 0>", "<LoadConstString>: <Reg8: 2, string_id: 6>  # String: 'k' (String)",
        "<DefineOwnByVal>: <Reg8: 0, Reg8: 1, Reg8: 2, UInt8: 0>", _RET,
    )

    assert '"k": param1' not in out
    assert 'r0["k"] = param1' in out


def test_dense_array_elements_fold_into_one_literal():
    out = _out(
        _PARAM, "<NewArray>: <Reg8: 0, UInt16: 2>",
        "<DefineOwnInDenseArray>: <Reg8: 0, Reg8: 1, UInt8: 0>",
        "<DefineOwnInDenseArray>: <Reg8: 0, Reg8: 1, UInt8: 1>", _RET,
    )

    assert "r0 = [param1, param1]" in out


def test_printed_literal_definition_before_a_nested_if_is_not_skipped():
    # The else-branch starts with `r4 = ...; r9 = { ... }; r8 = ...` and then
    # an `if`. The printer flattened such a branch to `else if` and dropped
    # the prefix, because a block of "pure" definitions counted as skippable
    # - leaving `r5[115] = r9` with no `r9`. (Earlier the stores into the
    # literal, being assignments, had hidden this.)
    hasm = (_DATA / "literal_def_before_nested_if.hasm").read_text(encoding="utf-8")
    out = Decompiler.render(Decompiler.build_context(hasm, 2600), verbose=False)

    assert 'r9 = { "context": r8, "memoizedValue": r8._currentValue2, "next": null }' in out
    assert "r4 = r5[114]" in out
