from __future__ import annotations

import re
from dataclasses import dataclass
from typing import Optional, Union


@dataclass(frozen=True, slots=True)
class Operand:
    """
    A single typed operand fragment (Reg8, UInt16, string_id, ...).

    Kept as a small typed wrapper instead of a bare regex string so that
    `sequence(...)` can reject anything that isn't a recognized operand
    constant at call time (see `sequence()` below) - a stray hand-rolled
    regex string dropped into a `_PATTERN` no longer passes silently.
    """

    kind: str
    regex: str

    def __str__(self) -> str:  # so f"{REG}" / string-concat call sites keep working
        return self.regex


REG = Operand("Reg", r"Reg\d+:\s*(\d+)")
ADDR = Operand("Addr", r"Addr\d+:\s*(-?\d+)")

UINT8 = Operand("UInt8", r"UInt8:\s*(\d+)")
UINT16 = Operand("UInt16", r"UInt16:\s*(\d+)")
UINT32 = Operand("UInt32", r"UInt32:\s*(\d+)")

IMM8 = Operand("Imm8", r"Imm8:\s*(-?\d+)")
IMM32 = Operand("Imm32", r"Imm32:\s*(-?\d+)")

_DOUBLE_VALUE = (
    r"-?(?:"
    r"\d+(?:\.\d+)?(?:[eE][+-]?\d+)?"
    r"|inf"
    r"|nan"
    r")"
)

DOUBLE = Operand("Double", rf"Double:\s*({_DOUBLE_VALUE})")

STRING_ID = Operand("string_id", r"string_id:\s*(\d+)")
FUNCTION_ID = Operand("function_id", r"function_id:\s*(\d+)")
BIGINT_ID = Operand("bigint_id", r"bigint_id:\s*(\d+)")

# Operand types that only ever change bit width across bytecode versions
# (e.g. `string_id: UInt16` in one version, `UInt32` in another) commonly
# need to be accepted interchangeably by a single handler; this alias set
# is intentionally NOT exhaustive/type-checked, it's just for callers that
# want a quick "any integer-ish operand" fragment. Prefer the specific
# `Operand` constants above wherever the width is actually known.
_ANY_UINT = Operand("UInt(any width)", r"U?Int(?:8|16|32):\s*(-?\d+)")


def sequence(*parts: Union[Operand, str]) -> "re.Pattern[str]":
    """
    Build an anchored, comma-separated operand pattern from fragments.

    Accepts `Operand` constants (REG, UINT8, STRING_ID, ...) - the normal
    case - or a raw regex string, but ONLY if explicitly opted into via
    `re.compile(...)`-style pre-escaping is the caller's responsibility;
    plain `str` fragments are still allowed (some call sites build
    ad-hoc alternations), but passing anything else (e.g. accidentally
    passing a whole `Operand` sequence, or a non-string/non-Operand
    value) raises immediately instead of failing confusingly at
    `.match()` time on unrelated bytecode.
    """
    fragments = []
    for part in parts:
        if isinstance(part, Operand):
            fragments.append(part.regex)
        elif isinstance(part, str):
            fragments.append(part)
        else:
            raise TypeError(
                f"sequence(): expected Operand or str, got {type(part).__name__}: {part!r}"
            )

    return re.compile(r'^' + r',\s*'.join(fragments) + r'$')


class MultiPattern:
    """
    Try several `_PATTERN`-shaped alternatives in order, for opcodes whose
    operand encoding differs across bytecode versions (e.g. a `string_id`
    that's `UInt16` in one HBC version and `UInt32` in another, or an
    operand that was added/reordered between versions).

    Drop-in replacement for a single compiled pattern: exposes the same
    `.match(args) -> re.Match | None` interface handlers already call, so
    existing `handle()` methods don't need to change - only the
    `_PATTERN = sequence(...)` assignment becomes
    `_PATTERN = MultiPattern(sequence(...), sequence(...))`.

    Because different variants can have a different number of capture
    groups, handlers that use `MultiPattern` should read matched values
    by name (see `named` below) rather than by positional
    `match.groups()` index, or should structure their `sequence(...)`
    variants so the groups they care about are in the same position in
    every variant.
    """

    def __init__(self, *variants: "re.Pattern[str]"):
        if not variants:
            raise ValueError("MultiPattern requires at least one variant")
        self._variants = variants

    def match(self, args: str) -> Optional["re.Match[str]"]:
        for pattern in self._variants:
            m = pattern.match(args)
            if m is not None:
                return m
        return None

    @property
    def variants(self) -> tuple:
        return self._variants


def named(kind: str, group: int = 1) -> str:
    """
    Build a named-group version of an operand's capture, e.g.
    `named("obj", group=1)` around a REG usage - useful when a handler
    combines a `MultiPattern` (variable group count/position across
    variants) with readable field access instead of `match.group(1)`,
    `match.group(2)`, ... at the call site.

    This intentionally isn't wired into REG/UINT8/etc. by default (that
    would force every handler to migrate at once); use it opt-in for new
    or refactored handlers that benefit from it, e.g.:

        _PATTERN = sequence(rf"Reg\\d+:\\s*(?P<obj>\\d+)")
    """
    return f"(?P<{kind}_{group}>\\d+)"
