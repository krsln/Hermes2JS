"""A `case` whose code runs on into the next one prints no `break` (F-177).

Hermes lays `case 5: case 26: case 27: if (!a) f();` out right in front of `case 6: g(); return`, and the
first body falls into the second. The printer ended every case body with an `break;` it added itself, so
`g()` was skipped on those three values: 96/2103 `commitDeletionEffectsOnFiber` dropped the
`recursivelyTraverseDeletionEffects` call. A jump-table body that flows into the next case's entry is
marked `falls_through` (only when that case is printed right after it) and the safety `break` is left out.

    96/2103   cases 5, 26, 27 -> case 6
    96/2607   the same function in the other bundle layout: cases 5, 26 -> case 6
"""

from pathlib import Path

from hermes_decompiler.Decompiler import Decompiler

_DATA = Path(__file__).parent / "data"


def _render(name: str, function_id: int) -> str:
    hasm = (_DATA / name).read_text(encoding="utf-8")
    out = Decompiler.render(Decompiler.build_context(hasm, function_id, strict=False), verbose=False, raw=False)

    return "\n".join(line for line in out.split("\n") if not line.strip().startswith("//"))


def test_the_shared_labels_run_on_into_case_6():
    out = _render("switch_case_fallthrough_96_2103.hasm", 2103)

    assert "goto" not in out
    start = out.index("        case 5:")
    end = out.index("        case 6:")
    assert "break;" not in out[start:end]
    assert "r1[429].call(undefined, param3, param2);" in out[start:end]


def test_the_same_shape_in_another_function():
    out = _render("switch_case_fallthrough_96_2607.hasm", 2607)

    start = out.index("        case 5:")
    end = out.index("        case 6:")
    assert "break;" not in out[start:end]
