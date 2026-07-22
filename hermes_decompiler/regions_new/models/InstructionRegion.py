from hermes_decompiler.regions_new.models.Region import Region


class InstructionRegion(Region):

    def __init__(self, result):

        self.result = result