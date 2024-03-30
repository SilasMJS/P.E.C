# função auxiliar onde vai ser executado uma função especifica
def sexo(n):
    # retorno da função onde retorna o resultado
    return n == 1
# função principal onde fica o codigo principal
def main():
    # variável vai receber dado informado pelo usuário
    nome=input("Digite Seu Nome: ").strip()
    # variável vai receber dado informado pelo usuário
    n = int(input("Digite Seu Sexo:\n(1)-Masculino\n(2)-Feminino\n"))
    # condição na qual se for verdadeiro vai executado a linha de comando contida nela
    if sexo(n):
        # vai exibir na tela do usuário o resultado
        print(f"Ilmo Sr. {nome}")
    # caso a condição de cima seja falsa ira executar a linha de comando contida nela
    else:
        # vai exibir na tela do usuário o resultado
        print(f"Ilma Sra. {nome}")
# condição que verifica se a função/modulo é o principal se for vai chamar e executar a função main 
if __name__ == "__main__":
    # chamando a função main
    main()