# função principal
def main():
    lista = []
    impar = []
    par = []
    # estrutura de repetição
    for i in range(20):
        # entrada de dados
        n = int(input())
        lista.append(n)
        # estrutura de condição
        if n % 2 == 0:
            par.append(n)
        else:
            impar.append(n)
    # saída de dados
    print(lista)
    print(par)
    print(impar)
# condição que verificar se a função/modulo é o principal de for vai chamar e executar
if __name__ == "__main__":
    main()