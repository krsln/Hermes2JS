"""
Unit tests for `CFGBuilder._merge_fragmented_handlers`.

Hermes records one try body as SEVERAL exception-table entries whenever
the body's instruction stream is interrupted by something the handler
must not cover (a `Jmp` over a conditional throw, a generator/async
suspend point). `TryStructurer` must see those fragments as ONE handler,
otherwise it builds a second try/catch against a handler block the first
one already relocated (scrambled output).

The merge is grouped by TARGET and gated only by "is the gap clear of
every other handler's boundary" - never by position in the sorted table.
The tables below are real ones from `apps/demo/fixtures/{96,98}`; the
function they come from is named in each test.
"""

from __future__ import annotations

import copy
import itertools

import pytest

from hermes_decompiler.backend.analysis.cfg.CFGBuilder import CFGBuilder


def h(start: int, end: int, target: int) -> dict:
    return {"start": start, "end": end, "target": target}


def merge(*entries: dict) -> list[dict]:
    return CFGBuilder._merge_fragmented_handlers(list(entries))


def triples(handlers: list[dict]) -> list[tuple[int, int, int]]:
    return sorted((x["start"], x["end"], x["target"]) for x in handlers)


def test_empty_table():
    assert CFGBuilder._merge_fragmented_handlers([]) == []


def test_single_handler_untouched():
    assert triples(merge(h(0x16, 0x45, 0x45))) == [(0x16, 0x45, 0x45)]


def test_contiguous_fragments_merge():
    # hbc96 tryCatchInsideLoopTest: `Jmp` over a conditional throw.
    merged = merge(h(0x3A, 0x63, 0x85), h(0x65, 0x85, 0x85))
    assert triples(merged) == [(0x3A, 0x85, 0x85)]


def test_long_fragment_chain_collapses_to_one():
    # hbc98 asyncTryCatchTest: one fragment per await/suspend point.
    merged = merge(
        h(0x4B, 0xD3, 0x1B6),
        h(0xDF, 0x12B, 0x1B6),
        h(0x133, 0x18E, 0x1B6),
        h(0x19A, 0x1A1, 0x1B6),
        h(0x1AD, 0x1B6, 0x1B6),
    )
    assert triples(merged) == [(0x4B, 0x1B6, 0x1B6)]


def test_fragments_separated_by_a_wider_other_target_handler_still_merge():
    # hbc96 asyncTryCatchTest (section 15181). The finally-wrapper
    # [0x20, 0x76)->0xd0 sorts BETWEEN the two 0x8d fragments; an
    # adjacency-based merge never saw them as neighbours and left the
    # catch split in two, scrambling the whole function.
    merged = merge(
        h(0x20, 0x54, 0x8D),
        h(0x56, 0x76, 0x8D),
        h(0x20, 0x76, 0xD0),
        h(0x8D, 0xA3, 0xD0),
    )
    assert triples(merged) == [(0x20, 0x76, 0x8D), (0x20, 0xA3, 0xD0)]


# hbc96 parseBoxShadowString (#1133): a for-of whose body is full of
# `continue`s. BOTH the catch (0x1d2) and its finally-wrapper (0x217) are
# fragmented, and each one's fragment edges fall inside the other's gaps.
# A single merge pass sees the wrapper's edges as "foreign boundaries" in
# the catch's gaps and leaves six catch fragments unmerged (each one then
# silently skipped by `TryStructurer`); the merge has to iterate.
PARSE_BOX_SHADOW = [
    h(0xB5, 0xED, 0x1D2),
    h(0xF9, 0x113, 0x1D2),
    h(0x11F, 0x139, 0x1D2),
    h(0x145, 0x156, 0x1D2),
    h(0x162, 0x16B, 0x1D2),
    h(0x170, 0x18F, 0x1D2),
    h(0x1A0, 0x1C1, 0x1D2),
    h(0x77, 0xF0, 0x217),
    h(0xF9, 0x116, 0x217),
    h(0x11F, 0x13C, 0x217),
    h(0x145, 0x159, 0x217),
    h(0x162, 0x197, 0x217),
    h(0x1A0, 0x1C9, 0x217),
    h(0x1D2, 0x209, 0x217),
]


def test_fragmented_catch_inside_fragmented_finally_wrapper():
    merged = merge(*PARSE_BOX_SHADOW)
    assert triples(merged) == [(0x77, 0x209, 0x217), (0xB5, 0x1C1, 0x1D2)]


def test_nested_try_catch_finally_table_from_15082():
    merged = merge(
        h(0x16, 0x4A, 0x4A),
        h(0x16, 0x60, 0x8A),
        h(0x16, 0x88, 0xA2),
        h(0x8A, 0xA2, 0xA2),
        h(0x16, 0xB8, 0xE4),
    )
    assert triples(merged) == [
        (0x16, 0x4A, 0x4A),
        (0x16, 0x60, 0x8A),
        (0x16, 0xA2, 0xA2),
        (0x16, 0xB8, 0xE4),
    ]


def test_shadowed_duplicate_range_is_folded_into_neighbour():
    # hbc96 tryCatchFinallyImplicitThrowTest: same range, different
    # targets, then a same-target continuation past a clear gap.
    merged = merge(h(0x19, 0x3F, 0x55), h(0x19, 0x3F, 0x87), h(0x55, 0x6B, 0x87))
    assert triples(merged) == [(0x19, 0x3F, 0x55), (0x19, 0x6B, 0x87)]


def test_gap_with_foreign_boundary_is_not_merged():
    # hbc98 nestedArrayDestructureTest: nested handlers sit INSIDE the
    # gap between the two 0x20a fragments; they are two distinct
    # protected regions that merely share a handler.
    table = [
        h(0x62, 0xA8, 0x215),
        h(0xDD, 0x11B, 0x20A),
        h(0x15B, 0x15D, 0x1F6),
        h(0x18F, 0x196, 0x196),
        h(0x1BD, 0x1C1, 0x1C7),
        h(0x203, 0x20A, 0x20A),
    ]
    assert triples(merge(*table)) == triples(table)


def test_other_target_handler_ending_inside_gap_blocks_merge():
    merged = merge(h(0, 10, 100), h(0, 12, 200), h(20, 30, 100))
    assert triples(merged) == [(0, 10, 100), (0, 12, 200), (20, 30, 100)]


def test_other_target_handler_exactly_filling_the_gap_blocks_merge():
    # Both of its boundaries lie ON the gap's edges, so a plain
    # "boundary strictly inside" test cannot see it.
    merged = merge(h(0, 10, 100), h(10, 20, 200), h(20, 30, 100))
    assert triples(merged) == [(0, 10, 100), (10, 20, 200), (20, 30, 100)]


def test_different_targets_never_merge_even_when_adjacent():
    merged = merge(h(0, 10, 100), h(10, 20, 200))
    assert triples(merged) == [(0, 10, 100), (10, 20, 200)]


def test_overlapping_same_target_ranges_union():
    merged = merge(h(0, 10, 100), h(5, 20, 100))
    assert triples(merged) == [(0, 20, 100)]


def test_input_is_not_mutated():
    table = [h(0x20, 0x54, 0x8D), h(0x56, 0x76, 0x8D), h(0x20, 0x76, 0xD0)]
    snapshot = copy.deepcopy(table)
    CFGBuilder._merge_fragmented_handlers(table)
    assert table == snapshot


@pytest.mark.parametrize(
    "table",
    [
        [h(0x20, 0x54, 0x8D), h(0x56, 0x76, 0x8D), h(0x20, 0x76, 0xD0), h(0x8D, 0xA3, 0xD0)],
        [h(0x16, 0x4A, 0x4A), h(0x16, 0x60, 0x8A), h(0x16, 0x88, 0xA2), h(0x8A, 0xA2, 0xA2), h(0x16, 0xB8, 0xE4)],
    ],
    ids=["asyncTryCatch-15181", "nestedTryCatchFinally-15082"],
)
def test_result_is_independent_of_input_order(table):
    expected = triples(CFGBuilder._merge_fragmented_handlers(list(table)))

    for perm in itertools.permutations(table):
        assert triples(CFGBuilder._merge_fragmented_handlers(list(perm))) == expected


def test_large_table_is_independent_of_input_order():
    # Too big to permute exhaustively; a fixed set of shuffles is enough.
    import random

    expected = triples(CFGBuilder._merge_fragmented_handlers(list(PARSE_BOX_SHADOW)))
    rng = random.Random(1133)

    for _ in range(50):
        shuffled = list(PARSE_BOX_SHADOW)
        rng.shuffle(shuffled)
        assert triples(CFGBuilder._merge_fragmented_handlers(shuffled)) == expected


def test_identical_ranges_keep_table_order():
    # Hermes matches entries in listed order, so of two identical ranges
    # the first-listed is the one that ever fires. TryStructurer's dedup
    # keeps the first it sees - the merge must not reorder them.
    merged = merge(h(0, 10, 200), h(0, 10, 100))
    assert [(x["start"], x["end"], x["target"]) for x in merged] == [(0, 10, 200), (0, 10, 100)]

    merged = merge(h(0, 10, 100), h(0, 10, 200))
    assert [(x["start"], x["end"], x["target"]) for x in merged] == [(0, 10, 100), (0, 10, 200)]


@pytest.mark.parametrize(
    "table",
    [
        PARSE_BOX_SHADOW,
        [h(0x20, 0x54, 0x8D), h(0x56, 0x76, 0x8D), h(0x20, 0x76, 0xD0), h(0x8D, 0xA3, 0xD0)],
        [h(0x62, 0xA8, 0x215), h(0xDD, 0x11B, 0x20A), h(0x15B, 0x15D, 0x1F6),
         h(0x18F, 0x196, 0x196), h(0x1BD, 0x1C1, 0x1C7), h(0x203, 0x20A, 0x20A)],
    ],
    ids=["parseBoxShadow-1133", "asyncTryCatch-15181", "nestedArrayDestructure-9487"],
)
def test_merge_never_loses_protection_and_never_grows_the_table(table):
    merged = CFGBuilder._merge_fragmented_handlers(list(table))

    assert len(merged) <= len(table)

    # Every original range is still covered by a merged range that has
    # the same target: merging may only widen protection, never drop it.
    for raw in table:
        assert any(
            m["target"] == raw["target"] and m["start"] <= raw["start"] and m["end"] >= raw["end"]
            for m in merged
        ), raw

    # Idempotent: merging an already-merged table changes nothing.
    assert triples(CFGBuilder._merge_fragmented_handlers(merged)) == triples(merged)
