#Função Auxiliar onde vai ocorrer o processamento de dados sendo focado em um processo especifico
def comparador(caract):
    result = (caract >= "A" and caract <= "Z" or
              caract >= "a" and caract <= "z" or
              caract >= "0" and caract <= "9" )
    return result

#Função Principal onde vai rodar o codigo principal
def main():
    #Variável vai receber o caractere informado pelo usuário
    caract = input().strip()
    #vai ser imprimido para o usuário o resultado 
    print(f'{comparador(caract)}')


if __name__ == '__main__':
    main()