class Flor:
    HABITATS_NORDESTE = ["Caatinga", "Mata Atlântica Nordestina", "Sertão", "Chapada Diamantina"]
    HABITATS_NORTE = ["Floresta Amazônica", "Igapó", "Várzea"]
    HABITATS_SUL = ["Pampas", "Mata de Araucária", "Campos Sulinos"]

    def __init__(self, nome, tipo, habitat, fragrancia, curiosidade):
        self.nome = nome
        self.tipo = tipo  
        self.habitat = habitat
        self.fragrancia = self.ajustar_fragrancia(fragrancia)
        self.curiosidade = curiosidade

    def ajustar_fragrancia(self, fragrancia):
        """Ajusta a fragrância dependendo da região"""
        if self.habitat in self.HABITATS_NORDESTE:
            return f"{fragrancia} (mais seca devido ao clima nordestino)"
        return fragrancia

    def crescer(self):
        """Define o crescimento baseado na região"""
        if self.habitat in self.HABITATS_NORDESTE:
            return f"A flor {self.nome} está crescendo lentamente devido ao clima seco do Nordeste."
        elif self.habitat in self.HABITATS_NORTE:
            return f"A flor {self.nome} está se desenvolvendo rapidamente no clima úmido do Norte."
        elif self.habitat in self.HABITATS_SUL:
            return f"A flor {self.nome} cresce melhor em temperaturas frias do Sul."
        return f"A flor {self.nome} está crescendo no seu habitat normal."

    def descrever(self):
        return (f"{self.nome} é uma flor do tipo {self.tipo.lower()} que cresce em {self.habitat}. "
                f"Tem uma fragrância {self.fragrancia.lower()} e uma curiosidade interessante: {self.curiosidade}")
    
    @staticmethod
    def mostrar_flores_por_regiao(regiao, lista_flores):
        """Filtra e imprime as flores baseadas na região fornecida"""
        flores_regiao = {
            "norte": Flor.HABITATS_NORTE,
            "nordeste": Flor.HABITATS_NORDESTE,
            "sul": Flor.HABITATS_SUL
        }

        if regiao not in flores_regiao:
            print(f"Região {regiao} inválida.")
            return
        
        habitat_valido = flores_regiao[regiao]

        flores_encontradas = [flor for flor in lista_flores if flor.habitat in habitat_valido]

        if flores_encontradas:
            print(f"Flores encontradas na região {regiao.capitalize()}:")
            for flor in flores_encontradas:
                print(flor.descrever())
        else:
            print(f"Nenhuma flor encontrada na região {regiao.capitalize()}.")

