def ler_porcentagem(mensagem):
    """Le e valida uma porcentagem entre 0 e 100."""
    while True:
        try:
            valor = float(input(mensagem).replace(",", "."))
            if 0 <= valor <= 100:
                return valor
            print("Valor invalido. Digite um numero entre 0 e 100.")
        except ValueError:
            print("Entrada invalida. Digite um numero.")


def ler_uptime():
    """Le e valida o uptime em horas."""
    while True:
        try:
            valor = float(input("Uptime (em horas): ").replace(",", "."))
            if valor >= 0:
                return valor
            print("O uptime nao pode ser negativo.")
        except ValueError:
            print("Entrada invalida. Digite um numero.")


def cadastrar_servidores(servidores, metricas):
    """Cadastra as identificacoes e metricas dos servidores."""
    for i in range(len(servidores)):
        while True:
            identificacao = input(
                f"\nIdentificacao do servidor {i + 1}: "
            ).strip()
            if not identificacao:
                print("A identificacao nao pode ficar vazia.")
            elif any(
                identificacao.casefold() == servidor.casefold()
                for servidor in servidores[:i]
            ):
                print("Essa identificacao ja foi cadastrada.")
            else:
                break

        servidores[i] = identificacao
        metricas[i][0] = ler_porcentagem("Uso de CPU (%): ")
        metricas[i][1] = ler_porcentagem("Uso de memoria RAM (%): ")
        metricas[i][2] = ler_uptime()
