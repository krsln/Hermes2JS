"""A loop's `found` exit whose body is several blocks and only ends the function moves into the loop (96/2662).

    for (; r10 !== null; r10 = r10.return) {
        ...
        if (1 === r11 && (A || B && (C || D))) goto BODY;     // BODY is laid out behind the loop
    }
    BODY: r9 = ...; r8 = ...; if (null !== r6) { ... }        // and returns

`LoopBreakStructurer` knew single-block exit bodies only, so the branch stayed a `goto`. A body entered only
through that branch, with no edge back into the loop or on to shared code, is spliced in as `if (cond) { ... }`
(Shape E).
"""

from pathlib import Path

from hermes_decompiler.Decompiler import Decompiler

_DATA = Path(__file__).parent / "data"


def test_the_found_body_moves_into_the_loop():
    hasm = (_DATA / "loop_exit_body_of_several_blocks_96_2662.hasm").read_text(encoding="utf-8")
    code = Decompiler.render(Decompiler.build_context(hasm, 2662, strict=False), verbose=False, raw=False)

    assert "goto" not in code

    loop = code.split("for (; null !== r10;")[1]
    arm = loop.split("r9 = r0[266].call(undefined, param3, param1);")[0]

    assert 'getDerivedStateFromError' in arm.split("\n")[-2] or "getDerivedStateFromError" in arm
    assert "if (null !== r6) {" in loop
    assert loop.count("return undefined;") == 2
