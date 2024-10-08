# função auxiliar
def menor_maior(matriz):
    n = len(matriz)
    maior = menor = matriz[0][0]
    pos_maior = pos_menor = (0,0)
    # estrutura de repetição
    for i in range(n):
        for j in range(n):
            if matriz[i][j] > maior:
                maior = matriz[i][j]
                pos_maior = i,j
            if matriz[i][j] < menor:
                menor = matriz[i][j]
                pos_menor = i,j
    return pos_maior, pos_menor
# função principal
def main():
    matriz = []
    # entrada de dados
    n = int(input("Digite um Número para definir a Matriz: "))
    # estrutura de repetição
    for i in range(n):
        l = []
        for col in range(n):
            l.append(int(input("Digite um Elemento para Adicionar: ")))
        matriz.append(l)
    # processamento de dados
    p_maior, p_menor = menor_maior(matriz)
    # saida de dados
    print(f"O Maior: {p_maior}\nO Menor: {p_menor}")
# condição que verifica se a função/modulo é o principal se for vai chamar e executar
if __name__ == "__main__":
    main()