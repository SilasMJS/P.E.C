# função auxiliar
def comprimento(lista):
    c = 0
    for i in lista:
        c +=1
    return c
# função auxiliar
def inverter(lista):
    lista_nova = []
    for i in range(comprimento(lista)):
        lista_nova.insert(0,lista[i])
    return lista_nova
# função auxiliar
def minimo(lista):
    menor = 999999
    for i in lista:
        if i < menor:
            menor = i
    return menor
# função auxiliar
def maximo(lista):
    maior = 0
    for i in lista:
        if i > maior:
            maior = i
    return maior
# função auxiliar
def soma(lista):
    soma = 0
    for i in lista:
        soma += i
    return soma
# função principal
def main():
    lista = []
    while True:
        # entrada de dados
        num = int(input("Digite um Número: "))
        if num != 0:
            lista.append(num)
        else:
            break
    # saída de dados
    print(f"Lista dos Números:\n{lista}")
    print(f"Comprimento da Lista:\n{comprimento(lista)}")
    print(f"Lista Invertida:\n{inverter(lista)}")
    print(f"Menor Número da Lista:\n{minimo(lista)}")
    print(f"Maior Número da Lista:\n{maximo(lista)}")
    print(f"Soma dos Número da Lista:\n{soma(lista)}")
# condição que verificar se a função/modulo é o principal se for vai chamar e executar
if __name__ == "__main__":
    main()