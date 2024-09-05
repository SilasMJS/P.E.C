def maior_element_posicao(lista):
    maior = 0
    posicao = 0
    for i in range(len(lista)):
        if lista[i] > maior:
            maior = lista[i]
            posicao = i
    return maior, posicao
def main():
    lista = []
    for i in range(10):
        n = int(input())
        lista.append(n)
    maior, posicao = maior_element_posicao(lista)
    print(f"{lista}\n{maior}\n{posicao}")
    
    
if __name__ == "__main__":
    main()