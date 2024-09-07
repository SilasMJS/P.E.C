# função auxiliar 
def soma_listas(lista_A,lista_B):
    lista_C = []
    # estrutura de repetição
    for i in range(20):
        lista_C.append(lista_A[i] + lista_B[i])
    return lista_C
# função principal
def main():
    lista_A = []
    lista_B = []
    # estrutura de repetição
    for i in range(20):
        # entrada de dados
        lista_A.append(int(input("Digite um Número: ")))
    for i in range(20):
        # entrada de dados
        lista_B.append(int(input("Digite um Número: ")))
    # saída de dados
    print(f"Sequência A:\n{lista_A}")
    print(f"Sequência B:\n{lista_B}")
    print(f"Soma das duas Sequências:\n{soma_listas(lista_A,lista_B)}")
# condição que verificar se a função/modulo é o principal se for vai chamar e executar
if __name__ == "__main__":
    main()