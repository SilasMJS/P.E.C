# função auxiliar onde vai retornado o resultado com base na condição
def quadrado_ou_retangulo(base,altura):
    if base == altura:
        return "QUADRADO"
    else:
        perimetro = 2*(base+altura)
        area = base*altura
        return f"{perimetro:.0f} - {area:.0f}"
# função principal onde vai ocorrer a entrada, processamento e saída de dados
def main():
    # entrada de dados
    base = float(input("Digite o Valor da Base: "))
    altura = float(input("Digite o Valor da Altura: "))
    # processamento de dados
    verificar = quadrado_ou_retangulo(base,altura)
    # saída de dados
    print(f"O Resultado é {verificar}")
# condição que verifica se a função/modulo é o principal se for vai chamar a função main
if __name__ == "__main__":
    main()