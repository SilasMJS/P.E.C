# função auxiliar onde sera executado de preferencia uma tarefa especifica
def conjuge():
    # a variável vai receber e armazenar o dado informado pelo usuário
    conjugue = input("Digite o Nome do seu Cônjugue: ").strip()
    # retorno, retornando o resultado
    return conjugue
# função auxiliar onde sera executado de preferencia uma tarefa especifica
def solteiro_ou_casado(nome,opc):
    # condição se for verdadeiro vai ser executado o bloco contido nela
    if opc == 1:
        # retornando o resultado
        return len(nome)+len(conjuge())
    # se não entra na condição acima ira executar esse bloco de comando 
    return len(nome)
# função principal onde o codigo principal fica
def main():
    # a varável vai receber e armazenar o dado informado pelo usuário
    nome = input("Digite Seu Nome: ").strip()
    # a variável vai receber e armazenar o dado informado pelo usuário
    opc = int(input("Estado Civil:\n(1)-Casado\n(2)-Solteiro\n"))
    # exibindo o resultado na tela do usuário
    print(f"A Quantidade de Caractere no nome é {solteiro_ou_casado(nome,opc)}")
# condição que verificar se a função/modulo é o principal se for vai chamar e executar a função main
if __name__ == "__main__":
    # chamando a função main
    main()