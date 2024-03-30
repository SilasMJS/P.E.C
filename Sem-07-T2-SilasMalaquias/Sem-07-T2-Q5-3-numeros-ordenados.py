# função auxiliar onde sera executado de preferencia uma tarefa especifica
def crescente(n,n2,n3):
    # condição se for verdadeira vai executar o bloco contido nela
    if n >= n2:
        # condição se for verdadeira vai executar o bloco contido nela
        if n2 >= n3:
            # retornando o resultado
            return (f"{n3}, {n2}, {n}")
        # retornando o resultado
        return (f"{n2}, {n3}, {n}")
    # se a condição de cima for falsa verifica se essa é verdadeira se for vai executar o bloco contido nela
    elif n2 >= n3:
        # condição se for verdadeira vai executar o bloco contido nela
        if n3 >= n:
            # retornando o resultado
            return (f"{n}, {n3}, {n2}")
        # retornando o resultado 
        return (f"{n3}, {n}, {n2}")
    # retornando o resultado
    return (f"{n}, {n2}, {n3}")   
# função principal onde fica o codigo principal
def main():
    # a variável vai receber e armazenar o dado informado pelo usuário
    n = int(input("Digite o Primeiro Número: "))
    # a variável vai receber e armazenar o dado informado pelo usuário
    n2 = int(input("Digite o Segundo Número: "))
    # a variável vai receber e armazenar o dado informado pelo usuário
    n3 = int(input("Digite o Terceiro Número: "))
    # vai ser exibido na tela do usuário o resultado
    print(f"A ordem Crescente dos Números {n,n2,n3} é {crescente(n,n2,n3)}")
# condição que verificar se a função/modulo é o principal se for vai chamar e executar a função main   
if __name__ == "__main__":
    # chamando a função main
    main()