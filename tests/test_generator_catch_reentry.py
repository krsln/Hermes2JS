"""A `catch` that resumes a generator/async state by re-entering the dispatch chain is folded (F-12, F-239).

The body's `try` has one exception handler: `catch (e) { env[5] = e; if (env[6] === 0) throw e;
env[4] = <state>; jmp <dispatch head> }`. The state is a constant the chain maps to a block (the cleanup / the
`catch` clause), so the jump is a jump to that block; the chain no longer stays reachable and the function folds.

    98/12484 `generatorTryFinallyTest`, 98/13743 `asyncTryCatchTest`, 98/13744 `asyncLoopTest`, 98/12918 and more

Three things have to hold together: the re-entry gets its OWN copy of the target's code (an edge from the `catch` into
the protected range would put the handler in front of the `try`), `try_blocks` is ordered by the folded layout (the
`try` starts at the first protected block, not at the resume code that has the lowest address), and the prologue's
other definitions the body reads (`r9 = getParentEnvironment(1)`, 98/13744; 98/13832 and 98/14155 too) are defined again.
"""

from __future__ import annotations

from test_register_semantics import decompile


def test_generator_try_finally_folds_into_a_try_with_the_cleanup_in_the_catch():
    out = decompile("98", 12484)

    assert "goto" not in out
    assert "NOT valid JavaScript" not in out
    assert "} catch (caughtException) {" in out
    # The try starts at the function body, not after the first `yield`.
    assert out.index("try {") < out.index('yield "a"')
    # The cleanup is reachable from the catch as its own copy.
    assert out.count("generatorTryFinallyTest/cleanup") == 2


def test_async_try_catch_keeps_the_await_inside_the_try():
    out = decompile("98", 13743)

    assert "goto" not in out
    assert out.index("try {") < out.index("await ")


def test_prologue_environment_the_body_reads_is_defined_again():
    # 98/13744 `asyncLoopTest`: `r1[5] = r9` where `r9 = getParentEnvironment(1)` sat in the folded prologue.
    out = decompile("98", 13744)

    assert "r9 = getParentEnvironment(1);" in out
    assert out.index("r9 = getParentEnvironment(1);") < out.index("r1[5] = r9;")
