from flor import Flor

class Ornamental(Flor):
    def __init__(self, nome, habitat, fragrancia, curiosidade):
        super().__init__(nome, "Ornamental", habitat, fragrancia, curiosidade)
