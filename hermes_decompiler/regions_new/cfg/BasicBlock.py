class BasicBlock:

    def __init__(self, id: int):
        self.id = id

        self.instructions = []

        self.predecessors = []

        self.successors = []
