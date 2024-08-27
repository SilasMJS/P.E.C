from random import *
def impar_E_par(lista):
    lista_N = []
    indice = 0
    for i in lista:
        if indice % 2 == 0:
            lista_N.append(i*3)
            indice+=1
        else:
            lista_N.append(i*5)
            indice+=1
    return lista_N

def main():
    lista = []
    for i in range(100):
        lista.append(int(input()))
        
    lista.sort()
    nova_L = impar_E_par(lista)
    print(nova_L)
    
if __name__ == "__main__":
    main()