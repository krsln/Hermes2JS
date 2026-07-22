from dataclasses import dataclass, field
from typing import List, Dict, Set, Optional, Any


class ASTNode:
    """Temel AST Düğümü"""
    pass


@dataclass
class InstructionNode(ASTNode):
    statement: str
    original_bytecode: str
    used: bool


@dataclass
class BlockNode(ASTNode):
    body: List[ASTNode] = field(default_factory=list)


@dataclass
class IfNode(ASTNode):
    condition: str
    then_branch: ASTNode
    else_branch: Optional[ASTNode] = None


@dataclass
class LoopNode(ASTNode):
    condition: Optional[str]  # While(cond) veya While(true)
    body: ASTNode


@dataclass
class LabelNode(ASTNode):
    label_name: str


@dataclass
class BreakNode(ASTNode):
    pass
