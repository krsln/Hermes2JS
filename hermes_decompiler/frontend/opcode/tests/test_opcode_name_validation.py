"""
Validate that every registered OpcodeHandler corresponds to a real Hermes
bytecode opcode.

Dispatch is performed by matching OpcodeEntry.opcode directly to the
OpcodeHandler subclass name. A typo in a handler class name therefore
creates silently unreachable code, while a missing handler represents an
unnoticed coverage gap.

The opcode catalog is generated from the hermes-dec project and contains
the union of all tracked Hermes bytecode versions (currently hbc51-hbc99).

Handlers are classified as:

    CURRENT  - present in the newest tracked bytecode version.
    LEGACY   - present only in older tracked versions.
    UNKNOWN  - not found in any tracked version.

UNKNOWN handlers fail the test unless explicitly allow-listed.
"""

from __future__ import annotations

import pytest

from hermes_decompiler.analysis.cfg import BasicBlock
from hermes_decompiler.handlers import HandlerLoader, OpcodeHandler
from hermes_decompiler.frontend.opcode import OpcodeStatus, classify_all

# Helper/mixin classes that intentionally do not correspond to Hermes
# bytecode opcodes.
#
# They provide shared OpcodeHandler functionality (operand parsing,
# helper methods, etc.) and must never appear in the handler registry.
# Most are excluded automatically via `_abstract = True`; this allow-list
# serves as a defensive safeguard in case one is accidentally registered.
NON_OPCODE_HELPER_CLASSES = {"OpcodeHandler"}

# Handler names that are intentionally exempt from validation until they
# have been verified against the tracked Hermes opcode catalog
# (currently hbc51-hbc99).
#
# Every entry must include a justification (Hermes version, upstream
# source, or another authoritative reference). This prevents temporary
# assumptions from silently becoming permanent exceptions.
#
# This allow-list should normally remain empty.
KNOWN_UNVERIFIED: dict[str, str] = {
    # "BitOrN": "TODO: Add the Hermes version and authoritative source.",
}

# Lower bound used to detect accidental registry shrinkage.
# Update intentionally whenever handlers are added, removed, or consolidated.
MIN_EXPECTED_HANDLER_COUNT = 200


@pytest.fixture(scope="module", autouse=True)
def initialize_handler_registry():
    """Populate OpcodeHandler.registry before any validation runs."""

    HandlerLoader.load()


@pytest.fixture(scope="module")
def registered_handler_names() -> list[str]:
    """Return the names of all registered concrete opcode handlers."""

    return [
        name for name in OpcodeHandler.registry
        if name not in NON_OPCODE_HELPER_CLASSES
    ]


def test_every_handler_name_is_a_known_opcode(registered_handler_names):
    buckets = classify_all(registered_handler_names)

    unknown = [
        info for info in buckets[OpcodeStatus.UNKNOWN]
        if info.name not in KNOWN_UNVERIFIED
    ]

    if unknown:
        details = "\n".join(
            f"  - {info.name}"
            for info in sorted(unknown, key=lambda x: x.name)
        )

        pytest.fail(
            "The following handler class names do not exist in any tracked "
            "Hermes bytecode version (hbc51-hbc99).\n\n"
            "Either:\n"
            "  1. the handler name contains a typo, or\n"
            "  2. the opcode belongs to a newer Hermes bytecode version that "
            "is not yet tracked.\n\n"
            "Verify the opcode against a trusted external source before "
            "merging.\n\n"
            f"{details}"
        )


def test_legacy_opcodes_are_visible_and_documented(registered_handler_names):
    """
    Informational test.

    Reports handlers that exist only in older Hermes bytecode versions.

    Legacy handlers are expected and therefore do not cause the test to fail.
    The goal is to make version-specific opcode coverage visible in CI output
    instead of leaving that information buried in source comments.
    """

    buckets = classify_all(registered_handler_names)
    legacy = sorted(
        buckets[OpcodeStatus.LEGACY],
        key=lambda item: item.name,
    )

    print(f"\n{len(legacy)} legacy handler(s) detected (not present in hbc99):")
    for info in legacy:
        v_min, v_max = info.versions[0], info.versions[-1]
        print(f"  - {info.name}: hbc{v_min}..hbc{v_max}")

    # assert True


def test_known_unverified_list_is_empty():
    """
    Enforces that KNOWN_UNVERIFIED remains empty.

    The project policy is to verify every handler against an authoritative
    Hermes opcode source before it is merged. Allowing unverified entries to
    accumulate would weaken the guarantees provided by the validation tests.
    """

    assert not KNOWN_UNVERIFIED, (
        f"KNOWN_UNVERIFIED contains {len(KNOWN_UNVERIFIED)} unverified "
        f"handler name(s): {sorted(KNOWN_UNVERIFIED)}. "
        "Verify each entry against an authoritative Hermes opcode source "
        "and remove it from the allow-list, or remove the handler if the "
        "opcode cannot be confirmed."
    )


def test_no_duplicate_registration_shadowing():
    """
    Detect accidental handler registration shadowing.

    OpcodeHandler.registry is keyed by class name. If two handler classes are
    defined with the same name, the later registration silently overwrites
    the previous one.

    Because HandlerLoader imports every handler module, such collisions may
    go unnoticed unless explicitly checked. This test provides a simple
    sanity check by ensuring the registry size does not unexpectedly shrink,
    which could indicate a duplicate registration or an unintentionally
    missing handler.
    """

    assert len(OpcodeHandler.registry) >= MIN_EXPECTED_HANDLER_COUNT


def test_basic_block_equality_is_id_based_not_identity_based():
    a = BasicBlock(block_id=3, address=100)
    b = BasicBlock(block_id=3, address=100)  # farklı nesne, aynı id

    assert a == b
    assert hash(a) == hash(b)
