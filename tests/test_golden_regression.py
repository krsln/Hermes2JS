"""
Golden-output regression tests for the full `.hasm` -> JavaScript pipeline.

Motivation: prior to this file, the only automated test coverage
(`test_opcode_name_validation.py`) checked that registered opcode handler
*names* correspond to real Hermes opcodes. Nothing exercised the actual
decompilation logic - CFG construction, dominance, loop/if/switch
structuring, region passes, or JS emission - so a regression in any of
that could land silently.

`apps/demo/fixtures/<set>/sections/function_<n>_<name>.hasm` and the
matching committed JavaScript outputs under
`apps/demo/fixtures/<set>/results/` already exist. Normal output keeps
the function name:

    function_<n>_<name>.js

while raw output uses:

    function_<n>.raw.js

This file turns that existing, already-reviewed data into an automated
regression net: every fixture section must keep decompiling to exactly
the JavaScript already committed alongside it.

Important caveat: the golden files are themselves generator output, not
independently hand-verified-correct JavaScript. A failure here means
"behavior changed since these were captured", not "this JS is wrong" -
that change may well be an intended improvement. When that's the case,
regenerate the affected golden file(s) as part of the same change (e.g.
via `scripts/decompile_sections.py`) and review the diff like any other
code change, rather than deleting or skipping the test.
"""

from __future__ import annotations

import re
from pathlib import Path
from typing import NamedTuple

import pytest

from hermes_decompiler.Decompiler import Decompiler
from hermes_decompiler.frontend.parsing import BatchContext, BatchPipeline, BatchTables
from hermes_decompiler.frontend.parsing.batch_stages import (
    ClassEnvironmentTableStage, CreatorTableStage, EnvironmentOriginTableStage, PrivateNameTableStage,
)

_REPO_ROOT = Path(__file__).resolve().parents[1]
_FIXTURES_ROOT = _REPO_ROOT / "apps" / "demo" / "fixtures"
_FUNCTION_RE = re.compile(r"^function_(?P<number>\d+)_(?P<name>.+)\.hasm$")


class _GoldenCase(NamedTuple):
    fixture_name: str
    sections_dir: Path
    results_dir: Path
    function_name: str
    function_index: int


def _discover_golden_cases() -> list[_GoldenCase]:
    """
    Find every fixture function that has both a
    `function_<n>_<name>.hasm` input and a matching
    `function_<n>_<name>.js` golden output.

    Raw output, when present, is expected to use the
    `function_<n>.raw.js` naming convention.

    Returns an empty list (rather than raising at collection time) when
    the fixtures directory isn't present.
    """
    cases: list[_GoldenCase] = []

    if not _FIXTURES_ROOT.is_dir():
        return cases

    for fixture_dir in sorted(_FIXTURES_ROOT.iterdir()):
        sections_dir = fixture_dir / "sections"
        results_dir = fixture_dir / "results"

        if not (sections_dir.is_dir() and results_dir.is_dir()):
            continue

        for hasm_path in sorted(sections_dir.glob("function_*.hasm")):
            match = _FUNCTION_RE.match(hasm_path.name)
            if not match:
                continue

            function_index = int(match.group("number"))
            function_name = match.group("name")

            golden_path = results_dir / (f"function_{function_index}_{function_name}.js")

            if not golden_path.exists():
                continue

            cases.append(
                _GoldenCase(
                    fixture_name=fixture_dir.name,
                    sections_dir=sections_dir,
                    results_dir=results_dir,
                    function_name=function_name,
                    function_index=function_index,
                )
            )

    return cases


_CASES = _discover_golden_cases()
_CASE_IDS = [
    f"{case.fixture_name}/function_{case.function_index}_{case.function_name}"
    for case in _CASES
]

#: One BatchTables bundle per fixture set (96, 98, ...), built once from
#: that set's complete `sections/` directory - the same input
#: `FileOperations.build_batch_tables` scans for a real batch run via
#: `scripts/decompile_sections.py`. Built here, not per-case, because
#: every table this bundles needs an edge that lives in a *different*
#: section than the one being tested (see CreatorTable/
#: EnvironmentOriginTable/PrivateNameTable/ClassEnvironmentTable) - so a
#: table built from a single case's own `.hasm` file would never resolve
#: anything and every fixture depending on one would silently fall back
#: to whatever a lone section can determine on its own.
_BATCH_TABLES: dict[str, BatchTables] = {}

for _sections_dir in {case.sections_dir for case in _CASES}:
    _fixture_name = _sections_dir.parent.name
    _sections: list[tuple[int, str]] = []

    for _hasm_path in sorted(_sections_dir.glob("function_*.hasm")):
        _match = _FUNCTION_RE.match(_hasm_path.name)
        if _match:
            _sections.append((int(_match.group("number")), _hasm_path.read_text(encoding="utf-8")))

    _batch_context = BatchPipeline([
        CreatorTableStage(),
        EnvironmentOriginTableStage(),
        PrivateNameTableStage(),
        ClassEnvironmentTableStage(),
    ]).run(BatchContext(sections=_sections))

    _BATCH_TABLES[_fixture_name] = _batch_context.to_batch_tables()


@pytest.mark.skipif(
    not _CASES,
    reason="No golden fixtures found under apps/demo/fixtures/*/{sections,results}",
)
@pytest.mark.parametrize("case", _CASES, ids=_CASE_IDS)
def test_matches_golden_output(case: _GoldenCase) -> None:
    """
    Decompiling a fixture function must keep producing byte-for-byte the
    same JavaScript already committed under `results/`.

    Mirrors `FileOperations.process_section`'s call shape (one
    `build_context()` against the fixture set's `BatchTables`, rendered
    once normally and, if present, once raw) so this also guards the
    "build once, render multiple times" contract `Decompiler` documents -
    a bug that leaks state between two renders of the same context would
    show up here.
    """
    hasm_path = (case.sections_dir / f"function_{case.function_index}_{case.function_name}.hasm")

    hasm_content = hasm_path.read_text(encoding="utf-8")

    context = Decompiler.build_context(
        hasm_content, case.function_index, strict=False,
        batch_tables=_BATCH_TABLES.get(case.fixture_name),
    )

    actual_js = Decompiler.render(context, verbose=True, raw=False)
    expected_js_path = (case.results_dir / f"function_{case.function_index}_{case.function_name}.js")
    expected_js = expected_js_path.read_text(encoding="utf-8")
    assert actual_js == expected_js

    golden_raw_path = (case.results_dir / f"function_{case.function_index}.raw.js")

    if golden_raw_path.exists():
        actual_raw_js = Decompiler.render(context, verbose=True, raw=True)
        expected_raw_js = golden_raw_path.read_text(encoding="utf-8")
        assert actual_raw_js == expected_raw_js


@pytest.mark.skipif(
    not _CASES,
    reason="No golden fixtures found under apps/demo/fixtures/*/{sections,results}",
)
@pytest.mark.parametrize("case", _CASES, ids=_CASE_IDS)
def test_render_is_order_independent(case: _GoldenCase) -> None:
    """
    Regression guard for a real bug: `render()` must not leak state
    between two renders of the same `PipelineContext`, in either
    direction.

    It previously did - rendering `raw=False` first would mutate the
    `OpcodeResult` instances backing `context.analysis.results` in
    place (structuring/region passes reassign `.value`/`.statement`/
    `.terminator`/`.definition_used` directly on them - see
    `OpcodeResult.clone`'s docstring), so a later `raw=True` render on
    that same context would see already-transformed IR instead of the
    original dispatched output. `FileOperations.process_section` always
    happened to render raw *first*, which is the only reason this went
    unnoticed - `test_matches_golden_output` above only ever exercised
    that one safe order.

    This test renders both orders from two otherwise-identical fresh
    contexts and requires them to agree, independent of any golden file.
    """
    golden_raw_path = (case.results_dir / f"function_{case.function_index}.raw.js")

    if not golden_raw_path.exists():
        pytest.skip("No raw output recorded for this function - nothing to compare orders against.")

    hasm_path = (case.sections_dir / f"function_{case.function_index}_{case.function_name}.hasm")
    hasm_content = hasm_path.read_text(encoding="utf-8")

    ctx_a = Decompiler.build_context(hasm_content, case.function_index, strict=False)
    js_first = Decompiler.render(ctx_a, verbose=True, raw=False)
    raw_second = Decompiler.render(ctx_a, verbose=True, raw=True)

    ctx_b = Decompiler.build_context(hasm_content, case.function_index, strict=False)
    raw_first = Decompiler.render(ctx_b, verbose=True, raw=True)
    js_second = Decompiler.render(ctx_b, verbose=True, raw=False)

    assert js_first == js_second
    assert raw_first == raw_second
