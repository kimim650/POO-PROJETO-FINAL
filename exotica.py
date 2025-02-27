from flor import Flor

class Exotica(Flor):
    def __init__(self, nome, habitat, fragrancia, origem):
        super().__init__(nome, "Exótica", habitat, fragrancia, f"É uma flor rara, originária de {origem}.")
