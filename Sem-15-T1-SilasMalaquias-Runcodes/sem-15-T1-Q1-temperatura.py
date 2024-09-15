def converter_celsius(f):
    return (f-32)*5/9
def converter_fahrenheit(c):
    return (c*9/5)+32

def maior_temp(temp1, temp2):
    valor1, escala1 = temp1
    valor2, escala2 = temp2
    
    
    if escala1 == escala2:
        return temp1 if valor1 > valor2 else temp2
    if escala1 == "C" and escala2 == "F":
        v2_celsius = converter_celsius(valor2)
        return temp1 if valor1 > v2_celsius else (valor2, escala2)
    elif escala1 == "F" and escala2 == "C":
        v1_celsius = converter_celsius(valor1)
        return (valor1, escala1) if v1_celsius > valor2 else temp2
    
def main():
    valor1 = float(input())
    escala1 = input().strip().upper()[0]
    temp1 = valor1, escala1
    valor2 = float(input())
    escala2 = input().strip().upper()[0]
    temp2 = valor2, escala2
    
    print(maior_temp(temp1, temp2))
    
if __name__ == "__main__":
    main()