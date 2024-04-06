# função auxiliar somando os digitos
def soma_digitos(n):
    cm = n//100000%10
    dm = n//10000%10
    um = n//1000%10
    c = n//100%10
    d = n//10%10
    u = n//1%10
    return cm + dm + um + c + d + u
# função auxiliar verificando digitos permitidos
def digitos_permitidos(n):
    if n > 0 and n < 100000:
        return soma_digitos(n)
    return -1
# função principal onde vai ocorrer a entrada, processamento e saída de dado
def main():
    # entrada de dado
    n = int(input("Digite os Digitos entre 0 a 100000: "))
    # processamento de dado
    soma = digitos_permitidos(n)
    # saída de dado
    print(f"A Soma do Digitos é {soma}")
#  condição que verifica se a função/modulo é a principal se for vai chamar e executar a função main
if __name__ == "__main__":
    main()