# RunCodes
# def nasc(nascimento):
#     nascimento = nascimento * 0.01
#     return nascimento
# def mort(mortes):
#     mortes = mortes * 0.06
#     return mortes
# def pop_Original(populacao):
#     populacao = populacao * 0.10
#     return populacao
# def main():
#     ano = 1600
#     populacao = float(input())
#     original_pop = populacao
#     nascimento = populacao
#     mortes = populacao
#     while True:
#         nascimento = nasc(populacao)
#         mortes = mort(populacao)
#         populacao -= mortes
#         populacao += nascimento
#         print(f"{ano},{nascimento:.0f},{mortes:.0f},{round(populacao)}")
#         ano += 1
#         if populacao < pop_Original(original_pop):
#             break
# if __name__ == "__main__":
#     main()



# ClassRoom
# Função auxiliar
def queda_populacao(popu):
    ano = 1600
    original_pop = popu
    nasc = popu
    mortes = popu
    # estrutura de repetição
    while True:
        # processamento de dados
        nasc = popu * 0.01
        mortes = popu * 0.06
        popu -= mortes
        popu += nasc
        print(f"Ano: {ano}, Nascimento: {nasc:.0f}, Mortes: {mortes:.0f}, População: {round(popu)}")
        ano += 1
        if popu < (original_pop * 0.10):
            break
# função principal
def main():
    # entrada de dados
    populacao = float(input("Digite o Valor da População Inicial: "))
    # saída de dados
    queda_populacao(populacao)
# condição que verifica se a função/modulo é o principal se for vai ser chamado e executado
if __name__ == "__main__":
    main()