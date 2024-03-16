#Função Auxiliar onde vai ocorrer o processamento de dados sendo focado em um processo especifico
def comparador(caract):
    result = (caract == "A" or caract == "B" or caract == "C" or
            caract == "D" or caract == "E" or caract == "F" or
            caract == "G" or caract == "H" or caract == "I" or
            caract == "J" or caract == "K" or caract == "L" or
            caract == "M" or caract == "N" or caract == "O" or
            caract == "P" or caract == "Q" or caract == "R" or
            caract == "S" or caract == "T" or caract == "U" or
            caract == "V" or caract == "W" or caract == "X" or
            caract == "Y" or caract == "Z" or caract == "a" or
            caract == "b" or caract == "c" or caract == "d" or
            caract == "e" or caract == "f" or caract == "g" or
            caract == "h" or caract == "i" or caract == "j" or
            caract == "k" or caract == "l" or caract == "m" or
            caract == "n" or caract == "o" or caract == "p" or
            caract == "q" or caract == "r" or caract == "s" or
            caract == "t" or caract == "u" or caract == "v" or
            caract == "w" or caract == "x" or caract == "y" or
            caract == "z" or caract == "0" or caract == "1" or
            caract == "2" or caract == "3" or caract == "4" or
            caract == "5" or caract == "6" or caract == "7" or
            caract == "8" or caract == "9")
    return result

#Função Principal onde vai rodar o codigo principal
def main():
    #Variável vai receber o caractere informado pelo usuário
    caract = input().strip()
    #vai ser imprimido para o usuário o resultado 
    print(f'{comparador(caract)}')


if __name__ == '__main__':
    main()