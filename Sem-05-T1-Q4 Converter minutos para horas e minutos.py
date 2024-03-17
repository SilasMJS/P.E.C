#Função Auxiliar vai executar uma tarefa especifica
def hora(m):
    #retorno da Função Auxiliar
    return m//60
#Função Auxiliar vai executar uma tarefa especifica
def minuto(m):
    #Retorno da Função Auxiliar
    return m%60
#Função Principal onde vai ser executado o codigo principal
def main():
    #Variável vai receber o valor informado pelo usuário
    m = int(input("Digite um Valor Inteiro em Minutos: "))
    #vai ser exibido ao usuário o resultado
    print(f"{m} minutos é {hora(m)}:{minuto(m)}")

if __name__ == "__main__":
    main()