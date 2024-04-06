# função auxiliar onde vai verificar o maior
def max(n1,n2,n3,n4,n5):
    # Maior *******************************************
    if n1 >= n2 and n1 >= n3 and n1 >= n4 and n1 >= n5 :
        return f"O Maior é {n1}\nO Menor é {min(n1,n2,n3,n4,n5)}"
    elif n2 >= n1 and n2 >= n3 and n2 >= n4 and n2 >= n5 :
        return f"O Maior é {n2}\nO Menor é {min(n1,n2,n3,n4,n5)}"
    elif n3 >= n1 and n3 >= n2 and n3 >= n4 and n3 >= n5 :
        return f"O Maior é {n3}\nO Menor é {min(n1,n2,n3,n4,n5)}"
    elif n4 >= n1 and n4 >= n2 and n4 >= n3 and n4 >= n5 :
        return f"O Maior é {n4}\nO Menor é {min(n1,n2,n3,n4,n5)}"
    elif n5 >= n1 and n5 >= n2 and n5 >= n3 and n5 >= n4 :
        return f"O Maior é {n5}\nO Menor é {min(n1,n2,n3,n4,n5)}"
# função auxiliar onde vai verificar o menor   
def min(n1,n2,n3,n4,n5):
    # Menor****************************************
    if n1 <= n2 and n1 <= n3 and n1 <= n4 and n1 <= n5 :
        return f"{n1}"
    elif n2 <= n1 and n2 <= n3 and n2 <= n4 and n2 <= n5 :
        return f"{n2}"
    elif n3 <= n1 and n3 <= n2 and n3 <= n4 and n3 <= n5 :
        return f"{n3}"
    elif n4 <= n1 and n4 <= n2 and n4 <= n3 and n4 <= n5 :
        return f"{n4}"
    elif n5 <= n1 and n5 <= n2 and n5 <= n3 and n5 <= n4 :
        return f"{n5}"
# função principal onde vai ocorrer a entrada, processamento e saída de dados
def main():
    # entrada de dados
    n1 = int(input("Digite o Primeiro Número: "))
    n2 = int(input("Digite o Segundo Número: "))
    n3 = int(input("Digite o Terceiro Número: "))
    n4 = int(input("Digite o Quarto Número: "))
    n5 = int(input("Digite o Quinto Número: "))
    # processamento de dados
    max_min = max(n1,n2,n3,n4,n5)
    # saída de dados
    print(f"{max_min}")
# condição que verifica se o modulo/função e a principal se for vai chamar a função main
if __name__ == "__main__":
    main()