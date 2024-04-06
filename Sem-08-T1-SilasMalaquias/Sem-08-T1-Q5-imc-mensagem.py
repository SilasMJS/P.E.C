# função auxiliar retornando o resultado da expressão matematica do imc
def calculo_imc(peso,altura):
    return peso / (altura**2)
# função principal onde ocorre a entrada, processamento e saída de dados
def main():
    # entrada de dados
    peso = float(input("Digite seu Peso: "))
    altura = float(input("Digite Sua Altura: "))
    # processamento de dados
    imc = calculo_imc(peso,altura)
    # saída de dados
    print(f"IMC: {imc:.2f}")
    if imc < 18.5: print("Abaixo do peso")
    elif imc < 25: print("Peso normal")
    elif imc < 30: print("Sobrepeso")
    elif imc < 35: print("Obeso leve")
    elif imc < 40: print("Obeso moderado")
    else: print("Obeso mórbido")
# condição que verifica se a função/modulo é o principal se for vai chamar a função main  
if __name__ == "__main__":
    main()