#Função Auxiliar onde vai fazer um processamento especifico
def area(l):
    #processamento de dados, operação matemática
    a = l**2
    #retorno da função auxiliar retornando o resultado
    return a
#Função Auxiliar onde o processamento de dados vai ocorrer
def perimetro(l):
    #processamento de dados, operação matemática
    p = l*4
    #retorno da função auxiliar retonando o resultado
    return p
#Função Principal onde fica o codigo principal
def main():
    #A variável vai receber o valor informado pelo usuário
    l = float(input("Digite o Valor do Lado do Quadrado: "))
    #vai imprimir o resultado para o usuário
    print(f"A Área do Quadrado é {area(l):10.4f}\nO Perímetro do Quadrado é{perimetro(l):10.4f}")

if __name__ == "__main__":
    main()