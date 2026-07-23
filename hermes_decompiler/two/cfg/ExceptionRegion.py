from __future__ import annotations

from dataclasses import dataclass


@dataclass(slots=True)
class ExceptionRegion:
    """
    Represents one exception handler region extracted from Hermes metadata.
    """

    start: int

    end: int

    handler: int