"""
Iterator destructuring whose element targets run code (F-215, 98/10423 `VirtualCollectionSpacer`, 98/10166).

    const [{ SpacerView }, setX] = useState(...)

Hermes reads the element's properties between two fetches and stores the last element into a slot, all behind a
cleanup handler. The pass knew register targets only, so these stayed an open-coded iterator state machine. The
property reads and the store are targets of the pattern now, and the pattern keeps the order JavaScript runs them
in (fetch, bind, fetch): nothing is moved across a `next()`. The target is recognised by the IR shape of the binding
code (a plain property load of the element register, a store of it into a slot that needs no evaluation), not by
opcode names.
"""

from pathlib import Path

from hermes_decompiler.Decompiler import Decompiler

_DATA = Path(__file__).parent / "data"


def _code(name: str, function_id: int) -> str:
    hasm = (_DATA / name).read_text(encoding="utf-8")
    out = Decompiler.render(Decompiler.build_context(hasm, function_id, strict=False), verbose=False, raw=False)
    return "\n".join(line for line in out.split("\n") if not line.strip().startswith("//"))


def test_an_object_pattern_element_and_a_slot_store_are_one_destructuring():
    code = _code("destructuring_object_target_98_10423.hasm", 10423)

    assert "[{ SpacerView: r0 }, __environment__[2]] = r10;" in code
    assert "goto" not in code
    assert ".next()" not in code


def test_a_hole_followed_by_a_slot_store():
    code = _code("destructuring_hole_store_98_10166.hasm", 10166)

    assert "[, __environment__[1]] = r9;" in code
    assert ".next()" not in code


def test_member_targets_with_constant_keys_in_a_per_element_try():
    # 98/11908 `maybeSwapComponents`: `[a[0], a[1]] = src`. The element value is stored straight from the fetch
    # register (the copy was folded away) and the key loads are dead; every store sits in its own try range whose
    # handler only closes the iterator.
    code = _code("destructuring_member_targets_98_11908.hasm", 11908)

    assert "[r0[0], r0[1]] = r5;" in code
    assert "goto" not in code
    assert ".next()" not in code


def test_a_register_read_after_the_pattern_is_restored_from_its_slot():
    # 98/5806: `const [a, b] = useState(...)` where `a` is a closure variable that is also kept in a register
    # (`r8`) and read later. The pattern stores into the slot; the register is read back from it.
    code = _code("destructuring_slot_restore_98_5806.hasm", 5806)

    assert "[__environment__[3], __environment__[4]] = r11;" in code
    assert "r8 = __environment__[3];" in code
    assert "goto" not in code
    assert ".next()" not in code


def test_fetch_that_reads_the_source_register_without_a_copy():
    # 98/10000: `const [key] = args`: the source already sits in the register `IteratorNext` reads, so
    # there is no `Mov t <- src` before the first fetch.
    code = _code("destructuring_no_source_copy_98_10000.hasm", 10000)

    assert "[r3] = r2;" in code
    assert ".next()" not in code


def test_environment_created_between_the_fetch_and_the_first_store():
    # 98/10817: parameter destructuring into a fresh environment. `CreateFunctionEnvironment` sits in the
    # element block, right before the store into its slot; the allocation moves in front of the pattern.
    code = _code("destructuring_env_creation_98_10817.hasm", 10817)

    assert "[__environment__[0], r11] = param1;" in code
    assert "r8 = __environment__[0];" in code
    assert ".next()" not in code


def test_no_source_copy_and_the_undefined_loaded_inside_the_check():
    # 98/10001: `const [key] = args` where the first block is `IteratorNext; Mov; LoadConstUndefined; StrictEq;
    # LoadConstUndefined; JmpTrue` (the shape of F-234 with the `undefined` loaded in the middle of the check).
    code = _code("destructuring_no_copy_late_undefined_98_10001.hasm", 10001)

    assert "[r2] = r1;" in code
    assert ".next()" not in code
