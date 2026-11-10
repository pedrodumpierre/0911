def ordenar_servidores(servidores, metricas):
    """Ordena os servidores alfabeticamente usando Bubble Sort."""
    quantidade = len(servidores)
    for limite in range(quantidade - 1, 0, -1):
        houve_troca = False
        for i in range(limite):
            if servidores[i].casefold() > servidores[i + 1].casefold():
                servidores[i], servidores[i + 1] = (
                    servidores[i + 1],
                    servidores[i],
                )
                metricas[i], metricas[i + 1] = metricas[i + 1], metricas[i]
                houve_troca = True
        if not houve_troca:
            break
