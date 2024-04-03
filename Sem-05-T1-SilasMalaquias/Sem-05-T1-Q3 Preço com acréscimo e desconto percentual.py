#Função Auxiliar onde vai ser executado so uma tarefa especifica
def atualizado(p,d):
    #Retorno da função 
    return p + (p*(d/100))
#Função Auxiliar onde vai ser executado so uma tarefa especifica
def desconto(p,d):
    #Retorno da Função
    return p - (p*(d/100))
#Função Principal onde vai ser executado o codigo principal
def main():
    #variável vai receber valor real informado pelo usuário
    p = float(input("Informe o Preço: "))
    #variável vai receber valor real informado pelo usuário
    d = float(input("Informe o Percentual: "))
    #vai ser exibido para o usuário o resultado
    print(f"O Preço com Aumento Percentual é {atualizado(p,d):.2f}\nO Preço com Desconto Percentual é {desconto(p,d):.2f}")

if __name__ == "__main__":
    main()