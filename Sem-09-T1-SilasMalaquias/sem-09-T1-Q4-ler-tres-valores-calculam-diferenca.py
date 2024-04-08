# função auxiliar onde vai retornar o resultado com base na condição
def diferenca(n1,n2,n3):
    dif2 = abs(n1-n2)
    dif3 = abs(n1-n3)
    if dif2 < dif3: return f"{dif2}"
    elif dif3 < dif2: return f"{dif3}"
    else: return f"{dif2}"
# função principal onde vai ocorrer a entrada, processamento e saída de dados
def main():
    # entrada de dados
    n1 = int(input("Digite o Primeiro Número: "))
    n3 = int(input("Digite o Segundo Número: "))
    n2 = int(input("Digite o Terceiro Número: "))
    # processamento de dados
    dif = diferenca(n1,n2,n3)
    # saída de dados
    print(f"A Menor Diferença é {dif}")
# condição que verifica se a função/modulo é o principal se for vai chamar a função main
if __name__ == "__main__":
    main()
    