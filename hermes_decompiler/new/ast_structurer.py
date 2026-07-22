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

            # -------------------------------------------------------------
            # PATTERN 1: For-In Döngüsü Algılama (GetPNameList + GetNextPName)
            # -------------------------------------------------------------
            if handler == "GetPNameList" or ("Object.keys(" in val_raw and "for-in property list" in val_raw):
                for_in_node, new_idx = self._parse_for_in(i)
                if for_in_node:
                    root.body.append(for_in_node)
                    i = new_idx
                    continue

            # -------------------------------------------------------------
            # PATTERN 2: For-Of / Iterator Döngüsü Algılama (IteratorBegin)
            # -------------------------------------------------------------
            if handler == "IteratorBegin" or "GetIterator(" in val_raw:
                for_of_node, new_idx = self._parse_for_of(i)
                if for_of_node:
                    root.body.append(for_of_node)
                    i = new_idx
                    continue

            # -------------------------------------------------------------
            # PATTERN 3: Standart If/Else Yapıları
            # -------------------------------------------------------------
            if "/* jump to" in val_raw and item.goto is not None:
                if_node, new_idx = self._parse_if_statement(i)
                root.body.append(if_node)
                i = new_idx
                continue

            # -------------------------------------------------------------
            # DÜZ İFADELER VEYA RETURN
            # -------------------------------------------------------------
            if handler == "Ret":
                value = val_raw.split("return ")[1].strip() if "return " in val_raw else val_raw
                root.body.append(InstructionNode(
                    statement=f"return {value}",
                    original_bytecode=item.opcode.bytecode,
                    used=var.used
                ))
            elif handler not in ("CompleteGenerator", "SaveGenerator"):
                stmt_text = item.result if item.result else val_raw
                root.body.append(InstructionNode(
                    statement=stmt_text,
                    original_bytecode=item.opcode.bytecode,
                    used=var.used
                ))

            i += 1

        return root

    def _parse_for_in(self, start_idx: int):
        first_item = self.results[start_idx]
        val_raw = first_item.variable.value or ""

        obj_name = "r10"
        if "Object.keys(" in val_raw:
            try:
                obj_name = val_raw.split("Object.keys(")[1].split(")")[0].strip()
            except IndexError:
                pass

        target_addr = None
        curr = start_idx
        while curr < self.n and curr < start_idx + 5:
            if self.results[curr].goto is not None and "=== undefined" in (self.results[curr].variable.value or ""):
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

            # 🔴 FILTRE BURADA ÇAĞRILIYOR: Redundant satırları atla
            if self._is_redundant_iterator_bytecode(handler, val):
                i += 1
                continue

            body_node.body.append(InstructionNode(
                statement=val,
                original_bytecode=curr_item.opcode.bytecode,
                used=curr_item.variable.used
            ))
            i += 1

        node = ForInNode(var_name="key", object_name=obj_name, body=body_node)
        return node, i

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

            # 🔴 FILTRE BURADA ÇAĞRILIYOR: Catch/IteratorClose/Throw görünce döngü gövdesini bitir
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

        node = ForOfNode(var_name="item", iterable_name=iterable, body=body_node)
        return node, i

    def _parse_if_statement(self, start_idx: int):
        item = self.results[start_idx]
        val_raw = item.variable.value or ""

        condition = "true"
        try:
            condition = val_raw.split("if (")[1].split(")")[0].strip()
        except IndexError:
            pass

        target_addr = item.goto
        then_body = BlockNode()
        i = start_idx + 1

        while i < self.n and self.results[i].variable.address < target_addr:
            curr_item = self.results[i]
            stmt = curr_item.result if curr_item.result else (curr_item.variable.value or "")
            then_body.body.append(InstructionNode(
                statement=stmt,
                original_bytecode=curr_item.opcode.bytecode,
                used=curr_item.variable.used
            ))
            i += 1

        return IfNode(condition=condition, then_branch=then_body), i

    def _is_redundant_iterator_bytecode(self, handler: str, val_raw: str) -> bool:
        """
        Hermes'in iterator / for-of / for-in için ürettiği alt seviye kontrol,
        exception handling ve ham jump satırlarını filtreler.
        """
        # 1. Iterator Kapatma ve Catch/Throw blokları
        if handler in ("Catch", "IteratorClose", "Throw"):
            return True

        # 2. Döngü adımı atlama ifadeleri (High-level döngüye dönüştüğü için gereksiz)
        if "GetNextPName" in val_raw or "GetIterator(" in val_raw:
            return True

        # 3. Ham goto/label atlamaları
        if "goto label_" in val_raw or "/* jump to" in val_raw:
            return True

        return False
