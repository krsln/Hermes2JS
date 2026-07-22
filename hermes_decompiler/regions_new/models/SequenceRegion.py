from hermes_decompiler.regions_new.models.Region import Region


class SequenceRegion(Region):

    def __init__(self):

        super().__init__()

        self.children: list[Region] = []

    def append(self, region: Region):

        region.parent = self
        self.children.append(region)