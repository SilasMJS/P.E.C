# função auxiliar
def converter_celsius(f):
    return (f-32)*5/9
# função auxiliar
def converter_fahrenheit(c):
    return (c*9/5)+32
# função auxiliar
def somar_Temp(temp1, temp2):
    g1, e1 = temp1
    g2, e2 = temp2
    # estrutura de condição
    if e1 == e2:
        return float(f"{(g1 + g2):.4f}"), e2
    if e1 == 'C' and e2 == 'F':
        n_g1 = converter_fahrenheit(g1)
        soma = g1 + n_g1
        return float(f"{soma:.4f}"), e2
    elif e1 == 'F' and e2 == 'C':
        n_g1 = converter_celsius(g1)
        soma = g1 + n_g1
        return float(f"{soma:.4f}"), e2
# função principal
def main():
    # entrada de dados
    grau_1 = float(input("Digite o Primeiro Grau: "))
    escala_1 = input("Digite a Escala (C) ou (F): ").strip().upper()[0]
    temp1 = grau_1, escala_1
    # entrada de dados
    grau_2 = float(input("Digite o Segundo Grau: "))
    escala_2 = input("Digite a Escala (C) ou (F): ").strip().upper()[0]
    temp2 = grau_2, escala_2
    # processamento de dados
    temperatura = somar_Temp(temp1, temp2)
    # saída de dados
    print(f"Soma das Temperaturas: {temperatura}")
# condição que verificar se a função/modulo é o principal se for vai chamar e executar
if __name__ == "__main__":
    main()