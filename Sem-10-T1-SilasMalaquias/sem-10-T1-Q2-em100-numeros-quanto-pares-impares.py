# função auxiliar que verificar quantos pares e impares existem em 100 números digitados pelo usuario
def pares_impares():
    par = 0
    impar = 0
    for x in range(1,101):
        # entrada de dados
        num = int(input("Digite um Número: "))
        if num % 2 == 0:
            par += 1
        else:
            impar += 1
    return par, impar
# função principal
def main():
    # processamento de dados
    par , impar = pares_impares()
    # saida de dados
    print(f"Nos Números Digitados Existem \nPar: {par}\nÍmpar:{impar}")
# condição que verificar se o modulo/função é o principal se for vai chamar a função main  
if __name__ == "__main__":
    main()