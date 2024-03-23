# função auxiliar onde sera executada de preferencia uma tarefa especifica
def numero_proximo(n):
    # retorno da função retornando o resultado
    return round(n)
# função principal onde se encontra o codigo principal
def main():
    # entrada de dados onde sera armazenado na variável o dado informado pelo usuário
    n = float(input("Digite um Valor Real: "))
    # saida de dados onde sera exibido na tela o resultado
    print(f"O Número Mais Próximo é {numero_proximo(n)}")
# condição que verificar se o modulo/função é o principal se for sera chamado e executado
if __name__ == "__main__":
    # chamando a função main
    main()