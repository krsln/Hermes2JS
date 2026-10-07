"""
Semantic checks for how registers are folded and how call-argument windows
are read, independent of the committed golden output.

The golden files are regenerated from the decompiler itself, so a wrong
output that was ever committed stays "correct" there. Each case below pins
a property that is true of the BYTECODE (checked by hand against the .hasm
listing), e.g. "every `rN` read has a printed definition" or "the
`this` slot of a CallBuiltin window is not an argument".

Inputs are real fixture sections (`apps/demo/fixtures/<set>/sections`),
decompiled the way `scripts/decompile_sections.py` does, with that set's
batch tables.
"""

from __future__ import annotations

import re
from functools import lru_cache
from pathlib import Path

import pytest

from hermes_decompiler.Decompiler import Decompiler
from hermes_decompiler.frontend.batch_pipeline import BatchContext, BatchPipeline
from hermes_decompiler.frontend.batch_pipeline.stages import (
    ClassEnvironmentTableStage, CreatorTableStage, EnvironmentOriginTableStage, PrivateNameTableStage,
)

_FIXTURES = Path(__file__).resolve().parents[1] / "apps" / "demo" / "fixtures"
_FUNCTION_RE = re.compile(r"^function_(?P<number>\d+)_(?P<name>.+)\.hasm$")

pytestmark = pytest.mark.skipif(not _FIXTURES.is_dir(), reason="fixtures not present")


@lru_cache(maxsize=None)
def _batch(fixture_set: str):
    sections = []

    for path in sorted((_FIXTURES / fixture_set / "sections").glob("function_*.hasm")):
        match = _FUNCTION_RE.match(path.name)
        if match:
            sections.append((int(match.group("number")), path.read_text(encoding="utf-8")))

    return BatchPipeline([
        CreatorTableStage(), EnvironmentOriginTableStage(), PrivateNameTableStage(), ClassEnvironmentTableStage(),
    ]).run(BatchContext(sections=sections)).to_batch_tables()


def decompile(fixture_set: str, function_id: int) -> str:
    """Final (non-raw) output of one fixture section, comments stripped."""
    path = next((_FIXTURES / fixture_set / "sections").glob(f"function_{function_id}_*.hasm"))

    context = Decompiler.build_context(
        path.read_text(encoding="utf-8"), function_id, batch_tables=_batch(fixture_set),
    )
    out = Decompiler.render(context, verbose=False)

    return "\n".join(line for line in out.split("\n") if not line.strip().startswith("//"))


_ASSIGNED = r"(?<![\w.$]){r}\s*=[^=]|for \((?:const|let|var) {r}\b|catch \({r}\)|\b(?:let|const|var) {r}\b"


def dangling_registers(source: str) -> list[str]:
    """`rN` names that are read somewhere but never assigned in `source`."""
    return [
        reg
        for reg in sorted(set(re.findall(r"(?<![\w.$])(r\d+)\b", source)))
        if not re.search(_ASSIGNED.format(r=reg), source)
    ]


# --- A.1: a folded definition must not be read back as a bare `rN` -------

def test_loop_bound_reads_the_items_register_not_a_dangling_one():
    # `Mov r2, r6` is read twice (an inlined use, then `r2.length`). The
    # first read used to fold the Mov away and leave `r2.length` dangling.
    out = decompile("96", 15084)

    assert dangling_registers(out) == []
    assert re.search(r"r2 = param1;\n", out)


def test_default_destructuring_reads_the_fetched_value_once():
    # `r3 = r2.timeout; ...; Mov r5, r3` -> `r5 = r3`, not a second
    # `r2.timeout` fetch; and `r2 = r2.retries` must not leave `r2.retries`
    # double-applied in the branch.
    out = decompile("96", 15104)

    assert "r5 = r3" in out
    assert "r4 = r2;\n" in out
    # one READ of each property (`.timeout` also appears once more as the
    # config literal's own `r2.timeout = 500`)
    assert out.count("= r2.timeout") == 1
    assert "r5 = r2.timeout" not in out
    assert out.count("= r2.retries") == 1


def test_increment_returns_the_stored_value_not_a_recomputation():
    out = decompile("96", 15213)

    assert "return r0 + 1" not in out
    assert "return r0;" in out


# --- closures are references, not calls -----------------------------------

def test_calling_a_closure_calls_it_once():
    out = decompile("96", 15072)

    assert 'sideEffect("and-left", param1)' in out
    assert "sideEffect(param1, param2)(" not in out


# --- A.2: CallBuiltin windows ---------------------------------------------

def test_callbuiltin_this_slot_is_not_an_argument():
    # bytecode: Mov r7,r4 / NewObjectWithBuffer r6 / CallBuiltin #44 argc=3
    # -> copyDataProperties(target=r7, source=r6); the third slot is `this`.
    out = decompile("96", 15119)

    assert "copyDataProperties(r7, r6)" in out
    assert dangling_registers(out) == []


def test_callbuiltin_window_top_is_not_the_highest_register_seen_so_far():
    # r11 was written earlier (by `new Set(...)`'s window), the builtin's
    # arguments are r10 (target), r9 (source), r8 (index 0).
    out = decompile("96", 15124)

    assert "arraySpread(r10, r9, r8)" in out
    assert dangling_registers(out) == []


def test_aliasing_a_constructed_object_does_not_construct_it_again():
    # `Mov r2, r3` / `Mov r9, r3` alias `unique`; they used to re-inline
    # `new Set(r10)`, i.e. build a second Set.
    out = decompile("96", 15124)

    assert out.count("new Set(") == 1
    assert "r2 = r3" in out


@pytest.mark.parametrize("function_id", [15110, 15118, 15120, 15132])
def test_builtin_calls_never_end_in_a_dangling_register(function_id):
    assert dangling_registers(decompile("96", function_id)) == []


def test_throw_type_error_takes_only_the_message():
    out = decompile("98", 9534)

    assert 'throwTypeError("Trying to call a non-function")' in out


def test_rest_args_builtin_keeps_only_the_start_index():
    out = decompile("98", 9514)

    assert "r8 = 0" in out
    assert "copyRestArgs(r8)" in out
