from dataclasses import dataclass

from hermes_decompiler.frontend.parsing.ClassEnvironmentTable import ClassEnvironmentTable
from hermes_decompiler.frontend.parsing.CreatorTable import CreatorTable
from hermes_decompiler.frontend.parsing.EnvironmentOriginTable import EnvironmentOriginTable
from hermes_decompiler.frontend.parsing.PrivateNameTable import PrivateNameTable


@dataclass(frozen=True)
class BatchTables:
    """
    Every batch-resolved (cross-section) table in one immutable bundle -
    what BatchPipeline.run() produces, and the ONE parameter
    Decompiler.build_context()/FileOperations.process_section() take for
    all of them, instead of a separate keyword per table. Adding a new
    table (its own BatchStage feeding a new field here) never grows that
    parameter list - see FileOperations.build_batch_tables for where the
    stage list actually lives.

    Every field is a real (never None) table - each table class's own
    `.empty()` stands in for "nothing to look up" (an unresolved lookup
    on an empty table behaves identically to one against a populated
    table that simply doesn't mention that function/slot), so callers
    downstream never need a `is not None` check before using one, only
    before using `PipelineContext.batch_tables` itself (still optional -
    a lone section decompiled with no batch at all).
    """

    creator_table: CreatorTable
    environment_origin_table: EnvironmentOriginTable
    private_name_table: PrivateNameTable
    class_environment_table: ClassEnvironmentTable

    @classmethod
    def empty(cls) -> "BatchTables":
        return cls(
            creator_table=CreatorTable.empty(),
            environment_origin_table=EnvironmentOriginTable.empty(),
            private_name_table=PrivateNameTable.empty(),
            class_environment_table=ClassEnvironmentTable.empty(),
        )
