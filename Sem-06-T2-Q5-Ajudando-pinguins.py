# função auxiliar executando de preferencia uma tarefa especifica
def fahrenheit(celsius):
    # retorno da função retornando o resultado
    return (celsius*(9/5))+32
# função principal onde esta localizado o codigo principal
def main():
    # entrada de dados onde sera armazenado na variável o dado informado pelo usuário
    celsius = float(input("Digite os Graus em Celsius: "))
    # saida de dados onde sera exibido o resultado na tela do usuário
    print(f"{celsius}°C é {fahrenheit(celsius):.2f}°F")
# condição que verificar se a função/modulo é o principal se for a função sera chamada e executada
if __name__ == "__main__":
    # chamando a função main
    main()