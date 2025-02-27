from flor import Flor

class Medicinal(Flor):
    def __init__(self, nome, habitat, fragrancia, beneficio):
        super().__init__(nome, "Medicinal", habitat, fragrancia,
                         f"É utilizada na medicina natural para {beneficio}.")
