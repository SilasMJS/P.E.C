# função auxiliar onde vai receber 100 numero e verificar qual o maior
def maior():
    maior = 0
    for i in range(1,101):
        # entrada de dados
        num = int(input("Digite um Número: "))
        if num > maior:
            maior = num
    return f"O Número Maior é {maior}"
# função principal
def main():
    # saida de dados
    print(maior())
# condição que verificar se a função/modulo é o principal se for vai chamar a função main 
if __name__ == "__main__":
    main()