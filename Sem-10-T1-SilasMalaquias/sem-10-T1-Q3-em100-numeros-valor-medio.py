# função auxiliar onde vai somar 100 numeros e tirar a media
def media_valores():
    soma = 0
    for x in range(1,101):
        # entrada de dados
        num = int(input())
        soma += num
    # processamento de dados
    media = soma/100
    return(f"{media:.2f}")
# função principal
def main():
    # saida de dados
    print(media_valores())
# condição que verifica se a função/modulo é o principal se for vai chamar a função main
if __name__ == "__main__":
    main()