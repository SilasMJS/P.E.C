# função auxiliar  realizando a adição
def adicao(n1,n2):
    return n1+n2
# função auxiliar realizando a subtração
def subtracao(n1,n2):
    return n1-n2
# função auxiliar realizando a multiplicação
def multipli(n1,n2):
    return n1*n2
# função auxiliar realizando a divisão
def divisao(n1,n2):
    return n1/n2
# função auxiliar retornando o resultado com base na condição
def ope_aritmetica(n1,n2,opc):
    if opc == 1: return adicao(n1,n2)
    elif opc == 2: return subtracao(n1,n2)
    elif opc == 3: return multipli(n1,n2)
    elif opc == 4: return divisao(n1,n2)
    else: raise ValueError ("Você Digitou a Opção Incorreta!")
# função principal onde ocorre a entrada, processamento e saída de dados
def main():
    # entrada de dados
    n1 = float(input("Digite o Primeiro Número: "))
    n2 = float(input("Digite o Segundo Número: "))
    opc = int(input("Digite:\n1- Adição\n2- Subtração\n3- Multiplicação\n4- Divisão\n"))
    # processamento de dados
    resultado = ope_aritmetica(n1,n2,opc)
    # saída de dados
    print(f"O Resultado é {resultado}")
# condição que verifica se a função/modulo é o principal se for vai chamar a função main
if __name__ == "__main__":
    main()