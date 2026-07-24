from __future__ import annotations

from dataclasses import dataclass

from ..expressions import Expression
from ..Node import Node
from ._Base import Statement

__all__ = [
    "ThrowStatement",
    "TryStatement",
    "CatchClause",
    "FinallyClause",
]


# ============================================================================
# Throw
# ============================================================================


@dataclass(frozen=True, slots=True)
class ThrowStatement(Statement):
    """
    Represents a throw statement.

    Example:

        throw error;
    """

    argument: Expression

    @property
    def children(self) -> tuple[Node, ...]:
        return (
            self.argument,
        )


# ============================================================================
# Catch Clause
# ============================================================================


@dataclass(frozen=True, slots=True)
class CatchClause(Node):
    """
    Represents a catch clause.

    Examples:

        catch (error) {
            ...
        }

        catch {
            ...
        }

    The parameter is optional because modern JavaScript
    supports optional catch binding.
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


# ============================================================================
# Finally
# ============================================================================


@dataclass(frozen=True, slots=True)
class FinallyClause(Node):
    """
    Represents a finally block.

    Example:

        finally {
            cleanup();
        }
    """

    body: Statement

    @property
    def children(self) -> tuple[Node, ...]:
        return (
            self.body,
        )


# ============================================================================
# Try
# ============================================================================


@dataclass(frozen=True, slots=True)
class TryStatement(Statement):
    """
    Represents try/catch/finally.

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


        try {
            foo();
        }
        catch(e) {
            handle(e);
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
        children: list[Node] = [
            self.body,
        ]

        if self.handler is not None:
            children.append(self.handler)

        if self.finalizer is not None:
            children.append(self.finalizer)

        return tuple(children)
