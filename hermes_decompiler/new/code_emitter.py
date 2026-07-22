from typing import List

from hermes_decompiler.new.ast_nodes import ASTNode, BlockNode, InstructionNode, IfNode, ForOfNode, ForInNode


class HighLevelCodeEmitter:
    def __init__(self, verbose: bool = True, indent_step: int = 4):
        self.verbose = verbose
        self.indent_step = indent_step

    def emit(self, ast: ASTNode) -> List[str]:
        lines: List[str] = []
        self._visit(ast, level=1, lines=lines)
        return lines

    def _visit(self, node: ASTNode, level: int, lines: List[str]):
        indent = " " * (level * self.indent_step)

        if isinstance(node, BlockNode):
            for stmt in node.body:
                self._visit(stmt, level, lines)

        elif isinstance(node, InstructionNode):
            if self.verbose and node.original_bytecode:
                bytecode_clean = (
                    node.original_bytecode.split(":", 1)[1].strip()
                    if ":" in node.original_bytecode
                    else node.original_bytecode.strip()
                )
                lines.append(f"{indent}// CODE → {bytecode_clean}")

            if node.used:
                if self.verbose and node.statement:
                    lines.append(f"{indent}// USED → {node.statement}")
            else:
                if node.statement:
                    lines.append(f"{indent}{node.statement}")

        elif isinstance(node, ForInNode):
            lines.append(f"{indent}for (const {node.var_name} in {node.object_name}) {{")
            self._visit(node.body, level + 1, lines)
            lines.append(f"{indent}}}")

        elif isinstance(node, ForOfNode):
            lines.append(f"{indent}for (const {node.var_name} of {node.iterable_name}) {{")
            self._visit(node.body, level + 1, lines)
            lines.append(f"{indent}}}")

        elif isinstance(node, IfNode):
            lines.append(f"{indent}if ({node.condition}) {{")
            self._visit(node.then_branch, level + 1, lines)
            if node.else_branch:
                lines.append(f"{indent}}} else {{")
                self._visit(node.else_branch, level + 1, lines)
            lines.append(f"{indent}}}")
