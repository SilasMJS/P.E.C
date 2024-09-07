# função auxiliar
def lista_AB(lista_A, lista_B):
    list_AB = []
    for i in range(10):
        list_AB.append(lista_A[i])
    for i in range(10):
        list_AB.append(lista_B[i])
    return list_AB
# função auxiliar
def eliminar_repetidos(lista):
    unicos = []
    for num in lista:
        if num not in unicos:
            unicos.append(num)
    return unicos
# função principal
def main():
    lista_A = []
    lista_B = []
    # estrutura de repetição
    for i in range(10):
        # entrada de dados
        a = int(input("Digite um Número: "))
        lista_A.append(a)
    for i in range(10):
        # entrada de dados
        b = int(input("Digite um Número: "))
        lista_B.append(b)
    # saída de dados
    print(f"A união das duas Listas:\n{eliminar_repetidos(lista_AB(lista_A,lista_B))}")
# condição que verificar se a função/modulo é o principal se for vai chamar e executar
if __name__ == "__main__":
    main()