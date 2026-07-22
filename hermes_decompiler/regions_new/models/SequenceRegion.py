from __future__ import annotations

from .Region import Region


class SequenceRegion(Region):

    def __init__(self):
        super().__init__()

        self.children: list[Region] = []