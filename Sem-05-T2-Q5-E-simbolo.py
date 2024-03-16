#Função Auxiliar onde vai ocorrer o processamento de dados ou operações
def comparador(caract):
    result = (caract == "'" or caract == '"' or caract == "!" or
            caract == "@" or caract == "#" or caract == "$" or
            caract == "%" or caract == "¨" or caract == "&" or
            caract == "*" or caract == "(" or caract == ")" or
            caract == "-" or caract == "+" or caract == "=" or
            caract == "\\" or caract == "/" or caract == "?" or
            caract == "^" or caract == "~" or caract == ":" or
            caract == ";" or caract == "." or caract == "," or
            caract == "<" or caract == ">" or caract == "[" or
            caract == "]" or caract == "{" or caract == "}" or
            caract == "´" or caract == "`" or caract == "|" or
            caract == "_")
    return result
#Função Principal onde o codigo principal vai rodar
def main():
    #a variável vai receber o caractere informado pelo usuário
    caract = input().strip()
    #vai ser imprimido na tela o resultado para o usuário
    print(f"{comparador(caract)}")

if __name__ == '__main__':
    main()