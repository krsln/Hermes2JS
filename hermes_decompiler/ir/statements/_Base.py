from __future__ import annotations

from abc import ABC
from dataclasses import dataclass

from hermes_decompiler.ir.Node import Node

__all__ = [
    "Statement",
]


@dataclass(frozen=True, slots=True, eq=False)
class Statement(Node, ABC):
    """
    Abstract base class for every JavaScript statement.

    A statement performs an action or controls program flow; unlike an
    `Expression`, it does not itself produce a value.
    """