def eliminar_repetidos(lista):
    unicos = []
    for num in lista:
        if num not in unicos:
            unicos.append(num)
    return unicos
def main():
    lista = []
    
    for i in range(20):
        n = int(input())
        lista.append(n)
    print(eliminar_repetidos(lista))
    
    
if __name__ == "__main__":
    main()