from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(slots=True)
class Loop:

    header: int

    latch: int

    body: set[int] = field(default_factory=set)