"""A register that no longer holds the class factory does not name a slot (98/570, `downloadAsync` of expo-asset).

`ClassEnvironmentTable` follows `CreateClosure r1, <helper>` -> `Call r1, r1` -> `StoreToEnvironment slot, r1`. It
kept `r1` as the helper after `LoadParam r1` and `GetByIndex r1` had overwritten it, so the module's slot 0
(`requireNativeModule("ExpoAsset")`) was named after the class `?anon_0_downloadAsync` and 98/12943 read
`r7 = ?anon_0_downloadAsync; r7.downloadAsync(...)`: not valid JavaScript, and the wrong object.
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
        (570, (_DATA / "native_module_slot_98_570.hasm").read_text(encoding="utf-8")),
        (5052, (_DATA / "native_module_slot_98_570_5052.hasm").read_text(encoding="utf-8")),
        (10540, (_DATA / "native_module_slot_98_570_10540.hasm").read_text(encoding="utf-8")),
        (12943, (_DATA / "native_module_slot_98_570_12943.hasm").read_text(encoding="utf-8")),
    ]
    tables = BatchPipeline([
        CreatorTableStage(), EnvironmentOriginTableStage(), PrivateNameTableStage(), ClassEnvironmentTableStage(),
    ]).run(BatchContext(sections=sections)).to_batch_tables()

    return Decompiler.render(Decompiler.build_context(sections[3][1], 12943, batch_tables=tables), verbose=False)


def test_the_native_module_is_not_named_after_a_class():
    out = _render()

    assert "?anon_" not in out
    assert "anon_0_downloadAsync;" not in out


def test_the_slot_is_read_from_the_environment():
    assert "r7 = r5[0];" in _render()
