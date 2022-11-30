class VillainBetrayException(Exception):
    def __init__(self, uzenet):
        self.uzenet = uzenet
        super().__init__(self.uzenet)