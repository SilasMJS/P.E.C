# função auxiliar
def maior_element_posicao(lista):
    maior = 0
    posicao = 0
    for i in range(len(lista)):
        if lista[i] > maior:
            maior = lista[i]
            posicao = i
    return maior, posicao
# função principal
def main():
    lista = []
    # estrutura de repetição
    for i in range(10):
        # entrada de dados
        n = int(input("Digite um Número: "))
        lista.append(n)
    # processamento de dados
    maior, posicao = maior_element_posicao(lista)
    # saída de dados
    print(f"Lista:\n{lista}\nMaior:\n{maior}\nPosição:\n{posicao}")
# condição que verificar se a função/modulo é o principal se for vai chamar e executar
if __name__ == "__main__":
    main()