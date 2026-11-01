"""
A small tail entered by a fall-through and by jumps, while an earlier test skips it, gets a copy per
way in (98/2216 `getScriptURL`).

    if (r5 == null) goto J;  ...  r3 = null;  if (startsWith) goto END;  ...
    if (includes) goto J;  r5 = "file://" + r7;
    J: r3 = r5       END: r4[5] = r3

`J` has three ways in; the first attempt printed it in the `r5 == null` arm only and stored the wrong
value on the other paths (`r4[5] = r5` even for an `assets://` URL, where it must be `null`). Level 5 of
the retries copies `J` per way in and names the register after the join.
"""

from pathlib import Path

from hermes_decompiler.Decompiler import Decompiler

_DATA = Path(__file__).parent / "data"


def test_every_way_into_the_shared_tail_writes_the_register_it_reads_after():
    hasm = (_DATA / "shared_tail_each_way_98_2216.hasm").read_text(encoding="utf-8")

    out = Decompiler.render(Decompiler.build_context(hasm, 2216, strict=False), verbose=False, raw=False)

    assert "goto" not in out
    assert out.count("r3 = r5;") == 2
    assert "r3 = null;" in out
    assert "r4[5] = r3;" in out
