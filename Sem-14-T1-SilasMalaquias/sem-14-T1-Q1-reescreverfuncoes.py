from random import *
def comprimento(lista):
    c = 0
    for i in lista:
        c +=1
    return c

def inverter(lista):
    lista_nova = []
    for i in range(comprimento(lista)):
        lista_nova.insert(0,lista[i])

    return lista_nova

def minimo(lista):
    menor = 999999
    for i in lista:
        if i < menor:
            menor = i
    return menor

def maximo(lista):
    maior = 0
    for i in lista:
        if i > maior:
            maior = i
    return maior

def soma(lista):
    soma = 0
    for i in lista:
        soma += i
    return soma

def main():
    lista = []

    while True:
        num = int(input())
        if num != 0:
            lista.append(num)
        else:
            break
        
    print(lista)
    print(comprimento(lista))
    print(inverter(lista))
    print(minimo(lista))
    print(maximo(lista))
    print(soma(lista))

if __name__ == "__main__":
    main()