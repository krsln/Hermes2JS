from hermes_decompiler.regions_new.models.Regions import (
    SequenceRegion,
    InstructionRegion,
    LoopRegion
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

        loops = sorted(
            self.cfg.loop_analysis.loops.values(),
            key=lambda loop: loop.header.id
        )

        for loop in loops:
            self._wrap_loop(loop)

    def _wrap_loop(self, natural_loop):

        loop_region = LoopRegion(natural_loop)

        new_children = []

        header_index = None

        for child in self.root.children:

            if not isinstance(child, InstructionRegion):
                new_children.append(child)
                continue

            block = child.block

            # Header
            if block == natural_loop.header:

                header_index = len(new_children)

                loop_region.header = child

                continue

            # Loop body
            if block in natural_loop.members:

                loop_region.body.append(child)

                continue

            # Outside loop
            new_children.append(child)

        if loop_region.header is None:
            return

        if header_index is None:
            header_index = len(new_children)

        new_children.insert(
            header_index,
            loop_region
        )

        self.root.children = new_children


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
