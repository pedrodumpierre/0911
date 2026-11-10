from busca import pesquisar_servidor
from cadastro import cadastrar_servidores
from exibicao import listar_servidores
from ordenacao import ordenar_servidores


def exibir_menu():
    print("\n===== Simulador de Desempenho de Servidores =====")
    print("1 - Listar servidores")
    print("2 - Ordenar servidores em ordem alfabetica")
    print("3 - Pesquisar servidor")
    print("0 - Sair")


def main():
    servidores = [""] * 5
    metricas = [[0.0, 0.0, 0.0] for _ in range(5)]

    print("Cadastro inicial dos cinco servidores")
    cadastrar_servidores(servidores, metricas)

    while True:
        exibir_menu()
        opcao = input("Escolha uma opcao: ").strip()

        match opcao:
            case "1":
                listar_servidores(servidores, metricas)
            case "2":
                ordenar_servidores(servidores, metricas)
                print("Servidores ordenados em ordem alfabetica.")
            case "3":
                pesquisar_servidor(servidores, metricas)
            case "0":
                print("Programa encerrado.")
                break
            case _:
                print("Opcao invalida. Tente novamente.")


if __name__ == "__main__":
    main()
