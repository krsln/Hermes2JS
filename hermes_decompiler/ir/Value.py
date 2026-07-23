from __future__ import annotations

from abc import ABC, abstractmethod


class Value(ABC):

    @abstractmethod
    def render(self) -> str:
        raise NotImplementedError()