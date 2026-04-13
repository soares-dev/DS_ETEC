# Contadores
excelente = 0
ruim = 0

# Loop para 50 entrevistados
for i in range(50):
    print("\nEntrevistado número:", i + 1)
    
    nome = input("Digite o nome: ")
    idade = int(input("Digite a idade: "))
    
    print("Opinião sobre o atendimento:")
    print("1 - EXCELENTE")
    print("2 - BOM")
    print("3 - RUIM")
    
    opiniao = int(input("Digite o número da sua opinião: "))

    # Estrutura de decisão
    if opiniao == 1:
        print("Você avaliou como EXCELENTE.")
        excelente += 1
    elif opiniao == 3:
        print("Você avaliou como RUIM.")
        ruim += 1
    elif opiniao == 2:
        print("Você avaliou como BOM.")
    else:
        print("Opção inválida, resposta não contabilizada.")

# Resultados finais
print("\n===== RESULTADO DA PESQUISA =====")
print("Quantidade de respostas EXCELENTE:", excelente)
print("Quantidade de respostas RUIM:", ruim)
