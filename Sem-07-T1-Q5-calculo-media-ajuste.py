# função auxiliar onde sera executado de preferencia uma tarefa especifica
def media(n1, n2, n3):
    # condição se for verdadeira vai ser executado o bloco contido nela
    if n3 > 8:
        # condição se for verdadeira vai ser executado o bloco contido nela
        if ((n1+n2+n3)/3)+1 > 10:
            # variavel recebendo um valor inteiro
            media = 10
            # retorno, retornando o resultado
            return media
        # se não entrar na condição acima ira executar o bloco contido nela
        else:
            # retorno, retonando o resultado
            return ((n1+n2+n3)/3)+1
    # se não entrar na condição acima ira executar o bloco contido nela
    else:
        # retorno, retornando o resultado
        return (n1+n2+n3)/3
# função principal onde fica contido o codigo principal
def main():
    # variável recebendo e armazenando o dado informado pelo usuário
    n1 = float(input("Digite a Primeira Nota: "))
    # variável recebendo e armazenando o dado informado pelo usuário
    n2 = float(input("Digite a Segunda Nota: "))
    # variável recebendo e armazenando o dado informado pelo usuário  
    n3 = float(input("Digite a Terceira Nota: "))
    # exibindo o resultado na tela do usuário
    print(f"Sua Média Final é {media(n1, n2, n3):.2f}")
# condição que verificar se a função/modulo é o principal se for vai chamar e executar a função main
if __name__ == "__main__":
    # chamando a função main
    main()