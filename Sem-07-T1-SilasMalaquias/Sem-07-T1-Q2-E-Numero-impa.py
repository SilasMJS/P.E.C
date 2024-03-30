# função auxiliar onde sera executado de preferencia uma tarefa especifica
def e_impa(n):
    # retorno da função retornando o resultado
    return n%2 != 0 
# função principal onde fica o codigo principal
def main():
    # variavel recebendo e armazenando o dado informado pelo usuário
    n = int(input("Digite um Número: "))
    # exibindo na tela o resultado para o usuário
    print(f"O {n} é Ímpar? R = {e_impa(n)}")
# condição que verifica se a função/modulo é o principal se for vai chamar e executar a função main
if __name__ == "__main__":
    # chamando a função main
    main()