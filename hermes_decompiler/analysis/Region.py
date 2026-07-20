from __future__ import annotations

from abc import ABC, abstractmethod


class Region(ABC):
    """
    Base class for every structured control-flow region.
    """

    @abstractmethod
    def accept(self, visitor):
        """
        Accept a RegionVisitor.
        """
        raise NotImplementedError