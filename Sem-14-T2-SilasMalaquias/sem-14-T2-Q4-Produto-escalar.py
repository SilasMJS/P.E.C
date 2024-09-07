# função auxiliar
def produto_escalar(lista_X, lista_Y):
    produto = 0
    for i in range(5):
        produto += (lista_X[i] * lista_Y[i])
    return produto
# função principal
def main():
    lista_X = []
    lista_Y = []
    # estrutura de repetição
    for i in range(5):
        # entrada de dados
        x = int(input("Digite um Número: "))
        lista_X.append(x)
    for i in range(5):
        # entrada de dados
        y = int(input("Digite um Número: "))
        lista_Y.append(y)
    # processamento de dados
    produto = produto_escalar(lista_X,lista_Y)
    # saída de dados
    print(f"Lista X:\n{lista_X}")
    print(f"Lista Y:\n{lista_Y}")
    print("Equação:")
    print(f"({lista_X[0]} x {lista_Y[0]}) + ({lista_X[1]} x {lista_Y[1]}) + ({lista_X[2]} x {lista_Y[2]}) + ({lista_X[3]} x {lista_Y[3]}) + ({lista_X[4]} x {lista_Y[4]}) = {produto}")
# condição que verificar se a função/modulo é o principal se for vai chamar e executar
if __name__ == "__main__":
    main()