"""A `for (x of param)` whose iterable is a parameter is a for-of (F-191).

Hermes primes a scratch register from the iterable right before `IteratorNext` (`r8 = r4`). With the iterable
a parameter the copy folds into `r8 = param2`, which `_is_plain_register_copy` did not take for the priming `Mov`,
so the header did not match, the loop stayed a `while` and printed the exit test BEFORE the statements that set
what it reads:

    while (!(r9 === undefined)) { r8 = r2.next(); r9 = r2; try { ... } catch { r2.return(); throw e } }

(`r9` is unset on the first check: the loop never ran.)

Two more things showed once the loop was recognized (98/5425 `matchAgainstConfigs`, whose body is a call and a
chain of tests with two `continue` edges):

  - the body's last block was a COPY of a latch (`loop.latches` held the original), its `goto` to the header
    stayed: `RedundantJumpRegionPass` also clears a trailing jump to the header at the end of the body;
  - the close on `break` reads the iterator through a scratch copy (`r8 = r2; r8.return(); break;`).

    98/7122 `cloneSet`   98/5425 `matchAgainstConfigs`
"""

from pathlib import Path

from hermes_decompiler.Decompiler import Decompiler

_DATA = Path(__file__).parent / "data"


def _render(name: str, function_id: int) -> str:
    hasm = (_DATA / name).read_text(encoding="utf-8")
    out = Decompiler.render(Decompiler.build_context(hasm, function_id, strict=False), verbose=False, raw=False)

    return "\n".join(line for line in out.split("\n") if not line.strip().startswith("//"))


def test_a_parameter_iterable_is_a_for_of():
    out = _render("for_of_param_iterable_98_7122.hasm", 7122)

    assert "for (const r8 of r4) {" in out
    assert "while" not in out and "caughtException" not in out and ".next()" not in out and ".return()" not in out


def test_the_back_edge_copy_and_the_close_on_break_are_scaffolding():
    out = _render("for_of_param_iterable_98_5425.hasm", 5425)

    # the body reuses r8 for the call result (`r8 = _loop.call(0, r8)`): a `let`, a `const` cannot be assigned (F-192)
    assert "for (let r8 of r4) {" in out
    assert "goto" not in out
    assert ".return()" not in out
    assert "break;" in out
