# função auxiliar onde sera executado de preferencia uma tarefa especifica
def contador_frase(frase):
    # frase = frase.replace(" ","")
    # retorno da função retornando o resultado
    return len(frase)
# função principal onde se encontra o codigo principal
def main():
    # entrada de dados onde sera armazenada na variável o dado informado pelo usuário
    frase = input("Digite uma Frase: ").strip()
    # saida de dados onde sera exibido o resultado na tela do usuário
    print(f"A Frase Digitada Possui {contador_frase(frase)} caracteres")
# condição que verifica se o modulo/função é a principal se for sera chamada e executada
if __name__ == "__main__":
    # chamando a função main
    main()

