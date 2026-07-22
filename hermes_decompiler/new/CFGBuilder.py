from typing import List, Any, Dict, Optional

from hermes_decompiler.new.cfg_models import BasicBlock


class CFGBuilder:
    def __init__(self, results: List[Any], goto_list: List[int]):
        self.results = results
        self.goto_list = set(goto_list)

    def build(self) -> List[BasicBlock]:
        if not self.results:
            return []

        # 1. Adım: Lider (Leader) Adreslerinin Tespiti
        leaders = {self.results[0].variable.address}

        for item in self.results:
            if item.goto is not None:
                leaders.add(item.goto)
            if item.extra_gotos:
                leaders.update(item.extra_gotos)
            if item.variable.address in self.goto_list:
                leaders.add(item.variable.address)

        # 2. Adım: Blokların Oluşturulması
        blocks: Dict[int, BasicBlock] = {}
        current_block: Optional[BasicBlock] = None
        block_id_seq = 0

        for i, item in enumerate(self.results):
            addr = item.variable.address

            if addr in leaders or current_block is None:
                current_block = BasicBlock(
                    id=block_id_seq,
                    start_addr=addr,
                    end_addr=addr
                )
                blocks[addr] = current_block
                block_id_seq += 1

            current_block.results.append(item)
            current_block.end_addr = addr

        # 3. Adım: Kenarların (Edges - Jump Connections) Bağlanması
        all_blocks_sorted = sorted(blocks.values(), key=lambda b: b.start_addr)
        addr_to_block = {b.start_addr: b for b in all_blocks_sorted}

        for idx, block in enumerate(all_blocks_sorted):
            last_item = block.results[-1]

            # Koşullu / Koşulsuz Atlama Tespiti
            if last_item.goto is not None:
                if last_item.goto in addr_to_block:
                    block.add_successor(addr_to_block[last_item.goto])

            # Switch veya Ekstra Atlama Hedefleri
            if last_item.extra_gotos:
                for target_addr in last_item.extra_gotos:
                    if target_addr in addr_to_block:
                        block.add_successor(addr_to_block[target_addr])

            # Fallthrough (Düz Akış): Son talimat unconditional JMP/RET değilse sonraki bloğa bağla
            if last_item.variable.handler not in ("Ret", "Jmp") and (idx + 1) < len(all_blocks_sorted):
                # Eğer conditional jump ise, fallthrough da bir successor'dır
                block.add_successor(all_blocks_sorted[idx + 1])

        return all_blocks_sorted
