"""`yield [key, value]` folds: the array is filled after it is created, the cut moves behind the last store (F-12, 98/9674).

    r7 = [env[1][1]]              // NewArray + DefineOwnInDenseArray
    r5 = env[1][0][env[1][1]]     // the element's own computation sits between the stores
    r7[1] = r5                    // DefineOwnInDenseArray
    r5 = 1; env[2] = r5           // protocol

The cut was put at the `NewArray`, so the stores and loads behind it counted as unrecognized protocol and the
whole dispatch stayed raw.
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
        (1720, (_DATA / "generator_yield_array_98_9674_creator.hasm").read_text(encoding="utf-8")),
        (9674, (_DATA / "generator_yield_array_98_9674.hasm").read_text(encoding="utf-8")),
    ]
    tables = BatchPipeline([
        CreatorTableStage(), EnvironmentOriginTableStage(), PrivateNameTableStage(), ClassEnvironmentTableStage(),
    ]).run(BatchContext(sections=sections)).to_batch_tables()

    return Decompiler.render(Decompiler.build_context(sections[1][1], 9674, batch_tables=tables), verbose=False)


def test_the_array_is_built_and_yielded():
    code = _render()

    assert "goto" not in code
    assert "yield r7;" in code
    assert "r7[1] = r5;" in code
    assert code.index("r7[1] = r5;") < code.index("yield r7;")
    assert "for (; r7 < r5; )" in code
