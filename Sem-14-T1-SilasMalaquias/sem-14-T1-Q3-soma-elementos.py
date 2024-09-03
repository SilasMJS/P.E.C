def soma_listas(lista_A,lista_B):
    lista_C = []
    for i in range(20):
        lista_C.append(lista_A[i] + lista_B[i])
    return lista_C
        
def main():
    lista_A = []
    lista_B = []

    for i in range(20):
        lista_A.append(int(input()))
    for i in range(20):
        lista_B.append(int(input()))

    print(lista_A)
    print(lista_B)
    print(soma_listas(lista_A,lista_B))

if __name__ == "__main__":
    main()