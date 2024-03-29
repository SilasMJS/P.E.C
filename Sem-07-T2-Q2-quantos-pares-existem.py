# função auxiliar onde vai ser executado uma tarefa especifica
def contador_pares(n):
    # a sequencia de numero sera convertida em caracteres
    n_str = str(n)
    # criando variável contadora para armazenar
    contador_pares = 0
    # vai percorrer o vetor armazenando 1 caractere por vez
    for digito in n_str:
        # o caractere vai ser armazenado na variável
        digito_int = int(digito)
        # se acondição for verdadeira sera executado o codigo a seguir
        if digito_int % 2 == 0:
            # a variável vai receber +1
            contador_pares+=1
    # retorno da função retornando o resultado
    return contador_pares
# função principal onde fica condido o codigo principal
def main():
    # armazena um dado na variável informado pelo usuário
    n = int(input())
    # exibi o resultado na tela para o usuário
    print(f"{contador_pares(n)}")
#condição que verificar se a função/modulo é o principal se for a função sera chamada e executada 
if __name__ == "__main__":
    main()

