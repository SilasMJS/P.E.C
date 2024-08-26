# RunCodes
# def main():
#     n = int(input())
#     penult = 1
#     ultimo = 0
#     resultado = "0, 1" 
#     for _ in range(2, n):
#         proximo = penult + ultimo
#         resultado += f", {proximo}"
#         ultimo = penult
#         penult = proximo
#     print(resultado)
# if __name__ == "__main__":
#     main()


# função auxiliar
def fibonacci(n):
    ultimo = 0
    penult = 1
    result = "0, 1"
    # estrutura de repetição
    for _ in range(2, n):
        # processamento de dados
        proximo = penult + ultimo
        result += f", {proximo}"
        ultimo = penult
        penult = proximo
# função principal
def main():
    n = int(input("Digite um Número: "))
# condição que verifica se a função/modulo é o principal se for vai chamar e executar
if __name__ == "__main__":
    main()