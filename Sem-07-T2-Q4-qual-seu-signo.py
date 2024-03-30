# função auxiliar onde sera executado uma tarefa especifica 
def signo(dia,mes):
    # condição se for verdadeira ira executar o bloco contido nela
    if  (dia >= 21 and mes == 3) or (dia <= 19 and mes == 4):
        # retornando o resultado
        return "Áries"
    # se a condição acima não for verdadeira ira ser verificado se essa condição é se for vai ser executado o bloco contido nela
    elif  (dia >= 20 and mes == 4) or (dia <= 20 and mes == 5):
        # retornando o resultado
        return "Touro"
    # se a condição acima não for verdadeira ira ser verificado se essa condição é se for vai ser executado o bloco contido nela
    elif  (dia >= 21 and mes == 5) or (dia <= 21 and mes == 6):
        # retornando o resultado
        return "Gêmeos"
    # se a condição acima não for verdadeira ira ser verificado se essa condição é se for vai ser executado o bloco contido nela
    elif  (dia >= 22 and mes == 6) or (dia <= 22 and mes == 7):
        # retornando o resultado
        return "Câncer"
    # se a condição acima não for verdadeira ira ser verificado se essa condição é se for vai ser executado o bloco contido nela
    elif  (dia >= 23 and mes == 7) or (dia <= 22 and mes == 8):
        # retornando o resultado
        return "Leão"
    # se a condição acima não for verdadeira ira ser verificado se essa condição é se for vai ser executado o bloco contido nela
    elif  (dia >= 23 and mes == 8) or (dia <= 22 and mes == 9):
        # retornando o resultado
        return "Virgem"
    # se a condição acima não for verdadeira ira ser verificado se essa condição é se for vai ser executado o bloco contido nela
    elif  (dia >= 23 and mes == 9) or (dia <= 22 and mes == 10):
        # retornando o resultado
        return "Libra"
    # se a condição acima não for verdadeira ira ser verificado se essa condição é se for vai ser executado o bloco contido nela
    elif  (dia >= 23 and mes == 10) or (dia <= 21 and mes == 11):
        # retornando o resultado
        return "Escorpião"
    # se a condição acima não for verdadeira ira ser verificado se essa condição é se for vai ser executado o bloco contido nela
    elif  (dia >= 22 and mes == 11) or (dia <= 21 and mes == 12):
        # retornando o resultado
        return "Sagitário"
    # se a condição acima não for verdadeira ira ser verificado se essa condição é se for vai ser executado o bloco contido nela
    elif  (dia >= 22 and mes == 12) or (dia <= 19 and mes == 1):
        # retornando o resultado
        return "Capricórnio"
    # se a condição acima não for verdadeira ira ser verificado se essa condição é se for vai ser executado o bloco contido nela
    elif  (dia >= 20 and mes == 1) or (dia <= 18 and mes == 2):
        # retornando o resultado
        return "Aquário"
    # retornando o resultado
    return "Peixes"
# função principal onde o codigo principal fica contido
def main():
    # a variável vai receber e armazenar o dado informado pelo usuário
    dia = int(input("Digite o Dia do Seu Nascimento: "))
    # a variável vai receber e armazenar o dado informado pelo usuário
    mes = int(input("Digite o Mês do Seu Nascimento: "))
    # vai ser exibido na tela do usuário o resultado
    print(f"Você é do Signo de {signo(dia,mes)}")
# condição que verificar se a função/modulo é o principal se for vai chamar e executar a função main
if __name__ == "__main__":
    # chamando a função main
    main()