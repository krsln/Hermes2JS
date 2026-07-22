from dataclasses import dataclass, field
from typing import List, Optional

class ASTNode:
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
    then_branch: BlockNode
    else_branch: Optional[BlockNode] = None

@dataclass
class ForInNode(ASTNode):
    var_name: str
    object_name: str
    body: BlockNode

@dataclass
class ForOfNode(ASTNode):
    var_name: str
    iterable_name: str
    body: BlockNode