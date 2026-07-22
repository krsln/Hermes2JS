from typing import List, Any
from hermes_decompiler.new.ast_nodes import BlockNode, InstructionNode, ForInNode, ForOfNode, IfNode


class HighLevelASTBuilder:
    def __init__(self, results: List[Any]):
        self.results = results
        self.n = len(results)

    def build(self) -> BlockNode:
        root = BlockNode()
        i = 0

        while i < self.n:
            item = self.results[i]
            var = item.variable
            val_raw = var.value.strip() if var.value else ""
            handler = var.handler

            # 1. For-In
            if handler == "GetPNameList" or ("Object.keys(" in val_raw and "for-in property list" in val_raw):
                for_in_node, new_idx = self._parse_for_in(i)
                if for_in_node:
                    root.body.append(for_in_node)
                    i = new_idx
                    continue

            # 2. For-Of
            if handler == "IteratorBegin" or "GetIterator(" in val_raw:
                for_of_node, new_idx = self._parse_for_of(i)
                if for_of_node:
                    root.body.append(for_of_node)
                    i = new_idx
                    continue

            # 3. If-Else (Sadece iterator step DIŞINDAKİ jump'lar)
            if handler in ("JmpTrue", "JmpFalse") and "for-in step" not in val_raw:
                if_node, new_idx = self._parse_if_statement(i)
                root.body.append(if_node)
                i = new_idx
                continue

            # 4. Redundant Iterator gürültülerini filtrele
            stmt_text = item.result if item.result else val_raw
            if self._is_redundant_iterator_bytecode(handler, stmt_text):
                i += 1
                continue

            # 5. Düz İfadeler
            if handler == "Ret":
                value = val_raw.split("return ")[1].strip() if "return " in val_raw else val_raw
                root.body.append(InstructionNode(
                    statement=f"return {value}",
                    original_bytecode=item.opcode.bytecode,
                    used=var.used
                ))
            elif handler not in ("CompleteGenerator", "SaveGenerator"):
                root.body.append(InstructionNode(
                    statement=stmt_text,
                    original_bytecode=item.opcode.bytecode,
                    used=var.used
                ))

            i += 1

        return root

    def _is_redundant_iterator_bytecode(self, handler: str, val_raw: str) -> bool:
        if handler in ("JmpUndefined", "JmpUndefinedLong", "JStrictEqual"):
            return True
        if handler in ("Catch", "IteratorClose", "Throw"):
            return True
        if "GetNextPName" in val_raw or "GetIterator(" in val_raw or "for-in step" in val_raw or "for-in property list" in val_raw:
            return True
        if handler in ("Jmp", "JmpLong") or "goto label_" in val_raw:
            return True
        return False

    def _parse_for_in(self, start_idx: int):
        first_item = self.results[start_idx]
        val_raw = first_item.variable.value or ""

        obj_name = "r10"
        if "Object.keys(" in val_raw:
            try:
                obj_name = val_raw.split("Object.keys(")[1].split(")")[0].strip()
            except IndexError:
                pass

        # Target address (Döngünün bittiği adresi bul)
        target_addr = None
        curr = start_idx
        while curr < self.n and curr < start_idx + 10:
            item_val = self.results[curr].variable.value or ""
            if self.results[curr].goto is not None and ("=== undefined" in item_val or "JmpUndefined" in self.results[curr].variable.handler):
                target_addr = self.results[curr].goto
                break
            curr += 1

        body_node = BlockNode()
        i = start_idx + 1

        while i < self.n:
            curr_item = self.results[i]
            if target_addr and curr_item.variable.address >= target_addr:
                break

            handler = curr_item.variable.handler
            val = curr_item.result if curr_item.result else (curr_item.variable.value or "")

            # Gerçek bir koşul (if) mi yoksa iterator step mi?
            if handler in ("JmpTrue", "JmpFalse") and "for-in step" not in val:
                if_node, next_i = self._parse_if_statement(i)
                body_node.body.append(if_node)
                i = next_i
                continue

            if self._is_redundant_iterator_bytecode(handler, val):
                i += 1
                continue

            body_node.body.append(InstructionNode(
                statement=val,
                original_bytecode=curr_item.opcode.bytecode,
                used=curr_item.variable.used
            ))
            i += 1

        return ForInNode(var_name="key", object_name=obj_name, body=body_node), i

    def _parse_for_of(self, start_idx: int):
        first_item = self.results[start_idx]
        val_raw = first_item.variable.value or ""

        iterable = "r13"
        if "GetIterator(" in val_raw:
            try:
                iterable = val_raw.split("GetIterator(")[1].split(")")[0].strip()
            except IndexError:
                pass

        body_node = BlockNode()
        i = start_idx + 1

        while i < self.n:
            curr_item = self.results[i]
            handler = curr_item.variable.handler
            val = curr_item.result if curr_item.result else (curr_item.variable.value or "")

            if self._is_redundant_iterator_bytecode(handler, val):
                if handler == "Throw":
                    i += 1
                    break
                i += 1
                continue

            body_node.body.append(InstructionNode(
                statement=val,
                original_bytecode=curr_item.opcode.bytecode,
                used=curr_item.variable.used
            ))
            i += 1

        return ForOfNode(var_name="item", iterable_name=iterable, body=body_node), i

    def _parse_if_statement(self, start_idx: int):
        item = self.results[start_idx]
        val_raw = item.variable.value or ""
        handler = item.variable.handler
        target_addr = item.goto

        condition = "true"
        if "if (" in val_raw:
            try:
                raw_cond = val_raw.split("if (")[1]
                cond_body = raw_cond.rsplit(")", 1)[0] if ")" in raw_cond else raw_cond
                condition = cond_body.split("/*")[0].strip()
            except Exception:
                condition = "true"

        # JmpFalse -> Koşul doğruysa ALTTAKİ koda girer (Condition)
        # JmpTrue -> Koşul yanlışsa ALTTAKİ koda girer (!(Condition))
        if handler == "JmpTrue":
            condition = f"!({condition})"

        then_body = BlockNode()
        else_body = BlockNode()

        # Jmp/JmpLong ile Else adresi yakalama
        else_target_addr = None
        i = start_idx + 1
        is_in_else = False

        while i < self.n:
            curr_item = self.results[i]
            c_handler = curr_item.variable.handler
            c_val = curr_item.result if curr_item.result else (curr_item.variable.value or "")

            # If/Else bloğunun tamamen bittiği adres
            if else_target_addr and curr_item.variable.address >= else_target_addr:
                break
            elif not is_in_else and target_addr and curr_item.variable.address >= target_addr:
                # If bloğu bitti, Else bloğuna geçiş kontrolü
                is_in_else = True
                if not else_target_addr:
                    break

            # İçteki For-Of döngüsü yakalama
            if c_handler == "IteratorBegin" or "GetIterator(" in c_val:
                for_of_node, next_i = self._parse_for_of(i)
                target_node = else_body if is_in_else else then_body
                target_node.body.append(for_of_node)
                i = next_i
                continue

            # İçteki If/Else yakalama
            if c_handler in ("JmpTrue", "JmpFalse") and "for-in step" not in c_val:
                # Eğer then_body'nin son adımı Jmp/JmpLong ise bu else geçişidir
                nested_if, next_i = self._parse_if_statement(i)
                target_node = else_body if is_in_else else then_body
                target_node.body.append(nested_if)
                i = next_i
                continue

            # Else geçiş sıçraması (Then bloğunun sonundaki Jmp)
            if not is_in_else and c_handler in ("Jmp", "JmpLong") and curr_item.goto:
                else_target_addr = curr_item.goto
                is_in_else = True
                i += 1
                continue

            if self._is_redundant_iterator_bytecode(c_handler, c_val):
                i += 1
                continue

            target_node = else_body if is_in_else else then_body
            target_node.body.append(InstructionNode(
                statement=c_val,
                original_bytecode=curr_item.opcode.bytecode,
                used=curr_item.variable.used
            ))
            i += 1

        if len(else_body.body) > 0:
            return IfNode(condition=condition, then_branch=then_body, else_branch=else_body), i
        return IfNode(condition=condition, then_branch=then_body), i