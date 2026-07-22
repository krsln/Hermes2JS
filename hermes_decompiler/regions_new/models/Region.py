from __future__ import annotations

from abc import ABC


class Region(ABC):

    def __init__(self):

        self.parent: "Region | None" = None