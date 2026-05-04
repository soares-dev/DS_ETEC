from colorama import init, Fore, Style

init(autoreset=True)

niveis = [
    "Nível 1 - Muito baixo (crítico)",
    "Nível 2 - Baixo",
    "Nível 3 - Médio",
    "Nível 4 - Alto",
    "Nível 5 - Muito alto (alerta)"
]

def definir_cor(nivel):
    if nivel == 1:
        return Fore.RED
    elif nivel == 2:
        return Fore.YELLOW
    elif nivel == 3:
        return Fore.GREEN
    elif nivel == 4:
        return Fore.CYAN
    elif nivel == 5:
        return Fore.BLUE
    else:
        return Fore.WHITE

# Função para exibir o status do reservatório
def exibir_status():
    print("\n=== MONITORAMENTO DO RESERVATÓRIO ===\n")
    
    for i, mensagem in enumerate(niveis, start=1):
        cor = definir_cor(i)
        print(cor + mensagem)

    # Restaura estilo padrão do terminal
    print(Style.RESET_ALL)

# Simulação do sistema
exibir_status()
