# função auxiliar onde de preferencia sera executado uma tarefa especifica
def transito(cor):
    # condição se for verdadeira vai executar o bloco contido nela
    if cor == "V":
        # retorno da função retornando o resultado
        return "Siga!"
    # condição se for verdadeira vai executar o bloco contido nela
    elif cor == "A":
        # retorno da função retornando o resultado
        return "Atenção!"
    # condição se for verdadeira vai executar o bloco contido nela
    elif cor == "E":
        # retorno da função retornando o resultado
        return "Pare!"
    # retorno da função retorno o resultado
    return "Essa Resposta não Corresponde as cores do Sinal"
# frunção principal onde fica o codigo principal
def main():
    # variável recebendo e armazenando o dado informado pelo usuário
    cor = input("""Digite a Letra correspondente do sinal de Trânsito;
(V)-Verde
(A)-Amarelo
(E)-Vermelho\n""").upper()
    # exibindo na tela o resultado para o usuário
    print(f"{transito(cor)}")
# condição que verificar se a função/modulo é o principal se for vai chamar e executar a função main
if __name__ == "__main__":
    # chamando a função main
    main()