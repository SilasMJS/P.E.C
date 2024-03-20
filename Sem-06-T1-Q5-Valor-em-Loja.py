def a_vista(valor):
    return valor - (valor*(9/100))
def parce_5(valor):
    return valor/5
def parce_10(valor):
    return (valor + (valor*(17/100)))/10


def main():
    valor = float(input())
    print(f"{a_vista(valor):.2f}\n{parce_5(valor):.2f}\n{parce_10(valor):.2f}")
if __name__ == "__main__":
    main()