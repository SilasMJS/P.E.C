#Função Auxiliar onde é aconcelhavel executar uma tarefa especifica
def calcular(a, b, c):
    #retorno da função
    return 2*a+5*b-c
#função Principal onde fica o codigo principal
def main():
    #a variável vai receber um valor inteiro
    a = int(input("Digite o Primeiro Valor Inteiro:"))
    #a variável vai receber um valor inteiro
    b = int(input("Digite o Segundo Valor Inteiro:"))
    #a variável vai receber um valor inteiro
    c = int(input("Digite o Terceiro Valor Inteiro:"))
    #vai ser exibido na telo o resultado
    print(f"O Resultado é {calcular(a, b, c,)}")

if __name__ == "__main__":
    main()