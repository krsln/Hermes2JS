"""A closing `return` the paths disagree on is copied for the jumpers that set the value themselves (F-162).

    r0 = Number(v); jmp RET      RET: return r0      (other paths reach RET with other values of r0)

The copy of that jumper returns ITS value (`r0 = Number(v); return r0`) whatever the others hold; the original
`return` stays for them. Used only by the last retry level.

    96/7556  `parseValue`: three tests of the `parseNumbers` arm jump onto the code the first test skips to.
    96/9896  `getReduceMotionFromConfig`: `!p || p === System` with the loads in the middle block.
"""

from pathlib import Path

from hermes_decompiler.Decompiler import Decompiler

_DATA = Path(__file__).parent / "data"


def _render(name: str, function_id: int) -> str:
    hasm = (_DATA / name).read_text(encoding="utf-8")
    out = Decompiler.render(Decompiler.build_context(hasm, function_id, strict=False), verbose=False, raw=False)

    return "\n".join(line for line in out.split("\n") if not line.strip().startswith("//"))


def test_a_number_that_parses_returns_before_the_boolean_tests():
    out = _render("own_value_return_96_7556.hasm", 7556)

    assert "goto" not in out
    assert out.index("r0 = Number.call(undefined, param1);") < out.index("param2.parseBooleans")
    assert out.count("return r0;") == 2


def test_the_loads_of_an_or_chain_stay_in_front_of_its_second_test():
    out = _render("own_value_return_96_9896.hasm", 9896)

    assert "goto" not in out
    assert "return param1 === r0.Always;" in out
    assert out.rstrip().endswith("return r1.value;\n}")
