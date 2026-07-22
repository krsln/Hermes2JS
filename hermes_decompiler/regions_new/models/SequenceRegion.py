from __future__ import annotations

from typing import List

from .Region import Region


class SequenceRegion(Region):
    """
    Linear sequence of child regions.
    """

    def __init__(self):
        self.children: List[Region] = []