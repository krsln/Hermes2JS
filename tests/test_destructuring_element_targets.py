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
