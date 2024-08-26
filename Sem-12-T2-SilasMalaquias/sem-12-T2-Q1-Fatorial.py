# RunCodes

# def main():
#     fatorial = aux = int(input())
    
#     if fatorial == 0:
#         fatorial = 1
#         print(fatorial)
#     else:    
#         for i in range(fatorial-1,0,-1):
#             aux *= i
#         print(f"{aux}")
        
    
# if __name__ == "__main__":
#     main()

# ClassRoom
# função auxiliar
def e_Fatorial(fatorial):
    aux = fatorial
    # estrutura de condição
    if fatorial == 0:
        fatorial = 1
        print(fatorial)
    else:  
        # estrutura de repetição  
        for i in range(fatorial-1,0,-1):
            # processamento de dados
            aux *= i
        print(f"O fatorial do {fatorial} é {aux}")
# função principal
def main():
    # entrada de dados
    fatorial = int(input("Digite um Número: "))
    # saída de dados
    e_Fatorial(fatorial)
# condição que verifica se a função/modulo é o principal se for vai chamar e executar
if __name__ == "__main__":
    main()