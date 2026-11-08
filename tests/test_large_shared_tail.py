"""A shared tail too big for the small copy limit is copied on the last rung (F-217, 98/6570).

    if (!a) goto T;  ...  r1 = false; if (c) goto J;  T: <several tests>;  J: return r1

`T` is the first test's target and the fall-through of the last test, whose other exit skips it: no `if` owns it.
`SharedTailDuplicationCfgPass` gives the skipping test its own copy, but `T` is longer than the usual limit (12
instructions / 4 blocks); the last retry rung raises it, so the earlier rungs keep the shapes they already built.
"""

from pathlib import Path

from hermes_decompiler.Decompiler import Decompiler
from hermes_decompiler.backend.transforms.cfg_passes import SharedTailDuplicationCfgPass

_DATA = Path(__file__).parent / "data"


def _render() -> str:
    hasm = (_DATA / "large_shared_tail_98_6570.hasm").read_text(encoding="utf-8")
    out = Decompiler.render(Decompiler.build_context(hasm, 6570, strict=False), verbose=False, raw=False)
    return "\n".join(line for line in out.split("\n") if not line.strip().startswith("//"))


def test_a_long_shared_tail_gets_a_private_copy():
    code = _render()

    assert "goto" not in code
    assert code.count("param1.preventDefault()") == 1


def test_the_large_limit_is_the_last_rung_only():
    small = SharedTailDuplicationCfgPass(None, regions=True, per_predecessor=True)
    large = SharedTailDuplicationCfgPass(None, regions=True, per_predecessor=True, large=True)

    assert small.max_instructions == 12 and small.max_region_blocks == 4
    assert large.max_instructions > 12 and large.max_region_blocks > 4
