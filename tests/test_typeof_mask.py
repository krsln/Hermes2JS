"""
`TypeOfIs` / `JmpTypeOfIs` decode their `TypeOfIsTypes` bitmask with the bit
assignment `hermesc` itself uses (bytecode 98). The masks below are what
`hermesc -dump-bytecode` printed for the matching source:

    typeof x === "undefined" -> 1       typeof x === "bigint"   -> 64
    typeof x === "string"    -> 4       typeof x === "function" -> 128
    typeof x === "symbol"    -> 8       typeof x === "object"   -> 258 (null | object)
    typeof x === "boolean"   -> 16      typeof x !== "object"   -> 253
    typeof x === "number"    -> 32

The old tables were guesses: `4` read as boolean, `16` as string, `64` as
`function`, `128` as `bigint` (`TypeOfIs`), and `258` stayed unresolved
(98/9594, F-02).
"""

import pytest

from hermes_decompiler.backend.emit.printer.ExpressionPrinter import ExpressionPrinter
from hermes_decompiler.frontend.handlers.shared import build_typeof_condition
from hermes_decompiler.ir.expressions import Identifier


def _print(mask: int) -> str:
    return ExpressionPrinter().visit(build_typeof_condition(Identifier("x"), mask))


@pytest.mark.parametrize(
    ("mask", "expected"),
    [
        (1, 'typeof x === "undefined"'),
        (4, 'typeof x === "string"'),
        (8, 'typeof x === "symbol"'),
        (16, 'typeof x === "boolean"'),
        (32, 'typeof x === "number"'),
        (64, 'typeof x === "bigint"'),
        (128, 'typeof x === "function"'),
        (258, 'typeof x === "object"'),
    ],
)
def test_single_type_masks_are_the_ones_hermesc_emits(mask, expected):
    assert _print(mask) == expected


@pytest.mark.parametrize(
    ("mask", "expected"),
    [
        (253, 'typeof x !== "object"'),
        (495, 'typeof x !== "boolean"'),
        (383, 'typeof x !== "function"'),
    ],
)
def test_a_mask_covering_most_types_is_written_as_its_complement(mask, expected):
    assert _print(mask) == expected


def test_a_few_types_stay_a_positive_chain_in_bit_order():
    assert _print(4 | 32) == 'typeof x === "string" || typeof x === "number"'
    assert _print(258 | 128) == 'typeof x === "function" || typeof x === "object"'


def test_one_half_of_object_is_not_a_plain_typeof_test():
    assert _print(2) == "x === null"
    assert _print(256) == 'typeof x === "object" && x !== null'


@pytest.mark.parametrize("mask", [0, 512, 1 << 12])
def test_unknown_masks_stay_visibly_unresolved(mask):
    assert "<unresolved_typeof_mask_" in _print(mask)
