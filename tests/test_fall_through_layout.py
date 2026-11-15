"""A branch's fall-through stays right behind it, and a long `return` tail is copied (F-12, 98/12903).

    if (r8) goto AWAIT;                  // falls into T (the layout put T last: the topological order of the
    T: requestPermission(...); return    //   generator dispatch)
    AWAIT: await ...;  if (!c) goto T;

`GeneratorStateDispatchCfgPass` orders the blocks by address under the topological order, so `T` (entered by
two resume tests as well) came after all of them. The output printed `if (r8) goto label_325;` and then the
await: the code for `!r8` was not behind the branch (wrong, not just a `goto`). On the last rungs the two
resume tests get their own copy of `T` (ten instructions; the limit was nine) and `FallThroughLayoutCfgPass`
moves the original behind the branch.
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
        (10465, (_DATA / "generator_tail_layout_98_10465_creator.hasm").read_text(encoding="utf-8")),
        (12903, (_DATA / "generator_tail_layout_98_12903.hasm").read_text(encoding="utf-8")),
    ]
    tables = BatchPipeline([
        CreatorTableStage(), EnvironmentOriginTableStage(), PrivateNameTableStage(), ClassEnvironmentTableStage(),
    ]).run(BatchContext(sections=sections)).to_batch_tables()
    out = Decompiler.render(
        Decompiler.build_context(sections[1][1], 12903, batch_tables=tables), verbose=False,
    )

    return "\n".join(line for line in out.split("\n") if not line.strip().startswith("//"))


def test_the_test_of_r8_owns_both_arms():
    code = _render()

    assert "goto" not in code
    assert "if (r8) {\n        r7 = r7[1];" in code
    assert "} else {\n        r8 = r1[2][0];" in code or "} else {\n        r10 = r1[3][1];" in code


def test_every_exit_calls_request_permission():
    # the `!r8` path and the two failed resume tests all reach `requestPermission`
    assert _render().count("requestPermission(") == 3
