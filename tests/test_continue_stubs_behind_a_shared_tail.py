"""Stores that end in `continue`, laid out behind a tail two tests fall into (98/8045 `parseSingleTransitionShorthand`).

`if (isTimeUnit(t)) { if (duration === undefined) <store>; else if (delay === undefined) <store> }` followed by the
`timingFunction` code: the compiler put the two stores AFTER that code, so the second test jumped forward past it
and the structurer left `goto label_245`. The last retry moves such a stub behind its test and reads the tail as
the code after the `if`, which every other path of the arm also reaches.
"""

from pathlib import Path

from hermes_decompiler.Decompiler import Decompiler

_DATA = Path(__file__).parent / "data"


def _render() -> str:
    hasm = (_DATA / "continue_stubs_behind_a_shared_tail_98_8045.hasm").read_text(encoding="utf-8")
    out = Decompiler.render(Decompiler.build_context(hasm, 0, strict=False), verbose=False, raw=False)

    return "\n".join(line for line in out.split("\n") if not line.strip().startswith("//"))


def test_no_goto_is_left():
    assert "goto" not in _render()


def test_the_timing_function_code_follows_the_time_unit_branch():
    out = _render()
    time_unit = out.split("if (r12) {")[1]
    arm, after = time_unit.split("r12 = r0.transitionTimingFunction;")[0], time_unit.split("r12 = r0.transitionTimingFunction;")[1]

    # the duration and delay stores sit in the arm; the timing code comes once, behind it (both paths reach it)
    assert "r0.transitionDuration = r11;" in arm and "r0.transitionDelay = r11;" in arm
    assert out.count("r12 = r0.transitionTimingFunction;") == 1
    assert "r0.transitionTimingFunction = r11;" in after
