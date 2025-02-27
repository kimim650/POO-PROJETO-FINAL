class Jardim:
    def __init__(self):
        self.flores = []

    def adicionar_flor(self, flor):
        """Adiciona uma flor ao jardim."""
        self.flores.append(flor)

    def listar_flores(self):
        """Lista todas as flores do jardim"""
        if not self.flores:
            return "O jardim ainda não tem flores cadastradas."
        return "\n".join([flor.descrever() for flor in self.flores])

    def crescer_flores(self):
        """Faz todas as flores crescerem de acordo com o habitat"""
        if not self.flores:
            return "Nenhuma flor para crescer."
        return "\n".join([flor.crescer() for flor in self.flores])

    def mostrar_flores_por_regiao(self, regiao):
        """Filtra e exibe flores por região, garantindo comparação correta entre maiúsculas e minúsculas."""
        
        # Dicionário com regiões e os habitats que pertencem a essas regiões
        flores_regiao = {
            "norte": ["Floresta Amazônica", "Igapó", "Várzea"],
            "nordeste": ["Caatinga", "Mata Atlântica Nordestina", "Sertão", "Chapada Diamantina"],
            "sul": ["Pampas", "Mata de Araucária", "Campos Sulinos"]
        }

        # Normalizando a região para minúsculas
        regiao = regiao.lower()

        # Filtrando flores que pertencem à região selecionada
        flores_encontradas = [
            flor for flor in self.flores
            if flor.habitat.lower() in [h.lower() for h in flores_regiao.get(regiao, [])]
        ]

        if flores_encontradas:
            print(f"Flores encontradas na região {regiao.capitalize()}:")
            for flor in flores_encontradas:
                print(flor.descrever())
        else:
            print(f"Nenhuma flor encontrada na região {regiao.capitalize()}.")
