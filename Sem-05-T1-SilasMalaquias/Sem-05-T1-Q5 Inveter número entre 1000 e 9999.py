#Função Auxiliar onde vai ser executado uma tarefa especifica
def inverter(n):
    #Convertendo de inteiro para string
    n = str(n)
    #Retorno da Função
    return n[3::-1]
#Função Principal onde o codigo Principal vai ser executado
def main():
    #Variável vai receber valor informado pelo usuário
    n = int(input("Digite Um Número inteiro entre 1000 e 9999: "))
    #vai ser exibido para o usuário o resultado
    print(f"O Número informado é {n}\nO Número Invertido é {inverter(n)}")

if __name__ == "__main__":
    main()