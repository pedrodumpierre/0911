def classificar_servidor(cpu, ram):
    """Classifica o servidor conforme o uso de CPU e memoria RAM."""
    if cpu > 85 or ram > 85:
        return "Sobrecarga Critica"
    if cpu < 40 and ram < 40:
        return "Servidor Ocioso"
    if 50 <= cpu <= 85 or 50 <= ram <= 85:
        return "Carga Moderada"
    return "Status: Estavel"
