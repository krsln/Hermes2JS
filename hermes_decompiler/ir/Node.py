from __future__ import annotations

from abc import ABC, abstractmethod

from abc import ABC
from dataclasses import fields, is_dataclass, dataclass


# @dataclass(frozen=True, slots=True)
# class Node(ABC):
#     pass



#                 Node
#               /      \
#          Statement   Value
#                       |
#                  Expression
#                       |
#          -------------------------
#          |           |          |
#      Binary      Call       Identifier

#                 Node
#                /    \
#               /      \
#      Statement      Expression
