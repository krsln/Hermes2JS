from typing import List, Set

from hermes_decompiler.new.ASTNode import ASTNode, BlockNode, InstructionNode, IfNode
from hermes_decompiler.new.cfg_models import BasicBlock


class ControlFlowStructuring:
    def __init__(self, blocks: List[BasicBlock]):
        self.blocks = blocks
        self.visited_blocks: Set[int] = set()

    def structure_cfg(self) -> ASTNode:
        root_block = BlockNode()
        for block in self.blocks:
            if block.id in self.visited_blocks:
                continue

            node = self._structure_block(block)
            root_block.body.append(node)

        return root_block

    def _structure_block(self, block: BasicBlock) -> ASTNode:
        self.visited_blocks.add(block.id)
        block_ast = BlockNode()

        # Blok içindeki normal talimatları ekle
        for item in block.results:
            var = item.variable
            val_raw = var.value.strip()

            # Koşullu Atlama Kontrolü (If Structure)
            if "/* jump to" in val_raw and item.goto is not None:
                condition = self._extract_condition(val_raw)

                # Successor'lardan jump hedefini bul
                then_body = BlockNode()
                else_body = None

                # Simplified block structuring for jump condition
                if_node = IfNode(
                    condition=condition,
                    then_branch=then_body,
                    else_branch=else_body
                )
                block_ast.body.append(if_node)
            elif var.handler == "Ret":
                value = val_raw.split("return ")[1].strip() if "return " in val_raw else val_raw
                block_ast.body.append(InstructionNode(
                    statement=f"return {value}",
                    original_bytecode=item.opcode.bytecode,
                    used=var.used
                ))
            else:
                block_ast.body.append(InstructionNode(
                    statement=item.result,
                    original_bytecode=item.opcode.bytecode,
                    used=var.used
                ))

        return block_ast

    @staticmethod
    def _extract_condition(raw: str) -> str:
        try:
            return raw.split("if (")[1].split(")")[0].strip()
        except IndexError:
            return raw
