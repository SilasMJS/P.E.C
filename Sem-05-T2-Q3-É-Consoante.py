#Função Auxiliar onde vai processar uma tarefa especifica
def consoante(consoant):
    result = (consoant >= "B" and consoant <= "D" or 
    consoant >= "F" and consoant <= "H" or 
    consoant >= "j" and consoant <= "N" or
    consoant >= "P" and consoant <= "T" or
    consoant >= "V" and consoant <= "Z" or
    consoant >= "b" and consoant <= "d" or
    consoant >= "f" and consoant <= "h" or
    consoant >= "j" and consoant <= "n" or
    consoant >= "p" and consoant <= "t" or
    consoant >= "v" and consoant <= "z")
    #retorno do resultado da função
    return result 
    

#Função Principal onde fica o codigo principal
def main():
    #A Variável vai receber um caractere
    letra = input("Digite so as Consoantes: ")
    #Vai ser exibido para o usuário o resultado
    print(f"É Consoante? {consoante(letra)}")


if __name__ == "__main__":
    main()