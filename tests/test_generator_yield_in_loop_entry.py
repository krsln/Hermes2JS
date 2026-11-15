"""A generator whose `yield` sits in a loop entered by two tests folds into a `for` (F-12, 98/9673 `createKeyIterator`).

    r7 = env[1][1]            // the yielded value, computed BEFORE the resume point's constant load
    r5 = 1                    // resume point
    env[2] = r5               // protocol

The constant load between the value and the suspend was an "unrecognized instruction" and the whole dispatch
stayed raw. Folded, the loop body (entered by the first test and by the latch) has to precede the `return` the
first test falls into; without a bridge block behind the branch the structurer read the wrong arm and printed
`if (r7 >= r5) { for ... }` around the loop (the loop never ran).
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
        (1719, (_DATA / "generator_loop_yield_98_9673_creator.hasm").read_text(encoding="utf-8")),
        (9673, (_DATA / "generator_loop_yield_98_9673.hasm").read_text(encoding="utf-8")),
    ]
    tables = BatchPipeline([
        CreatorTableStage(), EnvironmentOriginTableStage(), PrivateNameTableStage(), ClassEnvironmentTableStage(),
    ]).run(BatchContext(sections=sections)).to_batch_tables()

    return Decompiler.render(Decompiler.build_context(sections[1][1], 9673, batch_tables=tables), verbose=False)


def test_the_loop_runs_and_yields():
    code = _render()

    assert "goto" not in code
    assert "yield r1[1][1];" in code
    assert "if (r7 >= r5)" not in code
    assert "for (; r7 < r5; )" in code
    # the exhausted result comes after the loop, not inside the `if`
    assert code.index("for (") < code.index('"done": true')
