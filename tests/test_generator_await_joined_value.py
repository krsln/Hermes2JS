"""`await ref?.f()` (`yield` here) folds although the suspend block holds only protocol (F-12, 98/13533 `startAnimating`).

    r7 = undefined; if (r8) skip; r7 = r9.f();     // the value joins two paths
    join:  env[2] = r5; env[1] = r5; {value: r7, done: false}; ret

The resume point's number (`r5 = 1`) was loaded in the dispatch chain, so the suspend block has no leading constant
load and was declined as "could not find the yielded value". It also needs a suspend that does not borrow the
protocol store's identity: the protocol strip removed the suspend together with the store it was taken from.
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
        (11786, (_DATA / "generator_await_joined_value_98_13533_creator.hasm").read_text(encoding="utf-8")),
        (13533, (_DATA / "generator_await_joined_value_98_13533.hasm").read_text(encoding="utf-8")),
    ]
    tables = BatchPipeline([
        CreatorTableStage(), EnvironmentOriginTableStage(), PrivateNameTableStage(), ClassEnvironmentTableStage(),
    ]).run(BatchContext(sections=sections)).to_batch_tables()

    return Decompiler.render(Decompiler.build_context(sections[1][1], 13533, batch_tables=tables), verbose=False)


def test_the_awaited_joined_value_is_kept():
    code = _render()

    assert "goto" not in code
    assert "may not be called on executing" not in code
    # the section pair alone does not say whether the wrapper is async, so the suspend prints as `yield`
    assert "yield r7;" in code or "await r7;" in code
    assert code.index("r7 = r9.startAnimating();") < code.index("r7;", code.index("r7 = r9.startAnimating();") + 30)
