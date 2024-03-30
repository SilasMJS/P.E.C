# função auxiliar onde sera executado de preferencia uma tarefa especifica
def qnts_impar(n):
    # condição se for verdadeira ira executado o bloco contido nela
    if n == 0:
        # retornando o resultado
        return "Nenhum dígito é ímpar."
    # se a condição não entra vai verificar se essa condição é verdadeira se for vai executar o bloco contido
    elif n == 1:
        # retornando o resultado
        return "Apenas um dígito é ímpar."
    # retornando o resultado
    return "Os dois dígitos são ímpares."
# função auxiliar onde sera executado de preferencia uma tarefa especifica
def e_impar(n):
    # a variável vai receber e armazenar o valor de outra variável do tipo inteiro
    n_str = str(n)
    # inicializando uma variável com o valor 0
    contador_impar = 0
     # vai percorrer o vetor armazenando 1 caractere por vez
    for digito in n_str:
        # a variável vai receber e armazenar o valor de outra variável do tipo inteiro
        n_int = int(digito)
        # condição se a condição for verdadeira vai executar o bloco contido nela
        if n_int % 2 == 1:
            # a variável inicializada vai receber o valor de 1
            contador_impar += 1
    # retornando o resultado
    return qnts_impar(contador_impar)
# função principal onde fica o codigo principal
def main():
    # variável vai receber e armazenar o dado informado pelo usuário
    n = int(input("Digite um Número entre (10 a 99): "))  
    # vai ser exibido na tela do usuário o resultado
    print(f"{e_impar(n)}")  
# condição que verifica se a função/modulo é o principal se for vai chamar e executar a função main 
if __name__ == "__main__":
    # chamando a função main
    main()