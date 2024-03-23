# Função auxiliar onde de preferencia sera executado uma so tarefa especifica
def a_vista(valor):
    # retorno da função onde esta retornando o resultado da função
    return valor - (valor*(9/100))
# Função auxiliar onde de preferencia sera executado uma so tarefa especifica
def parce_5(valor):
    # retorno da função onde esta retornando o resultado da função
    return valor/5
# Função auxiliar onde de preferencia sera executado uma so tarefa especifica
def parce_10(valor):
    # retorno da função onde esta retornando o resultado da função
    return (valor + (valor*(17/100)))/10
# função principal onde esta o codigo principal que sera executado
def main():
    # entrada de dado e onde vai ser armazendado na variável o dado informado pelo usuário
    valor = float(input("Digite o Valor da Compra: "))
    # saida de dados onde sera exibido o resultado na tela para o usuário
    print(f"Valor à Vista: {a_vista(valor):.2f}\nValor Parcelado em 5x: {parce_5(valor):.2f}\nValor Parcelado em 10x: {parce_10(valor):.2f}")
# condição que verifica se a função/modulo é o principal se for sera chamado a função principal e executada
if __name__ == "__main__":
    # chamando a função main
    main()