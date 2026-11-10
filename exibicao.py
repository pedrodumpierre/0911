from classificacao import classificar_servidor


def exibir_servidor(servidor, metricas):
    cpu, ram, uptime = metricas
    print(f"\nServidor: {servidor}")
    print(f"Uso de CPU: {cpu:.1f}%")
    print(f"Uso de memoria RAM: {ram:.1f}%")
    print(f"Uptime: {uptime:.1f} horas")
    print(f"Classificacao: {classificar_servidor(cpu, ram)}")
    if uptime > 720:
        print("Reinicializacao Preventiva Necessaria")


def listar_servidores(servidores, metricas):
    """Exibe todos os servidores cadastrados e suas metricas."""
    print("\n--- Servidores cadastrados ---")
    for i in range(len(servidores)):
        exibir_servidor(servidores[i], metricas[i])
