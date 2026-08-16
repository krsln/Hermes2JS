from __future__ import annotations

from typing import Any

from hermes_decompiler.ir.Node import Node

__all__ = [
    "NodeVisitor",
]


class NodeVisitor:
    """
    Read-only traversal of an IR tree.

    Mirrors `ast.NodeVisitor`: define `visit_<ClassName>` to handle a
    specific node type, or rely on `generic_visit` to recurse into
    children unchanged.

    Example:

        class NameCollector(NodeVisitor):
            def __init__(self):
                self.names: list[str] = []

    # noinspection GrazieInspection
            def visit_Identifier(self, node: Identifier) -> None:
                self.names.append(node.name)
                self.generic_visit(node)
    """

    def visit(self, node: Node) -> Any:
        method_name = f"visit_{type(node).__name__}"

        if hasattr(self, method_name):
            method = getattr(self, method_name)
            return method(node)

        return self.generic_visit(node)

    def generic_visit(self, node: Node) -> None:
        for child in node.children:
            self.visit(child)

# class NodeTransformer(NodeVisitor):
#     """
#     Tree-to-tree rewriting of an IR tree.
#
#     `visit_<ClassName>` methods may return a new node, `None` (to drop
#     the node, only meaningful within tuple fields), or the original node
#     unchanged. Since nodes are frozen, new instances are produced via
#     `dataclasses.replace` rather than mutation.
#
#     Example:
#         class ConstantFolder(NodeTransformer):
#             def visit_BinaryExpression(self, node: BinaryExpression):
#                 node = self.generic_visit(node)
#                 # ... fold constants, return new node ...
#                 return node
#     """
#
#     def generic_visit(self, node: Node) -> Node:
#         replacements: dict[str, Any] = {}
#
#         for f in dataclasses.fields(node):
#             if f.name == "loc":
#                 continue
#
#             value = getattr(node, f.name)
#
#             if isinstance(value, Node):
#                 new_value = self.visit(value)
#                 if new_value is not value:
#                     replacements[f.name] = new_value
#
#             elif isinstance(value, tuple):
#                 new_items = []
#                 changed = False
#
#                 for item in value:
#                     if isinstance(item, Node):
#                         new_item = self.visit(item)
#                         if new_item is None:
#                             changed = True
#                             continue
#                         if new_item is not item:
#                             changed = True
#                         new_items.append(new_item)
#                     else:
#                         new_items.append(item)
#
#                 if changed:
#                     replacements[f.name] = tuple(new_items)
#
#         if not replacements:
#             return node
#
#         return dataclasses.replace(node, **replacements)
