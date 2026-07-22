from hermes_decompiler.regions_new.models.Region import Region


class LoopRegion(Region):

    def __init__(self, natural_loop):

        super().__init__()

        self.loop = natural_loop

        self.children: list[Region] = []

    def append(self, region):

        region.parent = self
        self.children.append(region)