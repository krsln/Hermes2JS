"""`__getClosureEnvironment__(r)` is environment plumbing, not a call that runs user code (F-228, 98/11900).

    if (len !== 1) goto T;  r5 = <closure env>; r6 = f(x); if (r6 || x === 0) goto B;  T: r6 = [];  B: ...

The crossed fold `len === 1 && (f(x) || x === 0)` counts the side effects of the second test's set-up: the closure
environment read counted as one (so did the call), two in all, and the fold was refused. With the read in
`PURE_CALLEES` the pair is one condition and the `goto` is gone.
"""

from pathlib import Path

from hermes_decompiler.Decompiler import Decompiler
from hermes_decompiler.backend.transforms.shared import has_side_effects
from hermes_decompiler.ir.expressions import CallExpression, Identifier

_DATA = Path(__file__).parent / "data"


def test_the_closure_environment_read_is_pure():
    read = CallExpression(callee=Identifier(name="__getClosureEnvironment__"), arguments=(Identifier(name="r4"),))

    assert not has_side_effects(read)


def test_the_guard_and_the_pair_become_one_condition():
    hasm = (_DATA / "closure_env_pure_98_11900.hasm").read_text(encoding="utf-8")
    out = Decompiler.render(Decompiler.build_context(hasm, 11900, strict=False), verbose=False, raw=False)
    code = "\n".join(line for line in out.split("\n") if not line.strip().startswith("//"))

    assert "goto" not in code
    assert "=== 1 && (" in code
