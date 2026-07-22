class CFG:

    def __init__(self):
        self.blocks = []

        self.entry = None

    @classmethod
    def from_results(cls, results):
        return CFG()