#Função Auxiliar onde vai ocorrer o processamento de dados ou operações com uma função especificar
def comparador(caract):
    result = not(caract >= "A" and caract <= "Z" or
              caract >= "a" and caract <= "z" or
              caract >= "0" and caract <= "9")
    return result
#Função Principal onde o codigo principal vai rodar
def main():
    #a variável vai receber o caractere informado pelo usuário
    caract = input().strip()
    #vai ser imprimido na tela o resultado para o usuário
    print(f"{comparador(caract)}")

if __name__ == '__main__':
    main() 