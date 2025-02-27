from jardim import Jardim
from ornamental import Ornamental
from medicinal import Medicinal
from exotica import Exotica

def menu():
    jardim = Jardim()

    while True:
        print("\nMenu:")
        print("1. Adicionar Flor Ornamental")
        print("2. Adicionar Flor Medicinal")
        print("3. Adicionar Flor Exótica")
        print("4. Listar Flores")
        print("5. Crescer Flores")
        print("6. Mostrar flores por região")
        print("7. Remover Flor")
        print("8. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("Nome da Flor: ")
            habitat = input("Habitat: ")
            fragrancia = input("Fragrância: ")
            curiosidade = input("Curiosidade:") 
            flor = Ornamental(nome, habitat, fragrancia, curiosidade)
            jardim.adicionar_flor(flor)

        elif opcao == "2":
            nome = input("Nome da Flor: ")
            habitat = input("Habitat: ")
            fragrancia = input("Fragrância: ")
            beneficio = input("Benefício: ")
            flor = Medicinal(nome, habitat, fragrancia, beneficio)
            jardim.adicionar_flor(flor)

        elif opcao == "3":
            nome = input("Nome da Flor: ")
            habitat = input("Habitat: ")
            fragrancia = input("Fragrância: ")
            origem = input("Origem: ")
            flor = Exotica(nome, habitat, fragrancia, origem)
            jardim.adicionar_flor(flor)

        elif opcao == "4":
            print(jardim.listar_flores())

        elif opcao == "5":
            print(jardim.crescer_flores())

        elif opcao == "6":
            regiao = input("Digite a região (norte, nordeste, sul): ").lower()
            jardim.mostrar_flores_por_regiao(regiao)

        elif opcao == "7":
            nome_flor = input("Digite o nome da flor para remover: ")
            jardim.remover_flor(nome_flor)

        elif opcao == "8":
            print("Saindo...")
            break

        else:
            print("Opção inválida, tente novamente.")

if __name__ == "__main__":
    menu()
