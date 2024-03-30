# função auxiliar onde vai ser executada de preferencia uma tarefa especifica
def comparador(caracter):
    # condição se for verdadeira vai executar o bloco contido nela
    if caracter == "A" or caracter == "E" or caracter == "I" or caracter == "O" or caracter == "U":
        # retorno, retornando o resultado
        return "vogal"
    # condição se a de cima não for verdadeira e essa for vai ser executado o bloco contido nela
    elif caracter >= "B" and caracter <= "D" or caracter >= "F" and caracter <= "H" or  caracter >= "j" and caracter <= "N" or caracter >= "P" and caracter <= "T" or caracter >= "V" and caracter <= "Z":
        # retorno, retornando o resultado
        return "consoante"
    #  condição se as condições acima não forem verdadeiras e essa for vai executar o bloco contido nela
    elif caracter >= "0" and caracter <= "9":
        # retorno, retornando o resultado
        return "número"
    # condição se não executar nenhuma acima ira executar o bloco contido 
    else:
        # retorno, retornando o resultado
        return "símbolo"
#  função principal onde esta contido o codigo principal
def main():
    # a variável vai receber e armazenar o dado informado pelo usuário
    caracter = input("Digite um Caractere: ").upper()
    # vai ser exibido na telo do usuário o resultado
    print(f"O Caractere ({caracter}) é um(a) {comparador(caracter)}")
# condição que verifica se a função/modulo é o principal se for vai chamar a função main e executar
if __name__ == "__main__":
    # chamando a função main
    main()