from typing import List, Set, Any

from hermes_decompiler.new.ASTNode import ASTNode, BlockNode, InstructionNode, IfNode
from hermes_decompiler.new.cfg_models import BasicBlock


class ControlFlowStructuring:
    def __init__(self, blocks: List[BasicBlock], results: List[Any]):
        self.blocks = blocks
        self.results = results
        self.addr_to_result = {r.variable.address: r for r in results}

    def structure_cfg(self) -> ASTNode:
        root_block = BlockNode()
        i = 0
        n = len(self.results)

        while i < n:
            item = self.results[i]
            var = item.variable
            val_raw = var.value.strip() if var.value else ""

            # Handler filtreleri
            if var.handler == "CompleteGenerator":
                i += 1
                continue

            # Return Komutu
            if var.handler == "Ret":
                value = val_raw.split("return ")[1].strip() if "return " in val_raw else val_raw
                root_block.body.append(InstructionNode(
                    statement=f"return {value};",
                    original_bytecode=item.opcode.bytecode,
                    used=var.used
                ))
                i += 1
                continue

            # Jmp / JmpLong (Koşulsuz Atlama / Loop Back)
            if var.handler in ("Jmp", "JmpLong") and item.goto is not None:
                root_block.body.append(InstructionNode(
                    statement=f"goto label_{item.goto};",
                    original_bytecode=item.opcode.bytecode,
                    used=var.used
                ))
                i += 1
                continue

            # Koşullu Atlama (If/Else Yapısı)
            if "/* jump to" in val_raw and item.goto is not None:
                condition = self._extract_condition(val_raw)
                then_body = BlockNode()

                # Atlama hedefine (goto) kadar olan talimatları 'then' bloğuna topla
                target_addr = item.goto
                i += 1  # 'if' satırını geç

                while i < n and self.results[i].variable.address < target_addr:
                    inner_item = self.results[i]
                    inner_var = inner_item.variable
                    inner_raw = inner_var.value.strip() if inner_var.value else ""

                    stmt_text = inner_item.result if inner_item.result else inner_raw
                    then_body.body.append(InstructionNode(
                        statement=stmt_text,
                        original_bytecode=inner_item.opcode.bytecode,
                        used=inner_var.used
                    ))
                    i += 1

                # Oluşturulan dolu 'then' bloğunu IfNode olarak ekle
                root_block.body.append(IfNode(
                    condition=condition,
                    then_branch=then_body,
                    else_branch=None
                ))
                continue

            # Normal Talimatlar (Assignments, Calls vb.)
            stmt_text = item.result if item.result else val_raw
            root_block.body.append(InstructionNode(
                statement=stmt_text,
                original_bytecode=item.opcode.bytecode,
                used=var.used
            ))
            i += 1

        return root_block

    @staticmethod
    def _extract_condition(raw: str) -> str:
        try:
            return raw.split("if (")[1].split(")")[0].strip()
        except IndexError:
            return raw
