# função auxiliar
def inverter(n):
    n_invertido = 0
    while n > 0:
        digito = n % 10
        n_invertido = (n_invertido * 10) + digito
        n //= 10
    return f"Invertido Fica assim {n_invertido}."
# função principal
def main():
    # entrada de dados
    n = int(input("Digite um Número Inteiro: "))
    # saida de dados
    print(f"O Número {n} "+inverter(n))
# condição que verificar se a função/modulo é o principal se for vai chamar e executar  
if __name__ == "__main__":
    main()