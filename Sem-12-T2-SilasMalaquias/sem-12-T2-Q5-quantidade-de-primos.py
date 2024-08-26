# RunCodes
# def e_primo(n):
#     if n <= 1:
#         return False
#     elif n == 2:
#         return True
#     elif n % 2 == 0:
#         return False
#     for i in range(3, int(n**0.5) + 1, 2):
#         if n % i == 0:
#             return False
#     else:
#         return True
# def num_primos(x,y):
#     for n in range(x, y + 1):
#         if e_primo(n):
#             print(n)
# def main():
#     x = int(input())
#     y = int(input())
#     num_primos(x, y)

# if __name__ == "__main__":
#     main()


# ClassRoom
# função auxiliar
def e_primo(n):
    # estrutura de condição
    if n <= 1:return False
    elif n == 2:return True
    elif n % 2 == 0:return False
    # estrutura de repetição
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:return False
    else:return True
# função auxiliar
def num_primos(x,y):
    # estrutura de repetição
    for n in range(x, y + 1):
        if e_primo(n):
            print(n)
# função principal
def main():
    x = int(input("Digite o valor Inicial: "))
    y = int(input("Digite o valor Final: "))
    # saída de dados
    num_primos(x, y)
# função principal
if __name__ == "__main__":
    main()