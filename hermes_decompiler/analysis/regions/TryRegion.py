from dataclasses import dataclass
from typing import Optional

from hermes_decompiler.analysis.Region import Region


@dataclass(slots=True)
class TryRegion(Region):
    """
    Try-catch-finally region from exception metadata.
    """

    try_region: Region
    catch_region: Optional[Region] = None
    finally_region: Optional[Region] = None
    exception_var: str | None = None

    def accept(self, visitor):
        return visitor.visit_try(self)