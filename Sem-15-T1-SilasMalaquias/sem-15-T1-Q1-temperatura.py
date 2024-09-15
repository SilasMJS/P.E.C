def converter_celsius(f):
    return (f-32)*5/9
def converter_fahrenheit(c):
    return (c*9/5)+32

def temp_Maior(temp1, temp2):
    g1, e1 = temp1
    g2, e2 = temp2
    
    if e1 == e2:
        return temp1 if g1 > g2 else temp2
    if e1 == 'C' and e2 == 'F':
        n_g2 = converter_celsius(g2)
        return temp1 if g1 > n_g2 else temp2
    elif e1 == 'F' and e2 == 'C':
        n_g2 = converter_fahrenheit(g2)
        return temp1 if g1 > n_g2 else temp2
    

def main():
    grau_1 = float(input("Digite o Primeiro Grau: "))
    escala_1 = input("Digite a Escala (C) ou (F): ").strip().upper()[0]
    temp1 = grau_1, escala_1
    grau_2 = float(input("Digite o Segundo Grau: "))
    escala_2 = input("Digite a Escala (C) ou (F): ").strip().upper()[0]
    temp2 = grau_2, escala_2
    temperatura = temp_Maior(temp1, temp2)
    print(temperatura)
    
    
if __name__ == "__main__":
    main()