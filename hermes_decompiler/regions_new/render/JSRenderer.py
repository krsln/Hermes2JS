from hermes_decompiler.regions_new.models.InstructionRegion import InstructionRegion
from hermes_decompiler.regions_new.models.SequenceRegion import SequenceRegion


class JSRenderer:

    def __init__(self, verbose=False):

        self.verbose = verbose

    def render(self, region):

        output=[]

        self._render(region,output,0)

        return output

    def _render(self, region, output, indent):

        if isinstance(region, SequenceRegion):

            ...

        elif isinstance(region, InstructionRegion):

            ...