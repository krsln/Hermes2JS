from dataclasses import dataclass

from hermes_decompiler.ir.Values import Value
from hermes_decompiler.regions_new.models.Statements import Statement


@dataclass(frozen=True)
class IfStatement(Value):
    condition: Value
    target: int

    def render(self):
        return (
            f"if ({self.condition.render()}) "
            f"{{ /* jump to label_{self.target} */ }}"
        )


@dataclass(frozen=True)
class GotoStatement(Value):
    target: int

    def render(self):
        return f"goto label_{self.target};"


@dataclass(frozen=True)
class AssignmentStatement(Value):
    left: Value
    right: Value

    def render(self):
        return f"{self.left.render()} = {self.right.render()};"
