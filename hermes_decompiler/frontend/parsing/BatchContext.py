from dataclasses import dataclass, field

from hermes_decompiler.frontend.parsing.ClassEnvironmentTable import ClassEnvironmentTable
from hermes_decompiler.frontend.parsing.CreatorTable import CreatorTable
from hermes_decompiler.frontend.parsing.EnvironmentOriginTable import EnvironmentOriginTable
from hermes_decompiler.frontend.parsing.PrivateNameTable import PrivateNameTable


@dataclass
class BatchContext:
    """
    Threaded through a BatchPipeline the same way PipelineContext is
    threaded through a Pipeline - each BatchStage reads/writes a slice of
    this and hands it to the next. `sections` is the one thing every
    stage shares as input (every section's own (function_id, raw .hasm
    text) pair, read once up front); each table field below starts out
    unset and is filled in by its own stage.

    Split into this mutable, in-progress shape and the frozen BatchTables
    a completed run produces (see `to_batch_tables()`) for the same
    reason PipelineContext and its eventual `.js_lines` output aren't the
    same object: downstream code (Decompiler.build_context, opcode
    handlers) should see a fixed, complete set of tables, not one a
    stage might still be partway through populating.
    """

    sections: list[tuple[int, str]]

    creator_table: CreatorTable | None = None
    environment_origin_table: EnvironmentOriginTable | None = None
    private_name_table: PrivateNameTable | None = None
    class_environment_table: ClassEnvironmentTable | None = None

    def to_batch_tables(self) -> "BatchTables":
        from hermes_decompiler.frontend.parsing.BatchTables import BatchTables

        return BatchTables(
            creator_table=self.creator_table or CreatorTable.empty(),
            environment_origin_table=self.environment_origin_table or EnvironmentOriginTable.empty(),
            private_name_table=self.private_name_table or PrivateNameTable.empty(),
            class_environment_table=self.class_environment_table or ClassEnvironmentTable.empty(),
        )
