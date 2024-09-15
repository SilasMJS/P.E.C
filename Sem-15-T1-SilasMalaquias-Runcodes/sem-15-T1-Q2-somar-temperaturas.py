def converter_celsius(f):
    return (f-32)*5/9
def converter_fahrenheit(c):
    return (c*9/5)+32

def soma_temp(temp1, temp2):
    valor1, escala1 = temp1
    valor2, escala2 = temp2
    
    
    if escala1 == escala2:
        soma = valor1 + valor2
        return float(f"{soma:.4f}"), escala1
    if escala1 == "C" and escala2 == "F":
        valor1_convertido = converter_fahrenheit(valor1)  
        soma = valor1_convertido + valor2
        return float(f"{soma:.4f}"), escala2
    elif escala1 == "F" and escala2 == "C":
        valor1_convertido = converter_celsius(valor1)  
        soma = valor1_convertido + valor2
        return float(f"{soma:.4f}"), escala2
    
def main():
    valor1 = float(input())
    escala1 = input().strip().upper()[0]
    temp1 = valor1, escala1
    valor2 = float(input())
    escala2 = input().strip().upper()[0]
    temp2 = valor2, escala2
    
    print(soma_temp(temp1, temp2))
    
if __name__ == "__main__":
    main()