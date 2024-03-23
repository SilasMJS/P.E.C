# função auxiliar onde sera executada de preferencia uma tarefa especifica
def idade_espacial(anos):
    # retorno da função retornando o resultado
    return anos//2
# função principal onde esta o codigo principal
def main():
    # entrada de dados onde sera armazenada o dado informado pelo usuário
    anos = int(input("Digite Sua Idade: "))
    # saida de dados onde sera exibido o resultado na tela do usuário
    print(f"Sua Idade em Anos Espaciais é {idade_espacial(anos)}")
# condição que verifica se a função/modulo é o principal se for sera chamado e executado
if __name__ == "__main__":
    # chamando a função main
    main()