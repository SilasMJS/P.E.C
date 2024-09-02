# função principal
def main():
    lista_A = []
    lista_B = []
    lista_C = []
    # estrutura de repetição
    for i in range(25):
        # entrada de dados
        lista_A.append(int(input()))
    for i in range(25):
        # entrada de dados
        lista_B.append(int(input()))
    for i in range(25):
        # entrada de dados
        lista_C.append(lista_A[i])
        lista_C.append(lista_B[i])
    # saída de dados
    print(lista_A)
    print(lista_B)
    print(lista_C)
# condição que verifica se a função/modulo é o principal se for vai chamar e executar
if __name__ == "__main__":
    main()