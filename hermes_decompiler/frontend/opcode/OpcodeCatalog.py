from __future__ import annotations

import json
from dataclasses import dataclass
from enum import Enum
from functools import lru_cache
from importlib import resources
from typing import Dict, FrozenSet, Tuple

# Highest bytecode version this catalog currently tracks. Update together
# with `data/opcode_version_map.json` (see `tools/update_opcode_catalog.py`
# for how that file is regenerated from the hermes-dec project).
CURRENT_VERSION = 99

# Oldest bytecode version this catalog currently tracks.
OLDEST_VERSION = 51


class OpcodeStatus(str, Enum):
    """Classification of an opcode name against the known bytecode history."""

    #: Present in the newest tracked bytecode version (CURRENT_VERSION).
    CURRENT = "current"
    #: Present in at least one older version, but not in CURRENT_VERSION -
    #: i.e. renamed, split (e.g. PutById -> PutByIdLoose/Strict) or removed.
    LEGACY = "legacy"
    #: Not present in ANY tracked version. Either a real opcode from a
    #: bytecode version we don't track yet, or a typo/incorrect name that
    #: needs to be verified against an actual `.hbc` dump.
    UNKNOWN = "unknown"


@dataclass(frozen=True, slots=True)
class OpcodeInfo:
    name: str
    status: OpcodeStatus
    versions: Tuple[int, ...]  # empty for UNKNOWN


@lru_cache(maxsize=1)
def _load_version_map() -> Dict[str, FrozenSet[int]]:
    """
    Load `data/opcode_version_map.json`: opcode name -> set of bytecode
    versions (from the hbc51..hbc99 definitions) it appears in.
    """
    raw = resources.files(__package__).joinpath("data/opcode_version_map.json").read_text()
    parsed = json.loads(raw)
    return {name: frozenset(versions) for name, versions in parsed.items()}


def classify(opcode_name: str) -> OpcodeInfo:
    """
    Classify a single opcode name (typically an `OpcodeHandler` subclass
    name, since dispatch resolves handlers by exact class name) against
    the known bytecode-version history.
    """
    versions = _load_version_map().get(opcode_name)

    if not versions:
        return OpcodeInfo(name=opcode_name, status=OpcodeStatus.UNKNOWN, versions=())

    status = OpcodeStatus.CURRENT if CURRENT_VERSION in versions else OpcodeStatus.LEGACY
    return OpcodeInfo(name=opcode_name, status=status, versions=tuple(sorted(versions)))


def classify_all(opcode_names) -> Dict[OpcodeStatus, list]:
    """
    Classify many opcode names at once, e.g. every key currently
    registered in `OpcodeHandler.registry`.

    Returns a dict keyed by OpcodeStatus, each value a list of OpcodeInfo,
    sorted by name, so callers/tests get stable, readable output.
    """
    buckets: Dict[OpcodeStatus, list] = {status: [] for status in OpcodeStatus}

    for name in opcode_names:
        info = classify(name)
        buckets[info.status].append(info)

    for infos in buckets.values():
        infos.sort(key=lambda i: i.name)

    return buckets
