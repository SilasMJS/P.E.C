#Função auxiliar onde vai ocorrer o processamente de dados especifico
def identficador_letra(letra):
    letra = (letra >= "A" and letra <= "Z" or
             letra >= "a" and letra <= "z")
    #retorno do resultado da função
    return letra
#função Principal onde fica o codigo principal
def main():
    #a Variável vai receber um caractere
    letra = input("Digite uma Letra: ").strip()
    #Vai ser exibido pro cliente o resultado
    print(f"É Letra? {identficador_letra(letra)}")


if __name__ == '__main__':
    main()