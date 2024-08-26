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

# def main():
#     n = int(input())
    
#     print(e_primo(n))
    
# if __name__ == "__main__":
#     main()

# ClassRoom
# função auxiliar
def e_primo(n):
    # estrutura de condição
    if n <= 1: return False
    elif n == 2: return True
    elif n % 2 == 0: return False
    # estrutura de repetição
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:return False
    else:return True
# função principal
def main():
    # entrada de dados
    n = int(input("Digite um Número: "))
    # saída de dados
    print(f"{e_primo(n)}")
# condição que verifica se a função/modulo é o principal se for vai chamar e executar
if __name__ == "__main__":
    main()