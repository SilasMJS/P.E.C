def adicao(n1,n2):
    return n1+n2
def subtracao(n1,n2):
    return n1-n2
def multipli(n1,n2):
    return n1*n2
def divisao(n1,n2):
    return n1/n2

def ope_aritmetica(n1,n2,opc):
    if opc == 1: return adicao(n1,n2)
    elif opc == 2: return subtracao(n1,n2)
    elif opc == 3: return multipli(n1,n2)
    elif opc == 4: return divisao(n1,n2)
    else: raise ValueError ("Você Digitou a Opção Incorreta!")


def main():
    n1 = float(input())
    n2 = float(input())
    opc = int(input())
    
    resultado = ope_aritmetica(n1,n2,opc)
    
    print(f"{resultado}")
    


if __name__ == "__main__":
    main()