def soma_Cumulativa(lista):
    lista_N = []
    lista_N.append(lista[0])
    soma = lista[0]
    for i in lista[1:]:
        soma += i
        lista_N.append(soma)
    return lista_N

def main():
    lista = []
    while True:
        n = int(input())
        
        if n == 0:
            break
        else:
            lista.append(n)
    print(soma_Cumulativa(lista))
    
    
    
if __name__ == "__main__":
    main()