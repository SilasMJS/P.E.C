# def maior_e_menor():
#     x = 1
#     maior = 0
#     menor = 99999
#     while x != 0:
#         n = int(input())
#         if n == 0:
#             x = 0
#         elif n >= maior:
#             maior = n
#         if n < menor:
#             if n != 0:
#                 menor = n
#     return f"{maior}\n{menor}"
# função principal
def main():
    # print(maior_e_menor())
    maior = 0
    menor = 99999
    while True:
        # entrada de dados
        n = int(input("Digite um Número Positivo: "))
        # estrutura de condição
        if n != 0:
            if n > maior:
                maior = n
            if n < menor:
                menor = n
        else:
            break
    # saída de dados
    print(f"Dos Números Informado o Maior é {maior} e o Menor é {menor}.")
# condição que verifica se a função/modulo é o principal se for vai chamar e executar
if __name__ == "__main__":
    main()