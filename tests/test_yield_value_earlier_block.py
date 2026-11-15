"""The yielded value may be computed in an earlier block than the suspend (F-231, 98/14158 `loadIcon`).

    r7 = env[1];  if (!r7) goto DONE;  r5 = r7 instanceof Promise;  if (r5) goto SUSPEND;  ...
    SUSPEND: r5 = 1; env[2] = r5; env[3] = r5; r5 = { value: null, done: false }; r5.value = r7; return r5

`GeneratorStateDispatchCfgPass` looked for the definition of the value register inside the suspend block only,
found none, and left the raw state machine (reentrancy guard, mode switch and all). A block that is nothing but
the protocol (constant loads, stores, the result object) now suspends on the register by name (`await r7`; `yield r7` when only the creator is in the set, as here).
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
        (13879, (_DATA / "yield_value_earlier_block_98_13879_creator.hasm").read_text(encoding="utf-8")),
        (14158, (_DATA / "yield_value_earlier_block_98_14158.hasm").read_text(encoding="utf-8")),
    ]
    tables = BatchPipeline([
        CreatorTableStage(), EnvironmentOriginTableStage(), PrivateNameTableStage(), ClassEnvironmentTableStage(),
    ]).run(BatchContext(sections=sections)).to_batch_tables()
    out = Decompiler.render(Decompiler.build_context(sections[1][1], 14158, batch_tables=tables), verbose=False)

    return "\n".join(line for line in out.split("\n") if not line.strip().startswith("//"))


def test_the_state_machine_becomes_a_suspend():
    code = _render()

    assert "goto" not in code
    assert "yield r7;" in code or "await r7;" in code
    assert "throwTypeError" not in code
