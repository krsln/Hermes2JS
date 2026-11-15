"""An async function that never awaits folds into its body (F-12, 98/12831 `queryCache`).

    async queryCache(key) { return default.queryCache(key); }

has a state machine with no suspend site: no resume slot, only the running/exhausted guards on the state and the
`.throw()`/`.return()` tests on the action in front of the body. With no site, `detect` returned None and the whole
machine stayed (17 files in 98). The body is what the first `.next()` runs, found by walking the guards and the
action tests.
"""

from pathlib import Path

from hermes_decompiler.Decompiler import Decompiler
from hermes_decompiler.frontend.batch_pipeline import BatchContext, BatchPipeline
from hermes_decompiler.frontend.batch_pipeline.stages import (
    ClassEnvironmentTableStage, CreatorTableStage, EnvironmentOriginTableStage, PrivateNameTableStage,
)

_DATA = Path(__file__).parent / "data"


def _render() -> str:
    sections = [
        (10269, (_DATA / "generator_no_suspend_98_12831_creator.hasm").read_text(encoding="utf-8")),
        (12831, (_DATA / "generator_no_suspend_98_12831.hasm").read_text(encoding="utf-8")),
    ]
    tables = BatchPipeline([
        CreatorTableStage(), EnvironmentOriginTableStage(), PrivateNameTableStage(), ClassEnvironmentTableStage(),
    ]).run(BatchContext(sections=sections)).to_batch_tables()

    return Decompiler.render(Decompiler.build_context(sections[1][1], 12831, batch_tables=tables), verbose=False)


def test_the_body_is_all_that_is_left():
    code = _render()

    assert "goto" not in code
    assert "may not be called on executing" not in code
    assert "switch" not in code
    assert "r7 = r7.queryCache(r8);" in code
    assert '{ "value": r7, "done": true }' in code
