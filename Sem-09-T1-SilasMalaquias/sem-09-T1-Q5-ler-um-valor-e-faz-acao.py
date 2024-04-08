# funçao auxiliar onde vai retornar o resultado com base na condição
def calcular(n):
    if n % 5 == 0:
        return (9*n)+7
    elif n % 5 == 1:
        return "par" if n % 2 == 0 else "ímpar"
    elif n % 5 == 2:
        return (5*n**2)-(3*n)+42
    elif n % 5 == 3:
        return n // 10
    else:
        return n ** 2
# função principal onde ocorre a entrada, processamento e saída dedados
def main():
    # entrada de dados
    n = int(input("Digite um Número: "))
    # processamento de dados
    result = calcular(n)
    # saída de dados
    print(f"O resultado é {result}")
# condição que verifica se a função/modulo é o principal se for vai chamar a função main
if __name__ == "__main__":
    main()
    