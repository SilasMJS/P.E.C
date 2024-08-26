# RunCodes
# def main():
#     h = 0
#     n = int(input())
#     for i in range(1,n+1):
#         h += 1/i
        
#     print(f"{h:.4f}")
    
    
# if __name__ == "__main__":
#     main()


# ClassRoom
def main():
    h = 0
    # entrada de dados
    n = int(input("Digite um Número: "))
    # estrutura de repetição
    for i in range(1,n+1):
        h += 1/i
    # saída de dados
    print(f"O Valor de H é {h:.4f}")
# condição que verifica se a função/modulo é o principal se for vai chamar e executar
if __name__ == "__main__":
    main()