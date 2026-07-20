from __future__ import annotations

from abc import ABC, abstractmethod


class RegionVisitor(ABC):

    @abstractmethod
    def visit_sequence(self, region):
        raise NotImplementedError

    @abstractmethod
    def visit_if(self, region):
        raise NotImplementedError

    @abstractmethod
    def visit_loop(self, region):
        raise NotImplementedError

    @abstractmethod
    def visit_try(self, region):
        raise NotImplementedError
