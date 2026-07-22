from hermes_decompiler.regions_new.models.Regions import SequenceRegion, InstructionRegion, LoopRegion

from hermes_decompiler.regions_new.models.Regions import (
    SequenceRegion, InstructionRegion, LoopRegion
)


class SequenceStructurer:
    def __init__(self, cfg):
        self.cfg = cfg

    def run(self):
        root = SequenceRegion()
        for block in self.cfg.blocks:
            root.append(InstructionRegion(block))
        return root


class LoopStructurer:
    def __init__(self, root, cfg):
        self.root = root
        self.cfg = cfg

    def run(self):
        if not self.cfg.loop_analysis:
            return

        loops = sorted(self.cfg.loop_analysis.loops.values(), key=lambda l: l.header.id)

        for loop in loops:
            self._insert_loop_region(loop)

    def _insert_loop_region(self, natural_loop):
        """Sırayı bozmadan loop'u sar"""
        loop_region = LoopRegion(natural_loop)
        body = SequenceRegion()

        # Header bul ve LoopRegion ile değiştir
        header_found = False
        new_children = []

        if body.children:
            loop_region.append(body)

        def traverse(region):
            nonlocal header_found
            if isinstance(region, SequenceRegion):
                i = 0
                while i < len(region.children):
                    child = region.children[i]
                    if isinstance(child, InstructionRegion):
                        if child.block == natural_loop.header and not header_found:
                            # Header'ı loop region ile değiştir
                            loop_region.append(child)  # header as first child
                            region.children[i] = loop_region
                            header_found = True
                            i += 1
                            continue

                        # Loop member ise body'ye taşı
                        if child.block.id in [b.id for b in natural_loop.members]:
                            body.append(child)
                            # Orijinalden kaldır
                            del region.children[i]
                            continue

                    else:
                        traverse(child)
                    i += 1

        traverse(self.root)

        # Body'yi loop'a ekle
        if body.children:
            loop_region.append(body)

        # Kalan temizlik
        self._cleanup_empty_sequences(self.root)

    def _cleanup_empty_sequences(self, region):
        if isinstance(region, SequenceRegion):
            region.children = [c for c in region.children if not (isinstance(c, SequenceRegion) and not c.children)]
            for child in region.children:
                self._cleanup_empty_sequences(child)
        elif hasattr(region, 'children'):
            for child in region.children:
                self._cleanup_empty_sequences(child)


class IfStructurer:
    def __init__(self, root, cfg):
        self.root = root
        self.cfg = cfg

    def run(self):
        self._structure_conditionals(self.root)

    def _structure_conditionals(self, region):
        if isinstance(region, SequenceRegion):
            i = 0
            while i < len(region.children):
                child = region.children[i]
                if isinstance(child, InstructionRegion):
                    last = child.block.last
                    val = last.variable.value
                    if "if (" in val and last.goto is not None:
                        # Basit if tespit
                        cond = val.split("if (")[1].split(")")[0]
                        # Şimdilik sadece yorum ekle
                        if "// if" not in child.block.instructions[-1].result:
                            child.block.instructions[-1].result = f"if ({cond}) {{ /* jump to {last.goto} */ }}"
                i += 1

        if hasattr(region, 'children'):
            for c in region.children:
                self._structure_conditionals(c)

class SwitchStructurer:
    def __init__(self, root, cfg):
        self.root = root
        self.cfg = cfg

    def run(self):
        pass  # TODO


class TryStructurer:
    def __init__(self, root, cfg):
        self.root = root
        self.cfg = cfg

    def run(self):
        pass  # IteratorClose vb. için önemli