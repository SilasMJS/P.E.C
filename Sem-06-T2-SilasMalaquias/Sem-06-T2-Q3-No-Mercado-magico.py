# função auxiliar onde sera executada de preferencia uma tarefa especifica
def macas(prc_macas):
    #retorno da função retornando o resultado da função 
    return prc_macas*3
# função auxiliar onde sera executada de preferencia uma tarefa especifica
def bananas(prc_bananas):
    #retorno da função retornando o resultado da função    
    return (prc_bananas*2)
# função principal onde se encontra o codigo principal
def main():
    #entrada de dado onde sera armazenado na variável o dado informado pelo usuário 
    prc_macas = float(input("Digite o Preço da Maça: "))
    #entrada de dado onde sera armazenado na variável o dado informado pelo usuário 
    prc_bananas = float(input("Digite o Preço da Banana: "))
    # armazenando na variavel o resultado da operação matemática do resultado da função
    prc_total = macas(prc_macas)+bananas(prc_bananas)
    # saida de dados exibindo na telo do usuário o resultado
    print(f"O Preço Total é {prc_total:.2f}")
# condição que verifica se a função/modulo é o principal se for sera chamado e executado
if __name__ == "__main__":
    # chamando a função main
    main()