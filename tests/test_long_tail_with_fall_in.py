"""A tail of up to nine instructions that a fall-through enters as well is copied when it reads the same on every
path (F-218, 98/2930 `resolve`).

    if (!a) goto T;  if (typeof a !== "object" ...) goto T;  ...  if (typeof then === "function") goto BIND;
    T: _y = 1; _z = v; finale(p); return           (eight instructions: two jumps and the fall-through enter it)

The last rung copies a tail longer than six instructions only when jumps alone reach it: with a fall-through the
paths may hold different values for what the tail reads (98/2844). `_reads_the_same_on_every_path` says whether they
do; here nothing the tail reads is written differently, so the fall-through counts too. The `goto` for the
`typeof then` test is gone and the `_y = 1` tail is the `else` of it.
"""

from pathlib import Path

from hermes_decompiler.Decompiler import Decompiler

_DATA = Path(__file__).parent / "data"


def test_the_fulfil_tail_is_the_else_of_the_typeof_test():
    hasm = (_DATA / "long_tail_with_fall_in_98_2930.hasm").read_text(encoding="utf-8")
    out = Decompiler.render(Decompiler.build_context(hasm, 2930, strict=False), verbose=False, raw=False)
    code = "\n".join(line for line in out.split("\n") if not line.strip().startswith("//"))

    assert "goto" not in code
    assert '} else if (typeof r7 === "function") {' in code
    assert "} else {\n                param1._y = 1;\n                param1._z = param2;" in code
