# função auxiliar soma elementos primeira linha
def somando(matriz):
    return sum(matriz[0])
# função auxiliar soma elementos ultima coluna
def ult_col_soma(matriz):
    n = len(matriz)
    m = len(matriz[0])
    return sum(matriz[i][m-1] for i in range(n))
# função auxiliar media total de todos elementos
def media(matriz):
    total = len(matriz)*len(matriz[0])
    soma = sum(sum(l) for l in matriz)
    m = round(soma/total,4)
    return m
# função auxiliar menor elemento
def menor(matriz):
    return min(min(l) for l in matriz)
# função auxiliar maior elemento
def maior(matriz):
    return max(max(l) for l in matriz)
# função principal
def main():
    matriz = []
    # entrada de dados
    n = int(input("Digite a Quantidade de Linhas: "))
    m = int(input("Digite a Quantidade de Colunas: "))
    # criando matriz
    for i in range(n):
        l = []
        for j in range(m):
            l.append(int(input()))
        matriz.append(l)
    # processamento de dados
    soma = somando(matriz)
    col_s =ult_col_soma(matriz)
    me_dia = media(matriz)
    min = menor(matriz)
    max = maior(matriz)
    result = soma, col_s, me_dia, min, max
    # saída de dados
    print(result)
# condição que verifica se a função/modulo é o principal se for vai chamar e executar
if __name__ == "__main__":
    main()