def lista_AB(lista_A, lista_B):
    list_AB = []
    for i in range(10):
        list_AB.append(lista_A[i])
    for i in range(10):
        list_AB.append(lista_B[i])
    return list_AB

def eliminar_repetidos(lista):
    unicos = []
    for num in lista:
        if num not in unicos:
            unicos.append(num)
    return unicos

def main():
    lista_A = []
    lista_B = []
    
    for i in range(10):
        a = int(input())
        lista_A.append(a)
    for i in range(10):
        b = int(input())
        lista_B.append(b)
    
    print(eliminar_repetidos(lista_AB(lista_A,lista_B)))
    
    
if __name__ == "__main__":
    main()