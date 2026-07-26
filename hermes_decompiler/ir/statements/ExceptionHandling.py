from __future__ import annotations

from dataclasses import dataclass

from hermes_decompiler.ir.Node import Node
from hermes_decompiler.ir.expressions import Expression
from ._Base import Statement

__all__ = [
    "ThrowStatement",
    "CatchClause",
    "FinallyClause",
    "TryStatement",
]


@dataclass(frozen=True, slots=True, eq=False)
class ThrowStatement(Statement):
    """
    Throw statement.

    Example:
        throw error;
    """

    argument: Expression

    @property
    def children(self) -> tuple[Node, ...]:
        return (self.argument,)


@dataclass(frozen=True, slots=True, eq=False)
class CatchClause(Node):
    """
    Catch clause. The parameter is optional to support the modern
    optional-catch-binding syntax.

    Examples:
        catch (error) {
            ...
        }

        catch {
            ...
        }
    """

    parameter: Expression | None
    body: Statement

    @property
    def children(self) -> tuple[Node, ...]:
        children: list[Node] = []

        if self.parameter is not None:
            children.append(self.parameter)

        children.append(self.body)

        return tuple(children)


@dataclass(frozen=True, slots=True, eq=False)
class FinallyClause(Node):
    """
    Finally clause.

    Example:
        finally {
            cleanup();
        }
    """

    body: Statement

    @property
    def children(self) -> tuple[Node, ...]:
        return (self.body,)


@dataclass(frozen=True, slots=True, eq=False)
class TryStatement(Statement):
    """
    Try/catch/finally statement.

    Examples:
        try {
            foo();
        }
        catch (e) {
            handle(e);
        }

        try {
            foo();
        }
        finally {
            cleanup();
        }
    """

    body: Statement
    handler: CatchClause | None = None
    finalizer: FinallyClause | None = None

    @property
    def children(self) -> tuple[Node, ...]:
        children: list[Node] = [self.body]

        if self.handler is not None:
            children.append(self.handler)

        if self.finalizer is not None:
            children.append(self.finalizer)

        return tuple(children)