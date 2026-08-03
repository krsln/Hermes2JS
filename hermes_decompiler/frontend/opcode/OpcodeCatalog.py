from __future__ import annotations

import json
from collections.abc import Iterable
from dataclasses import dataclass
from enum import Enum
from functools import lru_cache
from importlib import resources
from typing import Dict, FrozenSet

# Highest bytecode version this catalog currently tracks. Update together
# with `data/opcode_version_map.json` (see `tools/update_opcode_catalog.py`
# for how that file is regenerated from the hermes-dec project).
CURRENT_VERSION = 99


class OpcodeStatus(str, Enum):
    """Classification of an opcode name against the known bytecode history."""

    #: Present in the newest tracked bytecode version (CURRENT_VERSION).
    CURRENT = "current"

    #: Present in at least one older version, but not in CURRENT_VERSION,
    #: meaning the opcode was renamed, split, or removed.
    LEGACY = "legacy"

    #: Not present in any tracked bytecode version. This is either an opcode
    #: from an unsupported Hermes version or an unknown/incorrect opcode name.
    UNKNOWN = "unknown"


@dataclass(frozen=True, slots=True)
class OpcodeInfo:
    """Classification result for a single opcode."""

    name: str
    status: OpcodeStatus
    versions: tuple[int, ...]  # Empty for UNKNOWN.


@lru_cache(maxsize=1)
def _load_version_map() -> Dict[str, FrozenSet[int]]:
    """
    Load ``data/opcode_version_map.json``.

    Returns:
        Mapping of opcode name -> bytecode versions in which it exists.
    """
    raw = (
        resources.files(__package__)
        .joinpath("data/opcode_version_map.json")
        .read_text(encoding="utf-8")
    )

    parsed = json.loads(raw)
    return {
        name: frozenset(versions)
        for name, versions in parsed.items()
    }


def classify(opcode_name: str) -> OpcodeInfo:
    """
    Classify a single opcode name against the known Hermes bytecode history.
    """
    versions = _load_version_map().get(opcode_name)

    if versions is None:
        return OpcodeInfo(
            name=opcode_name,
            status=OpcodeStatus.UNKNOWN,
            versions=(),
        )

    return OpcodeInfo(
        name=opcode_name,
        status=(
            OpcodeStatus.CURRENT
            if CURRENT_VERSION in versions
            else OpcodeStatus.LEGACY
        ),
        versions=tuple(sorted(versions)),
    )


def classify_all(
        opcode_names: Iterable[str],
) -> Dict[OpcodeStatus, list[OpcodeInfo]]:
    """
    Classify multiple opcode names.

    Returns:
        A mapping from OpcodeStatus to a sorted list of OpcodeInfo objects.
    """
    buckets: Dict[OpcodeStatus, list[OpcodeInfo]] = {
        status: [] for status in OpcodeStatus
    }

    for name in opcode_names:
        info = classify(name)
        buckets[info.status].append(info)

    for infos in buckets.values():
        infos.sort(key=lambda item: item.name)

    return buckets
