# função auxiliar
def qnt_negat_soma_posit(lista):
    soma = 0
    qnt = 0
    for i in lista: 
        if i >= 0:
            soma += i
        else:
            qnt += 1
    return qnt, soma
# função principal
def main():
    lista = []
    # estrutura de repetição
    for i in range(10):
        # entrada de dados
        n = int(input("Digite um Número: "))
        lista.append(n)
    # processamento de dados
    quant, soma = qnt_negat_soma_posit(lista)
    # saída de dados
    print(f"Lista:\n{lista}\nQuantidade:\n{quant}\nSoma:\n{soma}")
# condição que verifica se a função/modulo é o principal se for vai chamar e executar
if __name__ == "__main__":
    main()