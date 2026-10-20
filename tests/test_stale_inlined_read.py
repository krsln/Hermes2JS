"""
A value built from a register (`r1 = r0[0]`, an environment slot) that is read
after that register was overwritten must not be inlined: the register in it
would then name the NEW value (F-01, F-04).

The frontend inlines a load into its reader and cannot yet know whether a
LATER definition of the register it mentions will end up printed. A scratch
pass (`OpcodeDispatcher.dispatch_all`) now tells the real pass which
definitions print - pinned by a bare read, or never folded into a reader.

    96/4456  r1 = r0[0]; r0 = {...}; r1._responderRegion = r0
             printed `r0[0]._responderRegion = r0`: `r0[0]` of the new object.
    96/9118  r4 = r0[0]; r0 = undefined; r0 = r4(r2)
             printed `r0 = undefined; r0 = r0[0](r2)`.

Also covered: when a fold swaps a register callee for a member expression, the
call keeps `this = undefined` (`env[1].call(undefined, x)`, not `env[1](x)`,
which would pass `env` as `this`).
"""

from pathlib import Path

from hermes_decompiler.Decompiler import Decompiler
from hermes_decompiler.backend.emit.printer.ExpressionPrinter import ExpressionPrinter
from hermes_decompiler.backend.transforms.shared import substitute_register
from hermes_decompiler.ir.expressions import (
    CallExpression, Identifier, MemberExpression, NumericLiteral, UndefinedLiteral,
)

_DATA = Path(__file__).parent / "data"


def _render(name: str, function_id: int) -> str:
    hasm = (_DATA / name).read_text(encoding="utf-8")
    out = Decompiler.render(Decompiler.build_context(hasm, function_id, strict=False), verbose=False, raw=False)

    return "\n".join(line for line in out.split("\n") if not line.strip().startswith("//"))


def test_environment_load_is_kept_when_the_register_is_overwritten_by_a_literal():
    """96/4456: the literal that overwrites `r0` is printed, so `r1` keeps its own statement."""
    out = _render("any_of_params_96_4456.hasm", 4456)

    assert "r1 = r0[0];" in out
    assert "r1._responderRegion = r0;" in out
    assert "r0[0]._responderRegion" not in out


def test_callee_load_is_kept_when_the_register_is_overwritten_before_the_call():
    """96/9118: `r4 = r0[0]` ... `r0 = undefined` ... `r4(r0)`. The call folds into
    the test (`r1 === 1 && env[0].call(undefined, param1[0])`): its callee comes from
    the environment load, not from `r0` as it is by then, and `this` is undefined."""
    out = _render("parseScaleX_stale_callee_96_9118.hasm", 9118)

    assert "goto" not in out
    assert "getEnvironment(0)[0].call(undefined, param1[0])" in out
    assert "r0[0](" not in out
    assert "undefined[0]" not in out


def test_a_register_callee_replaced_by_a_member_keeps_this_undefined():
    call = CallExpression(callee=Identifier("r4"), arguments=(Identifier("x"),))
    member = MemberExpression(obj=Identifier("env"), prop=NumericLiteral(1), computed=True)

    folded = substitute_register(call, "r4", member)

    assert ExpressionPrinter().visit(folded) == "env[1].call(undefined, x)"
    assert isinstance(folded.arguments[0], UndefinedLiteral)


def test_a_register_callee_replaced_by_another_register_stays_a_plain_call():
    call = CallExpression(callee=Identifier("r4"), arguments=(Identifier("x"),))

    folded = substitute_register(call, "r4", Identifier("r7"))

    assert ExpressionPrinter().visit(folded) == "r7(x)"
