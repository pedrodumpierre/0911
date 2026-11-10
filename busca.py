from exibicao import exibir_servidor
from ordenacao import ordenar_servidores


def busca_binaria(servidores, identificacao):
    """Procura uma identificacao em uma lista previamente ordenada."""
    inicio = 0
    fim = len(servidores) - 1
    procurado = identificacao.casefold()

    while inicio <= fim:
        meio = (inicio + fim) // 2
        atual = servidores[meio].casefold()

        if atual == procurado:
            return meio
        if atual < procurado:
            inicio = meio + 1
        else:
            fim = meio - 1

    return -1


def pesquisar_servidor(servidores, metricas):
    """Ordena os dados e pesquisa um servidor por busca binaria."""
    ordenar_servidores(servidores, metricas)
    identificacao = input("Digite a identificacao do servidor: ").strip()
    indice = busca_binaria(servidores, identificacao)

    if indice == -1:
        print("Servidor nao encontrado.")
    else:
        exibir_servidor(servidores[indice], metricas[indice])
