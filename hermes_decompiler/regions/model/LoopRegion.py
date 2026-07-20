from dataclasses import dataclass
from enum import Enum, auto

from hermes_decompiler.regions.model.Region import Region


class LoopKind(Enum):
    WHILE = auto()      # condition checked before the body runs
    DO_WHILE = auto()   # condition checked after the body runs
    INFINITE = auto()   # no single reconstructible exit test was found;
                         # emitted as `while (true)` with explicit
                         # break/goto markers inside the body instead


@dataclass(slots=True)
class LoopRegion(Region):

    kind: LoopKind
    condition: str | None
    body: Region

    def accept(self, visitor):
        return visitor.visit_loop(self)
