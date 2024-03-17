#Função Auxiliar vai processar os dados
def vogal(caract):
    result = (caract == 'a' or caract =='e' or 
        caract == 'i' or caract == 'o' or 
        caract == 'u' or caract == 'A' or 
        caract =='E' or caract == 'I' or 
        caract == 'O' or caract == 'U')
    return result

#Função Principal onde fica contido o codigo Principal
def main():
    #variavel vai receber caractere informado pelo usuário
    caract = input("Digite Uma Vogal: ").strip()
    #vai ser imprimido o resultado
    print(f"É Vogal? {vogal(caract)}")

if __name__ == "__main__":
    main()