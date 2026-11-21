"""The code behind a jump-table `switch` whose `default:` can `throw` was printed as the body of the empty cases
(98/2632 `commitBeforeMutationEffects`).

A `throw` in the default arm leaves the switch header without an immediate post-dominator, so the join (`r10 =
r12.sibling ...`) looked like one more case body: `case 3: case 4: ...` held it, `case 0`/`case 1` ended in a
`break` that skipped it, and the `try` in `case 1` kept a `goto` into it. The join is the last jump table target
that the other arms jump into: it follows the switch.
"""

from pathlib import Path

from hermes_decompiler.Decompiler import Decompiler

_DATA = Path(__file__).parent / "data"


def _render() -> str:
    hasm = (_DATA / "switch_join_after_a_throwing_default_98_2632.hasm").read_text(encoding="utf-8")
    return Decompiler.render(Decompiler.build_context(hasm, 0, strict=False), verbose=False, raw=False)


def test_no_goto_is_left():
    assert "goto label_" not in _render()


def test_the_join_runs_after_the_switch_not_inside_the_empty_cases():
    out = _render()
    empty_cases = out.split("case 3:")[1].split("default:")[0]

    assert "sibling" not in empty_cases
    assert out.index("r12.sibling") > out.index("default:")
