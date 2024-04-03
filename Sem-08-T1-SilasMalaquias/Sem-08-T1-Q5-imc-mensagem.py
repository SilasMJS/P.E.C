def calculo_imc(peso,altura):
    return peso / (altura**2)

def main():
    peso = float(input())
    altura = float(input())
    
    imc = calculo_imc(peso,altura)
    print(f"{imc:.2f}")
    if imc < 18.5: print("Abaixo do peso")
    elif imc < 25: print("Peso normal")
    elif imc < 30: print("Sobrepeso")
    elif imc < 35: print("Obeso leve")
    elif imc < 40: print("Obeso moderado")
    else: print("Obeso mórbido")
    
if __name__ == "__main__":
    main()